#!/usr/bin/env node

import { spawnSync } from 'node:child_process';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import astroConfig from '../astro.config.mjs';

const root = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const host = '127.0.0.1';
const port = 4321;
const routeArgument = process.argv.slice(2).find((argument) => argument !== '--');
const route = routeFrom(routeArgument ?? '/');
const base = normalizePath(astroConfig.base ?? '/');
const urlPath = base !== '/' && route.startsWith(base) ? route : joinUrlPath(base, route);
const url = new URL(urlPath, `http://${host}:${port}`).href;

const devServer = spawnSync(
  'pnpm',
  ['exec', 'astro', 'dev', '--background', '--host', host, '--port', String(port)],
  { cwd: root, encoding: 'utf8' },
);

if (devServer.status !== 0) {
  process.stderr.write(devServer.stderr || devServer.stdout);
  process.exit(devServer.status ?? 1);
}

const response = await fetch(url, {
  headers: { Accept: 'text/html,application/xhtml+xml' },
});

if (!response.ok) {
  console.error(`Preview returned HTTP ${response.status}: ${url}`);
  console.error('Check the source path or rendered route before opening Firefox.');
  process.exit(1);
}

const title = (await response.text()).match(/<title>([^<]+)<\/title>/)?.[1];
const browser = spawnSync('open', ['-a', 'Firefox', url], { encoding: 'utf8' });

if (browser.status !== 0) {
  process.stderr.write(browser.stderr || browser.stdout);
  process.exit(browser.status ?? 1);
}

console.log(`Opened ${title ?? 'rendered preview'} in Firefox:`);
console.log(url);

function routeFrom(input) {
  const value = input.replaceAll('\\', '/').replace(/^\.\//, '');
  const contentMatch = value.match(/^src\/content\/(.+)\.md$/);

  if (!contentMatch) return normalizePath(value);

  const contentPath = contentMatch[1];
  const mappings = [
    ['snippets/agents/', 'agents/'],
    ['principles/', 'why/'],
    ['guides/', 'guides/'],
    ['mechanisms/', 'mechanisms/'],
    ['patterns/', 'patterns/'],
    ['references/', 'references/'],
    ['rules/', 'rules/'],
  ];

  for (const [sourcePrefix, routePrefix] of mappings) {
    if (contentPath.startsWith(sourcePrefix)) {
      return normalizePath(routePrefix + contentPath.slice(sourcePrefix.length));
    }
  }

  throw new Error(`Cannot map content source to a rendered route: ${input}`);
}

function normalizePath(value) {
  const trimmed = value.replace(/^\/+|\/+$/g, '');
  return trimmed ? `/${trimmed}/` : '/';
}

function joinUrlPath(basePath, routePath) {
  const parts = [basePath, routePath]
    .map((part) => part.replace(/^\/+|\/+$/g, ''))
    .filter(Boolean);
  return normalizePath(parts.join('/'));
}
