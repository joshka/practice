#!/usr/bin/env python3
"""Generate the downstream AGENTS.md adoption template."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from textwrap import wrap

sys.dont_write_bytecode = True

from generate_agent_rules import RULES_DIR, discover_rules, domain_name


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TEMPLATE_DIR = ROOT / "templates" / "downstream"
AGENT_RULE_PACK = ROOT / "snippets" / "agents" / "rules.md"
CANONICAL_SITE = "https://www.joshka.net/practice/"


def render_agents() -> str:
    return """# Agent Guidance

Use this file as the repo-local map. Keep the reviewed shared rule pack in
`docs/development/` so every rule is available without making this file a long manual.

The copied development guidance comes from the `development-preferences` repo. The public reference
site is [Software Practices](https://www.joshka.net/practice/). Use the local compact rules first,
and use the site when a rule, pattern, principle, or guide needs more context.

## Local Rules

- Follow local code, tests, docs, and existing conventions before general preferences.
- Preserve unowned human or agent work.
- Keep changes small, atomic, and reviewable.
- Report validation evidence in handoffs instead of confidence language.
- Use the validation commands listed below before handoff.
- Read `docs/development/snippets/agents/rules.md` for the single-file reviewed rule pack.
- Read `docs/development/rules/README.md` when a task needs only one rule domain.
- Preserve and prioritize repo-specific instructions in this file. Merge shared guidance into the
  local agent map; do not replace local project rules with the template blindly.
- Refresh copied guidance with `python3 docs/development/update.py` when the shared rule set
  changes.
- If a shared rule causes trouble or should be changed for most projects, open a
  [guidance feedback issue][guidance-feedback].

## Validation

Replace these examples with the repo's real checks:

```bash
cargo fmt --check
cargo test
markdownlint-cli2 "**/*.md"
```

## Deeper Guidance

- `docs/development/snippets/agents/rules.md`: generated single-file reviewed rule pack.
- `docs/development/rules/README.md`: generated index for reviewed rule domains.
- `docs/development/bootstrap-downstream.md`: instructions for refreshing and merging this guidance
  into a downstream repo.
- `docs/development/README.md`: local map for development guidance.
- [Software Practices](https://www.joshka.net/practice/): canonical rendered reference for guides,
  rules, patterns, principles, mechanisms, and tags.

[guidance-feedback]: https://github.com/joshka/practice/issues/new?template=guidance-feedback.yml
"""


def render_readme() -> str:
    return """# Development Guidance

This directory carries repo-local development guidance for agents and maintainers.

The generated rule files are copied from the `development-preferences` repo. The canonical rendered
reference is [Software Practices](https://www.joshka.net/practice/). Update local validation
commands and repo-specific notes in the repo's `AGENTS.md`, but refresh copied shared guidance from
upstream instead of editing it by hand.

From a downstream repo that does not yet have this directory, install the copied guidance with:

```bash
temp_dir="$(mktemp -d)"
git -c commit.gpgsign=false clone --depth 1 https://github.com/joshka/practice.git \\
  "$temp_dir/practice"
python3 "$temp_dir/practice/scripts/generate_downstream_template.py" \\
  --output "$PWD" \\
  --preserve-agents
```

From this downstream repo, refresh this copy from GitHub with:

```bash
python3 docs/development/update.py
```

Set `DEVELOPMENT_PREFERENCES_DIR=/path/to/development-preferences` only when testing against a
local source checkout.

## Files

- `bootstrap-downstream.md`: instructions for an agent bootstrapping this guidance into a repo.
- `snippets/agents/rules.md`: generated single-file reviewed-rule pack.
- `rules/README.md`: generated index for the full compressed reviewed-rule pack.
- `rules/*.md`: generated domain files containing every reviewed rule.
- `update.py`: helper that refreshes this directory from the canonical source repository.

## Adoption Notes

Keep `AGENTS.md` short enough to scan. Put the full rule pack in generated domain files so agents
can load only the domains relevant to the task, while still ensuring every reviewed rule is
represented downstream.

This template intentionally copies compact agent-facing guidance rather than every source guide,
pattern, principle, and mechanism. When a compact rule needs more context, use the public reference
site or the canonical source repo.

Update local validation commands, source-control notes, and project-specific boundaries in
`AGENTS.md` or nearby local docs. If a generated rule is wrong for most projects, open a
[guidance feedback issue][guidance-feedback], update the canonical `development-preferences` repo,
and recopy the generated files.

[guidance-feedback]: https://github.com/joshka/practice/issues/new?template=guidance-feedback.yml
"""


def render_bootstrap_doc() -> str:
    return """# Bootstrap Downstream Guidance

Use this document when an agent is asked to bring shared development guidance into a downstream
repository.

The goal is a useful local agent map, not a verbatim replacement of the downstream repo's existing
instructions. Preserve local project rules, validation commands, architecture notes, and workflow
constraints. Add links to the copied shared guidance so future agents can load more context when a
task needs it.

## Source

- Canonical source repository: `https://github.com/joshka/practice`
- Canonical rendered reference: [Software Practices](https://www.joshka.net/practice/)
- Local copied guidance root: `docs/development/`

## Bootstrap Steps

1. Inspect the downstream repo's existing `AGENTS.md` and nearby project docs.
1. Install the copied shared guidance from a temporary clone when this repo does not yet have
   `docs/development/update.py`:

   ```bash
   temp_dir="$(mktemp -d)"
   git -c commit.gpgsign=false clone --depth 1 https://github.com/joshka/practice.git \\
     "$temp_dir/practice"
   python3 "$temp_dir/practice/scripts/generate_downstream_template.py" \\
     --output "$PWD" \\
     --preserve-agents
   ```

1. Refresh an existing copied guidance directory with:

   ```bash
   python3 docs/development/update.py
   ```

1. Merge the shared guidance into the downstream `AGENTS.md` instead of replacing local content.
1. Keep `AGENTS.md` short. It should route agents to deeper files rather than becoming the full
   rule book.
1. Add or keep local validation commands, source-control rules, ownership boundaries, and project
   conventions.
1. Run the downstream repo's normal formatting, linting, and test checks.
1. Report what changed, what was preserved, and what validation ran.

## Prompt For Another Agent

Use this prompt when asking a fresh Codex session to bootstrap another repo:

```text
Bootstrap this repo with the shared development guidance from
https://github.com/joshka/practice.

Use the downstream bootstrap template in that repo. Preserve this repo's existing AGENTS.md
instructions, validation commands, source-control rules, and project-specific conventions. Merge the
shared guidance into AGENTS.md instead of replacing local rules.

Install or refresh:

- docs/development/bootstrap-downstream.md
- docs/development/README.md
- docs/development/update.py
- docs/development/snippets/agents/rules.md
- docs/development/rules/*.md

Add a short "Shared Development Preferences" section to AGENTS.md that points agents to the copied
docs/development files and to https://www.joshka.net/practice/ for deeper context.

If a shared rule causes friction or seems wrong for most Rust or agent work, open a guidance
feedback issue upstream rather than only patching around it locally:
https://github.com/joshka/practice/issues/new?template=guidance-feedback.yml

Keep the change small and report exactly what was copied, what local instructions were preserved,
and what validation ran or was skipped.
```

## Recommended `AGENTS.md` Entry

Adapt this section to the downstream repo's voice:

```markdown
## Shared Development Preferences

This repo carries a local copy of shared development guidance in `docs/development/`.
Use this repo's local rules first. When local guidance is silent, use the shared guidance as a
fallback.

Entry points:

- `docs/development/snippets/agents/rules.md`: compact reviewed rule pack.
- `docs/development/rules/README.md`: rule domains for targeted loading.
- `docs/development/bootstrap-downstream.md`: how to refresh and merge the guidance.
- https://www.joshka.net/practice/: rendered reference with deeper guide, rule, pattern, principle,
  mechanism, and tag context.

If a shared rule causes friction or seems wrong for most Rust or agent work, open a guidance
feedback issue instead of only patching around it locally:
https://github.com/joshka/practice/issues/new?template=guidance-feedback.yml
```

## Merge Guidance

Prefer local specificity over shared defaults. For example, keep project-specific validation such as
`just check`, `cargo +nightly fmt --all`, fixture-update commands, or release gates.

Prefer shared guidance for general agent behavior, review handoffs, jj workflow, Rust
maintainability, documentation shape, and source-control hygiene when the downstream repo does not
already have a stronger local rule.

Do not copy every source guide into `AGENTS.md`. Link to the local compact rules and the public site
for deeper context.
"""


def render_update_script() -> str:
    return '''#!/usr/bin/env python3
"""Refresh copied development guidance from the canonical source repository."""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


SOURCE_REPO = "https://github.com/joshka/practice.git"


def explicit_source() -> Path | None:
    configured = os.environ.get("DEVELOPMENT_PREFERENCES_DIR")
    if not configured:
        return None
    source = Path(configured).expanduser().resolve()
    generator = source / "scripts" / "generate_downstream_template.py"
    if not generator.exists():
        raise SystemExit(
            f"DEVELOPMENT_PREFERENCES_DIR does not contain {generator.relative_to(source)}"
        )
    return source


def clone_source() -> tuple[tempfile.TemporaryDirectory[str], Path]:
    if shutil.which("git") is None:
        raise SystemExit(
            "git is required to refresh guidance from GitHub. Install git or set "
            "DEVELOPMENT_PREFERENCES_DIR to a local checkout."
        )

    temp = tempfile.TemporaryDirectory(prefix="development-preferences-")
    source = Path(temp.name) / "practice"
    subprocess.run(
        ["git", "-c", "commit.gpgsign=false", "clone", "--depth", "1", SOURCE_REPO, str(source)],
        check=True,
    )
    return temp, source


def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    temp: tempfile.TemporaryDirectory[str] | None = None
    source = explicit_source()
    if source is None:
        temp, source = clone_source()

    try:
        generator = source / "scripts" / "generate_downstream_template.py"
        subprocess.run(
            [sys.executable, str(generator), "--output", str(repo_root), "--preserve-agents"],
            check=True,
        )
    finally:
        if temp is not None:
            temp.cleanup()

    print(f"Refreshed development guidance from {source}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''


def wrap_bullet(text: str) -> list[str]:
    return wrap(
        text,
        width=100,
        initial_indent="- ",
        subsequent_indent="  ",
        break_long_words=False,
        break_on_hyphens=False,
    )


def rules_by_domain() -> dict[str, list]:
    domains: dict[str, list] = {}
    for rule in discover_rules():
        if rule.status != "reviewed":
            continue
        domains.setdefault(rule.domain, []).append(rule)
    for domain_rules in domains.values():
        domain_rules.sort(key=lambda rule: rule.id)
    return dict(sorted(domains.items()))


def render_domain_index(domains: dict[str, list]) -> str:
    lines = [
        "# Reviewed Rule Domains",
        "",
        "These generated files contain every reviewed rule from the `development-preferences` repo,",
        "which is the canonical source for this shared rule set. Keep them synchronized from that",
        "repo instead of editing copied rule text by hand.",
        "",
        "Use the domain file that matches the current task. Load more than one domain when work crosses",
        "boundaries such as Rust API changes, tests, docs, performance, and source control.",
        "",
        "## Domains",
        "",
    ]
    for domain, rules in domains.items():
        title = domain_name(RULES_DIR / domain)
        lines.append(f"- [{title}]({domain}.md): {len(rules)} rules.")
    lines.append("")
    return "\n".join(lines)


def render_domain_rules(domain: str, rules: list) -> str:
    title = domain_name(RULES_DIR / domain)
    lines = [
        f"# {title}",
        "",
        "Generated from the canonical `development-preferences` rule catalog. Do not edit copied rule",
        "text by hand; update the source repo and recopy this file.",
        "",
        "## Instructions",
        "",
    ]
    for rule in rules:
        lines.extend(wrap_bullet(f"`{rule.id}`: {rule.instruction}"))
    lines.append("")
    return "\n".join(lines)


def outputs(template_dir: Path) -> dict[Path, str]:
    agents = template_dir / "AGENTS.md"
    bootstrap = template_dir / "docs" / "development" / "bootstrap-downstream.md"
    readme = template_dir / "docs" / "development" / "README.md"
    update_script = template_dir / "docs" / "development" / "update.py"
    snippets = template_dir / "docs" / "development" / "snippets" / "agents"
    rules = template_dir / "docs" / "development" / "rules"
    domains = rules_by_domain()
    rendered = {
        agents: render_agents(),
        bootstrap: render_bootstrap_doc(),
        readme: render_readme(),
        update_script: render_update_script(),
        snippets / "rules.md": AGENT_RULE_PACK.read_text(),
        rules / "README.md": render_domain_index(domains),
    }
    for domain, domain_rules in domains.items():
        rendered[rules / f"{domain}.md"] = render_domain_rules(domain, domain_rules)
    return rendered


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail if templates/downstream is not up to date",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_TEMPLATE_DIR,
        help=(
            "directory to write the downstream template into; use a target repo root to copy "
            "AGENTS.md and docs/development/rules there"
        ),
    )
    parser.add_argument(
        "--preserve-agents",
        action="store_true",
        help="do not overwrite an existing AGENTS.md in the output directory",
    )
    args = parser.parse_args()

    template_dir = args.output if args.output.is_absolute() else ROOT / args.output
    rendered = outputs(template_dir)
    agents_path = template_dir / "AGENTS.md"
    if args.preserve_agents and agents_path.exists():
        rendered.pop(agents_path, None)
    if args.check:
        stale = [
            path.relative_to(ROOT).as_posix()
            for path, content in rendered.items()
            if not path.exists() or path.read_text() != content
        ]
        if stale:
            for path in stale:
                print(f"{path} is out of date", file=sys.stderr)
            return 1
        return 0

    for path, content in rendered.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)

    old_single_file = template_dir / "docs" / "development" / "agent-rules.md"
    if old_single_file.exists():
        old_single_file.unlink()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
