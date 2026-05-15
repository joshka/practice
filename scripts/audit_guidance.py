#!/usr/bin/env python3
"""Audit the guidance repository structure and generated surfaces."""

from __future__ import annotations

import re
import sys
import argparse
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RULES_DIR = ROOT / "rules"
AGENT_RULES = ROOT / "snippets" / "agents" / "rules.md"

REQUIRED_ROOTS = [
    "rules/README.md",
    "principles/README.md",
    "patterns/README.md",
    "mechanisms/README.md",
    "snippets/agents/README.md",
    "snippets/agents/rules.md",
    "references/guidance-plan.md",
    "templates/rule.md",
    "scripts/generate_rule_indexes.py",
    "scripts/generate_downstream_template.py",
    "templates/downstream/AGENTS.md",
    "templates/downstream/docs/development/rules/README.md",
]

RULE_SECTIONS = [
    "Metadata",
    "Rule",
    "Why",
    "Helps",
    "Limits",
    "Agent Instruction",
    "Mechanisms",
    "References",
]

ALLOWED_STATUSES = {"draft", "reviewed", "needs-work"}
ALLOWED_DEPTHS = {"compact", "expanded"}

PLACEHOLDER_PATTERNS = [
    r"\bTBD\b",
    r"needs expansion",
    r"promoted from reviewed guidance",
    r"Deepen this section",
    r"Rationale needs",
    r"Mechanisms need",
    r"References need",
    r"Record exceptions",
    r"Outcome notes",
    r"Add durable references when",
]

PRIVATE_CONTEXT_PATTERNS = [
    r"/Users/[^)\s]+",
    r"~/local/[^)\s]+",
    r"\.\./(?:komodo|tui-tracing|piers|jk|qwertty|qwertty-prototype|betamax|tidysrc)\b",
]


@dataclass(frozen=True)
class Rule:
    path: Path
    id: str
    legacy_id: str
    status: str
    domain: str
    depth: str
    agent_instruction: str


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


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
    return match.group(1).strip()


def public_markdown_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*.md"):
        parts = path.relative_to(ROOT).parts
        if any(part.startswith(".") for part in parts):
            continue
        files.append(path)
    return sorted(files)


def read_rules(errors: list[str]) -> list[Rule]:
    rules: list[Rule] = []
    seen_ids: dict[str, Path] = {}
    for path in sorted(RULES_DIR.glob("*/*.md")):
        if path.name == "README.md":
            continue
        text = path.read_text()
        missing_sections = [name for name in RULE_SECTIONS if not section(text, name)]
        for name in missing_sections:
            fail(errors, f"{rel(path)} is missing section content: {name}")

        rule = Rule(
            path=path,
            id=metadata(text, "ID"),
            legacy_id=metadata(text, "Legacy ID"),
            status=metadata(text, "Status"),
            domain=metadata(text, "Domain"),
            depth=metadata(text, "Depth"),
            agent_instruction=section(text, "Agent Instruction"),
        )
        for field, value in [
            ("ID", rule.id),
            ("Legacy ID", rule.legacy_id),
            ("Status", rule.status),
            ("Domain", rule.domain),
            ("Depth", rule.depth),
        ]:
            if not value:
                fail(errors, f"{rel(path)} is missing metadata field: {field}")
        if rule.id and not re.fullmatch(r"[A-Z][A-Z0-9]+(?:-[A-Z0-9]+)+", rule.id):
            fail(errors, f"{rel(path)} has invalid rule ID: {rule.id}")
        if rule.id in seen_ids:
            fail(errors, f"{rel(path)} duplicates ID from {rel(seen_ids[rule.id])}: {rule.id}")
        elif rule.id:
            seen_ids[rule.id] = path
        if rule.status and rule.status not in ALLOWED_STATUSES:
            fail(errors, f"{rel(path)} has invalid status: {rule.status}")
        if rule.depth and rule.depth not in ALLOWED_DEPTHS:
            fail(errors, f"{rel(path)} has invalid depth: {rule.depth}")
        if rule.domain and path.parent.name != rule.domain:
            fail(errors, f"{rel(path)} domain does not match directory: {rule.domain}")
        if rule.agent_instruction and "\n\n" in rule.agent_instruction:
            fail(errors, f"{rel(path)} agent instruction should be one compact paragraph")
        if rule.agent_instruction and rule.agent_instruction[-1] not in ".!?":
            fail(errors, f"{rel(path)} agent instruction should end with punctuation")
        rules.append(rule)
    if not rules:
        fail(errors, "no rule files found under rules/*/*.md")
    return rules


def audit_required_roots(errors: list[str]) -> None:
    for item in REQUIRED_ROOTS:
        if not (ROOT / item).exists():
            fail(errors, f"missing required guidance artifact: {item}")


def audit_domain_indexes(rules: list[Rule], errors: list[str]) -> None:
    by_domain: dict[str, list[Rule]] = {}
    for rule in rules:
        by_domain.setdefault(rule.domain, []).append(rule)

    root_index = (RULES_DIR / "README.md").read_text()
    for domain, domain_rules in sorted(by_domain.items()):
        readme = RULES_DIR / domain / "README.md"
        if not readme.exists():
            fail(errors, f"missing domain index: {rel(readme)}")
            continue
        text = readme.read_text()
        if "[Rule]" in text or re.search(r"^\s+- ID: ", text, re.MULTILINE):
            fail(errors, f"{rel(readme)} uses bare rule-list formatting instead of summaries")
        for rule in domain_rules:
            target = rule.path.name
            if f"[`{rule.id}`]({target})" not in text:
                fail(errors, f"{rel(readme)} does not link {target} with ID text")
            root_target = f"{domain}/{target}"
            if f"[`{rule.id}`]({root_target})" not in root_index:
                fail(errors, f"rules/README.md does not link {root_target} with ID text")
    if "[Rule]" in root_index or re.search(r"^\s+- ID: ", root_index, re.MULTILINE):
        fail(errors, "rules/README.md uses bare rule-list formatting instead of summaries")


def audit_agent_pack(rules: list[Rule], errors: list[str]) -> None:
    if not AGENT_RULES.exists():
        fail(errors, f"missing agent rule pack: {rel(AGENT_RULES)}")
        return
    pack = AGENT_RULES.read_text()
    pack_ids = set(re.findall(r"^- `([^`]+)`:", pack, re.MULTILINE))
    reviewed_ids = {rule.id for rule in rules if rule.status == "reviewed"}
    extra = pack_ids - reviewed_ids
    missing = reviewed_ids - pack_ids
    for rule_id in sorted(missing):
        fail(errors, f"snippets/agents/rules.md is missing reviewed rule {rule_id}")
    for rule_id in sorted(extra):
        fail(errors, f"snippets/agents/rules.md contains non-reviewed or unknown rule {rule_id}")
    if "Generated by `scripts/generate_agent_rules.py`" not in pack:
        fail(errors, "snippets/agents/rules.md does not identify its generator")
    if re.search(r"\[[^\]\n]+\]\([^)\n]+\)", pack):
        fail(errors, "snippets/agents/rules.md should not contain Markdown links")


def audit_rule_references(rules: list[Rule], errors: list[str]) -> None:
    rule_ids = {rule.id for rule in rules}
    pattern = re.compile(r"`([A-Z][A-Z0-9]+-[A-Z0-9][A-Z0-9-]+)`")
    for path in public_markdown_files():
        text = path.read_text()
        for match in pattern.finditer(text):
            rule_id = match.group(1)
            if rule_id in rule_ids or re.fullmatch(r"R-\d{4}", rule_id):
                continue
            line = text[: match.start()].count("\n") + 1
            fail(errors, f"{rel(path)}:{line} references unknown rule ID {rule_id}")


def audit_markdown_links(errors: list[str]) -> None:
    link_pattern = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)")
    for path in public_markdown_files():
        text = path.read_text()
        for match in link_pattern.finditer(text):
            raw_target = match.group(1).strip()
            if raw_target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = raw_target.split("#", 1)[0]
            if not target:
                continue
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                continue
            target_path = (path.parent / target).resolve()
            try:
                target_path.relative_to(ROOT)
            except ValueError:
                fail(errors, f"{rel(path)} links outside repo: {raw_target}")
                continue
            if not target_path.exists():
                line = text[: match.start()].count("\n") + 1
                fail(errors, f"{rel(path)}:{line} has missing link target: {raw_target}")


def audit_public_text(errors: list[str]) -> None:
    for path in public_markdown_files():
        text = path.read_text()
        for pattern in PLACEHOLDER_PATTERNS:
            for match in re.finditer(pattern, text, re.IGNORECASE):
                line = text[: match.start()].count("\n") + 1
                fail(errors, f"{rel(path)}:{line} contains placeholder text: {match.group(0)}")
        for pattern in PRIVATE_CONTEXT_PATTERNS:
            for match in re.finditer(pattern, text):
                line = text[: match.start()].count("\n") + 1
                fail(errors, f"{rel(path)}:{line} contains local/private context: {match.group(0)}")


def audit_rule_quality(rules: list[Rule], errors: list[str]) -> None:
    repeated_sections: dict[str, dict[str, list[Path]]] = {
        "Helps": defaultdict(list),
        "Limits": defaultdict(list),
        "Mechanisms": defaultdict(list),
    }
    for rule in rules:
        text = rule.path.read_text()
        rule_text = " ".join(section(text, "Rule").split())
        why_text = " ".join(section(text, "Why").split())
        agent_text = " ".join(section(text, "Agent Instruction").split())
        if why_text.startswith(rule_text):
            fail(errors, f"{rel(rule.path)} starts Why by repeating the rule text")
        if agent_text.rstrip(".") == rule_text.rstrip("."):
            fail(errors, f"{rel(rule.path)} repeats the rule text as its agent instruction")
        if len(agent_text.split()) > 45:
            fail(errors, f"{rel(rule.path)} has an overlong agent instruction")
        if agent_text.startswith("When "):
            fail(errors, f"{rel(rule.path)} starts its agent instruction with 'When'")
        if re.search(r"\bwhen\b", agent_text, re.IGNORECASE):
            fail(errors, f"{rel(rule.path)} uses stilted 'when' phrasing in its agent instruction")
        if re.search(r"\bbecause\b.+\bbecause\b", agent_text, re.IGNORECASE):
            fail(errors, f"{rel(rule.path)} repeats 'because' in its agent instruction")
        first_word = agent_text.split(" ", 1)[0] if agent_text else ""
        if first_word in {"And", "Or", "Not", "Then", "In"}:
            fail(errors, f"{rel(rule.path)} has a broken action-first agent instruction")
        if re.search(r"\bwhen\b.+\bwhen\b", agent_text, re.IGNORECASE):
            fail(errors, f"{rel(rule.path)} has a nested 'when' agent instruction")
        for name, values in repeated_sections.items():
            value = " ".join(section(text, name).split())
            if value:
                values[value].append(rule.path)

    for name, values in repeated_sections.items():
        for value, paths in values.items():
            if len(paths) < 10:
                continue
            examples = ", ".join(rel(path) for path in paths[:3])
            fail(
                errors,
                f"{name} section is repeated across {len(paths)} rules; "
                f"examples: {examples}; text: {value[:120]}",
            )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--quality",
        action="store_true",
        help="also fail on explanation-quality smells such as repeated rule rationales",
    )
    args = parser.parse_args()

    errors: list[str] = []
    audit_required_roots(errors)
    rules = read_rules(errors)
    audit_domain_indexes(rules, errors)
    audit_agent_pack(rules, errors)
    audit_rule_references(rules, errors)
    audit_markdown_links(errors)
    audit_public_text(errors)
    if args.quality:
        audit_rule_quality(rules, errors)

    if errors:
        print("Guidance audit failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    reviewed = sum(1 for rule in rules if rule.status == "reviewed")
    draft = sum(1 for rule in rules if rule.status == "draft")
    needs_work = sum(1 for rule in rules if rule.status == "needs-work")
    print(
        "Guidance audit passed: "
        f"{len(rules)} rules ({reviewed} reviewed, {draft} draft, {needs_work} needs-work)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
