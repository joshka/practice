# Change Use One Purpose Per Change

## Metadata

- ID: `CHANGE-USE-ONE-PURPOSE-PER-CHANGE`
- Status: `reviewed`
- Domain: `change-shape`
- Depth: `compact`

## Rule

Use one purpose per change.

## Why

One-purpose changes let reviewers ask one main question: did this accomplish the stated goal? Mixing
bug fixes, refactors, dependency bumps, docs rewrites, and generated updates makes review slower and
makes rollback riskier.

## Helps

- Improves review speed, revertability, and historical understanding of why code changed.

## Limits

A single purpose can still touch tests, docs, and generated files when those are required evidence
for the same change. The rule is about purpose, not file count.

## Agent Instruction

Use one purpose per change so reviewers can ask one main question: did this accomplish the stated
goal?

## Mechanisms

Supported by small jj changes, imperative descriptions, PR summaries, focused validation, and review
that asks whether each file supports the same goal.

## References

- [Pattern: Small Reviewable Chunks](../../patterns/small-reviewable-chunks.md)
- [Pattern: Separate Structure From Behavior](../../patterns/separate-structure-from-behavior.md)
- [Fowler: Definition of Refactoring](https://martinfowler.com/bliki/DefinitionOfRefactoring.html)
