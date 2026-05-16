# Docs Make Review Easy To Inspect

## Metadata

- ID: `DOCS-MAKE-REVIEW-EASY-TO-INSPECT`
- Status: `reviewed`
- Domain: `documentation`
- Depth: `compact`

## Rule

Make documentation review easy to inspect.

## Why

Docs are often reviewed as Markdown diffs even though users read rendered pages, generated Rustdoc,
examples, screenshots, or command output. A reviewer should be able to inspect the relevant artifact
without reconstructing commands or guessing what changed.

## Helps

- Speeds review and makes documentation proof concrete rather than confidence-based.

## Limits

Do not attach heavy rendered proof for a typo. Provide rendered links, screenshots, command output,
or before/after notes when layout, examples, generated docs, or user-visible structure changed.

## Agent Instruction

Make documentation review easy to inspect because docs are often reviewed as Markdown diffs even though
users read rendered pages, generated Rustdoc, examples, screenshots, or command output.

## Mechanisms

Supported by `cargo doc --open`, local preview servers, screenshots, generated artifact checks, PR
links to changed docs, and explicit validation notes.

## References

- [Principle: Docs Are Contracts](../../principles/docs-are-contracts.md)
- [Diataxis: how to use Diataxis](https://diataxis.fr/how-to-use-diataxis/)
- [Rustdoc: how to write
  documentation](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html)
