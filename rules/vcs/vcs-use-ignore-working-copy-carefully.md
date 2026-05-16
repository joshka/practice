# VCS Use Ignore Working Copy Carefully

## Metadata

- ID: `VCS-USE-IGNORE-WORKING-COPY-CAREFULLY`
- Name: `Use Ignore Working Copy Carefully`
- Summary: Use `--ignore-working-copy` only for understood lock-safe inspection or metadata work.
  It may read stale file state, so do not use it to bypass normal synchronization before edits.
- Status: `reviewed`
- Domain: `vcs`
- Depth: `compact`
- Related: `vcs-run-jj-mutations-sequentially, vcs-inspect-state-before-mutating`

## Rule

Use `--ignore-working-copy` only for lock-safe inspection or intended metadata updates.

## Why

`--ignore-working-copy` can be useful when the working copy is locked or when only metadata is
needed, but it also means jj may not snapshot current file changes before answering. Misuse can make
commands operate on stale state.

## Helps

- Avoids stale reads and accidental metadata changes during lock recovery.

## Limits

Use it for lock-safe inspection or intentional metadata updates after understanding the tradeoff. Do
not use it to skip normal working-copy synchronization before edits or publication.

## Agent Instruction

Use `--ignore-working-copy` only for lock-safe inspection or intended metadata work because it may
skip current file snapshots.

## Mechanisms

Supported by normal `jj status` first, targeted `--ignore-working-copy` use, lock diagnosis, and
follow-up status checks once the working copy is available.

## References

- [Principle: JJ Topology Is Repo Role
  Dependent](../../principles/jj-topology-is-repo-role-dependent.md)
- [Jujutsu docs: working copy](https://docs.jj-vcs.dev/latest/working-copy/)
- [Jujutsu docs: bookmarks](https://docs.jj-vcs.dev/latest/bookmarks/)
