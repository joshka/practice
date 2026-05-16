# Jujutsu Agent Instructions

## Metadata

- Name: `Jujutsu Agent Instructions`
- ID: `agent-jj-instructions`
- Summary: `Compact source-control instructions for coding agents working in repositories that use
  jujutsu. The snippet covers fresh changes, descriptions, non-interactive commands, recovery,
  remote handoff, and publication approval.`
- Status: `reviewed`
- Audience: `agents`
- Topics: `jujutsu, source-control, agent-workflow, publication`
- Tags: `agents, snippets, jj, vcs`
- Related: `guides/jj-workflow.md, principles/jj-topology-is-repo-role-dependent.md`

Use this snippet in repositories that use jujutsu for local source-control workflow.

```markdown
## Jujutsu Workflow

Use `jj` for local version-control operations. In repos with `.jj/`, do not use Git for normal local
workflow. Use Git only for transport-level operations that the current jj workflow does not cover.

Start separable work in a fresh change with `jj --no-pager new`, then set a clear description early
with `jj --no-pager desc --message "..."`. Keep changes small, atomic, and self-contained.

Use `jj new` when the task only needs another review lane in the same checkout. Use
`jj workspace add` only when the task needs another filesystem checkout, such as long-running
validation, a clean comparison tree, or a separate sparse view.

Use `--no-pager` on jj commands. Prefer `jj --no-pager diff --git` when an agent or reviewer needs
to interpret a diff. Avoid interactive-by-default commands unless you know how to supply the needed
message, paths, or tool choice non-interactively.

Do not rely on default revision selection for mutating commands when the target matters. Spell out
the intended revision, destination, fileset, bookmark, or remote. If repeated commands are not adding
information, stop and inspect graph, operation, workspace, bookmark, or help output before mutating
again.

For GitHub handoff, inspect jj bookmark and remote state first, publish only the intended bookmark,
then pass explicit `gh --repo`, `--head`, and `--base` values when inference is risky.
Before publishing or repairing remote state, identify whether the repo is owned, maintainer-access,
or fork-based contributor work. Align fetch remote, push remote, tracked bookmark, PR base/head, and
`trunk()` with that role. Ask before changing repo or user jj aliases unless the user explicitly
requested the repair and the target is unambiguous.

Do not run destructive commands, rewrite unrelated work, or publish without explicit approval.
Recover through `jj undo`, `jj op log`, `jj op restore`, or `jj evolog` instead of Git reset or
stash habits.

Canonical guide:

- `guides/jj-workflow.md`
- `principles/jj-topology-is-repo-role-dependent.md`
```
