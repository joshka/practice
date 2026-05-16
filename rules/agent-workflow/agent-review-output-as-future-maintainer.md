# Agent Review Output As Future Maintainer

## Metadata

- Name: `Review Output as Future Maintainer`
- ID: `AGENT-REVIEW-OUTPUT-AS-FUTURE-MAINTAINER`
- Summary: Review agent output as someone who will not have the chat transcript. This keeps attention
  on durable code, docs, tests, validation proof, and residual risk.
- Status: `reviewed`
- Domain: `agent-workflow`
- Depth: `compact`

## Rule

Review agent output from the perspective of a future maintainer who did not see the session.

## Why

Agent output can pass checks while depending on prompt-only context, vague names, hidden state,
over-broad abstractions, missing tests, or undocumented behavior changes. The future maintainer will
not have the chat transcript in front of them. They need the code, docs, tests, and handoff artifact
to explain the change without replaying the session.

Reviewing as a future maintainer keeps attention on the durable artifact: whether the owning module
is clear, behavior is observable, edge cases are covered, documentation is truthful, and residual
risk is named.

## Helps

- Catches agent output that is locally plausible but hard to maintain after context disappears.
- Turns review from confidence assessment into durable artifact inspection.

## Limits

Do not require perfection before accepting a useful, coherent chunk. If the artifact is correct but
has follow-up cleanup, name the residual risk and keep the follow-up scoped. Apply deeper review to
public APIs, security-sensitive work, generated behavior, persistence, rendering, and changes that
will be hard to reverse.

## Agent Instruction

Review agent output as a future maintainer: check correctness, edge cases, API clarity,
documentation truthfulness, readable ownership, focused tests, validation proof, and residual risk.

## Mechanisms

Supported by review packets, focused validation logs, owning-module inspection, code-review
checklists, generated-drift checks, screenshots for rendered output, and handoff notes that separate
proof from residual risk.

## References

- [Agent Produce Review Packets](agent-produce-review-packets.md)
- [Agent Report Proof In Handoffs](agent-report-proof-in-handoffs.md)
- [Google Engineering Practices: What to look for in a code review](https://google.github.io/eng-practices/review/reviewer/looking-for.html)
