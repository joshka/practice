# Encode Nonfunctional Requirements

## Metadata

- Name: `Encode Nonfunctional Requirements`
- ID: `encode-nonfunctional-requirements`
- Status: `reviewed`
- Audience: `both`
- Topics: `agents, architecture, quality`
- Related: `make-bad-output-mechanically-hard, prefer-tools-over-prompts`

## Problem

Quality often depends on requirements that are not visible in the feature prompt: reliability,
performance, security, accessibility, architecture boundaries, observability, maintainability, and
operational constraints. Agents miss these when they live only as human taste.

## Preferred Move

Write nonfunctional requirements down and encode the stable ones into checks, architecture rules,
templates, review gates, or examples. Make the invisible bar visible before the agent has to infer
it from rejection.

## Tradeoff

Do not freeze every preference too early. Start with docs and examples while the rule is forming;
promote it to mechanical enforcement when it is stable and repeatedly valuable.

## Agent Instruction

When a task has hidden quality requirements, name them before implementation. If a requirement is
stable and checkable, propose the smallest durable check that enforces it.

## Examples

Bad: the prompt implies performance without defining the bar.

```text
Make startup faster.
```

Good: the nonfunctional requirement is measurable.

```text
Make startup complete under 800 ms for the local development path and report the measured command.
```

## References

| Source                                  | Use        | Note                                                              |
| --------------------------------------- | ---------- | ----------------------------------------------------------------- |
| [OpenAI architecture enforcement][arch] | `supports` | Architecture and taste can be encoded as mechanical constraints.  |

[arch]: https://openai.com/index/harness-engineering/#enforcing-architecture-and-taste
