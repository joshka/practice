# Change Isolate Controversial Changes

## Metadata

- Name: `Isolate Controversial Changes`
- ID: `CHANGE-ISOLATE-CONTROVERSIAL-CHANGES`
- Summary: Put risky or contentious moves in their own review unit when they can stand alone. This
  lets reviewers approve, reject, or revise the decision without incidental cleanup attached.
- Status: `reviewed`
- Domain: `change-shape`
- Depth: `compact`

## Rule

Isolate controversial changes.

## Why

Formatting, renames, API breaks, dependency changes, unsafe code, large rewrites, and behavior
changes all invite different review questions. Putting a controversial move in its own change lets
reviewers evaluate that decision without also approving incidental cleanup.

## Helps

- Keeps contentious decisions explicit and makes reverting or revising them cheaper.

## Limits

Do not split a change so much that the intermediate state is misleading or impossible to validate.
Isolate the controversy when it can stand as its own decision.

## Agent Instruction

Isolate controversial changes because formatting, renames, API breaks, dependency changes, unsafe code,
large rewrites, and behavior changes all invite different review questions.

## Mechanisms

Supported by separate jj changes, clear descriptions, PR labels, ADR links, focused tests, and
review notes that name the controversial part.

## References

- [Pattern: Small Reviewable Chunks](../../patterns/small-reviewable-chunks.md)
- [Pattern: Separate Structure From Behavior](../../patterns/separate-structure-from-behavior.md)
- [Fowler: Definition of Refactoring](https://martinfowler.com/bliki/DefinitionOfRefactoring.html)
