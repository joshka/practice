# Change Prefer Small Follow Ups

## Metadata

- Name: `Prefer Small Follow-Ups`
- ID: `CHANGE-PREFER-SMALL-FOLLOW-UPS`
- Summary: Move adjacent cleanup or broader improvements into focused follow-up changes when the
  current diff can stand alone. This preserves review focus while still capturing useful work.
- Status: `reviewed`
- Domain: `change-shape`
- Tags: `change-shape, reviewability, documentation`
- Related: `small-reviewable-chunks, make-the-change-easy-first, remediate-doc-drift`

## Rule

Prefer small follow-up changes over overloaded changes.

## Why

When a change uncovers adjacent cleanup, docs drift, naming issues, or broader refactoring, folding
all of it into the current diff can hide the original purpose. A small follow-up keeps momentum
without making the current review pay for every discovered improvement.

## Helps

- Preserves review focus while still capturing useful nearby work.

## Limits

Do the follow-up immediately when the current change is misleading or incomplete without it. Defer
only work that can stand on its own later.

## Agent Instruction

Prefer small follow-ups for adjacent cleanup, docs drift, naming issues, or broader refactoring so
the current diff keeps its purpose.

## Mechanisms

Supported by follow-up issues, stacked jj changes, TODO-free review notes, and handoffs that name
the next slice explicitly.

## References

- [Pattern: Small Reviewable Chunks](../../patterns/small-reviewable-chunks.md)
- [Pattern: Separate Structure From Behavior](../../patterns/separate-structure-from-behavior.md)
- [Fowler: Definition of Refactoring](https://martinfowler.com/bliki/DefinitionOfRefactoring.html)
