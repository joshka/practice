# VCS Use Evolog And Operation Log

## Metadata

- ID: `VCS-USE-EVOLOG-AND-OPERATION-LOG`
- Name: `Use Evolog and Operation Log`
- Summary: Use `jj evolog` for a change's evolution and `jj op log` for repository operations.
  Picking the right log distinguishes rewrite history from workspace, bookmark, and import events.
- Status: `reviewed`
- Domain: `vcs`
- Depth: `compact`

## Rule

Use `jj evolog` for one change's evolution and `jj op log` for repository operations.

## Why

`jj evolog` answers how one change evolved; `jj op log` answers how the repository state changed.
Using the wrong log can hide whether a problem came from a change rewrite, workspace operation,
bookmark update, or remote import.

## Helps

- Makes diagnosis faster by choosing the log that matches the question.

## Limits

Use normal `jj log` when current stack shape is enough. Reach for evolog or op log when history was
rewritten or recovery is needed.

## Agent Instruction

Use `jj evolog` for one change's evolution and `jj op log` for repository operations because `jj
evolog` answers how one change evolved; `jj op log` answers how the repository state changed.

## Mechanisms

Supported by `jj evolog -r <change>`, `jj op log`, `jj op show`, and recovery notes that name which
history was inspected.

## References

- [Principle: JJ Topology Is Repo Role
  Dependent](../../principles/jj-topology-is-repo-role-dependent.md)
- [Jujutsu docs: working copy](https://docs.jj-vcs.dev/latest/working-copy/)
- [Jujutsu docs: bookmarks](https://docs.jj-vcs.dev/latest/bookmarks/)
