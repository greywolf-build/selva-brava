# Carruseles — templates Instagram

Slides **1080×1350** (vertical, máximo alcance en feed) generados con el motor
visual de marca: paleta oficial, Barlow Condensed / Barlow / Space Mono,
textura papel + film grain + vignette. Cromática de carrusel: contador
`01 — 05` arriba a la derecha, flecha de swipe abajo (menos en el último
slide), "DESLIZÁ" solo en el cover.

## Templates (uno por pilar de contenido)

| Template | Slides | Arco narrativo | Pilar |
|---|---|---|---|
| `01-mito-real/` | 5 | Hook (pregunta) → mito → real → dato → cierre "pensá por vos mismo" | Educación honesta |
| `02-ingrediente/` | 4 | Cover foto → qué hace → declarado ante ANMAT → CTA destacada CIENCIA | Ciencia / apothecary |
| `03-producto/` | 5 | Hook producto → protección → resistencia → multifunción → CTA compra | Producto |
| `04-manifiesto/` | 4 | Serie de quotes (carbón) → cierre en bosque con @ | Filosofía |

## Cómo crear un carrusel nuevo

1. Abrir `generate_carousels.py` → lista `CAROUSELS`.
2. Duplicar el template más parecido, cambiar `name` y el copy de los bloques.
3. `python3 generate_carousels.py mi-template` → genera solo ese.

**Bloques disponibles** (del motor `../../highlights/generate_stories.py`):
`eyebrow` · `title` · `body` · `mono` · `chips` · `rule` · `img` · `cta` ·
`gap`. Fondo plano (`bg`) o foto (`photo` + `ov` para el overlay).

## Reglas de serie (manual §10)

- **Un mismo look por carrusel**: no mezclar fondos foto y planos sin criterio
  — acá cada template ya tiene su ritmo (ej: 03-producto alterna plano/foto/plano).
- El template `02-ingrediente` está pensado como **serie coleccionable**:
  Ingrediente 01 cúrcuma, 02 karité, 03 zinc, 04 cacao… duplicar y cambiar
  número, foto y datos (los % reales están en la destacada CIENCIA / ANMAT).
- CTAs de compra: al publicar, el link va en bio o en el caption — los botones
  del slide son diseño.
- Copy siempre con la voz del CLAUDE.md: sin superlativos, sin urgencia falsa.
