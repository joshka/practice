# Measure Before Optimizing

## Metadata

- Name: `Measure Before Optimizing`
- ID: `measure-before-optimizing`
- Summary: `Performance work needs a workload, baseline, goal, change, and comparison. Evidence
  keeps optimization from becoming readability, dependency, or API churn without a proven payoff.`
- Status: `reviewed`
- Audience: `both`
- Topics: `performance, testing, review`
- Related: `smallest-trustworthy-verification, review-proof-not-just-code`

## Claim

Do not optimize for performance until the changed code is shown to matter in the relevant workload.
Performance changes need a goal, a measurement, a change, and a comparison.

## Why I Believe This

Optimizing cold code can waste review attention while making the system harder to maintain.
Changing a once-per-command path from 20 ms to 10 ms rarely matters. Improving a hot path by a
small percentage can matter if it runs millions of times. The cost is not just time spent measuring:
performance-motivated diffs often add complexity, dependencies, public churn, or less readable
code.

Evidence keeps the tradeoff honest. Without a workload and before/after comparison, a performance
claim is indistinguishable from churn.

## What This Changes

Treat performance as a hypothesis:

1. Name the relevant workload.
1. Identify the hot path.
1. State the performance goal.
1. Measure the baseline.
1. Change the code.
1. Compare with the same workload.
1. Report complexity, dependency, readability, and API tradeoffs.

## Good Uses

- Profiling points to a rendering loop called for every cell.
- A benchmark captures a parser workload from realistic input.
- A trace shows a repeated allocation inside a high-frequency path.
- A dependency avoids substantial hot-path work and its maintenance cost is justified.

## Bad Smells

- The PR says "faster" but has no workload or baseline.
- The optimized code is harder to read and the path is not known to be hot.
- A dependency is added for a tiny improvement in a cold path.
- The benchmark measures a synthetic case that does not represent real use.
- The change raises public API or downstream churn without proving the payoff.

## Mechanisms

- Profilers, tracing spans, flamegraphs, and call counts.
- `criterion`, repeated `hyperfine`, or saved benchmark scripts.
- Realistic corpora and representative fixtures.
- Benchmark output stored or summarized with enough detail for review.
- Diff review that weighs runtime gain against complexity and dependency cost.

## Rules This Supports

- `PERF-OPTIMIZE-MEASURED-HOTSPOTS`
- `PERF-MEASURE-GOAL-CHANGE-COMPARE`
- `PERF-JUSTIFY-COMPLEXITY-CHURN-AND-DEPENDENCIES`

## Agent Consequences

Do not make performance-motivated changes without evidence that the path matters. Report the
workload, baseline, changed result, and tradeoff. If a cleanup also happens to remove waste, describe
it as simplification unless performance was actually measured.

## Limits

Removing obviously wasteful work is fine when it also simplifies code and does not claim a
performance win. Exploratory profiling can happen before a goal is finalized, but it should not land
as a performance change without comparison.

## References

| Source                                 | Use        | Note                                             |
| -------------------------------------- | ---------- | ------------------------------------------------ |
| [Microsoft hot path][ms-hotpath]       | `supports` | Optimization should focus on relevant hot paths. |
| [Microsoft throughput][ms-throughput]  | `supports` | Throughput claims need evidence.                 |

[ms-hotpath]: https://microsoft.github.io/rust-guidelines/agents/all.txt#M-HOTPATH
[ms-throughput]: https://microsoft.github.io/rust-guidelines/agents/all.txt#M-THROUGHPUT
