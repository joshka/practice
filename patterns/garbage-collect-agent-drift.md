# Garbage Collect Agent Drift

## Metadata

- Name: `Garbage Collect Agent Drift`
- ID: `garbage-collect-agent-drift`
- Summary: Agent-generated notes, plans, and assumptions can outlive their usefulness and mislead
  later work. Periodically remove, update, or promote them so durable guidance stays current and
  temporary scaffolding does not become false context.
- Status: `reviewed`
- Audience: `both`
- Topics: `agents, maintenance, refactoring`
- Related: `optimize-for-long-term-coherence, turn-feedback-into-guidance`

## Problem

Agent-generated systems accumulate drift by copying existing uneven patterns, spreading weak
abstractions, and leaving stale docs or tests behind. Waiting for a large cleanup lets the drift
compound.

## Preferred Move

Run small recurring cleanup loops. Encode golden principles as patterns, lints, tests, quality
grades, or focused review checks. Let agents open targeted fixups that are easy to review and merge.

## Tradeoff

Do not churn code just to make it uniform. Garbage collection should remove real drift: stale docs,
broken boundaries, repeated weak patterns, noisy tests, or quality gaps that will mislead future
work.

## Agent Instruction

When you find repeated drift, propose the recurring check or small cleanup path. Prefer focused
fixups that keep future agent runs aligned.

## Examples

Bad: cleanup is saved for a painful rewrite.

```text
We should eventually clean up all the inconsistent schema helpers.
```

Good: cleanup is continuous and scoped.

```text
Added a check for schema helper naming and opened a focused follow-up to normalize the three
violations it found.
```

## References

| Source                          | Use        | Note                                                               |
| ------------------------------- | ---------- | ------------------------------------------------------------------ |
| [OpenAI garbage collection][gc] | `supports` | Agent systems need recurring cleanup to prevent entropy and drift. |

[gc]: https://openai.com/index/harness-engineering/#entropy-and-garbage-collection
