# Agent Instructions Are Operational Controls

## Metadata

- Name: `Agent Instructions Are Operational Controls`
- ID: `agent-instructions-are-operational-controls`
- Status: `reviewed`
- Audience: `both`
- Topics: `agents, rules, instructions, token-budget`
- Related: `mechanize-repeated-feedback, private-context-is-not-shared-context`

## Claim

Agent-facing instructions should shape behavior, not merely restate preferences. A good compressed
rule gives the agent enough trigger, purpose, and boundary information to act correctly while using
as few durable tokens as possible.

## Why This Exists

Every word in a global agent rule is paid for repeatedly, but a missing reason can cost much more
when the agent applies the sentence mechanically in the wrong situation. The useful middle ground is
a short instruction that includes the action and the key reason or trigger.

For example, "Avoid global mutable state" is directionally correct but under-specified. "Avoid
global mutable state because it hides ownership, ordering, reset, and concurrency requirements"
gives the agent enough context to recognize exceptions and alternatives.

## Good Uses

- Compress reviewed guidance into agent snippets.
- Turn repeated review feedback into reusable instructions.
- Encode nonfunctional requirements such as reviewability, diagnostics, privacy, and API stability.
- Keep agent rules focused on behavior that should change future work.

## Bad Smells

- The agent instruction repeats the rule title with no added operational context.
- The instruction starts with a generic conditional such as "When ..." and buries the action.
- The instruction contains links instead of the actual guidance needed during execution.
- The instruction is so abstract that the agent must infer common cases such as PRs, issues, commit
  messages, tests, or docs.

## Limits

Not every detailed rule belongs in the compressed agent pack. Some ideas should remain in human
guidance, patterns, or principles when the judgment is too nuanced for a short instruction. The
agent pack should contain the stable operational part, not every argument behind it.

## Agent Consequences

Write agent rules as action-first instructions. Add a compact reason when it helps the agent choose
between superficially similar moves. Omit links from compressed snippets and keep detailed
references in the rule or principle file.
