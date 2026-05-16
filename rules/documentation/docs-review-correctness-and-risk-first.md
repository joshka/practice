# Docs Review Correctness And Risk First

## Metadata

- Name: `Review Correctness and Risk First`
- ID: `DOCS-REVIEW-CORRECTNESS-AND-RISK-FIRST`
- Summary: `Lead documentation review with false contracts, drift, operability, and unsupported
  claims before style polish. This separates blocking risk from wording cleanup.`
- Status: `reviewed`
- Domain: `documentation`
- Depth: `compact`

## Rule

Lead documentation review with correctness, contract ambiguity, risk, drift, and operability.

## Why

Documentation polish is visible, but the expensive failures are usually false contracts, ambiguous
caller obligations, stale examples, unverifiable commands, unsupported claims, hidden operational
effects, or docs that no longer match the code. If review starts with wording preferences, the
author can spend attention on style while merge-blocking misunderstandings remain unresolved.

Risk-first documentation review makes the review useful even when prose still needs later polish. It
also helps authors distinguish defects that change behavior, trust, support load, or agent
execution from edits that only improve phrasing.

## Helps

- Keeps documentation review focused on user trust, operational accuracy, and contract drift.
- Separates merge-blocking doc defects from style or polish comments.

## Limits

Polish still matters when unclear prose changes the reader's behavior or hides the contract. Use
severity labels when they help; do not turn a small typo review into a full risk audit.

## Agent Instruction

Review docs for correctness, contract ambiguity, risk, drift, and operability before style polish;
use severity labels to separate blocking misunderstandings from wording cleanup.

## Mechanisms

Supported by docs review checklists, rendered-page inspection, command and link verification,
support-matrix checks, severity labels, and review packets that list validation evidence.

## References

- [Docs Treat Docs As Contracts](docs-treat-docs-as-contracts.md)
- [Docs Verify Commands Paths And Links](docs-verify-commands-paths-and-links.md)
- [Google Engineering Practices: What to look for in a code review](https://google.github.io/eng-practices/review/reviewer/looking-for.html)
