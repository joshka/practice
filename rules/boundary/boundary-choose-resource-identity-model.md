# Boundary Choose Resource Identity Model

## Metadata

- Name: `Choose Resource Identity Model`
- ID: `BOUNDARY-CHOOSE-RESOURCE-IDENTITY-MODEL`
- Summary: Decide whether the boundary mutates records, sets, files, sessions, handles, or whole
  documents before designing reconciliation. The chosen unit controls idempotency, matching,
  conflict handling, and the cost of later migration.
- Status: `reviewed`
- Domain: `boundary`
- Tags: `boundary-correctness, state-transitions, validation-policy, public-api`
- Related: `parse-dont-validate, make-state-transitions-explicit, prefer-standard-conversions`

## Rule

Choose the resource identity model up front.

## Why

A system that mutates individual records behaves differently from one that mutates record sets,
files, sessions, handles, or whole documents. The identity model determines idempotency, matching,
update strategy, conflict handling, and error recovery.

## Helps

- Prevents reconciliation bugs caused by comparing or mutating the wrong unit of state.

## Limits

The model can evolve, but changing it after callers depend on it is often a breaking API or
migration. Choose deliberately at the boundary before broad propagation.

## Agent Instruction

Choose the resource identity model up front because a system that mutates individual records behaves
differently from one that mutates record sets, files, sessions, handles, or whole documents.

## Mechanisms

Supported by resource ID types, API docs, reconciliation tests, provider fixtures, and update
functions named after the unit they mutate.

## References

- [Principle: Explicit Boundaries Preserve
  Correctness](../../principles/explicit-boundaries-preserve-correctness.md)
- [Parse, don't validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)
- [Rust API Guidelines: validate arguments and return
  errors](https://rust-lang.github.io/api-guidelines/dependability.html#c-validate)
