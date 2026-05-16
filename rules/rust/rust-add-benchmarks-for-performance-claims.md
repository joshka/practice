# Rust Add Benchmarks For Performance Claims

## Metadata

- Name: `Add Benchmarks for Performance Claims`
- ID: `RUST-ADD-BENCHMARKS-FOR-PERFORMANCE-CLAIMS`
- Summary: Use benchmarks when Rust changes rely on speed, allocation, or hot-path claims. The
  evidence makes performance tradeoffs reviewable instead of relying on intuition.
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Add benchmarks where Rust performance claims, hot paths, or allocation behavior matter.

## Why

Performance-sensitive Rust changes are easy to justify from intuition and hard to validate by
inspection. Benchmarks make the goal, input shape, environment, and comparison visible enough for
future maintainers to keep or revise the optimization.

Microsoft's Pragmatic Rust safety guidance is especially strict when `unsafe` is justified by
performance: benchmark first, then document the safety argument. The same evidence habit applies to
safe optimizations that add caching, allocation tricks, concurrency, or dependency complexity.

## Helps

- Helps performance-sensitive changes carry evidence instead of folklore.

## Limits

Do not add benchmark infrastructure for cold code or trivial changes. Use the smallest benchmark
that proves the claim when performance matters. Keep correctness tests separate so a faster wrong
implementation cannot look like a successful optimization.

## Agent Instruction

Benchmark Rust hot paths or allocation-sensitive changes before making or preserving performance
claims.

## Mechanisms

Supported by Criterion or project benchmarks, allocation checks where available, benchmark
provenance notes, and correctness tests before timing tests.

## References

- [Rule: PERFORMANCE-MEASURE-GOAL-CHANGE-COMPARE](../performance/perf-measure-goal-change-compare.md)
- [Microsoft Pragmatic Rust Guidelines: Safety](https://microsoft.github.io/rust-guidelines/guidelines/safety/)
- [Rule: RUST-DOCUMENT-PERFORMANCE-CONTRACTS](rust-document-performance-contracts.md)
