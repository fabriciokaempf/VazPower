# Handoff: Check-up da LP de Ligacao (call-quote) + estado geral Vaz Power

Contexto compilado da sessao de 24/07/2026 para continuar em outra sessao. O objetivo imediato
que travou aqui: validar a LP https://call-quote.vazpower.com.au/ apos os ajustes do webdesigner
Yuri, mas o dominio esta bloqueado na rede deste ambiente (ver secao "Bloqueio de rede").

## ATUALIZACAO 24/07/2026 (sessao de continuacao): LP DE CALL VALIDADA

O bloqueio de rede caiu: `call-quote.vazpower.com.au` passou a responder HTTP 200 neste ambiente.
Baixei o HTML renderizado e validei o checklist inteiro contra o codigo real. Todos os itens P0 e
P1 do briefing do Yuri estao FEITOS.

Observacao de arquitetura: o Yuri recodificou o hero em HTML/CSS custom (blocos `vp-call-hero` e
`vp-mobile-call-bar`), nao usou mais os botoes padrao do Elementor. Por isso a checagem por classe
`elementor-size-lg` do checklist original nao se aplica: o objetivo (botao de ligar dominante) foi
atingido por outro caminho.

Resultado por item (evidencia no HTML de call-quote):

- P0.1 Botao de ligar visivel no mobile/tablet: FEITO. Hero custom sempre visivel; o unico
  `elementor-hidden-mobile` da pagina esta na secao "About us", nao em botao de ligar.
- P0.2 Barra sticky no rodape mobile: FEITO. `.vp-mobile-call-bar` com `position:fixed; bottom:0`,
  full-width, `href="tel:1300875197"`, texto "Tap to Call Now / 1300 875 197". Regra base
  `display:none` (some no desktop) e vira `display:flex` dentro de `@media (max-width:980px)`.
- P0.3 Botao de ligar do hero dominante: FEITO. `.vp-call-hero__phone` (tel:1300875197) e o
  elemento primario; o "Get a Quote" virou link de texto secundario.
- P1.4 H1 duplicado corrigido: FEITO. H1 unico "Call Brisbane's #1 Removalists / Answer in Under
  60 Seconds". Zero ocorrencia de "5-Star 5-Star".
- P1.5 Horario perto do CTA: FEITO. Subtitle do hero: "5 Stars . 1,500+ Moves . Mon-Sat 8am-6pm .
  Average Wait Under 60 Seconds". (Atencao: hero diz Mon-Sat 8am-6pm; briefing sugeria
  Mon-Fri 8am-6pm e Sat 8am-2pm. Confirmar o horario correto com o Vaz.)
- P1.6 "Get a Quote" rebaixado a secundario: FEITO. Virou link de texto "Prefer not to call? Get a
  free online quote" apontando para a LP de formulario.
- P1.7 Reviews com nomes brasileiros removidos: FEITO. Zero ocorrencia de Lucas Almeida / Sofia
  Martins / Pedro Ramos / Mariana Costa / Joao Silva / Beatriz Mendes. O bloco de reviews agora
  puxa o Google real via widget Trustindex.
- P1.8 Linha de estrelas no hero: FEITO. "4.9 Google Rating" + estrelas + link para o Google real
  (`share.google/...`).

Comandos usados para baixar e validar estao na secao "Bloqueio de rede" (curl com header de
navegador) e "Checklist da LP de Call" (grep). Repetir se precisar reconferir.

### Ponto de atencao aberto (acionado com o Yuri em 24/07)

Inconsistencia de numeros na LP de Call: o hero mostra "1,500+ verified moves" (mudancas feitas) e
o widget de avaliacoes do Google (Trustindex) logo abaixo mostra "Based on 2299 reviews". Nao sao a
mesma metrica, mas para o visitante fica estranho ter mais avaliacoes (2299) do que mudancas feitas
(1.500+), e o "1.500+" ainda subvende (o numero real do Google hoje e 2299; em abril a analise
falava em ~961, ou seja cresceu de verdade). Yuri foi acionado no grupo "Vaz Power AUS | Monitorar
Leads" para alinhar os dois numeros. Numero final a definir pelo Fabricio: opcao A "3,000+ moves"
(mantem a metrica de mudancas, acima das avaliacoes) ou opcao B focar nas 2.299 avaliacoes reais do
Google.

### Tracking de ligacao: FEITO e publicado (24/07)

O tracking de chamada foi montado, validado no Tag Assistant e publicado no mesmo dia. Como ficou:
- Google Ads (conta AW-11125805827): acao `Click to Call LP Call Quote`, categoria Contato,
  contagem Uma, janela 30 dias, valor fixo 1 AUD, enhanced conversions OFF. ID `11125805827`,
  rotulo `sUbyCKSHqNscEIOmmbkp`.
- GTM container GTM-TVL5NMMF (o do Vaz, GA4 G-L9MY62LFGY): acionador `CL - Click to Call
  (call-quote)` (Clique Apenas links, Click URL contem tel:1300875197 E Page Hostname contem
  call-quote.vazpower.com.au) e tag `GADS | Click to Call | LP Call Quote` disparando nesse
  acionador.
- Contagem dupla resolvida: havia uma tag legada do contrato anterior, `GADS | Click to Call
  (Website/LP)` (mesmo ID, rotulo antigo `Qn0hCKeVwsQbEIOmmbkp`, acionador `Trigger Click - Phone
  Call` sem filtro de hostname), disparando junto no call-quote. Foi adicionada uma EXCECAO nela
  com o acionador `CL - Click to Call (call-quote)`, entao nao conta mais em dobro na LP (segue
  rodando no resto do site).

Detalhes e passo a passo em `INSTRUCAO-TRACKING-LP-CALL.md`.

## O projeto (visao geral)

Vaz Power Removals & Storage (Brisbane, AU). Teste A/B de duas landing pages dedicadas, mesmo
template Elementor (page-id-8, WordPress 6.9.x + Elementor 3.33.5, tema Hello). Editar uma NAO
altera a outra, aplicar em cada pagina separadamente.

- LP A (formulario): https://moving-quote.vazpower.com.au/ -> objetivo 100% formulario, nenhum
  caminho para telefone acima da dobra.
- LP B (ligacao): https://call-quote.vazpower.com.au/ -> objetivo 100% ligacao para 1300 875 197,
  botao de ligar deve ser o elemento dominante, inclusive no mobile.

Documentos-fonte (PDFs que o Fabricio subiu, guardados na sessao): "revisaolpsvazpower.pdf"
(revisao completa das 2 LPs) e "briefingwebdesigner.pdf" (escopo tecnico do Yuri).

## Bloqueio de rede (o que trava a validacao da LP de Call)

RESOLVIDO em 24/07 (sessao de continuacao): `call-quote.vazpower.com.au` passou a responder HTTP
200 e a validacao foi feita (ver ATUALIZACAO no topo). O historico abaixo fica como referencia
caso o bloqueio volte em outro ambiente.

Neste ambiente o proxy libera `moving-quote.vazpower.com.au` (HTTP 200) mas BLOQUEIA
`call-quote.vazpower.com.au` (403 na tentativa de CONNECT, negacao de politica). O subdominio
call-quote precisa ser adicionado a lista de permissoes da rede do ambiente, igual foi feito com
o moving-quote (era Trusted, virou Full/Custom). Sem isso, so validando via view-source colado
manualmente. Docs: https://code.claude.com/docs/en/claude-code-on-the-web

Para baixar quando liberar (o WAF da Hostinger devolve 403 para fetch generico, usar header de
navegador e furar cache LiteSpeed):

```bash
curl -sSL -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36" "https://call-quote.vazpower.com.au/?nocache=1" -o /tmp/call.html
```

## Checklist da LP de Call (o que foi pedido ao Yuri e como validar)

Extraido do briefing do webdesigner. Marcar FEITO/PENDENTE com trecho do HTML.

P0 (critico, sem isso a LP de ligacao nao funciona no mobile):
1. Botao de ligar VISIVEL no mobile e tablet -> ausencia das classes `elementor-hidden-tablet` e
   `elementor-hidden-mobile` no botao do header.
2. Barra fixa (sticky) no rodape mobile -> presenca de barra full-width com link `tel:1300875197`,
   fundo `#DE312A`, texto "Call Now: 1300 875 197", posicao fixa na base (so mobile/tablet).
3. Botao de ligar do hero MAIOR -> `elementor-size-lg` no lugar de `elementor-size-sm`, maior que
   o botao "Get a Quote".

P1 (importante):
4. H1 duplicado corrigido -> um unico "5-Star" (o bug era "5-Star 5-Star Removalists Brisbane...").
5. Horario de atendimento perto do CTA -> texto tipo "Mon-Fri 8am-6pm - Sat 8am-2pm" abaixo do
   botao de ligar (hoje so no rodape).
6. Botao "Get a Quote" rebaixado para secundario (menor, abaixo da dobra).
7. Reviews com nomes brasileiros removidos -> ausencia de "Lucas Almeida", "Sofia Martins",
   "Pedro Ramos" (e Mariana Costa, Joao Silva, Beatriz Mendes), substituidos por reviews reais com
   nome + suburbio de Brisbane (ex.: "James T. - Chermside").
8. Linha de estrelas visivel no hero -> "4.9 stars" + "1,500+ ... reviews".

Grep sugerido apos baixar o HTML:
```bash
grep -n 'elementor-hidden-tablet\|elementor-hidden-mobile\|tel:1300875197\|#DE312A\|elementor-size-lg\|5-Star 5-Star\|Lucas Almeida\|Sofia Martins\|Pedro Ramos' /tmp/call.html
```

Atencao: nesta LP o telefone DEVE existir (objetivo e ligacao). E o oposto da LP de formulario,
onde telefone era proibido acima da dobra. Nao confundir.

## Estado da LP de Formulario (moving-quote) - CONCLUIDO nesta sessao

Os 3 ajustes que estavam pendentes foram publicados pelo Yuri e validados (16/07):
- Campo Phone: `type="tel"`, `name="form_fields[phone]"`, `id="form-field-phone"` (era number/email). OK.
- Campo Email ficou com ID generico no rebuild: `name="form_fields[field_75b5ef7]"` /
  `id="form-field-field_75b5ef7"`. Importa para enhanced conversions (seletor do email mudou).
- CSS `.vas-count`: `font-weight:700;;` (ponto-e-virgula duplo, cosmetico, funciona). OK.

Decisao do Fabricio: manter os 7 campos (Name, Phone, Email, Pickup, Drop Off, Move Date, Details).
A reducao para 4 campos sugerida no PDF foi DESCARTADA (email mantido viabiliza enhanced conversions).

## Tracking GTM (LP de formulario) - PUBLICADO e validado 2x

Container GTM-TVL5NMMF. GA4 G-L9MY62LFGY (propriedade 384115925). Form Elementor Pro form_id
`a353750`, page post id 8.

Google Ads conversao criada:
- ID de conversao: `11125805827` (tag usa `AW-11125805827`)
- Rotulo: `7IRtCJSd0NEcEIOmmbkp`
- Nome da acao: `Lead Form LP Moving Quote`, categoria Enviar formulario de lead, "Uma" por clique,
  janela de clique 30 dias, valor fixo 1 AUD, enhanced conversions ativado.

Itens montados no GTM (tudo publicado):
1. Tag HTML `Listener - Elementor Form Submit` (All Pages): escuta `submit_success` em
   `.elementor-form` e da push `{event:'lead_form_success', form_id, lead_email, lead_phone}`.
   Seletores: email `#form-field-field_75b5ef7`, phone `#form-field-phone`.
2. Variaveis camada de dados: `dlv - form_id`, `dlv - lead_email`, `dlv - lead_phone`.
3. Variavel dados fornecidos pelo usuario `UPD - Lead Form` (email + telefone).
4. Acionador `CE - lead_form_success (a353750)` (evento personalizado, form_id = a353750).
5. Tag `GADS | Lead Form LP | Moving Quote` (conversao Google Ads) no acionador acima.
6. Tag do Google `GADS Tag | AW-11125805827` recebeu parametro de evento `user_data` =
   `{{UPD - Lead Form}}` (para enhanced conversions).
7. Conversion Linker ja existia. Snippet GTM duplicado no head/body (nao quebra, limpar um dia).

Validado no Tag Assistant 2x: dispara so a tag certa, NAO dispara as antigas de thank-you page
(Quote/Form Submitted) nem a Click to Call. Sem contagem dupla, sem telefone.

## Campanha Google Ads (LP de formulario) - NO AR

`[Search] Removals Brisbane | LP Form A/B` (renomeada, tirou "EM CONSTRUCAO"). Config:
- Rede: so Search (Display e parceiros OFF). IA Max OFF. Recursos automaticos OFF.
- Locais: Brisbane cidade, opcao "Presenca". Idiomas: English, Espanhol, Portugues.
- Lances: Maximizar conversoes SEM tCPA. Orcamento AU$ 53,98/dia.
- Metas: especificas da campanha "Enviar formularios de lead" (contem 3 acoes; so a nossa dispara
  nesta LP, decisao de deixar assim). Conversao ja registrou.
- 3 grupos: `00 - Removalists Brisbane | Core`, `01 - Removalists Brisbane | Premium Intent`,
  `02 - Removalists Brisbane | House Moving`. Keywords em frase e exata (nada de ampla).
- RSA por grupo, tudo empurrando para o formulario, ancora preco "from $399".
- Sitelinks para ancoras da LP: #free-quote, #our-services, #pricing, #faq.
- Recursos de conta (chamada, lead form): confirmado que NAO herdam nesta campanha (limpo).
- Negativas aplicadas: lista anti-barato/DIY/emprego + `moving truck`. Nao negativar: `free`
  sozinho, piano, interstate, brisbane to, self storage (Vaz FAZ storage), packers and movers
  (intencao premium), removalists logan (area atendida). Gold/Sunshine Coast so em exata se o Vaz
  confirmar que nao atende.

Dia 1 (18/07): 33 impressoes, 5 cliques, CTR 15,15%, 1 conversao, CPL AU$ 66,30. Amostra pequena,
NAO mexer em lance por ~2 semanas (aprendizado). Termos de pesquisa limpos, "hire moving truck
brisbane" ja coberto por `truck hire`.

## Pendencias abertas (dependem de terceiros)

- Vaz: confirmar se a conversao do dia 1 foi lead real; definir preco correto (396 na mensagem de
  sucesso vs 399 no hero/anuncio).
- Yuri (mensagens ja enviadas no grupo "Vaz Power AUS | Monitorar Leads"): corrigir typo "tocuh"
  -> "touch" na mensagem de sucesso; padronizar preco; adicionar email fabricio.kaempf@gmail.com
  nas notificacoes do formulario; integrar formulario com Google Sheets (modelo de planilha de
  leads ja entregue ao Fabricio, com colunas de qualificacao para o ciclo de negativacao).
- Yuri (LP de Call, acionado em 24/07 no mesmo grupo): alinhar os numeros da LP de Call. O hero
  mostra "1,500+ verified moves" e o widget do Google mostra "Based on 2299 reviews"; ficou
  estranho ter mais avaliacoes que mudancas feitas. Numero final a definir pelo Fabricio, opcao A
  "3,000+ moves" ou opcao B focar nas 2.299 avaliacoes reais (ver ATUALIZACAO no topo).
- Fabricio: avisar equipe do Vaz para descartar 2 leads de teste (nome "teste"/"TESTE 2", tel
  9999999).

## Tracking da LP de Call: CONCLUIDO em 24/07

LP validada e tracking de ligacao publicado no mesmo dia (ver "Tracking de ligacao: FEITO" na
ATUALIZACAO do topo, e o passo a passo em `INSTRUCAO-TRACKING-LP-CALL.md`). Link do botao:
tel:1300875197.

Confirmado (conferido no dia seguinte): a acao `Click to Call LP Call Quote` esta ATIVA no Google
Ads e ja gravou conversoes (2 conv registradas), origem Site, otimizacao Principal. Tracking
validado ponta a ponta (clique no botao -> GTM -> conversao). A campanha de Search para o objetivo
de ligacao ja foi criada e ativada (ver secao "Campanha de teste da LP de Call" abaixo).

Nota (limpeza futura): no resumo de conversoes do Google Ads ha varias acoes secundarias do
contrato anterior com "Requer atencao"/"Inativo" (Call Click Website/LP, Click - Phone Call
(Website), WhatsApp Click etc.), todas com 0 conversao. Nao afetam a campanha (que usa so a
`Click to Call LP Call Quote` como meta). Limpar quando revisar o tracking do site.

Limpeza futura (quando revisar o tracking do site, nao urgente): a tag legada `GADS | Click to
Call (Website/LP)` do contrato anterior ainda roda no resto do site, mal configurada (dispara em
qualquer tel: sem escopo). Hoje so foi neutralizada no call-quote via excecao.

## Campanha de teste da LP de Call: NO AR

Campanha `[Search] Removals Brisbane | LP Call A/B`, duplicada da campanha de formulario e ativada
na sessao de continuacao (mesma da validacao da LP e do tracking). E o lado "ligacao" do teste A/B
(a outra ponta e a `LP Form A/B`, que ficou intacta).

Config:
- Orcamento AU$ 53,98/dia (a form esta em 67,98/dia; o teste roda com verba um pouco menor, decisao
  do Fabricio).
- Meta: Contatos > Site (acao `Click to Call LP Call Quote`). Lance Maximizar conversoes SEM tCPA
  (a copia veio com tCPA de AU$65, removido porque a conversao e nova, zero historico). IA Max OFF.
  Brisbane cidade / Presenca. Idiomas EN + ES + PT. Correspondencia ampla OFF.
- 3 grupos (Core, Premium Intent, House Moving). RSAs reescritos para intencao de LIGACAO, URL final
  `call-quote.vazpower.com.au` em todos, cada grupo com titulos da sua keyword (Core: removalists
  brisbane; Premium: premium/professional; House: house movers / home removals). Ad strength
  Excelente nos 3.
- Sitelinks proprios da campanha apontando pro call-quote: Call Now for a Quote (/), Pricing
  (/#pricing), Moving FAQs (/#faq), Why Vaz Power (/). Os sitelinks antigos (form) foram
  desvinculados so da Call; a Form seguiu com os originais (Get A Free Quote / Fill the form).
- Sem call asset: o recurso de chamada da conta ("1300 875 197", nivel conta) nao herda nessas
  campanhas, entao todas as conversoes vem pelo clique na LP (A/B limpo).

Benchmark a bater: a campanha de formulario esta com CPL AU$ 68,14 no periodo.

Cuidados / pendencias:
- Primeiros 3 a 5 dias sao de aprendizado (conversao nova). NAO mexer em lance nem orcamento nesse
  comeco.
- Depois de juntar termos de pesquisa (~3-5 dias), rodar negativacao com base nos termos reais
  (skill google-ads-2026).
- O RSA do grupo Core ainda tem o titulo "Full Service From $399". Alinhar o preco quando o Vaz
  confirmar 396 vs 399.

## Regras de estilo do Fabricio (sempre)

- Nunca usar travessao, em nenhum texto.
- Nao usar emojis em dashboards (icones viram SVG de linha).
- Comunicacao com o Yuri: tom construtivo, sem apontar culpa, o cliente Vaz le o grupo.
- Respostas em portugues.
- Email do Fabricio para leads/tracking: fabricio.kaempf@gmail.com.
