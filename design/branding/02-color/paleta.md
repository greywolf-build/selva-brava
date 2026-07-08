# Paleta de color — Selva Brava

Paleta extraída del análisis de las etiquetas reales (`design/tags`). La marca
opera con un **sistema de neutros compartidos + un color de acento por producto**
(color-coding de línea).

---

## Neutros de marca (compartidos en toda la línea)

| Rol | Nombre | HEX | RGB | Swatch |
|---|---|---|---|---|
| **Blanco hueso** 🆕 | Hueso | `#FAF8F1` | 250, 248, 241 | `swatches/hueso-FAF8F1.png` |
| Fondo base | Crema hueso | `#F6F4EC` | 246, 244, 236 | `swatches/crema-F6F4EC.png` |
| Trama / retícula | Gris niebla | `#DDE0DA` | 221, 224, 218 | `swatches/gris-reticula-DDE0DA.png` |
| **Verde marca (wordmark)** | **Bosque** | `#4C6759` | 76, 103, 89 | `swatches/verde-marca-4C6759.png` |
| Tinta principal | Slate teal | `#687978` | 104, 121, 120 | `swatches/tinta-687978.png` |
| Tinta profunda | Slate teal oscuro | `#60716E` | 96, 113, 110 | `swatches/tinta-profunda-60716E.png` |
| **Negro suave** 🆕 | Carbón | `#1E2523` | 30, 37, 35 | `swatches/carbon-1E2523.png` |

> 🆕 **Hueso** (`#FAF8F1`) — blanco cálido de papel, un paso más claro que la crema;
> aporta aire y respiración en packaging/web sin ser blanco puro clínico.
> 🆕 **Carbón** (`#1E2523`) — negro suave con **undertono bosque** (no es negro puro);
> texto de máximo contraste y fondos oscuros premium. Cierra el rango de neutros por
> abajo, igual que Hueso lo abre por arriba.

---

## Escaleras tonales — espectro ampliado (50 → 900)

Cada familia se abre en 10 pasos, mezclando el color ancla (`500`) hacia **Hueso**
(tintes) y hacia **Carbón** (sombras). Así el sistema conserva la calidez orgánica en
todo el rango en vez de virar a blanco/negro puro. Uso típico: `50–200` fondos y
superficies, `300–400` bordes/estados hover, `500` color firma, `600–700` texto sobre
claro, `800–900` fondos oscuros y texto de alto contraste.

Ver tiras: `scales/escalera-*.png` · Poster completo: `paleta-completa.png`

**Neutro** (Hueso → Carbón) — retícula base de UI/texto
| 50 | 100 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 900 |
|---|---|---|---|---|---|---|---|---|---|
| `#FAF8F1` | `#F6F4EC` | `#DDE0DA` | `#BEC2BD` | `#9CA09C` | `#7E827E` | `#5F6561` | `#444A48` | `#313835` | `#1E2523` |

**Bosque** — verde marca / firma
| 50 | 100 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 900 |
|---|---|---|---|---|---|---|---|---|---|
| `#ECECE5` | `#D0D5CD` | `#ACB7AD` | `#87988D` | `#687E71` | `#4C6759` | `#435A4E` | `#394B42` | `#2E3B35` | `#242E2B` |

**Slate** — tinta teal / UI
| 50 | 100 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 900 |
|---|---|---|---|---|---|---|---|---|---|
| `#EEEEE7` | `#D7DAD4` | `#B8BFBB` | `#9AA4A1` | `#7F8D8B` | `#687978` | `#596867` | `#495654` | `#374240` | `#28312F` |

**Salvia** — acento Sunscreen (frío / verde)
| 50 | 100 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 900 |
|---|---|---|---|---|---|---|---|---|---|
| `#F4F3EA` | `#E7E8DD` | `#D6DACB` | `#C5CCBA` | `#B6C0AA` | `#A9B59D` | `#8D9885` | `#6F796A` | `#4D564C` | `#313934` |

**Terracota** — acento Cacao (cálido / tierra)
| 50 | 100 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 900 |
|---|---|---|---|---|---|---|---|---|---|
| `#F5EEE6` | `#EADBD1` | `#DDC1B5` | `#CFA799` | `#C39280` | `#B97E6B` | `#9A6C5D` | `#78594D` | `#53433B` | `#34312D` |

---

## Acentos por producto (color-coding)

### 🌞 Sunscreen — Organic Sunscreen (SPF 60)
Familia **fría / verde salvia** (protección, frescura, montaña).

| Nombre | HEX | RGB |
|---|---|---|
| Salvia eucalipto | `#A9B59D` | 169, 181, 157 |
| Salvia sombra | `#929F8F` | 146, 159, 143 |
| Salvia clara | `#BBC6AA` | 187, 198, 170 |

### 🍫 Cacao Butter — Bálsamo labial (SPF 20)
Familia **cálida / terracota** (tierra, cacao, piel).

| Nombre | HEX | RGB |
|---|---|---|
| Terracota arcilla | `#B97E6B` | 185, 126, 107 |
| Arcilla clara | `#CEA798` | 206, 167, 152 |
| Terracota media | `#BE8977` | 190, 137, 119 |

### 🌿 Moist — Skin Regeneration (SPF 20)
Familia **salvia lavada** (suavidad, regeneración, calma).

| Nombre | HEX | RGB |
|---|---|---|
| Salvia lavada | `#A9B59D` | 169, 181, 157 |
| Salvia neblina | `#C3CAB8` | 195, 202, 184 |
| Verde apagado | `#B0BAA4` | 176, 186, 164 |

---

## Reglas de uso

- **Contraste principal**: tinta `#687978` / carbón `#1E2523` sobre hueso `#FAF8F1` o crema `#F6F4EC` (y viceversa, hueso sobre oscuros).
- El **acento de producto** define el fondo del sello / etiqueta; los neutros mantienen la cohesión de línea.
- Evitar colores puros saturados (rojo/azul brillante) **y** blanco/negro puros: rompen la estética raw/orgánica. Usar siempre Hueso en vez de `#FFFFFF` y Carbón en vez de `#000000`.
- Para versión monocromática usar solo tinta profunda `#60716E` / carbón o hueso.
- Mínimo de contraste texto/fondo recomendado: WCAG AA para body copy (revisar combinaciones claras entre sí, p. ej. crema sobre salvia lavada — usar tinta).
- **Mockups de logo** (colores × fondos): `mockups-logo.png`.

## Formato tokens (para dev / web)

```json
{
  "neutral": {
    "bone":       "#FAF8F1",
    "cream":      "#F6F4EC",
    "mist":       "#DDE0DA",
    "forest":     "#4C6759",
    "ink":        "#687978",
    "ink-deep":   "#60716E",
    "charcoal":   "#1E2523"
  },
  "accent": {
    "sunscreen":  "#A9B59D",
    "cacao":      "#B97E6B",
    "moist":      "#A9B59D"
  },
  "scale": {
    "neutral":   { "50":"#FAF8F1","100":"#F6F4EC","200":"#DDE0DA","300":"#BEC2BD","400":"#9CA09C","500":"#7E827E","600":"#5F6561","700":"#444A48","800":"#313835","900":"#1E2523" },
    "forest":    { "50":"#ECECE5","100":"#D0D5CD","200":"#ACB7AD","300":"#87988D","400":"#687E71","500":"#4C6759","600":"#435A4E","700":"#394B42","800":"#2E3B35","900":"#242E2B" },
    "slate":     { "50":"#EEEEE7","100":"#D7DAD4","200":"#B8BFBB","300":"#9AA4A1","400":"#7F8D8B","500":"#687978","600":"#596867","700":"#495654","800":"#374240","900":"#28312F" },
    "sage":      { "50":"#F4F3EA","100":"#E7E8DD","200":"#D6DACB","300":"#C5CCBA","400":"#B6C0AA","500":"#A9B59D","600":"#8D9885","700":"#6F796A","800":"#4D564C","900":"#313934" },
    "terracotta":{ "50":"#F5EEE6","100":"#EADBD1","200":"#DDC1B5","300":"#CFA799","400":"#C39280","500":"#B97E6B","600":"#9A6C5D","700":"#78594D","800":"#53433B","900":"#34312D" }
  }
}
```
