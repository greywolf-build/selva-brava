# 01 · Logo

Sistema de logo de Selva Brava, derivado del wordmark hand-lettered oficial.
Color principal: verde bosque `#4C6759`.

## Estructura
- `wordmark/vertical/`   — logo apilado (2 líneas). SVG + PNG en verde / crema / negro.
- `wordmark/horizontal/` — logo en 1 línea. SVG + PNG en verde / crema / negro.
- `full-badge/`          — sello completo: neutro (EN, vector) + producto (ES, PNG).
- `isotipo/`             — el símbolo: globo + anillo, sin wordmark (SVG + PNG).
- `lockups/`             — logo con margen sobre fondo de color (verde↔crema).
- `favicon/`             — cuadrado 512/180/32/16 px (wordmark vertical crema sobre verde).

## Convención de nombres
`selva-brava_wordmark_<orientacion>_<color>.<ext>`
p. ej. `selva-brava_wordmark_horizontal_cream.svg`

## Colores disponibles
| Color | HEX | Uso |
|---|---|---|
| verde  | #4C6759 | principal (sobre fondos claros) |
| cream  | #F6F4EC | sobre fondos oscuros |
| black  | #1a1a1a | una tinta / monocromo |

## Elementos del sistema
- **Wordmark** (texto) · **Isotipo** (símbolo) · **Full badge** (todo combinado).

## Nota
El full badge español es PNG (su PDF usa compositing con filtros y no vectoriza
limpio). Para producción a gran escala conviene reconstruir su versión vectorial.
