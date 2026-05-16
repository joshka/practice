#!/usr/bin/env python3
"""Fail when package dependencies are outdated."""

from __future__ import annotations

import json
import subprocess
import sys
from typing import Any


def main() -> int:
    result = subprocess.run(
        ["pnpm", "outdated", "--format", "json"],
        check=False,
        capture_output=True,
        text=True,
    )

    if result.returncode not in {0, 1}:
        print(result.stderr.strip() or result.stdout.strip(), file=sys.stderr)
        return result.returncode

    output = result.stdout.strip()
    if not output:
        print("Dependency health check passed: no outdated packages.")
        return 0

    try:
        packages: dict[str, dict[str, Any]] = json.loads(output)
    except json.JSONDecodeError as error:
        print(f"Dependency health check failed: could not parse pnpm outdated JSON: {error}")
        return 1

    if not packages:
        print("Dependency health check passed: no outdated packages.")
        return 0

    print(f"Dependency health check failed: {len(packages)} outdated package(s).")
    for name, details in sorted(packages.items()):
        current = details.get("current", "?")
        wanted = details.get("wanted", "?")
        latest = details.get("latest", "?")
        dependency_type = details.get("dependencyType", "dependency")
        print(f"- {name} ({dependency_type}): current {current}, wanted {wanted}, latest {latest}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
