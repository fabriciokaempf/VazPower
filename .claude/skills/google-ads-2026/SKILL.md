---
name: google-ads-2026
description: Use para tarefas de Google Ads (Search) de negocio premium / servico local — principalmente (1) analisar relatorio de TERMOS DE PESQUISA (search terms) e montar lista de PALAVRAS-CHAVE NEGATIVAS para filtrar lead fraca/barata/DIY/emprego/concorrente/fora de area; (2) qualificar leads premium (anuncio + landing page); (3) otimizacao semanal de campanhas. Gatilhos: "Google Ads", "negativar", "negativa(s)", "termos de pesquisa", "search terms", "palavras-chave negativas", "lead ruim/fraca/sem consciencia", "filtrar lead", "removalist/mudancas/movers/mover". NAO usar para Meta/Facebook/Instagram Ads nem LinkedIn (existe skill especifica para cada).
license: Kaempf Business — uso interno
---

# Google Ads 2026 — Negativacao & Qualificacao Premium

Metodologia da Kaempf Business (Fabricio Kaempf) para Search de negocios premium /
servico local (ex.: Vaz Power Removals & Storage — Brisbane, AU). Validada contra a
documentacao oficial do Google Ads e best practices de PPC para movers.

## Quando usar
- Cliente reclama de "lead ruim, fraca, sem consciencia" que nao combina com a
  entrega premium.
- Chegou um export de **termos de pesquisa** (CSV/zip) do Google Ads.
- Revisao semanal de campanhas de Search para cortar desperdicio e subir qualidade.

## Passo a passo

### 1. Ler o relatorio de termos de pesquisa
- Aceite o export "Pesquisar/Search terms" (e o "Palavra/Keyword" se vier junto).
- Numeros podem vir em formato BR ("AU$ 1.079,40") — normalize antes de somar.
- Atencao: se a coluna **Conversoes vier 0**, NAO da pra rankear por conversao —
  a negativacao sera por **qualidade de intencao** (encaixe premium). Diga isso ao
  cliente e recomende validar o rastreamento de conversao.

### 2. Classificar a intencao ruim (categorias de negativa)
Procure padroes que NAO combinam com premium:
- **Preco / barato / parcelamento**: cheap, cheapest, budget, affordable, discount,
  bargain, afterpay, zippay, humm, "payment plan", hourly, "per hour", calculator.
- **DIY / aluguel de caminhao / mao de obra avulsa**: "truck hire", "truck rental",
  rental, uhaul, ute, trailer, "man with a van", "labour only", "moving help", helpers.
- **Materiais / faca-voce-mesmo**: boxes, "moving boxes", supplies, "packing supplies",
  blankets, pallet, "how to pack", "best way to pack".
- **Emprego / formacao** (procura vaga, nao cliente): jobs, hiring, salary, wage,
  career, course, licence, "how to become a removalist".
- **Marcas concorrentes** (exata): negative os concorrentes que aparecem + os fortes
  do mercado local.
- **Fora da area** (exata, para PRESERVAR interestadual): cidades/regioes que o cliente
  nao atende em mudanca local.

### 3. Escolher o tipo de correspondencia (regra do Google — decorar)
- **Ampla** (`palavra`): bloqueia qualquer busca que contenha TODAS as palavras (em
  qualquer ordem). Forte para temas (cheap, calculator, jobs).
- **Frase** (`"palavra"`): bloqueia na ordem exata, deixa passar com palavras a mais.
- **Exata** (`[palavra]`): bloqueia SO a busca identica.
- Negativa **nao** filtra por "sentido", so pelas palavras digitadas.
- CUIDADOS validados:
  - NAO negative "free" sozinho (amplo) — cortaria "free quote" (lead boa).
  - Area fora usa **exata**: `[movers townsville]` NAO bloqueia "brisbane to
    townsville movers" (interestadual saindo de Brisbane = lead premium, manter).

### 4. Proteger (nunca negativar)
- Core: removalists/removalist/movers + cidade-alvo, "near me", marca do cliente.
- Especialidades premium (ex.: piano), interestadual / long distance / "brisbane to X".
- Bairros da cidade-alvo (mudanca local = boa).
- Intencao premium (otima): professional, reliable, best, insured, fragile,
  "removalists who pack for you", "free quote", "same day".

### 5. Entregar
- Arquivo .txt/.md pronto pra colar, separando **"PRONTO PRA COLAR"** dos
  **"REVISAR ANTES"** (decisoes do cliente: packers and movers, item avulso,
  self-storage, Sunshine/Gold Coast conforme raio de atendimento).
- Opcional: planilha de importacao em massa (colunas `Keyword` + `Match Type`).
- Recomende: lista mestre na Shared Library + revisao semanal (15 min).

## Alem de negativar (tracionar lead premium)
A negativacao corta o lixo; o que mais sobe qualidade e o **par anuncio + LP qualificar
antes do clique**: ancorar preco ("a partir de A$..."), destacar "fully insured / no
subcontractors / X anos", e separar campanha de **interstate** (ticket alto). Feche o
ciclo cruzando com a **qualidade da lead reportada pelo comercial** (planilha do cliente)
para, na rodada seguinte, negativar com base em DADO real, nao so intencao.

## Fontes de referencia
- Google Ads Help — About negative keywords / Negative broad match.
- Best practices de PPC para moving companies (negativar marca propria + concorrentes,
  excluir rental/supplies/boxes/uhaul/jobs e regioes nao atendidas).
