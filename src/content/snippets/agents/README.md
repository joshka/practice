# Agent Snippets

These snippets are copyable `AGENTS.md` sections. They provide compact instructions and point back
to the canonical guides for detail.

Use snippets as a starting point, then adapt paths and commands to the target repository. Do not
copy every snippet by default; choose the sections that match the repo's work.

## Snippets

- [core.md](core.md): A repo needs the broad development-preference baseline.
- [full-software-doctrine.md](full-software-doctrine.md): A repo wants one large pasteable
  doctrine with rules and reasons.
- [rust.md](rust.md): Rust code, APIs, Rustdoc, or dependency shape matters.
- [markdown-docs.md](markdown-docs.md): Agents edit Markdown, Rustdoc, READMEs, or review notes.
- [coding-agents.md](coding-agents.md): The repo delegates work to coding agents.
- [jj.md](jj.md): The repo uses jujutsu for local version-control workflow.
- [rules.md](rules.md): Reviewed compact rule instructions with per-rule traceability.

## Adaptation Checklist

- Use `templates/downstream/` when the downstream repo should carry every reviewed rule.
- Keep only snippets that apply to the repo when copying small profile snippets directly.
- Use `full-software-doctrine.md` when one coherent pasteable prompt is more important than token
  efficiency or modular loading.
- Rewrite guide paths when the target repo stores guidance elsewhere.
- Replace validation commands with the repo's actual commands.
- Keep source-control instructions aligned with the repo's real workflow.
- Prefer short `AGENTS.md` files that point to deeper guides.

For broad adoption, prefer the downstream template over copying `rules.md` by hand:

```bash
python3 scripts/generate_downstream_template.py --output /path/to/target-repo
```

The template keeps `AGENTS.md` short and splits the full reviewed rule pack into generated domain
files under `docs/development/rules/`, so agents can load the relevant rule domains without losing
coverage. Treat this repo as the canonical source for the copied rule text; refresh downstream repos
from here when the shared rules change.
