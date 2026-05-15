# Rust Docs Validation

## Metadata

- Name: `Rust Docs Validation`
- ID: `rust-docs-validation`
- Status: `reviewed`
- Audience: `both`
- Topics: `rust, rustdoc, docs.rs, doctest, examples`
- Related: `docs-are-contracts`

## Purpose

Build documentation the way users and docs.rs will read it. Rust documentation is often a contract
for public APIs, so doc checks should prove that examples compile, feature-gated docs render, and
release-facing pages can be inspected before publication.

## Supported Principles

- [Docs Are Contracts](../principles/docs-are-contracts.md)
- [Public API Changes Have Downstream Cost](../principles/public-api-changes-have-downstream-cost.md)

## Checks

- Run doctests for public examples and Rustdoc code blocks.

```bash
cargo test --doc
```

- Build local docs without dependency docs when checking project output.

```bash
RUSTDOCFLAGS="-D warnings" cargo doc --no-deps
```

- Open rendered docs during documentation-heavy review when visual navigation matters.

```bash
cargo doc --no-deps --open
```

- Reproduce docs.rs-style configuration when docs.rs behavior is part of the release surface.

```bash
RUSTDOCFLAGS="--cfg docsrs -D warnings" cargo +nightly doc --no-deps --all-features
```

## What It Catches

- Broken doctest examples.
- Missing imports or feature flags in examples.
- Rustdoc warnings promoted to release blockers.
- docs.rs-only configuration gaps.
- Navigation and rendering issues that are hard to see from Markdown or source alone.

## What It Cannot Catch

Documentation builds do not prove that the explanation is helpful or that the documented behavior
is the behavior users need. Pair these checks with review for claim strength, examples, and
contract accuracy.
