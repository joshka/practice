# Manage Agent Work Not Sessions

## Metadata

- Name: `Manage Agent Work Not Sessions`
- ID: `manage-agent-work-not-sessions`
- Status: `reviewed`
- Audience: `both`
- Topics: `agents, workflow, orchestration`
- Related: `produce-review-packets, spend-human-attention-on-ambiguity`

## Problem

Interactive agent sessions do not scale past the amount of state a maintainer can hold in working
memory. Once the human is tracking which terminal is doing what, nudging stalled runs, and remembering
handoff state, the human has become the orchestrator.

## Preferred Move

Represent agent work as durable tasks with states, owners, workspaces, validation, and handoff
criteria. Let humans manage priorities, scope, and review decisions while the system handles setup,
continuation, retries, conflict recovery, and routine landing work.

## Tradeoff

Keep interactive sessions for ambiguous work that needs strong judgment, real-time exploration, or
deep design collaboration. Do not force every task into a background queue when the acceptance
criteria are not yet understood.

## Agent Instruction

When the work is routine and well-scoped, prefer a task-oriented handoff over a long supervised
session. State the task state, review criteria, and next human decision.

## Examples

Bad: the maintainer has to supervise the implementation loop directly.

```text
Open five terminals, start five agents, remember which one is blocked, and nudge each session until
it produces something reviewable.
```

Good: the work is tracked at the task level.

```text
Each active issue has one agent run, a workspace, current status, retry state, and a review packet
when it reaches Human Review.
```

## References

| Source                         | Use        | Note                                                                        |
| ------------------------------ | ---------- | --------------------------------------------------------------------------- |
| [Symphony blog][symphony-blog] | `supports` | Symphony shifts the human role from supervising sessions to reviewing work. |
| [Symphony SPEC problem][spec]  | `supports` | The spec defines issue execution as a repeatable daemon workflow.           |
| [Symphony README][readme]      | `supports` | Symphony frames the system as managing work instead of supervising agents.  |

[readme]: https://github.com/openai/symphony#readme
[spec]: https://github.com/openai/symphony/blob/main/SPEC.md#1-problem-statement
[symphony-blog]: https://openai.com/index/open-source-codex-orchestration-symphony/
