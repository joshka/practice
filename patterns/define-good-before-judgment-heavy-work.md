# Define Good Before Judgment-Heavy Work

## Metadata

- Name: `Define Good Before Judgment-Heavy Work`
- ID: `define-good-before-judgment-heavy-work`
- Status: `reviewed`
- Audience: `agents`
- Topics: `agents, acceptance criteria, verification, judgment`
- Related: `smallest-trustworthy-verification, report-verification-honestly`

## Problem

Agents can produce plausible work by inferring the quality bar from nearby context. That inference
often works for routine edits, but it breaks down when the task depends on taste, naming, grouping,
scope, review shape, public API judgment, or another standard that is easy for the user to hold but
hard for the agent to guess.

A long plan is not a substitute for acceptance criteria, validation evidence, or proof that the
result satisfies the user's real goal.

## Preferred Move

Before delegating or starting judgment-heavy execution, identify what "good" means for this task.
Ask the model or the maintainer to state the ideas, rules, goal posts, naming criteria, review
criteria, or acceptance checks first. Use that stated quality bar to perform the work, then verify
the output against it.

Name the observable output, the checks that should pass, the evidence the handoff should include,
and the remaining judgment that requires human review.

## Tradeoff

Do not over-specify exploratory work before the shape is known. For discovery, define good as a
bounded answer with evidence, open questions, and a recommended next move. For taste-heavy work,
define the taste criteria without freezing every resulting edit.

## Agent Instruction

For judgment-heavy work, establish the quality bar before changing the artifact. At handoff, show
the proof of work against those criteria instead of relying on the existence of a plan.

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

Good: the agent defines the naming bar before renaming.

```text
Rule IDs should be stable handles: short enough to cite, specific enough to preserve meaning, and
careful about connector words when removing them would change the concept. I will rename against
that bar and then check for stale references.
```
