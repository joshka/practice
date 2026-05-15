# VCS Ask Before Repairing JJ Aliases

## Metadata

- ID: `VCS-ASK-BEFORE-REPAIRING-JJ-ALIASES`
- Legacy ID: `R-0727`
- Status: `reviewed`
- Domain: `vcs`
- Depth: `compact`

## Rule

Ask the user to repair jj aliases when topology and aliases disagree.

## Why

Aliases such as `trunk()` or publish helpers encode assumptions about remotes and bookmarks. If the
repo topology changes from `origin` to `upstream`, or from owned repo to fork workflow, silently
repairing aliases can change future commands for the user.

## Helps

- Keeps user-level jj configuration deliberate and prevents agents from rewriting source-control
  policy unexpectedly.

## Limits

Repo-local aliases can be updated as part of an explicit repo setup task. Ask first for user or
global aliases, or when the intended topology is still ambiguous.

## Agent Instruction

Ask before repairing jj aliases that encode remote or bookmark assumptions, especially `trunk()` and
publish helpers.

## Mechanisms

Supported by `jj config list`, repo versus user config inspection, topology notes, and explicit user
approval before alias repair.

## References

- [Principle: JJ Topology Is Repo Role
  Dependent](../../principles/jj-topology-is-repo-role-dependent.md)
- [Jujutsu docs: working copy](https://docs.jj-vcs.dev/latest/working-copy/)
- [Jujutsu docs: bookmarks](https://docs.jj-vcs.dev/latest/bookmarks/)
