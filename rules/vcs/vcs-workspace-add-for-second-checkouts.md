# VCS Workspace Add For Second Checkouts

## Metadata

- ID: `VCS-WORKSPACE-ADD-FOR-SECOND-CHECKOUTS`
- Legacy ID: `R-0702`
- Status: `reviewed`
- Domain: `vcs`
- Depth: `compact`

## Rule

Use `jj workspace add` only when a second filesystem checkout is needed.

## Why

`jj new` creates another change in the current checkout; `jj workspace add` creates another
filesystem checkout. Use the heavier workspace tool only when the task needs separate files on disk,
such as long-running tests, clean comparison, or different sparse state.

## Helps

- Avoids unnecessary checkout proliferation while preserving isolation when filesystem state
  matters.

## Limits

Use a second workspace for parallel long-running work or clean validation. Use `jj new` for ordinary
separate review lanes in the same checkout.

## Agent Instruction

Use `jj workspace add` only for a second filesystem checkout; use `jj new` for another change in the
same checkout.

## Mechanisms

Supported by `jj new`, `jj workspace add`, workspace cleanup notes, sparse pattern inspection, and
task ownership documentation.

## References

- [Principle: Jj Topology Is Repo Role
  Dependent](../../principles/jj-topology-is-repo-role-dependent.md)
- [Jujutsu docs: working copy](https://docs.jj-vcs.dev/latest/working-copy/)
- [Jujutsu docs: bookmarks](https://docs.jj-vcs.dev/latest/bookmarks/)
