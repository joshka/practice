# Agent Budget For Feedback Loops

## Metadata

- ID: `AGENT-BUDGET-FOR-FEEDBACK-LOOPS`
- Legacy ID: `R-0822`
- Status: `reviewed`
- Domain: `agent-workflow`
- Depth: `compact`

## Rule

Budget tokens and time for feedback loops.

## Why

Agent work needs room for reading, editing, running checks, inspecting failures, and reporting
proof. If the task budget only covers the first implementation attempt, the agent is pushed toward
optimistic handoff instead of using feedback from tests, docs builds, screenshots, or reviewer
notes.

## Helps

- Prevents premature handoff and makes validation failures part of the planned work instead of a
  surprise.

## Limits

Do not reserve heavy feedback loops for tiny edits that can be verified directly. Match the loop to
the risk, surface area, and cost of being wrong.

## Agent Instruction

Budget tokens and time for reading, editing, checks, failure inspection, and proof reporting.

## Mechanisms

Supported by explicit task budgets, staged plans, validation checklists, long-running command
timeouts, and handoffs that separate run checks from skipped checks.

## References

- [Principle: Private Context Is Not Shared
  Context](../../principles/private-context-is-not-shared-context.md)
- [OpenAI Harness Engineering: agent legibility is the
  goal](https://openai.com/index/harness-engineering/#agent-legibility-is-the-goal)
- [OpenAI Symphony README](https://github.com/openai/symphony#readme)
