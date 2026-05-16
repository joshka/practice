# Docs Choose Document Type

## Metadata

- ID: `DOCS-CHOOSE-DOCUMENT-TYPE`
- Status: `reviewed`
- Domain: `documentation`
- Depth: `compact`

## Rule

Choose the document type before editing.

## Why

A page that mixes tutorial, reference, explanation, decision record, and changelog work makes every
reader pay for every mode. Choosing the document type first keeps a README task-first, a reference
page precise, and an ADR focused on the decision instead of blending all three.

## Helps

- Keeps docs navigable and prevents local edits from expanding into accidental page rewrites.

## Limits

Some pages need a small blend, such as a README with a short concept note. Pick the dominant mode
and move deeper reference or decision detail behind links.

## Agent Instruction

Choose the document type before editing because a page that mixes tutorial, reference, explanation,
decision record, and changelog work makes every reader pay for every mode.

## Mechanisms

Supported by doc-type review, page outlines, README/reference/ADR templates, and links that move
secondary modes to the right layer.

## References

- [Principle: Docs Are Contracts](../../principles/docs-are-contracts.md)
- [Diataxis: how to use Diataxis](https://diataxis.fr/how-to-use-diataxis/)
- [Rustdoc: how to write
  documentation](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html)
