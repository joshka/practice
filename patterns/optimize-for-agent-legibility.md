# Optimize For Agent Legibility

## Metadata

- Name: `Optimize For Agent Legibility`
- ID: `optimize-for-agent-legibility`
- Summary: Repositories that are hard for agents to inspect, search, run, and validate make
  delegated work slower and less reliable. Prefer structures, commands, names, examples, and
  runtime signals that help both agents and human maintainers reason locally.
- Status: `reviewed`
- Audience: `both`
- Topics: `agents, architecture, documentation`
- Tags: `agent-context, agent-workflow, reader-locality`
- Related: `document-system-mental-models, make-runtime-state-agent-legible`

## Problem

Humans are no longer the only important reader of a repo. If the repository is difficult for agents
to inspect, search, run, validate, or reason about, agent work becomes slower and less reliable even
when the code is understandable to a human expert.

## Preferred Move

Design repo structure, docs, commands, tests, examples, and runtime signals so agents can navigate
them. Prefer consistent layouts, explicit boundaries, searchable names, local run commands,
machine-readable artifacts, and clear maps from high-level concepts to files.

## Tradeoff

Do not sacrifice human maintainability for agent convenience. The best legibility improvements help
both: clearer ownership, sharper boundaries, better validation, and less implicit knowledge.

## Agent Instruction

When changing repo structure or docs, consider whether future agents can find the right context and
validate the result. Report any agent-legibility improvement or gap.

## Examples

Bad: the concept exists, but its owner is only discoverable by tribal knowledge.

```text
The import retry policy is spread across helpers, tests, and a Slack decision from last month.
```

Good: the repo gives agents and humans a map.

```text
`docs/imports/retry-policy.md` links to the service module, retry tests, and runtime metric used to
verify import recovery behavior.
```

## References

| Source                                      | Use        | Note                                                        |
| ------------------------------------------- | ---------- | ----------------------------------------------------------- |
| [OpenAI agent legibility][agent-legibility] | `supports` | Repos should expose the domain in a way agents can inspect. |

[agent-legibility]: https://openai.com/index/harness-engineering/#agent-legibility-is-the-goal
