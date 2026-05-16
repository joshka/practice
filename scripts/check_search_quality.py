#!/usr/bin/env python3
"""Check important rendered search-index queries."""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SEARCH_INDEX = ROOT / "dist" / "search.json"


@dataclass(frozen=True)
class SearchExpectation:
    query: str
    expected_top: tuple[str, ...]


EXPECTATIONS = [
    SearchExpectation(
        query="copy review note",
        expected_top=(
            "/practice/rules/documentation/docs-make-review-easy-to-inspect/",
            "/practice/patterns/review-proof-not-just-code/",
            "/practice/patterns/produce-review-packets/",
        ),
    ),
    SearchExpectation(
        query="copy citation",
        expected_top=(
            "/practice/guides/software-change-preferences/",
            "/practice/guides/coding-agents/",
            "/practice/mechanisms/guidance-generation-and-audit/",
            "/practice/agents/core/",
        ),
    ),
    SearchExpectation(
        query="jj workflow",
        expected_top=(
            "/practice/guides/jj-workflow/",
            "/practice/mechanisms/jj-agent-workflow/",
        ),
    ),
    SearchExpectation(
        query="rust api",
        expected_top=(
            "/practice/mechanisms/rust-api-and-release-checks/",
            "/practice/rules/rust/",
            "/practice/guides/rust-maintainability/",
        ),
    ),
    SearchExpectation(
        query="global mutable state",
        expected_top=(
            "/practice/why/avoid-global-mutable-state/",
            "/practice/rules/boundary/boundary-avoid-global-mutable-state/",
        ),
    ),
    SearchExpectation(
        query="feedback guidance",
        expected_top=(
            "/practice/patterns/turn-feedback-into-guidance/",
            "/practice/rules/agent-workflow/agent-turn-feedback-into-guidance/",
            "/practice/mechanisms/guidance-generation-and-audit/",
        ),
    ),
]


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value.lower()).strip()


def score(entry: dict[str, Any], query: str) -> int | None:
    normalized_query = normalize(query)
    tokens = [token for token in normalized_query.split(" ") if token]
    title = normalize(entry["title"])
    item_id = normalize(entry.get("id") or "")
    description = normalize(entry["description"])
    headings = normalize(" ".join(entry["headings"]))
    text = normalize(entry["text"])

    if not all(token in text for token in tokens):
        return None

    value = 0
    if title == normalized_query:
        value += 80
    if item_id == normalized_query:
        value += 95
    if title.startswith(normalized_query):
        value += 45
    if item_id.startswith(normalized_query):
        value += 65
    if normalized_query in title:
        value += 30
    if normalized_query in item_id:
        value += 45
    if normalized_query in description:
        value += 12
    if normalized_query in headings:
        value += 18
    for token in tokens:
        if token in item_id:
            value += 18
        if token in title:
            value += 12
        if token in headings:
            value += 8
        if token in description:
            value += 4
        if token in text:
            value += 1
    return value


def search(entries: list[dict[str, Any]], query: str) -> list[str]:
    scored = [
        (entry_score, entry["title"], entry["url"])
        for entry in entries
        if (entry_score := score(entry, query)) is not None
    ]
    return [
        url
        for _entry_score, _title, url in sorted(scored, key=lambda item: (-item[0], item[1]))[:8]
    ]


def main() -> int:
    if not SEARCH_INDEX.exists():
        print("dist/search.json does not exist; run `pnpm build` first", file=sys.stderr)
        return 1

    entries = json.loads(SEARCH_INDEX.read_text())
    errors: list[str] = []
    for expectation in EXPECTATIONS:
        top_urls = search(entries, expectation.query)
        if not any(url in top_urls for url in expectation.expected_top):
            expected = ", ".join(expectation.expected_top)
            actual = ", ".join(top_urls)
            errors.append(
                f"{expectation.query!r} did not return an expected page in the top 8; "
                f"expected one of: {expected}; actual: {actual}",
            )

    if errors:
        print("Search quality check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Search quality check passed: {len(EXPECTATIONS)} queries.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
