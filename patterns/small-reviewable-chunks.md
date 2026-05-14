# Small Reviewable Chunks

## Metadata

- Name: `Small Reviewable Chunks`
- ID: `small-reviewable-chunks`
- Status: `reviewed`
- Audience: `both`
- Topics: `workflow, review, version-control`
- Related: `report-verification-honestly, smallest-trustworthy-verification`

## Problem

Large mixed changes make it hard for a maintainer to give strong input. Structure, wording,
behavior, and workflow decisions blur together, so review becomes either slow or shallow.

## Preferred Move

Choose one coherent purpose for each chunk. Implement, validate, and review that unit before moving
to the next. When the next chunk is preference-sensitive, offer concrete choices and wait for
direction.
For structural preparation, include only the cleanup needed for the next behavior change or review
decision. Integrate that chunk before expanding the scope.

## Tradeoff

Splitting too aggressively can create process overhead. Keep tiny follow-ups together when they are
obviously inseparable from the same review decision.
Review latency changes the economics: fast review supports smaller chunks; slow review rewards
larger chunks unless the workflow deliberately keeps review units focused.
Oversized batches raise the chance of conflicts, hidden behavior changes, and cleanup that no longer
serves the current decision.

## Agent Instruction

Work one reviewable chunk at a time. Before choosing the next preference-sensitive chunk, offer a
few concrete options with the recommended one first and explain the tradeoff.
When preparing structure, stop once the next behavior change is easy enough to review.

## Examples

Bad: one change mixes guide structure, pattern content, lint config, and publication workflow.

```text
Add guides, rewrite patterns, change lint rules, and push all updates.
```

Good: the next chunk has one reviewable purpose.

```text
Add the Rust maintainability guide and link it to existing reviewed patterns.
```

## References

| Source                          | Use      | Note                                                      |
| ------------------------------- | -------- | --------------------------------------------------------- |
| [Tidy First, Ch. 16][tidy-ch16] | `adapts` | Split structure and behavior when review would blur them. |
| [Tidy First, Ch. 18][tidy-ch18] | `adapts` | Chunk size depends on review cost and integration risk.   |

[tidy-ch16]: https://www.oreilly.com/library/view/tidy-first/9781098151232/ch16.html
[tidy-ch18]: https://www.oreilly.com/library/view/tidy-first/9781098151232/ch18.html
