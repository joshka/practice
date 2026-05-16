# Rust Make Feature Flags Additive Where Possible

## Metadata

- ID: `RUST-MAKE-FEATURE-FLAGS-ADDITIVE-WHERE-POSSIBLE`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

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
