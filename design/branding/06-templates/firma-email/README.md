# Firma de email — Selva Brava

Firma para `info@selvabrava.org` (Zoho Mail). Texto en inglés, paleta y orden
tipográfico del manual: Bosque `#4C6759`, Carbón `#1E2523`, Slate `#687978`;
Barlow Condensed para el nombre, Space Mono para los datos.

| Archivo | Cuándo usarla |
|---|---|
| `firma-con-logo.html` | La que está en uso. Lockup verde + datos. |
| `firma-texto.html` | Sin imágenes. No se rompe nunca ni depende de ningún servidor. |
| `preview.html` | Las dos, sobre fondo claro y oscuro. Abrir en el navegador. |

## El logo tiene que salir de selvabrava.org

`firma-con-logo.html` apunta a:

```
https://selvabrava.org/firma/logo-firma.png
```

El archivo vive en `web/public/firma/logo-firma.png` y se publica al deployar la
web. **La URL no existe hasta que se deploya.**

Verificar antes de activar la firma:

```bash
curl -s -o /dev/null -w "%{http_code}\n" https://selvabrava.org/firma/logo-firma.png   # 200
```

### Dos cosas que ya se probaron y no funcionan

**Subir la imagen desde el editor de Zoho.** Zoho la incrusta en el mensaje (CID),
y toda imagen incrustada es técnicamente un adjunto: al destinatario le aparece el
clip de adjunto en cada mail. Poco serio para B2B.

**Hosts de imágenes gratuitos (postimg.cc y similares).** Bloquean el hotlinking.
`https://i.postimg.cc/...` devuelve **403** cuando la pide un cliente de correo —
quien redacta la ve bien por caché del navegador, quien recibe ve el ícono roto.

Por eso la imagen se sirve desde el dominio propio. Es la única de las tres
opciones que no adjunta nada y no depende de un tercero.

## Instalación en Zoho

1. Abrir `firma-con-logo.html` en un editor de texto y copiar el HTML.
2. Zoho → **Configuración → Correo → Firmas → Nueva firma**.
3. Entrar por el **modo código** (botón `< >` / *Insertar HTML*). Si se pega en el
   editor visual, el código aparece como texto.
4. Asociarla a `info@selvabrava.org`, activa en mensajes nuevos **y** respuestas.

Probar siempre mandando un mail a una casilla externa y abriéndolo **desde el
celular** — es donde más se rompen las firmas.

## Regenerar el PNG del logo

Origen: `design/branding/01-logo/lockups/horizontal_sobre-bosque.png` (3534×863).
Se sirve a 2x (560×136) y se muestra a 280×68.

```bash
python3 -c "
from PIL import Image
im = Image.open('design/branding/01-logo/lockups/horizontal_sobre-bosque.png').convert('RGB')
im.resize((560,136), Image.LANCZOS).save('web/public/firma/logo-firma.png','PNG',optimize=True)"
```

`selva-brava-firma.png` es una alternativa: wordmark verde sobre fondo hueso, para
cuando haga falta el logo sobre claro. El fondo es opaco a propósito — un wordmark
verde sobre transparente desaparece en el modo oscuro de Gmail.

## Reglas al editar

- **Nunca fuentes web.** Gmail y Outlook eliminan `@font-face` y `<link>`. Los
  stacks caen a Arial Narrow / Helvetica / Courier. Está previsto.
- **Todo con `<table>` y estilos inline.** Nada de flexbox, grid ni `<style>`.
- **Sin tablas anidadas.** El editor de Zoho les mete espaciado propio y descoloca
  el contenido. El filete verde es una fila directa de la tabla principal.
- **Sin claims nuevos ni superlativos.** Lo que dice la firma ("No chemical
  filters. No plastic.") es verificable y está respaldado en `docs/`. Lista de
  palabras prohibidas en `CLAUDE.md`.
- Si cambia el teléfono, actualizar el texto **y** el link `wa.me/59899814711`.

## Alias

La firma dice `info@selvabrava.org`. Los alias (`hello@`, `comercial@`, `ventas@`)
caen en la misma bandeja y no necesitan firma propia.
