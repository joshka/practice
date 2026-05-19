# Change Treat And As Scope Warning

## Metadata

- Name: `Treat And as Scope Warning`
- ID: `CHANGE-TREAT-AND-AS-SCOPE-WARNING`
- Summary: Use compound change descriptions as a prompt to inspect whether the work has more than
  one purpose. The word is not a rule, but it catches scope creep while splitting is still cheap.
- Status: `reviewed`
- Domain: `change-shape`
- Tags: `change-shape, reviewability, reader-locality`
- Related: `small-reviewable-chunks, change-shape-controls-review-cost`

## Rule

Treat `and` in a change description as a scope warning.

## Why

A change titled "fix parser and update docs and clean API" often contains multiple review units. The
word `and` is a cheap signal to ask whether the work has one purpose or whether it should become a
stack of smaller changes.

## Helps

- Catches accidental scope creep before the diff becomes hard to split.

## Limits

Some compound titles still name one purpose, such as "parse and display validation errors." Use the
warning to inspect scope, not as a grammar rule.

## Agent Instruction

Treat `and` in a change description as a scope warning because a change titled "fix parser and update
docs and clean API" often contains multiple review units.

## Mechanisms

Supported by jj description review, PR title review, issue slicing, and handoff options that name
the next independent chunk.

## References

- [Pattern: Small Reviewable Chunks](../../patterns/small-reviewable-chunks.md)
- [Pattern: Separate Structure From Behavior](../../patterns/separate-structure-from-behavior.md)
- [Fowler: Definition of Refactoring](https://martinfowler.com/bliki/DefinitionOfRefactoring.html)
