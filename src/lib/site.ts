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
  markdown: string;
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
    title: 'Change scope and handoff',
    route: '/guides/software-change-preferences/',
    description: 'Scope, review shape, validation depth, and handoff.',
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
      'Broad decisions that span rules, patterns, principles, and mechanisms.',
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
    title: 'Principles',
    description: 'Rationale, tradeoffs, and limits behind related rules and patterns.',
    sourceDir: 'principles',
    route: '/why/',
  },
  {
    key: 'mechanisms',
    title: 'Mechanisms',
    description: 'Checks, commands, generators, and workflows that support the guidance.',
    sourceDir: 'mechanisms',
    route: '/mechanisms/',
  },
  {
    key: 'agents',
    title: 'Agents',
    description: 'Copyable instruction packs and rule packs for coding agents.',
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

export const guidanceTags = [
  'reader-locality',
  'change-shape',
  'reviewability',
  'verification',
  'testing',
  'failure-output',
  'boundary-correctness',
  'validation-policy',
  'state-transitions',
  'side-effects',
  'async',
  'observability',
  'errors',
  'security-privacy',
  'public-api',
  'rust',
  'rustdoc',
  'dependencies',
  'performance',
  'documentation',
  'examples',
  'source-truth',
  'local-conventions',
  'ownership',
  'agent-workflow',
  'agent-context',
  'ai-assistance',
  'tooling',
  'automation',
  'accessibility',
  'vcs-jj',
  'release',
  'generated-artifacts',
  'review-handoff',
  'refactoring',
  'voice',
  'anti-slop',
] as const;

export type GuidanceTag = (typeof guidanceTags)[number];

const root = process.cwd();
const contentRoot = 'src/content';
const contentAbsoluteRoot = path.join(root, contentRoot);

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

function sourceUrlForRepoPath(repoPath: string): string {
  return sourceUrl(sourceStoragePath(repoPath));
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
  return truncateWords(plainTextFromMarkdown(paragraph ?? ''), 180);
}

export function renderMarkdown(repoPath: string): MarkdownPage {
  repoPath = logicalRepoPath(repoPath);
  const absolute = contentStoragePath(repoPath);
  const rawMarkdown = readFileSync(absolute, 'utf8');
  const parsed = parseFrontmatter(rawMarkdown);
  const markdown = stripLegacyMetadata(parsed.body);
  const metadata = {
    ...metadataFromMarkdown(parsed.body),
    ...parsed.metadata,
  };
  const html = rewriteLinks(marked.parse(markdown) as string, repoPath);
  const sections = markdownSections(markdown, repoPath);
  const route = routeForRepoPath(repoPath);
  const fallbackTitle = displayTitleForRepoPath(
    repoPath,
    pageTitleFromMarkdown(markdown, titleFromSlug(path.basename(repoPath, '.md'))),
  );
  return {
    title: metadata.name || fallbackTitle,
    description: metadata.summary || descriptionFromMarkdown(markdown),
    html,
    introHtml: markdownIntro(markdown, repoPath),
    sections,
    route,
    repoPath,
    sourceUrl: sourceUrlForRepoPath(repoPath),
    metadata,
  };
}

export function getSection(key: string): Section | undefined {
  return sections.find((section) => section.key === key);
}

export function sectionPages(section: Section): MarkdownPage[] {
  const directory = path.join(contentAbsoluteRoot, section.sourceDir);
  return readMarkdownFiles(directory)
    .filter((file) => path.basename(file) !== 'README.md')
    .map((file) => renderMarkdown(toRepoPath(file)))
    .sort((a, b) => a.title.localeCompare(b.title));
}

export function sectionIndex(section: Section): MarkdownPage {
  const readme = path.join(section.sourceDir, 'README.md');
  if (existsSync(contentStoragePath(readme))) {
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
    sourceUrl: sourceUrlForRepoPath(section.sourceDir),
    metadata: {},
  };
}

export function ruleDomains(): MarkdownPage[] {
  return readMarkdownFiles(path.join(contentAbsoluteRoot, 'rules'), 2)
    .filter(
      (file) =>
        path.basename(file) === 'README.md' &&
        path.dirname(file) !== path.join(contentAbsoluteRoot, 'rules'),
    )
    .map((file) => renderMarkdown(toRepoPath(file)))
    .sort((a, b) => a.title.localeCompare(b.title));
}

export function rulesForDomain(domain: string): MarkdownPage[] {
  return readMarkdownFiles(path.join(contentAbsoluteRoot, 'rules', domain))
    .filter((file) => path.basename(file) !== 'README.md')
    .map((file) => renderMarkdown(toRepoPath(file)))
    .sort((a, b) => a.title.localeCompare(b.title));
}

export function allPublicPages(): MarkdownPage[] {
  if (publicPagesCache) return publicPagesCache;
  const basePages = [renderMarkdown('README.md'), renderMarkdown('rules/README.md')];
  const sectionIndexes = sections.map(sectionIndex);
  const sectionChildren = sections.flatMap(sectionPages);
  const domains = ruleDomains();
  const domainRules = domains.flatMap((domain) => {
    const parts = domain.repoPath.split('/');
    return rulesForDomain(parts[1]);
  });
  publicPagesCache = [
    ...basePages,
    ...sectionIndexes,
    ...sectionChildren,
    ...domains,
    ...domainRules,
  ];
  return publicPagesCache;
}

let publicPagesCache: MarkdownPage[] | undefined;

export function tagSlug(value: string): string {
  return value.trim().toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
}

export function tagLabel(value: string): string {
  const acronyms: Record<string, string> = {
    api: 'API',
    async: 'Async',
    rustdoc: 'Rustdoc',
    rust: 'Rust',
    vcs: 'VCS',
    jj: 'JJ',
  };
  return tagSlug(value)
    .split('-')
    .map((part) => acronyms[part] ?? part.charAt(0).toUpperCase() + part.slice(1))
    .join(' ');
}

export function tagsForPage(page: MarkdownPage): string[] {
  const tags = splitMetadataList(page.metadata.tags).map(tagSlug).filter(Boolean);
  const domain = page.metadata.domain ? tagSlug(page.metadata.domain) : '';
  if (domain && guidanceTags.includes(domain as GuidanceTag) && !tags.includes(domain)) {
    tags.unshift(domain);
  }
  return [...new Set(tags)];
}

export function taggedPages(tag: string): MarkdownPage[] {
  const normalized = tagSlug(tag);
  return allPublicPages()
    .filter((page) => isTaggedGuidancePage(page) && tagsForPage(page).includes(normalized))
    .sort((a, b) => pageKindSort(a).localeCompare(pageKindSort(b)) || a.title.localeCompare(b.title));
}

export function tagCounts(): { tag: string; count: number }[] {
  return guidanceTags
    .map((tag) => ({ tag, count: taggedPages(tag).length }))
    .filter((entry) => entry.count > 0);
}

function isTaggedGuidancePage(page: MarkdownPage): boolean {
  return (
    page.repoPath.startsWith('guides/') ||
    (page.repoPath.startsWith('rules/') && !page.repoPath.endsWith('/README.md')) ||
    page.repoPath.startsWith('patterns/') ||
    page.repoPath.startsWith('principles/') ||
    page.repoPath.startsWith('mechanisms/') ||
    page.repoPath.startsWith('snippets/agents/')
  );
}

function pageKindSort(page: MarkdownPage): string {
  if (page.repoPath.startsWith('guides/')) return `1:${page.repoPath}`;
  if (page.repoPath.startsWith('rules/')) return `2:${page.repoPath}`;
  if (page.repoPath.startsWith('patterns/')) return `3:${page.repoPath}`;
  if (page.repoPath.startsWith('principles/')) return `4:${page.repoPath}`;
  if (page.repoPath.startsWith('mechanisms/')) return `5:${page.repoPath}`;
  if (page.repoPath.startsWith('snippets/agents/')) return `6:${page.repoPath}`;
  return `7:${page.repoPath}`;
}

export function splitMetadataList(value: string | undefined): string[] {
  if (!value) return [];
  return value
    .split(',')
    .map((item) => cleanMetadataValue(item))
    .filter(Boolean);
}

export function routeForRepoPath(repoPath: string): string {
  const normalized = logicalRepoPath(repoPath);
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
  const target = logicalRepoPath(path.normalize(path.join(path.dirname(fromRepoPath), withoutHash)));
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
  const absolute = path.resolve(file);
  const relativeToContent = path.relative(contentAbsoluteRoot, absolute);
  if (!relativeToContent.startsWith('..') && !path.isAbsolute(relativeToContent)) {
    return relativeToContent.replaceAll('\\', '/');
  }
  return path.relative(root, absolute).replaceAll('\\', '/');
}

function logicalRepoPath(repoPath: string): string {
  const normalized = repoPath.replaceAll('\\', '/');
  if (normalized.startsWith(`${contentRoot}/`)) {
    return normalized.slice(contentRoot.length + 1);
  }
  return normalized;
}

function contentStoragePath(repoPath: string): string {
  const logical = logicalRepoPath(repoPath);
  const rootPath = path.join(root, logical);
  if (existsSync(rootPath)) {
    return rootPath;
  }
  return path.join(contentAbsoluteRoot, logical);
}

function sourceStoragePath(repoPath: string): string {
  const logical = logicalRepoPath(repoPath);
  if (existsSync(path.join(contentAbsoluteRoot, logical))) {
    return `${contentRoot}/${logical}`;
  }
  return logical;
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
  let currentKey = '';
  let currentValue: string[] = [];

  const commit = () => {
    if (!currentKey) return;
    metadata[currentKey] = cleanMetadataValue(currentValue.join(' '));
  };

  for (const line of match[1].split('\n')) {
    const item = line.match(/^-\s+([^:]+):\s+(.+)$/);
    if (item) {
      commit();
      currentKey = item[1].trim().toLowerCase();
      currentValue = [item[2].trim()];
      continue;
    }

    if (currentKey && /^\s+\S/.test(line)) {
      currentValue.push(line.trim());
    }
  }
  commit();
  return metadata;
}

function markdownIntro(markdown: string, repoPath: string): string {
  const parsed = splitMarkdownSections(markdown);
  const intro = parsed.intro.trim();
  return rewriteLinks(marked.parse(withReferenceDefinitions(intro, markdown)) as string, repoPath);
}

function markdownSections(markdown: string, repoPath: string): MarkdownSection[] {
  return splitMarkdownSections(markdown).sections
    .filter((section) => section.title.toLowerCase() !== 'metadata')
    .map((section) => {
      const sectionMarkdown = section.markdown.trim();
      return {
        title: section.title,
        markdown: sectionMarkdown,
        html: rewriteLinks(
          marked.parse(withReferenceDefinitions(sectionMarkdown, markdown)) as string,
          repoPath,
        ),
      };
    });
}

function withReferenceDefinitions(markdown: string, fullMarkdown: string): string {
  const definitions = referenceDefinitions(fullMarkdown);
  if (!markdown || !definitions) return markdown;
  return `${markdown}\n\n${definitions}`;
}

function referenceDefinitions(markdown: string): string {
  return Array.from(
    markdown.matchAll(/^(?: {0,3})\[[^\]\n]+\]:[^\n]*(?:\n[ \t]+[^\n]+)*/gm),
    (match) => match[0],
  ).join('\n');
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

export function plainTextFromMarkdown(markdown: string): string {
  return markdown
    .replace(/^(?: {0,3})\[[^\]\n]+\]:[^\n]*(?:\n[ \t]+[^\n]+)*/gm, '')
    .replace(/!\[([^\]\n]*)\]\([^)]+\)/g, '$1')
    .replace(/\[([^\]\n]+)\]\[[^\]\n]+\]/g, '$1')
    .replace(/\[([^\]\n]+)\]\([^)]+\)/g, '$1')
    .replace(/`([^`]+)`/g, '$1')
    .replace(/\s+/g, ' ')
    .trim();
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
