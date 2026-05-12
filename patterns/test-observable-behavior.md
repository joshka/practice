# Test Observable Behavior

## Metadata

- Name: `Test Observable Behavior`
- ID: `test-observable-behavior`
- Status: `reviewed`
- Audience: `both`
- Topics: `testing, correctness, review`
- Related: `smallest-trustworthy-verification, preserve-error-context`

## Problem

Tests that pin private helper calls, incidental structure, or exact internal sequencing make
refactors harder without protecting the behavior callers depend on. A change can pass those tests
while still breaking the public result.

## Preferred Move

Write tests around behavior that callers can observe: outputs, errors, side effects, persisted
state, emitted events, or integration boundaries. Name the behavior under test rather than the
private implementation path.

## Tradeoff

Some private logic deserves direct tests when it contains dense rules or hard-to-reach edge cases.
Keep those tests focused on the rule they protect, and avoid making them a contract for incidental
helper shape.

## Agent Instruction

Prefer behavior-level tests for changed paths. Do not add tests that freeze private implementation
shape unless that private rule is the real risk being protected.

## References

| Source                | Use      | Note                                                          |
| --------------------- | -------- | ------------------------------------------------------------- |
| [Feathers][feathers]  | `adapts` | Legacy-code work depends on tests that preserve behavior.     |
| [Refactoring][fowler] | `adapts` | Refactoring relies on preserving externally visible behavior. |

[feathers]: https://www.pearson.com/en-us/subject-catalog/p/working-effectively-with-legacy-code/P200000008984
[fowler]: https://refactoring.com/
