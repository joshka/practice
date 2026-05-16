# Rust API And Release Checks

## Metadata

- Name: `Rust API And Release Checks`
- ID: `rust-api-and-release-checks`
- Status: `reviewed`
- Audience: `both`
- Topics: `rust, api, semver, release, cargo`
- Tags: `rust, public-api, release, dependencies, verification`
- Related: `public-api-changes-have-downstream-cost`

## Purpose

Use release-facing checks to protect downstream users from accidental API, feature, packaging, and
minimum-version changes. Rust libraries can break consumers through more than removed functions:
feature unification, public dependency exposure, missing files in packages, raised dependency
minimums, and docs.rs failures can all be real compatibility problems.

## Supported Principles

- [Public API Changes Have Downstream Cost](../principles/public-api-changes-have-downstream-cost.md)
- [Docs Are Contracts](../principles/docs-are-contracts.md)
- [Tests Should Explain Failures](../principles/tests-should-explain-failures.md)

## Checks

- Inspect semver-relevant public API changes.

```bash
cargo semver-checks
```

- Inspect public API shape when a textual API snapshot is useful.

```bash
cargo public-api
```

- Validate package contents before release.

```bash
cargo package --list
cargo package
```

- Inspect feature and optional dependency shape.

```bash
cargo tree -e features
cargo metadata --format-version 1
```

- Validate direct dependency minimums when minimum versions are part of the contract.

```bash
cargo minimal-versions check --direct
```

## Dependency Automation

Use lockfile updates for newer compatible releases. Avoid raising `Cargo.toml` minimum versions
unless the crate actually needs a newer API or behavior. For automation, prefer compatible update
strategies such as `increase-if-necessary` when the goal is to keep CI fresh without changing the
declared minimum support surface.

## What It Cannot Catch

API tools do not know every downstream integration pattern. A technically semver-compatible change
can still be disruptive if it changes behavior, docs, feature defaults, performance contracts, or
trait coherence expectations. Use external usage checks or targeted downstream validation when the
public surface is popular, subtle, or high risk.
