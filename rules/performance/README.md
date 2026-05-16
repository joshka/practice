# Measure Before Optimizing

Performance rules cover measuring before optimizing, benchmark provenance, single-run skepticism,
correctness gates, and the cost of complexity or dependency churn.

Use this index to scan the domain and jump to the rule files. The one-line summaries are
for orientation; the rule files hold the rationale, limits, mechanisms, and references.

## Rules

- [`PERF-AVOID-SINGLE-RUN-CONCLUSIONS`](perf-avoid-single-run-conclusions.md). Do not land
  performance conclusions from one short benchmark run. Repeat and contextualize timing evidence
  because warmup, scheduling, cache state, and background load can make a single result
  non-reproducible.
- [`PERF-JUSTIFY-COMPLEXITY-CHURN-AND-DEPENDENCIES`](perf-justify-complexity-churn-and-dependencies.md).
  Explain why a performance win justifies added complexity, churn, unsafe code, caching, or
  dependencies. Measured speedups still need to pay for the maintenance cost every future reader
  inherits.
- [`PERF-MEASURE-GOAL-CHANGE-COMPARE`](perf-measure-goal-change-compare.md). State the performance
  goal, baseline measurement, implementation change, and comparison result together. Those pieces
  let reviewers judge whether the patch improved the relevant workload enough to justify its
  tradeoffs.
- [`PERF-OPTIMIZE-MEASURED-HOTSPOTS`](perf-optimize-measured-hotspots.md). Optimize code that
  measurement shows is on the important runtime path. This keeps review attention on changes whose
  user-visible impact justifies altering the code shape.
- [`PERF-RECORD-BENCHMARK-PROVENANCE`](perf-record-benchmark-provenance.md). Record the commands,
  inputs, tool versions, build profile, and runner conditions behind benchmark numbers. Provenance
  makes future comparisons meaningful and helps separate real changes from environment drift.
- [`PERF-RUN-CORRECTNESS-FIRST`](perf-run-correctness-first.md). Run relevant correctness checks
  before interpreting performance timing. Fast code that changes behavior invalidates the benchmark
  claim and wastes review effort.
- [`PERF-RUN-TIMING-BENCHMARKS-SEQUENTIALLY`](perf-run-timing-benchmarks-sequentially.md). Serialize
  timing-sensitive benchmarks when their numbers will be used as evidence. Concurrent runs compete
  for shared resources and can make the comparison describe the runner more than the code.
