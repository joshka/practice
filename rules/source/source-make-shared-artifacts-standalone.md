# Source Make Shared Artifacts Standalone

## Metadata

- ID: `SOURCE-MAKE-SHARED-ARTIFACTS-STANDALONE`
- Status: `reviewed`
- Domain: `source`
- Depth: `compact`

## Rule

Make issues, PRs, commit messages, docs, and handoffs stand alone.

## Why

Shared artifacts often leave the development session with missing context. Issues, PRs, commits,
docs, and handoffs should restate the problem, rationale, decision, evidence, and relevant
tradeoffs for readers who did not see the local notes or agent transcript.

## Helps

- Makes shared work reviewable, auditable, and useful to future readers without local source
  material.

## Limits

Shared artifacts do not need to replay every local note or abandoned path. Include enough context
for the reader to trust the result, and leave out private scaffolding that would distract from the
published decision.

## Agent Instruction

Make issues, PRs, commit messages, docs, and handoffs stand alone because they leave the development
session.

## Mechanisms

Supported by source-link review, stale-reference checks, private-context cleanup, and explicit
provenance notes where they help.

## References

- [Principle: Private Context Is Not Shared
  Context](../../principles/private-context-is-not-shared-context.md)
- [Rust API Guidelines: public APIs are stable](https://rust-lang.github.io/api-guidelines/necessities.html#c-stable)
- [Microsoft Pragmatic Rust Guidelines: prefer simple abstractions](https://microsoft.github.io/rust-guidelines/guidelines/libs/ux/#M-SIMPLE-ABSTRACTIONS)
