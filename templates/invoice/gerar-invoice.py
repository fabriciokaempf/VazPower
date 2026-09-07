#!/usr/bin/env python3
"""
Gera a invoice mensal em PDF a partir do template.

Os dados fixos (nome, documento, e-mail, dados de pagamento, valor) NAO ficam
no repositorio, porque ele e publico. Eles vem de um arquivo local, ignorado
pelo git: `dados.local.json` (use `dados.exemplo.json` como base).

Uso:
    python gerar-invoice.py --numero INV-2026-09-001 \
                            --periodo "September 2026" \
                            --data "1 September 2026"

Item entregue sem cobranca (opcional). Aparece como linha propria, com o valor
de mercado riscado, e como credito de 100% nos totais, de modo que o total a
pagar nao muda:

    python gerar-invoice.py --numero INV-2026-09-001 \
                            --periodo "September 2026" \
                            --extra-titulo "Conversion Tracking Rebuild (Website)" \
                            --extra-desc "Auditoria, build no GTM e validacao." \
                            --extra-periodo "August 2026" \
                            --extra-qtd "6.7 hrs" \
                            --extra-valor "A$800.00"

Se --data for omitida, usa a data de hoje. O vencimento acompanha a emissao
("due on receipt"), que e o padrao usado ate aqui.

PDF: usa o playwright se estiver disponivel; senao cai no Chrome ou Edge em
modo headless, que ja existem no Windows.

Saida: "Invoice #<MES> - <Cliente>.pdf" na pasta atual.
"""

import argparse
import html
import json
import os
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

AQUI = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(AQUI, "invoice-template.html")
DADOS = os.path.join(AQUI, "dados.local.json")

# Nomes de mes fixos: a invoice e em ingles e o locale da maquina pode nao ser.
MESES_EN = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]

MESES_PT = {
    "January": "JANEIRO", "February": "FEVEREIRO", "March": "MARCO",
    "April": "ABRIL", "May": "MAIO", "June": "JUNHO",
    "July": "JULHO", "August": "AGOSTO", "September": "SETEMBRO",
    "October": "OUTUBRO", "November": "NOVEMBRO", "December": "DEZEMBRO",
}

NAVEGADORES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]


def carregar_dados():
    if not os.path.exists(DADOS):
        sys.exit(
            f"Falta o arquivo {DADOS}.\n"
            "Copie dados.exemplo.json para dados.local.json e preencha com os "
            "dados reais. Esse arquivo e ignorado pelo git de proposito."
        )
    with open(DADOS, encoding="utf-8") as f:
        return json.load(f)


def montar_extra(args):
    """Monta a linha e os totais do item entregue sem cobranca."""
    if not args.extra_titulo:
        return "", ""

    linha = f"""          <tr class="gift">
            <td>
              <div class="desc-title">{html.escape(args.extra_titulo)}<span class="tag-gift">Included</span></div>
              <div class="desc-sub">{html.escape(args.extra_desc or "")}</div>
            </td>
            <td>{html.escape(args.extra_periodo or "")}</td>
            <td>{html.escape(args.extra_qtd or "")}</td>
            <td class="r amount struck">{html.escape(args.extra_valor)}<span class="nocharge">No charge</span></td>
          </tr>"""

    valor = html.escape(args.extra_valor)
    credito = valor.replace("A$", "-A$", 1)
    totais = f"""        <div class="trow"><div class="tlabel">{html.escape(args.extra_rotulo)}</div><div class="tval">{valor}</div></div>
        <div class="trow"><div class="tlabel">{html.escape(args.extra_rotulo_credito)}</div><div class="tval">{credito}</div></div>"""

    return linha, totais


def montar_html(dados, numero, periodo, data_emissao, extra_linha, extra_totais):
    with open(TEMPLATE, encoding="utf-8") as f:
        pagina = f.read()

    valores = dict(dados)

    # FROM_DOC e opcional. Vazio, some do bloco "From" e do rodape sem deixar
    # separador solto. O que sustenta o GST 0% e ser fornecedor no exterior,
    # nao o documento brasileiro, que nao tem efeito fiscal na Australia.
    doc = (dados.get("FROM_DOC") or "").strip()
    valores["FROM_DOC_ROW"] = f'        <div class="row">{html.escape(doc)}</div>' if doc else ""
    valores["FROM_DOC_INLINE"] = f" - {html.escape(doc)}" if doc else ""

    valores.update({
        "INVOICE_NO": numero,
        "ISSUE_DATE": data_emissao,
        "DUE_DATE": data_emissao,          # due on receipt
        "SERVICE_PERIOD": periodo,
        "EXTRA_ROWS": extra_linha,
        "EXTRA_TOTALS": extra_totais,
    })

    for chave, valor in valores.items():
        pagina = pagina.replace("{{" + chave + "}}", str(valor))

    if "{{" in pagina:
        restantes = sorted({p.split("}}")[0] for p in pagina.split("{{")[1:]})
        sys.exit(f"Placeholders sem valor: {restantes}")

    return pagina


def achar_navegador():
    for nome in ("chrome", "msedge", "chromium"):
        caminho = shutil.which(nome)
        if caminho:
            return caminho
    for caminho in NAVEGADORES:
        if os.path.exists(caminho):
            return caminho
    return None


def gerar_pdf(pagina, saida):
    tmp_html = os.path.join(os.getcwd(), "_invoice_tmp.html")
    with open(tmp_html, "w", encoding="utf-8") as f:
        f.write(pagina)

    url = Path(tmp_html).as_uri()
    tmp_js = os.path.join(os.getcwd(), "_invoice_tmp.cjs")
    temporarios = [tmp_html]

    try:
        tem_playwright = subprocess.run(
            ["node", "-e", "require('playwright')"],
            capture_output=True,
        ).returncode == 0

        if tem_playwright:
            script = f"""
const {{ chromium }} = require('playwright');
(async () => {{
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto({json.dumps(url)}, {{ waitUntil: 'networkidle' }});
  await p.pdf({{ path: {json.dumps(saida)}, format: 'A4', printBackground: true }});
  await b.close();
}})();
"""
            with open(tmp_js, "w", encoding="utf-8") as f:
                f.write(script)
            temporarios.append(tmp_js)
            subprocess.run(["node", tmp_js], check=True)
            return

        navegador = achar_navegador()
        if not navegador:
            sys.exit(
                "Nao encontrei playwright nem Chrome/Edge para gerar o PDF.\n"
                "Instale o playwright (npm i playwright) ou use um dos navegadores."
            )

        subprocess.run([
            navegador,
            "--headless",
            "--disable-gpu",
            "--no-pdf-header-footer",
            "--virtual-time-budget=4000",
            f"--print-to-pdf={saida}",
            url,
        ], check=True, capture_output=True)

    finally:
        for t in temporarios:
            if os.path.exists(t):
                os.remove(t)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--numero", required=True, help="ex.: INV-2026-09-001")
    ap.add_argument("--periodo", required=True, help='ex.: "September 2026"')
    ap.add_argument("--data", help='ex.: "1 September 2026" (padrao: hoje)')
    ap.add_argument("--saida", help="caminho do PDF (padrao: nome no padrao da pasta)")

    ap.add_argument("--extra-titulo", help="titulo do item entregue sem cobranca")
    ap.add_argument("--extra-desc", help="descricao do item")
    ap.add_argument("--extra-periodo", help='periodo do item, ex.: "August 2026"')
    ap.add_argument("--extra-qtd", help='quantidade, ex.: "6.7 hrs"')
    ap.add_argument("--extra-valor", help='valor de mercado, ex.: "A$800.00"')
    ap.add_argument("--extra-rotulo", default="Additional services delivered",
                    help="rotulo da linha de valor nos totais")
    ap.add_argument("--extra-rotulo-credito", default="Partnership credit (100%)",
                    help="rotulo da linha de credito nos totais")

    args = ap.parse_args()

    if args.extra_titulo and not args.extra_valor:
        ap.error("--extra-titulo exige --extra-valor")

    dados = carregar_dados()

    if args.data:
        data_emissao = args.data
    else:
        hoje = date.today()
        data_emissao = f"{hoje.day} {MESES_EN[hoje.month - 1]} {hoje.year}"

    mes_en = args.periodo.split()[0]
    mes_pt = MESES_PT.get(mes_en, mes_en.upper())
    cliente = dados.get("TO_NAME", "Cliente").replace(" Pty Ltd", "")
    saida = args.saida or f"Invoice #{mes_pt} - {cliente}.pdf"

    extra_linha, extra_totais = montar_extra(args)
    pagina = montar_html(dados, args.numero, args.periodo, data_emissao,
                         extra_linha, extra_totais)
    gerar_pdf(pagina, os.path.abspath(saida))
    print(f"PDF gerado: {saida}")


if __name__ == "__main__":
    main()
