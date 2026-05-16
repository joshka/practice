# Refactoring Align Seams With Real Variation

## Metadata

- Name: `Align Seams with Real Variation`
- ID: `REFACTORING-ALIGN-SEAMS-WITH-REAL-VARIATION`
- Summary: Put abstraction seams where code already varies across backends, policies, protocols,
  tests, or ownership boundaries. Avoid adding names and jumps for hypothetical futures unless the
  next change or risk clearly justifies them.
- Status: `reviewed`
- Domain: `refactoring`
- Depth: `compact`

## Rule

Align seams with real variation, not hypothetical variation.

## Why

A seam is useful when the code actually varies there: different backends, policies, protocols, test
doubles, or ownership boundaries. Creating seams for hypothetical futures adds names, types, and
jumps before the variation exists.

## Helps

- Keeps abstractions tied to observed change pressure and avoids speculative indirection.

## Limits

Prepare for variation when the next change is known or the cost of not preparing is high. Avoid
seams whose only justification is that variation might happen someday.

## Agent Instruction

Align seams with observed variation such as backends, policies, protocols, test doubles, or
ownership boundaries, not hypothetical variation.

## Mechanisms

Supported by commit-history review, caller analysis, tests around real variants, and code review
that asks what change the seam makes easier.

## References

- [Pattern: Reader Locality](../../patterns/reader-locality.md)
- [Fowler: Definition of Refactoring](https://martinfowler.com/bliki/DefinitionOfRefactoring.html)
- [Refactoring catalog](https://refactoring.com/catalog/)
