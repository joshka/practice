# VCS Track Remotes Explicitly

## Metadata

- ID: `VCS-TRACK-REMOTES-EXPLICITLY`
- Legacy ID: `R-0718`
- Status: `reviewed`
- Domain: `vcs`
- Depth: `compact`

## Rule

Track remotes explicitly when bookmark names exist on multiple remotes.

## Why

When the same bookmark name exists on multiple remotes, implicit tracking can choose the wrong
source or make publication ambiguous. Explicit tracking tells jj which remote bookmark represents
the local line of work.

## Helps

- Prevents fetch, rebase, and publication confusion in fork and upstream workflows.

## Limits

Single-remote repos may not need explicit repair after inspection confirms there is only one
meaningful remote for the bookmark.

## Agent Instruction

Track remotes explicitly for bookmark names that exist on multiple remotes so source and publication
targets are clear.

## Mechanisms

Supported by `jj bookmark list --all-remotes`, tracking commands, remote topology notes, and PR
base/head checks.

## References

- [Principle: Jj Topology Is Repo Role
  Dependent](../../principles/jj-topology-is-repo-role-dependent.md)
- [Jujutsu docs: working copy](https://docs.jj-vcs.dev/latest/working-copy/)
- [Jujutsu docs: bookmarks](https://docs.jj-vcs.dev/latest/bookmarks/)
