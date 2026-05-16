# Rust Keep Ci High Signal

## Metadata

- Name: `Keep CI High Signal`
- ID: `RUST-KEEP-CI-HIGH-SIGNAL`
- Summary: Keep required Rust checks strict, fast, deterministic, and actionable. Slow or flaky
  ritual trains maintainers to ignore failures while real drift accumulates.
- Status: `reviewed`
- Domain: `rust`
- Tags: `rust, verification, testing, automation`
- Related: `smallest-trustworthy-verification, tests-should-explain-failures`

## Rule

Keep Rust CI strict, fast, deterministic, and high-signal.

## Why

CI should make quality cheaper. A pile of slow, flaky, redundant, or low-signal jobs trains
maintainers to ignore failures, while missing fast checks lets formatting, docs, feature, and MSRV
drift accumulate.

The Pragmatic Rust checklist emphasizes static verification, upstream guidelines, documentation,
feature behavior, and safety checks. Those checks are useful when they produce actionable failures
at the right cadence. Required PR CI should catch common regressions quickly; slower evidence belongs
in scheduled, manual, or release workflows.

## Helps

- Helps required checks catch real regressions without burying maintainers in ritual.

## Limits

Expensive fuzzing, exhaustive compatibility checks, and long benchmarks can be valuable. Put them in
scheduled, manual, or release workflows when they are not suitable for required PR CI.
Do not remove a slow check without replacing the release or scheduled evidence it provided.

## Agent Instruction

Keep Rust PR CI focused on fast deterministic gates, and move expensive checks to scheduled,
manual, or release workflows.

## Mechanisms

Supported by `cargo fmt`, clippy, tests, docs, feature matrices, MSRV jobs, platform jobs, scheduled
fuzzing, and manual benchmark workflows.

## References

- [Rule: TEST-CHECK-MAINTAINER-COMMANDS-IN-CI](../testing/test-check-maintainer-commands-in-ci.md)
- [Rule: TEST-KEEP-SLOW-CHECKS-OUT-OF-PR-CI](../testing/test-keep-slow-checks-out-of-pr-ci.md)
- [Microsoft Pragmatic Rust Guidelines:
  Checklist](https://microsoft.github.io/rust-guidelines/guidelines/checklist/index.html)
