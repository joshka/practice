# Perf Optimize Measured Hotspots

## Metadata

- Name: `Optimize Measured Hotspots`
- ID: `PERF-OPTIMIZE-MEASURED-HOTSPOTS`
- Summary: Optimize code that measurement shows is on the important runtime path. This keeps review
  attention on changes whose user-visible impact justifies altering the code shape.
- Status: `reviewed`
- Domain: `performance`
- Tags: `performance, verification, change-shape`
- Related: `measure-before-optimizing, encode-nonfunctional-requirements, cap-change-radius`

## Rule

Optimize measured hotspots, not interesting code.

## Why

Speeding up code that runs once, is not on the critical path, or is not visible to users usually
wastes review attention. A tiny percentage win in a hot loop can matter more than a large percentage
win in cold setup code.

## Helps

- Focuses optimization on code whose runtime contribution justifies changing its shape.

## Limits

Small cleanup that also improves performance is fine when readability does not suffer. Call it a
cleanup unless measurement shows performance is the reason to land it.

## Agent Instruction

Optimize measured hotspots, not interesting code that runs once, is off the critical path, or is
invisible to users.

## Mechanisms

Supported by profiling, flamegraphs, tracing, workload counters, benchmark selection, and PR notes
that identify why the target is hot.

## References

- [Principle: Measure Before Optimizing](../../principles/measure-before-optimizing.md)
- [Microsoft Pragmatic Rust Guidelines: hot path
  performance](https://microsoft.github.io/rust-guidelines/agents/all.txt#M-HOTPATH)
- [Microsoft Pragmatic Rust Guidelines: throughput
  requirements](https://microsoft.github.io/rust-guidelines/agents/all.txt#M-THROUGHPUT)
