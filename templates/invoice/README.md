# Template de Invoice

Modelo da invoice mensal de gestão de tráfego pago, no layout usado desde maio/2026.

## Atenção: este repositório é público

O repo `VazPower` é público (é ele que serve o GitHub Pages). Por isso o template
guarda apenas a **estrutura**, com placeholders no lugar dos dados sensíveis:
documento, e-mail de recebimento, dados de pagamento e valor.

Os dados reais ficam em `dados.local.json`, que está no `.gitignore` e **nunca
deve ser commitado**.

## Como gerar

1. Na primeira vez, crie o arquivo de dados a partir do exemplo:

   ```
   cp dados.exemplo.json dados.local.json
   ```

   Preencha com os dados reais (documento, e-mails, endereço, valor).

2. Gere a invoice do mês:

   ```
   python3 gerar-invoice.py --numero INV-2026-09-001 \
                            --periodo "September 2026" \
                            --data "1 September 2026"
   ```

   Saída: `Invoice #SETEMBRO - Vaz Power.pdf`

O `--data` é opcional (usa a data de hoje). O vencimento acompanha a emissão,
porque a condição é *due on receipt*.

**PDF:** usa o `playwright` se ele estiver disponível para o Node. Se não estiver,
cai automaticamente no Chrome ou no Edge em modo headless, que já existem no
Windows. Não precisa instalar nada.

## Serviço entregue sem cobrança

Trabalho fora do escopo mensal, entregue sem custo, pode aparecer como linha
própria: o valor de mercado sai riscado, com o selo "no charge", e nos totais
entra como valor cheio mais crédito de 100%. O total a pagar não muda.

```
python gerar-invoice.py --numero INV-2026-09-001 \
                        --periodo "September 2026" \
                        --extra-titulo "Conversion Tracking Rebuild (Website)" \
                        --extra-desc "Audit, GTM build and live validation." \
                        --extra-periodo "August 2026" \
                        --extra-qtd "6.7 hrs" \
                        --extra-valor "A\$800.00"
```

Os rótulos dos totais são configuráveis com `--extra-rotulo` e
`--extra-rotulo-credito` (padrão: *Additional services delivered* e
*Partnership credit (100%)*).

**Por que na invoice e não só na mensagem:** a invoice é o documento que o
cliente arquiva e revê. Ali o número é lido como registro contábil, e não como
quem está pedindo reconhecimento. Também deixa a âncora pronta para quando o
escopo aumentar. Na mensagem, uma frase apontando para o documento basta.

Usado pela primeira vez em `INV-2026-09-001` (reconstrução do rastreamento
de conversão do site, executada de 23 a 26/08/2026).

## Convenções em uso

- **Numeração:** `INV-AAAA-MM-001`, onde `MM` é o mês de emissão.
- **Faturamento antecipado:** a invoice de agosto cobre o serviço de agosto.
  (A primeira, de junho/2026, cobriu maio; a partir de julho passou a ser antecipada.)
- **GST 0%**, por ser fornecedor no exterior (GSTR 2003/4).
- **Nome do arquivo:** `Invoice #MES - Cliente.pdf`, para casar com a pasta local
  de invoices do Fabricio.

## Placeholders disponíveis

| Placeholder | Conteúdo |
|---|---|
| `{{INVOICE_NO}}` | Número da invoice |
| `{{ISSUE_DATE}}` / `{{DUE_DATE}}` | Datas de emissão e vencimento |
| `{{SERVICE_PERIOD}}` | Período do serviço (ex.: August 2026) |
| `{{FROM_NAME}}` / `{{FROM_DOC}}` / `{{FROM_COUNTRY}}` / `{{FROM_EMAIL}}` | Prestador |
| `{{TO_NAME}}` / `{{TO_ABN}}` / `{{TO_ADDRESS}}` / `{{TO_CITY}}` / `{{TO_EMAIL}}` | Cliente |
| `{{AMOUNT}}` | Valor (aparece no item, subtotal e total) |
| `{{PAYMENT_METHOD}}` / `{{PAYMENT_EMAIL}}` / `{{CURRENCY}}` | Pagamento |
| `{{EXTRA_ROWS}}` / `{{EXTRA_TOTALS}}` | Linha e totais do serviço sem cobrança (o script preenche com vazio quando não há) |
