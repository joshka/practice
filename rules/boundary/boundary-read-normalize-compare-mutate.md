# Boundary Read Normalize Compare Mutate

## Metadata

- Name: `Read Normalize Compare Mutate`
- ID: `BOUNDARY-READ-NORMALIZE-COMPARE-MUTATE`
- Summary: Reconcile external state by reading the current provider view, normalizing it, comparing
  intent, and mutating only the real difference. The loop avoids destructive or noisy writes when
  formatting, defaults, ordering, or outside actors create drift.
- Status: `reviewed`
- Domain: `boundary`
- Depth: `compact`

## Rule

Reconcile external state by reading, normalizing, comparing, and then mutating.

## Why

External state may be formatted differently, reordered, defaulted, or partially managed by another
actor. Reading and normalizing before mutation prevents unnecessary writes and reduces destructive
updates caused by comparing raw local intent to raw provider state.

## Helps

- Makes reconciliation idempotent and safer against provider drift.

## Limits

Skip the full reconcile loop for simple create-only operations or APIs that already provide strong
compare-and-swap semantics. Use it when safe mutation depends on current remote state.

## Agent Instruction

Reconcile external state by reading, normalizing, comparing, then mutating so formatting, ordering,
defaults, and outside actors do not hide drift.

## Mechanisms

Supported by read models, normalization functions, diff plans, dry runs, idempotency tests, and
provider fixtures.

## References

- [Principle: Explicit Boundaries Preserve
  Correctness](../../principles/explicit-boundaries-preserve-correctness.md)
- [Parse, don't validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)
- [Rust API Guidelines: validate arguments and return
  errors](https://rust-lang.github.io/api-guidelines/dependability.html#c-validate)
