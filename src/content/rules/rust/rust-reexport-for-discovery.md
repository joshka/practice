# Rust Reexport For Discovery

## Metadata

- Name: `Reexport For Discovery`
- ID: `RUST-REEXPORT-FOR-DISCOVERY`
- Summary: Re-export public items where callers naturally look so the crate surface is discoverable
  without hiding ownership. Keep canonical definitions and docs clear so re-exports do not become
  competing homes.
- Status: `reviewed`
- Domain: `rust`
- Tags: `rust, public-api, reader-locality, module-layout`
- Related: `rust-use-doc-inline-for-canonical-reexports, rust-keep-preludes-reexport-only`

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
