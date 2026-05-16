# Agent Report Proof In Handoffs

## Metadata

- Name: `Report Proof in Handoffs`
- ID: `AGENT-REPORT-PROOF-IN-HANDOFFS`
- Summary: Replace confidence language with the exact checks, inspection, screenshots, and skipped
  validation behind a handoff. Proof lets reviewers decide what to trust and what remains risky.
- Related: `report-verification-honestly, review-proof-not-just-code, produce-review-packets`
- Status: `reviewed`
- Domain: `agent-workflow`
- Tags: `agent-workflow, review-handoff, verification, testing`

## Rule

Report proof, not confidence, in agent handoffs.

## Why

Confidence language is not evidence. A handoff that says "looks good" tells the maintainer less than
one that names `cargo test`, `markdownlint-cli2`, a screenshot, a skipped check, or the exact file
inspected. Proof lets the reviewer decide what to trust.

## Helps

- Improves handoff quality and makes residual risk visible.

## Limits

Do not drown the handoff in raw logs. Summarize the checks that matter and call out skipped or
inconclusive validation directly.

## Agent Instruction

Report proof in handoffs instead of confidence language, because confidence is not evidence.

## Mechanisms

Supported by validation sections, command transcripts when useful, screenshot links, generated
artifact checks, and final summaries that separate run, skipped, and failed checks.

## References

- [Principle: Private Context Is Not Shared
  Context](../../principles/private-context-is-not-shared-context.md)
- [OpenAI Harness Engineering: agent legibility is the
  goal](https://openai.com/index/harness-engineering/#agent-legibility-is-the-goal)
- [OpenAI Symphony README](https://github.com/openai/symphony#readme)
