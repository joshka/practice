# Refactoring Prefer Loops For Side Effects

## Metadata

- Name: `Prefer Loops for Side Effects`
- ID: `REFACTORING-PREFER-LOOPS-FOR-SIDE-EFFECTS`
- Summary: Use ordinary loops when the main purpose is mutation, I/O, logging, or other side
  effects. Iterator chains are better for value transformation; using them for effects can hide
  order, early exits, and error handling.
- Status: `reviewed`
- Domain: `refactoring`
- Depth: `compact`

## Rule

Prefer loops over combinators for business-logic side effects.

## Why

Iterator chains are compact, but business-logic side effects often need named steps, early exits,
logging, error handling, or comments. A loop can make mutation and control flow visible where a
combinator chain hides it inside closures.

## Helps

- Keeps side effects and branch behavior readable in review.

## Limits

Use combinators when the transformation is pure and the chain remains readable. Prefer loops when
side effects, policy, or error handling are the point.

## Agent Instruction

Prefer loops over combinators for business-logic side effects because iterator chains are compact, but
business-logic side effects often need named steps, early exits, logging, error handling, or
comments.

## Mechanisms

Supported by code review, clippy judgment rather than blanket linting, focused tests, and
readability comparisons for before/after refactors.

## References

- [Pattern: Reader Locality](../../patterns/reader-locality.md)
- [Fowler: Definition of Refactoring](https://martinfowler.com/bliki/DefinitionOfRefactoring.html)
- [Refactoring catalog](https://refactoring.com/catalog/)
