# Make Runtime State Agent Legible

## Metadata

- Name: `Make Runtime State Agent Legible`
- ID: `make-runtime-state-agent-legible`
- Status: `reviewed`
- Audience: `both`
- Topics: `agents, observability, validation`
- Related: `define-good-before-judgment-heavy-work, close-the-agent-loop`

## Problem

Agents cannot reliably validate behavior they cannot observe. If UI state, logs, metrics, traces,
screenshots, or local app instances are only available to humans, the agent must guess whether the
change worked.

## Preferred Move

Expose runtime state through tools the agent can query. Make local app boot, UI inspection, logs,
metrics, traces, screenshots, and generated artifacts available per task or worktree when they are
needed for validation.

## Tradeoff

Do not build a full observability harness for every small repo. Start with the smallest signal that
lets the agent prove the changed behavior, then add richer runtime visibility for repeated or
high-risk workflows.

## Agent Instruction

When behavior depends on runtime state, use or create a legible validation path. Report the runtime
signal used, not only the code change.

## Examples

Bad: the agent claims a UI fix without seeing the UI.

```text
Changed the modal state handling; the dialog should close now.
```

Good: the agent uses runtime evidence.

```text
Launched the local app, opened the modal, clicked Save, and captured before/after screenshots showing
the dialog closes and the success toast appears.
```

## References

| Source                                   | Use        | Note                                                              |
| ---------------------------------------- | ---------- | ----------------------------------------------------------------- |
| [OpenAI application legibility][legible] | `supports` | Agents need direct access to app state and observability signals. |

[legible]: https://openai.com/index/harness-engineering/#increasing-application-legibility
