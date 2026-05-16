# VCS Use Git Formatted Diffs For Agents

## Metadata

- ID: `VCS-USE-GIT-FORMATTED-DIFFS-FOR-AGENTS`
- Name: `Use Git-Formatted Diffs for Agents`
- Summary: Prefer `jj diff --git` when agents or patch-oriented tools need diff text.
  Git patch format preserves hunks and paths in a shape those consumers can parse reliably.
- Status: `reviewed`
- Domain: `vcs`
- Depth: `compact`
- Related: `shape-tool-output-for-agents, produce-review-packets, vcs-jj-as-source-of-truth`

## Rule

Prefer Git-formatted diffs when agents need to interpret patch text.

## Why

Many agents and review tools understand Git patch format better than native jj summaries. `jj diff
--git` preserves file paths, hunks, renames, and patch shape in a format that patch-oriented tooling
can parse reliably.

## Helps

- Makes diffs easier for agents and humans to inspect, quote, and apply.

## Limits

Use native jj summaries for graph and change-shape questions. Use Git-formatted diffs when the
consumer needs patch text.

## Agent Instruction

Use Git-formatted diffs for agents and review tools that understand patch format better than native
jj summaries.

## Mechanisms

Supported by `jj diff --git`, `jj show --git`, path-scoped diffs, and handoffs that include
important files rather than raw huge patches.

## References

- [Principle: JJ Topology Is Repo Role
  Dependent](../../principles/jj-topology-is-repo-role-dependent.md)
- [Jujutsu docs: working copy](https://docs.jj-vcs.dev/latest/working-copy/)
- [Jujutsu docs: bookmarks](https://docs.jj-vcs.dev/latest/bookmarks/)
