# Small Reviewable Chunks

## Metadata

- Name: `Small Reviewable Chunks`
- ID: `small-reviewable-chunks`
- Status: `draft`
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

## Tradeoff

Splitting too aggressively can create process overhead. Keep tiny follow-ups together when they are
obviously inseparable from the same review decision.

## Agent Instruction

Work one reviewable chunk at a time. Before choosing the next preference-sensitive chunk, offer a
few concrete options with the recommended one first and explain the tradeoff.

## References

- Link: `README.md`
- Use: `supports`
- Note: The repo delivery approach is built around local review loops and incremental chunks.
