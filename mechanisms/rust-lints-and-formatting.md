# Rust Lints And Formatting

## Metadata

- Name: `Rust Lints And Formatting`
- ID: `rust-lints-and-formatting`
- Status: `reviewed`
- Audience: `both`
- Topics: `rust, clippy, rustfmt, lint, markdownlint`
- Tags: `rust, tooling, automation, documentation, verification`
- Related: `explicit-boundaries-preserve-correctness`

## Purpose

Use lints and formatting for rules that should be enforced mechanically. Formatting should remove
style debate from review. Lints should encode actual project policy, not generic cleverness or churn
that makes code harder to read.

## Supported Principles

- [Explicit Boundaries Preserve Correctness](../principles/explicit-boundaries-preserve-correctness.md)
- [Docs Are Contracts](../principles/docs-are-contracts.md)
- [Agent Instructions Are Operational Controls](../principles/agent-instructions-are-operational-controls.md)

## Rust Lints

- Use `unsafe_code = "forbid"` when the crate intends to stay in safe Rust.
- Use `undocumented_unsafe_blocks` when unsafe is allowed but every unsafe block needs a local
  `SAFETY:` explanation.
- Use `missing_docs` when public documentation is part of the library contract.
- Consider `missing_debug_implementations` for public types that appear in diagnostics.
- Use `unfulfilled_lint_expectations` with `#[expect(..., reason = "...")]` so stale suppressions
  are visible.

## Formatting

- Run `cargo fmt --check` in CI.
- Keep `rustfmt.toml` focused on stable house choices that the project truly wants.
- Prefer module-based imports and `name.rs` module files unless local conventions differ.
- Use `markdownlint-cli2` for Markdown line length, fenced code blocks, blank lines around blocks,
  and ordered-list marker shape.

## What It Cannot Catch

Lint-clean code can still have poor boundaries, confusing names, weak tests, or an unstable public
API. Treat lints as guardrails around reviewed judgment, not as proof that the design is good.
