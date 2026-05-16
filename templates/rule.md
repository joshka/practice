# Rule Template

Use this template for one stable rule. Replace bracketed text before publishing an entry.

## Metadata

- ID: `[DOMAIN-VERB-OBJECT]`
- Status: `draft`
- Domain: `[domain]`
- Tags: `[comma-separated cluster tags]`

## Rule

State the direct human-readable instruction.

## Why

Explain why the rule exists when the rule needs justification, tradeoff framing, examples, or
source-backed support. Use concrete examples or named surfaces when an abstract category would make
the reader infer where the rule applies.

## Helps

- Name concrete development outcomes this rule improves.

## Limits

Explain exceptions, costs, or counter-signals. Name concrete cases where the rule should bend or
where a narrower rule would be more useful.

## Agent Instruction

Write the highly compressed instruction that can be included in agent execution packs. Start with
the action the agent should take. Do not repeat the rule text. Add a short `when`, `because`, or
`so` clause only when the trigger, failure mode, or constraint helps the agent avoid doing the
literal-but-wrong thing.

## Mechanisms

List lints, formatters, CI checks, cargo commands, jj config, docs builds, or workflow mechanisms
that can enforce or support the rule.

## References

List durable references when they clarify, support, adapt, or contrast the rule.
