# Agent Preserve Intent

## Metadata

- ID: `AGENT-PRESERVE-INTENT`
- Status: `reviewed`
- Domain: `agent-workflow`
- Depth: `compact`

## Rule

Preserve intent over literalism.

## Why

Literal execution can satisfy the words while missing the goal. If a requested rename, rewrite, or
rule shape is meant to solve a readability or review problem, the agent should preserve that purpose
even when the exact phrasing needs adjustment.

## Helps

- Keeps agent work aligned with the user's real objective instead of producing brittle literal
  compliance.

## Limits

Do not silently reinterpret risky or ambiguous requests. When preserving intent would change scope,
state the interpretation and ask or proceed with a conservative slice.

## Agent Instruction

Preserve intent over literalism because literal execution can satisfy the words while missing the goal.

## Mechanisms

Supported by restating objectives, checking proposed edits against the user's stated reason, and
handoffs that explain intent-preserving deviations.

## References

- [Principle: Private Context Is Not Shared
  Context](../../principles/private-context-is-not-shared-context.md)
- [OpenAI Harness Engineering: agent legibility is the
  goal](https://openai.com/index/harness-engineering/#agent-legibility-is-the-goal)
- [OpenAI Symphony README](https://github.com/openai/symphony#readme)
