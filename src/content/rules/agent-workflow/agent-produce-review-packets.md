# Agent Produce Review Packets

## Metadata

- Name: `Produce Review Packets`
- ID: `AGENT-PRODUCE-REVIEW-PACKETS`
- Summary: Hand off agent work with purpose, changed files, evidence, skipped checks, risks, and
  follow-ups. A review packet lets maintainers inspect the output without replaying the session.
- Related: `produce-review-packets, write-pr-narrative, review-proof-not-just-code`
- Status: `reviewed`
- Domain: `agent-workflow`
- Tags: `agent-workflow, review-handoff, verification, documentation`

## Rule

Produce review packets for agent output.

## Why

Agent output often spans code, docs, generated artifacts, and validation logs. A review packet
gathers the purpose, changed files, evidence, skipped checks, risks, and follow-ups so the human
reviewer can inspect the work without replaying the whole session.

## Helps

- Makes agent output reviewable and reduces trust gaps around what was actually checked.

## Limits

Keep packets proportional. A one-line docs fix needs a short validation note, not a full dossier.

## Agent Instruction

Produce review packets for agent output because agent output often spans code, docs, generated
artifacts, and validation logs.

## Mechanisms

Supported by PR summaries, final handoff templates, changed-file lists, validation sections,
screenshots, command output, and links to generated artifacts.

## References

- [Principle: Private Context Is Not Shared
  Context](../../principles/private-context-is-not-shared-context.md)
- [OpenAI Harness Engineering: agent legibility is the
  goal](https://openai.com/index/harness-engineering/#agent-legibility-is-the-goal)
- [OpenAI Symphony README](https://github.com/openai/symphony#readme)
