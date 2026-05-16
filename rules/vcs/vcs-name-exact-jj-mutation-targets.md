# VCS Name Exact JJ Mutation Targets

## Metadata

- ID: `VCS-NAME-EXACT-JJ-MUTATION-TARGETS`
- Name: `Name Exact JJ Mutation Targets`
- Summary: Specify revisions, filesets, bookmarks, and destinations for mutating jj commands.
  Explicit targets make intent reviewable and prevent defaults from acting on surprising state.
- Status: `reviewed`
- Domain: `vcs`
- Depth: `compact`

## Rule

Name exact targets for mutating jj commands.

## Why

Mutating commands that rely on defaults can target the wrong revision, fileset, bookmark, or
destination when the stack is not what the agent assumes. Naming targets turns hidden selection into
reviewable intent.

## Helps

- Reduces accidental rewrites and makes command effects easier to audit.

## Limits

Defaults are fine for harmless inspection or when the command target is unambiguous and local. Be
explicit when state changes.

## Agent Instruction

Name exact revisions, filesets, bookmarks, and destinations for mutating jj commands instead of
relying on stack-sensitive defaults.

## Mechanisms

Supported by explicit revsets, pathspecs, destination flags, bookmark names, remote names, and
pre-command `jj log` or `jj status` inspection.

## References

- [Principle: JJ Topology Is Repo Role
  Dependent](../../principles/jj-topology-is-repo-role-dependent.md)
- [Jujutsu docs: working copy](https://docs.jj-vcs.dev/latest/working-copy/)
- [Jujutsu docs: bookmarks](https://docs.jj-vcs.dev/latest/bookmarks/)
