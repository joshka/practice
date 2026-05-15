# Agent Snippets

These snippets are copyable `AGENTS.md` sections. They provide compact instructions and point back
to the canonical guides for detail.

Use snippets as a starting point, then adapt paths and commands to the target repository. Do not
copy every snippet by default; choose the sections that match the repo's work.

## Snippets

| Snippet                              | Use When                                                       |
| ------------------------------------ | -------------------------------------------------------------- |
| [core.md](core.md)                   | A repo needs the broad development-preference baseline.        |
| [rust.md](rust.md)                   | Rust code, APIs, Rustdoc, or dependency shape matters.         |
| [markdown-docs.md](markdown-docs.md) | Agents edit Markdown, Rustdoc, READMEs, or review notes.       |
| [coding-agents.md](coding-agents.md) | The repo delegates work to coding agents.                      |
| [jj.md](jj.md)                       | The repo uses jujutsu for local version-control workflow.      |
| [rules.md](rules.md)                 | Reviewed compact rule instructions with per-rule traceability. |

## Adaptation Checklist

- Keep only snippets that apply to the repo.
- Rewrite guide paths when the target repo stores guidance elsewhere.
- Replace validation commands with the repo's actual commands.
- Keep source-control instructions aligned with the repo's real workflow.
- Prefer short `AGENTS.md` files that point to deeper guides.
