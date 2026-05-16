# Docs Write For Non Linear Readers

## Metadata

- ID: `DOCS-WRITE-FOR-NON-LINEAR-READERS`
- Status: `reviewed`
- Domain: `documentation`
- Depth: `compact`

## Rule

Write docs for non-linear readers.

## Why

Many readers do not read documentation front to back. They arrive from search, Rustdoc links, review
comments, or agent retrieval into the middle of a page. Each section needs enough local context to
make sense without replaying the entire document.

## Helps

- Makes sections useful when linked directly and improves agent retrieval quality.

## Limits

Do not repeat the whole introduction in every section. Add just enough local subject, contract, or
prerequisite to make the section stand alone.

## Agent Instruction

Write docs for non-linear readers because many readers do not read documentation front to back.

## Mechanisms

Supported by heading review, direct-link review, Rustdoc intra-links, examples near the API they
explain, and checks that section titles name the real subject.

## References

- [Principle: Docs Are Contracts](../../principles/docs-are-contracts.md)
- [Diataxis: how to use Diataxis](https://diataxis.fr/how-to-use-diataxis/)
- [Rustdoc: how to write
  documentation](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html)
