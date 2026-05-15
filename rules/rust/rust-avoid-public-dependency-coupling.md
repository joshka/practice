# Rust Avoid Public Dependency Coupling

## Metadata

- ID: `RUST-AVOID-PUBLIC-DEPENDENCY-COUPLING`
- Legacy ID: `R-0201`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Avoid leaking dependency types in public APIs unless integration is the point.

## Why

Public APIs that expose dependency types force downstream users to care about that dependency
version, feature set, and semantics. Leak those types only when integration with the dependency is
the point of the API, not as an implementation convenience.

## Helps

Helps preserve semver freedom by keeping implementation dependencies from becoming downstream
compile-time, feature, and version requirements.

## Limits

Expose dependency types when interoperability is the purpose, such as adapters, trait integrations,
ecosystem standard types, or APIs explicitly built around that dependency.

## Agent Instruction

Avoid leaking dependency types in public APIs unless integration is the point; exposed dependency
types make downstream users care about that dependency's version, features, and semantics.

## Mechanisms

Use local wrapper types, conversion traits, feature-gated integration modules, borrowed standard
types, or private dependency types behind stable public contracts.

## References

- [Rust API Guidelines: conversions use standard
  traits](https://rust-lang.github.io/api-guidelines/interoperability.html#c-conv-traits)
- [Cargo Book: SemVer compatibility](https://doc.rust-lang.org/cargo/reference/semver.html)
