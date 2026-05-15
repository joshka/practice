# Rust Avoid Path Attribute

## Metadata

- ID: `RUST-AVOID-PATH-ATTRIBUTE`
- Legacy ID: `none`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Avoid `#[path]` unless generated code or platform layout makes it the clearest option.

## Why

`#[path]` breaks the ordinary relationship between module names and file paths. That makes search,
navigation, code ownership, and public API browsing harder because readers cannot infer where code
lives from normal Rust module rules.

The Rust Reference documents detailed path-resolution behavior for `#[path]`, especially inside
inline modules. That complexity is the point: use the standard lookup rules unless the unusual
layout is clearer than the ordinary module-to-file mapping.

## Helps

- Helps module paths remain predictable for readers, tools, and code review.

## Limits

Use `#[path]` for generated code, platform-specific layout, or migration cases where the unusual
layout is clearer than moving files. Prefer named platform modules plus conditional `use` aliases
when that keeps the file layout predictable.

## Agent Instruction

Avoid `#[path]` in Rust modules unless an unusual generated or platform layout is genuinely clearer.

## Mechanisms

Supported by source review, module layout conventions, and generated-code boundaries.

## References

- [Rust Reference: path attribute](https://doc.rust-lang.org/reference/items/modules.html#the-path-attribute)
- [Ed Page Rust Style: Avoid `#[path]`](https://epage.github.io/dev/rust-style/#avoid-path-p-path-mod)
- [Rule: RUST-PREFER-CONCEPT-OWNED-MODULES-AND-NAMED-FILES](rust-prefer-concept-owned-modules-and-named-files.md)
