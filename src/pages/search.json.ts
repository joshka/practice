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
