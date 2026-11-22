#!/usr/bin/env python3
"""Generate local SVG product illustrations, logo and favicon."""
from pathlib import Path

IMG = Path("/workspace/bryan-demo/img")
IMG.mkdir(parents=True, exist_ok=True)


def svg(inner, w=400, h=480):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" fill="none">
{inner}
</svg>
'''


def bg(c1, c2, w=400, h=480):
    return f'''  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{c1}"/>
      <stop offset="100%" stop-color="{c2}"/>
    </linearGradient>
    <linearGradient id="shine" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#fff" stop-opacity="0"/>
      <stop offset="35%" stop-color="#fff" stop-opacity=".18"/>
      <stop offset="70%" stop-color="#fff" stop-opacity="0"/>
    </linearGradient>
    <filter id="s" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#000" flood-opacity=".45"/>
    </filter>
  </defs>
  <rect width="{w}" height="{h}" rx="0" fill="url(#bg)"/>
  <ellipse cx="200" cy="430" rx="110" ry="16" fill="#000" opacity=".28"/>
'''


def longneck(filename, glass, liquid, label, label2, cap, text, sub, text_color="#f6ecda"):
    # glass bottle 330ml long neck
    inner = bg("#1c1510", "#0e0b08") + f'''
  <g filter="url(#s)" transform="translate(0,-8)">
    <!-- cap -->
    <rect x="178" y="42" width="44" height="28" rx="4" fill="{cap}"/>
    <rect x="176" y="66" width="48" height="8" rx="2" fill="{cap}" opacity=".85"/>
    <!-- neck -->
    <path d="M186 74h28v62c0 8-4 14-14 14s-14-6-14-14V74Z" fill="{glass}" opacity=".95"/>
    <path d="M190 74h8v70" stroke="url(#shine)" stroke-width="6"/>
    <!-- shoulder + body -->
    <path d="M186 148c-28 18-48 42-50 72v128c0 16 14 28 64 28s64-12 64-28V220c-2-30-22-54-50-72"
          fill="{glass}"/>
    <!-- liquid -->
    <path d="M140 228c2-24 18-44 40-58 22 14 38 34 40 58v116c0 12-12 22-60 22s-60-10-60-22V228Z"
          fill="{liquid}" opacity=".88"/>
    <path d="M156 200c0 0 8 40 8 100" stroke="url(#shine)" stroke-width="10" opacity=".5"/>
    <!-- label -->
    <rect x="132" y="268" width="136" height="86" rx="6" fill="{label}"/>
    <rect x="132" y="268" width="136" height="8" fill="{label2}"/>
    <rect x="132" y="346" width="136" height="8" fill="{label2}"/>
    <text x="200" y="312" text-anchor="middle" font-family="Georgia, serif" font-size="15" font-weight="700" fill="{text_color}">{text}</text>
    <text x="200" y="332" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" letter-spacing="1.5" fill="{text_color}" opacity=".8">{sub}</text>
  </g>
'''
    (IMG / filename).write_text(svg(inner), encoding="utf-8")


def can(filename, body, top, accent, text, sub, text_color="#fff"):
    inner = bg("#1a1410", "#0c0a08") + f'''
  <g filter="url(#s)" transform="translate(0,-4)">
    <rect x="132" y="96" width="136" height="268" rx="28" fill="{body}"/>
    <rect x="132" y="96" width="136" height="28" rx="14" fill="{top}"/>
    <rect x="132" y="112" width="136" height="14" fill="{top}" opacity=".9"/>
    <ellipse cx="200" cy="96" rx="68" ry="16" fill="{top}"/>
    <ellipse cx="200" cy="90" rx="36" ry="8" fill="#2a2a2a"/>
    <ellipse cx="200" cy="88" rx="22" ry="5" fill="#444"/>
    <rect x="132" y="200" width="136" height="96" fill="{accent}"/>
    <path d="M148 120c0 0 10 80 10 200" stroke="url(#shine)" stroke-width="12" opacity=".45"/>
    <text x="200" y="248" text-anchor="middle" font-family="Arial Black, Arial, sans-serif" font-size="16" font-weight="700" fill="{text_color}">{text}</text>
    <text x="200" y="268" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" letter-spacing="2" fill="{text_color}" opacity=".85">{sub}</text>
    <ellipse cx="200" cy="364" rx="68" ry="14" fill="{body}"/>
    <path d="M132 350c8 14 36 22 68 22s60-8 68-22" fill="{body}" opacity=".8"/>
  </g>
'''
    (IMG / filename).write_text(svg(inner), encoding="utf-8")


def bottle600(filename, glass, liquid, foil, label, text, sub, text_color="#f6ecda"):
    inner = bg("#1b140f", "#0d0a08") + f'''
  <g filter="url(#s)" transform="translate(0,-6)">
    <rect x="178" y="36" width="44" height="22" rx="3" fill="{foil}"/>
    <path d="M184 58h32v50c0 6-4 12-16 12s-16-6-16-12V58Z" fill="{glass}"/>
    <path d="M184 108c-32 22-54 54-56 88v168c0 18 16 30 72 30s72-12 72-30V196c-2-34-24-66-56-88"
          fill="{glass}"/>
    <path d="M134 214c3-30 22-56 50-74 28 18 47 44 50 74v146c0 14-14 24-66 24s-66-10-66-24V214Z"
          fill="{liquid}" opacity=".9"/>
    <rect x="172" y="58" width="20" height="48" fill="url(#shine)" opacity=".4"/>
    <path d="M150 190c0 0 10 50 10 140" stroke="url(#shine)" stroke-width="10" opacity=".4"/>
    <!-- foil wrap at neck -->
    <path d="M184 100c-8 8-12 16-14 24h60c-2-8-6-16-14-24H184Z" fill="{foil}" opacity=".85"/>
    <rect x="128" y="268" width="144" height="80" rx="4" fill="{label}"/>
    <text x="200" y="304" text-anchor="middle" font-family="Georgia, serif" font-size="18" font-weight="700" fill="{text_color}">{text}</text>
    <text x="200" y="326" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" letter-spacing="2" fill="{text_color}" opacity=".8">{sub}</text>
  </g>
'''
    (IMG / filename).write_text(svg(inner), encoding="utf-8")


def spirits(filename, glass, liquid, cap, label, accent, text, sub, text_color="#f6ecda"):
    inner = bg("#16120f", "#0b0907") + f'''
  <g filter="url(#s)" transform="translate(0,-4)">
    <rect x="176" y="32" width="48" height="26" rx="5" fill="{cap}"/>
    <rect x="172" y="54" width="56" height="8" rx="2" fill="{cap}" opacity=".8"/>
    <path d="M186 62h28v78c0 6-3 10-14 10s-14-4-14-10V62Z" fill="{glass}" opacity=".7"/>
    <path d="M186 148c-30 14-52 40-54 70v156c0 16 14 28 68 28s68-12 68-28V218c-2-30-24-56-54-70"
          fill="{glass}" opacity=".55"/>
    <path d="M138 230c2-22 18-44 46-58 28 14 44 36 46 58v140c0 12-12 22-62 22s-62-10-62-22V230Z"
          fill="{liquid}" opacity=".55"/>
    <rect x="190" y="70" width="8" height="70" fill="#fff" opacity=".18"/>
    <path d="M152 200c0 0 8 50 8 140" stroke="#fff" stroke-width="8" opacity=".12"/>
    <rect x="126" y="268" width="148" height="92" rx="3" fill="{label}"/>
    <rect x="126" y="268" width="148" height="7" fill="{accent}"/>
    <rect x="126" y="353" width="148" height="7" fill="{accent}"/>
    <text x="200" y="312" text-anchor="middle" font-family="Georgia, serif" font-size="16" font-weight="700" fill="{text_color}">{text}</text>
    <text x="200" y="334" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" letter-spacing="1.6" fill="{text_color}" opacity=".8">{sub}</text>
  </g>
'''
    (IMG / filename).write_text(svg(inner), encoding="utf-8")


def wine(filename, glass, liquid, foil, label, text, sub, text_color="#f6ecda"):
    inner = bg("#17110f", "#0b0807") + f'''
  <g filter="url(#s)" transform="translate(0,-8)">
    <rect x="182" y="28" width="36" height="18" rx="2" fill="{foil}"/>
    <path d="M188 46h24v110c0 4-2 8-12 8s-12-4-12-8V46Z" fill="{glass}" opacity=".7"/>
    <rect x="186" y="46" width="28" height="50" fill="{foil}" opacity=".9"/>
    <path d="M188 164c-36 28-58 70-58 110v100c0 18 18 30 70 30s70-12 70-30V274c0-40-22-82-58-110"
          fill="{glass}" opacity=".55"/>
    <path d="M136 280c2-36 20-70 48-94 28 24 46 58 48 94v90c0 14-14 24-64 24s-64-10-64-24v-90Z"
          fill="{liquid}" opacity=".85"/>
    <path d="M198 50v110" stroke="#fff" stroke-width="5" opacity=".15"/>
    <path d="M150 250c0 0 8 40 8 110" stroke="#fff" stroke-width="8" opacity=".1"/>
    <rect x="138" y="300" width="124" height="78" rx="3" fill="{label}"/>
    <text x="200" y="334" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="700" fill="{text_color}">{text}</text>
    <text x="200" y="354" text-anchor="middle" font-family="Arial, sans-serif" font-size="9" letter-spacing="1.2" fill="{text_color}" opacity=".8">{sub}</text>
  </g>
'''
    (IMG / filename).write_text(svg(inner), encoding="utf-8")


def pet2l(filename, liquid, cap, label, text, sub, text_color="#fff"):
    inner = bg("#171412", "#0c0a08") + f'''
  <g filter="url(#s)">
    <rect x="176" y="40" width="48" height="22" rx="6" fill="{cap}"/>
    <path d="M184 62h32c6 16 10 28 12 44H172c2-16 6-28 12-44Z" fill="#d9e2e8" opacity=".35"/>
    <path d="M168 106h64c8 16 16 48 18 90v140c0 20-14 36-50 36s-50-16-50-36V196c2-42 10-74 18-90Z"
          fill="#d9e2e8" opacity=".28"/>
    <path d="M172 200c2-40 8-70 16-88h40c8 18 14 48 16 88v128c0 16-12 28-36 28s-36-12-36-28V200Z"
          fill="{liquid}" opacity=".85"/>
    <path d="M186 120c0 0 8 60 8 180" stroke="#fff" stroke-width="10" opacity=".18"/>
    <rect x="150" y="230" width="100" height="110" rx="6" fill="{label}"/>
    <text x="200" y="280" text-anchor="middle" font-family="Arial Black, Arial, sans-serif" font-size="15" font-weight="700" fill="{text_color}">{text}</text>
    <text x="200" y="302" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" letter-spacing="1.4" fill="{text_color}" opacity=".85">{sub}</text>
  </g>
'''
    (IMG / filename).write_text(svg(inner), encoding="utf-8")


def bag(filename, body, accent, icon_paths, text, sub, text_color="#f6ecda"):
    inner = bg("#1a1510", "#0c0a08") + f'''
  <g filter="url(#s)">
    <path d="M118 150c0-18 10-36 42-48 12-20 28-32 40-32s28 12 40 32c32 12 42 30 42 48v200c0 20-16 36-82 36s-82-16-82-36V150Z"
          fill="{body}"/>
    <path d="M160 110c8-18 22-28 40-28s32 10 40 28" stroke="{accent}" stroke-width="6" fill="none" stroke-linecap="round"/>
    <rect x="118" y="200" width="164" height="150" fill="{accent}" opacity=".92"/>
    {icon_paths}
    <text x="200" y="310" text-anchor="middle" font-family="Arial Black, Arial, sans-serif" font-size="20" font-weight="700" fill="{text_color}">{text}</text>
    <text x="200" y="334" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" letter-spacing="2" fill="{text_color}" opacity=".85">{sub}</text>
    <path d="M140 170c0 0 12 20 12 50" stroke="#fff" stroke-width="10" opacity=".12"/>
  </g>
'''
    (IMG / filename).write_text(svg(inner), encoding="utf-8")


def combo(filename, title, sub, swatches):
    boxes = []
    x = 108
    for color, label in swatches:
        boxes.append(f'''
    <g>
      <rect x="{x}" y="168" width="56" height="86" rx="8" fill="{color}"/>
      <text x="{x+28}" y="218" text-anchor="middle" font-family="Arial, sans-serif" font-size="8" fill="#fff" opacity=".9">{label}</text>
    </g>''')
        x += 64
    inner = bg("#1c150e", "#0e0a07") + f'''
  <g filter="url(#s)">
    <rect x="86" y="120" width="228" height="250" rx="18" fill="#2a1c10"/>
    <rect x="86" y="120" width="228" height="44" rx="18" fill="#c4841d"/>
    <rect x="86" y="148" width="228" height="16" fill="#c4841d"/>
    <text x="200" y="148" text-anchor="middle" font-family="Georgia, serif" font-size="16" font-weight="700" fill="#1a1208">COMBO</text>
    {''.join(boxes)}
    <text x="200" y="300" text-anchor="middle" font-family="Georgia, serif" font-size="18" font-weight="700" fill="#f6ecda">{title}</text>
    <text x="200" y="324" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="#c4b7a1">{sub}</text>
    <rect x="120" y="344" width="160" height="8" rx="4" fill="#e8a84a" opacity=".5"/>
  </g>
'''
    (IMG / filename).write_text(svg(inner), encoding="utf-8")


# ---- products ----
longneck("heineken.svg", "#1a5c38", "#0e3d24", "#0a2e1c", "#c9a227", "#1a1a1a", "HEINEKEN", "LONG NECK 330ml")
longneck("corona.svg", "#c8e4d0", "#f2f7e8", "#0055a5", "#f2c94c", "#f2c94c", "CORONA", "EXTRA 330ml", "#08315a")
longneck("stella.svg", "#dce6ea", "#b9c4c8", "#1a1a1a", "#c9a227", "#1a1a1a", "STELLA", "ARTOIS 330ml")

can("brahma.svg", "#c4161c", "#8e0f14", "#f0d78c", "BRAHMA", "DUPLO MALTE", "#3a1a00")
can("skol.svg", "#efc400", "#c9a200", "#1a1a1a", "SKOL", "PILSEN", "#fff8d6")
can("spaten.svg", "#1a1a1a", "#111", "#c9a227", "SPATEN", "PURO MALTE")
can("redbull.svg", "#003087", "#001e55", "#ed1c24", "RED BULL", "250 ml")
can("monster.svg", "#111111", "#0a0a0a", "#78be20", "MONSTER", "ENERGY 473ml")
can("tnt.svg", "#1a1a1a", "#111", "#ff3b00", "TNT", "ENERGY 473ml")

bottle600("original.svg", "#5a3310", "#3d220a", "#c9a227", "#6b1d12", "ORIGINAL", "600 ml")

spirits("smirnoff.svg", "#e8eef2", "#d5dde3", "#c0c6cc", "#b00", "#fff", "SMIRNOFF", "VODKA 998ml", "#4a0000")
spirits("jack.svg", "#5a2e10", "#3e1e0a", "#1a1a1a", "#1a1a1a", "#c9a227", "JACK DANIEL'S", "OLD NO.7  1L")
spirits("cachaca51.svg", "#e8eef0", "#d0d8dc", "#c4161c", "#c4161c", "#fff", "PITU? 51", "CACHAÇA 965ml")  # fix text
spirits("tanqueray.svg", "#e8eef0", "#d4dde0", "#0b3d2e", "#0b3d2e", "#c9a227", "TANQUERAY", "LONDON DRY 750ml")

wine("casillero.svg", "#4a1020", "#5a1224", "#8a0f1a", "#6b1020", "CASILLERO", "CABERNET 750ml")
wine("miolo.svg", "#3a1218", "#4a1820", "#7a1a28", "#4a1820", "MIOLO", "SELEÇÃO TINTO")
wine("salton.svg", "#e8e6d8", "#f3f0de", "#c9a227", "#f4efe0", "SALTON", "CHARDONNAY", "#5a4a20")

pet2l("coca.svg", "#6b0008", "#c4161c", "#c4161c", "Coca-Cola", "2 litros")
pet2l("guarana.svg", "#0d5c2e", "#0a4a24", "#0d5c2e", "GUARANÁ", "ANTARCTICA 2L")
pet2l("crystal.svg", "#b9d8ee", "#1a7aad", "#1a7aad", "CRYSTAL", "ÁGUA 1,5L")

ice_icon = '''<circle cx="168" cy="248" r="10" fill="#fff" opacity=".7"/>
    <circle cx="188" cy="242" r="8" fill="#fff" opacity=".55"/>
    <circle cx="178" cy="260" r="7" fill="#fff" opacity=".5"/>
    <rect x="210" y="236" width="22" height="22" rx="3" transform="rotate(20 221 247)" fill="#fff" opacity=".55"/>'''
bag("gelo.svg", "#3a6a8a", "#1e4e6e", ice_icon, "GELO", "CUBOS 5 kg")

coal_icon = '''<circle cx="176" cy="250" r="11" fill="#2a2a2a"/>
    <circle cx="194" cy="246" r="9" fill="#1a1a1a"/>
    <circle cx="186" cy="262" r="10" fill="#333"/>
    <circle cx="208" cy="256" r="8" fill="#222"/>'''
bag("carvao.svg", "#3a3028", "#2a241e", coal_icon, "CARVÃO", "VEGETAL 4 kg")

combo("combo-churras.svg", "Combo Churras", "12 latas + gelo + carvão",
      [("#efc400", "Skol"), ("#3a6a8a", "Gelo"), ("#3a3028", "Carvão")])
combo("kit-heineken.svg", "Kit Heineken", "6 long necks 330ml",
      [("#1a5c38", "330"), ("#1a5c38", "330"), ("#1a5c38", "330")])

# fix cachaça 51 label — rewrite file with correct text
spirits("cachaca51.svg", "#e8eef0", "#d0d8dc", "#c4161c", "#c4161c", "#fff", "51", "CACHAÇA 965ml")

# Logo
logo = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64" fill="none">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#f3c16b"/>
      <stop offset="100%" stop-color="#c4841d"/>
    </linearGradient>
  </defs>
  <circle cx="32" cy="32" r="30" fill="#1a120c" stroke="url(#g)" stroke-width="2.4"/>
  <path d="M26 16h12l-1.2 8.5c6.4 3.2 10.2 9.4 10.2 16.6 0 8.4-6.4 14.2-16.9 14.2S13.4 49.5 13.4 41.1c0-7.2 3.8-13.4 10.2-16.6L22.4 16H26Z" fill="url(#g)" opacity=".15" stroke="url(#g)" stroke-width="1.8" stroke-linejoin="round"/>
  <path d="M24.8 41.2c0-6.2 3.6-10.2 7.2-12.2 3.6 2 7.2 6 7.2 12.2 0 4.8-3 7.6-7.2 7.6s-7.2-2.8-7.2-7.6Z" fill="url(#g)"/>
  <path d="M30 16.5h4v7h-4z" fill="url(#g)"/>
  <circle cx="32" cy="24.5" r="1.4" fill="#f6ecda"/>
</svg>
'''
(IMG / "logo.svg").write_text(logo, encoding="utf-8")

# Favicon (same, 32)
(IMG / "favicon.svg").write_text(logo.replace('width="64" height="64"', 'width="32" height="32"'), encoding="utf-8")

print("Generated", len(list(IMG.glob('*.svg'))), "svg files")
for p in sorted(IMG.glob("*.svg")):
    print(" ", p.name, p.stat().st_size)
