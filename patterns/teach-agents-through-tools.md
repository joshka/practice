# Teach Agents Through Tools

## Metadata

- Name: `Teach Agents Through Tools`
- ID: `teach-agents-through-tools`
- Summary: Repeated agent confusion often means the repo lacks a command, fixture, wrapper, or
  check rather than another instruction. Convert repeatable setup, inspection, validation, and
  remediation into tools when they will improve future runs.
- Status: `reviewed`
- Audience: `agents`
- Topics: `agents, tooling, enablement`
- Tags: `tooling, automation, agent-workflow`
- Related: `prefer-tools-over-prompts, code-is-memory-of-process`

## Problem

When an agent struggles, the missing piece is often not another instruction. The repo may lack the
tool, command, fixture, wrapper, script, or check that would put the agent in position to do the work
reliably.

## Preferred Move

Teach agents by building the tools they need. Convert repeated manual setup, inspection, validation,
or remediation into commands and checked artifacts the agent can use directly. Prefer enabling the
next run over rescuing only the current run.

## Tradeoff

Do not build a tool for a one-off confusion. Add tooling when the missing capability blocks repeated
work, reduces human attention, or makes validation more reliable.

## Agent Instruction

When blocked, ask what tool or repo artifact would make the task straightforward next time. If the
scope is small, build that enabling tool before continuing.

## Examples

Bad: the agent repeatedly asks the human to gather the same evidence.

```text
Can you open the app, reproduce the modal bug, and paste the console error?
```

Good: the repo gains a tool that gives the agent the evidence.

```text
Added `scripts/capture-modal-error.sh` to boot the app, drive the modal path, and save the console
log for agent review.
```

## References

| Source                                  | Use        | Note                                                        |
| --------------------------------------- | ---------- | ----------------------------------------------------------- |
| [OpenAI missing capability][capability] | `supports` | Agent failures point to missing tools, guardrails, or docs. |

[capability]: https://openai.com/index/harness-engineering/#redefining-the-role-of-the-engineer
