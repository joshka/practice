#!/usr/bin/env python3
"""Generate readable rule indexes from per-rule files."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from textwrap import wrap


ROOT = Path(__file__).resolve().parents[1]
RULES_DIR = ROOT / "rules"

DOMAIN_SUMMARIES = {
    "agent-workflow": (
        "Agent workflow rules cover objectives, scoped capabilities, durable context, review "
        "packets, security proof, feedback loops, and concrete next choices."
    ),
    "boundary": (
        "Boundary rules cover parsing, validation policy, explicit inputs, state transitions, "
        "provider diagnostics, effect boundaries, and external reconciliation."
    ),
    "change-shape": (
        "Change-shape rules cover one-purpose changes, small follow-ups, generated artifacts, "
        "dependency churn, ownership, and structure-versus-behavior review boundaries."
    ),
    "documentation": (
        "Documentation rules cover docs-as-contracts, rendered docs, examples, reviewability, "
        "source links, concrete prose, and drift checks."
    ),
    "observability": (
        "Observability rules cover owned logging boundaries, durable failure visibility, "
        "diagnostic context, failure states, and safe telemetry retention."
    ),
    "performance": (
        "Performance rules cover measuring before optimizing, benchmark provenance, single-run "
        "skepticism, correctness gates, and the cost of complexity or dependency churn."
    ),
    "refactoring": (
        "Refactoring rules cover local reasoning, concept helpers, visible linear stories, "
        "side-effect loops, whitespace paragraphs, DRY pressure, and weak abstractions."
    ),
    "review": (
        "Review artifact rules cover issue slices, PR narratives, ADRs, speculation labels, "
        "thread ownership, and artifacts that stand alone without private session context."
    ),
    "rust": (
        "Rust rules cover public API shape, crate layout, dependency policy, docs.rs behavior, "
        "feature flags, public errors, unsafe boundaries, and release checks."
    ),
    "source": (
        "Source hygiene rules cover turning mined lessons into public guidance, preferring stable "
        "sources, and keeping local or private context out of shared artifacts."
    ),
    "test-failures": (
        "Test-failure rules cover assertion shape and failure output that help humans and agents "
        "diagnose the failing case quickly."
    ),
    "testing": (
        "Testing rules cover risk-based validation, doctests, feature matrices, deterministic "
        "tests, parser samples, command construction, dependency floors, and regressions."
    ),
    "vcs": (
        "VCS rules cover jj-first source-control work, remote topology, operation-log recovery, "
        "workspaces, publication safety, and file-tracking decisions."
    ),
}


@dataclass(frozen=True)
class Rule:
    id: str
    status: str
    domain: str
    title: str
    why: str
    helps: str
    path: Path


def metadata(text: str, name: str) -> str:
    match = re.search(rf"^- {re.escape(name)}: `([^`]+)`$", text, re.MULTILINE)
    return match.group(1) if match else ""


def section(text: str, name: str) -> str:
    match = re.search(
        rf"^## {re.escape(name)}\n\n(.*?)(?=\n\n## |\Z)",
        text,
        re.MULTILINE | re.DOTALL,
    )
    if not match:
        return ""
    return " ".join(match.group(1).split())


def first_sentence(text: str) -> str:
    match = re.search(r"(.+?[.!?])(?:\s+(?=[A-Z`])|$)", text)
    return (match.group(1) if match else text).strip()


def domain_name(domain_dir: Path) -> str:
    readme = domain_dir / "README.md"
    if readme.exists():
        first_line = readme.read_text().splitlines()[0]
        if first_line.startswith("# "):
            return first_line[2:]
    return domain_dir.name.replace("-", " ").title()


def discover_rules() -> list[Rule]:
    rules: list[Rule] = []
    for path in sorted(RULES_DIR.glob("*/*.md")):
        if path.name == "README.md":
            continue
        text = path.read_text()
        rule = Rule(
            id=metadata(text, "ID"),
            status=metadata(text, "Status"),
            domain=metadata(text, "Domain"),
            title=section(text, "Rule"),
            why=first_sentence(section(text, "Why")),
            helps=section(text, "Helps").lstrip("- "),
            path=path,
        )
        missing = [
            name
            for name, value in [
                ("ID", rule.id),
                ("Status", rule.status),
                ("Domain", rule.domain),
                ("Rule", rule.title),
                ("Why", rule.why),
            ]
            if not value
        ]
        if missing:
            joined = ", ".join(missing)
            raise SystemExit(f"{path.relative_to(ROOT)} is missing {joined}")
        rules.append(rule)
    return rules


def wrap_bullet(link: str, summary: str) -> list[str]:
    text = f"{link}. {summary}"
    return wrap(
        text,
        width=100,
        initial_indent="- ",
        subsequent_indent="  ",
        break_long_words=False,
        break_on_hyphens=False,
    )


def summary(rule: Rule) -> str:
    if rule.helps:
        return f"{rule.title} {rule.why} Helps: {rule.helps}"
    return f"{rule.title} {rule.why}"


def render_domain(domain: str, rules: list[Rule]) -> str:
    domain_dir = RULES_DIR / domain
    title = domain_name(domain_dir)
    intro = DOMAIN_SUMMARIES.get(domain, f"Rules in this group cover {title.lower()}.")
    lines = [
        f"# {title}",
        "",
        *wrap(
            intro,
            width=100,
            break_long_words=False,
            break_on_hyphens=False,
        ),
        "",
        "Use this index to scan the domain and jump to the rule files. The one-line summaries are",
        "for orientation; the rule files hold the rationale, limits, mechanisms, and references.",
        "",
        "## Rules",
        "",
    ]
    for rule in sorted(rules, key=lambda item: item.id):
        target = rule.path.name
        lines.extend(wrap_bullet(f"[`{rule.id}`]({target})", summary(rule)))
    return "\n".join(lines) + "\n"


def render_root(rules: list[Rule]) -> str:
    by_domain: dict[str, list[Rule]] = {}
    for rule in rules:
        by_domain.setdefault(rule.domain, []).append(rule)

    lines = [
        "# Rules",
        "",
        "Rules are compact instructions supported by the guides, principles, patterns, and",
        "mechanisms in this repo. Each rule has its own file so it can be reviewed, deepened, linked,",
        "and extracted into compressed agent instructions independently.",
        "",
        "## Rule File Shape",
        "",
        "Each rule file should keep these sections:",
        "",
        "- `Metadata`: stable ID, legacy ID, status, domain, and depth.",
        "- `Rule`: the direct human-readable instruction.",
        "- `Why`: rationale when the rule needs justification or tradeoff framing.",
        "- `Helps`: concrete development outcomes the rule improves.",
        "- `Limits`: exceptions, costs, or counter-signals.",
        "- `Agent Instruction`: compressed wording suitable for agent execution packs.",
        "- `Mechanisms`: lints, formatters, CI checks, commands, or workflows that support the rule.",
        "- `References`: durable sources that support, adapt, or contrast the rule in a useful way.",
        "",
        "Rules can stay compact when the rationale is obvious, but compact should still mean finished.",
        "A rule should explain the failure mode, tradeoff, or design pressure well enough that a",
        "reviewer does not need the original source material to understand why it exists. Prefer",
        "concrete surfaces and examples over abstract categories when the reader would otherwise have",
        "to infer applicability.",
        "",
        "Agent instructions are not repeated titles. They should encode the trigger, failure mode, or",
        "useful constraint that helps an agent apply the rule without blindly doing the literal",
        "shortest version of the instruction.",
        "",
        "## Naming",
        "",
        "Use uppercase, dash-separated IDs:",
        "",
        "```text",
        "DOCS-TREAT-DOCS-AS-CONTRACTS",
        "RUST-KEEP-PUBLIC-API-SHAPE-INTENTIONAL",
        "VCS-JJ-AS-SOURCE-OF-TRUTH",
        "TEST-OPTIMIZE-FAILURE-OUTPUT",
        "OBSERVABILITY-PRESERVE-OPERATION-CONTEXT-IN-ERRORS",
        "```",
        "",
        "Do not abbreviate broad family names in public rule IDs. Use `OBSERVABILITY`, not `OBS`.",
        "",
        "Rule IDs are handles, not compressed titles. A good ID is short enough to cite in reviews,",
        "preserves the rule's real concept, and keeps connector words when dropping them would change",
        "the meaning. Prefer a verb-oriented handle when the rule is an action, and use domain nouns",
        "plus a decisive verb and object. Write titles as direct instructions when possible.",
        "",
        "## Domains",
        "",
    ]

    for domain in sorted(by_domain):
        title = domain_name(RULES_DIR / domain)
        count = len(by_domain[domain])
        intro = DOMAIN_SUMMARIES.get(domain, f"Rules in this group cover {title.lower()}.")
        lines.extend(
            wrap_bullet(
                f"[{title}]({domain}/README.md)",
                f"{count} rules. {intro}",
            )
        )

    lines.extend(["", "## All Rules", ""])
    for domain in sorted(by_domain):
        title = domain_name(RULES_DIR / domain)
        lines.extend([f"### {title}", ""])
        for rule in sorted(by_domain[domain], key=lambda item: item.id):
            target = rule.path.relative_to(RULES_DIR).as_posix()
            lines.extend(wrap_bullet(f"[`{rule.id}`]({target})", summary(rule)))
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_all(rules: list[Rule]) -> dict[Path, str]:
    rendered = {RULES_DIR / "README.md": render_root(rules)}
    by_domain: dict[str, list[Rule]] = {}
    for rule in rules:
        by_domain.setdefault(rule.domain, []).append(rule)
    for domain, domain_rules in by_domain.items():
        rendered[RULES_DIR / domain / "README.md"] = render_domain(domain, domain_rules)
    return rendered


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail if rule indexes are not up to date",
    )
    args = parser.parse_args()

    rendered = render_all(discover_rules())
    if args.check:
        stale = [path.relative_to(ROOT).as_posix() for path, text in rendered.items() if path.read_text() != text]
        if stale:
            print("rule indexes are out of date:", file=sys.stderr)
            for item in stale:
                print(f"- {item}", file=sys.stderr)
            return 1
        return 0

    for path, text in rendered.items():
        path.write_text(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
