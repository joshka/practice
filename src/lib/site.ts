import { type Dirent, existsSync, readFileSync, readdirSync } from 'node:fs';
import path from 'node:path';
import { marked } from 'marked';

export type MarkdownPage = {
  title: string;
  description: string;
  html: string;
  introHtml: string;
  sections: MarkdownSection[];
  route: string;
  repoPath: string;
  sourceUrl: string;
  metadata: Record<string, string>;
};

export type MarkdownSection = {
  title: string;
  html: string;
};

export type Section = {
  key: string;
  title: string;
  description: string;
  sourceDir: string;
  route: string;
};

export type PracticeTask = {
  title: string;
  route: string;
  description: string;
};

export const repoUrl = 'https://github.com/joshka/practice';

export const practiceTasks: PracticeTask[] = [
  {
    title: 'Change shape',
    route: '/guides/software-change-preferences/',
    description: 'Review-unit, validation-depth, and handoff decisions before a change grows.',
  },
  {
    title: 'Rust review',
    route: '/guides/rust-maintainability/',
    description: 'API shape, module ownership, docs, tests, dependencies, and release risk.',
  },
  {
    title: 'Code shape',
    route: '/guides/code-shape/',
    description: 'Live context, cohesion, and behavior-preserving source moves.',
  },
  {
    title: 'Documentation',
    route: '/guides/markdown-documentation/',
    description: 'Task-first, lintable docs that stay close to the behavior they describe.',
  },
  {
    title: 'Coding-agent work',
    route: '/guides/coding-agents/',
    description: 'Objectives, boundaries, context, tools, proof, and reusable feedback loops.',
  },
  {
    title: 'JJ workflow',
    route: '/guides/jj-workflow/',
    description: 'Reviewable, recoverable local changes aligned with jj source control.',
  },
];

export const sections: Section[] = [
  {
    key: 'guides',
    title: 'Guides',
    description:
      'Decision maps for recurring engineering work: how changes should be shaped, reviewed, documented, verified, and handed to coding agents.',
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
  const view = repoPath.endsWith('.md') ? 'blob' : 'tree';
  return `${repoUrl}/${view}/main/${repoPath}`;
}

export function pageTitleFromMarkdown(markdown: string, fallback: string): string {
  const match = markdown.match(/^#\s+(.+)$/m);
  return formatDisplayTitle(match?.[1]?.trim() ?? fallback);
}

export function descriptionFromMarkdown(markdown: string): string {
  const withoutTitle = stripLegacyMetadata(markdown).replace(/^#\s+.+$/m, '').trim();
  const paragraph = withoutTitle.split(/\n\s*\n/).find((block) => {
    const trimmed = block.trim();
    return (
      trimmed &&
      !trimmed.startsWith('#') &&
      !trimmed.startsWith('```') &&
      !/^Status:\s*`?[\w-]+`?$/i.test(trimmed)
    );
  });
  return truncateWords(paragraph?.replace(/\s+/g, ' ') ?? '', 180);
}

export function renderMarkdown(repoPath: string): MarkdownPage {
  const absolute = path.join(root, repoPath);
  const rawMarkdown = readFileSync(absolute, 'utf8');
  const parsed = parseFrontmatter(rawMarkdown);
  const markdown = stripLegacyMetadata(parsed.body);
  const html = rewriteLinks(marked.parse(markdown) as string, repoPath);
  const sections = markdownSections(markdown, repoPath);
  const route = routeForRepoPath(repoPath);
  return {
    title: displayTitleForRepoPath(
      repoPath,
      pageTitleFromMarkdown(markdown, titleFromSlug(path.basename(repoPath, '.md'))),
    ),
    description: descriptionFromMarkdown(markdown),
    html,
    introHtml: markdownIntro(markdown, repoPath),
    sections,
    route,
    repoPath,
    sourceUrl: sourceUrl(repoPath),
    metadata: {
      ...metadataFromMarkdown(parsed.body),
      ...parsed.metadata,
    },
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
    introHtml: `<p>${escapeHtml(section.description)}</p>`,
    sections: [],
    route: section.route,
    repoPath: section.sourceDir,
    sourceUrl: sourceUrl(section.sourceDir),
    metadata: {},
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
    .map((word) => (word === 'jj' ? 'JJ' : word.charAt(0).toUpperCase() + word.slice(1)))
    .join(' ');
}

function displayTitleForRepoPath(repoPath: string, title: string): string {
  const parts = repoPath.split('/');
  if (parts[0] !== 'rules' || !parts[2] || parts[2] === 'README.md') {
    return title;
  }

  const rulePrefixes: Record<string, string[]> = {
    'agent-workflow': ['Agent'],
    boundary: ['Boundary'],
    'change-shape': ['Change'],
    documentation: ['Docs'],
    observability: ['Observability'],
    performance: ['Perf'],
    refactoring: ['Refactoring'],
    review: ['Review'],
    rust: ['Rust'],
    source: ['Source'],
    'test-failures': ['Test'],
    testing: ['Test'],
    vcs: ['VCS'],
  };

  let displayTitle = title;
  for (const prefix of rulePrefixes[parts[1]] ?? []) {
    displayTitle = displayTitle.replace(new RegExp(`^${escapeRegExp(prefix)}\\s+`, 'i'), '');
  }
  return displayTitle;
}

function formatDisplayTitle(title: string): string {
  title = title
    .replace(/\bAgents Md\b/g, 'AGENTS.md')
    .replace(/\bDocs Rs\b/g, 'docs.rs')
    .replace(/\bMod Rs\b/g, 'mod.rs')
    .replace(/\bPre Release\b/g, 'Pre-release');

  const smallWords = new Set([
    'a',
    'an',
    'and',
    'as',
    'at',
    'by',
    'for',
    'from',
    'in',
    'into',
    'of',
    'on',
    'only',
    'or',
    'out',
    'over',
    'the',
    'to',
    'with',
  ]);
  const acronyms: Record<string, string> = {
    adr: 'ADR',
    adrs: 'ADRs',
    api: 'API',
    ci: 'CI',
    cli: 'CLI',
    dry: 'DRY',
    jj: 'JJ',
    md: 'MD',
    msrv: 'MSRV',
    pr: 'PR',
    prs: 'PRs',
    readme: 'README',
    ui: 'UI',
    vcs: 'VCS',
  };

  const words = title.split(/\s+/);
  return words
    .map((word, index) => {
      const normalized = word.toLowerCase().replace(/[^a-z0-9]/g, '');
      const trailing = word.match(/[.,:;!?)]$/)?.[0] ?? '';
      const core = trailing ? word.slice(0, -trailing.length) : word;

      if (core === 'AGENTS.md') return `${core}${trailing}`;
      if (acronyms[normalized]) return `${acronyms[normalized]}${trailing}`;
      if (index > 0 && smallWords.has(normalized)) return `${normalized}${trailing}`;
      return `${core}${trailing}`;
    })
    .join(' ');
}

function metadataFromMarkdown(markdown: string): Record<string, string> {
  const match = markdown.match(/^##\s+Metadata\s*\n([\s\S]*?)(?=^##\s+)/m);
  if (!match) return {};
  const metadata: Record<string, string> = {};
  for (const line of match[1].split('\n')) {
    const item = line.match(/^-\s+([^:]+):\s+(.+)$/);
    if (!item) continue;
    metadata[item[1].trim().toLowerCase()] = item[2].replaceAll('`', '').trim();
  }
  return metadata;
}

function markdownIntro(markdown: string, repoPath: string): string {
  const parsed = splitMarkdownSections(markdown);
  const intro = parsed.intro.trim();
  return rewriteLinks(marked.parse(intro) as string, repoPath);
}

function markdownSections(markdown: string, repoPath: string): MarkdownSection[] {
  return splitMarkdownSections(markdown).sections
    .filter((section) => section.title.toLowerCase() !== 'metadata')
    .map((section) => ({
      title: section.title,
      html: rewriteLinks(marked.parse(section.markdown.trim()) as string, repoPath),
    }));
}

function splitMarkdownSections(markdown: string): {
  intro: string;
  sections: { title: string; markdown: string }[];
} {
  const withoutTitle = markdown.replace(/^#\s+.+\n?/, '').trimStart();
  const intro: string[] = [];
  const sections: { title: string; markdown: string[] }[] = [];
  let current: { title: string; markdown: string[] } | undefined;
  let inFence = false;

  for (const line of withoutTitle.split('\n')) {
    if (line.startsWith('```')) {
      inFence = !inFence;
    }

    const heading = !inFence ? line.match(/^##\s+(.+)$/) : undefined;
    if (heading) {
      current = { title: heading[1].trim(), markdown: [] };
      sections.push(current);
      continue;
    }

    if (current) {
      current.markdown.push(line);
    } else {
      intro.push(line);
    }
  }

  return {
    intro: intro.join('\n').trim(),
    sections: sections.map((section) => ({
      title: formatDisplayTitle(section.title),
      markdown: section.markdown.join('\n').trim(),
    })),
  };
}

function parseFrontmatter(markdown: string): { body: string; metadata: Record<string, string> } {
  if (!markdown.startsWith('---\n')) return { body: markdown, metadata: {} };
  const end = markdown.indexOf('\n---', 4);
  if (end === -1) return { body: markdown, metadata: {} };

  const metadata: Record<string, string> = {};
  const frontmatter = markdown.slice(4, end);
  for (const line of frontmatter.split('\n')) {
    const item = line.match(/^([A-Za-z][A-Za-z0-9_-]*):\s*(.*)$/);
    if (!item) continue;
    metadata[item[1].trim().toLowerCase()] = cleanMetadataValue(item[2]);
  }

  const bodyStart = markdown.indexOf('\n', end + 4);
  return {
    body: bodyStart === -1 ? '' : markdown.slice(bodyStart + 1),
    metadata,
  };
}

function stripLegacyMetadata(markdown: string): string {
  return markdown.replace(/^##\s+Metadata\s*\n[\s\S]*?(?=^##\s+)/m, '').trim();
}

function cleanMetadataValue(value: string): string {
  return value
    .trim()
    .replace(/^['"`]|['"`]$/g, '')
    .replace(/^\[(.*)\]$/, '$1')
    .replaceAll('"', '')
    .replaceAll("'", '')
    .replaceAll('`', '')
    .trim();
}

function truncateWords(value: string, maxLength: number): string {
  if (value.length <= maxLength) return value;
  const truncated = value.slice(0, maxLength);
  const lastSpace = truncated.lastIndexOf(' ');
  return `${truncated.slice(0, lastSpace > 80 ? lastSpace : maxLength).trimEnd()}...`;
}

function escapeRegExp(value: string): string {
  return value.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

function escapeHtml(value: string): string {
  return value
    .replaceAll('&', '&amp;')
    .replaceAll('"', '&quot;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;');
}
