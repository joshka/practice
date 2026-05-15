# VCS JJ New For Review Lanes

## Metadata

- ID: `VCS-JJ-NEW-FOR-REVIEW-LANES`
- Legacy ID: `R-0701`
- Status: `reviewed`
- Domain: `vcs`
- Depth: `compact`

## Rule

Use `jj new` for separate review lanes.

## Why

A new task needs a separate review lane before unrelated edits accumulate. `jj new` creates a fresh
change in the same workspace so the current change remains focused and later squash or absorb
decisions stay easy.

## Helps

- Keeps review units atomic and prevents unrelated work from piling into one change.

## Limits

Use the current change when the new edit is clearly part of the same atomic purpose. Use another
workspace only when another filesystem checkout is needed.

## Agent Instruction

Use `jj new` for separate review lanes because a new task needs a separate review lane before unrelated
edits accumulate.

## Mechanisms

Supported by `jj new`, early `jj desc`, small changes, status checks, and later `jj squash` or `jj
absorb` when follow-up belongs with its parent.

## References

- [Principle: JJ Topology Is Repo Role
  Dependent](../../principles/jj-topology-is-repo-role-dependent.md)
- [Jujutsu docs: working copy](https://docs.jj-vcs.dev/latest/working-copy/)
- [Jujutsu docs: bookmarks](https://docs.jj-vcs.dev/latest/bookmarks/)
