# Docs Match Page Shape To Reader Task

## Metadata

- Name: `Match Page Shape to Reader Task`
- ID: `DOCS-MATCH-PAGE-SHAPE-TO-READER-TASK`
- Summary: `Shape pages around the reader's task, such as learning, choosing, reference, or review.
  The right structure lowers scan cost without forcing one page to do every job.`
- Status: `reviewed`
- Domain: `documentation`
- Tags: `documentation, reader-locality, reviewability`
- Related: `choose-doc-type, DOCS-CHOOSE-DOCUMENT-TYPE`

## Rule

Match each rendered documentation page shape to the reader task it serves.

## Why

A documentation site can use Markdown as its source without making every page feel like raw
Markdown. Landing pages, indexes, catalogs, rule details, runnable mechanisms, references, and long
guides each ask the reader to do different work. When they all render through the same prose-first
template, readers have to infer what is clickable, what is summary, what is source metadata, and
what action they should take next.

The page shape should make that job obvious. A catalog should help a reader choose an entry. A rule
detail page should separate the rule from rationale and limits. A mechanism page should make checks
and commands feel executable. A reference page should make source role and adoption stance easy to
scan.

## Helps

- Keeps navigation pages from turning into README dumps.
- Makes links, tags, cards, rows, code blocks, and source metadata behave consistently.
- Gives first-time readers a clear answer to where they are, what the page is for, and what to click
  next.

## Limits

A small or temporary documentation set can use one generic template while the content model is still
forming. Add purpose-specific page shapes when repeated rendered pages show the same awkwardness:
duplicated headings, metadata as body content, unclear click targets, pseudo-lists, or dense prose
where a catalog would be easier to scan.

## Agent Instruction

For documentation sites that render Markdown, choose a page shape for the reader task before
exposing the content. Use catalogs for choosing, prose pages for explanation, rule layouts for
instructions, mechanism layouts for runnable checks, and reference layouts for source catalogs.

## Mechanisms

Supported by route-specific templates, content-type metadata, generated indexes, rendered-page
screenshots, and review checklists for hierarchy, spacing, tags, links, and responsive wrapping.

## References

- [Diataxis: how to use Diataxis](https://diataxis.fr/how-to-use-diataxis/)
- [Docs Use Descriptive Headings](docs-use-descriptive-headings.md)
- [Docs One Dominant Mode Per Page](docs-one-dominant-mode-per-page.md)
