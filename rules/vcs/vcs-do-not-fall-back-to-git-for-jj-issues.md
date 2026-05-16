# VCS Do Not Fall Back To Git For JJ Issues

## Metadata

- ID: `VCS-DO-NOT-FALL-BACK-TO-GIT-FOR-JJ-ISSUES`
- Status: `reviewed`
- Domain: `vcs`
- Depth: `compact`

## Rule

Do not switch to Git because a jj command hits a transient lock or sandbox issue.

## Why

In a jj repo, Git does not represent the full working-copy and change graph semantics. Switching to
Git because of a jj lock, pager, or sandbox issue can bypass jj state and make recovery harder.

## Helps

- Keeps jj as the source of truth and avoids mixed-tool corruption or confusion.

## Limits

Use Git for transport-level operations that the workflow requires, such as GitHub interop, after jj
state is coherent. Do not use Git as a substitute for jj recovery.

## Agent Instruction

Stay in jj for transient jj lock or sandbox issues; Git does not represent the full jj change graph.

## Mechanisms

Supported by retrying after lock inspection, `jj op log`, `jj st`, `jj git` subcommands, and reading
jj help or config before switching tools.

## References

- [Principle: JJ Topology Is Repo Role
  Dependent](../../principles/jj-topology-is-repo-role-dependent.md)
- [Jujutsu docs: working copy](https://docs.jj-vcs.dev/latest/working-copy/)
- [Jujutsu docs: bookmarks](https://docs.jj-vcs.dev/latest/bookmarks/)
