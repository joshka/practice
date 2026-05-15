# Rust Keep Pre Release Compatibility Intentional

## Metadata

- ID: `RUST-KEEP-PRE-RELEASE-COMPATIBILITY-INTENTIONAL`
- Legacy ID: `none`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Do not preserve accidental development-era compatibility in pre-release crates.

## Why

Before a crate commits to stable public API, preserving accidental names, re-exports, features, or
error variants can freeze poor shapes early. Pre-release cleanup is often cheaper than carrying
compatibility shims that make the intended API harder to learn.

Cargo's versioning model treats `0.x` compatibility differently from `1.x`, but downstream users
can still depend on pre-release crates. The point is not to break users casually; it is to avoid
pretending an accidental development shape is a durable contract before the maintainer has chosen
that contract.

## Helps

- Helps pre-release crates converge on intentional public shape before semver compatibility hardens.

## Limits

Keep compatibility when real users already depend on the shape, migration cost is high, or the
project has promised stability despite a pre-1.0 version. If you remove accidental compatibility,
make the intended replacement clear in docs or release notes.

## Agent Instruction

Clean up accidental pre-release Rust API compatibility when the crate has not promised that shape
and the intended API becomes clearer.

## Mechanisms

Supported by semver review, changelog notes, migration examples, and public API diff tools.

## References

- [Cargo Book: specifying dependencies](https://doc.rust-lang.org/cargo/reference/specifying-dependencies.html)
- [Rust API Guidelines: public APIs are stable](https://rust-lang.github.io/api-guidelines/necessities.html#c-stable)
