# Docs Build Docs Like Users Read Them

## Metadata

- ID: `DOCS-BUILD-DOCS-LIKE-USERS-READ-THEM`
- Status: `reviewed`
- Domain: `documentation`
- Depth: `compact`

## Rule

Build Rust docs the way users will read them.

## Why

Rust docs are consumed through rendered Rustdoc, docs.rs feature configuration, intra-doc links,
search, and examples. A Markdown diff can look fine while the rendered page has broken links, hidden
cfg-gated items, unreadable examples, or warnings that only appear in the real build mode.

## Helps

- Catches rendered-doc failures and makes documentation review match the user-facing artifact.

## Limits

A local Markdown or Rustdoc check is enough for small prose-only edits. Use heavier docs.rs-style
builds when features, cfg docs, crate metadata, or public examples change.

## Agent Instruction

Build Rust docs the way users will read them because rust docs are consumed through rendered Rustdoc,
docs.rs feature configuration, intra-doc links, search, and examples.

## Mechanisms

Supported by `cargo doc --no-deps`, `cargo doc --open`, `cargo test --doc`, `RUSTDOCFLAGS="-D
warnings"`, docs.rs cfg builds, and rendered-output review.

## References

- [Principle: Docs Are Contracts](../../principles/docs-are-contracts.md)
- [Diataxis: how to use Diataxis](https://diataxis.fr/how-to-use-diataxis/)
- [Rustdoc: how to write
  documentation](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html)
