import { type Config } from "tailwindcss";

export default {
  content: ["./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      fontFamily: {
        stencil: ["GUERRILLA", "sans-serif"],
      },
      colors: {
        jcb: {
          50: "#fbfbfe",
          100: "#f1f2fd",
          200: "#dde1fe",
          300: "#bcc2fd",
          400: "#9196fb",
          500: "#6261f8",
          600: "#4b3ef0",
          700: "#3c2bdd",
          800: "#3224ba",
          900: "#2b2099",
          950: "#17126a",
        },
      },
    },
  },
  plugins: [],
} satisfies Config;
