/*
 ** TailwindCSS Configuration File
 **
 ** Docs: https://tailwindcss.com/docs/configuration
 ** Default: https://github.com/tailwindcss/tailwindcss/blob/master/stubs/defaultConfig.stub.js
 */
module.exports = {
  theme: {
    extend: {
      gridTemplateColumns: {
        '1/3-2/3': '1fr 2fr'
      }
    }
  },
  variants: {},
  plugins: [require('@tailwindcss/ui')]
}
