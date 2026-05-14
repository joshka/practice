# Prefer Durable Summaries

## Metadata

- Name: `Prefer Durable Summaries`
- ID: `prefer-durable-summaries`
- Status: `reviewed`
- Audience: `both`
- Topics: `documentation, summaries, rationale`
- Related: `write-docs-as-contracts, delete-redundant-comments`

## Problem

Important context becomes expensive when every maintainer or agent has to rediscover it by scanning
the implementation. Long narration creates another maintenance burden, but no summary at all makes
future work start from a cold read.

## Preferred Move

Capture stable context as a short summary: the invariant, rationale, boundary, ordering rule,
compatibility constraint, or side effect that future work needs. Prefer a concise paragraph or
comment over either exhaustive narration or no durable context.

## Tradeoff

Do not summarize facts that are obvious from the next line of code. The summary should survive
nearby implementation changes and still help a reader avoid rediscovery.

## Agent Instruction

When a change relies on non-obvious context, add a short durable summary near the relevant code or
guide. Keep the summary stable enough that it will not need editing for ordinary implementation
changes.

## Examples

Bad: the comments narrate each statement without preserving useful context.

```rust
// Get the pending jobs.
let jobs = queue.pending();
// Sort the jobs.
let jobs = sort_by_priority(jobs);
// Run each job.
for job in jobs {
    runner.run(job)?;
}
```

Good: the comment captures the durable ordering rule.

```rust
// Run high-priority jobs first so lease renewal work cannot starve user-visible work.
for job in sort_by_priority(queue.pending()) {
    runner.run(job)?;
}
```

## References

| Source                                  | Use        | Note                                                          |
| --------------------------------------- | ---------- | ------------------------------------------------------------- |
| [Diátaxis explanation context][context] | `supports` | Explanation is where durable context and rationale belong.    |
| [Rust API examples][examples]           | `adapts`   | Documentation should communicate purpose, not just mechanics. |

[context]: https://diataxis.fr/explanation/#provide-context
[examples]: https://rust-lang.github.io/api-guidelines/documentation.html#c-example
