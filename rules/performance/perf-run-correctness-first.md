# Perf Run Correctness First

## Metadata

- ID: `PERF-RUN-CORRECTNESS-FIRST`
- Status: `reviewed`
- Domain: `performance`
- Depth: `compact`

## Rule

Run correctness before performance timing.

## Why

Fast wrong code is still wrong, and correctness failures can invalidate timing data. Running
correctness checks first prevents time spent interpreting benchmarks from an implementation that
does not preserve the behavior under test.

## Helps

- Keeps performance work grounded in behavior preservation before speed claims.

## Limits

During exploratory profiling, partial correctness may be enough to locate a hotspot. Before landing,
run the relevant correctness checks and report any gaps.

## Agent Instruction

Run correctness before performance timing because fast wrong code is still wrong, and correctness
failures can invalidate timing data.

## Mechanisms

Supported by tests before benchmarks, regression tests for optimized paths, invariant checks, and PR
validation that separates correctness evidence from timing evidence.

## References

- [Principle: Measure Before Optimizing](../../principles/measure-before-optimizing.md)
- [Microsoft Pragmatic Rust Guidelines: hot path
  performance](https://microsoft.github.io/rust-guidelines/agents/all.txt#M-HOTPATH)
- [Microsoft Pragmatic Rust Guidelines: throughput
  requirements](https://microsoft.github.io/rust-guidelines/agents/all.txt#M-THROUGHPUT)
