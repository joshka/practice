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
GUIDES_DIR = ROOT / "guides"
AGENT_RULES = ROOT / "snippets" / "agents" / "rules.md"
CORE_AGENT_SNIPPET = ROOT / "snippets" / "agents" / "core.md"
MAX_FLAT_GUIDE_BULLETS = 7
GUIDE_LONG_LIST_EXCEPTIONS = {
    "guides/rust-maintainability.md",
}

REQUIRED_ROOTS = [
    ".github/ISSUE_TEMPLATE/guidance-feedback.yml",
    "rules/README.md",
    "principles/README.md",
    "patterns/README.md",
    "mechanisms/README.md",
    "snippets/agents/README.md",
    "snippets/agents/rules.md",
    "templates/rule.md",
    "scripts/generate_rule_indexes.py",
    "scripts/generate_downstream_template.py",
    "templates/downstream/AGENTS.md",
    "templates/downstream/docs/development/rules/README.md",
]

FEEDBACK_FORM_FIELDS = {
    "item_url",
    "item_file",
    "item_id",
    "item_kind",
    "feedback_type",
    "what_happened",
    "suggested_change",
    "downstream_context",
}

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
    status: str
    domain: str
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
            status=metadata(text, "Status"),
            domain=metadata(text, "Domain"),
            agent_instruction=section(text, "Agent Instruction"),
        )
        for field, value in [
            ("ID", rule.id),
            ("Status", rule.status),
            ("Domain", rule.domain),
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


def audit_feedback_flow(errors: list[str]) -> None:
    template = ROOT / ".github" / "ISSUE_TEMPLATE" / "guidance-feedback.yml"
    if not template.exists():
        return

    text = template.read_text()
    fields = set(re.findall(r"^\s+id: ([a-z_]+)$", text, re.MULTILINE))
    for field in sorted(FEEDBACK_FORM_FIELDS - fields):
        fail(errors, f"{rel(template)} is missing issue-form field id: {field}")

    component = ROOT / "src" / "components" / "PageContent.astro"
    if not component.exists():
        fail(errors, "missing detail page component for feedback action")
        return
    component_text = component.read_text()
    for snippet in [
        "template', 'guidance-feedback.yml'",
        "'item_url'",
        "'item_file'",
        "'item_id'",
        "'item_kind'",
        "Give feedback",
    ]:
        if snippet not in component_text:
            fail(errors, f"src/components/PageContent.astro feedback flow is missing: {snippet}")


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


def audit_core_agent_snippet(errors: list[str]) -> None:
    if not CORE_AGENT_SNIPPET.exists():
        fail(errors, f"missing core agent snippet: {rel(CORE_AGENT_SNIPPET)}")
        return
    text = CORE_AGENT_SNIPPET.read_text()
    for guide in sorted(GUIDES_DIR.glob("*.md")):
        guide_ref = f"guides/{guide.name}"
        if guide_ref not in text:
            fail(errors, f"snippets/agents/core.md does not reference {guide_ref}")
    if "snippets/agents/rules.md" not in text:
        fail(errors, "snippets/agents/core.md does not reference the reviewed rule pack")


def audit_draft_review_queue(rules: list[Rule], errors: list[str]) -> None:
    draft_ids = {rule.id for rule in rules if rule.status == "draft"}
    if not draft_ids:
        return

    guide_rule_audit = ROOT / "references" / "guide-rule-audit.md"
    if not guide_rule_audit.exists():
        fail(errors, f"missing guide rule audit: {rel(guide_rule_audit)}")
        return
    text = guide_rule_audit.read_text()
    queue = section(text, "Draft Review Queue")
    queued_ids = set(re.findall(r"`([A-Z][A-Z0-9]+(?:-[A-Z0-9]+)+)`", queue))
    for rule in sorted(rules, key=lambda item: item.id):
        if rule.status != "draft":
            continue
        if rule.id not in queued_ids:
            fail(errors, f"references/guide-rule-audit.md does not list draft rule {rule.id}")
    known_ids = {rule.id for rule in rules}
    for rule_id in sorted(queued_ids - draft_ids):
        if rule_id in known_ids:
            fail(errors, f"references/guide-rule-audit.md lists non-draft rule {rule_id}")
        else:
            fail(errors, f"references/guide-rule-audit.md lists unknown draft rule {rule_id}")

    valid_guides = {f"guides/{path.name}" for path in GUIDES_DIR.glob("*.md")}
    queue_items = {}
    for item in re.findall(r"(?ms)^- .*?(?=^\- |\Z)", queue):
        item_ids = re.findall(r"`([A-Z][A-Z0-9]+(?:-[A-Z0-9]+)+)`", item)
        for rule_id in item_ids:
            queue_items[rule_id] = item
    for rule_id in sorted(queued_ids):
        bullet = queue_items.get(rule_id, "")
        mentioned_guides = set(re.findall(r"`(guides/[^`]+\.md)`", bullet))
        has_pre_existing_note = "pre-existing draft" in bullet
        if not mentioned_guides and not has_pre_existing_note:
            fail(errors, f"references/guide-rule-audit.md queue lacks origin context for {rule_id}")
            continue
        for guide in sorted(mentioned_guides - valid_guides):
            fail(errors, f"references/guide-rule-audit.md queue records unknown origin guide {guide}")


def audit_extracted_draft_rules(rules: list[Rule], errors: list[str]) -> None:
    draft_ids = {rule.id for rule in rules if rule.status == "draft"}
    if not draft_ids:
        return

    guide_rule_audit = ROOT / "references" / "guide-rule-audit.md"
    if not guide_rule_audit.exists():
        return
    text = guide_rule_audit.read_text()
    extracted = section(text, "Extracted Draft Rules")
    if not extracted:
        fail(errors, "references/guide-rule-audit.md is missing extracted draft rule evidence")
        return

    extracted_ids = set(re.findall(r"`([A-Z][A-Z0-9]+(?:-[A-Z0-9]+)+)`", extracted))
    if not extracted_ids:
        fail(errors, "references/guide-rule-audit.md extracted draft rule section lists no rules")
        return

    known_ids = {rule.id for rule in rules}
    for rule_id in sorted(extracted_ids - draft_ids):
        if rule_id in known_ids:
            fail(errors, f"references/guide-rule-audit.md extracts non-draft rule {rule_id}")
        else:
            fail(errors, f"references/guide-rule-audit.md extracts unknown rule {rule_id}")

    queue = section(text, "Draft Review Queue")
    queued_ids = set(re.findall(r"`([A-Z][A-Z0-9]+(?:-[A-Z0-9]+)+)`", queue))
    for rule_id in sorted(extracted_ids - queued_ids):
        fail(errors, f"references/guide-rule-audit.md extracts rule not queued for review: {rule_id}")

    valid_guides = {f"guides/{path.name}" for path in GUIDES_DIR.glob("*.md")}
    for rule_id in sorted(extracted_ids):
        match = re.search(
            rf"((?:.|\n)*?)\[`{re.escape(rule_id)}`\]",
            extracted,
        )
        if not match:
            continue
        bullet_start = match.group(1).rfind("\n- ")
        bullet = extracted[bullet_start + 1 : match.end()] if bullet_start >= 0 else match.group(0)
        mentioned_guides = set(re.findall(r"`(guides/[^`]+\.md)`", bullet))
        if not mentioned_guides:
            fail(errors, f"references/guide-rule-audit.md does not record an origin guide for {rule_id}")
            continue
        for guide in sorted(mentioned_guides - valid_guides):
            fail(errors, f"references/guide-rule-audit.md records unknown origin guide {guide}")


def audit_draft_external_references(rules: list[Rule], errors: list[str]) -> None:
    for rule in rules:
        if rule.status != "draft":
            continue
        references = section(rule.path.read_text(), "References")
        if not re.search(r"https?://", references):
            fail(errors, f"{rel(rule.path)} draft rule should cite at least one external source")


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


def audit_guide_grouping(errors: list[str]) -> None:
    for path in sorted(GUIDES_DIR.glob("*.md")):
        if rel(path) in GUIDE_LONG_LIST_EXCEPTIONS:
            continue
        lines = path.read_text().splitlines()
        start: int | None = None
        count = 0
        for line_number, line in enumerate(lines, 1):
            if line.startswith("- "):
                if start is None:
                    start = line_number
                    count = 0
                count += 1
                continue
            if start is not None and count > MAX_FLAT_GUIDE_BULLETS:
                fail(
                    errors,
                    f"{rel(path)}:{start} has {count} consecutive top-level bullets; "
                    "group long guide lists under named subheadings",
                )
            start = None
            count = 0
        if start is not None and count > MAX_FLAT_GUIDE_BULLETS:
            fail(
                errors,
                f"{rel(path)}:{start} has {count} consecutive top-level bullets; "
                "group long guide lists under named subheadings",
            )


def audit_guide_structure(errors: list[str]) -> None:
    for path in sorted(GUIDES_DIR.glob("*.md")):
        text = path.read_text()
        for heading in ["Related Guidance", "Review Questions"]:
            if f"\n## {heading}\n" not in text:
                fail(errors, f"{rel(path)} is missing guide section: {heading}")
        if rel(path) not in GUIDE_LONG_LIST_EXCEPTIONS:
            review_questions = section(text, "Review Questions")
            if not re.search(r"^### ", review_questions, re.MULTILINE):
                fail(errors, f"{rel(path)} review questions are not grouped under named subheadings")


def audit_related_guidance_rule_links(errors: list[str]) -> None:
    for path in sorted(GUIDES_DIR.glob("*.md")):
        text = path.read_text()
        related = section(text, "Related Guidance")
        definitions = {
            match.group(1): match.group(2)
            for match in re.finditer(r"^\[([^\]]+)\]:\s+(\S+)", text, re.MULTILINE)
        }
        inline_targets = re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", related)
        reference_targets = [
            definitions[label]
            for label in re.findall(r"\[[^\]\n]+\]\[([^\]\n]+)\]", related)
            if label in definitions
        ]
        if not any(target.startswith("../rules/") for target in inline_targets + reference_targets):
            fail(errors, f"{rel(path)} related guidance does not link to a rules artifact")


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
    audit_feedback_flow(errors)
    rules = read_rules(errors)
    audit_domain_indexes(rules, errors)
    audit_agent_pack(rules, errors)
    audit_core_agent_snippet(errors)
    audit_draft_review_queue(rules, errors)
    audit_extracted_draft_rules(rules, errors)
    audit_draft_external_references(rules, errors)
    audit_rule_references(rules, errors)
    audit_markdown_links(errors)
    audit_public_text(errors)
    audit_guide_grouping(errors)
    audit_guide_structure(errors)
    audit_related_guidance_rule_links(errors)
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
