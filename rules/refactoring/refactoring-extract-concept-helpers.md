# Refactoring Extract Concept Helpers

## Metadata

- Name: `Extract Concept Helpers`
- ID: `REFACTORING-EXTRACT-CONCEPT-HELPERS`
- Summary: Extract helpers when the new function names a real concept boundary with a stable
  purpose. Hiding a few lines behind a weak name adds a jump without reducing the reader's burden.
- Status: `reviewed`
- Domain: `refactoring`
- Tags: `reader-locality, change-shape, ownership`
- Related: `reader-locality, use-explaining-variable, strengthen-cohesion`

## Rule

Extract helpers only when they reveal a real concept boundary.

## Why

A helper should reduce the reader's burden by naming a concept, not merely hide three lines. If the
extracted function has a purpose such as `parse_header`, `normalize_path`, or `render_status`, the
call site becomes clearer; if it is just `do_stuff`, it adds a jump.

## Helps

- Improves local reasoning by replacing low-level steps with a meaningful name.

## Limits

Keep code inline when the sequence is already clearer than a new helper. Extract when the helper has
a stable concept, limited inputs, and a useful name.

## Agent Instruction

Extract helpers only for real concept boundaries, not just to hide a few lines from the reader.

## Mechanisms

Supported by automated extract refactorings, compiler checks, tests around extracted behavior, and
review that asks whether the helper name carries real meaning.

## References

- [Pattern: Reader Locality](../../patterns/reader-locality.md)
- [Fowler: Definition of Refactoring](https://martinfowler.com/bliki/DefinitionOfRefactoring.html)
- [Refactoring catalog](https://refactoring.com/catalog/)
