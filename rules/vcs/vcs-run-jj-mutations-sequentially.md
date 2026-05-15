# VCS Run JJ Mutations Sequentially

## Metadata

- ID: `VCS-RUN-JJ-MUTATIONS-SEQUENTIALLY`
- Legacy ID: `R-0703`
- Status: `reviewed`
- Domain: `vcs`
- Depth: `compact`

## Rule

Run jj mutations sequentially.

## Why

Jj mutating commands update working-copy and operation state. Running them in parallel risks locks,
stale reads, and confusing operation order, especially when agents issue tool calls concurrently.

## Helps

- Keeps source-control state coherent and avoids avoidable lock contention.

## Limits

Read-only inspections can often run in parallel, but do not overlap commands that write jj state,
working copy, bookmarks, or config.

## Agent Instruction

Run jj mutations sequentially because jj mutating commands update working-copy and operation state.

## Mechanisms

Supported by serialized jj command execution, waiting for one mutation to finish, lock-error
inspection, and `jj op log` after unexpected state.

## References

- [Principle: Jj Topology Is Repo Role
  Dependent](../../principles/jj-topology-is-repo-role-dependent.md)
- [Jujutsu docs: working copy](https://docs.jj-vcs.dev/latest/working-copy/)
- [Jujutsu docs: bookmarks](https://docs.jj-vcs.dev/latest/bookmarks/)
