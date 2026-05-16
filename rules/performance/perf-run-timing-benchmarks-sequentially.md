# Perf Run Timing Benchmarks Sequentially

## Metadata

- Name: `Run Timing Benchmarks Sequentially`
- ID: `PERF-RUN-TIMING-BENCHMARKS-SEQUENTIALLY`
- Summary: Serialize timing-sensitive benchmarks when their numbers will be used as evidence.
  Concurrent runs compete for shared resources and can make the comparison describe the runner more
  than the code.
- Status: `reviewed`
- Domain: `performance`
- Depth: `compact`

## Rule

Never run timing benchmarks in parallel when timing data matters.

## Why

Parallel timing benchmarks compete for CPU, cache, memory bandwidth, disk, and thermal headroom.
Running them concurrently can make both results noisy enough that the comparison says more about the
runner than the code.

## Helps

- Produces timing data that reviewers can treat as meaningful.

## Limits

Parallel CI is fine for correctness checks. Serialize timing-sensitive benchmarks or isolate them on
stable runners when the numbers are used as evidence.

## Agent Instruction

Run timing benchmarks sequentially so CPU, cache, memory, disk, and thermal contention do not
distort results.

## Mechanisms

Supported by sequential benchmark scripts, CI concurrency controls, dedicated benchmark jobs, and
benchmark documentation that names runner conditions.

## References

- [Principle: Measure Before Optimizing](../../principles/measure-before-optimizing.md)
- [Microsoft Pragmatic Rust Guidelines: hot path
  performance](https://microsoft.github.io/rust-guidelines/agents/all.txt#M-HOTPATH)
- [Microsoft Pragmatic Rust Guidelines: throughput
  requirements](https://microsoft.github.io/rust-guidelines/agents/all.txt#M-THROUGHPUT)
