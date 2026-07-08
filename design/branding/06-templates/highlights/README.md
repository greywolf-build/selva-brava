# Covers de highlights — Instagram

Sistema unificado de 8 portadas 1080×1080 para las historias destacadas de
@selva.brava. Palabra centrada en **Barlow Condensed Bold** (tracking +0.08em,
MAYÚSCULAS), hairlines al 30%, textura de papel + film grain sutil y vignette
suave. Todos los elementos dentro del círculo seguro de 900px.

**Isotipo integrado:** cada tapa lleva el isotipo (globo + anillo EARTH
FRIENDLY) como marca de agua tono-sobre-tono (30% del color del texto),
a 1000px de diámetro — el anillo enmarca justo el recorte circular de IG y
las tapas se leen como sellos. Ajustes: `ISOTIPO_D` / `ISOTIPO_ALPHA` en el
script.

## Covers generados

| # | Archivo | Fondo | Texto |
|---|---|---|---|
| 01 | `highlight_01_manifiesto.png` | Carbón `#1E2523` | Crema `#F6F4EC` |
| 02 | `highlight_02_propiedades.png` | Salvia `#A9B59D` | Carbón `#1E2523` |
| 03 | `highlight_03_producto.png` | Bosque `#4C6759` | Hueso `#FAF8F1` |
| 04 | `highlight_04_invierno.png` | Slate `#687978` | Hueso `#FAF8F1` |
| 05 | `highlight_05_historias.png` | Terracota `#B97E6B` | Crema `#F6F4EC` |
| 06 | `highlight_06_ciencia.png` | Hueso `#FAF8F1` | Bosque `#4C6759` |
| 07 | `highlight_07_comprar.png` | Crema `#F6F4EC` | Carbón `#1E2523` |
| 08 | `highlight_08_comunidad.png` | Bosque 400 `#687E71` | Hueso `#FAF8F1` |

## Cómo se usan en Instagram

1. Subir el PNG como **story** (se puede subir y borrar a los 5 minutos — la
   portada queda igual).
2. En el perfil → destacada → **Editar → Editar portada** → elegir la imagen
   de la galería.
3. Nombre de la destacada: la misma palabra en minúscula (ej. "producto") —
   IG lo muestra debajo del círculo.
4. Orden sugerido (izq → der): manifiesto · producto · invierno · historias ·
   ciencia · comprar · comunidad · propiedades. Al terminar la temporada,
   "invierno" pasa al final o se archiva.

> IG recorta el cuadrado a círculo: por eso todo el diseño vive dentro del
> círculo central de 900px. No editar los PNG agregando elementos cerca de
> las esquinas.

## Cómo regenerar

```bash
python3 generate_highlights.py            # los 8
python3 generate_highlights.py producto   # uno solo (por nombre)
```

- **Cambiar color/texto/palabra:** editar la lista `HIGHLIGHTS` en
  `generate_highlights.py` (usar solo hex de `02-color/paleta.md`).
- **Cambiar tipografía:** editar `FONT_PATH` (fuentes oficiales en
  `03-typography/fonts/`).
- **Ajustes de sistema:** `TARGET_WIDTH` (ocupación de la palabra),
  `TRACKING_EM`, gaps de hairlines — constantes al inicio del script.
- El cuerpo tipográfico se autoajusta al ancho con techo de 128px para que
  palabras cortas no rompan la uniformidad.

## Contenido interno — `stories/`

28 stories de diseño (1080×1920) listas para subir, organizadas por highlight:

| Highlight | Stories | Contenido |
|---|---|---|
| `manifiesto/` | 4 | Manifiesto · visión · misión (3 pilares) · principios |
| `propiedades/` | 5 | Portada+lata · FPS 60 UVA+UVB · agua/bajo cero · regeneración · orgánico |
| `producto/` | 5 | Portada · qué es · ingredientes (INCI real) · modo de uso · comprar |
| `invierno/` | 3 | Sol en altura · aplicable bajo cero · shops en cerros (B2B) |
| `historias/` | 2 | Portada · invitación a etiquetar (el resto se llena con UGC real) |
| `ciencia/` | 4 | Solo evidencia · ingredientes declarados ANMAT · ensayos · registro |
| `comprar/` | 3 | Canales · WhatsApp sin bots · mayorista |
| `comunidad/` | 2 | Vida consciente · etiquetá @selva.brava |

**Datos verificados:** fórmula y ensayos del expediente ANMAT (`docs/`),
propiedades de `propiedades.jpeg`, INCI de la etiqueta real. Nada inventado.

**Fotos:** 9 stories llevan fotografía de `invierno2026/` como fondo con
overlay carbón (surf, product_snow, snowy2, snowboarder, product_nature,
mountain_m, turmeric, outdoor, couple). Para cambiar una foto: editar el campo
`"photo"` de esa story en `generate_stories.py` y regenerar.

**Al subirlas:** las stories con botón dibujado (Mercado Libre / WhatsApp)
necesitan el **sticker de link real de IG encima** del botón — el PNG es solo
diseño. Orden de subida = orden numérico de archivo.

**Regenerar:** `python3 generate_stories.py` (todas) o
`python3 generate_stories.py ciencia comprar` (por highlight). Copy y bloques
se editan en la lista `STORIES` del script.

## Alternativa existente

En `../social/destacadas/` hay un segundo sistema de covers **con iconos**
(sin palabra, fondo bosque único). Elegir uno de los dos sistemas para el
perfil — no mezclar.
