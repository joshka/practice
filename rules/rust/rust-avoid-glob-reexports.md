# Rust Avoid Glob Reexports

## Metadata

- ID: `RUST-AVOID-GLOB-REEXPORTS`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Avoid glob re-exports in public facades.

## Why

`pub use module::*` hides which names the facade intends to expose. It can accidentally publish new
items when a child module changes and makes public API review harder because the exported set is no
longer visible at the facade.

Microsoft's Pragmatic Rust Guidelines call this out directly for resilient library APIs. A public
facade is a compatibility surface; reviewers should be able to see every exported name without
expanding another module and asking which future additions will leak through.

## Helps

- Helps public API review see every re-exported name and avoid accidental facade expansion.

## Limits

Glob re-exports can be acceptable for generated code, internal preludes, or tightly controlled
facades where the exported set is mechanically audited. Avoid them in public crate roots and module
facades unless the wildcard is itself the documented contract.

## Agent Instruction

Use explicit public re-exports in Rust facades so the exported API is reviewable at the facade.

## Mechanisms

Supported by public API diff tools, lint review, and facade modules that list exported names
explicitly.

## References

- [Rust Reference: use declarations](https://doc.rust-lang.org/reference/items/use-declarations.html)
- [Microsoft Pragmatic Rust Guidelines: Don't Glob Re-Export
  Items](https://microsoft.github.io/rust-guidelines/guidelines/checklist/index.html)
- [Rule: RUST-REEXPORT-FOR-DISCOVERY](rust-reexport-for-discovery.md)
