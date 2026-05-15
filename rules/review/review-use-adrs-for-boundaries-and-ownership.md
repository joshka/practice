# Review Use Adrs For Boundaries And Ownership

## Metadata

- ID: `REVIEW-USE-ADRS-FOR-BOUNDARIES-AND-OWNERSHIP`
- Legacy ID: `R-0904`
- Status: `reviewed`
- Domain: `review`
- Depth: `compact`

## Rule

Use ADRs for durable boundary and ownership decisions.

## Why

Some decisions outlive the PR that introduces them: module ownership, public API boundaries,
storage formats, source-control topology, runtime responsibility, and service or crate boundaries.
An ADR gives those decisions a durable home so later contributors can understand the accepted
tradeoff without rereading old review threads.

## Helps

- Preserves architectural context, reduces repeated debate, and gives future changes a decision to
  affirm, revise, or replace.

## Limits

Do not require ADRs for routine local edits. Use them when the decision changes ownership,
compatibility, integration boundaries, or future design options.

## Agent Instruction

Use ADRs for decisions that outlive a PR, such as ownership, API boundaries, storage formats,
runtime responsibility, and service or crate boundaries.

## Mechanisms

Supported by ADR templates, decision indexes, PR links to the accepted decision, and follow-up ADRs
when the project deliberately reverses or narrows a previous choice.

## References

- [Principle: Private Context Is Not Shared
  Context](../../principles/private-context-is-not-shared-context.md)
- [Ed Page: PR style](https://epage.github.io/dev/pr-style/)
- [GitHub Docs: helping others review your
  changes](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/helping-others-review-your-changes)
