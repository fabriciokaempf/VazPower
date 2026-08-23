# Estado da operação · Vaz Power

Resumo vivo do projeto, para retomar o contexto em qualquer sessão nova.
Atualizado em **24/08/2026** (Semana 12 montada; **fim do corte decidido**).

---

## 0. ESTADO ATUAL (retomar daqui)

### VIRADA: o corte de orçamento ACABA na Semana 13 (24-30/08)

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

### Semana 12 (17-23/08) PUBLICADA em `agosto-17-23/` (24/08)
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
- **Semana da retomada**: executar a Fase 1 acima e registrar as datas de cada
  aumento, porque a S13 vai ser meia cortada, meia retomada (igual à S11 ao contrário).
  No dashboard, a subida de leads é **decisão do cliente**, não mérito de otimização.
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

Semana 11 = primeira sob o teto novo (corte no meio da semana).
Semana 12 = primeira inteira sob o teto; fechou A$388 acima (PMax e BRAND seguram).
Recorde de volume: **72 leads** na Semana 10. Melhor CPL: A$49,37 na Semana 6.

## Meses fechados

| Mês | Investimento | Leads | CPL | Google | Meta |
|---|---|---|---|---|---|
| Junho | A$12.478,20 | 176 | A$70,90 | A$8.737,42 · 137 conv | A$3.740,78 · 59 result |
| Julho | A$13.283,97 | 238 | A$55,81 | A$9.673,82 · 152 conv | A$3.610,15 · 91 result |

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
