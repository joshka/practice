# Change Separate Structure From Behavior

## Metadata

- Name: `Separate Structure From Behavior`
- ID: `CHANGE-SEPARATE-STRUCTURE-FROM-BEHAVIOR`
- Summary: Split refactoring or layout changes from behavior changes when the combined diff obscures
  intent. Separate review units make meaning preservation and new behavior easier to check.
- Status: `reviewed`
- Domain: `change-shape`
- Tags: `change-shape, reviewability, reader-locality`
- Related: `change-shape-controls-review-cost, separate-structure-from-behavior`

## Rule

Keep structure changes separate from behavior changes when the combined diff obscures review.

## Why

Structure changes ask reviewers to confirm the code means the same thing; behavior changes ask them
to confirm the system now does the right new thing. Combining them in one diff makes both questions
harder and hides accidental behavior changes inside cleanup.

## Helps

- Makes reviews sharper and makes structure-only changes easier to revert if they were wrong.

## Limits

Keep them together when the structure change is tiny and only legible next to the behavior change.
Split when the combined diff obscures either intent.

## Agent Instruction

Separate structure and behavior changes because the combined diff makes reviewers prove both meaning
preservation and new behavior.

## Mechanisms

Supported by separate jj changes, focused tests, before/after diff review, clear descriptions, and
handoffs that label structure versus behavior work.

## References

- [Pattern: Small Reviewable Chunks](../../patterns/small-reviewable-chunks.md)
- [Pattern: Separate Structure From Behavior](../../patterns/separate-structure-from-behavior.md)
- [Fowler: Definition of Refactoring](https://martinfowler.com/bliki/DefinitionOfRefactoring.html)
