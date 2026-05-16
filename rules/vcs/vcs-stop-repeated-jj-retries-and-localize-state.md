# VCS Stop Repeated JJ Retries And Localize State

## Metadata

- ID: `VCS-STOP-REPEATED-JJ-RETRIES-AND-LOCALIZE-STATE`
- Name: `Stop Repeated JJ Retries And Localize State`
- Summary: Stop repeating a failing jj command after a transient retry and inspect relevant state.
  Diagnosis beats command spam when locks, sparse paths, bookmarks, or remotes disagree.
- Status: `reviewed`
- Domain: `vcs`
- Depth: `compact`
- Related: `vcs-inspect-state-before-mutating, vcs-use-evolog-and-operation-log`

## Rule

Stop repeated jj retries and localize state.

## Why

Repeating a failing jj command without new information usually compounds confusion. A lock error,
missing bookmark, sparse path, or remote mismatch needs state inspection, not another identical
retry.

## Helps

- Turns source-control failures into diagnosis instead of command spam.

## Limits

One retry can be reasonable for a transient lock after the prior command finishes. After that,
inspect the relevant state before mutating.

## Agent Instruction

Stop repeated jj retries and localize state because repeating a failing jj command without new
information usually compounds confusion.

## Mechanisms

Supported by `jj status`, `jj op log`, lock-file inspection, `jj help`, sparse inspection, remote
inspection, and explicit notes about the localized failure.

## References

- [Principle: JJ Topology Is Repo Role
  Dependent](../../principles/jj-topology-is-repo-role-dependent.md)
- [Jujutsu docs: working copy](https://docs.jj-vcs.dev/latest/working-copy/)
- [Jujutsu docs: bookmarks](https://docs.jj-vcs.dev/latest/bookmarks/)
