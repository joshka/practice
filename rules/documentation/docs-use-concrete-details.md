# Docs Use Concrete Details

## Metadata

- ID: `DOCS-USE-CONCRETE-DETAILS`
- Legacy ID: `R-0511`
- Status: `reviewed`
- Domain: `documentation`
- Depth: `compact`

## Rule

Use concrete nouns and real paths, defaults, commands, and examples.

## Why

Abstract nouns make readers infer the actual object. A sentence about "shared artifacts" is weaker
than one naming issues, PRs, commit messages, docs, and handoffs when those are the surfaces at
stake. Concrete paths, commands, defaults, types, and examples remove guesswork.

## Helps

- Makes guidance easier to apply, review, and encode for agents.

## Limits

Do not overload prose with incidental detail. Use concrete examples that clarify scope, not examples
that distract from the rule.

## Agent Instruction

Use concrete nouns, real paths, defaults, commands, and examples so readers do not infer the actual
object.

## Mechanisms

Supported by terminology review, examples, path and command verification, and quality checks that
flag abstract repeated rationale for deeper review.

## References

- [Principle: Docs Are Contracts](../../principles/docs-are-contracts.md)
- [Diataxis: how to use Diataxis](https://diataxis.fr/how-to-use-diataxis/)
- [Rustdoc: how to write
  documentation](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html)
