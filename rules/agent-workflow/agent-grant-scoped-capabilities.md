# Agent Grant Scoped Capabilities

## Metadata

- ID: `AGENT-GRANT-SCOPED-CAPABILITIES`
- Status: `reviewed`
- Domain: `agent-workflow`
- Depth: `compact`

## Rule

Grant scoped agent capabilities.

## Why

Agents with broad authority can accidentally mutate external systems, publish state, delete files,
or read secrets unrelated to the task. Scope capabilities to the task so the agent can make progress
without receiving authority it does not need.

## Helps

- Reduces blast radius and makes permission boundaries auditable.

## Limits

Do not block necessary tools so tightly that the agent cannot verify its work. Grant broader access
deliberately when the task requires it and the risk is understood.

## Agent Instruction

Grant scoped agent capabilities because agents with broad authority can accidentally mutate external
systems, publish state, delete files, or read secrets unrelated to the task.

## Mechanisms

Supported by sandbox settings, scoped credentials, read-only modes, dry runs, explicit approval
gates, and tool-specific allowlists.

## References

- [Principle: Private Context Is Not Shared
  Context](../../principles/private-context-is-not-shared-context.md)
- [OpenAI Harness Engineering: agent legibility is the
  goal](https://openai.com/index/harness-engineering/#agent-legibility-is-the-goal)
- [OpenAI Symphony README](https://github.com/openai/symphony#readme)
