# Rust Make Feature Flags Additive Where Possible

## Metadata

- Name: `Make Feature Flags Additive Where Possible`
- ID: `RUST-MAKE-FEATURE-FLAGS-ADDITIVE-WHERE-POSSIBLE`
- Summary: Design feature flags as additive capabilities whenever possible so Cargo feature
  unification does not surprise downstream builds. Make incompatible combinations explicit when
  addition cannot model the real choice.
- Status: `reviewed`
- Domain: `rust`
- Tags: `rust, dependencies, public-api, boundary-correctness`
- Related: `keep-public-dependencies-intentional, rust-document-feature-contracts`

## Rule

Make feature flags additive where possible.

## Why

Rust feature unification means enabling a feature in one dependency path can affect the whole build.
Additive features compose better; non-additive features create surprising behavior when downstream
crates combine dependencies.

## Helps

Helps dependency unification behave predictably when multiple downstream crates enable different
feature sets.

## Limits

Some features are inherently mutually exclusive, such as runtime choices, backend selection, or
no-std/std policy. Make those conflicts explicit and documented.

## Agent Instruction

Make feature flags additive where possible because Rust feature unification means enabling a feature
in one dependency path can affect the whole build.

## Mechanisms

Design features as additive capabilities, avoid disabling behavior through feature flags, document
incompatible combinations, and test representative feature sets in CI.

## References

- [Cargo Book: feature
  unification](https://doc.rust-lang.org/cargo/reference/features.html#feature-unification)
- [Cargo Book: features](https://doc.rust-lang.org/cargo/reference/features.html)
