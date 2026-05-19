# Source Make Shared Artifacts Standalone

## Metadata

- Name: `Make Shared Artifacts Standalone`
- ID: `SOURCE-MAKE-SHARED-ARTIFACTS-STANDALONE`
- Summary: Restate the problem, rationale, evidence, and tradeoffs in shared docs, templates,
  generated packs, or reusable guidance. Future readers should not need private notes or
  transcripts to trust the artifact.
- Related: `private-context-is-not-shared-context, prefer-durable-summaries,
  review-make-review-artifacts-standalone`
- Status: `reviewed`
- Domain: `source`
- Tags: `source-truth, documentation, review-handoff, agent-context`

## Rule

Make shared docs, templates, generated packs, and reusable guidance stand alone.

## Why

Shared source artifacts often leave the development session with missing context. Docs, templates,
generated packs, and reusable guidance should restate the problem, rationale, decision, evidence,
and relevant tradeoffs for readers who did not see the local notes or agent transcript.

## Helps

- Makes shared work reviewable, auditable, and useful to future readers without local source
  material.

## Limits

Shared artifacts do not need to replay every local note or abandoned path. Include enough context
for the reader to trust the result, and leave out private scaffolding that would distract from the
published decision.

For issues, PRs, commit messages, and review handoffs, use
[`REVIEW-MAKE-REVIEW-ARTIFACTS-STANDALONE`](../review/review-make-review-artifacts-standalone.md).

## Agent Instruction

Make shared docs, templates, generated packs, and reusable guidance stand alone because they leave
the development session.

## Mechanisms

Supported by source-link review, stale-reference checks, private-context cleanup, and explicit
provenance notes where they help.

## References

- [Principle: Private Context Is Not Shared
  Context](../../principles/private-context-is-not-shared-context.md)
- [Rust API Guidelines: public APIs are stable](https://rust-lang.github.io/api-guidelines/necessities.html#c-stable)
- [Microsoft Pragmatic Rust Guidelines: prefer simple abstractions](https://microsoft.github.io/rust-guidelines/guidelines/libs/ux/#M-SIMPLE-ABSTRACTIONS)
