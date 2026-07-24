# HANDOFF — LP de Ligação (`call-quote.vazpower.com.au`)

**De:** Tráfego (Fabricio)
**Para:** Webdesigner (Yuri)
**Escopo:** somente Elementor / HTML / CSS. Rastreamento (GTM / conversões) **não** entra aqui — fica com o tráfego.
**Plataforma:** WordPress 6.9.x + Elementor 3.33.5 (tema Hello).

> ⚠️ **Importante:** as duas LPs são `page-id-8` (mesmo template). Editar a LP de formulário **não** altera esta — aplicar as mudanças **nesta página separadamente**.

---

## Objetivo da página

**Somente ligação.** O botão de ligar precisa ser o elemento **dominante** da tela, inclusive (e principalmente) no **mobile**. Nenhum caminho deve competir com a ligação acima da dobra.

---

## Checklist de itens PENDENTES

### P0 — essencial (sem isso o teste A/B fica inválido)

- [ ] **Botão de ligar do header oculto no mobile/tablet** — hoje tem as classes `elementor-hidden-tablet elementor-hidden-mobile`. Remover essas classes (aba *Advanced* → *Responsive* → desmarcar "Hide on Tablet / Hide on Mobile"). O CTA principal está invisível na maioria das sessões.
- [ ] **Criar barra fixa no rodapé (sticky bar mobile)** com botão de ligar full-width:
  - Link: `tel:1300875197`
  - Posição: fixa na base da tela (sticky bottom), **só no mobile/tablet**.
  - Texto: **"Ligar Agora: 1300 875 197"**.
- [ ] **Aumentar o botão de ligar do hero** — trocar `elementor-size-sm` por `elementor-size-lg` (ou largura full-width no mobile). Deve ficar **visualmente maior** que o botão "Get a Quote".

### P1 — melhora (não muda a variável do teste)

- [ ] **Adicionar horários abaixo do botão de ligar:** "Seg–Sex 8h–18h · Sáb 8h–14h".
- [ ] **Rebaixar o botão "Get a Quote"** do hero — mover para abaixo da dobra ou deixar como botão secundário menor. Não pode competir no mesmo nível visual com o CTA de ligação.
- [ ] **H1 duplicado** — corrigir o título "5-Star 5-Star Removalists Brisbane…". Remover a primeira ocorrência de "5-Star".

---

## O que NÃO mudar

- Oferta, textos de preço (`$399`) e imagens fora do que está listado acima.
- Estrutura das seções abaixo da dobra (depoimentos, benefícios, etc.).

## Definição de pronto (DoD)

1. Todos os P0 aplicados **e publicados**.
2. Testado em **mobile real** (não só no preview do Elementor) — a maior parte do problema está no comportamento mobile.
3. Avisar o tráfego para validação e configuração do tracking de conversão (GTM).

---

*Documento de handoff — LP de ligação. A LP de formulário (`moving-quote.vazpower.com.au`) tem checklist próprio.*
