# Agent Turn Feedback Into Guidance

## Metadata

- ID: `AGENT-TURN-FEEDBACK-INTO-GUIDANCE`
- Status: `reviewed`
- Domain: `agent-workflow`
- Depth: `compact`

## Rule

Turn repeated feedback into durable guidance.

## Why

Repeated corrections such as "show why," "name the next thing," or "do not use abstract rule names"
are process bugs. Turning them into rules, templates, snippets, or checks prevents future agents
from needing the same steering.

## Helps

- Converts review friction into durable improvement of the workflow.

## Limits

Do not encode one-off taste or situational feedback as a global rule. Generalize the repeated
failure mode before promotion.

## Agent Instruction

Turn repeated feedback into durable guidance because repeated corrections such as "show why,"
"name the next thing," or "do not use abstract rule names" are process bugs.

## Mechanisms

Supported by rule files, patterns, snippets, audit checks, templates, and review retrospectives that
identify repeated corrections.

## References

- [Principle: Private Context Is Not Shared
  Context](../../principles/private-context-is-not-shared-context.md)
- [OpenAI Harness Engineering: agent legibility is the
  goal](https://openai.com/index/harness-engineering/#agent-legibility-is-the-goal)
- [OpenAI Symphony README](https://github.com/openai/symphony#readme)
