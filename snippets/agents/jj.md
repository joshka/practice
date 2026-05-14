# Jujutsu Agent Instructions

Use this snippet in repositories that use jujutsu for local source-control workflow.

```markdown
## Jujutsu Workflow

Use `jj` for local version-control operations. In repos with `.jj/`, do not use Git for normal local
workflow. Use Git only for transport-level operations that the current jj workflow does not cover.

Start separable work in a fresh change with `jj --no-pager new`, then set a clear description early
with `jj --no-pager desc --message "..."`. Keep changes small, atomic, and self-contained.

Use `--no-pager` on jj commands. Prefer `jj --no-pager diff --git` when an agent or reviewer needs
to interpret a diff. Avoid interactive-by-default commands unless you know how to supply the needed
message, paths, or tool choice non-interactively.

Do not run destructive commands, rewrite unrelated work, or publish without explicit approval.

Canonical guide:

- `guides/jj-workflow.md`
```
