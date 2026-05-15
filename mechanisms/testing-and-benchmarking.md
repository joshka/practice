# Testing And Benchmarking

## Metadata

- Name: `Testing And Benchmarking`
- ID: `testing-and-benchmarking`
- Status: `reviewed`
- Audience: `both`
- Topics: `tests, ci, benchmarks, fuzzing, cargo`
- Related: `tests-should-explain-failures, measure-before-optimizing`

## Purpose

Choose validation tools by the kind of risk being controlled. Fast local checks protect the edit
loop. Broader CI matrices protect integration surfaces. Heavy checks such as fuzzing, property
tests, feature matrices, or benchmarks should be targeted at risks where the added runtime buys
real information.

## Supported Principles

- [Tests Should Explain Failures](../principles/tests-should-explain-failures.md)
- [Measure Before Optimizing](../principles/measure-before-optimizing.md)
- [Public API Changes Have Downstream Cost](../principles/public-api-changes-have-downstream-cost.md)

## Normal Checks

- Run `cargo test` or `cargo nextest run` for normal correctness gates.
- Run format and lint checks early when they are cheap and deterministic.
- Keep slow or flaky checks out of the default PR loop unless they control a high-value risk.

## Feature And Boundary Checks

- Use `cargo hack` for no-default, each-feature, all-features, and selected feature combinations.
- Use pinned toolchain or MSRV checks when Rust version support is a public contract.
- Use realistic parser samples for formats, protocols, and integrations.
- Use fuzzing or property tests for parsers, decoders, state machines, and untrusted input.

## Performance Checks

- Use `criterion`, repeated `hyperfine`, or saved benchmark scripts for performance claims.
- Record benchmark provenance: command, dataset, environment, compared revisions, and goal.
- Optimize measured hotspots, not code that merely looks inefficient.

## What It Cannot Catch

More tests do not automatically make a change safer. Tests with opaque assertions, unrealistic
fixtures, or noisy failures can increase maintenance cost without helping the next developer fix the
problem. Prefer failures that point directly at the broken contract.
