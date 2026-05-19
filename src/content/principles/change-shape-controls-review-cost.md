# Change Shape Controls Review Cost

## Metadata

- Name: `Change Shape Controls Review Cost`
- ID: `change-shape-controls-review-cost`
- Summary: `Change boundaries determine how much intent, risk, validation, and revert cost a
  reviewer must reconstruct. Use the smallest coherent unit that preserves trust without splitting
  one decision into noise.`
- Status: `reviewed`
- Audience: `both`
- Topics: `change-shape, review, commits, refactoring`
- Tags: `change-shape, reviewability, review-handoff, verification`
- Related: `private-context-is-not-shared-context`

## Claim

The shape of a change affects how expensive it is to review, validate, revert, and explain. A small
change with one purpose usually costs less to trust than a broad change whose correctness depends on
holding many unrelated facts at once.

## Why This Exists

Reviewers do not only review the final diff. They also reconstruct intent, check blast radius,
decide whether the tests prove the right thing, and estimate what might break. Mixed-purpose changes
make that work harder because structure edits, behavior edits, dependency churn, generated output,
and documentation updates can obscure each other.

## Good Uses

- Split behavior changes from large mechanical cleanup.
- Keep generated artifacts synchronized with the source that produced them.
- Move controversial or speculative changes into their own review lane.
- Prefer follow-up changes when a small safe improvement is useful but not required.

## Bad Smells

- A PR description cannot name one primary purpose.
- Reviewers need private chat history to understand why the change exists.
- A revert would remove unrelated fixes.
- Dependency updates, formatting, API changes, and behavior changes are all mixed without need.

## Limits

Small changes are not automatically better. A sequence of tiny changes can become expensive if each
one needs the same reviewer context or if the value is only visible when several files are read
together. Split where it reduces risk or review burden, and batch where the combined artifact is the
smallest coherent unit.

## Agent Consequences

Prefer one-purpose changes with standalone descriptions. Keep unrelated edits separate unless the
reviewer needs them together to understand or validate the work.
