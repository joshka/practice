# Refactoring Prefer Local Reasoning

## Metadata

- ID: `REFACTORING-PREFER-LOCAL-REASONING`
- Status: `reviewed`
- Domain: `refactoring`
- Depth: `compact`

## Rule

Prefer local reasoning over distant reconstruction.

## Why

Code is easier to change when the reader can see the relevant state, invariants, and effects nearby.
Distant reconstruction through globals, callbacks, broad context objects, or scattered helper chains
increases the number of facts the reader must hold at once.

## Helps

- Reduces cognitive load and makes behavior changes less error-prone.

## Limits

Some concepts are intentionally centralized, such as shared policy, public API contracts, or
cross-cutting infrastructure. Centralize when it reduces total reasoning, not just local line count.

## Agent Instruction

Prefer designs where readers can see relevant state, invariants, and effects nearby instead of
reconstructing distant context.

## Mechanisms

Supported by narrow parameters, explicit inputs, nearby helpers, module ownership, code review for
hidden state, and tests at the owning boundary.

## References

- [Pattern: Reader Locality](../../patterns/reader-locality.md)
- [Fowler: Definition of Refactoring](https://martinfowler.com/bliki/DefinitionOfRefactoring.html)
- [Refactoring catalog](https://refactoring.com/catalog/)
