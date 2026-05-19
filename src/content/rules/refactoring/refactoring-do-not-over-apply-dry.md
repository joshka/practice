# Refactoring Do Not Over Apply Dry

## Metadata

- Name: `Do Not Over-apply DRY`
- ID: `REFACTORING-DO-NOT-OVER-APPLY-DRY`
- Summary: Keep similar-looking code separate until it has the same meaning and changes together.
  Premature sharing can couple unrelated policies and make later edits harder.
- Status: `reviewed`
- Domain: `refactoring`
- Tags: `reader-locality, change-shape, ownership`
- Related: `name-coupling, strengthen-cohesion, keep-structure-reversible`

## Rule

Do not over-apply DRY.

## Why

Two blocks that look similar may change for different reasons. Forcing them into one abstraction can
couple unrelated behavior and make future changes harder because every caller inherits the same
shared shape.

## Helps

- Preserves useful duplication until the shared concept and change pattern are real.

## Limits

Remove duplication when the repeated code has the same meaning, changes together, and gains clarity
from a shared name. Avoid DRY when it hides different policies behind one helper.

## Agent Instruction

Do not over-apply DRY because two blocks that look similar may change for different reasons.

## Mechanisms

Supported by change-history review, naming review, focused helper extraction, and tests that show
whether call sites really share one contract.

## References

- [Pattern: Reader Locality](../../patterns/reader-locality.md)
- [Fowler: Definition of Refactoring](https://martinfowler.com/bliki/DefinitionOfRefactoring.html)
- [Refactoring catalog](https://refactoring.com/catalog/)
