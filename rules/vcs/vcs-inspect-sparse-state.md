# VCS Inspect Sparse State

## Metadata

- ID: `VCS-INSPECT-SPARSE-STATE`
- Legacy ID: `R-0724`
- Status: `reviewed`
- Domain: `vcs`
- Depth: `compact`

## Rule

Inspect sparse state before treating a missing path as missing history.

## Why

In sparse checkouts, a missing file may be outside the sparse patterns rather than deleted from
history. Treating it as absent can lead agents to recreate files, misread ownership, or make edits
in the wrong location.

## Helps

- Prevents false conclusions about repository contents in sparse workspaces.

## Limits

If the repo is not sparse, normal path and history inspection is enough. Check sparse state when
paths expected from docs, tests, or history are missing.

## Agent Instruction

Inspect sparse state before treating a missing path as missing history; sparse patterns can hide
files that still exist.

## Mechanisms

Supported by `jj sparse list`, workspace inspection, path search, adjusting sparse patterns
deliberately, and handoffs that note sparse limitations.

## References

- [Principle: Jj Topology Is Repo Role
  Dependent](../../principles/jj-topology-is-repo-role-dependent.md)
- [Jujutsu docs: working copy](https://docs.jj-vcs.dev/latest/working-copy/)
- [Jujutsu docs: bookmarks](https://docs.jj-vcs.dev/latest/bookmarks/)
