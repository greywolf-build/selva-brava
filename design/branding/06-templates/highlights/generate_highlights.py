#!/usr/bin/env python3
"""
Covers de highlights de Instagram — Selva Brava
================================================
Genera 8 covers 1080x1080 como sistema visual unificado:
palabra centrada en Barlow Condensed Bold (tracking +0.08em),
hairlines arriba/abajo (30% opacidad), textura papel + film grain
sutil y vignette suave. Todo dentro del círculo seguro de 900px.

Regenerar:  python3 generate_highlights.py
Colores:    paleta oficial (design/branding/02-color/paleta.md)
Tipografía: design/branding/03-typography/fonts/BarlowCondensed-Bold.ttf
"""
from PIL import Image, ImageDraw, ImageFont, ImageChops
import os

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(BASE, "..", "..", ".."))  # design/
FONT_PATH = os.path.join(ROOT, "branding", "03-typography", "fonts", "BarlowCondensed-Bold.ttf")
OUTPUT_DIR = BASE

CANVAS = 1080
TARGET_WIDTH = 0.50 * CANVAS   # la palabra ocupa ~50% del ancho (rango 45-55%)
TRACKING_EM = 0.08             # letter-spacing
HAIRLINE_HALF = 80             # línea de 160px (centro ± 80)
HAIRLINE_GAP_TOP = 64          # separación línea ↔ texto
HAIRLINE_GAP_BOTTOM = 52
HAIRLINE_ALPHA = 77            # 30% de 255

HIGHLIGHTS = [
    {"num": "01", "name": "manifiesto",  "text": "MANIFIESTO",  "bg": "#1E2523", "fg": "#F6F4EC"},
    {"num": "02", "name": "propiedades", "text": "PROPIEDADES", "bg": "#A9B59D", "fg": "#1E2523"},
    {"num": "03", "name": "producto",    "text": "PRODUCTO",    "bg": "#4C6759", "fg": "#FAF8F1"},
    {"num": "04", "name": "invierno",    "text": "INVIERNO",    "bg": "#687978", "fg": "#FAF8F1"},
    {"num": "05", "name": "historias",   "text": "HISTORIAS",   "bg": "#B97E6B", "fg": "#F6F4EC"},
    {"num": "06", "name": "ciencia",     "text": "CIENCIA",     "bg": "#FAF8F1", "fg": "#4C6759"},
    {"num": "07", "name": "comprar",     "text": "COMPRAR",     "bg": "#F6F4EC", "fg": "#1E2523"},
    # "forest green más suave" = Bosque 400 de la escalera oficial
    {"num": "08", "name": "comunidad",   "text": "COMUNIDAD",   "bg": "#687E71", "fg": "#FAF8F1"},
]


def hex_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def word_width(font, text, tracking_px):
    """Ancho total de la palabra con tracking entre letras."""
    d = ImageDraw.Draw(Image.new("L", (8, 8)))
    w = 0
    for i, ch in enumerate(text):
        bbox = d.textbbox((0, 0), ch, font=font)
        w += bbox[2] - bbox[0]
        if i < len(text) - 1:
            w += tracking_px
    return w


def fit_font(text):
    """Busca el cuerpo que deja la palabra en ~TARGET_WIDTH, con techo de
    128px para que palabras cortas no rompan la uniformidad del sistema."""
    lo, hi = 40, 128
    while hi - lo > 1:
        mid = (lo + hi) // 2
        f = ImageFont.truetype(FONT_PATH, mid)
        if word_width(f, text, TRACKING_EM * mid) <= TARGET_WIDTH:
            lo = mid
        else:
            hi = mid
    return ImageFont.truetype(FONT_PATH, lo)


def paper_texture(img, strength=0.30):
    """Grano de papel: ruido fino + manchas suaves de pulpa (overlay)."""
    s = img.size
    fine = Image.effect_noise(s, 16)
    fine = fine.point(lambda p: 128 + int((p - 128) * strength))
    img = ImageChops.overlay(img, Image.merge("RGB", (fine,) * 3))
    coarse = Image.effect_noise((s[0] // 8, s[1] // 8), 22).resize(s, Image.BILINEAR)
    coarse = coarse.point(lambda p: 128 + int((p - 128) * strength * 0.4))
    return ImageChops.overlay(img, Image.merge("RGB", (coarse,) * 3))


def film_grain(img, opacity=0.045):
    """Film grain global 3-5%."""
    noise = Image.effect_noise(img.size, 34)
    grain = Image.merge("RGB", (noise,) * 3)
    return Image.blend(img, ImageChops.overlay(img, grain), opacity * 3)


def vignette(img, opacity=0.07):
    """Oscurecido radial suave hacia los bordes (5-10%)."""
    s = 270  # máscara chica reescalada = falloff suave
    m = Image.new("L", (s, s), 0)
    d = ImageDraw.Draw(m)
    cx = s / 2
    steps = 90
    for i in range(steps):
        r = cx * (1 - i / steps)
        a = int(255 * (i / steps))
        d.ellipse([cx - r, cx - r, cx + r, cx + r], fill=a)
    m = m.resize(img.size, Image.BILINEAR)
    inv = m.point(lambda p: int((255 - p) * opacity))
    black = Image.new("RGB", img.size, (0, 0, 0))
    return Image.composite(img, black, inv.point(lambda p: 255 - p))


ISOTIPO_SVG = os.path.join(ROOT, "branding", "01-logo", "isotipo",
                           "variantes", "isotipo_original.svg")
ISOTIPO_D = 1000       # diámetro: enmarca el recorte circular de IG (1080)
ISOTIPO_ALPHA = 0.30   # tono sobre tono, marca de agua


def isotipo_layer(fg_hex, size=ISOTIPO_D):
    """Isotipo recoloreado al color del texto, como marca de agua."""
    import subprocess, tempfile
    svg = open(ISOTIPO_SVG).read()
    svg = svg.replace("#687978", fg_hex).replace("#BBC6AA", fg_hex)
    with tempfile.NamedTemporaryFile("w", suffix=".svg", delete=False) as f:
        f.write(svg); tmp = f.name
    png = tmp + ".png"
    subprocess.run(["rsvg-convert", "-w", str(size), "-h", str(size), tmp, "-o", png],
                   check=True)
    im = Image.open(png).convert("RGBA")
    a = im.getchannel("A").point(lambda p: int(p * ISOTIPO_ALPHA))
    im.putalpha(a)
    os.unlink(tmp); os.unlink(png)
    return im


def create_cover(cfg):
    bg, fg = hex_rgb(cfg["bg"]), hex_rgb(cfg["fg"])
    img = Image.new("RGB", (CANVAS, CANVAS), bg)
    img = paper_texture(img)
    # isotipo centrado — su anillo queda justo dentro del círculo visible
    iso = isotipo_layer(cfg["fg"])
    img = img.convert("RGBA")
    img.alpha_composite(iso, ((CANVAS - ISOTIPO_D) // 2, (CANVAS - ISOTIPO_D) // 2))
    img = img.convert("RGB")

    # capa RGBA para texto + hairlines (las líneas llevan alpha)
    layer = Image.new("RGBA", (CANVAS, CANVAS), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)

    text = cfg["text"]
    font = fit_font(text)
    tracking = TRACKING_EM * font.size

    # centrado vertical por caja visual de la palabra completa
    ref = d.textbbox((0, 0), text, font=font)
    text_h = ref[3] - ref[1]
    y_draw = (CANVAS - text_h) // 2 - ref[1]

    # dibujar letra por letra con tracking
    total_w = word_width(font, text, tracking)
    x = (CANVAS - total_w) / 2
    for i, ch in enumerate(text):
        b = d.textbbox((0, 0), ch, font=font)
        d.text((x - b[0], y_draw), ch, font=font, fill=fg + (255,))
        x += (b[2] - b[0]) + (tracking if i < len(text) - 1 else 0)

    # hairlines arriba y abajo (30% opacidad, 160px)
    top_y = (CANVAS - text_h) // 2 - HAIRLINE_GAP_TOP
    bot_y = (CANVAS + text_h) // 2 + HAIRLINE_GAP_BOTTOM
    for ly in (top_y, bot_y):
        d.line(
            [(CANVAS // 2 - HAIRLINE_HALF, ly), (CANVAS // 2 + HAIRLINE_HALF, ly)],
            fill=fg + (HAIRLINE_ALPHA,), width=2,
        )

    img = Image.alpha_composite(img.convert("RGBA"), layer).convert("RGB")
    img = film_grain(img)
    img = vignette(img)

    path = os.path.join(OUTPUT_DIR, f"highlight_{cfg['num']}_{cfg['name']}.png")
    img.save(path, "PNG")
    print(f"✓ {os.path.basename(path)}  (font {font.size}px)")
    return path


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    import sys
    only = sys.argv[1:] if len(sys.argv) > 1 else None
    for cfg in HIGHLIGHTS:
        if only and cfg["name"] not in only:
            continue
        create_cover(cfg)
