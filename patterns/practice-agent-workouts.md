# Practice Agent Workouts

## Metadata

- Name: `Practice Agent Workouts`
- ID: `practice-agent-workouts`
- Summary: High-risk or repeated agent workflows are unreliable when first exercised during real
  work. Build safe practice tasks with explicit win conditions so the workflow, skill, or runbook
  can improve before pressure arrives.
- Status: `reviewed`
- Audience: `agents`
- Topics: `agents, skills, reliability`
- Tags: `agent-workflow, verification, automation`
- Related: `close-the-agent-loop, define-good-before-judgment-heavy-work`

## Problem

High-level workflows are unreliable when they are only tested during real work. Login flows,
uploads, permission changes, UI navigation, and deployment procedures need practice targets before
they can be trusted under pressure.

## Preferred Move

Create practice tasks with explicit win conditions. Use safe fixtures, flags, canaries, or sandbox
states so the agent can exercise the workflow, reflect on failures, update the skill or runbook, and
rerun until reliability improves.

## Tradeoff

Do not build elaborate training harnesses for one-off tasks. Use workouts for workflows that will be
repeated, delegated, or allowed to run with less supervision.

## Agent Instruction

When a workflow is important and repeatable, propose a safe workout that exercises it end to end.
Capture failures as updates to the skill, runbook, or validation checklist.

## Examples

Bad: the first real permission change is the first full test of the workflow.

```text
Grant the production group access and see whether the UI flow works.
```

Good: the agent practices against a harmless target first.

```text
Grant access to the sandbox group, verify the expected marker appears, update the runbook for the
two-factor prompt, then repeat before touching production.
```
