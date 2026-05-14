# Prefer Tools Over Prompts

## Metadata

- Name: `Prefer Tools Over Prompts`
- ID: `prefer-tools-over-prompts`
- Status: `reviewed`
- Audience: `agents`
- Topics: `agents, validation, tooling`
- Related: `make-bad-output-mechanically-hard, smallest-trustworthy-verification`

## Problem

Instructions alone are weak guardrails. Agents can forget them, overfit them, or apply them too late
after already producing the wrong shape. Maintainers should not have to enforce repeatable checks by
manual review.

## Preferred Move

Prefer runnable tools, local commands, lint rules, tests, templates, and examples over prose-only
instructions when a preference can be checked or scaffolded mechanically. Keep prose for judgment
and tradeoffs; use tools for repeatable constraints.

## Tradeoff

Not every preference deserves tooling. Use prose when the rule is rare, judgment-heavy, or still
being discovered. Add tools when the same failure is common, cheap to detect, and expensive to
review manually.

## Agent Instruction

When you notice a repeatable quality rule, prefer adding or using a check, template, or command over
adding another paragraph of instructions. Report the tool or command that now enforces the rule.

## Examples

Bad: the repo relies on a reminder for a mechanical Markdown rule.

```text
Please remember to align table columns.
```

Good: the repo encodes the rule and validates it.

```yaml
config:
  table-column-style:
    style: aligned
```
