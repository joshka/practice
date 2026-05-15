# Measure Before Optimizing

Performance rules cover measuring before optimizing, benchmark provenance, single-run skepticism,
correctness gates, and the cost of complexity or dependency churn.

Use this index to scan the domain and jump to the rule files. The one-line summaries are
for orientation; the rule files hold the rationale, limits, mechanisms, and references.

## Rules

- [`PERF-AVOID-SINGLE-RUN-CONCLUSIONS`](perf-avoid-single-run-conclusions.md). Do not decide
  performance from one short benchmark run. One short benchmark run can be dominated by warmup,
  scheduling, cache state, background load, or measurement noise. Helps: Keeps performance claims
  reviewable and avoids optimizing noise.
- [`PERF-JUSTIFY-COMPLEXITY-CHURN-AND-DEPENDENCIES`](perf-justify-complexity-churn-and-dependencies.md).
  Justify complexity, churn, and dependency cost in performance wins. Performance changes often buy
  speed by adding branches, unsafe code, caching, data structure churn, or dependencies. Helps:
  Keeps performance improvements proportional to their maintenance and downstream costs.
- [`PERF-MEASURE-GOAL-CHANGE-COMPARE`](perf-measure-goal-change-compare.md). Performance changes
  need goal, measurement, change, and comparison. A performance patch is hard to review without
  knowing the goal, baseline, change, and comparison. Helps: Gives reviewers the evidence needed to
  accept or reject a performance tradeoff.
- [`PERF-OPTIMIZE-MEASURED-HOTSPOTS`](perf-optimize-measured-hotspots.md). Optimize measured
  hotspots, not interesting code. Speeding up code that runs once, is not on the critical path, or
  is not visible to users usually wastes review attention. Helps: Focuses optimization on code whose
  runtime contribution justifies changing its shape.
- [`PERF-RECORD-BENCHMARK-PROVENANCE`](perf-record-benchmark-provenance.md). Record benchmark
  provenance. Benchmark numbers without provenance are hard to compare later. Helps: Makes
  performance evidence repeatable enough for future review and regression analysis.
- [`PERF-RUN-CORRECTNESS-FIRST`](perf-run-correctness-first.md). Run correctness before performance
  timing. Fast wrong code is still wrong, and correctness failures can invalidate timing data.
  Helps: Keeps performance work grounded in behavior preservation before speed claims.
- [`PERF-RUN-TIMING-BENCHMARKS-SEQUENTIALLY`](perf-run-timing-benchmarks-sequentially.md). Never run
  timing benchmarks in parallel when timing data matters. Parallel timing benchmarks compete for
  CPU, cache, memory bandwidth, disk, and thermal headroom. Helps: Produces timing data that
  reviewers can treat as meaningful.
