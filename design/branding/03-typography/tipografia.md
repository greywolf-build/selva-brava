# Tipografía — Selva Brava

Sistema derivado del **análisis del sello** (`01-logo/full-badge`). El badge combina
cinco registros tipográficos; abajo se traducen a un **sistema de fuentes reales,
libres (SIL OFL) y usables en web/print/packaging**, con archivos incluidos en
`fonts/`.

Regla madre: **display condensado en mayúsculas con tracking amplio** + **sans
humanista cálida para lectura** + **un script usado con cuentagotas**. Nada de
blanco/negro puro (ver `02-color`): tinta = Slate/Carbón, fondos = Hueso/Crema.

---

## Lo que dice el sello (análisis)

| Elemento del badge | Rasgo observado | Rol en el sistema |
|---|---|---|
| `SELVA BRAVA` (wordmark) | Lettering hand-brush, condensado, alto contraste, bordes rotos | **Logo custom** — nunca como fuente de texto |
| Anillo `EARTH FRIENDLY ORGANIC…` | Sans humanista condensada, mayúsculas, tracking amplio | **Display / Titulares** |
| `Organics` | Script manuscrito | **Acento script** |
| `Organic Sunscreen` (base) | Script fluido caligráfico | **Acento script** (uso alterno) |
| `20 grs.` · `SPF 60` | Sans condensada bold + números | **Display** (números) / **Datos** |
| Retícula del globo · descriptores back | Sans técnica de bajo contraste | **Datos / mono** |

---

## Sistema tipográfico (definitivo)

Superfamilia **Barlow** como columna vertebral (nace de la señalética outdoor
californiana → encaja con el ADN montaña/playa/consciente de la marca), un script
para el toque emocional, y un mono para lo técnico.

### 1 · Display / Titulares → **Barlow Condensed**
- **Pesos**: SemiBold / Bold. Siempre **MAYÚSCULAS + tracking `+4…8%`**.
- **Uso**: H1–H2, claims, frente de packaging, portada de campañas, números (`SPF 60`, `20 grs.`, `50+`).
- **Por qué**: replica el anillo del sello sin competir con el wordmark.
- Archivos: `fonts/BarlowCondensed-{Medium,SemiBold,Bold}.ttf`
- *Alterna de máximo impacto*: **Anton** (`fonts/Anton-Regular.ttf`) para titulares gigantes de una sola palabra.

### 2 · Texto / Body → **Barlow**
- **Pesos**: Regular / Medium / SemiBold. Caja normal, interlineado generoso (1.5–1.7).
- **Uso**: párrafos, e-commerce, fichas de producto, descriptores, UI, botones.
- **Por qué**: misma familia que el display → cohesión total; humanista y cálida a cualquier tamaño.
- Archivos: `fonts/Barlow-{Regular,Medium,SemiBold}.ttf`

### 3 · Acento script → **Caveat**
- **Uso**: **una palabra** emocional (`Organics`, `naturaleza`, `ritual`, `puro`), firmas, dedicatorias. Nunca en bloques ni mayúsculas ni párrafos.
- **Por qué**: script manuscrito de pincel, cruda y honesta — es la que mejor conecta con el **lettering hand-brush del wordmark** (mismo gesto “hecho a mano” raw). Variable `wght 400–700`; usar `~600` en tamaños grandes para dar cuerpo.
- Archivo: `fonts/Caveat-Variable.ttf`
- *Alternas (fluidas / más caligráficas)*: **Yellowtail** (brush fluida, calca el `Organic Sunscreen` del sello) o **Kaushan Script** (brush con energía). Descargables de Google Fonts si se necesita otro tono.

### 4 · Datos / Técnico → **Space Mono**
- **Pesos**: Regular / Bold.
- **Uso**: ingredientes (`Cera Alba (beeswax)…`), propiedades, `UVA + UVB`, specs, lotes, precios, legales, tablas.
- **Por qué**: registro técnico-apothecary de bajo contraste; contrasta con lo orgánico y aporta credibilidad “de laboratorio”.
- Archivos: `fonts/SpaceMono-{Regular,Bold}.ttf`

---

## Jerarquía y escala (referencia web, base 16px / 1rem)

| Nivel | Fuente · peso | Tamaño / tracking | Uso |
|---|---|---|---|
| Logo | Wordmark custom | — | Solo marca |
| Display XL | Barlow Condensed Bold · MAYÚS | `56–96px` · `+6%` | Hero, portada, frente packaging |
| H1 | Barlow Condensed SemiBold · MAYÚS | `40–52px` · `+5%` | Títulos de sección, claims |
| H2 | Barlow Condensed SemiBold · MAYÚS | `28–34px` · `+5%` | Subtítulos |
| Acento | Caveat (~600) | `32–64px` | 1 palabra emocional |
| H3 / Eyebrow | Barlow SemiBold · MAYÚS | `13–15px` · `+12%` | Kickers, etiquetas |
| Body | Barlow Regular | `16–18px` · `1.6` | Párrafos, e-commerce |
| Small | Barlow Medium | `13–14px` | Captions, metadatos |
| Datos | Space Mono Regular | `12–14px` · `+2%` | Specs, ingredientes, precios, legales |

**Emparejamientos clave**: Barlow Condensed (título) + Barlow (bajada) es el par por
defecto. Caveat entra solo como acento sobre 1 palabra. Space Mono para todo lo
que sea número/dato/lista técnica.

---

## Reglas de uso

- **Mayúsculas + tracking amplio** en display = tono premium-outdoor del sello.
- **Script con moderación**: 1 palabra por composición, nunca frases largas ni en caja alta.
- **Interlineado generoso** en body → aire “clean apothecary”.
- **Números** (SPF, gramaje, precios): Barlow Condensed o Space Mono, nunca script.
- **Color de tinta**: Slate teal `#687978` / Carbón `#1E2523` sobre claros; Hueso `#FAF8F1` sobre oscuros (ver `02-color`).
- Evitar mezclar más de **2 familias** en una misma pieza (display + body). El script/mono suman como tercer registro puntual.

## Archivos
- `fonts/` — TTF con licencia **SIL OFL** (redistribuibles): Barlow, Barlow Condensed, Caveat, Space Mono, Anton + sus `OFL-*.txt`.
- `muestra-tipografica.png` — espécimen del sistema completo.
- `mockups-tipografia.png` — aplicaciones (packaging, social, e-commerce, editorial) con color de marca.

## Web / CSS (Google Fonts)
Todas las familias están en Google Fonts:
```css
/* Barlow + Barlow Condensed + Caveat + Space Mono (+ Anton opcional) */
--font-display: "Barlow Condensed", sans-serif;
--font-body:    "Barlow", sans-serif;
--font-accent:  "Caveat", cursive;   /* usar font-weight: 600 en tamaños grandes */
--font-mono:    "Space Mono", monospace;
```
