# Agent Make Bad Output Hard

## Metadata

- Name: `Make Bad Output Hard`
- ID: `AGENT-MAKE-BAD-OUTPUT-HARD`
- Summary: Turn recurring bad agent output into scripts, templates, lint, or checks that fail fast.
  Mechanical enforcement lowers review cost more reliably than repeated prompt reminders.
- Related: `make-bad-output-mechanically-hard, prefer-tools-over-prompts,
  mechanize-repeated-feedback`
- Status: `reviewed`
- Domain: `agent-workflow`
- Tags: `agent-workflow, tooling, automation, verification`

## Rule

Make bad output mechanically hard.

## Why

Repeated prompt reminders are weaker than a repo that rejects bad output mechanically. If agents
keep producing stale generated files, unformatted docs, invalid rule IDs, or missing validation
notes, add a script, template, lint, or check that makes the bad path fail fast.

## Helps

- Turns recurring review feedback into enforcement and lowers the cost of good output.

## Limits

Do not add tools that are heavier than the failure they catch. Prefer simple checks before complex
automation.

## Agent Instruction

Make bad output mechanically hard because repeated prompt reminders are weaker than a repo that rejects
bad output mechanically.

## Mechanisms

Supported by generators, lint rules, schema checks, preflight scripts, CI jobs, templates, and audit
commands such as `scripts/audit_guidance.py`.

## References

- [Principle: Private Context Is Not Shared
  Context](../../principles/private-context-is-not-shared-context.md)
- [OpenAI Harness Engineering: agent legibility is the
  goal](https://openai.com/index/harness-engineering/#agent-legibility-is-the-goal)
- [OpenAI Symphony README](https://github.com/openai/symphony#readme)
