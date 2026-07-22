# Characterize Then Fix

## Metadata

- Name: `Characterize Then Fix`
- ID: `characterize-then-fix`
- Summary: Before fixing incorrect behavior, add a passing test that records the observed result and
  labels it as known incorrect. Then fix the implementation, update that same expectation to the
  intended contract, and rewrite the rationale as durable regression context.
- Status: `draft`
- Audience: `both`
- Topics: `testing, correctness, review`
- Tags: `testing, verification, reviewability`
- Related: `test-observable-behavior, smallest-trustworthy-verification,
  review-proof-not-just-code`

## Problem

A regression test added with a bug fix proves the corrected behavior, but it may not prove that its
fixture reached the original problem. Reviewers then have to infer whether the test would have
distinguished the broken implementation from the repaired one.

## Preferred Move

Use a two-state test workflow, regardless of whether the starting point is main, an existing pull
request, a local change, or another revision:

1. At the smallest observable surface that reproduces the problem, add a passing characterization
   test whose expectation records the current output. Explicitly say that the observed behavior is
   known to be incorrect.
1. Run the test before the fix. A green baseline proves that the fixture reaches the problem without
   depending on the proposed implementation.
1. Fix the implementation and update the same test expectation to the intended output. This keeps
   the implementation and behavioral delta together where a reviewer can compare them.
1. Rewrite the test name, comment, or rationale so it no longer describes the incorrect behavior as
   current. Preserve the useful history: the case is non-obvious and was previously missed.

Changing the expectation does not weaken the test. The characterization expectation described what
the system did; the corrected expectation describes what the system must do. The resulting test is
durable regression protection for the repaired contract.

## Tradeoff

Do not silently freeze known-bad behavior or present it as the intended contract. Label the first
state as characterization, keep its baseline green, and replace stale "known incorrect" language
after the fix. Prefer the smallest observable surface that proves the problem; a broad snapshot can
hide the relevant delta and accidentally pin unrelated behavior.

This method is less useful when an existing test already proves the fixture reaches the bug, or when
the failure cannot safely be represented as a passing assertion. In those cases, retain the closest
trustworthy before-and-after evidence without forcing a misleading characterization test.

## Agent Instruction

Before fixing reproducible incorrect behavior, add and run a passing characterization test at the
smallest observable surface, explicitly labeling the current result as wrong. Fix the implementation,
update the same expectation to the intended contract, rewrite stale rationale as durable regression
context, and report both test states.

## Examples

Before the fix, the passing assertion records the defect without endorsing it:

```rust
// Characterization: the formatter incorrectly drops the final field.
assert_eq!(format_record(input), "name=Ada");
```

After the fix, the same assertion protects the intended contract and the comment records why the
case matters:

```rust
// Regression: preserve the final field when the record has no trailing newline.
assert_eq!(format_record(input), "name=Ada,role=admin");
```

## References

| Source                       | Use        | Note                                                        |
| ---------------------------- | ---------- | ----------------------------------------------------------- |
| [Feathers][feathers]         | `adapts`   | Characterization tests establish actual behavior first.     |
| [Fowler testing culture][mf] | `supports` | A bug fix needs a test to keep it from being undone later.  |

[feathers]: https://www.pearson.com/en-us/subject-catalog/p/working-effectively-with-legacy-code/P200000008984
[mf]: https://martinfowler.com/articles/testing-culture.html
