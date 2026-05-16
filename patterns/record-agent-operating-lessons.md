# Record Agent Operating Lessons

## Metadata

- Name: `Record Agent Operating Lessons`
- ID: `record-agent-operating-lessons`
- Summary: Agent work produces useful operational knowledge that is easy to lose after the task
  succeeds or fails. Record reusable lessons in the right durable place so future runs inherit the
  improved workflow instead of rediscovering it.
- Status: `reviewed`
- Audience: `agents`
- Topics: `agents, observability, handoff`
- Related: `turn-feedback-into-guidance, report-verification-honestly`

## Problem

Agent failures often disappear into the conversation transcript. Missing tools, missing context,
environment surprises, and repeated mistakes then recur because no durable artifact captures the
operating lesson.

## Preferred Move

When a lesson will help future sessions, record it in the repo's chosen durable place: an agent
guide, pattern, snippet, template, or backlog. Separate mistakes, missing context or tools, and
environment discoveries when that distinction helps action.

## Tradeoff

Do not create noisy logs of every transient issue. Capture lessons that are likely to recur, affect
handoff quality, or point to an improvement in docs, checks, tools, or workflow.

## Agent Instruction

If you discover a repeated mistake, missing tool, missing context, or environment fact that future
agents need, add it to the appropriate durable guidance or backlog. Do not hide the lesson in the
final message only.

## Examples

Bad: the lesson is left as a one-time apology.

```text
Sorry, I forgot to run markdownlint.
```

Good: the lesson updates the operating system.

```text
Added markdownlint to the validation checklist and ran it for this change.
```
