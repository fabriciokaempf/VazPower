# Handoff: Check-up da LP de formulario Vaz Power

Contexto para continuar o trabalho iniciado na sessao "Vaz Power form LP validation" (13/07/2026).

## O trabalho

Validar a LP https://moving-quote.vazpower.com.au/ (WordPress + Elementor, form da Elementor Pro) apos correcoes do webdesigner Yuri, como pre-requisito para configurar o tracking de conversao no GTM. Objetivo da LP: 100% formulario, nenhum caminho para telefone acima da dobra (teste A/B).

## Status do checklist (validado no view-source de 13/07 18:04 UTC, cache LiteSpeed)

FEITO:
1. Bloco "Call Now and Get 5% OFF" removido do topo. Nao existe "Call Now" na pagina.
2. Nenhum href="tel:" nem telefone em pagina inteira. CTA do header aponta para #free-quote.
6. Hero novo visivel com H1 ("Brisbane's Most Reviewed Removalists / 5 Stars From 1,500+ Moves") e o texto "Full service from $399,00". O bloco antigo id 82f180a nao existe mais, foi reconstruido (classes vp-left-*), sem elementor-hidden-*.
7. H1 duplicado ("5-Star 5-Star...") corrigido. Ha um unico h1 na pagina.

PENDENTE (aguardando Yuri publicar):
- Campo Phone do form: trocar type="number" para type="tel".
- Campo Phone: renomear ID. Hoje esta name="form_fields[email]" / id="form-field-email". Deve virar phone (form_fields[phone] / form-field-phone). E o item que trava o tracking: telefone chega mapeado como email.
- CSS: regra .vas-count tem "font-weight20;" sem os dois-pontos. Corrigir para "font-weight: 700;".

DECISAO DO FABRICIO: manter o formulario com os 7 campos atuais (Name, Phone, Email, Pickup Location, Drop Off Location, Move Date, Additional Details). A reducao para 4 campos foi descartada. Email mantido viabiliza enhanced conversions depois.

Mensagem com os 3 ajustes ja foi enviada ao Yuri em 13/07 (tom cordial, o cliente Vaz le a conversa).

## Como validar quando o Yuri publicar

Rede do ambiente foi liberada (era Trusted, virou Full/Custom). Buscar no HTML da home:

1. `type="tel"` no input do Phone (e ausencia de `type="number"` nesse campo)
2. `form_fields[phone]` e `form-field-phone` (e ausencia de `form_fields[email]` no campo Phone)
3. `.vas-count` com `font-weight: 700;` (e ausencia de `font-weight20`)

Usar curl com header de navegador, o WAF da Hostinger devolve 403 para fetch generico:

```bash
curl -sSL -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36" https://moving-quote.vazpower.com.au/ -o /tmp/lp.html
grep -n 'form_fields\[email\]\|form_fields\[phone\]\|type="number"\|type="tel"\|font-weight20' /tmp/lp.html
```

Atencao ao cache LiteSpeed: conferir o comentario "Page supported by LiteSpeed Cache" no fim do HTML (timestamp). Se vier versao velha, acrescentar `?nocache=1` na URL ou pedir para limpar o cache.

## Dados tecnicos para o GTM

- Container GTM: GTM-TVL5NMMF (snippet duplicado no head e body, nao quebra, vale limpar um dia)
- Form Elementor Pro: form_id = a353750, name = "New Form", pagina post id 8
- Receita de tracking (independe dos ajustes do Yuri):
  1. Tag Custom HTML em All Pages escutando o evento jQuery `submit_success` em `.elementor-form`, com push `{event: 'lead_form_success', form_id: <valor do input hidden form_id>}`
  2. Variavel de camada de dados `form_id`
  3. Acionador de evento personalizado `lead_form_success` com condicao form_id = a353750
  4. Tag de conversao Google Ads (categoria Enviar formulario de lead, uma por clique) nesse acionador
  5. Conversion Linker em All Pages (conferir se ja nao existe)
  6. Testar com GTM Preview enviando lead de teste (avisar equipe do Vaz)
- Apos o rename do campo: o gatilho/variaveis que referenciarem o campo usam `#form-field-phone`. Automacoes que esperam form_fields[email] precisam ser atualizadas junto.
- Depois: ativar enhanced conversions usando os campos email e phone do form.

## Regras de estilo do Fabricio (sempre)

- Nunca usar travessao, em nenhum texto.
- Nao usar emojis em dashboards (regra do cliente, icones viram SVG de linha).
- Comunicacao com o Yuri: tom construtivo, sem apontar culpa, o cliente le.
- Respostas em portugues.
