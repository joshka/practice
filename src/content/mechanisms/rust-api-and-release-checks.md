# Rust API And Release Checks

## Metadata

- Name: `Rust API And Release Checks`
- ID: `rust-api-and-release-checks`
- Summary: Cargo release, semver, feature, packaging, and minimum-version checks protect downstream
  users from accidental compatibility changes. Use these checks when public API, crate metadata, or
  release artifacts are part of the changed surface.
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

Choose checks for the affected contract. A passing workspace build is not evidence for every
published crate, target, or feature combination. Select the supported release baseline explicitly
when using API comparison tools; confirm installed tool options before relying on their defaults.

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

## Consumer Configurations

When feature forwarding or target support changes, use a small downstream crate outside the
workspace. Check the facade and any directly consumable component crates separately, with their
documented feature sets and default features disabled where required. Workspace feature unification
or dev-dependencies can otherwise supply a missing feature and hide the defect.

Choose a target that actually lacks the capability being tested. A `no_std` target with native
atomics does not establish support for a target without pointer atomics. Record the target and
feature configuration with the result, including prerequisites supplied by the consumer.

For a compatibility claim, run the same legal consumer against the baseline and candidate. A
candidate-only failure establishes a defect, but does not alone establish that the PR introduced it.
Use [Validate Semver Breaks Against External Use][semver] to separate release consequences from
design preferences.

## Packaged Artifact

Inspect the package listing for required assets, fixture inputs, and locally linked documentation.
When consumers need these files, unpack the archive into an isolated location and run the relevant
checks there. Nested Cargo packages may be excluded even when a broad include pattern names their
parent directory. An archive can compile successfully while still omitting files needed by tests
or documented workflows.

Keep source fixtures unchanged during validation. If fixture manifests need a stored template form
to be packaged, materialize runnable copies in temporary directories and test that construction
path as part of archive validation.

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

## References

- [Cargo feature unification](https://doc.rust-lang.org/cargo/reference/features.html#feature-unification)
- [Cargo package contents](https://doc.rust-lang.org/cargo/reference/manifest.html#the-exclude-and-include-fields)
- [Cargo package verification](https://doc.rust-lang.org/cargo/commands/cargo-package.html)

[semver]: ../rules/rust/rust-validate-semver-breaks-against-external-use.md
