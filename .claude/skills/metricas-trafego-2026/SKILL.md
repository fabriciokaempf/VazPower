---
name: metricas-trafego-2026
description: Use para montar/atualizar o DASHBOARD SEMANAL de trafego pago (Google Ads + Meta Ads) e os COMPARATIVOS entre periodos do cliente (ex.: Vaz Power). Cobre ler CSV de GADS/META, calcular metricas (investimento, CPL, CPM, CPC, leads = forms + ligacoes, CPL geral), gerar o HTML do dashboard no modelo do projeto, montar comparativo (semana vs semana + acumulado do mes), atualizar o hub/README e publicar via GitHub Pages, alem da planilha comercial para o cliente preencher. Gatilhos: "dashboard", "relatorio semanal", "comparativo", "metricas de trafego", "GADS/META csv", "CPL/CPM", "planilha do Vaz/cliente". NAO usar para negativacao de palavras-chave (use google-ads-2026).
license: Kaempf Business — uso interno
---

# Metricas de Trafego 2026 — Dashboards Semanais & Comparativos

Playbook da Kaempf Business para os relatorios de trafego pago (Google + Meta) do
Vaz Power Removals & Storage (Brisbane, AU). Saida = dashboards HTML publicados no
GitHub Pages + planilha comercial para o cliente preencher.

## Insumos
- `GADS - <cliente> <periodo>.csv` (Google Ads — export "Relatorio de campanha").
- `META - <cliente> <periodo>.csv` (Meta Ads — export por campanha).
- Conferir o intervalo de datas no cabecalho do CSV (o GADS as vezes vem com 1 dia a
  mais — avise o cliente se Google e Meta nao baterem no periodo).

## Gotchas de parsing (decorar)
- **GADS = formato BR**: virgula decimal e ponto de milhar ("1.283,39"). Normalize:
  remova ".", troque "," por "." antes de converter.
- **META = formato US**: ponto decimal ("368.85").
- Use os totais do GADS na linha **"Total: Campanhas"**. No META, **some** as campanhas
  ativas (com gasto > 0); ignore as `inactive`.

## Definicoes de metrica (manter consistencia entre semanas)
- **Google conversoes / CPL**: use "Conversoes" e "Custo / conv." da linha de total.
- **Google forms/ligacoes**: "Enviar formulario de lead" / "Ligacoes telefonicas".
- **Meta resultados** = forms (`...fb_pixel_lead`) + ligacoes (`...click_to_call...`).
  Remarketing/reach NAO entra como resultado (CPL "--").
- **Meta CPL** = (gasto forms + gasto calls) / resultados — **exclui** o gasto de RMKT.
- **Meta CPM medio** = media simples dos CPMs das campanhas (nao ponderada).
- **Total de Leads (overview)** = (Google forms + Google ligacoes) + Meta resultados.
- **CPL geral** = investimento total / total de leads.
- **Distribuicao de investimento**: % de cada plataforma no total.

## Dashboard (HTML)
- Modelo de referencia: `junho-01-07/index.html` (mesmo `<head>`/CSS para todos).
- Tecnica: reaproveitar o `<head>` ate `</head>` do modelo + corpo novo (mesclar via
  script), mudando so o `<title>`. Validar: balanco de `<div>`, 5 `<table>`, termina
  em `</html>`.
- Pasta por periodo: `junho-08-14/`, `junho-15-21/` etc. (padrao `mes-DD-DD`).
- Secoes: overview, **analise & acoes** (ver abaixo), distribuicao, por plataforma,
  destaques (melhor CPL), tabelas de campanha, investimento diario (implementado vs
  praticado) e rastreamento UTM.
- **NAO** incluir a secao "Resultado Comercial" (funil/pipeline que dependia do cliente
  reportar) — foi removida em jul/2026 porque virava um "pendente" e um entrave. O CSS
  antigo (`.comercial-section` etc.) segue no `<head>` so porque o remarketing reaproveita
  a classe no funil estrategico; nao renderizar bloco comercial pendente nos dashboards.

## Secao "Analise & Acoes da Semana"
- Fica logo apos a overview (antes da barra de investimento). Traduz numero em valor:
  mostra ao cliente a gestao ativa da conta.
- 4 cards (grid 2x2, CSS injetado antes de `</style>` — classes `.analysis-grid`,
  `.an-card` + `.an-diag/.an-action/.an-watch/.an-next`, borda colorida a esquerda) +
  1 faixa `.mgmt-strip` (chips) logo abaixo do grid:
  1. **Diagnostico** (azul) — o que os dados da semana mostraram.
  2. **Acao da semana** (verde, card em destaque) — a decisao ESPECIFICA daquela semana
     em resposta ao diagnostico. Texto em `<p>`, 1 paragrafo narrativo (nao bullets).
  3. **Monitorando** (dourado) — o que esta sendo vigiado.
  4. **Proximos passos** (roxo) — o que vem.
  5. **Gestao continua** (faixa de chips, `.mgmt-strip`) — o trabalho recorrente que roda
     TODA semana (monitoramento diario, refino de negativas, ajuste de lances, gestao de
     criativos, gestao do remarketing). E fixo e igual em todas as semanas.
- **POR QUE separar:** as acoes recorrentes se repetiam toda semana e viravam texto
  padrao (o cliente le como copia-e-cola, perde credibilidade). Entao a rotina vai na
  faixa "Gestao continua" (assumida como rotina) e o card "Acao da semana" carrega so o
  movimento especifico daquela semana — muda a cada relatorio e conta a historia.
- **CRITICO:** a "Acao da semana" e uma acao que o gestor EXECUTOU de fato — nunca
  inventar (lembrar do episodio "reset de aprendizado" que ficou ruim perante o cliente).
  Fluxo: eu proponho um rascunho com base nos dados/estrategia e o gestor valida/ajusta
  antes de publicar. Diagnostico/Monitorando/Proximos derivam dos numeros (sem risco).
- **Tom premium:** evitar "barato/barata" e "lixo" no texto voltado ao cliente; usar
  "eficiencia de CPL / custo por lead / de baixo valor".
- **SEM TRAVESSAO:** nao usar travessao (em-dash) em nenhum lugar dos dashboards. Trocar
  por "·" (separador, no padrao da marca), ":" ou virgula; e usar hifen "-" para faixas
  (datas, S1-S4) e sinais negativos ("-19%"). Nada de em-dash nem "&mdash;".

## Comparativo
- Estrutura: semana atual vs anterior (deltas %), evolucao S1->S2->S3 e **acumulado do
  mes** (MTD = soma das semanas). Use chips de variacao (verde = bom, vermelho = ruim,
  cinza = neutro). CSS extra de comparativo fica injetado antes de `</style>`.

## Hub e README
- `index.html` (hub): card por periodo (mais recente primeiro) + card de comparativo.
- Atualizar `README.md` com os links.

## Planilha comercial (cliente preenche)
- Gerar **Google Sheet nativo** no Drive (pasta "Planilhas - Comercial") via
  `create_file` com `contentMimeType=text/csv` (converte sozinho).
- **CRITICO (locale pt-BR)**: formulas com varios argumentos usam **;** e nao "," —
  `=IFERROR(C18/B18;"")`. Com virgula da #ERROR!. `SUM(B:B)` (sem separador) funciona.
- Pre-preencher "Leads Gerados" com o total da semana; so as celulas (*) ficam pro Vaz.
- Tambem entregar versao .xlsx (openpyxl) com celulas amarelas + formulas, se pedirem.

## Publicacao (GitHub Pages)
- Commitar na branch de trabalho, abrir PR e fazer merge na `master` (Pages serve da
  master). Build "pages build and deployment" leva ~1 min.
- **ATENCAO a caixa da URL**: o repo e `VazPower` (V e P maiusculos). O Pages diferencia
  maiusculas no caminho -> `https://fabriciokaempf.github.io/VazPower/junho-08-14/`.
  Minusculo da "There isn't a GitHub Pages site here".

## Boas praticas
- Validar todos os numeros com um script (parsear CSV + conferir contra o esperado)
  antes de escrever o HTML.
- Sempre cruzar com a planilha comercial do cliente quando disponivel (qualidade da
  lead) para a leitura/recomendacao da semana.
