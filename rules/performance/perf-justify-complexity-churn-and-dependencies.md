# Perf Justify Complexity Churn And Dependencies

## Metadata

- ID: `PERF-JUSTIFY-COMPLEXITY-CHURN-AND-DEPENDENCIES`
- Status: `reviewed`
- Domain: `performance`
- Depth: `compact`

## Rule

Justify complexity, churn, and dependency cost in performance wins.

## Why

Performance changes often buy speed by adding branches, unsafe code, caching, data structure churn,
or dependencies. A small or unmeasured win may not justify the long-term cost paid by every future
reader and maintainer.

## Helps

- Keeps performance improvements proportional to their maintenance and downstream costs.

## Limits

Accept complexity when the measured hotspot matters and the new shape is still explainable. Reject
cleverness when the win is marginal, speculative, or outside the workload users care about.

## Agent Instruction

Justify complexity, churn, and dependency cost because performance work adds branches, unsafe code,
caching, data structure churn, or dependencies.

## Mechanisms

Supported by before/after benchmarks, complexity notes in PR descriptions, dependency audits, code
comments for non-obvious optimizations, and follow-up cleanup tasks.

## References

- [Principle: Measure Before Optimizing](../../principles/measure-before-optimizing.md)
- [Microsoft Pragmatic Rust Guidelines: hot path
  performance](https://microsoft.github.io/rust-guidelines/agents/all.txt#M-HOTPATH)
- [Microsoft Pragmatic Rust Guidelines: throughput
  requirements](https://microsoft.github.io/rust-guidelines/agents/all.txt#M-THROUGHPUT)
