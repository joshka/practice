# Change Minimal But Complete

## Metadata

- Name: `Minimal but Complete`
- ID: `CHANGE-MINIMAL-BUT-COMPLETE`
- Summary: Keep the diff as small as the purpose allows while including the evidence that purpose
  needs. Reviewers should see one coherent unit they can understand, validate, and revert.
- Status: `reviewed`
- Domain: `change-shape`
- Tags: `change-shape, reviewability, verification`
- Related: `small-reviewable-chunks, review-proof-not-just-code, smallest-trustworthy-verification`

## Rule

Keep each change minimal but complete.

## Why

A change that is too large hides risk, but a change that is too small can leave reviewers with an
unexplained half-step. Minimal but complete means the diff has one purpose and enough code, tests,
docs, and generated artifacts for that purpose to make sense.

## Helps

- Gives reviewers a coherent unit that can be understood, validated, and reverted.

## Limits

Completeness depends on the purpose. A structure-only change may need no behavior tests, while a
public API change may need docs, examples, and compatibility notes.

## Agent Instruction

Keep each change minimal but complete because a change that is too large hides risk, but a change that
is too small can leave reviewers with an unexplained half-step.

## Mechanisms

Supported by jj descriptions, focused validation, generated-artifact checks, PR summaries, and
review checklists that ask whether the change can stand alone.

## References

- [Pattern: Small Reviewable Chunks](../../patterns/small-reviewable-chunks.md)
- [Pattern: Separate Structure From Behavior](../../patterns/separate-structure-from-behavior.md)
- [Fowler: Definition of Refactoring](https://martinfowler.com/bliki/DefinitionOfRefactoring.html)
