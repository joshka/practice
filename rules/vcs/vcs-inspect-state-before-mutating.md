# VCS Inspect State Before Mutating

## Metadata

- ID: `VCS-INSPECT-STATE-BEFORE-MUTATING`
- Name: `Inspect State Before Mutating`
- Summary: Inspect working-copy, stack, bookmark, conflict, and unowned state before mutation.
  Current state keeps edits scoped and avoids rewriting work the agent did not inspect.
- Status: `reviewed`
- Domain: `vcs`
- Tags: `vcs-jj, verification, ownership, change-shape`
- Related: `preserve-unowned-work, vcs-name-exact-jj-mutation-targets`

## Rule

Inspect working-copy and stack state before mutating.

## Why

Before creating, squashing, rebasing, publishing, or editing files, the agent needs to know the
current working copy, parent, bookmarks, conflicts, and unowned changes. Mutating first risks mixing
tasks or rewriting work it did not inspect.

## Helps

- Keeps changes scoped and avoids surprises from hidden graph or working-copy state.

## Limits

Tiny read-only tasks do not need full graph inspection. Inspect before commands that alter files,
changes, bookmarks, remotes, or publication state.

## Agent Instruction

Before creating, squashing, rebasing, publishing, or editing files, the agent needs to know the
current working copy, parent, bookmarks, conflicts, and unowned changes, inspect working-copy and
stack state before mutating.

## Mechanisms

Supported by `jj status`, `jj log`, `jj bookmark list`, `jj diff --stat`, and explicit path review
before editing.

## References

- [Principle: JJ Topology Is Repo Role
  Dependent](../../principles/jj-topology-is-repo-role-dependent.md)
- [Jujutsu docs: working copy](https://docs.jj-vcs.dev/latest/working-copy/)
- [Jujutsu docs: bookmarks](https://docs.jj-vcs.dev/latest/bookmarks/)
