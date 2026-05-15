# Agent Preserve Human Work

## Metadata

- ID: `AGENT-PRESERVE-HUMAN-WORK`
- Legacy ID: `R-0803`
- Status: `reviewed`
- Domain: `agent-workflow`
- Depth: `compact`

## Rule

Preserve unrelated human work.

## Why

Agents share a working tree with human edits and sometimes other agents. Unrelated changes may be
unfinished, intentional, or locally important. Preserving them is a baseline safety rule because
reverting or formatting them destroys work outside the task scope.

## Helps

- Protects user work and keeps diffs limited to the task the agent owns.

## Limits

If unrelated changes block the task, inspect and adapt around them. Ask before reverting, deleting,
or rewriting work that is not clearly yours.

## Agent Instruction

Preserve unrelated human work because agents share a working tree with human edits and sometimes other
agents.

## Mechanisms

Supported by `jj status`, path-scoped edits, careful diff review, fresh changes for separable work,
and handoffs that identify files touched.

## References

- [Principle: Private Context Is Not Shared
  Context](../../principles/private-context-is-not-shared-context.md)
- [OpenAI Harness Engineering: agent legibility is the
  goal](https://openai.com/index/harness-engineering/#agent-legibility-is-the-goal)
- [OpenAI Symphony README](https://github.com/openai/symphony#readme)
