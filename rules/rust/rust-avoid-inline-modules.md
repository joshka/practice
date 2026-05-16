# Rust Avoid Inline Modules

## Metadata

- Name: `Avoid Inline Modules`
- ID: `RUST-AVOID-INLINE-MODULES`
- Summary: Put nontrivial modules in named files unless tests, preludes, or generated code justify
  inline layout. Stable paths make search, review, and ownership clearer.
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Avoid inline modules except for tests, preludes, and generated code.

## Why

Inline modules hide file boundaries and make navigation, search, and ownership harder in larger Rust
crates. Named files give concepts stable homes, while inline modules are best reserved for tests,
small preludes, or generated code with a clear reason.

## Helps

Helps search, review, ownership, and navigation by giving each nontrivial module a stable file path.

## Limits

Inline modules are reasonable for small tests, short preludes, generated code, and examples where a
separate file would hide rather than clarify the concept.

## Agent Instruction

Avoid inline modules except for tests, preludes, and generated code because named files improve
navigation, search, and ownership.

## Mechanisms

Prefer `name.rs` or `name/mod.rs` according to crate convention, move substantial inline modules to
files, and keep module declarations as a readable map.

## References

- [Rust Reference: modules and source files](https://doc.rust-lang.org/reference/items/modules.html)
- [Ed Page Rust Style: source organization](https://epage.github.io/dev/rust-style/)
