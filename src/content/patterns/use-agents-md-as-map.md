# Use AGENTS.md As Map

## Metadata

- Name: `Use AGENTS.md As Map`
- ID: `use-agents-md-as-map`
- Summary: A giant `AGENTS.md` grows stale and crowds out the context the agent actually needs.
  Keep it as a compact map to canonical guides, patterns, commands, and safety rules, with details
  living in owned files.
- Status: `reviewed`
- Audience: `agents`
- Topics: `agents, documentation, context`
- Tags: `agent-context, documentation, local-conventions`
- Related: `deliver-context-just-in-time, keep-docs-near-their-subject`

## Problem

A giant `AGENTS.md` becomes stale, crowded, and hard to verify. When every rule is in one injected
file, the agent loses attention for the task, the code, and the relevant deeper docs.

## Preferred Move

Keep `AGENTS.md` compact. Use it as the table of contents for the repo's durable guidance: guides,
patterns, runbooks, architecture notes, validation commands, and workflow rules. Put detailed
guidance in named files with clear ownership and links.

## Tradeoff

Some constraints must be visible immediately: safety, version-control rules, validation commands,
and the repo's highest-level purpose. Keep those in `AGENTS.md`, but link to the canonical details
instead of duplicating them.

## Agent Instruction

Treat `AGENTS.md` as the entry point, not the whole manual. Load the linked guide, pattern, or
runbook before making specialized changes.

## Examples

Bad: the agent file tries to be the full encyclopedia.

```md
# AGENTS.md

## Rust

Ten pages of Rust API preferences...

## Markdown

Ten pages of Markdown preferences...
```

Good: the agent file names the map and points to canonical owners.

```md
# AGENTS.md

- Rust API design: `guides/rust-maintainability.md`
- Markdown style: `guides/markdown-documentation.md`
- Agent workflow: `guides/coding-agents.md`
```

## References

| Source                                      | Use        | Note                                                          |
| ------------------------------------------- | ---------- | ------------------------------------------------------------- |
| [OpenAI knowledge system][knowledge-system] | `supports` | `AGENTS.md` works best as an entry point to deeper repo docs. |

[knowledge-system]: https://openai.com/index/harness-engineering/#we-made-repository-knowledge-the-system-of-record
