# Give Agents Objectives With Boundaries

## Metadata

- Name: `Give Agents Objectives With Boundaries`
- ID: `give-agents-objectives-with-boundaries`
- Status: `reviewed`
- Audience: `both`
- Topics: `agents, delegation, workflow`
- Related: `define-good-before-delegating, grant-scoped-agent-capabilities`

## Problem

Rigid step lists can make agents less effective when the real work requires judgment, tool use, or a
different route than the prompt author predicted. Fully open-ended delegation has the opposite
problem: the agent may expand scope, choose unsafe actions, or optimize the wrong outcome.

## Preferred Move

Give the agent the objective, success criteria, boundaries, available tools, and handoff state. Let
the agent choose the implementation path inside those boundaries, and require evidence before the
work moves to review or merge.

## Tradeoff

Some tasks genuinely need exact procedures: compliance steps, production commands, migration order,
or destructive operations. Use step-by-step instructions when the sequence is part of the safety
contract.

## Agent Instruction

When delegating or accepting work, restate the objective, boundaries, and success evidence. Do not
treat a step list as more important than the user's actual goal when the steps become stale.

## Examples

Bad: the task overfits the implementation route and hides the goal.

```text
Edit checkout.ts line 42, add a timeout, rerun this one test, and open a PR.
```

Good: the task gives the agent a bounded objective.

```text
Make checkout retry payment-intent refresh once after a transient provider timeout. Keep retries
idempotent, update tests, and hand off with the failing/passing regression evidence.
```

## References

| Source                         | Use        | Note                                                                 |
| ------------------------------ | ---------- | -------------------------------------------------------------------- |
| [Symphony blog][symphony-blog] | `supports` | The workflow moved toward objectives instead of rigid transitions.   |
| [Harness engineering][harness] | `supports` | Strict boundaries and tools let agents work without micromanagement. |

[harness]: https://openai.com/index/harness-engineering/#enforcing-architecture-and-taste
[symphony-blog]: https://openai.com/index/open-source-codex-orchestration-symphony/
