import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';

const guides = defineCollection({
  loader: glob({ base: './src/content/guides', pattern: '**/*.md' }),
});

const mechanisms = defineCollection({
  loader: glob({ base: './src/content/mechanisms', pattern: '**/*.md' }),
});

const patterns = defineCollection({
  loader: glob({ base: './src/content/patterns', pattern: '**/*.md' }),
});

const principles = defineCollection({
  loader: glob({ base: './src/content/principles', pattern: '**/*.md' }),
});

const references = defineCollection({
  loader: glob({ base: './src/content/references', pattern: '**/*.md' }),
});

const rules = defineCollection({
  loader: glob({ base: './src/content/rules', pattern: '**/*.md' }),
});

const snippets = defineCollection({
  loader: glob({ base: './src/content/snippets', pattern: '**/*.md' }),
});

export const collections = {
  guides,
  mechanisms,
  patterns,
  principles,
  references,
  rules,
  snippets,
};
