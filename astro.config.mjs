// @ts-check
import tailwindcss from '@tailwindcss/vite';
import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://joshka.net',
  base: '/practice',
  vite: {
    plugins: [tailwindcss()],
  },
});
