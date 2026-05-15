# Docs Write Technical Prose

## Metadata

- ID: `DOCS-WRITE-TECHNICAL-PROSE`
- Legacy ID: `R-0502`
- Status: `reviewed`
- Domain: `documentation`
- Depth: `compact`

## Rule

Write technical docs, not marketing, coaching, or chat.

## Why

Technical docs should help readers make correct decisions. Marketing copy, coaching language,
chatty narration, and interface narration add tone without carrying contracts, commands, tradeoffs,
or evidence. That makes the page harder to scan and easier for agents to imitate badly.

## Helps

- Keeps documentation direct, actionable, and grounded in behavior rather than persuasion.

## Limits

Plain language and a human voice are good. Cut the prose when it stops explaining the system and
starts selling, apologizing, narrating the writing process, or narrating the page structure.

## Agent Instruction

Write technical docs, not marketing, coaching, or chat, so readers can make correct decisions.

## Mechanisms

Supported by prose review, local style examples, markdown lint, and review comments that ask for
actor, action, contract, evidence, or tradeoff.

## References

- [Principle: Docs Are Contracts](../../principles/docs-are-contracts.md)
- [Docs Hide Catalog Mechanics](docs-hide-catalog-mechanics.md)
- [Diataxis: how to use Diataxis](https://diataxis.fr/how-to-use-diataxis/)
- [Rustdoc: how to write
  documentation](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html)
