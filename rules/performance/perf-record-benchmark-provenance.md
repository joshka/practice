# Perf Record Benchmark Provenance

## Metadata

- Name: `Record Benchmark Provenance`
- ID: `PERF-RECORD-BENCHMARK-PROVENANCE`
- Summary: Record the commands, inputs, tool versions, build profile, and runner conditions behind
  benchmark numbers. Provenance makes future comparisons meaningful and helps separate real changes
  from environment drift.
- Status: `reviewed`
- Domain: `performance`
- Tags: `performance, verification, tooling, source-truth`
- Related: `measure-before-optimizing, report-verification-honestly, prefer-durable-summaries`

## Rule

Record benchmark provenance.

## Why

Benchmark numbers without provenance are hard to compare later. Tool version, command line, input
data, machine class, feature flags, build profile, and run conditions can explain differences that
would otherwise look like regressions or wins.

## Helps

- Makes performance evidence repeatable enough for future review and regression analysis.

## Limits

Do not over-document throwaway exploration. Record provenance for numbers used to justify a change
or track a release-facing claim.

## Agent Instruction

Record benchmark provenance so timing numbers remain comparable later.

## Mechanisms

Supported by checked benchmark scripts, saved fixture data, Criterion reports, `hyperfine
--export-*`, PR notes, and CI artifacts for stable benchmark jobs.

## References

- [Principle: Measure Before Optimizing](../../principles/measure-before-optimizing.md)
- [Microsoft Pragmatic Rust Guidelines: hot path
  performance](https://microsoft.github.io/rust-guidelines/agents/all.txt#M-HOTPATH)
- [Microsoft Pragmatic Rust Guidelines: throughput
  requirements](https://microsoft.github.io/rust-guidelines/agents/all.txt#M-THROUGHPUT)
