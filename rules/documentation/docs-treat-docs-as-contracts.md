# Docs Treat Docs As Contracts

## Metadata

- Name: `Treat Docs as Contracts`
- ID: `DOCS-TREAT-DOCS-AS-CONTRACTS`
- Summary: `Treat supported behavior, commands, errors, and examples in docs as promises readers may
  rely on. Separate normative claims from background, examples, and future plans.`
- Status: `reviewed`
- Domain: `documentation`
- Depth: `compact`

## Rule

Treat docs as contracts.

## Why

Docs increasingly guide both humans and agents. When docs say how an API behaves, what errors mean,
which examples are supported, or what a command does, that prose becomes part of the system contract
even if it is not executable code.

## Helps

- Aligns code, tests, examples, and agent behavior around explicit English-language contracts.

## Limits

Not every sentence is a normative guarantee. Separate contract language from background explanation,
examples, and future plans so readers know what must stay true.

## Agent Instruction

Treat docs as contracts because humans and agents use them to infer supported behavior.

## Mechanisms

Supported by doctests, integration tests, docs drift review, generated examples, CI docs builds, and
PR checks that update nearby docs with behavior changes.

## References

- [Principle: Docs Are Contracts](../../principles/docs-are-contracts.md)
- [Diataxis: how to use Diataxis](https://diataxis.fr/how-to-use-diataxis/)
- [Rustdoc: how to write
  documentation](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html)
