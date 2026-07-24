# Instrucao de tracking da LP de Ligacao (call-quote): conversao de chamada

Espelho do tracking ja feito e validado na LP de formulario (moving-quote), mas na chave de
LIGACAO. Mesmo container GTM, mesma conta Google Ads, mesma propriedade GA4. A diferenca central:
na LP de formulario a conversao e o envio do formulario; aqui a conversao e o clique no link de
telefone (Click to Call) para tel:1300875197.

## Dados fixos (reaproveitados da LP de formulario)

- Container GTM: GTM-TVL5NMMF
- GA4: G-L9MY62LFGY (propriedade 384115925)
- Conta Google Ads (tag base): AW-11125805827 (o Conversion Linker ja existe no container)
- LP de Call: https://call-quote.vazpower.com.au/ (WordPress + Elementor, page-id 8)
- Numero: tel:1300875197 (sem espacos, e assim que os links aparecem no HTML). Na LP ha varios
  pontos de ligar com esse mesmo link: botao do header, botao do hero, barra sticky do mobile e
  demais CTAs da pagina.

## Regra de ouro (nao repetir o erro inverso)

Na LP de formulario o telefone foi mantido FORA de proposito e a tag Click to Call foi impedida de
disparar la. Aqui e o oposto: a conversao de chamada DEVE disparar. Ao configurar, escopar o
acionador pelo hostname `call-quote.vazpower.com.au`, para a chamada nao contar na LP de formulario
nem em outras paginas.

## Passo 1: Google Ads, criar a acao de conversao de chamada

Ferramentas e configuracoes > Conversoes (Metas) > Nova acao de conversao.

- Origem: Site (vamos disparar via GTM, igual a conversao do formulario).
- Categoria: Contato (Contact).
- Nome da acao: `Click to Call LP Call Quote`.
- Valor: fixo, 1 AUD (espelha o formulario; pode ajustar depois).
- Contagem: "Uma" por clique (um clique = um lead; se a pessoa clicar 2x, conta 1).
- Janela de conversao por clique: 30 dias.
- Enhanced conversions: DEIXAR DESLIGADO aqui. No clique de ligar nao capturamos os dados do
  cliente (o telefone do link e o SEU, nao o do visitante), entao enhanced conversions for leads
  nao se aplica. Isso e diferente da LP de formulario, onde havia email e telefone do lead.
- Ao salvar, o ID de conversao continua sendo `11125805827` (AW-11125805827) e o Google gera um
  ROTULO novo, so dessa acao. Anotar esse rotulo, ele vai na tag do GTM. Para referencia, o rotulo
  da conversao de formulario era `7IRtCJSd0NEcEIOmmbkp`; a de chamada tera um rotulo proprio,
  diferente.

Alternativa (so se quiser duracao de chamada, nao apenas o clique): usar "Chamadas para um numero
de telefone no seu site" com numero de encaminhamento do Google. Isso exige trocar o numero
exibido pelo numero do Google (snippet de telefone), e o Yuri teria que aceitar o swap do numero
na LP. Mais completo, porem mais invasivo. Para manter o espelho simples e sem mexer no numero
real, seguir com o clique (acima).

## Passo 2: GTM, montar o disparo

Abrir o container GTM-TVL5NMMF e criar um Workspace novo.

1. Variaveis internas: em Variaveis > Configurar, habilitar as built-in `Click URL` e
   `Page Hostname`.
2. Acionador: novo, tipo "Clique - Apenas links" (Just Links).
   - Nome: `CL - Click to Call (call-quote)`.
   - Disparar em: Alguns cliques em links.
   - Condicao 1: `Click URL` contem `tel:1300875197`.
   - Condicao 2: `Page Hostname` e igual a `call-quote.vazpower.com.au`.
   - Deixar "Aguardar tags" e "Verificar validacao" desligados, para nao atrasar a acao do tel: no
     mobile.
3. Tag: nova, tipo "Conversao do Google Ads" (Google Ads Conversion Tracking).
   - Nome: `GADS | Click to Call | LP Call Quote`.
   - ID de conversao: `11125805827`.
   - Rotulo de conversao: o rotulo novo criado no Passo 1.
   - Valor: 1, moeda AUD (ou deixar vazio).
   - Acionador: `CL - Click to Call (call-quote)`.
4. Opcional, para relatorio no GA4: tag de evento GA4.
   - Nome: `GA4 | click_to_call | LP Call Quote`.
   - Nome do evento: `click_to_call`. Mesmo acionador do item 3.

## Passo 3: evitar contagem dupla (tag legada)

O container ja tinha uma tag "Click to Call" antiga (mencionada no handoff, ficou fora da LP de
formulario). Antes de publicar:

- Verificar se essa tag legada dispara em cliques `tel:` e em quais paginas.
- Se ela cobrir a LP de Call: ou desativa-la e usar so a nova (recomendado, porque a config nova e
  conhecida e escopada), ou manter so a legada. Nao deixar as duas disparando no mesmo clique.
- Conferir tambem que as tags antigas de thank-you page (Quote / Form Submitted) NAO disparam
  nesta LP.

## Passo 4: validar (Preview / Tag Assistant)

No GTM, clicar em "Visualizar" e abrir https://call-quote.vazpower.com.au/.

- Clicar nos 3 pontos de ligar: botao do header, botao do hero e barra sticky do mobile
  (redimensionar o navegador para no maximo 980px de largura para a barra aparecer).
- Confirmar: a tag `GADS | Click to Call | LP Call Quote` dispara UMA vez por clique.
- Confirmar: NAO disparam a conversao do formulario, nem as tags de thank-you page, nem 2x a de
  chamada.
- Em Google Ads a conversao pode levar horas para aparecer. Fazer um clique de teste real e
  conferir o status da acao depois (deve sair de "Nao verificada" para gravando conversoes).

## Passo 5: publicar

Publicar o container com nome de versao tipo `Click to Call LP Call Quote`. Registrar o resultado
da validacao (igual foi feito 2x no Tag Assistant para o formulario), para o proximo handoff.

## Depois do tracking: campanha

Com a conversao de chamada valida, seguir o plano do projeto de duplicar a campanha de Search para
o objetivo de ligacao (uma campanha empurrando formulario, outra empurrando ligacao), usando a nova
acao `Click to Call LP Call Quote` como meta da campanha de ligacao. A config de rede, local,
idiomas e lances pode espelhar a campanha de formulario ja no ar
(`[Search] Removals Brisbane | LP Form A/B`).
