# Rust Agent Instructions

Use this snippet in Rust repos where maintainability, API shape, and reviewability matter.

```markdown
## Rust Work

Follow the repo's Rust maintainability guide before introducing new abstractions. Optimize for
reader locality, clear ownership, explicit side effects, precise boundaries, and small meaningful
types and functions.

Prefer boring, idiomatic Rust. Use types, constructors, enums, `FromStr`, `TryFrom`, `From`,
`AsRef`, `Borrow`, and iterator traits when they honestly express the contract. Keep visibility
narrow and avoid making dependencies part of the public surface unless that is intentional.

When changing public or reusable APIs, update nearby Rustdoc and examples in the same review unit.
Document errors, panics, safety, side effects, and compatibility when callers need that contract.

Canonical guides:

- `guides/rust-maintainability.md`
- `guides/code-shape.md`
- `guides/boundary-correctness.md`
- `guides/observability-and-failure.md`
```
