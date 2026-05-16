# Rust Use Doc Inline For Canonical Reexports

## Metadata

- Name: `Use Doc Inline For Canonical Reexports`
- ID: `RUST-USE-DOC-INLINE-FOR-CANONICAL-REEXPORTS`
- Summary: Use `#[doc(inline)]` when a re-export should be the canonical place readers encounter an
  item. Avoid inlining re-exports that would obscure the owning module or create duplicate-looking
  documentation.
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Use `#[doc(inline)]` when a re-export is the canonical path readers should land on.

## Why

Rustdoc can show a re-export as a link away from the facade or inline the item's documentation at
the facade. Inlining is useful when the facade path is the intended public path and users should not
have to chase the implementation module first.

The rustdoc book describes `#[doc(inline)]` as the mechanism for making a re-export appear as part
of the facade's item listing. Microsoft's Pragmatic Rust checklist also recommends marking `pub use`
items with `#[doc(inline)]` when that public path is what users should see.

## Helps

- Helps Rustdoc present canonical public paths without hiding implementation ownership in source.

## Limits

Do not inline every re-export. Use links when the child module is the better place to understand the
concept or when duplicating docs at the facade makes the page noisy. Review the rendered docs
instead of assuming the attribute produced the intended navigation.

## Agent Instruction

Use `#[doc(inline)]` only for Rust re-exports whose facade path is the canonical public landing
point.

## Mechanisms

Supported by `cargo doc`, docs.rs review, and facade documentation checks.

## References

- [rustdoc book: Re-exports](https://doc.rust-lang.org/rustdoc/write-documentation/re-exports.html)
- [Microsoft Pragmatic Rust Guidelines: Mark `pub use` Items with
  `#[doc(inline)]`](https://microsoft.github.io/rust-guidelines/guidelines/checklist/index.html)
- [Rule: RUST-REEXPORT-FOR-DISCOVERY](rust-reexport-for-discovery.md)
