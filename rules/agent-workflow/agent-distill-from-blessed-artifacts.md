# Agent Distill From Blessed Artifacts

## Metadata

- Name: `Distill From Blessed Artifacts`
- ID: `AGENT-DISTILL-FROM-BLESSED-ARTIFACTS`
- Summary: `Study accepted code, docs, tests, and reviews first. Adapt local convention to this task.`
- Status: `reviewed`
- Domain: `agent-workflow`
- Depth: `compact`

## Rule

Distill from blessed artifacts.

## Why

Existing accepted code, docs, tests, PRs, and review comments are often denser than a new prompt.
Distilling from those artifacts lets agents reuse the project's real conventions instead of
producing generic output that sounds plausible but does not match the repo.

## Helps

- Preserves local voice and implementation style while reducing repeated human steering.

## Limits

Do not copy old artifacts blindly when they are stale or known-bad. Extract the convention that was
accepted, then adapt it to the current problem.

## Agent Instruction

Distill conventions, principles, and review expectations from accepted artifacts before inventing
style; adapt the accepted pattern to the current task.

## Mechanisms

Supported by exemplar files, blessed snippets, style guides, review packets, and prompts that name
which artifacts should be treated as authoritative.

## References

- [Principle: Private Context Is Not Shared
  Context](../../principles/private-context-is-not-shared-context.md)
- [OpenAI Harness Engineering: agent legibility is the
  goal](https://openai.com/index/harness-engineering/#agent-legibility-is-the-goal)
- [OpenAI Symphony README](https://github.com/openai/symphony#readme)
