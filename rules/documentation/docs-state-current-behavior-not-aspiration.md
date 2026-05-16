# Docs State Current Behavior Not Aspiration

## Metadata

- Name: `State Current Behavior, Not Aspiration`
- ID: `DOCS-STATE-CURRENT-BEHAVIOR-NOT-ASPIRATION`
- Summary: `Describe what the system does now and label limitations or future plans separately.
  Otherwise roadmap language becomes a false contract for readers and agents.`
- Status: `reviewed`
- Domain: `documentation`
- Depth: `compact`

## Rule

State current behavior, not aspiration.

## Why

Docs that describe intended behavior as if it already exists become false contracts. A reader or
agent may implement against the aspiration, file invalid bugs, or preserve a promise the code never
made. Current behavior, known limitations, and future plans need different wording and homes.

## Helps

- Keeps docs trustworthy and prevents roadmaps from masquerading as API or behavior guarantees.

## Limits

Mention future direction when it is clearly labeled as roadmap, non-goal, or open decision. Do not
mix that language into current usage instructions.

## Agent Instruction

State current behavior, not aspiration, because aspirational docs become false contracts.

## Mechanisms

Supported by docs/code drift checks, issue and roadmap links, release-note review, and tests or
examples that back behavior claims.

## References

- [Principle: Docs Are Contracts](../../principles/docs-are-contracts.md)
- [Diataxis: how to use Diataxis](https://diataxis.fr/how-to-use-diataxis/)
- [Rustdoc: how to write
  documentation](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html)
