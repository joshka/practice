"""Regression checks for prose that the guidance audit should accept."""

import unittest
from pathlib import Path
from unittest.mock import patch

from audit_guidance import ROOT, Rule, audit_rule_quality


class RuleQualityTests(unittest.TestCase):
    def audit_instruction(self, instruction: str) -> list[str]:
        text = (
            "## Rule\n\nPreserve useful conditions.\n\n"
            "## Why\n\nReaders need to know where an instruction applies.\n\n"
            f"## Agent Instruction\n\n{instruction}\n"
        )
        rule = Rule(ROOT / "example.md", "EXAMPLE", "reviewed", "documentation", instruction)
        errors: list[str] = []
        with patch.object(Path, "read_text", return_value=text):
            audit_rule_quality([rule], errors)
        return errors

    def test_conditions_are_allowed(self):
        for instruction in (
            "When a build fails, retain the last successful preview.",
            "Retain the last successful preview when a build fails.",
            "Retry when the connection fails. Stop when the deadline expires.",
        ):
            with self.subTest(instruction=instruction):
                self.assertEqual(self.audit_instruction(instruction), [])

    def test_repeated_rule_still_fails(self):
        errors = self.audit_instruction("Preserve useful conditions.")
        self.assertEqual(
            errors, ["example.md repeats the rule text as its agent instruction"]
        )

    def test_overlong_instruction_still_fails(self):
        errors = self.audit_instruction(" ".join(["word"] * 46))
        self.assertEqual(errors, ["example.md has an overlong agent instruction"])


if __name__ == "__main__":
    unittest.main()
