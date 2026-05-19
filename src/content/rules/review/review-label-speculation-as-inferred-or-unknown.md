# Review Label Speculation As Inferred Or Unknown

## Metadata

- Name: `Label Speculation as Inferred or Unknown`
- ID: `REVIEW-LABEL-SPECULATION-AS-INFERRED-OR-UNKNOWN`
- Summary: Mark review claims as observed, inferred, assumed, or unknown when the evidence level
  matters. Clear labels keep guesses from hardening into false project knowledge.
- Status: `reviewed`
- Domain: `review`
- Tags: `reviewability, source-truth, verification, documentation`
- Related: `label-doc-claims-by-evidence, report-verification-honestly, review-proof-not-just-code`

## Rule

Label speculation as inferred or unknown.

## Why

Review notes often mix facts, traces, guesses, and model-based conclusions. If "this cannot happen"
really means "I did not find a caller" or "the type shape appears to prevent it," the reviewer needs
that distinction. Labeling claims as observed, inferred, assumed, or unknown keeps uncertain
reasoning from hardening into false project knowledge.

## Helps

- Makes risk visible, keeps review discussion precise, and helps future readers decide what still
  needs verification.

## Limits

Do not weaken every sentence with hedging. Mark uncertainty where the evidence level changes the
decision, test plan, or risk.

## Agent Instruction

Label speculation as inferred or unknown because review notes often mix facts, traces, guesses, and
model-based conclusions.

## Mechanisms

Supported by PR notes that separate observed evidence from assumptions, review comments that ask
for proof, and validation sections that name skipped or unresolved checks.

## References

- [Principle: Private Context Is Not Shared
  Context](../../principles/private-context-is-not-shared-context.md)
- [Ed Page: PR style](https://epage.github.io/dev/pr-style/)
- [GitHub Docs: helping others review your
  changes](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/helping-others-review-your-changes)
