# Como montar o dashboard · Vaz Power

Receita completa do dashboard semanal e mensal, escrita em 04/10/2026 pela sessão que montou
as semanas 11 a 17 e os fechamentos de agosto. Vale para qualquer sessão nova. Regras que não
mudam estão em `CLAUDE.md`; o estado vivo está em `ESTADO.md`. Este arquivo é o **como**.

---

## 1. Fontes de dado e como ler cada uma

### Google Ads (export CSV ou MCP)
- Quatro cortes, sempre no período da semana (segunda a domingo, fuso de Brisbane):
  **Campanhas · Por Dia · Dispositivos · Ação de Conversão**.
- CSV em formato BR: `.` de milhar, `,` decimal. Duas linhas de título antes do cabeçalho
  (cabeçalho na linha 3).
- **Ler sempre a linha `Total: Conta`. Nunca somar linhas.** O export traz subtotais
  (`Total: Campanhas`, `Total: Pesquisa`, `Total: Performance Max`) que, somados, dobram ou
  quadruplicam o número. Em agosto isso dobrou a base por 2,00x exato.
- **Campanha pausada no meio da semana some de `Total: Campanhas` e fica em `Total: Conta`.**
  Resíduo = Conta menos a soma das ativas. Mostrar o resíduo como linha própria, marcada
  "Pausada em dd/mm". Aconteceu com a LP Call (S12), PMax e LP Form (S16).
- No export **por Dia**, cada dia tem as próprias linhas de total. Pegar `Total: Conta` de
  cada dia; a soma dos dias tem de bater com o total da semana ao centavo.
- Colunas de presença: `Parcela impr rede de pesquisa`, `Parc impr perd (class.)`,
  `Parc impr perd (orç)`. **Comparar Search com Search** (`Total: Pesquisa`), nunca o total da
  conta entre semanas com e sem PMax: a PMax sai do denominador e o número da conta sobe
  sem ganho real.
- Ações de conversão: `Submit Form Volume` + `Book Form Submit (Site)` (+ `Lead Form LP
  Moving Quote` quando a LP existia) = formulários; `Click to call (Website)` + `Calls From
  Ads` = ligações. **A cesta mudou em 22/09**: o clique no telefone virou ação secundária e o
  Google recalcula o passado. Export novo de semana antiga vem com número menor que o
  dashboard publicado (S16: 25 virou 23). **Não republicar semana antiga por isso**; o mensal
  explica numa linha.
- Conversões com fração são crédito dividido do Google. Mostrar com duas casas na tabela.
- Com MCP: puxar os mesmos cortes e **reconciliar o total da conta contra a soma das
  campanhas** do mesmo jeito. O MCP não dispensa a conferência.

### Meta Ads
- Três cortes: **Campanhas · Dispositivos · Posicionamento** (mais Por Dia, se der).
- CSV em formato US. A única campanha ativa é `LEADS | CALL | BRISBANE | Asset Call`;
  `Resultados` = ligações. As outras linhas são campanhas inativas com zero.
- **Posicionamento precisa vir segmentado por "Posicionamento"**, não por "Dispositivo":
  na S16 veio o arquivo errado com o nome certo (idêntico byte a byte ao de dispositivos).
  Conferir as colunas `Plataforma` e `Posicionamento` antes de usar.
- **Export por plataforma (Facebook x Instagram) não resolve**: a campanha imprime só no
  Facebook mesmo com Instagram selecionado. Encerrado em 20/09.
- A soma por posicionamento pode divergir do total da campanha em uma impressão
  (arredondamento). Usar o total da campanha no rodapé e avisar na nota.
- Alcance não se soma entre dispositivos nem posicionamentos (mesma pessoa em mais de um).

### CRM Movermate (export CSV; a sessão de otimização tem acesso por navegador)
- Dois exports por semana: **Leads** e **Jobs**, filtrados por **Creation Date** (nunca por
  Job Date, que é a data da mudança). Botão `Export` na tela, com o filtro aplicado.
- **Lead ganho vira Job e sai de Leads.** "Agendamento" = ficha criada na semana que virou
  job na mesma semana. Reler a semana anterior dias depois dá o "contando até dd/mm".
- Status, no uso real do Rodrigo (27/09): `New` = sem contato; `Pending` = não atendeu;
  `Quoted` = orçamento enviado; `FollowUp` = em follow-up; `Lost` = não atendeu ou desistiu,
  **sem motivo registrado, por decisão dele** (parar de pedir Lost Reason). Em Jobs, o
  cancelamento tem motivo.
- **A origem é reescrita à mão quando a ficha é aberta**: Google Form (form), Incoming Call
  (ligação sem form), Facebook (social), mais Repeat Customer, Referral e contas. Logo:
  `Volume Calculator` e `Cost Estimator Form` **só aparecem enquanto a ficha está New**;
  depois viram "Google Forms". E **o CRM não separa Meta de Google** (nenhuma ficha
  "Facebook" em três semanas). O corte por origem é aproximado; o agregado de mídia não.
- Mídia = Google Forms + Incoming Call + Volume Calculator + Cost Estimator Form.
  Fora da mídia = Repeat Customer, Referral, contas (governo etc.).
- Mudança em duas pernas gera dois jobs para a mesma pessoa: contar pessoas (fone + e-mail)
  quando a pergunta for "quantos agendaram".
- Reconciliação esperada: Ads conta conversões, CRM conta pessoas; 37 formulários no Ads
  viraram 44 fichas de formulário no CRM (inclui orgânico). Diferença pequena é normal.
- **Os arquivos têm telefone e e-mail de cliente final. NUNCA entram no repositório**, que é
  público. Ler do upload, devolver só agregados. Nunca escrever nome de lead em lugar nenhum.

### Fuso (o erro mais repetido)
- Brisbane = UTC+10 o ano todo = **13h à frente do BRT**. O dia da conta fecha às ~11h BRT
  da mesma data. **O domingo fecha às 11h BRT de domingo**; export puxado à tarde de domingo
  traz a semana completa. Quem disser "fecha segunda" está errado.
- Sydney tem horário de verão (UTC+11 de 04/10/2026 a 04/04/2027); Brisbane não. O Carlos
  está em Sydney.
- A data do container é UTC e pode estar um dia à frente do Brasil. Conferir com `TZ=America/Sao_Paulo date` antes de escrever qualquer data.

---

## 2. Pipeline de montagem, na ordem

1. **Validar tudo em Python antes de escrever uma linha de HTML.** Totais contra `Total:
   Conta`; soma por campanha, por dia e por dispositivo batendo ao centavo; formulários +
   ligações = conversões; impressões e cliques batendo. Se algo não fecha, parar e achar o
   motivo (resíduo de campanha pausada é o mais comum).
2. Calcular os derivados: investimento total = Google + Meta; leads = conversões Google +
   resultados Meta; formulários (só Google); ligações (Google + Meta); **% de formulário sobre
   o total** (a medida combinada com o cliente); CPL geral; variação contra a semana anterior
   (investimento, leads, CPL, formulários, ligações, reservas); utilização por campanha =
   (gasto/7) / orçamento diário; presença Search x Search.
3. Escrever o `<body>` no scratchpad. Pegar o `<head>` do dashboard anterior com
   `src.split('<body>')[0]` e trocar só o `<title>` ("Vaz Power | Dashboard dd a dd/mm/aa -
   Semana N"). O CSS nunca muda; os SVGs e a faixa "Gestão contínua" são copiados do
   anterior. Pasta: `mes-dd-dd/` dentro do mês (`setembro-21-27`), ou `mes1dd-mes2dd/` na
   virada (`agosto31-setembro06`, logo `setembro28-outubro04`). Mensal: `mes-01-30/`.
4. **Bateria de validação do HTML**, tudo tem de passar: `<div>` e todas as tags (table,
   thead, tbody, tfoot, tr, td, th, span, ul, li, p, strong, svg, header, footer) abrindo e
   fechando em igual número (regex `<tag[\s>]` contra `</tag>`, porque `<strong style=…>`
   existe); termina em `</html>`; um único `<body>`; **zero travessão** (— – −); **zero
   emoji** (só ★ · • ▸); sem "barat"; sem "dinheiro"; `@media` intacto (7); título certo;
   nenhum resíduo da semana anterior no body; e as palavras vigiadas (ver seção 4).
5. Card no hub `index.html` (inserir antes do card da semana anterior, na seção do mês;
   outubro precisa de seção nova "Outubro 2026 · Relatórios Semanais" acima da de
   setembro); linha no `README.md`; linha na tabela "Histórico semanal" do `ESTADO.md`
   (5 colunas: Semana, Período, Investimento, Leads, CPL). Impressões do card = Google + Meta.
6. Screenshot com Playwright para conferir o render:
   `require('/opt/node22/lib/node_modules/playwright')`, `chromium.launch({ executablePath:
   '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' })`, viewport 1440x1100. Olhar o topo
   e o meio. Zero `pageerror`.
7. Commit na branch de trabalho. **Não publicar antes de o Fabricio validar o bloco "Ação da
   semana"**: mandar o print do topo e o texto do bloco; publicar só com o OK dele.
8. Publicar: `git fetch origin master && git merge origin/master --no-edit` (outras sessões
   escrevem no master toda hora), depois `git push origin <branch>:master`. Pages serve do
   master; o build leva ~1 min. Rejeição de push = alguém publicou antes; mesclar e repetir.
9. Depois de publicado: mensagem ao Vaz (seção 5), registrar no `ESTADO.md` o que foi dito,
   e fechar o ciclo quando o Fabricio avisar que enviou.

---

## 3. Estrutura do dashboard semanal (ordem fixa desde a S17)

1. **Header**: `★ Semana N do Novo Contrato` · período · "Gerado em dd/mm/aaaa".
2. **Visão Geral da Semana**, quatro cards nesta ordem: **Formulários sobre o total** (ov-card
   combined; valor "65%", sub "37 formulários em 57 leads / Semana anterior: 45%") ·
   **Total de Leads** (cpl-ov; sub "37 formulários + 20 ligações / 18 agendamentos no CRM") ·
   **Investimento Total** (google-ov) · **Custo por Lead** (meta-ov; sub com Google e Meta e
   a semana anterior). As classes de cor são as do `<head>` e não mudam.
3. **Análise & Ações da Semana**, quatro cards: **Diagnóstico** (4 a 5 `<li>`, o primeiro
   sempre com a medida combinada) · **Ação da semana** (um `<p>`; ver seção 4) ·
   **Monitorando** (4 `<li>`) · **Próximos passos** (4 `<li>`).
4. Faixa **Gestão contínua · toda semana** (copiar igual; o Fabricio decidiu mantê-la).
5. **Semana N contra Semana N-1**: tabela com Formulários sobre o total (primeira linha,
   badge "A medida combinada"), Formulários, Reservas pelo site, Ligações, Leads,
   Investimento total, CPL geral, Google · CPL, Meta · CPL. Variação em verde quando é bom,
   dourado quando é atenção. Nota "Como ler esta tabela".
6. **Do Lead ao Agendamento · o que o CRM mostra**: tabela por origem (fichas criadas na
   semana, viraram agendamento na semana, taxa; linha "Calculadora de volume e estimador"
   com badge "Ainda novas no CRM" quando for o caso; linha "Cliente recorrente e indicação"
   com badge "Fora da mídia"; rodapé "Leads de mídia") + tabela semana contra semana
   (fichas de mídia, agendamentos na própria semana [badge "A medida combinada"],
   agendamentos contando até dd/mm, investimento por agendamento nas duas bases, linhas
   por origem) + nota. Entrou na S17 por decisão do Fabricio e **é rotina**.
7. **Distribuição do Investimento** (barra Google x Meta com percentuais).
8. **Por Plataforma**: card Google (impressões, cliques, CTR, CPC, CPL médio, formulários
   com "Inclui N reservas", ligações) e card Meta (impressões, cliques, alcance, CPM, CPL,
   formulários "Campanha pausada", ligações).
9. **Os Dois Movimentos da Semana**: dois spotlight cards (`sg` dourado para Google, `sm`
   azul para Meta; ribbon com o rótulo do movimento, ex. "Primeira semana inteira", "Em
   leitura, faixa a faixa", "Público ajustado"). Pills: `forms` verde, `calls` dourado,
   `pmax` roxo. Não usar pill verde para número que piorou.
10. **Campanhas | período** (Google): Impressões, Cliques, CTR, Investimento, Conv., CPL,
    CPC; badges `badge-active` (Ativa / Nova / Melhor semana), `badge-limited` (Limitada por
    orçamento / Pausada em dd/mm / Em leitura), `badge-search`, `badge-pmax`, `badge-brand`.
    Rodapé `Total Google Ads` com os números de `Total: Conta`. Nota com onde foi o
    investimento e a frase das frações.
11. **Quanto do Mercado a Conta Está Capturando**: Aparece em, Perde por posição, Perde por
    orçamento, por campanha; rodapé "Search inteira" ou "Conta inteira" (dizer qual). Nota.
12. **De Onde Vieram os Leads do Google**: Formulários do site, Reservas pelo formulário do
    site, Formulário da landing page (se existir), Ligações; % do total. Nota.
13. **Onde o Meta Está Entregando** (posicionamento): Reels, Feed, Marketplace, com alcance,
    impressões, investimento, CPM, ligações, CPL. Nota.
14. **Desempenho por Dispositivo**: Google (celulares, computadores, tablets) e Meta (iPhone,
    Android, tablet). Uma nota para os dois.
15. **Investimento Diário · Implementado vs Praticado**: três cards (Google, Meta, Combinado)
    com implementado/dia, praticado/dia, utilização; tabela por campanha com "(era A$x)"
    quando o teto mudou; nota.
16. **Dia a dia** (Google): segunda a domingo com dia da semana, impressões, cliques,
    investimento, conversões; badges nos dias que importam (Melhor dia, Linha de corte,
    etc.); nota "A semana tem dois ritmos" quando houver mudança no meio. Os dias são de
    Brisbane.
17. **Footer** com o período e "Semana N do novo contrato".

Mensal: mesma linguagem visual do `agosto-01-31/`, com o comparativo junho/julho/agosto/
setembro (tabela "Meses fechados" do `ESTADO.md`), a série de % de formulário por mês (está
no `ESTADO.md`, bloco "Diagnóstico de composição"), as semanas do mês, e a seção do CRM
com o mês inteiro. Setembro: pasta `setembro-01-30/`, head do `agosto-01-31/`.

---

## 4. Regras de texto (além do `CLAUDE.md`)

- **Ação da semana = só o que saiu da rotina**, no nível de decisão e resultado. Teste: se
  aparece na faixa "Gestão contínua" (negativas, lances, criativos, medição), não entra.
  Rotina intensificada não é ação destacada. O bloco é proposto, o Fabricio valida.
- **Objetivo e resultado**, não lista de ajustes: "o objetivo da semana era X; resultado Y".
  Ajuste sem resultado para mostrar fica só no `ESTADO.md`.
- **Variação por decisão aparece como decisão**, nunca como performance: corte de agosto,
  filtro do Meta ("está sendo filtrado de propósito para deixar de trazer o lead que decide
  por preço"), foco local de 27/09, FRONT com público maior "para descobrir em qual faixa
  está o lead que fecha".
- **Palavras vigiadas, zero ocorrência no body**: teste, negativ (fora da faixa), lance,
  leilão, aprendiz, Advantage, tCPA, maximizar, cesta, idade, renda, geolocal, coorte,
  atribuição, denominador, amadurecida, piano, dinheiro, barat, travessão, emoji.
  Campanha é "frente de rotas", "campanha de busca", nunca a sigla interna no texto corrido
  (nas tabelas o nome curto vale: ROTAS, FRONT, SUPORTE, BRAND, MADRUGA).
- **Nenhuma projeção de semana parcial.** Em 01/10 a mensagem disse "ritmo perto de 35,
  dentro da meta" com 4 dias, e a segunda era fila sendo limpa; o cliente respondeu na hora
  "essa semana tá fraca". Número de semana só com a semana fechada.
- **Nada de faturamento, prejuízo, fee ou valor de job** no dashboard, na mensagem ou no
  repositório. O cliente citou faturamento e prejuízo no grupo em 01/10: fica fora.
- Operação do cliente aparece como fato e oportunidade, nunca como erro ("sete fichas ainda
  aguardam o primeiro contato: é o agendamento mais rápido disponível").
- Datas no texto são de Brisbane quando falam de dia da conta.

---

## 5. Mensagem ao Vaz

- Vai no **privado do Rodrigo e no grupo "Vaz Power AUS - Backup | Dashboards"** (Vaz, Victor,
  Fabricio). O Antonio Carlos **não** está nesse grupo e não entra por enquanto; assunto de
  tráfego e lead vai no grupo "Tráfego e Leads"; decisão de dono vai no privado.
- Forma que funcionou: link no topo; objetivo da semana numa frase; resultado em negrito
  com os três números da medida combinada (formulários, % do total, reservas); investimento
  e CPL; o que explica o custo, com motivo; a frente de rotas; o CRM ("dos leads de mídia,
  N viraram agendamento na própria semana, contra M"); Meta como decisão; próximo passo;
  "Qualquer coisa me chama". Sem jargão, sem campanha nomeada, sem projeção.
- Registrar no `ESTADO.md` o que foi dito (bloco "O que foi dito ao cliente"), para nenhuma
  sessão contradizer depois.

---

## 6. Ferramentas desta sessão de dashboards (04/10)

- A sessão original **não tinha MCP do Google Ads, nem do Meta, nem navegador**. Trabalhava
  com exports anexados. A sessão de otimização tem o MCP do Google Ads (só leitura,
  testado contra export em 01/10: bateu exato).
- Para a sessão nova: ligar os conectores em https://claude.ai/customize/connectors antes
  de abrir (conectores são lidos no início da sessão). Com MCP, puxar por campanha, por dia,
  por dispositivo e por ação de conversão, e reconciliar como na seção 1. O CRM segue por
  export ou por navegador.
