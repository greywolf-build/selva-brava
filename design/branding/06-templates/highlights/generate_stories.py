#!/usr/bin/env python3
"""
Contenido de highlights — stories 1080x1920 · Selva Brava
==========================================================
Genera las stories de diseño de cada highlight con el mismo sistema visual
que los covers: paleta oficial, Barlow Condensed / Barlow / Space Mono,
hairlines, textura papel + film grain + vignette. Zona segura IG respetada
(sin contenido en los 250px superiores ni 300px inferiores).

Regenerar:  python3 generate_stories.py [highlight ...]
Datos: fórmula y ensayos = ANMAT (docs/), propiedades = propiedades.jpeg,
INCI = etiqueta real. Nada inventado.
"""
from PIL import Image, ImageDraw, ImageFont, ImageChops
import os

BASE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.abspath(os.path.join(BASE, "..", "..", "..", ".."))
FONTS = os.path.join(PROJ, "design", "branding", "03-typography", "fonts")
OUT = os.path.join(BASE, "stories")

W, H = 1080, 1920
SAFE_TOP, SAFE_BOTTOM = 260, 320
MARGIN = 96

C = {
    "hueso": "#FAF8F1", "crema": "#F6F4EC", "niebla": "#DDE0DA",
    "bosque": "#4C6759", "bosque400": "#687E71", "bosque700": "#394B42",
    "slate": "#687978", "carbon": "#1E2523", "salvia": "#A9B59D",
    "salviaC": "#C3CAB8", "terra": "#B97E6B", "arcilla": "#CEA798",
}

F = {
    "disp_b": os.path.join(FONTS, "BarlowCondensed-Bold.ttf"),
    "disp_sb": os.path.join(FONTS, "BarlowCondensed-SemiBold.ttf"),
    "body": os.path.join(FONTS, "Barlow-Regular.ttf"),
    "body_m": os.path.join(FONTS, "Barlow-Medium.ttf"),
    "mono": os.path.join(FONTS, "SpaceMono-Regular.ttf"),
}

def rgb(h): h = h.lstrip("#"); return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
def font(k, s): return ImageFont.truetype(F[k], s)

# ── texturas (mismas que los covers) ─────────────────────────────
def paper(img, strength=0.28):
    s = img.size
    n = Image.effect_noise(s, 16).point(lambda p: 128 + int((p-128)*strength))
    img = ImageChops.overlay(img, Image.merge("RGB", (n,)*3))
    c = Image.effect_noise((s[0]//8, s[1]//8), 22).resize(s, Image.BILINEAR)
    c = c.point(lambda p: 128 + int((p-128)*strength*0.4))
    return ImageChops.overlay(img, Image.merge("RGB", (c,)*3))

def grain(img, op=0.04):
    n = Image.effect_noise(img.size, 34)
    return Image.blend(img, ImageChops.overlay(img, Image.merge("RGB", (n,)*3)), op*3)

def vignette(img, op=0.07):
    s = 270
    m = Image.new("L", (s, s), 0); d = ImageDraw.Draw(m)
    for i in range(90):
        r = (s/2)*(1-i/90)
        d.ellipse([s/2-r, s/2-r, s/2+r, s/2+r], fill=int(255*i/90))
    m = m.resize(img.size, Image.BILINEAR)
    inv = m.point(lambda p: 255-int((255-p)*op))
    black = Image.new("RGB", img.size, (0, 0, 0))
    return Image.composite(img, black, inv)

# ── helpers de texto ─────────────────────────────────────────────
_meas = ImageDraw.Draw(Image.new("L", (8, 8)))

def tracked_w(f, text, tr):
    w = 0
    for i, ch in enumerate(text):
        b = _meas.textbbox((0, 0), ch, font=f)
        w += b[2]-b[0] + (tr if i < len(text)-1 else 0)
    return w

def draw_tracked(d, cx, y, text, f, fill, tr):
    x = cx - tracked_w(f, text, tr)/2
    for i, ch in enumerate(text):
        b = _meas.textbbox((0, 0), ch, font=f)
        d.text((x-b[0], y), ch, font=f, fill=fill)
        x += b[2]-b[0] + (tr if i < len(text)-1 else 0)

def wrap(text, f, maxw):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur+" "+w_).strip()
        if _meas.textbbox((0, 0), t, font=f)[2] <= maxw:
            cur = t
        else:
            lines.append(cur); cur = w_
    if cur: lines.append(cur)
    return lines

# ── motor de bloques ─────────────────────────────────────────────
def measure(block):
    t = block[0]
    if t == "gap": return block[1]
    if t == "rule": return 2
    if t == "eyebrow": return 30
    if t == "title":
        _, text, size = block
        lines = text.split("\n")
        return len(lines)*int(size*0.98)
    if t == "body":
        _, text, size, maxw = block
        return len(wrap(text, font("body", size), maxw))*int(size*1.5)
    if t == "mono":
        _, lines, size = block
        return len(lines)*int(size*1.9)
    if t == "chips":
        _, items, size = block
        # medir filas
        fnt = font("disp_sb", size); rows, x = 1, 0
        for it in items:
            w_ = tracked_w(fnt, it.upper(), size*0.06)+56
            if x + w_ > W-2*MARGIN: rows += 1; x = 0
            x += w_+18
        return rows*(size+46)+ (rows-1)*14
    if t == "img": return block[2]
    if t == "cta": return 96
    return 0

def render_block(img, d, block, y, fg, accent):
    t = block[0]; cx = W//2
    if t == "eyebrow":
        f = font("mono", 26)
        draw_tracked(d, cx, y, block[1].upper(), f, accent+(255,), 26*0.24)
    elif t == "title":
        _, text, size = block
        f = font("disp_b", size)
        for ln in text.split("\n"):
            draw_tracked(d, cx, y, ln.upper(), f, fg+(255,), size*0.045)
            y += int(size*0.98)
    elif t == "body":
        _, text, size, maxw = block
        f = font("body", size)
        for ln in wrap(text, f, maxw):
            w_ = _meas.textbbox((0, 0), ln, font=f)[2]
            d.text((cx-w_/2, y), ln, font=f, fill=fg+(255,))
            y += int(size*1.5)
    elif t == "mono":
        _, lines, size = block
        f = font("mono", size)
        for ln in lines:
            w_ = _meas.textbbox((0, 0), ln, font=f)[2]
            d.text((cx-w_/2, y), ln, font=f, fill=fg+(255,))
            y += int(size*1.9)
    elif t == "rule":
        d.line([(cx-80, y), (cx+80, y)], fill=fg+(77,), width=2)
    elif t == "chips":
        _, items, size = block
        fnt = font("disp_sb", size)
        rows, row = [], []
        x = 0
        for it in items:
            w_ = tracked_w(fnt, it.upper(), size*0.06)+56
            if x + w_ > W-2*MARGIN and row:
                rows.append(row); row = []; x = 0
            row.append((it, w_)); x += w_+18
        if row: rows.append(row)
        for r in rows:
            tw = sum(w_ for _, w_ in r)+18*(len(r)-1)
            x = cx-tw/2
            hgt = size+46
            for it, w_ in r:
                d.rounded_rectangle([x, y, x+w_, y+hgt], radius=hgt//2,
                                    outline=fg+(150,), width=2)
                draw_tracked(d, x+w_/2, y+23, it.upper(), fnt, fg+(255,), size*0.06)
                x += w_+18
            y += hgt+14
    elif t == "img":
        _, path, hh = block
        im = Image.open(path).convert("RGBA")
        im = im.resize((int(im.width*hh/im.height), hh), Image.LANCZOS)
        img.alpha_composite(im, (cx-im.width//2, y))
    elif t == "cta":
        _, text = block
        f = font("disp_b", 42)
        w_ = tracked_w(f, text.upper(), 42*0.08)+120
        x0 = cx-w_/2
        d.rounded_rectangle([x0, y, x0+w_, y+96], radius=8, fill=accent+(255,))
        # texto en carbón u hueso según luminancia del acento
        lum = sum(accent[:3])/3
        tcol = rgb(C["carbon"]) if lum > 140 else rgb(C["hueso"])
        draw_tracked(d, cx, y+24, text.upper(), f, tcol+(255,), 42*0.08)

def make_story(spec):
    bgc = rgb(spec.get("bg", C["carbon"]))
    fg = rgb(spec.get("fg", C["hueso"]))
    accent = rgb(spec.get("accent", C["salvia"]))
    base = Image.new("RGB", (W, H), bgc)
    if "photo" in spec:
        ph = Image.open(spec["photo"]).convert("RGB")
        r = max(W/ph.width, H/ph.height)
        ph = ph.resize((int(ph.width*r), int(ph.height*r)), Image.LANCZOS)
        base.paste(ph.crop(((ph.width-W)//2, (ph.height-H)//2,
                            (ph.width-W)//2+W, (ph.height-H)//2+H)), (0, 0))
        ov = Image.new("L", (1, H))
        for yy in range(H):  # gradiente vertical: oscuro arriba y abajo
            edge = min(yy, H-yy)/(H/2)
            ov.putpixel((0, yy), int(255*(spec.get("ov", .55)+(1-edge)*.25)))
        ov = ov.resize((W, H))
        base = Image.composite(Image.new("RGB", (W, H), bgc), base, ov)
    base = paper(base, 0.18 if "photo" in spec else 0.28)

    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    blocks = spec["blocks"]
    heights = [measure(b) for b in blocks]
    total = sum(heights)
    y = max(SAFE_TOP, (H-SAFE_BOTTOM+SAFE_TOP)//2 - total//2)
    imgRGBA = base.convert("RGBA")
    for b, hh in zip(blocks, heights):
        render_block(imgRGBA, ImageDraw.Draw(imgRGBA) if b[0] == "img" else d,
                     b, y, fg, accent)
        y += hh
    out = Image.alpha_composite(imgRGBA, layer).convert("RGB")
    out = grain(out); out = vignette(out)
    path = os.path.join(OUT, spec["file"])
    os.makedirs(os.path.dirname(path), exist_ok=True)
    out.save(path, "PNG")
    print("✓", spec["file"])

# ═════════════════════════ CONTENIDO ═════════════════════════════
IMG = os.path.join(PROJ, "web", "src", "assets", "images")
INV = os.path.join(PROJ, "invierno2026")
TIN = os.path.join(IMG, "producto.webp")

STORIES = [
# ── MANIFIESTO ───────────────────────────────────────────────────
{"file": "manifiesto/01_manifiesto.png", "bg": C["carbon"], "fg": C["crema"], "accent": C["salvia"], "blocks": [
    ("eyebrow", "Manifiesto"), ("gap", 40), ("rule",), ("gap", 60),
    ("title", "Cuestionamos\nlo establecido\ny pensamos por\nnosotros mismos…", 92),
    ("gap", 44), ("title", "desde ahí creamos.", 64), ("gap", 60), ("rule",),
]},
{"file": "manifiesto/02_vision.png", "bg": C["carbon"], "fg": C["crema"], "accent": C["salvia"], "blocks": [
    ("eyebrow", "Visión"), ("gap", 50),
    ("title", "Desafiar lo que\ndamos por normal", 84), ("gap", 50),
    ("body", "Hace 10 años que elaboramos protectores solares 100% orgánicos, sin químicos sintéticos ni envoltorios plásticos. La cosmética natural es donde ponemos en práctica lo que creemos.", 38, 800),
]},
{"file": "manifiesto/03_mision.png", "bg": C["carbon"], "fg": C["crema"], "accent": C["salvia"], "blocks": [
    ("eyebrow", "Misión — más allá del producto"), ("gap", 60),
    ("title", "Despertar\nconsciencia", 88), ("gap", 36), ("rule",), ("gap", 36),
    ("title", "Romper con\nfalsas creencias", 88), ("gap", 36), ("rule",), ("gap", 36),
    ("title", "Desechar paradigmas\nque ya no sirven", 88),
]},
{"file": "manifiesto/04_principios.png", "bg": C["carbon"], "fg": C["crema"], "accent": C["salvia"], "blocks": [
    ("eyebrow", "Nuestros principios"), ("gap", 60),
    ("chips", ["Simplicidad", "Multifunción", "Honestidad", "Responsabilidad",
               "Ética", "Ecología", "Diseño consciente", "Directo al grano"], 34),
    ("gap", 40),
    ("body", "Y amor por la naturaleza, los animales y las personas.", 40, 760),
]},
# ── PROPIEDADES ──────────────────────────────────────────────────
{"file": "propiedades/01_portada.png", "bg": C["salvia"], "fg": C["carbon"], "accent": C["carbon"], "blocks": [
    ("eyebrow", "Sunscreen SPF 60"), ("gap", 40),
    ("title", "Propiedades", 100), ("gap", 50),
    ("img", TIN, 480), ("gap", 50),
    ("mono", ["LATA 20 GRS · Ø 5 CM"], 26),
]},
{"file": "propiedades/02_proteccion.png", "bg": C["salvia"], "fg": C["carbon"], "accent": C["carbon"], "blocks": [
    ("eyebrow", "Protección"), ("gap", 50),
    ("title", "FPS 60", 150), ("gap", 20),
    ("title", "UVA + UVB", 66), ("gap", 50), ("rule",), ("gap", 50),
    ("body", "Filtros minerales: óxido de zinc y dióxido de titanio. Protección muy alta, piel extremadamente sensible a la quemadura solar.", 38, 800),
]},
{"file": "propiedades/03_resistencia.png", "photo": os.path.join(INV, "surf.png"), "ov": .42, "bg": C["carbon"], "fg": C["hueso"], "accent": C["salvia"], "blocks": [
    ("eyebrow", "Hecho para condiciones reales"), ("gap", 50),
    ("title", "Súper resistente\nal agua", 84), ("gap", 40), ("rule",), ("gap", 40),
    ("title", "Aplicable en\ntemperaturas bajo cero", 84), ("gap", 50),
    ("body", "Montaña, playa, altura, exposición prolongada. El mismo producto para todo — multifuncional por diseño.", 38, 800),
]},
{"file": "propiedades/04_regeneracion.png", "bg": C["salvia"], "fg": C["carbon"], "accent": C["carbon"], "blocks": [
    ("eyebrow", "Hidrata, nutre y suaviza"), ("gap", 50),
    ("title", "Propiedades\nregeneradoras", 88), ("gap", 50),
    ("body", "Manteca de karité y manteca de cacao orgánicas. El color beige es infusión de cúrcuma orgánica — no hay colorantes.", 38, 780),
    ("gap", 40), ("mono", ["HIPERCONCENTRADO:", "APLICACIONES MÍNIMAS"], 28),
]},
{"file": "propiedades/05_organico.png", "bg": C["salvia"], "fg": C["carbon"], "accent": C["carbon"], "blocks": [
    ("eyebrow", "100% natural"), ("gap", 50),
    ("title", "Hecho con\nmaterias primas\norgánicas", 88), ("gap", 50),
    ("body", "A base de plantas, aceites, ceras naturales y minerales. Sin filtros químicos sintéticos, sin envase plástico.", 38, 780),
]},
# ── PRODUCTO ─────────────────────────────────────────────────────
{"file": "producto/01_portada.png", "bg": C["bosque"], "fg": C["hueso"], "accent": C["salvia"], "blocks": [
    ("eyebrow", "El producto"), ("gap", 40),
    ("title", "Sunscreen\nSPF 60", 110), ("gap", 50),
    ("img", TIN, 500), ("gap", 50),
    ("mono", ["PROTECTOR SOLAR ORGÁNICO", "LATA 20 GRS"], 26),
]},
{"file": "producto/02_que-es.png", "photo": os.path.join(INV, "product_nature.png"), "ov": .45, "bg": C["carbon"], "fg": C["hueso"], "accent": C["salvia"], "blocks": [
    ("eyebrow", "Qué es"), ("gap", 50),
    ("title", "Lo que lo diferencia\nes lo que no tiene", 80), ("gap", 50),
    ("body", "Sin filtros químicos sintéticos. Sin conservantes. Sin envase plástico. Protector solar orgánico de alta protección con filtros minerales, para uso diario y condiciones exigentes.", 38, 800),
]},
{"file": "producto/03_ingredientes.png", "bg": C["bosque"], "fg": C["hueso"], "accent": C["salvia"], "blocks": [
    ("eyebrow", "Ingredientes — todos, no un resumen"), ("gap", 60),
    ("mono", ["Prunus amygdalus dulcis (almendras)",
              "Zinc oxide (filtro UV mineral)",
              "Titanium dioxide (filtro UV)",
              "Theobroma cacao (cacao)",
              "Simmondsia chinensis (jojoba)",
              "Beeswax (cera de abejas)",
              "Butyrospermum parkii (karité)",
              "Cocos nucifera (coco)",
              "Curcuma longa (cúrcuma)"], 30),
    ("gap", 50),
    ("body", "Ingredientes que se leen y se entienden.", 38, 760),
]},
{"file": "producto/04_modo-de-uso.png", "bg": C["bosque"], "fg": C["hueso"], "accent": C["salvia"], "blocks": [
    ("eyebrow", "Modo de uso"), ("gap", 50),
    ("title", "Simple,\ncomo debe ser", 88), ("gap", 50),
    ("body", "Aplicar suavemente hasta cubrir las zonas a proteger. No precisa esperar ni tener la piel seca. Reaplicar cada 2 horas de exposición, después de nadar o de sudoración intensa.", 38, 800),
    ("gap", 40), ("mono", ["NIÑOS MENORES DE 6 MESES:", "CONSULTAR AL MÉDICO"], 26),
]},
{"file": "producto/05_comprar.png", "bg": C["bosque"], "fg": C["hueso"], "accent": C["salvia"], "blocks": [
    ("eyebrow", "Dónde conseguirlo"), ("gap", 50),
    ("title", "Directo,\nsin vueltas", 96), ("gap", 60),
    ("cta", "Comprar en Mercado Libre"), ("gap", 30),
    ("cta", "Consultar por WhatsApp"), ("gap", 50),
    ("mono", ["LINK EN BIO · @SELVA.BRAVA"], 26),
]},
# ── INVIERNO ─────────────────────────────────────────────────────
{"file": "invierno/01_montania.png", "photo": os.path.join(INV, "snowy2.png"), "ov": .42, "bg": C["carbon"], "fg": C["hueso"], "accent": C["salviaC"], "blocks": [
    ("eyebrow", "Temporada de nieve"), ("gap", 50),
    ("title", "En altura el sol\nno perdona", 88), ("gap", 50),
    ("body", "La radiación UV aumenta con la altitud y la nieve la refleja. Protección muy alta, pensada para jornadas largas de montaña.", 38, 800),
]},
{"file": "invierno/02_bajo-cero.png", "photo": os.path.join(INV, "product_snow.png"), "ov": .40, "bg": C["carbon"], "fg": C["hueso"], "accent": C["salviaC"], "blocks": [
    ("eyebrow", "Hecho para el frío"), ("gap", 50),
    ("title", "Aplicable\nbajo cero", 110), ("gap", 50),
    ("body", "Fórmula sólida en lata: no se congela como las cremas con agua, no se derrama en la mochila y entra en cualquier bolsillo de la campera.", 38, 800),
]},
{"file": "invierno/03_shops.png", "photo": os.path.join(INV, "snowboarder.png"), "ov": .48, "bg": C["carbon"], "fg": C["hueso"], "accent": C["salviaC"], "blocks": [
    ("eyebrow", "Shops y cerros"), ("gap", 50),
    ("title", "¿Tenés un shop\nen la montaña?", 84), ("gap", 50),
    ("body", "Trabajamos con tiendas outdoor y locales en cerros de ski de Argentina y Uruguay. Condiciones claras, sin letra chica.", 38, 780),
    ("gap", 50), ("cta", "Consultar por distribución"),
]},
# ── HISTORIAS ────────────────────────────────────────────────────
{"file": "historias/01_portada.png", "photo": os.path.join(INV, "mountain_m.png"), "ov": .45, "bg": C["carbon"], "fg": C["crema"], "accent": C["arcilla"], "blocks": [
    ("eyebrow", "Historias reales"), ("gap", 50),
    ("title", "Gente real,\npiel real", 96), ("gap", 50),
    ("body", "Acá no hay modelos ni guiones. Lo que ves es gente que eligió el producto y lo usa donde vive: montaña y playa.", 38, 780),
]},
{"file": "historias/02_compartir.png", "bg": C["terra"], "fg": C["crema"], "accent": C["crema"], "blocks": [
    ("eyebrow", "Sumá la tuya"), ("gap", 50),
    ("title", "¿Usás\nSelva Brava?", 96), ("gap", 50),
    ("body", "Etiquetanos en tus fotos y videos. Las mejores historias aparecen acá.", 40, 720),
    ("gap", 50), ("mono", ["@SELVA.BRAVA"], 34),
]},
# ── CIENCIA ──────────────────────────────────────────────────────
{"file": "ciencia/01_portada.png", "photo": os.path.join(INV, "turmeric.png"), "ov": .48, "bg": C["carbon"], "fg": C["hueso"], "accent": C["salvia"], "blocks": [
    ("eyebrow", "Ciencia"), ("gap", 50),
    ("title", "Sin promesas.\nSolo evidencia.", 92), ("gap", 50),
    ("body", "Cada afirmación de este producto está respaldada por ensayos de laboratorio. Los podés pedir — no tenemos nada que esconder.", 38, 780),
]},
{"file": "ciencia/02_formula.png", "bg": C["hueso"], "fg": C["bosque700"], "accent": C["bosque"], "blocks": [
    ("eyebrow", "Ingredientes declarados ante ANMAT"), ("gap", 60),
    ("mono", ["Aceite de almendras",
              "Óxido de zinc",
              "Dióxido de titanio",
              "Cacao",
              "Aceite de jojoba",
              "Cera de abeja",
              "Manteca de karité",
              "Aceite de coco",
              "Manteca de cacao",
              "Cúrcuma"], 30),
    ("gap", 50),
    ("body", "Todos los ingredientes, sin resúmenes. Ninguno que no se entienda.", 38, 760),
]},
{"file": "ciencia/03_ensayos.png", "bg": C["hueso"], "fg": C["bosque700"], "accent": C["bosque"], "blocks": [
    ("eyebrow", "Ensayos de laboratorio"), ("gap", 60),
    ("chips", ["Factor de protección solar", "Ensayo UVA", "Ensayo UVB",
               "Fototoxicidad", "Irritación dérmica", "Challenger test",
               "Estabilidad 90 días"], 32),
    ("gap", 50),
    ("body", "Todos realizados sobre el producto real, no sobre promesas.", 38, 760),
]},
{"file": "ciencia/04_registro.png", "bg": C["hueso"], "fg": C["bosque700"], "accent": C["bosque"], "blocks": [
    ("eyebrow", "Legal y trazable"), ("gap", 50),
    ("title", "Habilitado\npor ANMAT", 96), ("gap", 50),
    ("body", "Industria argentina. Elaborado en laboratorio habilitado, con lote y vencimiento impresos en cada lata.", 38, 760),
    ("gap", 40), ("mono", ["RES. M.S. Y A.S. 155/98"], 26),
]},
# ── COMPRAR ──────────────────────────────────────────────────────
{"file": "comprar/01_canales.png", "bg": C["crema"], "fg": C["carbon"], "accent": C["bosque"], "blocks": [
    ("eyebrow", "Dónde comprar"), ("gap", 50),
    ("title", "Dos canales.\nCero fricción.", 92), ("gap", 60),
    ("cta", "Mercado Libre"), ("gap", 30),
    ("cta", "WhatsApp +598 99 814 711"), ("gap", 50),
    ("mono", ["LINK EN BIO"], 28),
]},
{"file": "comprar/02_whatsapp.png", "bg": C["crema"], "fg": C["carbon"], "accent": C["bosque"], "blocks": [
    ("eyebrow", "Atención real"), ("gap", 50),
    ("title", "Sin bots.\nDel otro lado hay\nuna persona.", 84), ("gap", 50),
    ("body", "Consultas, pedidos, dudas sobre el producto. Respondemos nosotros.", 40, 720),
    ("gap", 50), ("cta", "Escribinos por WhatsApp"),
]},
{"file": "comprar/03_mayorista.png", "bg": C["crema"], "fg": C["carbon"], "accent": C["bosque"], "blocks": [
    ("eyebrow", "Mayorista"), ("gap", 50),
    ("title", "¿Tenés un local,\nshop o distribuidora?", 78), ("gap", 50),
    ("body", "Shops de wellness, tiendas outdoor, cerros de ski, boutiques conscientes. Condiciones claras.", 38, 760),
    ("gap", 50), ("cta", "Consultar por distribución"),
]},
# ── COMUNIDAD ────────────────────────────────────────────────────
{"file": "comunidad/01_vida.png", "photo": os.path.join(INV, "outdoor.png"), "ov": .45, "bg": C["carbon"], "fg": C["hueso"], "accent": C["salviaC"], "blocks": [
    ("eyebrow", "Comunidad"), ("gap", 50),
    ("title", "Cuerpo, mente\ny entorno", 92), ("gap", 50),
    ("body", "No vendemos un estilo de vida: acompañamos el tuyo. Montaña, mar, yoga, ruta — donde sea que tu piel viva afuera.", 38, 780),
]},
{"file": "comunidad/02_etiqueta.png", "photo": os.path.join(INV, "couple.png"), "ov": .45, "bg": C["carbon"], "fg": C["hueso"], "accent": C["salviaC"], "blocks": [
    ("eyebrow", "Sumate"), ("gap", 50),
    ("title", "Mostranos\ntu afuera", 100), ("gap", 50),
    ("body", "Etiquetá @selva.brava en tus salidas. Compartimos lo que nos vuela la cabeza.", 40, 720),
    ("gap", 50), ("mono", ["@SELVA.BRAVA"], 34),
]},
]

if __name__ == "__main__":
    import sys
    only = sys.argv[1:] or None
    os.makedirs(OUT, exist_ok=True)
    for s in STORIES:
        if only and not any(s["file"].startswith(o) for o in only):
            continue
        make_story(s)
    print(f"\n{sum(1 for s in STORIES if not only or any(s['file'].startswith(o) for o in only))} stories.")
