// @ts-check
import { existsSync, readdirSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import tailwindcss from '@tailwindcss/vite';
import { defineConfig } from 'astro/config';

const markdownSourceDirs = [
  'guides',
  'mechanisms',
  'patterns',
  'principles',
  'references',
  'rules',
  'snippets/agents',
];

export default defineConfig({
  site: 'https://joshka.net',
  base: '/practice',
  integrations: [markdownSourceWatch()],
  vite: {
    plugins: [tailwindcss()],
  },
});

/** @returns {import('astro').AstroIntegration} */
function markdownSourceWatch() {
  return {
    name: 'markdown-source-watch',
    hooks: {
      'astro:config:setup': ({ addWatchFile, config }) => {
        for (const file of markdownSourceFiles(fileURLToPath(config.root))) {
          addWatchFile(new URL(file, config.root));
        }
      },
    },
  };
}

/** @param {string} root */
function markdownSourceFiles(root) {
  return [
    'README.md',
    ...markdownSourceDirs.flatMap((directory) =>
      readMarkdownFiles(path.join(root, directory), root),
    ),
  ];
}

/**
 * @param {string} directory
 * @param {string} root
 * @returns {string[]}
 */
function readMarkdownFiles(directory, root) {
  if (!existsSync(directory)) return [];
  return readdirSync(directory, { withFileTypes: true })
    .sort((a, b) => a.name.localeCompare(b.name))
    .flatMap((entry) => {
      const fullPath = path.join(directory, entry.name);
      if (entry.isDirectory()) {
        return readMarkdownFiles(fullPath, root);
      }
      if (entry.isFile() && entry.name.endsWith('.md')) {
        return path.relative(root, fullPath).replaceAll(path.sep, '/');
      }
      return [];
    });
}
