# Review Make Review Artifacts Standalone

## Metadata

- Name: `Make Review Artifacts Standalone`
- ID: `REVIEW-MAKE-REVIEW-ARTIFACTS-STANDALONE`
- Summary: Put the needed problem, decision, context, validation, and risk in the issue, PR, commit,
  or handoff itself. Standalone artifacts make review and future debugging possible without private
  session context.
- Status: `reviewed`
- Domain: `review`
- Depth: `compact`

## Rule

Make issues, PRs, commit messages, and review handoffs stand alone.

## Why

Issues, PR descriptions, commit messages, and agent handoffs are read by people who did not see the
chat, scratch notes, local plan, or discarded attempts. They need the problem, decision, relevant
context, validation, and remaining risk in the artifact itself, not hidden in the development
session that produced it.

## Helps

- Makes review possible without private context and leaves durable reasoning for future debugging,
  archaeology, and follow-up work.

## Limits

Do not paste transcripts or long local notes. Summarize only the context that changes how a
reviewer, maintainer, or future agent should understand the work.

## Agent Instruction

Make issues, PRs, commit messages, and handoffs stand alone for readers who did not see the chat,
notes, plan, or discarded attempts.

## Mechanisms

Supported by issue and PR templates, commit-message bodies, review packets, ADR links, validation
sections, and final handoff notes that restate private decisions in shared language.

## References

- [Principle: Private Context Is Not Shared
  Context](../../principles/private-context-is-not-shared-context.md)
- [Ed Page: PR style](https://epage.github.io/dev/pr-style/)
- [GitHub Docs: helping others review your
  changes](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/helping-others-review-your-changes)
