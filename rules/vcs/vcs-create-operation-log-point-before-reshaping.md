# VCS Create Operation Log Point Before Reshaping

## Metadata

- ID: `VCS-CREATE-OPERATION-LOG-POINT-BEFORE-RESHAPING`
- Name: `Create an Operation Log Point Before Reshaping`
- Summary: Create a recent jj operation boundary before risky stack reshaping.
  Recovery is easier when there is a known point before rebases, splits, squashes, or repairs.
- Status: `reviewed`
- Domain: `vcs`
- Depth: `compact`
- Related: `vcs-recover-with-operation-log, vcs-use-evolog-and-operation-log`

## Rule

Use harmless jj inspection to create an operation-log point before risky reshaping.

## Why

JJ can recover through the operation log, but recovery is easier when there is a recent known point
before a risky stack reshape. A harmless inspection or description update creates a visible
operation boundary before rebases, splits, squashes, or publication repair.

## Helps

- Makes recovery from a bad reshape faster and easier to explain.

## Limits

Do not add meaningless operations before every command. Use this before risky graph changes or when
the current state would be expensive to reconstruct.

## Agent Instruction

Before risky jj stack reshaping, run harmless inspection so there is a recent operation-log point
for recovery.

## Mechanisms

Supported by `jj status`, `jj log`, `jj op log`, `jj desc` for meaningful descriptions, and noting
the operation before reshaping.

## References

- [Principle: JJ Topology Is Repo Role
  Dependent](../../principles/jj-topology-is-repo-role-dependent.md)
- [Jujutsu docs: working copy](https://docs.jj-vcs.dev/latest/working-copy/)
- [Jujutsu docs: bookmarks](https://docs.jj-vcs.dev/latest/bookmarks/)
