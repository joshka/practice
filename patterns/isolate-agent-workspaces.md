# Isolate Agent Workspaces

## Metadata

- Name: `Isolate Agent Workspaces`
- ID: `isolate-agent-workspaces`
- Summary: Shared worktrees make it easy for agent edits, generated files, or validation steps to
  collide with unrelated work. Use isolated workspaces when concurrent tasks or uncertain changes
  need clear ownership and cleanup.
- Status: `reviewed`
- Audience: `both`
- Topics: `agents, workflow, safety`
- Related: `preserve-agent-context-coherence, grant-scoped-agent-capabilities`

## Problem

Parallel agent work becomes fragile when agents share a mutable checkout, ambient state, or unclear
ownership boundary. One run can corrupt another run's context, overwrite work, leak secrets, or make
recovery depend on manual cleanup.

## Preferred Move

Give each independent agent task its own workspace and execution identity. Make the workspace path,
task identifier, setup hooks, cleanup policy, approval posture, and logs explicit enough that the run
can be restarted or inspected without guessing.

## Tradeoff

Isolation has setup cost. For tiny read-only questions, a side session may be enough. Use dedicated
workspaces when the agent will edit files, run long-lived commands, use credentials, or execute in
parallel with other work.

## Agent Instruction

Before starting parallel or long-running agent work, confirm the workspace boundary and ownership.
Do not share a dirty checkout across unrelated agent tasks.

## Examples

Bad: two agents edit the same checkout without task ownership.

```text
Agent A updates checkout retry logic while Agent B refactors payment errors in the same working tree.
```

Good: each task has an isolated workspace and state.

```text
PAY-142 runs in workspaces/PAY-142 with its own branch/change, logs, retry state, and cleanup policy.
PAY-151 runs separately and cannot overwrite PAY-142's files.
```

## References

| Source                                 | Use        | Note                                                                        |
| -------------------------------------- | ---------- | --------------------------------------------------------------------------- |
| [Symphony SPEC workspaces][workspaces] | `supports` | Symphony assigns workspaces per issue and documents lifecycle rules.        |
| [Symphony SPEC state][state]           | `supports` | Explicit orchestration state prevents duplicate dispatch and aids recovery. |

[state]: https://github.com/openai/symphony/blob/main/SPEC.md#7-orchestration-state-machine
[workspaces]: https://github.com/openai/symphony/blob/main/SPEC.md#9-workspace-management-and-safety
