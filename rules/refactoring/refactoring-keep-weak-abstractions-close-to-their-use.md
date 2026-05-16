# Refactoring Keep Weak Abstractions Close To Their Use

## Metadata

- ID: `REFACTORING-KEEP-WEAK-ABSTRACTIONS-CLOSE-TO-THEIR-USE`
- Status: `reviewed`
- Domain: `refactoring`
- Depth: `compact`

## Rule

Keep weak abstractions close to their use.

## Why

New abstractions are often tentative. Keeping a weak helper, type, or trait near its first use makes
it easier to revise, inline, or delete before other modules depend on it.

## Helps

- Limits coupling from premature abstractions and keeps experiments reversible.

## Limits

Promote the abstraction when several callers rely on the same concept and the name has proven
useful. Keep it local while the boundary is still uncertain.

## Agent Instruction

Keep weak abstractions close to their use because new abstractions are often tentative.

## Mechanisms

Supported by module-local helpers, narrow visibility, private types, search for call sites, and
review that asks whether the abstraction has earned a wider home.

## References

- [Pattern: Reader Locality](../../patterns/reader-locality.md)
- [Fowler: Definition of Refactoring](https://martinfowler.com/bliki/DefinitionOfRefactoring.html)
- [Refactoring catalog](https://refactoring.com/catalog/)
