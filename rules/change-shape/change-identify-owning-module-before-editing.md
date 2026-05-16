# Change Identify Owning Module Before Editing

## Metadata

- ID: `CHANGE-IDENTIFY-OWNING-MODULE-BEFORE-EDITING`
- Status: `reviewed`
- Domain: `change-shape`
- Depth: `compact`

## Rule

Identify the owning module before editing.

## Why

Editing the first file that mentions a behavior can put new logic in a caller, facade, test helper,
or adapter that does not own the concept. Identifying the owning module first keeps invariants,
tests, and documentation near the code responsible for the behavior.

## Helps

- Reduces scattered fixes and makes future readers find the behavior where they expect it.

## Limits

A narrow caller-side adaptation is fine when the caller truly owns the variation. Move inward only
when the concept or invariant belongs there.

## Agent Instruction

Identify the owning module before editing because editing the first file that mentions a behavior can
put new logic in a caller, facade, test helper, or adapter that does not own the concept.

## Mechanisms

Supported by code search, module README or crate-root docs, existing test locations, ownership
comments, and review that asks where the concept belongs.

## References

- [Pattern: Small Reviewable Chunks](../../patterns/small-reviewable-chunks.md)
- [Pattern: Separate Structure From Behavior](../../patterns/separate-structure-from-behavior.md)
- [Fowler: Definition of Refactoring](https://martinfowler.com/bliki/DefinitionOfRefactoring.html)
