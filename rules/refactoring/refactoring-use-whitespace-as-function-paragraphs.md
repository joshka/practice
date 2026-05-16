# Refactoring Use Whitespace As Function Paragraphs

## Metadata

- ID: `REFACTORING-USE-WHITESPACE-AS-FUNCTION-PARAGRAPHS`
- Status: `reviewed`
- Domain: `refactoring`
- Depth: `compact`

## Rule

Use whitespace as function paragraphs.

## Why

Blank lines can show that a function has phases: gather inputs, validate, calculate, perform
effects, return. Without those visual paragraphs, readers must parse every statement to find the
conceptual groups.

## Helps

- Improves scanability without introducing new names or control flow.

## Limits

Do not use whitespace to disguise an oversized or incoherent function. If a paragraph has a strong
name and limited interaction with the rest, consider extracting it.

## Agent Instruction

Use whitespace as function paragraphs because blank lines can show that a function has phases: gather
inputs, validate, calculate, perform effects, return.

## Mechanisms

Supported by formatting review, chunking before deeper refactors, and follow-up extraction when a
paragraph becomes a clear helper candidate.

## References

- [Pattern: Reader Locality](../../patterns/reader-locality.md)
- [Fowler: Definition of Refactoring](https://martinfowler.com/bliki/DefinitionOfRefactoring.html)
- [Refactoring catalog](https://refactoring.com/catalog/)
