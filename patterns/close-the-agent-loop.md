# Close The Agent Loop

## Metadata

- Name: `Close The Agent Loop`
- ID: `close-the-agent-loop`
- Summary: Agent work is incomplete when it stops at edits without checking the result or explaining
  residual risk. Finish the loop by validating, reporting evidence, and making the next human
  decision clear.
- Status: `reviewed`
- Audience: `agents`
- Topics: `agents, verification, feedback`
- Related: `turn-feedback-into-guidance, define-good-before-judgment-heavy-work`

## Problem

Agent work stalls when it is one-way: prompt, output, human correction, repeat. The system only
improves when failures become feedback that changes the checks, docs, tools, or workflow for the
next run.

## Preferred Move

Create a closed loop: produce work, validate it, inspect the failure, update the harness or guidance,
and rerun when appropriate. Prefer loops with a concrete win condition, such as a passing test,
captured flag, successful canary, benchmark threshold, or accepted review checklist.

## Tradeoff

Not every task needs a full self-improvement loop. Use the loop when the workflow is repeated,
high-risk, or expensive for humans to supervise manually.

## Agent Instruction

When a task exposes a repeated failure mode, improve the loop that produced it. Report the new
validation point or harness change that should prevent the same failure next time.

## Examples

Bad: the same UI workflow is retried manually after every failure.

```text
The login automation failed again; I clicked through it by hand.
```

Good: the failure updates the loop.

```text
The login automation failed at the two-factor step, so I added that state to the runbook and reran
the workflow until the success marker appeared.
```
