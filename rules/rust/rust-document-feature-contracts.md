# Rust Document Feature Contracts

## Metadata

- Name: `Document Feature Contracts`
- ID: `RUST-DOCUMENT-FEATURE-CONTRACTS`
- Summary: Explain what each feature flag enables, requires, and promises. Feature contracts help
  users choose combinations without guessing from dependency names.
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Document each feature flag as a public contract.

## Why

Feature flags can add public API, change runtime behavior, enable optional dependencies, affect
platform support, and alter docs.rs output. Downstream users need to know what enabling a feature
does beyond making a build pass.

Cargo features are unified across the dependency graph, so a feature enabled by one dependent can
affect the whole build. That makes feature names, additivity, optional dependencies, and
feature-gated docs part of the public integration contract.

## Helps

- Helps users choose features intentionally and helps maintainers test feature-gated behavior.

## Limits

Purely internal workspace features still need maintainer-facing documentation, but they may not
need public README treatment. Do not document features as implementation toggles when they alter
public API, dependency graph, platform behavior, or runtime semantics.

## Agent Instruction

Document Rust feature flags by naming the public API, runtime behavior, dependencies, platform
support, or docs coverage they enable.

## Mechanisms

Supported by `Cargo.toml` comments where appropriate, README/Rustdoc feature sections, docs.rs
metadata, and feature-combination CI.

## References

- [Cargo Book: features](https://doc.rust-lang.org/cargo/reference/features.html)
- [Rule: RUST-MAKE-FEATURE-FLAGS-ADDITIVE-WHERE-POSSIBLE](rust-make-feature-flags-additive-where-possible.md)
