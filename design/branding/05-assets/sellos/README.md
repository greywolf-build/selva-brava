# Sellos — badges de confianza

Sellos circulares de línea (estilo apothecary, mismo lenguaje que el full badge):
anillo doble + texto en curva (Barlow Condensed SemiBold) + pictograma central +
rombos separadores. Vista rápida: `_preview.png`.

| Sello | Texto | Centro | Uso |
|---|---|---|---|
| `sello_reef-safe` | REEF SAFE · OCEAN FRIENDLY | Olas | Sunscreen, claims océano |
| `sello_organic` | 100% ORGANIC · SKIN CARE | Hoja | Toda la línea |
| `sello_earth-friendly` | EARTH FRIENDLY · SELVA BRAVA ORGANICS | Globo | Packaging, papelería |
| `sello_spf-60` | PROTECCIÓN ALTA · UVA + UVB | SPF 60 | Sunscreen |
| `sello_spf-20` | PROTECCIÓN · UVA + UVB | SPF 20 | Cacao Butter, Moist |

## Archivos
- `<sello>_slate.svg` — **canónico** (tinta `#687978`), texto ya vectorizado.
- `<sello>_bosque.svg` — verde marca `#4C6759`.
- `<sello>_hueso.svg` — reverse `#FAF8F1`, solo sobre fondos oscuros.
- `<sello>.png` — render 1024 px del canónico (fondo transparente).
- `src/<sello>_editable.svg` — fuente con **texto vivo** para editar copy
  (requiere las fuentes de `../../03-typography/fonts/` instaladas; luego
  vectorizar con `inkscape --export-text-to-path`).

## Reglas
- Un solo color por aplicación (nunca multicolor).
- Tamaño mínimo: 18 mm print / 64 px digital.
- Recolorear solo dentro de la paleta (`../../02-color/paleta.md`).
