# Rust Reexport For Discovery

## Metadata

- ID: `RUST-REEXPORT-FOR-DISCOVERY`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Use re-exports for discovery, not ownership hiding.

## Why

Re-exports help users find the public API from the crate root or module facade, but they should not
obscure where the concept is owned. Discovery and ownership are different jobs.

## Helps

Helps users find the intended API from the crate root or module facade while preserving clear
implementation ownership.

## Limits

Avoid re-exporting everything. Too many re-exports hide where concepts live and make accidental
public API expansion easier.

## Agent Instruction

Use re-exports for discovery, not ownership hiding, so users find APIs without losing where concepts
live.

## Mechanisms

Re-export central public types from facade modules, keep implementation modules named and navigable,
and review `pub use` changes as API changes.

## References

- [Rust Reference: use
  declarations](https://doc.rust-lang.org/reference/items/use-declarations.html)
- [Rust API Guidelines: crate-level docs are
  thorough](https://rust-lang.github.io/api-guidelines/documentation.html#c-crate-doc)
