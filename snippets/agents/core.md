# Core Agent Instructions

Use this snippet in `AGENTS.md` files when a repo needs the broad development-preference baseline.

```markdown
## Development Preferences

Use small, reviewable changes with one clear purpose. Preserve unrelated work and keep source
control state clean. Prefer existing project patterns over generic advice.

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
```
