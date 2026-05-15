# Docs Front Load Useful Point

## Metadata

- ID: `DOCS-FRONT-LOAD-USEFUL-POINT`
- Legacy ID: `R-0510`
- Status: `reviewed`
- Domain: `documentation`
- Depth: `compact`

## Rule

Front-load the useful point.

## Why

Readers scan docs for the decision, command, invariant, or warning that matters. If the first
paragraph only says what the page will do or gives broad motivation, both humans and agents must
search before they can use the page.

## Helps

- Improves scanning and makes important commands, contracts, and caveats harder to miss.

## Limits

Narrative setup is useful when context changes interpretation. Put that setup after the concrete
point or make the first sentence carry both context and conclusion.

## Agent Instruction

Front-load the useful point because readers scan docs for the decision, command, invariant, or warning
that matters.

## Mechanisms

Supported by first-paragraph review, heading review, task-first README structure, and PR feedback
that asks what the reader should learn first.

## References

- [Principle: Docs Are Contracts](../../principles/docs-are-contracts.md)
- [Diataxis: how to use Diataxis](https://diataxis.fr/how-to-use-diataxis/)
- [Rustdoc: how to write
  documentation](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html)
