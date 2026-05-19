# Perf Measure Goal Change Compare

## Metadata

- Name: `Measure Goal, Change, and Comparison`
- ID: `PERF-MEASURE-GOAL-CHANGE-COMPARE`
- Summary: State the performance goal, baseline measurement, implementation change, and comparison
  result together. Those pieces let reviewers judge whether the patch improved the relevant
  workload enough to justify its tradeoffs.
- Status: `reviewed`
- Domain: `performance`
- Tags: `performance, verification, reviewability`
- Related: `measure-before-optimizing, review-proof-not-just-code, write-pr-narrative`

## Rule

Performance changes need goal, measurement, change, and comparison.

## Why

A performance patch is hard to review without knowing the goal, baseline, change, and comparison.
Those four pieces show whether the work targeted a real problem, improved the relevant workload, and
paid for any complexity it introduced.

## Helps

- Gives reviewers the evidence needed to accept or reject a performance tradeoff.

## Limits

Exploration can start looser, but the final change should state enough measurement context for
another person to understand the claim.

## Agent Instruction

State the performance goal, measurement, change, and comparison so reviewers can evaluate the patch.

## Mechanisms

Supported by benchmark scripts, profiler output, saved command lines, workload descriptions, and PR
sections for goal, baseline, result, and tradeoff.

## References

- [Principle: Measure Before Optimizing](../../principles/measure-before-optimizing.md)
- [Microsoft Pragmatic Rust Guidelines: hot path
  performance](https://microsoft.github.io/rust-guidelines/agents/all.txt#M-HOTPATH)
- [Microsoft Pragmatic Rust Guidelines: throughput
  requirements](https://microsoft.github.io/rust-guidelines/agents/all.txt#M-THROUGHPUT)
