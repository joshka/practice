# Rust Teach Crate From Crate Root

## Metadata

- Name: `Teach Crate From Crate Root`
- ID: `RUST-TEACH-CRATE-FROM-CRATE-ROOT`
- Summary: Use crate-root docs and exports to teach the crate's main concepts, entry points, and
  common paths. Keep the root focused enough to orient readers without duplicating every item-level
  contract.
- Status: `reviewed`
- Domain: `rust`
- Tags: `rust, rustdoc, documentation, public-api, module-layout`
- Related: `docs-readme-as-entry-point, rust-expose-primary-path-from-crate-root`

## Rule

Teach the crate from the crate root.

## Why

The crate root is the first Rustdoc page and often the first source file a reader opens. It should
explain the crate purpose, main concepts, feature gates, and entry points before sending readers
deeper.

## Helps

Helps new users learn the crate purpose, main types, feature flags, and first example before they
browse module details.

## Limits

Tiny internal crates can use a shorter crate-root doc. Public crates should still explain the core
workflow and where to go next.

## Agent Instruction

Teach the crate from the crate root because the crate root is the first Rustdoc page and often the
first source file a reader opens.

## Mechanisms

Write crate-level Rustdoc with purpose, quick example, feature notes, important modules, error
model, and links to deeper guides or examples.

## References

- [Rust API Guidelines: crate-level docs are
  thorough](https://rust-lang.github.io/api-guidelines/documentation.html#c-crate-doc)
- [Rustdoc: documenting
  components](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html#documenting-components)
