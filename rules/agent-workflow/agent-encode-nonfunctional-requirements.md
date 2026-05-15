# Agent Encode Nonfunctional Requirements

## Metadata

- ID: `AGENT-ENCODE-NONFUNCTIONAL-REQUIREMENTS`
- Legacy ID: `R-0820`
- Status: `reviewed`
- Domain: `agent-workflow`
- Depth: `compact`

## Rule

Encode nonfunctional requirements.

## Why

Requirements such as latency, accessibility, reviewability, security, privacy, determinism, and
downstream compatibility are easy for agents to miss because they may not appear in the immediate
diff. Encode them near the task so they become part of the implementation target.

## Helps

- Keeps invisible constraints from being discovered only during review or production use.

## Limits

Do not add generic nonfunctional checklists to every task. Name the constraints that materially
affect this change or the surface it touches.

## Agent Instruction

Encode nonfunctional requirements that may not appear in the diff, such as latency, accessibility,
security, privacy, determinism, and compatibility.

## Mechanisms

Supported by acceptance criteria, CI gates, lint configs, performance baselines, security review
notes, and PR templates with explicit risk sections.

## References

- [Principle: Private Context Is Not Shared
  Context](../../principles/private-context-is-not-shared-context.md)
- [OpenAI Harness Engineering: agent legibility is the
  goal](https://openai.com/index/harness-engineering/#agent-legibility-is-the-goal)
- [OpenAI Symphony README](https://github.com/openai/symphony#readme)
