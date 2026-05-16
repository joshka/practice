# Rust Document Visibility Ownership

## Metadata

- ID: `RUST-DOCUMENT-VISIBILITY-OWNERSHIP`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

When a Rust item becomes visible outside its module, its name and docs should make ownership
obvious.

## Why

Widening visibility creates a new surface for other modules or downstream users to depend on. If
the name and docs do not say what concept owns the item, shared internals start to look like stable
API.

The Rust API Guidelines warn that public APIs are stable, and rustdoc should hide unhelpful
implementation details. Even `pub(crate)` creates a crate-wide dependency path, so widening
visibility should be paired with clearer ownership, not just a broader keyword.

## Helps

- Helps prevent accidental shared APIs and makes ownership clear at call sites.

## Limits

Private helpers inside one module do not need public-style docs. Add ownership detail when the item
crosses a module, crate, or public boundary. Prefer reducing visibility when docs would have to
explain that other modules should not really use the item.

## Agent Instruction

Update names and docs while widening Rust visibility so the owning concept and intended callers are
clear.

## Mechanisms

Supported by visibility review, Rustdoc checks, and public API diff review.

## References

- [Rust API Guidelines: public APIs are stable](https://rust-lang.github.io/api-guidelines/necessities.html#c-stable)
- [Rust API Guidelines: Rustdoc does not show unhelpful implementation
  details](https://rust-lang.github.io/api-guidelines/documentation.html#c-hidden)
- [Rule: RUST-DO-NOT-DEFAULT-PUB-CRATE](rust-do-not-default-pub-crate.md)
