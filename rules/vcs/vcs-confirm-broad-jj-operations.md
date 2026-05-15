# VCS Confirm Broad JJ Operations

## Metadata

- ID: `VCS-CONFIRM-BROAD-JJ-OPERATIONS`
- Legacy ID: `R-0716`
- Status: `reviewed`
- Domain: `vcs`
- Depth: `compact`

## Rule

Treat broad jj operations as confirmation-worthy.

## Why

Commands that abandon, rebase, squash, split, restore, publish, or affect many revisions can rewrite
a large part of the graph. Confirmation protects unrelated work when the target, fileset, or remote
is broader than a normal local edit.

## Helps

- Reduces accidental history reshaping and publication mistakes.

## Limits

Routine local inspection and narrowly targeted edits should not require ceremony. Confirm when the
operation is destructive, public, or broad enough to surprise the user.

## Agent Instruction

Treat broad jj operations as confirmation-worthy because commands that abandon, rebase, squash, split,
restore, publish, or affect many revisions can rewrite a large part of the graph.

## Mechanisms

Supported by dry-run output, explicit revsets, operation summaries, `jj op log`, and user
confirmation before broad mutation.

## References

- [Principle: Jj Topology Is Repo Role
  Dependent](../../principles/jj-topology-is-repo-role-dependent.md)
- [Jujutsu docs: working copy](https://docs.jj-vcs.dev/latest/working-copy/)
- [Jujutsu docs: bookmarks](https://docs.jj-vcs.dev/latest/bookmarks/)
