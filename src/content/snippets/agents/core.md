# Core Agent Instructions

## Metadata

- Name: `Core Agent Instructions`
- ID: `agent-core-instructions`
- Summary: `Broad baseline instructions for coding agents working in repositories that adopt these
  development preferences. The snippet keeps AGENTS.md short while routing agents to canonical
  guides, principles, mechanisms, and the reviewed rule pack.`
- Status: `reviewed`
- Audience: `agents`
- Topics: `agent-workflow, development-preferences, handoff, validation`
- Tags: `agent-workflow, agent-context, review-handoff, verification`
- Related: `guides/software-change-preferences.md, guides/coding-agents.md, snippets/agents/rules.md`

Use this snippet in `AGENTS.md` files when a repo needs the broad development-preference baseline.

```markdown
## Development Preferences

Use small, reviewable changes with one clear purpose. Preserve unrelated work and keep source
control state clean. Prefer existing project patterns over generic advice.

Keep `AGENTS.md` as a task-start map, not as the full software doctrine. If the repo has a project
operating manual or equivalent project-owned guidance artifact, read that before substantial work.

Before editing, identify the relevant guide or local convention. During handoff, describe what
changed, why it changed, and what validation ran. Report skipped checks and remaining risk
honestly.

Treat private session context as private. Shared issues, PRs, commits, docs, and review packets
must restate the problem, rationale, choices made, evidence, validation, and remaining risk for
readers who did not see the agent session.

After a validated chunk, offer concrete next options. When continuing is the normal path, make the
first option `I've reviewed, do the next thing`, name that next thing, and handle the workflow work
behind it: mark reviewed material, update the jj description, create a fresh jj change when needed,
and begin the named next chunk.

Prefer the project guides as the source of truth:

- Project operating manual or applied local doctrine: `docs/development/project-operating-manual.md`
- Software change shape: `guides/software-change-preferences.md`
- Rust maintainability: `guides/rust-maintainability.md`
- Code shape: `guides/code-shape.md`
- Boundary correctness: `guides/boundary-correctness.md`
- Observability and failure: `guides/observability-and-failure.md`
- Markdown and documentation: `guides/markdown-documentation.md`
- Documentation workflow: `guides/documentation-workflow.md`
- Coding agents: `guides/coding-agents.md`
- Jujutsu workflow: `guides/jj-workflow.md`
- Principles and reasoning notes: `principles/README.md`
- Tooling mechanisms: `mechanisms/README.md`

For compact execution rules, use the reviewed rule pack:

- Reviewed rules: `snippets/agents/rules.md`
```
