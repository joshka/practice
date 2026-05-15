# VCS JJ As Source Of Truth

## Metadata

- ID: `VCS-JJ-AS-SOURCE-OF-TRUTH`
- Legacy ID: `R-0700`
- Status: `reviewed`
- Domain: `vcs`
- Depth: `compact`

## Rule

Use `jj` as the source of truth in `.jj` repositories.

## Why

A `.jj` repo has jj changes, operation log, working-copy state, and bookmarks layered over Git
storage. Normal local workflow should use jj so descriptions, stack shape, and recovery stay
coherent.

## Helps

- Prevents Git commands from bypassing jj semantics and confusing the change graph.

## Limits

Git can still be used for transport or host tooling when jj does not cover the operation, but return
to jj for local state and review shape.

## Agent Instruction

Use `jj` as the source of truth in `.jj` repositories because a `.jj` repo has jj changes, operation
log, working-copy state, and bookmarks layered over Git storage.

## Mechanisms

Supported by `jj status`, `jj diff`, `jj desc`, `jj new`, `jj git fetch`, and repo instructions that
translate Git-centric advice into jj operations.

## References

- [Principle: JJ Topology Is Repo Role
  Dependent](../../principles/jj-topology-is-repo-role-dependent.md)
- [Jujutsu docs: working copy](https://docs.jj-vcs.dev/latest/working-copy/)
- [Jujutsu docs: bookmarks](https://docs.jj-vcs.dev/latest/bookmarks/)
