# Boundary Name Lifecycle Transitions

## Metadata

- Name: `Name Lifecycle Transitions`
- ID: `BOUNDARY-NAME-LIFECYCLE-TRANSITIONS`
- Summary: Model creation, activation, cancellation, teardown, reload, and promotion as named
  operations when they carry different invariants. This keeps ordering, cleanup, retry, and recovery
  rules visible without adding ceremony to simple constructed values.
- Status: `reviewed`
- Domain: `boundary`
- Depth: `compact`

## Rule

Treat lifecycle transitions as named operations.

## Why

Creation, activation, cancellation, teardown, reload, and promotion are different operations with
different invariants. Treating them as incidental flag changes makes cleanup, retries, and error
recovery harder to reason about.

## Helps

- Makes lifecycle behavior explicit and keeps invalid ordering visible.

## Limits

Do not invent lifecycle ceremony for values that are simply constructed and dropped. Name
transitions when resources, external effects, or stateful protocols are involved.

## Agent Instruction

Treat lifecycle transitions as named operations because creation, activation, cancellation, teardown,
reload, and promotion are different operations with different invariants.

## Mechanisms

Supported by transition methods, state enums, RAII guards, cancellation tokens, teardown tests, and
docs for caller obligations.

## References

- [Principle: Explicit Boundaries Preserve
  Correctness](../../principles/explicit-boundaries-preserve-correctness.md)
- [Parse, don't validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)
- [Rust API Guidelines: validate arguments and return
  errors](https://rust-lang.github.io/api-guidelines/dependability.html#c-validate)
