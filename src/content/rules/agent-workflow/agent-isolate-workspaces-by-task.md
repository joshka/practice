# Agent Isolate Workspaces By Task

## Metadata

- Name: `Isolate Workspaces by Task`
- ID: `AGENT-ISOLATE-WORKSPACES-BY-TASK`
- Summary: Put separable or parallel agent work in its own workspace or source-control lane.
  Isolation keeps diffs, validation, and ownership clear when multiple changes are in flight.
- Related: `isolate-agent-workspaces, preserve-unowned-work, small-reviewable-chunks`
- Status: `reviewed`
- Domain: `agent-workflow`
- Tags: `agent-workflow, vcs-jj, change-shape, reviewability`

## Rule

Isolate agent workspaces by task.

## Why

Parallel agent tasks can overwrite each other, mix unrelated diffs, or make validation ambiguous
when they share one working copy. Isolating work by task gives each change its own filesystem state,
source-control lane, and handoff.

## Helps

- Keeps concurrent work reviewable and prevents one task from inheriting another task's partial
  edits.

## Limits

Use the same workspace when the work is one atomic change. Extra workspaces add coordination cost
and cleanup responsibility.

## Agent Instruction

Isolate workspaces for parallel agent tasks so diffs, validation, and ownership stay unambiguous.

## Mechanisms

Supported by `jj new`, `jj workspace add`, task-owned branches or changes, clear changed-file
ownership, and cleanup notes after integration.

## References

- [Principle: Private Context Is Not Shared
  Context](../../principles/private-context-is-not-shared-context.md)
- [OpenAI Harness Engineering: agent legibility is the
  goal](https://openai.com/index/harness-engineering/#agent-legibility-is-the-goal)
- [OpenAI Symphony README](https://github.com/openai/symphony#readme)
