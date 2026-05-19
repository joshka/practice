# Choose Doc Pass Depth

## Metadata

- Name: `Choose Doc Pass Depth`
- ID: `choose-doc-pass-depth`
- Summary: Documentation work ranges from quick polish to structural repair, and using the wrong
  pass depth wastes attention. Match the edit depth to the evidence, risk, and review need before
  changing the document.
- Status: `reviewed`
- Audience: `both`
- Topics: `documentation, workflow, review`
- Tags: `documentation, reviewability, source-truth`
- Related: `choose-doc-type, small-reviewable-chunks`

## Problem

Documentation edits sprawl when every problem invites a full rewrite. A typo fix turns into voice
cleanup, voice cleanup turns into information architecture, and the original change becomes hard to
review.

## Preferred Move

Choose the page job and pass depth before editing. Use a surgical pass for local correctness, a
coherence pass for one document's structure and flow, and an architecture pass when the
documentation set itself has the wrong map. Keep one dominant mode per page: task, reference,
explanation, or decision record.

## Tradeoff

Sometimes a local edit exposes a deeper structural problem. Capture the larger problem as follow-up
work unless the current doc is actively misleading or the behavior change cannot be understood
without the broader repair.

## Agent Instruction

Before editing docs, state the intended page job and pass depth, then keep edits inside them. If you
discover a larger problem, record it separately instead of silently expanding the diff.

## Examples

Bad: the change mixes unrelated pass depths.

```diff
- This command starts the server.
+ This command starts the server.
+
+ ## Architecture
+
+ The product has three deployment modes...
```

Good: the change fixes the local contract and leaves the larger rewrite as follow-up.

```diff
- This command starts the server.
+ This command starts the server and writes the PID file.
```

## References

| Source                         | Use      | Note                                                   |
| ------------------------------ | -------- | ------------------------------------------------------ |
| [Diataxis workflow][workflow]  | `adapts` | Documentation work benefits from an explicit workflow. |
| [GitHub PR guidance][pr]       | `adapts` | Small focused changes are easier to review.            |

[pr]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/helping-others-review-your-changes
[workflow]: https://diataxis.fr/how-to-use-diataxis/
