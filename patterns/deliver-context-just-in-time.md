# Deliver Context Just In Time

## Metadata

- Name: `Deliver Context Just In Time`
- ID: `deliver-context-just-in-time`
- Status: `reviewed`
- Audience: `agents`
- Topics: `agents, context, harness`
- Related: `use-disk-as-context-sink, keep-docs-near-their-subject`

## Problem

Bloated prompts make agents juggle instructions that may not matter yet, while missing context at
the decision point leads to local but wrong choices. The problem is often timing, not total amount
of information.

## Preferred Move

Keep durable context near its owner and deliver the relevant slice when the agent reaches the task
that needs it. Prefer linked guides, runbooks, snippets, tool output, and retrieval over one giant
static instruction block.

## Tradeoff

Some global constraints need to be present from the start, especially safety, ownership, and
workflow boundaries. Keep those compact, then retrieve task-specific context later.

## Agent Instruction

Before acting on a specialized area, load the nearest relevant guide, runbook, examples, or source
files. Avoid carrying unrelated instructions forward as active constraints.

## Examples

Bad: every automation receives every policy document.

```text
Read all repo guidance, all security policies, all deployment docs, and all historical incident
notes before checking the nightly job.
```

Good: the automation loads the relevant runbook at the point of use.

```text
For the nightly job, read docs/automations/nightly-import.md and the linked validation checklist.
```
