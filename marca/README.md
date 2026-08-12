# Marca · Avatares de grupo

Imagens de perfil para os grupos de WhatsApp do projeto, montadas com os ativos
oficiais da Vaz Power.

## Baixar

| Grupo | Arquivo | Link direto |
|---|---|---|
| Dashboards | `grupo-dashboards.png` | https://fabriciokaempf.github.io/VazPower/marca/grupo-dashboards.png |
| Tráfego e Leads | `grupo-trafego-leads.png` | https://fabriciokaempf.github.io/VazPower/marca/grupo-trafego-leads.png |

Ambos em 1024x1024.

## O detalhe que guiou o layout

O WhatsApp **recorta a foto do grupo em círculo**. Por isso toda a composição vive
dentro de uma zona segura de 80% do diâmetro, e cada linha de texto é medida contra
a corda do círculo naquela altura. Os cantos do quadrado são descartados no recorte,
então nada importante pode ficar neles.

## Ativos oficiais

Baixados de `vazpower.com.au` (tema do site), não recriados:

- `logo-marca.svg` · favicon do tema, traz a marca em **vetor** (nítida em qualquer tamanho)
- `marca-path.txt` · o path da marca extraído do SVG, já isolado
- `logo-wordmark.png` · wordmark em branco, fundo transparente, recortado do logo de rodapé
- `logo-completo.png` · lockup completo original (marca + wordmark)

## Gerar de novo ou criar variações

```
python3 gerar-avatares.py
```

As peças ficam definidas na lista `PECAS`, no fim do arquivo. Para um grupo novo,
basta acrescentar uma linha:

```python
PECAS = [("dashboards",    ["DASHBOARDS"]),
         ("trafego-leads", ["TRÁFEGO", "E LEADS"]),
         ("financeiro",    ["FINANCEIRO"])]
```

Rótulos curtos cabem em uma linha; os longos ficam melhores quebrados em duas.

Requer `playwright` disponível para o Node (usa Chromium para rasterizar).

## Tipografia

O rótulo usa **Outfit Bold** (licença OFL, incluída em `LICENCA-Outfit.txt`). O
wordmark não é tipografado: é o arquivo original da marca, para não haver risco de
divergir da fonte real usada pela Vaz.
