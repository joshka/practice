# Docs One Dominant Mode Per Page

## Metadata

- Name: `One Dominant Mode per Page`
- ID: `DOCS-ONE-DOMINANT-MODE-PER-PAGE`
- Summary: `Let each page have one primary mode and move competing material behind links. This keeps
  readers from paying for tutorial, reference, explanation, and policy at once.`
- Status: `reviewed`
- Domain: `documentation`
- Tags: `documentation, reader-locality, source-truth`
- Related: `choose-doc-type, DOCS-CHOOSE-DOCUMENT-TYPE`

## Rule

Pick one dominant documentation mode per page.

## Why

A page with competing modes forces readers to switch mental models. A task page wants steps, a
reference page wants completeness, an explanation wants causality, and an ADR wants a decision.
Mixing them without hierarchy makes the page harder to scan and harder to keep current.

## Helps

- Keeps each page useful for its main reader and moves secondary detail to better-linked places.

## Limits

A page can include small supporting sections from another mode. The problem is letting secondary
material dominate or interrupt the main reading path.

## Agent Instruction

Pick one dominant documentation mode per page because a page with competing modes forces readers to
switch mental models.

## Mechanisms

Supported by page outlines, doc-type labels, table-of-contents review, and splitting reference or
decision material into linked pages.

## References

- [Principle: Docs Are Contracts](../../principles/docs-are-contracts.md)
- [Diataxis: how to use Diataxis](https://diataxis.fr/how-to-use-diataxis/)
- [Rustdoc: how to write
  documentation](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html)
