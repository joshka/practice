# Turn Feedback Into Guidance

## Metadata

- Name: `Turn Feedback Into Guidance`
- ID: `turn-feedback-into-guidance`
- Summary: Repeated steering signals that a preference is missing from durable repo guidance or
  tooling. Fix the current artifact and encode the reusable lesson at the right level when the
  feedback applies beyond one line.
- Status: `reviewed`
- Audience: `agents`
- Topics: `agents, feedback, process`
- Tags: `agent-workflow, automation, source-truth, feedback-loops`
- Related: `prefer-durable-summaries, report-verification-honestly`

## Problem

Repeated steering wastes maintainer attention. If the same correction is needed across sessions,
the agent treated feedback as a one-off patch instead of a signal that the repo lacks durable
guidance, tests, lint, snippets, or workflow support.

## Preferred Move

When feedback reveals a reusable preference, update the system that should have prevented the miss.
That might be a pattern, guide, template, lint rule, test, snippet, or agent instruction. Fix the
current artifact and capture the generalized lesson at the right level.

## Tradeoff

Do not turn every comment into a permanent rule. Capture feedback when it applies beyond the
current line, when it has repeated, or when failing to encode it will likely cost future review
time.

## Agent Instruction

When maintainer feedback points to a broader preference, propose or make a small durable guidance
update in addition to fixing the immediate issue. Name the generalized lesson in the handoff.

## Examples

Bad: the agent fixes only the specific example.

```text
Changed this one bool return into a named error.
```

Good: the agent fixes the instance and records the reusable rule.

```text
Changed this bool return into a named error and added the API pattern that fallible operations
should report the failing condition instead of collapsing it into success/failure.
```
