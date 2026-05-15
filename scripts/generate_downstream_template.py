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


def render_agents() -> str:
    return """# Agent Guidance

Use this file as the repo-local map. Keep the full reviewed rule pack in
`docs/development/rules/` so every rule is available without making this file a long manual.

The copied rule files come from the `development-preferences` repo, which is the canonical source
for these rules. Refresh those files from that repo when the shared rule set changes.

## Local Rules

- Follow local code, tests, docs, and existing conventions before general preferences.
- Preserve unowned human or agent work.
- Keep changes small, atomic, and reviewable.
- Report validation evidence in handoffs instead of confidence language.
- Use the validation commands listed below before handoff.
- Read `docs/development/rules/README.md` for the full reviewed development rule pack.

## Validation

Replace these examples with the repo's real checks:

```bash
cargo fmt --check
cargo test
markdownlint-cli2 "**/*.md"
```

## Deeper Guidance

- `docs/development/rules/README.md`: generated index for all reviewed rule domains.
- `docs/development/README.md`: local map for development guidance.
"""


def render_readme() -> str:
    return """# Development Guidance

This directory carries repo-local development guidance for agents and maintainers.

The generated rule files are copied from the `development-preferences` repo, which is the canonical
source for these shared rules. Update local validation commands and repo-specific notes here, but
refresh copied rule text from upstream instead of editing it by hand.

From the canonical repo, refresh this downstream copy with:

```bash
python3 scripts/generate_downstream_template.py --output /path/to/this-repo
```

## Files

- `rules/README.md`: generated index for the full compressed reviewed-rule pack.
- `rules/*.md`: generated domain files containing every reviewed rule.

## Adoption Notes

Keep `AGENTS.md` short enough to scan. Put the full rule pack in generated domain files so agents
can load only the domains relevant to the task, while still ensuring every reviewed rule is
represented downstream.

Update local validation commands, source-control notes, and project-specific boundaries in
`AGENTS.md` or nearby local docs. If a generated rule is wrong, update the canonical
`development-preferences` repo and recopy the generated files.
"""


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
    readme = template_dir / "docs" / "development" / "README.md"
    rules = template_dir / "docs" / "development" / "rules"
    domains = rules_by_domain()
    rendered = {
        agents: render_agents(),
        readme: render_readme(),
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
    args = parser.parse_args()

    template_dir = args.output if args.output.is_absolute() else ROOT / args.output
    rendered = outputs(template_dir)
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
