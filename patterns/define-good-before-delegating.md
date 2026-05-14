# Define Good Before Delegating

## Metadata

- Name: `Define Good Before Delegating`
- ID: `define-good-before-delegating`
- Status: `reviewed`
- Audience: `agents`
- Topics: `agents, delegation, verification`
- Related: `smallest-trustworthy-verification, report-verification-honestly`

## Problem

Agents can produce plausible work without knowing what would make the task complete. A long plan is
not a substitute for acceptance criteria, validation evidence, or proof that the result satisfies
the user's real goal.

## Preferred Move

Before delegating or starting execution, identify what "good" means for this task. Name the
observable output, the checks that should pass, the evidence the handoff should include, and the
remaining judgment that requires human review.

## Tradeoff

Do not over-specify exploratory work before the shape is known. For discovery, define good as a
bounded answer with evidence, open questions, and a recommended next move.

## Agent Instruction

State the task's acceptance criteria before or during implementation. At handoff, show the proof of
work against those criteria instead of relying on the existence of a plan.

## Examples

Bad: the agent treats a plan as the artifact.

```text
I wrote a detailed plan for fixing the flaky import workflow.
```

Good: the agent names the expected proof.

```text
The import workflow is done when the retry test fails on main, passes with the fix, and the handoff
names the remaining external-service risk.
```
