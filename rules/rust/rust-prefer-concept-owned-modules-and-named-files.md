# Rust Prefer Concept Owned Modules And Named Files

## Metadata

- ID: `RUST-PREFER-CONCEPT-OWNED-MODULES-AND-NAMED-FILES`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Prefer concept-owned modules and named files.

## Why

Modules should be owned by concepts, not by miscellaneous implementation layers. A file named after
the concept gives readers a stable place to find its types, invariants, tests, and docs.

## Helps

Helps readers find the code for a domain concept without translating through arbitrary layers such
as helpers, utils, types, or misc.

## Limits

Infrastructure modules can be useful when the concept really is cross-cutting. Avoid them becoming
catch-all homes for unrelated shared code.

## Agent Instruction

Prefer concept-owned modules and named files because modules should be owned by concepts, not by
miscellaneous implementation layers.

## Mechanisms

Name modules after concepts they own, use `name.rs` files for discoverability, and move helpers near
the concept that gives them meaning.

## References

- [Rust Reference: modules and source files](https://doc.rust-lang.org/reference/items/modules.html)
- [Ed Page Rust Style: source organization](https://epage.github.io/dev/rust-style/)
