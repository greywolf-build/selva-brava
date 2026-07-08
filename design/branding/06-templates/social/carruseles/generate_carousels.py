#!/usr/bin/env python3
"""
Carruseles de Instagram — templates Selva Brava
================================================
Slides 1080x1350 (vertical, máximo alcance en feed) generados con el mismo
motor visual de las stories: paleta oficial, Barlow Condensed / Barlow /
Space Mono, textura papel + grano + vignette.

Cromática de carrusel: contador "01 — 05" arriba a la derecha, flecha de
swipe abajo a la derecha (menos en el último slide), "deslizá" solo en el
cover. Regla de marca: un mismo look por serie.

4 templates (uno por pilar de contenido):
  01-mito-real      → educación honesta (mito vs. realidad + dato)
  02-ingrediente    → ficha apothecary de un ingrediente (ej: cúrcuma)
  03-producto       → propiedades del Sunscreen SPF 60 + CTA
  04-manifiesto     → serie de quotes de filosofía

Regenerar:  python3 generate_carousels.py [template ...]
Duplicar un template: copiar su bloque en CAROUSELS, cambiar copy y regenerar.
"""
import os, sys, importlib.util
from PIL import Image, ImageDraw

BASE = os.path.dirname(os.path.abspath(__file__))
HL = os.path.abspath(os.path.join(BASE, "..", "..", "highlights"))

# importar el motor de stories
spec_ = importlib.util.spec_from_file_location("gs", os.path.join(HL, "generate_stories.py"))
gs = importlib.util.module_from_spec(spec_); spec_.loader.exec_module(gs)

# reconfigurar el lienzo para formato post vertical
gs.W, gs.H = 1080, 1350
gs.SAFE_TOP, gs.SAFE_BOTTOM = 170, 210
gs.OUT = BASE

C, F = gs.C, gs.F
PROJ = gs.PROJ
INV = os.path.join(PROJ, "invierno2026")
TIN = os.path.join(PROJ, "web", "src", "assets", "images", "producto.webp")


def slide_chrome(path, idx, total, fg_hex, cover=False):
    """Contador + flecha de swipe sobre el slide ya renderizado."""
    img = Image.open(path).convert("RGBA")
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    fg = gs.rgb(fg_hex)
    W, H = img.size
    # contador arriba derecha
    f = gs.font("mono", 26)
    txt = f"{idx:02d} — {total:02d}"
    w = d.textbbox((0, 0), txt, font=f)[2]
    d.text((W - 90 - w, 84), txt, font=f, fill=fg + (200,))
    # flecha de swipe (no en el último)
    if idx < total:
        y = H - 120; x1 = W - 200; x2 = W - 96
        d.line([(x1, y), (x2, y)], fill=fg + (220,), width=3)
        d.line([(x2 - 18, y - 12), (x2, y), (x2 - 18, y + 12)], fill=fg + (220,), width=3)
        if cover:
            f2 = gs.font("mono", 22)
            lbl = "DESLIZÁ"
            w2 = gs.tracked_w(f2, lbl, 22 * 0.2)
            gs.draw_tracked(d, x1 + (x2 - x1) / 2 - 6, y - 46, lbl, f2, fg + (200,), 22 * 0.2)
    out = Image.alpha_composite(img, layer).convert("RGB")
    out.save(path, "PNG")


def build(template):
    total = len(template["slides"])
    for i, s in enumerate(template["slides"], 1):
        s = dict(s)
        s["file"] = os.path.join(template["name"], f"{i:02d}.png")
        gs.make_story(s)
        slide_chrome(os.path.join(BASE, s["file"]), i, total,
                     s.get("fg", C["hueso"]), cover=(i == 1))


# ═════════════════════════ TEMPLATES ═════════════════════════════

CAROUSELS = [

# ── 01 · EDUCACIÓN HONESTA — mito vs. real ───────────────────────
{"name": "01-mito-real", "slides": [
  {"bg": C["crema"], "fg": C["carbon"], "accent": C["bosque"], "blocks": [
    ("eyebrow", "Educación honesta"), ("gap", 50),
    ("title", "¿El sol es\nel enemigo?", 120), ("gap", 50),
    ("body", "Spoiler: no. Pero lo que te ponés para protegerte, tal vez sí.", 42, 760),
  ]},
  {"bg": C["crema"], "fg": C["carbon"], "accent": C["terra"], "blocks": [
    ("eyebrow", "El mito"), ("gap", 50),
    ("title", "“Cualquier protector\nsirve, son todos\niguales”", 88), ("gap", 50),
    ("body", "La mayoría de los protectores comerciales usan filtros químicos sintéticos que tu piel absorbe — y que el agua se lleva al mar.", 40, 800),
  ]},
  {"bg": C["crema"], "fg": C["carbon"], "accent": C["bosque"], "blocks": [
    ("eyebrow", "Lo real"), ("gap", 50),
    ("title", "Filtro mineral:\nbarrera física,\nno química", 88), ("gap", 50),
    ("body", "El óxido de zinc y el dióxido de titanio no se absorben: quedan sobre la piel y reflejan la radiación. Protección que se entiende.", 40, 800),
  ]},
  {"bg": C["bosque"], "fg": C["hueso"], "accent": C["salvia"], "blocks": [
    ("eyebrow", "El dato"), ("gap", 50),
    ("title", "90%", 200), ("gap", 20),
    ("body", "de los protectores solares comerciales terminan en el océano. Nosotros no queremos ser parte de esa estadística.", 40, 780),
    ("gap", 40), ("mono", ["REEF SAFE · SIN FILTROS SINTÉTICOS"], 26),
  ]},
  {"bg": C["carbon"], "fg": C["crema"], "accent": C["salvia"], "blocks": [
    ("eyebrow", "Selva Brava"), ("gap", 50),
    ("title", "Pensá por\nvos mismo.", 110), ("gap", 50),
    ("body", "Leé la etiqueta de tu protector. Toda la nuestra está en nuestro perfil — todos los ingredientes, sin resúmenes.", 40, 760),
    ("gap", 40), ("mono", ["@SELVA.BRAVA"], 30),
  ]},
]},

# ── 02 · INGREDIENTE — ficha apothecary (ej: cúrcuma) ────────────
{"name": "02-ingrediente", "slides": [
  {"photo": os.path.join(INV, "turmeric.png"), "ov": .40, "bg": C["carbon"], "fg": C["hueso"], "accent": C["salvia"], "blocks": [
    ("eyebrow", "Ingrediente · 01"), ("gap", 50),
    ("title", "Cúrcuma", 140), ("gap", 30),
    ("mono", ["CURCUMA LONGA ROOT POWDER"], 28),
  ]},
  {"bg": C["hueso"], "fg": C["bosque700"], "accent": C["terra"], "blocks": [
    ("eyebrow", "Qué hace acá"), ("gap", 50),
    ("title", "El color beige\nsale de acá", 92), ("gap", 50),
    ("body", "No usamos colorantes: el tono natural del producto es infusión de cúrcuma orgánica. Acondicionador de la piel, de raíz.", 40, 780),
  ]},
  {"bg": C["hueso"], "fg": C["bosque700"], "accent": C["terra"], "blocks": [
    ("eyebrow", "En la fórmula"), ("gap", 60),
    ("mono", ["CURCUMA LONGA ROOT POWDER", "", "FUNCIÓN: ACONDICIONADOR", "DECLARADA ANTE ANMAT"], 32),
    ("gap", 50),
    ("body", "Cada ingrediente está declarado ante ANMAT y cumple una función. Nada de relleno.", 40, 740),
  ]},
  {"bg": C["carbon"], "fg": C["crema"], "accent": C["salvia"], "blocks": [
    ("eyebrow", "La fórmula completa"), ("gap", 50),
    ("title", "10 ingredientes.\nNada más.", 96), ("gap", 50),
    ("body", "Está entera en nuestra destacada CIENCIA — con ensayos de laboratorio.", 40, 740),
    ("gap", 40), ("mono", ["@SELVA.BRAVA"], 30),
  ]},
]},

# ── 03 · PRODUCTO — propiedades + CTA ────────────────────────────
{"name": "03-producto", "slides": [
  {"bg": C["bosque"], "fg": C["hueso"], "accent": C["salvia"], "blocks": [
    ("eyebrow", "Sunscreen SPF 60"), ("gap", 40),
    ("title", "20 gramos que\nrinden lo que\ntienen que rendir", 88), ("gap", 50),
    ("img", TIN, 400),
  ]},
  {"photo": os.path.join(INV, "product_snow.png"), "ov": .42, "bg": C["carbon"], "fg": C["hueso"], "accent": C["salvia"], "blocks": [
    ("eyebrow", "Protección"), ("gap", 50),
    ("title", "FPS 60\nUVA + UVB", 110), ("gap", 40),
    ("body", "Filtros minerales. Protección muy alta. Aplicable bajo cero.", 40, 700),
  ]},
  {"photo": os.path.join(INV, "surf.png"), "ov": .42, "bg": C["carbon"], "fg": C["hueso"], "accent": C["salvia"], "blocks": [
    ("eyebrow", "Resistencia"), ("gap", 50),
    ("title", "Súper resistente\nal agua", 96), ("gap", 40),
    ("body", "Mar, nieve, sudor. Reaplicar cada 2 horas de exposición.", 40, 700),
  ]},
  {"bg": C["salvia"], "fg": C["carbon"], "accent": C["carbon"], "blocks": [
    ("eyebrow", "Multifunción"), ("gap", 50),
    ("title", "Protege, hidrata\ny suaviza", 92), ("gap", 50),
    ("body", "Karité, cacao, coco, almendras y jojoba. Hiperconcentrado: aplicaciones mínimas.", 40, 740),
  ]},
  {"bg": C["carbon"], "fg": C["crema"], "accent": C["salvia"], "blocks": [
    ("eyebrow", "Dónde conseguirlo"), ("gap", 60),
    ("cta", "Mercado Libre"), ("gap", 30),
    ("cta", "WhatsApp +598 99 814 711"), ("gap", 50),
    ("mono", ["LINK EN BIO · @SELVA.BRAVA"], 26),
  ]},
]},

# ── 04 · MANIFIESTO — serie de quotes ────────────────────────────
{"name": "04-manifiesto", "slides": [
  {"bg": C["carbon"], "fg": C["crema"], "accent": C["salvia"], "blocks": [
    ("eyebrow", "Manifiesto"), ("gap", 60), ("rule",), ("gap", 60),
    ("title", "Cuestionamos\nlo establecido.", 110), ("gap", 60), ("rule",),
  ]},
  {"bg": C["carbon"], "fg": C["crema"], "accent": C["salvia"], "blocks": [
    ("gap", 20), ("rule",), ("gap", 60),
    ("title", "Una empresa\nse define tanto\npor lo que rechaza\ncomo por lo que crea.", 84), ("gap", 60), ("rule",),
  ]},
  {"bg": C["carbon"], "fg": C["crema"], "accent": C["salvia"], "blocks": [
    ("gap", 20), ("rule",), ("gap", 60),
    ("title", "Sin plásticos.\nSin químicos\nsintéticos.\nSin promesas\nexageradas.", 84), ("gap", 60), ("rule",),
  ]},
  {"bg": C["bosque"], "fg": C["hueso"], "accent": C["salvia"], "blocks": [
    ("gap", 20), ("rule",), ("gap", 60),
    ("title", "Pensamos por\nnosotros mismos…\ndesde ahí creamos.", 92), ("gap", 60), ("rule",), ("gap", 50),
    ("mono", ["@SELVA.BRAVA"], 30),
  ]},
]},
]

if __name__ == "__main__":
    only = sys.argv[1:] or None
    for t in CAROUSELS:
        if only and t["name"] not in only:
            continue
        build(t)
    print("\nCarruseles OK.")
