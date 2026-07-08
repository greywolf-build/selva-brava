# Selva Brava — selvabrava.org

Sitio de presencia de marca. Landing única de storytelling que deriva la venta a
Mercado Libre y WhatsApp. **No es ecommerce** — sin carrito ni pagos.

Stack: **Astro 4 + Tailwind CSS**. Sin más dependencias.

## Desarrollo

```bash
npm install
npm run dev        # http://localhost:4321
npm run build      # genera dist/
npm run preview    # sirve dist/ localmente
```

## Estructura

```
src/
├── pages/index.astro        # única página — orquesta las secciones
├── layouts/Layout.astro     # <head>, SEO, fuentes, script de reveal
├── components/
│   ├── Hero.astro           # manifiesto + nav mínima
│   ├── History.astro        # la historia (10 años)
│   ├── Principles.astro     # los 9 principios
│   ├── Product.astro        # Sunscreen SPF 60 + INCI + CTAs  ← links de venta acá
│   ├── Mission.astro        # misión + 3 pilares
│   ├── Wholesale.astro      # B2B mayorista
│   ├── Contact.astro        # canales                          ← link ML acá también
│   └── Footer.astro
├── styles/global.css        # tokens, grano, reveal, botones
└── assets/                  # fotos webp + SVG de marca (de design/branding/)
```

## Links de Mercado Libre

Ya conectados a la publicación real (`MLAU2977910815` / item `MLA2002373762`).
Si cambia la publicación, actualizar en **dos archivos**:

1. `src/components/Product.astro` → constante `MERCADOLIBRE`.
2. `src/components/Contact.astro` → tarjeta "Mercado Libre" (`href`).

```bash
grep -rn "mercadolibre.com" src/   # los encuentra a ambos
```

## Deploy

### Netlify
- Build command: `npm run build` · Publish directory: `dist`
- O con CLI: `npx netlify deploy --prod --dir=dist`

### Cloudflare Pages
- Framework preset: **Astro** · Build: `npm run build` · Output: `dist`

### Dominio
Apuntar `selvabrava.org` (y `www`) al host elegido. El `site` ya está configurado
en `astro.config.mjs`, y el canonical/OG apuntan a `https://selvabrava.org/`.

## Identidad

Todo sale de `../CLAUDE.md` y `../design/branding/` (paleta, tipografía, sellos,
manual de marca). Reglas duras al editar contenido:

- Voz: honesta, directa, rioplatense. **Sin superlativos** ni promesas
  ("milagroso", "el mejor", "garantizado" están prohibidas — lista completa en CLAUDE.md).
- Color: nunca `#FFFFFF` ni `#000000` — usar `hueso` y `carbon` (tokens en
  `tailwind.config.mjs`).
- Tipografía: Barlow Condensed (títulos, MAYÚS) · Barlow (texto) · Caveat (una
  palabra, nunca frases) · Space Mono (datos/INCI).
- Claims: solo verificables. Los ensayos de laboratorio están en `../docs/`.

## Fases futuras (fuera de este MVP)

Cacao Butter y Moist como productos, ecommerce completo, blog, multi-idioma.
