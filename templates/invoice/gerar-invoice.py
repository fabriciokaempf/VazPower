#!/usr/bin/env python3
"""
Gera a invoice mensal em PDF a partir do template.

Os dados fixos (nome, documento, e-mail, dados de pagamento, valor) NAO ficam
no repositorio, porque ele e publico. Eles vem de um arquivo local, ignorado
pelo git: `dados.local.json` (use `dados.exemplo.json` como base).

Uso:
    python3 gerar-invoice.py --numero INV-2026-09-001 \
                             --periodo "September 2026" \
                             --data "1 September 2026"

Se --data for omitida, usa a data de hoje. O vencimento acompanha a emissao
("due on receipt"), que e o padrao usado ate aqui.

Saida: "Invoice #<MES> - <Cliente>.pdf" na pasta atual.
"""

import argparse
import json
import os
import subprocess
import sys
from datetime import date

AQUI = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(AQUI, "invoice-template.html")
DADOS = os.path.join(AQUI, "dados.local.json")

MESES_PT = {
    "January": "JANEIRO", "February": "FEVEREIRO", "March": "MARCO",
    "April": "ABRIL", "May": "MAIO", "June": "JUNHO",
    "July": "JULHO", "August": "AGOSTO", "September": "SETEMBRO",
    "October": "OUTUBRO", "November": "NOVEMBRO", "December": "DEZEMBRO",
}


def carregar_dados():
    if not os.path.exists(DADOS):
        sys.exit(
            f"Falta o arquivo {DADOS}.\n"
            "Copie dados.exemplo.json para dados.local.json e preencha com os "
            "dados reais. Esse arquivo e ignorado pelo git de proposito."
        )
    with open(DADOS, encoding="utf-8") as f:
        return json.load(f)


def montar_html(dados, numero, periodo, data_emissao):
    with open(TEMPLATE, encoding="utf-8") as f:
        html = f.read()

    valores = dict(dados)
    valores.update({
        "INVOICE_NO": numero,
        "ISSUE_DATE": data_emissao,
        "DUE_DATE": data_emissao,          # due on receipt
        "SERVICE_PERIOD": periodo,
    })

    for chave, valor in valores.items():
        html = html.replace("{{" + chave + "}}", str(valor))

    faltando = [p for p in ("{{" in html and html.split("{{")[1:] or [])]
    if faltando:
        restantes = sorted({p.split("}}")[0] for p in faltando})
        sys.exit(f"Placeholders sem valor: {restantes}")

    return html


def gerar_pdf(html, saida):
    tmp_html = os.path.join(os.getcwd(), "_invoice_tmp.html")
    with open(tmp_html, "w", encoding="utf-8") as f:
        f.write(html)

    script = f"""
const {{ chromium }} = require('playwright');
(async () => {{
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://{tmp_html}', {{ waitUntil: 'networkidle' }});
  await p.pdf({{ path: {json.dumps(saida)}, format: 'A4', printBackground: true }});
  await b.close();
}})();
"""
    tmp_js = os.path.join(os.getcwd(), "_invoice_tmp.cjs")
    with open(tmp_js, "w", encoding="utf-8") as f:
        f.write(script)

    try:
        subprocess.run(["node", tmp_js], check=True)
    finally:
        for t in (tmp_html, tmp_js):
            if os.path.exists(t):
                os.remove(t)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--numero", required=True, help="ex.: INV-2026-09-001")
    ap.add_argument("--periodo", required=True, help='ex.: "September 2026"')
    ap.add_argument("--data", help='ex.: "1 September 2026" (padrao: hoje)')
    ap.add_argument("--saida", help="caminho do PDF (padrao: nome no padrao da pasta)")
    args = ap.parse_args()

    dados = carregar_dados()
    data_emissao = args.data or date.today().strftime("%-d %B %Y")

    mes_en = args.periodo.split()[0]
    mes_pt = MESES_PT.get(mes_en, mes_en.upper())
    cliente = dados.get("TO_NAME", "Cliente").replace(" Pty Ltd", "")
    saida = args.saida or f"Invoice #{mes_pt} - {cliente}.pdf"

    html = montar_html(dados, args.numero, args.periodo, data_emissao)
    gerar_pdf(html, os.path.abspath(saida))
    print(f"PDF gerado: {saida}")


if __name__ == "__main__":
    main()
