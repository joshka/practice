#!/usr/bin/env python3
"""Print guidance tags and the titles of their matching catalog items."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIR = ROOT / "src" / "content"
TAG_SOURCE = ROOT / "src" / "lib" / "site.ts"
STRUCTURED_DIRS = [
    "guides",
    "patterns",
    "principles",
    "mechanisms",
    "snippets/agents",
]


@dataclass(frozen=True)
class TagItem:
    title: str
    kind: str
    path: str
    source: str


def guidance_tags() -> list[str]:
    source = TAG_SOURCE.read_text()
    match = re.search(
        r"export const guidanceTagDefinitions = \[(.*?)\] as const satisfies",
        source,
        re.DOTALL,
    )
    if not match:
        raise RuntimeError("src/lib/site.ts does not expose guidanceTagDefinitions")
    tags = re.findall(r'''tag:\s*["']([^"']+)["']''', match.group(1))
    if not tags:
        raise RuntimeError("guidanceTagDefinitions does not contain any tags")
    return tags


def guidance_files() -> list[Path]:
    files = [
        path
        for directory in STRUCTURED_DIRS
        for path in (CONTENT_DIR / directory).glob("*.md")
        if path.name != "README.md"
    ]
    files.extend(
        path
        for path in (CONTENT_DIR / "rules").glob("*/*.md")
        if path.name != "README.md"
    )
    return sorted(files)


def title(text: str, path: Path) -> str:
    metadata_name = re.search(r"^- Name: `([^`]*)`", text, re.MULTILINE)
    if metadata_name:
        return metadata_name.group(1).strip()
    match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    return match.group(1).strip() if match else path.stem


def tags_for_file(text: str, path: Path, allowed_tags: set[str]) -> set[str]:
    match = re.search(r"^- Tags: `([^`]*)`", text, re.MULTILINE)
    tags = {value.strip() for value in match.group(1).split(",")} if match else set()

    if path.parent.parent.name == "rules" and path.parent.name in allowed_tags:
        tags.add(path.parent.name)

    return tags & allowed_tags


def item_kind(path: Path) -> str:
    relative = path.relative_to(CONTENT_DIR)
    if relative.parts[0] == "rules":
        return f"Rule / {relative.parts[1].replace('-', ' ').title()}"
    if relative.parts[:2] == ("snippets", "agents"):
        return "Agent"
    return relative.parts[0].removesuffix("s").title()


def tag_items(tags: list[str]) -> dict[str, list[TagItem]]:
    items: dict[str, list[TagItem]] = {tag: [] for tag in tags}
    allowed_tags = set(tags)
    for path in guidance_files():
        text = path.read_text()
        item_title = title(text, path)
        explicit_match = re.search(r"^- Tags: `([^`]*)`", text, re.MULTILINE)
        explicit_tags = (
            {value.strip() for value in explicit_match.group(1).split(",")}
            if explicit_match
            else set()
        )
        for tag in tags_for_file(text, path, allowed_tags):
            items[tag].append(
                TagItem(
                    title=item_title,
                    kind=item_kind(path),
                    path=path.relative_to(CONTENT_DIR).as_posix(),
                    source="explicit" if tag in explicit_tags else "inferred from rule domain",
                )
            )
    return items


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Print each guidance tag followed by matching item titles."
    )
    parser.add_argument("tags", nargs="*", help="Optional exact tag names to report")
    parser.add_argument(
        "--details",
        action="store_true",
        help="Include each item's kind, source path, and explicit or inferred membership",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    tags = guidance_tags()
    requested = set(args.tags)
    unknown = sorted(requested - set(tags))
    if unknown:
        raise SystemExit(f"unknown guidance tag: {', '.join(unknown)}")

    selected = sorted(requested or tags)
    items = tag_items(tags)
    for index, tag in enumerate(selected):
        if index:
            print()
        print(f"## {tag} ({len(items[tag])})")
        for item in sorted(items[tag], key=lambda value: value.title.casefold()):
            if args.details:
                print(f"- {item.kind}: {item.title} [{item.source}] (`{item.path}`)")
            else:
                print(f"- {item.title}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
