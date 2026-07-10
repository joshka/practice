# Rust Avoid Giant Crate Roots

## Metadata

- Name: `Avoid Giant Crate Roots`
- ID: `RUST-AVOID-GIANT-CRATE-ROOTS`
- Summary: Use the crate root to teach the public shape and route readers to focused modules. This
  keeps `lib.rs` or `main.rs` from becoming the whole implementation surface.
- Status: `reviewed`
- Domain: `rust`
- Tags: `rust, reader-locality, public-api, documentation, module-layout`
- Related: `reader-locality, RUST-EXPOSE-PRIMARY-PATH-FROM-CRATE-ROOT`

## Rule

Avoid giant crate roots.

## Why

A giant `lib.rs` or `main.rs` makes the crate root carry every concept, helper, import, and
re-export. Readers need the crate root to teach the public shape and route them to modules, not to
be the whole implementation.

## Helps

Helps the crate root teach users the public shape while letting maintainers find implementation
concepts in focused modules.

## Limits

Tiny crates can keep more code in the root while the public story is still obvious. Split when
scanning, docs, or review start to require too much context.

## Agent Instruction

Avoid giant crate roots because a giant `lib.rs` or `main.rs` makes the crate root carry every concept,
helper, import, and re-export.

## Mechanisms

Move implementation into named modules, keep crate-root docs and re-exports near the top, and use
the root as an orientation page instead of a dumping ground.

## References

- [Rust API Guidelines: crate-level docs are
  thorough](https://rust-lang.github.io/api-guidelines/documentation.html#c-crate-doc)
- [Ed Page Rust Style: source organization](https://epage.github.io/dev/rust-style/)
