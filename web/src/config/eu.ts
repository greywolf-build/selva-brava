/**
 * Selva Brava — Europa (landing de validación de demanda).
 *
 * ────────────────────────────────────────────────────────────────
 *  TEXTOS EDITABLES. Tocá acá y cambia en toda la versión /eu.
 * ────────────────────────────────────────────────────────────────
 *
 * Importante: esta versión NO vende. El registro regulatorio europeo
 * no está listo. El botón BUY lleva a /eu/coming-soon (lista de espera).
 */

/** Precio mostrado al lado del botón BUY. Solo referencia, no se cobra. */
export const PRICE = '€50';

/**
 * Reemplaza el "SPF 60" fijo de la versión argentina.
 * En la UE el número de SPF es un claim regulado (Rec. 2006/647/CE):
 * se declara por categoría y requiere el ensayo del producto tal como
 * se comercializa acá. Hasta tener eso, texto genérico.
 */
export const SPF_LABEL = 'High SPF — mineral filter';

/**
 * Reemplaza "100% orgánico". En la UE "orgánico"/"natural" en cosmética
 * se apoya en ISO 16128 + Reg. 655/2013 (claims comunes): sin certificación
 * europea a mano, mejor describir la fórmula que etiquetarla.
 */
export const FORMULA_LABEL = 'Natural mineral formula';

/** Placeholder de origen — ajustalo cuando definas la narrativa europea. */
export const ORIGIN_LINE = 'Born in the South Atlantic — made in Europe';

/** Bajada corta que acompaña al origen en el hero. */
export const ORIGIN_TAGLINE = 'Mineral sun care · Europe';

/** Formato: lo único cuantitativo que sí es seguro afirmar. */
export const FORMAT_LABEL = '20 g tin · UVA + UVB · Reef safe';

/** Endpoint de la lista de espera (Formspree). Solo email, sin pagos. */
export const FORMSPREE_ENDPOINT = 'https://formspree.io/f/maewwlbe';

/** Incentivo de la lista de espera. */
export const WAITLIST_INCENTIVE =
  'Be the first to get it + 15% off at launch. Drop your email.';

/** Confirmación tras enviar el email. */
export const WAITLIST_CONFIRMATION = "You're on the list — we'll be in touch.";

/** Canales (los mismos que Argentina — no hay tienda europea todavía). */
export const INSTAGRAM = 'https://instagram.com/selva.brava';
export const WHATSAPP = 'https://wa.me/59899814711';
