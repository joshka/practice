# Docs Expose Move Risk And Example In Patterns

## Metadata

- Name: `Expose Move, Risk, and Example in Patterns`
- ID: `DOCS-EXPOSE-MOVE-RISK-AND-EXAMPLE-IN-PATTERNS`
- Summary: `Give pattern guidance a recognizable trigger, preferred move, risk, example, and agent
  instruction. The extra structure makes repeatable advice easier to cite and apply.`
- Status: `reviewed`
- Domain: `documentation`
- Tags: `documentation, reviewability, agent-workflow, examples`
- Related: `write-docs-as-contracts, label-doc-claims-by-evidence`

## Rule

Expose symptom, move, risk, example, and agent instruction in pattern-style guidance.

## Why

Pattern-style guidance is useful when a reader can recognize the situation and apply the move. If a
pattern only names an abstract preference, the reader must infer the trigger, risk, and example,
which makes the pattern hard to cite in review or encode for agents.

## Helps

- Makes patterns reviewable, teachable, and usable as agent instructions instead of vague slogans.

## Limits

Tiny rules may not need a full pattern. Use the pattern shape when the move is repeatable and has a
meaningful failure mode or tradeoff.

## Agent Instruction

For pattern-style guidance, include the recognizable situation, preferred move, risk, example, and
agent instruction.

## Mechanisms

Supported by pattern templates, examples, related-rule links, and reviews that ask whether the
trigger and risk are concrete enough to act on.

## References

- [Principle: Docs Are Contracts](../../principles/docs-are-contracts.md)
- [Diataxis: how to use Diataxis](https://diataxis.fr/how-to-use-diataxis/)
- [Rustdoc: how to write
  documentation](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html)
