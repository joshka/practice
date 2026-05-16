import { allPublicPages, plainTextFromMarkdown, withBase } from '../lib/site';

export function GET() {
  const entries = allPublicPages().map((page) => {
    const sectionText = page.sections
      .map((section) => `${section.title} ${plainTextFromMarkdown(section.markdown)}`)
      .join(' ');
    const metadataText = Object.values(page.metadata).join(' ');

    return {
      title: page.title,
      id: page.metadata.id,
      kind: pageKind(page.repoPath),
      kindLabel: pageKindLabel(page.repoPath),
      description: page.description,
      url: withBase(page.route),
      headings: page.sections.map((section) => section.title),
      text: [page.title, page.description, metadataText, sectionText]
        .join(' ')
        .replace(/\s+/g, ' ')
        .trim(),
    };
  });

  return new Response(JSON.stringify(entries), {
    headers: {
      'content-type': 'application/json; charset=utf-8',
    },
  });
}

function pageKind(repoPath: string): string {
  if (repoPath.startsWith('rules/') && !repoPath.endsWith('/README.md')) return 'rule';
  if (repoPath.startsWith('patterns/')) return 'pattern';
  if (repoPath.startsWith('principles/')) return 'principle';
  if (repoPath.startsWith('mechanisms/')) return 'mechanism';
  if (repoPath.startsWith('snippets/agents/')) return 'agent';
  if (repoPath.startsWith('guides/')) return 'guide';
  if (repoPath.startsWith('references/')) return 'reference';
  return 'page';
}

function pageKindLabel(repoPath: string): string {
  if (repoPath.startsWith('rules/') && repoPath.endsWith('/README.md')) return 'Rule Area';
  if (repoPath === 'rules/README.md') return 'Rule Index';
  return pageKind(repoPath).replace(/^\w/, (letter) => letter.toUpperCase());
}
