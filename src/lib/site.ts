import { type Dirent, existsSync, readFileSync, readdirSync } from 'node:fs';
import path from 'node:path';
import { marked } from 'marked';

export type MarkdownPage = {
  title: string;
  description: string;
  html: string;
  route: string;
  repoPath: string;
  sourceUrl: string;
};

export type Section = {
  key: string;
  title: string;
  description: string;
  sourceDir: string;
  route: string;
};

export const repoUrl = 'https://github.com/joshka/practice';

export const sections: Section[] = [
  {
    key: 'guides',
    title: 'Guides',
    description: 'Narrative guidance for software changes, Rust maintenance, docs, agents, and jj.',
    sourceDir: 'guides',
    route: '/guides/',
  },
  {
    key: 'patterns',
    title: 'Patterns',
    description: 'Repeatable situations and moves that can be cited in review.',
    sourceDir: 'patterns',
    route: '/patterns/',
  },
  {
    key: 'why',
    title: 'Why',
    description: 'Principles that explain the reasoning behind several rules and patterns.',
    sourceDir: 'principles',
    route: '/why/',
  },
  {
    key: 'mechanisms',
    title: 'Mechanisms',
    description: 'Commands, checks, lints, and workflows that make repeated guidance mechanical.',
    sourceDir: 'mechanisms',
    route: '/mechanisms/',
  },
  {
    key: 'agents',
    title: 'Agents',
    description: 'Copyable execution guidance and compressed rule packs for coding agents.',
    sourceDir: 'snippets/agents',
    route: '/agents/',
  },
  {
    key: 'references',
    title: 'References',
    description: 'Durable source material that supports, contrasts, or frames the guidance.',
    sourceDir: 'references',
    route: '/references/',
  },
];

const root = process.cwd();

marked.use({ gfm: true });

export function withBase(route: string): string {
  const base = import.meta.env.BASE_URL.replace(/\/$/, '');
  if (route === '/') {
    return base || '/';
  }
  return `${base}${route}`;
}

export function sourceUrl(repoPath: string): string {
  return `${repoUrl}/blob/main/${repoPath}`;
}

export function pageTitleFromMarkdown(markdown: string, fallback: string): string {
  const match = markdown.match(/^#\s+(.+)$/m);
  return match?.[1]?.trim() ?? fallback;
}

export function descriptionFromMarkdown(markdown: string): string {
  const withoutTitle = markdown.replace(/^#\s+.+$/m, '').trim();
  const paragraph = withoutTitle.split(/\n\s*\n/).find((block) => block.trim() && !block.startsWith('```'));
  return truncateWords(paragraph?.replace(/\s+/g, ' ') ?? '', 180);
}

export function renderMarkdown(repoPath: string): MarkdownPage {
  const absolute = path.join(root, repoPath);
  const markdown = readFileSync(absolute, 'utf8');
  const html = rewriteLinks(marked.parse(markdown) as string, repoPath);
  const route = routeForRepoPath(repoPath);
  return {
    title: pageTitleFromMarkdown(markdown, titleFromSlug(path.basename(repoPath, '.md'))),
    description: descriptionFromMarkdown(markdown),
    html,
    route,
    repoPath,
    sourceUrl: sourceUrl(repoPath),
  };
}

export function getSection(key: string): Section | undefined {
  return sections.find((section) => section.key === key);
}

export function sectionPages(section: Section): MarkdownPage[] {
  const directory = path.join(root, section.sourceDir);
  return readMarkdownFiles(directory)
    .filter((file) => path.basename(file) !== 'README.md')
    .map((file) => renderMarkdown(toRepoPath(file)))
    .sort((a, b) => a.title.localeCompare(b.title));
}

export function sectionIndex(section: Section): MarkdownPage {
  const readme = path.join(section.sourceDir, 'README.md');
  if (existsSync(path.join(root, readme))) {
    return renderMarkdown(readme);
  }
  return {
    title: section.title,
    description: section.description,
    html: `<p>${escapeHtml(section.description)}</p>`,
    route: section.route,
    repoPath: section.sourceDir,
    sourceUrl: sourceUrl(section.sourceDir),
  };
}

export function ruleDomains(): MarkdownPage[] {
  return readMarkdownFiles(path.join(root, 'rules'), 2)
    .filter((file) => path.basename(file) === 'README.md' && path.dirname(file) !== path.join(root, 'rules'))
    .map((file) => renderMarkdown(toRepoPath(file)))
    .sort((a, b) => a.title.localeCompare(b.title));
}

export function rulesForDomain(domain: string): MarkdownPage[] {
  return readMarkdownFiles(path.join(root, 'rules', domain))
    .filter((file) => path.basename(file) !== 'README.md')
    .map((file) => renderMarkdown(toRepoPath(file)))
    .sort((a, b) => a.title.localeCompare(b.title));
}

export function allPublicPages(): MarkdownPage[] {
  const basePages = [renderMarkdown('README.md'), renderMarkdown('rules/README.md')];
  const sectionIndexes = sections.map(sectionIndex);
  const sectionChildren = sections.flatMap(sectionPages);
  const domains = ruleDomains();
  const domainRules = domains.flatMap((domain) => {
    const parts = domain.repoPath.split('/');
    return rulesForDomain(parts[1]);
  });
  return [...basePages, ...sectionIndexes, ...sectionChildren, ...domains, ...domainRules];
}

export function routeForRepoPath(repoPath: string): string {
  const normalized = repoPath.replaceAll('\\', '/');
  if (normalized === 'README.md') return '/';
  if (normalized === 'rules/README.md') return '/rules/';
  if (normalized.startsWith('rules/') && normalized.endsWith('/README.md')) {
    return `/${normalized.replace('/README.md', '/')}`;
  }
  if (normalized.startsWith('rules/') && normalized.endsWith('.md')) {
    return `/${normalized.replace(/\.md$/, '/')}`;
  }
  for (const section of sections) {
    if (normalized === `${section.sourceDir}/README.md`) return section.route;
    if (normalized.startsWith(`${section.sourceDir}/`) && normalized.endsWith('.md')) {
      const slug = normalized.slice(section.sourceDir.length + 1, -3);
      return `${section.route}${slug}/`;
    }
  }
  return `${repoUrl}/blob/main/${normalized}`;
}

function rewriteLinks(html: string, fromRepoPath: string): string {
  return html.replace(/href="([^"]+)"/g, (_match, href: string) => {
    return `href="${escapeHtml(rewriteHref(href, fromRepoPath))}"`;
  });
}

function rewriteHref(href: string, fromRepoPath: string): string {
  if (
    href.startsWith('http://') ||
    href.startsWith('https://') ||
    href.startsWith('#') ||
    href.startsWith('mailto:')
  ) {
    return href;
  }
  const [withoutHash, hash = ''] = href.split('#');
  if (!withoutHash.endsWith('.md')) {
    return href;
  }
  const target = path.normalize(path.join(path.dirname(fromRepoPath), withoutHash)).replaceAll('\\', '/');
  const route = routeForRepoPath(target);
  const routed = route.startsWith('http') ? route : withBase(route);
  return hash ? `${routed}#${hash}` : routed;
}

function readMarkdownFiles(directory: string, maxDepth = 1): string[] {
  const files: string[] = [];
  const visit = (current: string, depth: number) => {
    if (!existsSync(current) || depth > maxDepth) return;
    for (const entry of readdirSorted(current)) {
      const fullPath = path.join(current, entry.name);
      if (entry.isDirectory()) {
        visit(fullPath, depth + 1);
      } else if (entry.isFile() && entry.name.endsWith('.md')) {
        files.push(fullPath);
      }
    }
  };
  visit(directory, 1);
  return files;
}

function readdirSorted(directory: string) {
  return readdirSync(directory, { withFileTypes: true }).sort((a: Dirent, b: Dirent) =>
    a.name.localeCompare(b.name),
  );
}

function toRepoPath(file: string): string {
  return path.relative(root, file).replaceAll('\\', '/');
}

function titleFromSlug(slug: string): string {
  return slug
    .split('-')
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(' ');
}

function truncateWords(value: string, maxLength: number): string {
  if (value.length <= maxLength) return value;
  const truncated = value.slice(0, maxLength);
  const lastSpace = truncated.lastIndexOf(' ');
  return `${truncated.slice(0, lastSpace > 80 ? lastSpace : maxLength).trimEnd()}...`;
}

function escapeHtml(value: string): string {
  return value
    .replaceAll('&', '&amp;')
    .replaceAll('"', '&quot;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;');
}
