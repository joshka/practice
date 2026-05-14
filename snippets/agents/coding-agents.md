# Coding Agent Workflow Instructions

Use this snippet when a repo wants agent work to be durable, reviewable, and easy to integrate.

```markdown
## Coding-Agent Workflow

Treat agents as workers producing reviewable artifacts, not as magic sessions. Define the objective,
boundaries, acceptance criteria, available tools, and expected proof before delegating or starting a
large edit.

Prefer repo-owned context, tools, checks, and workspaces over repeated prompt steering. Keep
long-running or parallel work isolated by task. Do not overwrite unrelated human or agent changes.

Handoff should include the purpose, changed files, validation, skipped checks, known risks, and any
follow-up. If repeated feedback exposes a missing rule, tool, test, or doc, turn that feedback into
durable guidance instead of relying on memory.

Canonical guide:

- `guides/coding-agents.md`
```
