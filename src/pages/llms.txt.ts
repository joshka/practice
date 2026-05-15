import type { APIRoute } from 'astro';
import { allPublicPages, withBase } from '../lib/site';

export const GET: APIRoute = () => {
  const lines = [
    '# Practice',
    '',
    'Durable software-development preferences for code, docs, tests, review, and coding agents.',
    '',
    '## Public Pages',
    '',
    ...allPublicPages().map((page) => `- [${page.title}](${withBase(page.route)}): ${page.description}`),
    '',
  ];

  return new Response(lines.join('\n'), {
    headers: {
      'content-type': 'text/plain; charset=utf-8',
    },
  });
};
