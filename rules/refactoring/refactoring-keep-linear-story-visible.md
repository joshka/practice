# Refactoring Keep Linear Story Visible

## Metadata

- ID: `REFACTORING-KEEP-LINEAR-STORY-VISIBLE`
- Status: `reviewed`
- Domain: `refactoring`
- Depth: `compact`

## Rule

Keep the whole story visible when work is linear.

## Why

Some logic is easiest to understand as a straight narrative: read input, validate, transform, emit
result. Splitting every step into tiny helpers can make the reader reconstruct the story by jumping
around the file.

## Helps

- Preserves readability when the order of operations is the main concept.

## Limits

Extract helpers when a sub-step has its own concept, policy, reuse, or test surface. Keep the story
inline when extraction would only scatter a simple flow.

## Agent Instruction

Keep linear work visible because the clearest story is read input, validate, transform, then emit
result.

## Mechanisms

Supported by whitespace chunking, local comments when needed, small functions, and review that
compares jump cost with local readability.

## References

- [Pattern: Reader Locality](../../patterns/reader-locality.md)
- [Fowler: Definition of Refactoring](https://martinfowler.com/bliki/DefinitionOfRefactoring.html)
- [Refactoring catalog](https://refactoring.com/catalog/)
