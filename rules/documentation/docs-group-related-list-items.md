# Docs Group Related List Items

## Metadata

- Name: `Group Related List Items`
- ID: `DOCS-GROUP-RELATED-LIST-ITEMS`
- Summary: `Cluster long lists under useful names when the relationships matter. Keep short or
  causal material flat or in prose so structure does not add noise.`
- Status: `reviewed`
- Domain: `documentation`
- Depth: `compact`

## Rule

Group related list items under named subheadings when a list grows past easy scanning.

## Why

Long flat lists make every item compete at the same level. Readers can see that many rules exist,
but they cannot see the pattern: which items describe document mode, sentence shape, evidence,
links, examples, review gates, or exceptions. Grouping gives the list a local map and makes missing
or duplicated guidance easier to spot.

## Helps

- Turns long checklists into coherent clusters that are easier to scan, review, and extend.
- Makes hidden rule families visible enough to promote into standalone rule pages.

## Limits

Do not add headings for tiny lists where the grouping is obvious. If the items explain a causal
relationship or tradeoff, rewrite them as prose instead of adding more list structure.

## Agent Instruction

Group long lists into named clusters for distinct rule families, reader tasks, or decision surfaces;
keep short homogeneous lists flat.

## Mechanisms

Supported by table-of-contents review, heading review, documentation linting, and audits that look
for long runs of bullets without internal topic names.

## References

- [Docs Prose For Relationships Lists For Enumeration](docs-prose-for-relationships-lists-for-enumeration.md)
- [Google developer documentation style guide: Lists](https://developers.google.com/style/lists)
- [Google developer documentation style guide: Headings and titles](https://developers.google.com/style/headings)
- [Microsoft Style Guide: Scannable content](https://learn.microsoft.com/en-us/style-guide/scannable-content/)
