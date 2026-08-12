#!/usr/bin/env python3
"""
Avatares de grupo do WhatsApp para a Vaz Power.
Agora com os ATIVOS OFICIAIS da marca, baixados de vazpower.com.au:
  - marca: path vetorial do favicon.svg do tema (nitido em qualquer tamanho)
  - wordmark: recorte de VazPower_logo_footer.webp (branco, fundo transparente)

Restricao critica: o WhatsApp recorta a foto do grupo em CIRCULO.
Toda a composicao vive dentro de uma zona segura de raio 0.40 do lado.
"""
import base64, json, os, subprocess

AQUI = os.path.dirname(os.path.abspath(__file__))
ATIVOS = AQUI            # ativos oficiais versionados nesta pasta
S = 1024
CX = CY = S / 2
R_SEGURO = S * 0.40

INDIGO_TOP, INDIGO_BOT, INDIGO_DEEP = "#453B8C", "#332B6B", "#241E4E"
LARANJA, TIJOLO, BRASA = "#F58220", "#E4502D", "#D3381C"

# --- ativos ---
PATH_MARCA = open(os.path.join(ATIVOS, "marca-path.txt")).read().strip()
BB = {"x": -97.46, "y": 0.0, "w": 328.60, "h": 250.14}   # bbox medido no navegador
TX, TY = 189, 118                                         # transform original
RAZAO = BB["w"] / BB["h"]

WORDMARK = base64.b64encode(open(os.path.join(ATIVOS, "logo-wordmark.png"), "rb").read()).decode()
WM_RAZAO = 267 / 85

fonts = {"OutfitBold": base64.b64encode(
    open(os.path.join(AQUI, "Outfit-Bold.ttf"), "rb").read()).decode()}


def corda(dy):
    dy = min(abs(dy), R_SEGURO)
    return (R_SEGURO ** 2 - dy ** 2) ** 0.5


def marca(cx, cy, h):
    """Marca oficial em vetor, reescalada e recolorida com o gradiente da casa."""
    w = h * RAZAO
    k = h / BB["h"]
    # leva o bbox para a origem, escala, e reposiciona centralizado
    x = cx - w / 2 - (BB["x"] + TX) * k
    y = cy - h / 2 - (BB["y"] + TY) * k
    return f'''  <g transform="translate({x:.2f},{y:.2f}) scale({k:.5f})">
    <path transform="translate({TX},{TY})" d="{PATH_MARCA}" fill="url(#calor)"/>
  </g>'''


def rotulo(linhas, y_topo, fs):
    CAP = 0.72
    out, y = [], y_topo + fs * CAP
    for txt in linhas:
        esp = 5 if len(txt) <= 9 else 3
        out.append(f'<text x="{CX}" y="{y:.0f}" text-anchor="middle" font-family="OutfitBold" '
                   f'font-size="{fs}" letter-spacing="{esp}" fill="#FFFFFF">{txt}</text>')
        y += fs * 0.96
    return "\n  ".join(out)


def svg(linhas):
    duas = len(linhas) > 1
    fs = 78 if duas else 84
    acento = any(c in "ÁÉÍÓÚÂÊÔÃÕÀÇ" for l in linhas for c in l)

    h_marca = 150
    topo = CY - (266 if duas else 240)

    y_wm_topo = topo + h_marca + 52          # topo do wordmark
    wm_w = 300
    wm_h = wm_w / WM_RAZAO
    y_regua = y_wm_topo + wm_h + 38
    y_rot = y_regua + 38 + (fs * 0.21 if acento else 0)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{S}" height="{S}" viewBox="0 0 {S} {S}">
  <style>
    @font-face {{ font-family:'OutfitBold'; src:url(data:font/ttf;base64,{fonts['OutfitBold']}); }}
  </style>
  <defs>
    <linearGradient id="campo" x1="0" y1="0" x2="0.35" y2="1">
      <stop offset="0%" stop-color="{INDIGO_TOP}"/><stop offset="100%" stop-color="{INDIGO_BOT}"/>
    </linearGradient>
    <linearGradient id="calor" x1="0" y1="0" x2="0.85" y2="1">
      <stop offset="0%" stop-color="{LARANJA}"/>
      <stop offset="55%" stop-color="{TIJOLO}"/>
      <stop offset="100%" stop-color="{BRASA}"/>
    </linearGradient>
    <radialGradient id="vinheta" cx="50%" cy="42%" r="70%">
      <stop offset="52%" stop-color="{INDIGO_DEEP}" stop-opacity="0"/>
      <stop offset="100%" stop-color="{INDIGO_DEEP}" stop-opacity="0.66"/>
    </radialGradient>
    <pattern id="sedimento" width="12" height="12" patternUnits="userSpaceOnUse">
      <rect width="12" height="1" fill="#FFFFFF" fill-opacity="0.03"/>
    </pattern>
  </defs>

  <rect width="{S}" height="{S}" fill="url(#campo)"/>
  <rect width="{S}" height="{S}" fill="url(#sedimento)"/>
  <rect width="{S}" height="{S}" fill="url(#vinheta)"/>

{marca(CX, topo + h_marca / 2, h_marca)}

  <image x="{CX - wm_w/2:.0f}" y="{y_wm_topo:.0f}" width="{wm_w}" height="{wm_h:.0f}"
         href="data:image/png;base64,{WORDMARK}"/>

  <line x1="{CX - 58}" y1="{y_regua:.0f}" x2="{CX + 58}" y2="{y_regua:.0f}"
        stroke="{TIJOLO}" stroke-width="3" stroke-linecap="round"/>

  {rotulo(linhas, y_rot, fs)}
</svg>"""


PECAS = [("dashboards", ["DASHBOARDS"]),
         ("trafego-leads", ["TRÁFEGO", "E LEADS"])]

alvos = []
for slug, linhas in PECAS:
    p = os.path.join(AQUI, f"grupo-{slug}.svg")
    open(p, "w", encoding="utf-8").write(svg(linhas))
    alvos.append([p, os.path.join(AQUI, f"grupo-{slug}.png")])

js = os.path.join(AQUI, "_r.cjs")
open(js, "w").write(f"""
const {{ chromium }} = require('/opt/node22/lib/node_modules/playwright');
(async () => {{
  const b = await chromium.launch({{ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' }});
  for (const [src, out] of {json.dumps(alvos)}) {{
    const p = await b.newPage({{ viewport: {{ width: {S}, height: {S} }}, deviceScaleFactor: 1 }});
    await p.goto('file://' + src, {{ waitUntil: 'networkidle' }});
    await p.screenshot({{ path: out }});
    await p.close();
    console.log('png:', out.split('/').pop());
  }}
  await b.close();
}})();
""")
subprocess.run(["node", js], check=True)
os.remove(js)
