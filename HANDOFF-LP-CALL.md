# Handoff: Check-up da LP de Ligacao (call-quote) + estado geral Vaz Power

Contexto compilado da sessao de 24/07/2026 para continuar em outra sessao. O objetivo imediato
que travou aqui: validar a LP https://call-quote.vazpower.com.au/ apos os ajustes do webdesigner
Yuri, mas o dominio esta bloqueado na rede deste ambiente (ver secao "Bloqueio de rede").

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
- Fabricio: avisar equipe do Vaz para descartar 2 leads de teste (nome "teste"/"TESTE 2", tel
  9999999).

## Quando a LP de Call for validada e aprovada: proximo passo de tracking

Repetir a receita do GTM, mas na chave de LIGACAO (oposto da LP de formulario): conversao de
chamada Google Ads, recurso de telefone e tag Click to Call (que foram mantidos FORA da LP de
formulario) entram aqui. Link do botao: tel:1300875197.

## Regras de estilo do Fabricio (sempre)

- Nunca usar travessao, em nenhum texto.
- Nao usar emojis em dashboards (icones viram SVG de linha).
- Comunicacao com o Yuri: tom construtivo, sem apontar culpa, o cliente Vaz le o grupo.
- Respostas em portugues.
- Email do Fabricio para leads/tracking: fabricio.kaempf@gmail.com.
