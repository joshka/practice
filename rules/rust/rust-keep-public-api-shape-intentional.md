# Rust Keep Public API Shape Intentional

## Metadata

- Name: `Keep Public API Shape Intentional`
- ID: `RUST-KEEP-PUBLIC-API-SHAPE-INTENTIONAL`
- Summary: Make public visibility, aliases, features, re-exports, bounds, and variants reflect
  intended commitments. Published surface area becomes something downstream users can depend on.
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Keep public API shape intentional.

## Why

Every public item becomes something users can import, name, document, and depend on. Public API
shape should reflect intended concepts and compatibility commitments, not whichever helpers happened
to need cross-module access during implementation.

## Helps

Helps prevent accidental semver commitments through visibility, type aliases, features, re-exports,
trait bounds, and error variants.

## Limits

Examples, prototypes, and private binaries can move faster. Published libraries need slower
public-surface changes because downstream code depends on them.

## Agent Instruction

Keep public API shape intentional because every public item becomes something users can import, name,
document, and depend on.

## Mechanisms

Review public items explicitly, run semver or public API checks when available, document intended
extension points, and prefer private visibility until an item is meant for users.

## References

- [Cargo Book: SemVer compatibility](https://doc.rust-lang.org/cargo/reference/semver.html)
- [Rust API Guidelines: public dependencies are
  stable](https://rust-lang.github.io/api-guidelines/necessities.html#c-stable)
