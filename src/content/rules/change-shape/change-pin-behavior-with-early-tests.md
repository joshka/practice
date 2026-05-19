# Change Pin Behavior With Early Tests

## Metadata

- Name: `Pin Behavior With Early Tests`
- ID: `CHANGE-PIN-BEHAVIOR-WITH-EARLY-TESTS`
- Summary: Add characterization tests before changing messy behavior when the existing contract is
  unclear. The baseline separates intentional behavior changes from accidental drift.
- Status: `reviewed`
- Domain: `change-shape`
- Tags: `change-shape, testing, verification`
- Related: `test-observable-behavior, smallest-trustworthy-verification`

## Rule

Use early test changes to pin existing behavior when that makes behavior changes easier to review.

## Why

Before changing messy behavior, an early test can document what the system currently does. That test
gives reviewers a stable baseline, separates characterization from the behavior change, and catches
accidental changes during refactoring.

## Helps

- Makes behavior changes safer and clarifies whether later diffs preserve or intentionally change
  existing behavior.

## Limits

Do not freeze behavior that is obviously wrong unless the test names it as characterization. Skip
this when existing tests already pin the relevant contract.

## Agent Instruction

Use early tests to pin current behavior before changing messy behavior so reviewers can separate
existing behavior from the intended change.

## Mechanisms

Supported by characterization tests, regression fixtures, snapshots, before/after commits, and jj
changes that separate test characterization from behavior edits.

## References

- [Pattern: Small Reviewable Chunks](../../patterns/small-reviewable-chunks.md)
- [Pattern: Separate Structure From Behavior](../../patterns/separate-structure-from-behavior.md)
- [Fowler: Definition of Refactoring](https://martinfowler.com/bliki/DefinitionOfRefactoring.html)
