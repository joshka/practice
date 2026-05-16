# Rust Tooling Profile

## Metadata

- Name: `Rust Tooling Profile`
- ID: `rust-tooling-profile`
- Status: `reviewed`
- Audience: `both`
- Topics: `rust, lints, rustfmt, cargo, ci, agents`
- Tags: `rust, tooling, automation, verification, release`
- Related: `docs-are-contracts, measure-before-optimizing, public-api-changes-have-downstream-cost`

## Purpose

Use mechanical tooling to support durable Rust rules where tools can catch drift, make review
cheaper, or encode project policy. Tooling should make the preferred path easier without pretending
that lints and checks replace design judgment.

## Supported Principles

- [Docs Are Contracts](../principles/docs-are-contracts.md)
- [Measure Before Optimizing](../principles/measure-before-optimizing.md)
- [Public API Changes Have Downstream Cost](../principles/public-api-changes-have-downstream-cost.md)
- [Tests Should Explain Failures](../principles/tests-should-explain-failures.md)
- [JJ Topology Is Repo Role Dependent](../principles/jj-topology-is-repo-role-dependent.md)

## Rust Lints

- Use `unsafe_code = "forbid"` for crates that should remain safe Rust.
- Use `undocumented_unsafe_blocks` when unsafe is intentional and every block needs a local
  `SAFETY:` explanation.
- Use `missing_docs` for library crates where public documentation is part of the API contract.
- Consider `missing_debug_implementations` for public library types where diagnostics matter.
- Use `unfulfilled_lint_expectations` with `#[expect(..., reason = "...")]` so stale suppressions
  are visible.
- Enable Clippy policy selectively when the lint encodes a real project rule rather than generic
  preference churn.

## Formatting

- Run `cargo fmt --check` in CI.
- Use `rustfmt.toml` only for stable house choices the project actually wants to enforce.
- Prefer module-based imports and `name.rs` files over broad single-import lists and `mod.rs`
  layouts unless local conventions differ.
- Use `markdownlint-cli2` for Markdown line length, fences, blank lines around blocks, and ordered
  list style.

## Cargo And Rustdoc Checks

- Run `cargo clippy --all-targets --all-features` when feature cost is acceptable.
- Run `cargo test` or `cargo nextest` for normal correctness gates.
- Run `cargo test --doc` for public examples and Rustdoc compatibility.
- Run `cargo doc --no-deps` with `RUSTDOCFLAGS="-D warnings"` when Rustdoc quality matters.
- Use `cargo doc --open` when rendered docs should be easy for a maintainer to inspect.
- Use docs.rs-parity builds for release-facing docs, including the project's docs.rs-equivalent
  feature set, `cargo +nightly doc`, `RUSTDOCFLAGS="--cfg docsrs"`, and `--no-deps` where
  appropriate.

## API And Release Checks

- Use `cargo-semver-checks` for semver-relevant public API changes.
- Use `cargo public-api` to snapshot or inspect public API shape.
- Use `cargo package --list` and `cargo package` to inspect release artifacts.
- Use `cargo tree -e features` and `cargo metadata` to audit feature and optional dependency shape.
- Use `cargo minimal-versions check --direct` or direct minimal-version resolution to validate
  declared direct dependency minimums.
- Configure dependency automation with `versioning-strategy: increase-if-necessary` when the goal
  is compatible lockfile refresh rather than raising manifest minimums.

## Matrix And Heavy Checks

- Use `cargo hack` for no-default, each-feature, all-features, and selected feature combinations.
- Use pinned toolchain CI or MSRV checks when MSRV is part of the public contract.
- Use fuzzing or property tests for parsers, decoders, state machines, and untrusted input.
- Use `criterion`, repeated `hyperfine`, or saved benchmark scripts for performance claims.

## Agentic Tooling

- Prefer Git-formatted diffs when agents need to interpret patch output.
- Configure `JJ_PAGER=cat` for unattended jj command execution.
- Use repo-scoped jj aliases when the repo topology is known.
- Add `AGENTS.override.md` to global Git excludes for local-only Codex notes that must not be
  committed.
- Turn repeated feedback into scripts, lints, templates, generated checks, or review checklists
  before relying on prompts.

## Limits

Do not add tools just to look rigorous. Each mechanism should identify the rule it supports, the
failure it catches, and the cost it adds. Heavy checks belong in release or targeted validation
when they would make the normal edit loop too slow.
