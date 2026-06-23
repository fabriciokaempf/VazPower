# Correções Mínimas para Validar o Teste A/B: Formulário vs. Ligação

**Objetivo do teste:** Descobrir qual mecanismo de conversão gera mais lead qualificado com menor CPL.
**Condição para o teste ser válido:** cada LP deve ter UMA única saída de conversão, sem vazamento para a outra.

---

## LP 1 — moving-quote.vazpower.com.au
**Conversão-alvo:** envio de formulário

### P0 — Sem isso o teste é inválido

- [ ] **Remover bloco "Call Now and Get 5% OFF"** acima da dobra — está desviando tráfego para ligação dentro da LP de formulário
- [ ] **Remover ou ocultar o número de telefone** de qualquer área visível acima da dobra (header, hero, sticky bar)
- [ ] **Corrigir `type="number"` → `type="tel"`** no campo de telefone do form — sem teclado de discagem no mobile, abandono aumenta
- [ ] **Corrigir `name="form_fields[email]"`** no campo de telefone — dado de telefone está caindo no slot de e-mail no CRM
- [ ] **Confirmar no GTM** que o evento `form_submit` está disparando corretamente para esta LP (tag separada ou com parâmetro de origem)

### P1 — Melhora a qualidade do dado sem mudar a variável

- [ ] Reduzir form de 8 → 4 campos: **Nome, Telefone, Cidade de Origem, Data da Mudança** — menos abandono, mais leads para comparar
- [ ] Tornar o bloco hero visível (ID `82f180a` está com `elementor-hidden-desktop elementor-hidden-tablet elementor-hidden-mobile`) — H1 e $399 estão ocultos para todos os visitantes
- [ ] Corrigir H1 duplicado: "5-Star 5-Star Removalists..." → remover uma ocorrência

---

## LP 2 — call-quote.vazpower.com.au
**Conversão-alvo:** ligação para 1300 875 197

### P0 — Sem isso o teste é inválido

- [ ] **Remover `elementor-hidden-tablet elementor-hidden-mobile`** do botão de ligar no header — o CTA principal está oculto na maioria das sessões
- [ ] **Adicionar barra fixa no rodapé (mobile)** com botão `tel:1300875197` full-width — elemento essencial para LP de ligação, não existe no DOM
- [ ] **Aumentar tamanho do botão de ligar**: `elementor-size-sm` → `elementor-size-lg` ou largura customizada — visualmente igualado ao "Get a Quote", sem hierarquia
- [ ] **Confirmar no GTM** que o evento de clique em `tel:1300875197` está configurado como conversão — sem isso a ligação não é contabilizada no Google Ads

### P1 — Melhora a qualidade do dado

- [ ] Adicionar horários de atendimento abaixo do botão de ligar: "Seg–Sex 8h–18h · Sáb 8h–14h" — reduz cliques perdidos fora do horário
- [ ] Rebaixar "Get a Quote" para abaixo da dobra ou remover do hero — botão de form competindo com o CTA de ligação no mesmo nível visual
- [ ] Corrigir H1 duplicado: "5-Star 5-Star Removalists..."

---

## Rastreamento (vale para as duas LPs)

- [ ] Confirmar que GTM-TVL5NMMF tem **duas conversões separadas**: `form_submit` e `call_click`
- [ ] No Google Ads: criar **colunas de conversão separadas** por tipo (form vs. ligação) para leitura do teste
- [ ] Período mínimo de teste: **3 semanas ou 50 conversões por LP** — o que vier primeiro

---

## O que NÃO mudar durante o teste

Para não contaminar as variáveis, manter igual nas duas LPs:

- Mesma oferta ($399 mínimo, seguro incluído)
- Mesmo orçamento de mídia
- Mesmo segmento de audiência / campanha
- Mesmo período de veiculação

---

## Critério de decisão

| Métrica | LP vencedora se... |
|---|---|
| CPL (custo por lead) | menor custo por conversão válida |
| Taxa de lead qualificado | % de leads que viraram orçamento enviado |
| Taxa de fechamento | % de orçamentos que viraram contrato |

**Atenção:** volume de lead sozinho não decide — uma ligação qualificada pode valer 3x um form preenchido errado.
