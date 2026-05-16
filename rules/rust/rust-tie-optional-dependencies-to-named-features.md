# Rust Tie Optional Dependencies To Named Features

## Metadata

- Name: `Tie Optional Dependencies To Named Features`
- ID: `RUST-TIE-OPTIONAL-DEPENDENCIES-TO-NAMED-FEATURES`
- Summary: Connect optional dependencies to clear feature names that explain the capability callers
  enable. Avoid leaking dependency names as the public feature design when the capability needs a
  more stable contract.
- Status: `reviewed`
- Domain: `rust`
- Tags: `rust, dependencies, public-api, documentation`
- Related: `rust-make-feature-flags-additive-where-possible, keep-public-dependencies-intentional`

## Rule

Keep optional dependencies tied to clearly named features.

## Why

Optional dependencies become part of the feature contract. Named features should explain why the
dependency exists and let downstream users opt into integrations deliberately instead of inheriting
surprise dependencies.

## Helps

Helps downstream users understand why an optional dependency exists and how enabling it changes
compile time, platform support, and API surface.

## Limits

Workspace-private crates can be simpler when no external user chooses features. Published crates
should make optional dependency features intentional and documented.

## Agent Instruction

Keep optional dependencies tied to clearly named features because they become part of the feature
contract.

## Mechanisms

Give optional dependencies named features, avoid exposing raw dependency names when a domain feature
is clearer, and test feature combinations that users are likely to enable.

## References

- [Cargo Book: optional
  dependencies](https://doc.rust-lang.org/cargo/reference/features.html#optional-dependencies)
- [Cargo Book: features](https://doc.rust-lang.org/cargo/reference/features.html)
