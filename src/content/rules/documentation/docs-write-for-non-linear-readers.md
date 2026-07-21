# Docs Write For Non Linear Readers

## Metadata

- Name: `Write for Non-Linear Readers`
- ID: `DOCS-WRITE-FOR-NON-LINEAR-READERS`
- Summary: `Give sections enough local context to work when reached from search, links, review, or
  retrieval. Avoid repeating the whole introduction; add only the subject and prerequisite needed.`
- Status: `reviewed`
- Domain: `documentation`
- Tags: `documentation, reader-locality, agent-context`
- Related: `reader-locality, deliver-context-just-in-time`

## Rule

Write docs for non-linear readers.

## Why

Many readers do not read documentation front to back. They arrive from search, Rustdoc links, review
comments, or agent retrieval into the middle of a page. Each section needs enough local context to
make sense without replaying the entire document.

For source documentation, establish the local subject and required general concept before descending
into a project-specific representation, formula, or optimization. Link to the nearest owning
explanation for shared context, while keeping the local contract, exception, or warning usable at the
entry point the reader reached.

## Helps

- Makes sections useful when linked directly and improves agent retrieval quality.

## Limits

Do not repeat the whole introduction in every section. Add just enough local subject, contract, or
prerequisite to make the section stand alone.

## Agent Instruction

Write docs for non-linear readers. Give each likely entry point enough subject and prerequisite
context to stand alone, then link to the nearest owning explanation instead of repeating it.

## Mechanisms

Supported by heading review, direct-link review, Rustdoc intra-links, examples near the API they
explain, and checks that section titles name the real subject.

## References

- [Principle: Docs Are Contracts](../../principles/docs-are-contracts.md)
- [Diataxis: how to use Diataxis](https://diataxis.fr/how-to-use-diataxis/)
- [Rustdoc: how to write
  documentation](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html)
