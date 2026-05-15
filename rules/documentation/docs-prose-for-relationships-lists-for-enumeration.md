# Docs Prose For Relationships Lists For Enumeration

## Metadata

- ID: `DOCS-PROSE-FOR-RELATIONSHIPS-LISTS-FOR-ENUMERATION`
- Legacy ID: `R-0509`
- Status: `reviewed`
- Domain: `documentation`
- Depth: `compact`

## Rule

Use prose for relationships and lists for enumeration.

## Why

Lists are good for fields, steps, options, and checks, but weak for explaining causality. When every
sentence becomes a bullet, the reader loses the relationship between ideas: why one tradeoff
matters, how a failure unfolds, or when to choose one path over another.

## Helps

- Makes explanations coherent while keeping procedural or enumerated material easy to scan.

## Limits

Use lists when the order or set matters. Use prose when the point is relationship, cause, contrast,
or judgment.

## Agent Instruction

Use prose for relationships and lists for enumeration because lists are good for fields, steps,
options, and checks, but weak for explaining causality.

## Mechanisms

Supported by structure review, page-mode review, and edits that merge low-signal bullets back into
paragraphs when the bullets are really one explanation.

## References

- [Principle: Docs Are Contracts](../../principles/docs-are-contracts.md)
- [Diataxis: how to use Diataxis](https://diataxis.fr/how-to-use-diataxis/)
- [Rustdoc: how to write
  documentation](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html)
