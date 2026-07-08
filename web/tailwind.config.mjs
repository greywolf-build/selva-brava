/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,md}'],
  theme: {
    extend: {
      colors: {
        // Neutros de marca — nunca blanco/negro puros (ver 02-color/paleta.md)
        hueso:  '#FAF8F1',
        crema:  '#F6F4EC',
        niebla: '#DDE0DA',
        carbon: '#1E2523',
        bosque: {
          50:'#ECECE5',100:'#D0D5CD',200:'#ACB7AD',300:'#87988D',400:'#687E71',
          DEFAULT:'#4C6759',500:'#4C6759',600:'#435A4E',700:'#394B42',800:'#2E3B35',900:'#242E2B',
        },
        slate: {
          50:'#EEEEE7',100:'#D7DAD4',200:'#B8BFBB',300:'#9AA4A1',400:'#7F8D8B',
          DEFAULT:'#687978',500:'#687978',600:'#596867',700:'#495654',800:'#374240',900:'#28312F',
        },
        salvia: {
          50:'#F4F3EA',100:'#E7E8DD',200:'#D6DACB',300:'#C5CCBA',400:'#B6C0AA',
          DEFAULT:'#A9B59D',500:'#A9B59D',600:'#8D9885',700:'#6F796A',800:'#4D564C',900:'#313934',
        },
        terracota: {
          100:'#EADBD1',200:'#DDC1B5',300:'#CFA799',
          DEFAULT:'#B97E6B',500:'#B97E6B',600:'#9A6C5D',700:'#78594D',
        },
      },
      fontFamily: {
        display: ['"Barlow Condensed"', 'Barlow', 'Arial', 'sans-serif'],
        body:    ['Barlow', 'Helvetica', 'Arial', 'sans-serif'],
        script:  ['Caveat', 'cursive'],
        mono:    ['"Space Mono"', 'ui-monospace', 'Menlo', 'monospace'],
      },
      letterSpacing: {
        display: '0.05em',
        eyebrow: '0.22em',
      },
      maxWidth: { site: '72rem' },
    },
  },
  plugins: [],
};
