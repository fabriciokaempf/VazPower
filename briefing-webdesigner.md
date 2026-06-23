# Briefing Técnico — Webdesigner (Elementor)

**Escopo:** alterações de layout/HTML/CSS no Elementor. Rastreamento (GTM/conversões) NÃO entra aqui — fica com o cliente.
**Plataforma:** WordPress 6.9.x + Elementor 3.33.5 (tema Hello).
**Importante:** as duas LPs são `page-id-8` (mesmo template). Editar uma NÃO altera a outra automaticamente — aplicar em cada página separadamente.

---

## LP 1 — moving-quote.vazpower.com.au
Objetivo da página: **só formulário**. Remover qualquer caminho para telefone acima da dobra.

### P0
- [ ] **Remover o bloco "Call Now and Get 5% OFF"** que fica acima da dobra (no hero). Excluir o widget inteiro.
- [ ] **Remover o número de telefone / botão de ligar** de qualquer área visível acima da dobra (header e hero).
- [ ] **Campo de telefone do formulário:** trocar o tipo do input de `number` para **`tel`**.
  - No Elementor: editar o campo do form → *Type* → selecionar **Tel** (não "Number").
- [ ] **Campo de telefone — nome/ID errado:** hoje está como `form_fields[email]`. Renomear o campo para um ID próprio (ex.: `phone`) no painel do campo (aba *Advanced* → *ID*).

### P1
- [ ] **Reduzir o formulário de 8 → 4 campos.** Manter apenas: **Nome, Telefone, Cidade de Origem, Data da Mudança.** Remover: Email, Drop Off Location, checkbox "Packing?", checkbox "Storage?".
- [ ] **Bloco hero oculto:** o bloco de ID `82f180a` está com as classes `elementor-hidden-desktop elementor-hidden-tablet elementor-hidden-mobile` — está invisível para todos. Remover essas classes (aba *Advanced* → *Responsive* → desmarcar "Hide on…") para que o H1 e o "$399" apareçam.
- [ ] **H1 duplicado:** o título está "5-Star 5-Star Removalists Brisbane…". Remover a primeira ocorrência de "5-Star".
- [ ] **Bug de CSS:** na regra `.vas-count` está `font-weight20;` (faltam os dois-pontos). Corrigir para `font-weight: 20;` — ou o valor correto desejado.

---

## LP 2 — call-quote.vazpower.com.au
Objetivo da página: **só ligação**. O botão de ligar precisa ser o elemento dominante, inclusive no mobile.

### P0
- [ ] **Botão de ligar no header está oculto no mobile/tablet:** remover as classes `elementor-hidden-tablet elementor-hidden-mobile` do botão (aba *Advanced* → *Responsive*).
- [ ] **Criar barra fixa no rodapé (mobile)** com botão de ligar full-width:
  - Link: `tel:1300875197`
  - Posição: fixa na base da tela (sticky bottom), só no mobile/tablet.
  - Texto: "📞 Ligar Agora: 1300 875 197".
- [ ] **Aumentar o botão de ligar do hero:** trocar `elementor-size-sm` por **`elementor-size-lg`** (ou largura customizada full-width no mobile). Ele deve ficar visualmente maior que o botão "Get a Quote".

### P1
- [ ] **Adicionar horários abaixo do botão de ligar:** "Seg–Sex 8h–18h · Sáb 8h–14h".
- [ ] **Rebaixar o botão "Get a Quote"** do hero — mover para abaixo da dobra ou deixar como botão secundário menor.
- [ ] **H1 duplicado:** mesmo bug "5-Star 5-Star…". Remover uma ocorrência.

---

## Observações gerais
- Aplicar tudo **em cada página separadamente** (são page-id duplicado).
- Não alterar oferta, textos de preço ($399) ou imagens fora do que está listado.
- Testar no **mobile real** após publicar — a maioria do problema está no comportamento mobile.
