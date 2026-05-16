# Rust Run Feature Gated Validation

## Metadata

- ID: `RUST-RUN-FEATURE-GATED-VALIDATION`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Run feature-gated tests and docs when changing feature-gated Rust integrations.

## Why

Feature-gated code can compile, document, and behave differently from the default build. A change to
an optional integration is not validated by default-feature tests alone.

Cargo features are additive across a resolved dependency graph, and docs.rs often builds with a
selected feature set. That means feature-gated API, examples, and docs need direct validation; a
default build can miss missing imports, broken docs, or incompatible optional dependency versions.

## Helps

- Helps optional integrations stay buildable, documented, and behaviorally covered.

## Limits

Do not run every expensive feature matrix on every small edit. Choose the feature combinations that
cover the changed surface and keep slower combinations scheduled or manual. Always include the
feature combination that users are told to enable in docs or examples.

## Agent Instruction

Validate the feature combinations affected by a Rust change, including docs for features that change
public items.

## Mechanisms

Supported by `cargo test --all-features`, targeted `--features` checks, docs builds with selected
features, and CI matrices for important combinations.

## References

- [Cargo Book: features](https://doc.rust-lang.org/cargo/reference/features.html)
- [docs.rs: metadata](https://docs.rs/about/metadata)
- [Rule: TEST-CHECK-IMPORTANT-FEATURE-COMBINATIONS](../testing/test-check-important-feature-combinations.md)
