# Agent Budget For Feedback Loops

## Metadata

- Name: `Budget for Feedback Loops`
- ID: `AGENT-BUDGET-FOR-FEEDBACK-LOOPS`
- Summary: Reserve enough time and tokens for checks, failure inspection, and handoff proof.
  Planning for the feedback loop keeps validation from being squeezed out after the first edit.
- Related: `budget-tokens-for-feedback-loops, close-the-agent-loop,
  report-verification-honestly`
- Status: `reviewed`
- Domain: `agent-workflow`
- Tags: `agent-workflow, verification, review-handoff, feedback-loops`

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

Respect the user's budget. Stop after the required checks pass unless a new finding, changed
artifact, or unresolved contract justifies more work. Repeated equivalent reviews and status
narration consume capacity without adding evidence.

## Agent Instruction

Reserve time and tokens for validation and handoff. Give each extra pass a distinct question. Stop
after required gates pass unless new evidence warrants another pass; budgets are ceilings.

## Mechanisms

Supported by explicit task budgets, staged plans, validation checklists, long-running command
timeouts, and handoffs that separate run checks from skipped checks.

## References

- [Principle: Private Context Is Not Shared
  Context](../../principles/private-context-is-not-shared-context.md)
- [OpenAI Harness Engineering: agent legibility is the
  goal](https://openai.com/index/harness-engineering/#agent-legibility-is-the-goal)
- [OpenAI Symphony README](https://github.com/openai/symphony#readme)
