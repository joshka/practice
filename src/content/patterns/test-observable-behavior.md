# Test Observable Behavior

## Metadata

- Name: `Test Observable Behavior`
- ID: `test-observable-behavior`
- Summary: Tests that pin private structure can block useful refactors while missing broken user
  outcomes. Test observable outputs, errors, side effects, state, events, and boundaries, reserving
  private tests for dense rules that are otherwise hard to reach.
- Status: `reviewed`
- Audience: `both`
- Topics: `testing, correctness, review`
- Tags: `testing, verification, observability`
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

## Examples

Bad: the test freezes the helper chosen by the current implementation.

```rust
assert_eq!(parse_rows_called(), 1);
```

Good: the test protects the output callers depend on.

```rust
assert_eq!(parse_report(input)?.rows.len(), 3);
```

## References

| Source                | Use      | Note                                                          |
| --------------------- | -------- | ------------------------------------------------------------- |
| [Feathers][feathers]  | `adapts` | Legacy-code work depends on tests that preserve behavior.     |
| [Refactoring][fowler] | `adapts` | Refactoring relies on preserving externally visible behavior. |

[feathers]: https://www.pearson.com/en-us/subject-catalog/p/working-effectively-with-legacy-code/P200000008984
[fowler]: https://refactoring.com/
