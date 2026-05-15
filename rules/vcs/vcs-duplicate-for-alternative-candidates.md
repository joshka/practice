# VCS Duplicate For Alternative Candidates

## Metadata

- ID: `VCS-DUPLICATE-FOR-ALTERNATIVE-CANDIDATES`
- Legacy ID: `R-0714`
- Status: `reviewed`
- Domain: `vcs`
- Depth: `compact`

## Rule

Use `jj duplicate` for safe alternative candidates.

## Why

When comparing two possible fixes or refactor shapes, mutating the only candidate makes it hard to
return to the original. `jj duplicate` gives an alternative change its own identity while preserving
the first candidate for comparison or recovery.

## Helps

- Makes experiments reversible and keeps competing designs reviewable.

## Limits

Do not duplicate just to avoid deciding. Use it when two plausible alternatives need independent
edits or validation.

## Agent Instruction

Use `jj duplicate` for alternative fixes or refactor shapes so the original candidate stays available.

## Mechanisms

Supported by `jj duplicate`, separate descriptions, focused validation per candidate, and eventual
abandon or squash of the losing candidate.

## References

- [Principle: Jj Topology Is Repo Role
  Dependent](../../principles/jj-topology-is-repo-role-dependent.md)
- [Jujutsu docs: working copy](https://docs.jj-vcs.dev/latest/working-copy/)
- [Jujutsu docs: bookmarks](https://docs.jj-vcs.dev/latest/bookmarks/)
