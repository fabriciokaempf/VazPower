# Estado da operação · Vaz Power

Resumo vivo do projeto, para retomar o contexto em qualquer sessão nova.
Atualizado em **27/08/2026** (queda de entrega em diagnóstico; tracking do /book/ no ar).

---

## 0. ESTADO ATUAL (retomar daqui)

### ATUALIZAÇÃO DE 27/08, ESCRITA PELA SESSÃO DE OTIMIZAÇÃO · LEIA ANTES DE TUDO

Quatro coisas aconteceram entre 24 e 27/08 que mudam o que está escrito abaixo nesta
mesma seção. A escada de retomada foi executada em parte e **mesmo assim o gasto
despencou**. Não é falta de orçamento.

#### 1. QUEDA DE ENTREGA: a conta caiu para ~A$70/dia

| Dia | Custo total |
|---|---|
| 24/08 | A$580,10 |
| 25/08 | A$270,98 |
| 26/08 | A$74,10 |
| 27/08 | A$70,70 |

A projeção da escada para este ponto era **A$584/dia**. O realizado foi A$70,70, ou seja,
**12% do previsto**. E o orçamento estava lá: SUPORTE foi para A$80,98 (a escada pedia
A$71), acima do plano.

**Orçamento não é o gargalo.** Repetir a escada não resolve.

#### 2. AS DUAS HIPÓTESES E O TESTE QUE AS SEPARA

Já descartado: não é a mudança de tracking (a queda começou antes), não é anúncio
reprovado (sete "Qualificada", zero reprovação, os dois "Em análise" são resíduo de grupo
removido na BRAND), não é campanha parada (a FRONT teve impressão, logo está apta).

- **A)** Sequela do site fora do ar de 20 a 25/08. O PHP do vazpower.com.au ficou em erro
  fatal, mascarado pelo cache do WP Rocket. Página de destino quebrada derruba Ad Rank sem
  gerar reprovação formal. O site voltou em 26/08
- **B)** O teto de CPA de A$60 apertou demais. A regra é de 30/07, quando o problema era o
  oposto: CPA A$109 com volume alto

**O teste é de graça: se for o site, a entrega volta sozinha. Se for o teto, fica parada.**

> **VEREDITO DE 31/08, lido pela sessão do dashboard: cenário B. A ENTREGA NÃO VOLTOU.**
>
> **Fuso, para ler certo:** a conta roda em **Brisbane, 13h à frente do BRT**. O dia da
> conta **fecha às ~11h da manhã (BRT) da mesma data**. Puxando depois disso, aquele dia
> está completo. É por isso que dá para fechar o mês australiano ainda no dia 31 aqui.
> Os dias abaixo são todos completos.
>
> - Média de dia útil ANTES do site cair (10 a 19/08): **712**
> - Média de dia útil DEPOIS de voltar (26, 27, 28 e 31/08): **252**, ou **35% do
>   patamar**, com o site no ar há seis dias
> - Segunda contra segunda: 680 (10/08), 1.574 (17/08), **348 (31/08)**. A última
>   segunda entregou **metade da segunda mais fraca** do período
>
> Seis dias com o site no ar e a entrega parada em um terço: **não é sequela do site.**
> Aponta para o **teto de CPA de A$60**, e a ação de 01/09 é subir o tCPA. Fecha com o
> que a FRONT já mostrava: "Limitada pela meta de lance" gastando A$0,00.
>
> **A confirmar na conta antes de agir:** parcela de impressões perdida por classificação
> e o status atual de cada campanha. Aqui só tenho as impressões diárias.
>
> **A conferir também:** a janela "site fora do ar de 20 a 25/08" está em data brasileira
> ou australiana? Com 13h de diferença ela pode deslocar um dia, o que muda quantos dias
> de cada semana foram atingidos.

**Ponto de observação: a FRONT.** Carrega A$287,98/dia, 34% do orçamento, status literal
"Limitada pela meta de lance", tCPA A$65, gastando A$0,00. Isso confirma o que a seção 4
já suspeitava: é tCPA, não orçamento.

#### 3. REGRA ATIVA ATÉ 31/08: CONGELAR O GOOGLE, NÃO A META

**Google congelado.** Nem orçamento, nem alvo de CPA, nem correspondência. Qualquer
mudança destrói o teste.

**A Meta segue a escada normalmente.** O diagnóstico é de entrega do Google e a Meta não
tem relação com ele. Congelar a Meta não produz informação e custa lead: Ligações está no
melhor CPL da operação e travada no teto.

Veredito marcado para **31/08**. As ações ficam para **01/09**, junto do fechado de agosto.

#### 4. O /book/ PASSOU A SER MEDIDO (26/08, container Versão 21)

O formulário de reserva do site nunca teve ação própria no Google Ads. Agora tem.

| Item | Valor |
|---|---|
| Ação | `Book Form Submit (Site)` |
| Código do tipo de conversão | 7735227297 |
| Valor | A$100 |
| Otimização | Principal |

**O achado que valeu o trabalho:** o `/book/` **redireciona para
`/cost-estimator-thank-you/`**, onde a `Quote Form Conversion` dispara por URL. Ou seja,
ele nunca foi invisível, era contado com o nome errado. Sem correção, a ação nova teria
criado **contagem dupla** em todo envio. Resolvido com exceção no GTM e validado em dois
testes reais.

No primeiro dia registrou **2 reservas reais**, uma pela BRAND e uma pela SUPORTE. As 6
campanhas ativas usam a meta "Enviar formulários de lead", então a conversão alcança o
lance de todas.

#### 5. A QUEDA DA SEMANA 13 NÃO É DECISÃO DO CLIENTE

O `CLAUDE.md` deste repositório está correto e atualizado desde 23/08: ele diz que variação
por decisão do cliente aparece como decisão, "tanto na queda quanto na retomada". A regra é
condicional e continua valendo.

**O ponto é que a queda da S13 não se encaixa nela.** Ela não foi pedida pelo cliente. É
queda de entrega sem causa confirmada, com diagnóstico em curso.

E tem um agravante de comunicação: em 23/08 o Fabricio escreveu ao Rodrigo *"essa foi a
última semana do teto: já começamos a retomada gradual do investimento"*. Ele leu que ia
subir e vai ver caindo. Apresentar como decisão dele contradiz a mensagem de dois dias
antes.

**O dashboard da S13 precisa encarar a queda de frente, com a causa determinada em 31/08.**

#### 5b. ONDE A ESCADA DA META PAROU

Meta Ligações está em **A$80,98/dia**, rodando a **102% do orçamento**. A escada previa
A$52,98 -> A$66 -> A$82 -> A$95. Ou seja, ela pegou o degrau de 27/08 e ainda não pegou o
de 30/08.

**Como está batendo no teto, subir para A$95 tende a render volume direto.** E a Meta não
está congelada: o congelamento vale só para o Google.

#### 6. CUIDADOS DE NÚMERO NO RELATÓRIO

- **Não escrever "a conta usa 8% do orçamento".** O cálculo inclui a MADRUGA, que roda das
  00h às 03h somente em computador e nunca teve como gastar os A$128,98/dia dela. O
  orçamento realmente alcançável é **~A$720 a A$730**, não A$846,98
- **Não vender o CPA de ~A$18** dos dias 26 e 27. É amostra de dois dias com a conta em
  fração da verba. Se sobreviver ao retorno do volume, aí vira número
- A Semana 13 não fecha conclusão sozinha: site fora do ar até 25/08, escada de orçamento
  a partir de 24/08, PMax recalibrando desde 23/08, mudança de tracking em 26/08 e a queda
  de entrega ainda sem causa

#### 7. RESPOSTAS ÀS PENDÊNCIAS QUE ESTE ARQUIVO PERGUNTAVA

- **"A LP Call foi mesmo encerrada?"** Sim. Pausada em 17/08. Perdeu o teste A/B para a de
  formulário: A$971,03 e 12 conversões (CPA A$80,92) contra A$686,60 e 3 conversões
  (CPA A$228,87). O resíduo de A$79,67 é consistente com pausa no meio da semana
- **"O incremento de negativas de 17/08 foi aplicado?"** **Não confirmado.** Houve rodadas
  de negativas depois disso, mas não dá para afirmar que foi esta lista de 45. Verificar
  antes de dar como feito

#### 8. ONDE MORA O RESTO DO CONTEXTO

A frente de otimização trabalha em `Jobs 2026/Vaz Power/`, que tem memória de projeto
própria (17 arquivos) e um `CLAUDE.md` reescrito em 27/08. **Aquela memória não é visível
aqui**, e esta não é visível lá. Este arquivo é o canal entre as duas.

Documento mais detalhado do tracking: `Jobs 2026/Vaz Power/Plano de Tracking - Vaz Power -
26.08.2026.md`.

---

### VIRADA: o corte de orçamento ACABA na Semana 13 (24-30/08)

> **NOTA DE 27/08:** o plano abaixo segue válido em intenção, mas a execução esbarrou na
> queda de entrega descrita acima. A parte Google está congelada até 31/08. A parte Meta
> segue normalmente.

Decidido pelo Fabricio em 24/08: **o teto de A$2.500/semana deixa de valer**. O Vaz
voltou e a capacidade de atendimento é normalizada no início de setembro (o reforço
entra até 03/09). A conta precisa estar de volta ao patamar de volume quando isso
acontecer, então a **retomada começa nesta semana, de forma gradual**.

**REGRA DA RETOMADA (definida pelo Fabricio em 24/08): aumentos GRADUAIS, para não
perder a inteligência das campanhas.** Saltos grandes de orçamento jogam o Smart
Bidding de volta ao aprendizado. Degraus de **~25% a cada 3 dias**, uma alavanca por
vez, chegando ao patamar cheio até 03/09.

*Escada de orçamento diário implementado:*
| Campanha | Hoje | 24/08 | 27/08 | 30/08 | 03/09 | Por quê |
|---|---|---|---|---|---|---|
| Meta Ligações | A$52,98 | A$66 | A$82 | A$95 | A$95 | Melhor CPL da operação (A$17,15), travada no teto |
| SUPORTE | A$45,98 | A$57 | A$71 | A$89 | A$111 | Foi a mais cortada (-86%); CPL A$81,46 |
| LP Form | A$67,98 | A$85 | A$106 | A$110 | A$110 | Melhor CPL do Google (A$69,95) |

*Reativações (voltam no orçamento anterior, não reduzido: cortar o orçamento de uma
campanha que está reiniciando só prolonga o reaprendizado):*
- Meta Formulários: pausada -> A$50,98
- Meta Remarketing: pausado -> A$11,00

*Projeção de gasto por degrau:* A$509/dia (~A$3.562/semana) -> A$550 -> A$584 ->
**A$606/dia (~A$4.239/semana)**. Referência pré-corte, S10: A$573,27/dia, A$4.013 na
semana, 72 leads a A$55,73. Hoje, S12: A$412,56/dia, A$2.888, 46 leads a A$62,78.

*Fora da escada, condicional: PMax e BRAND só quando o custo normalizar.*
Ambas estão fora do padrão (PMax A$120,88 contra A$56,93; BRAND A$92,53 contra
A$32,24). Subir orçamento nelas agora multiplicaria o custo ruim.

*Não é questão de orçamento:* FRONT (14% de uso, limitada por lances/volume) e
MADRUGA (sem entrega). Nessas o ajuste é de lance/estrutura.

*Junto com a escada:* nova rodada de **negativas** a partir dos termos de pesquisa
da semana (o Fabricio envia). Negativar enquanto sobe orçamento protege o gasto novo
de ir para busca ruim.

### CALL COM O VAZ: segunda 31/08, 20h BRT = terca 01/09, 9h AEST (Brisbane)
Pedida pelo Vaz. Convite proposto por e-mail em 30/08, aguardando a confirmacao dele
para o Fabricio subir no Google Agenda. Foi pedida a pauta com antecedencia.
Pauta provavel: queda de entrega e o site fora do ar, veredito do congelamento,
fechado de agosto. **Ao criar o evento, usar 20h BRT e deixar o Google converter.**

### AGOSTO FECHADO e publicado em `agosto-01-31/` (31/08)
A$12.581,76 | 245 leads (121 forms + 124 lig) | **CPL A$51,35, o melhor da operacao**.
Terceiro mes seguido de queda: A$70,90 -> A$55,81 -> A$51,35. Agosto bateu julho com
5,3% menos verba e 2,9% mais leads, no mes do corte e do site fora do ar.
- **A virada veio do Meta**: 111 resultados (+22%) com 30% menos verba. O Google foi ao
  contrario: 134 conv (-18) e CPL de A$63,64 para A$75,09.
- Dashboard ja incorpora o veredito (a entrega nao voltou com o site; a causa da
  permanencia e o limite de CPA; ajuste em 01/09).
- **PENDENCIA DE 03/08 ATENDIDA**: secao de plataforma e posicionamento do Meta.
  Reels 72 resultados a A$17,16 contra Feed 39 a A$29,52, com verba quase igual.
  Ligacoes vao melhor no Reels (A$15,99 x A$21,47), formularios no Feed (A$79,49 x
  A$99,74). Instagram levou 1% da verba e zero resultado, so no remarketing.

**Entrega ao cliente:** mensagem de fechamento **enviada por WhatsApp em 01/09** (do
numero pessoal do Fabricio; o business segue fora do ar), tambem nos grupos backup.
Versao por e-mail preparada como registro detalhado, sem o pedido de "recebido".

### PROXIMOS PASSOS COMBINADOS (01 a 04/09)
- **01/09 de manha (BRT): o Fabricio ajusta o limite de CPA no Google.** Como Brisbane
  esta 13h a frente, isso cai no fim do dia 01/09 la: **o primeiro dia inteiro com a
  config nova e 02/09 australiano.**
- **04/09 (sexta): compromisso assumido com o cliente no e-mail de fechamento** de
  escrever dizendo se a entrega voltou, com numero. Puxar o export **depois das 11h BRT**
  para ter o 04/09 completo. Referencia prometida: 50 a 70 leads/semana (historico real
  de julho ao inicio de agosto).
- **Se nao reagir ate 04/09**, o passo seguinte combinado e trocar a estrategia de lances.
- Redistribuir o Meta por formato (ligacao no Reels, formulario no Feed) e testar
  Instagram fora do remarketing.

### Semana 13 (24-30/08) PUBLICADA em `agosto-24-30/` (31/08)
A$1.436,25 | 48 leads (17 forms + 31 lig) | CPL A$29,92. Montada com a memoria de
27/08: encara a queda de entrega de frente, com a tabela de gasto por dia
(A$580 -> A$271 -> A$74 -> A$71) contra o previsto. NAO atribui a queda as negativas
(nao confirmadas) e NAO vende o CPL como recorde (conta rodou em fracao da verba).
Utilizacao calculada sobre o teto alcancavel (A$718, sem a MADRUGA) = 17%.
Traz bloco proprio para a medicao do /book/ e a contagem dupla evitada.
Entrega ao cliente foi por E-MAIL, enviado em 31/08, cobrindo a S13 e a correcao da
S12 num so e-mail, com pedido de resposta ("recebido") por falta de outro canal.

**CANAL DE ENTREGA (31/08): o WhatsApp do Fabricio esta instavel.** O business esta fora
do ar ha dias; o pessoal voltou e caiu de novo em 31/08. Enquanto durar, **o e-mail e o
canal** para mandar dashboard e invoice. E-mail pede outro registro que o WhatsApp:
assunto, saudacao e assinatura, mas o mesmo tom de sempre.

### Semana 12 (17-23/08) CORRIGIDA e republicada em 31/08
A leitura da BRAND atribuia o estouro de CPL a "leilao de marca mais disputado".
Com o achado do site fora do ar de 20 a 25/08 (quatro dos sete dias da S12, contra
dois da S13), a causa provavel e a pagina de destino quebrada. Correcao marcada de
forma VISIVEL no dashboard, com nota de "Atualizacao de 31/08", porque a versao
anterior ja tinha sido enviada ao cliente. Numeros inalterados, so a leitura mudou.

### Semana 12 (17-23/08) publicada em `agosto-17-23/`, mensagem enviada ao Vaz (24/08)
A$2.887,89 | 46 leads (22 forms + 24 lig) | CPL A$62,78 | A$388 acima do teto.
Ação da semana: semana cheia sob o teto + encerramento do teste de LP Call.
Próximos passos do dashboard já anunciam o fim do teto e a retomada gradual.
**Segue pendente confirmar com o Fabricio:** (1) a LP Call foi mesmo encerrada na
otimização? (sumiu das ativas, deixou resíduo de A$79,67); (2) a lista de negativas
da seção 0.1 chegou a ser aplicada?

**Semana 11 (10 a 16/08) publicada** em `agosto-10-16/` (hub e README atualizados,
mensagem enviada ao Vaz em 17/08). Ação da semana registrada: redução e controle de
investimento a pedido do Vaz (teto A$2.500/semana), queda de leads apresentada como
decisão do cliente. Números: A$3.188,58 | 53 leads (27 forms + 26 lig) | CPL A$60,16.

**Incremento de negativas entregue em 17/08** (análise dos termos de 10-16/08 com o
skill google-ads-2026). Lista completa na seção 0.1 abaixo, para a **sessão de
otimização aplicar na lista compartilhada** (a mesma das 41 de julho; duplicado o
Google ignora). Teria evitado ~A$229 na semana (PRONTO) + ~A$80 nos itens de revisão,
11% do investimento Google. Pendência de relatório de termos de julho: ATENDIDA.

### 0.1 Incremento de negativas (17/08, termos de 10-16/08) · APLICAR

**PRONTO PRA COLAR (45):**

```
[move me in]
[ss removals]
[ss removals and rentals]
[one stop movers]
[toucan removals]
[knights force removals]
[wecube removals]
[easy little moves]
[redcliffe furniture relocations and storage]
[2 men and a truck]
[2 men and a truck removalists]
[two men with a truck]
[two guys and a truck]
[abel truck]
[mover truck]
[townsville removals]
[townsville mini moves]
taxibox
container
containers
uber
trailer
trailers
rent
renting
rental
rentals
supercheap
hourly
"per hour"
"truck hire"
"truck hires"
"truck rental"
"rental trucks"
"truck movers"
"for hire"
"hire movers"
"hire a mover"
"labour hire"
"small job"
"free removalist"
"free furniture removal"
"packing box"
"storage box"
"best way"
```

**REVISAR ANTES (decisão do Fabricio):**
- Família de custo (`cost`, `costs`, `price`, `prices`, `"how much"`): A$29,85 na
  semana, MAS 1 conversão veio de "how much do packers and movers cost" (A$10,57).
- `[gantic removals & storage]`: concorrente, mas converteu 1 vez (A$21,84).
- `[removalists in adelaide]`: fora de área, mas converteu 1 vez (A$28,75); pode ser
  mudança Adelaide -> Brisbane.
- Gold Coast / Sunshine Coast em exata, se o raio não cobre: `[removalists gold coast]`
  `[removalist gold coast]` `[removals gold coast]` `[gold coast removalists]`
  `[furniture removalists gold coast]` `[removalists on the gold coast]`
  `[removalist sunshine coast]` `[best removalists sunshine coast]`
  `[hope island removalists]`
- `truck` em ampla: corta tudo de uma vez, mas pode pegar busca legítima (por isso
  só as frases estão no bloco pronto).

**PROTEGIDOS (não negativar):** corredores "brisbane to X" / "X to brisbane"
(interestadual = premium, inclui "moving to perth"), tudo de piano, "packers and
movers", "near me", marca Vaz Power.

### Para a Semana 13 (24-30/08, dashboard ~31/08) e o fechado de agosto
- ~~**Semana da retomada**: executar a Fase 1 acima e registrar as datas de cada
  aumento, porque a S13 vai ser meia cortada, meia retomada (igual à S11 ao contrário).
  No dashboard, a subida de leads é **decisão do cliente**, não mérito de otimização.~~
  **VENCIDO EM 27/08.** A previsão era subida de leads e o que houve foi queda de entrega,
  no Google. A escada da Meta seguiu e parou no segundo degrau. Ver os itens 5 e 5b da
  atualização no topo desta seção
- **PMax e BRAND**: as duas seguem fora do padrão. É o que precisa normalizar antes
  de receber orçamento. BRAND com CPC de A$14,32 (era A$8,79) sugere leilão de marca
  mais disputado; vale checar quem está anunciando sobre "Vaz Power".
- **MADRUGA**: três semanas sem entrega. Decidir se mantém, reestrutura ou encerra.
- **FRONT**: status voltou a acusar limitação de lances. É tCPA, não orçamento.
- **Fechamento de agosto** (dashboard do mês, início de setembro): pedir ao Fabricio
  os exports de **PLATAFORMA e POSICIONAMENTO do Meta** (combinado desde 03/08).
- Gotchas dos exports recentes: o GADS pode vir SEM a coluna "Enviar formulário de
  lead" (forms = conversões - ligações); campanha encerrada no meio da semana some
  de "Total: Campanhas" mas continua em "Total: Conta" (foi assim com a LP Call na
  S12: resíduo de A$79,67, 132 impressões).
- Config no fim da S12: Google A$798,98/dia implementado (SUPORTE em A$45,98, LP Call
  encerrada); Meta só Ligações ativa (A$52,98/dia); Meta Forms e RMKT pausadas.

---
## 2. Histórico semanal

| Semana | Período | Investimento | Leads | CPL geral |
|---|---|---|---|---|
| 1 | 01-07/06 | A$2.941 | 36 | A$81,71 |
| 2 | 08-14/06 | A$2.890 | 49 | A$58,97 |
| 3 | 15-21/06 | A$2.926 | 46 | A$63,62 |
| 4 | 22-28/06 | A$2.963 | 40 | A$74,06 |
| 5 | 29/06-05/07 | A$2.635 | 43 | A$61,28 |
| 6 | 06-12/07 | A$2.567 | 52 | A$49,37 |
| 7 | 13-19/07 | A$3.392 | 62 | A$54,71 |
| 8 | 20-26/07 | A$3.527 | 53 | A$66,54 |
| 9 | 27/07-02/08 | A$2.956 | 50 | A$59,11 |
| 10 | 03-09/08 | A$4.013 | **72** | A$55,73 |
| 11 | 10-16/08 | A$3.189 | 53 | A$60,16 |
| 12 | 17-23/08 | A$2.888 | 46 | A$62,78 |
| 13 | 24-30/08 | A$1.436 | 48 | **A$29,92** |

Semana 11 = primeira sob o teto novo (corte no meio da semana).
Semana 12 = primeira inteira sob o teto; fechou A$388 acima (PMax e BRAND seguram).
Recorde de volume: **72 leads** na Semana 10. Melhor CPL: A$49,37 na Semana 6.

## Meses fechados

| Mês | Investimento | Leads | CPL | Google | Meta |
|---|---|---|---|---|---|
| Junho | A$12.478,20 | 176 | A$70,90 | A$8.737,42 · 137 conv | A$3.740,78 · 59 result |
| Julho | A$13.283,97 | 238 | A$55,81 | A$9.673,82 · 152 conv | A$3.610,15 · 91 result |
| Agosto | A$12.581,76 | 245 | **A$51,35** | A$10.062,52 · 134 conv | A$2.519,24 · 111 result |

Julho superou junho em 35% de leads com 6,5% mais verba. O salto veio das **ligações**
(12 em junho para 76 em julho), efeito do reposicionamento do Meta para marca premium.

---

## 3. Situação das campanhas (Semana 11, pós-corte)

| Campanha | Orç./dia | Uso | CPL | Observação |
|---|---|---|---|---|
| PMax | A$139,08 | 100% | A$193,91 | **Semana ruim** (era A$56,93), vigiar |
| SUPORTE | A$45,98 | 106%* | A$85,29 | **Reduzida em 86%** no corte |
| Teste LP Form | A$67,98 | 100% | A$78,98 | No teto |
| Teste LP Call | A$53,98 | 83% | A$313,59 | Segue com custo alto |
| BRAND | A$128,98 | 32% | A$32,24 | Melhor CPL Google, 9 conv |
| FRONT | A$287,98 | 17% | A$87,20 | Retomou parcial (4 conv) |
| MADRUGA | A$128,98 | 0% | - | Zero entrega na S11 |
| Meta Ligações | A$52,98 | 99% | A$16,71 | **Recorde da operação** |
| Meta Formulários | pausada | - | A$28,71 | Pausada no corte (rodou 2 dias) |
| Meta Remarketing | pausada | - | alcance | Pausado no corte |

*Uso acima de 100% porque o gasto da semana inclui os dias antes do corte.

---

## 4. Pontos abertos

**FRONT travada.** Duas semanas em ~5% do orçamento. O status do Google passou de
"volume de pesquisas limitado" para **"volume limitado E estratégia de lances limitada"**,
o que normalmente indica **CPA alvo baixo demais**. Subir o tCPA tende a destravar mais
que mexer no orçamento.

**Configurações automáticas do Google.** Foram encontradas ativadas em 27/07-02/08 e
geraram inconsistências de entrega. Vale desativar o *auto-apply* de recomendações para
não reverter sozinho o que for ajustado.

**Padrões por dispositivo** (confirmados em julho e na Semana 10):
- Google: **computador converte ~18% mais eficiente** que celular (A$52,63 vs A$63,80)
- Meta: **100% dos resultados vêm do celular**; ligações saem melhor no iPhone
- **Tablets: zero conversão** em três semanas seguidas, nas duas plataformas

---

## 5. Pendências combinadas

- **Aplicar o incremento de negativas** entregue em 17/08 na lista compartilhada
  (Fabricio executa; itens REVISAR ANTES dependem de decisão dele sobre raio e custo).
- **Plataforma e posicionamento do Meta**: pedir no **fechamento de agosto** (início de
  setembro). Combinado em 03/08.
- **Fechamento de agosto** (início de setembro) e **invoice INV-2026-09-001** via
  `templates/invoice/`.

---

## 6. Convenções

**Pastas dos dashboards:** `mes-DD-DD` para semanas dentro do mês (`agosto-03-09`),
`mesA-DD-mesB-DD` quando cruza o mês (`julho27-agosto02`), `mes-01-DD` para mês fechado
(`julho-01-31`).

**Invoices:** `INV-AAAA-MM-001`, faturamento antecipado (a de agosto cobre agosto).
Emitidas até aqui: 06-001 (serviço de maio), 07-001, 08-001. Próxima: **INV-2026-09-001**.
Template em `templates/invoice/`, dados sensíveis fora do git.

**Branches:** trabalho em `claude/adoring-curie-qww6u5`, publicação por commit direto no
`master`. Antes de "restaurar" algo que parece faltando, **conferir o histórico**: em
21/07 os dashboards de abril e maio foram removidos de propósito (são pré-contrato, que
começou em junho) e as skills saíram do repo por serem metodologia interna.
