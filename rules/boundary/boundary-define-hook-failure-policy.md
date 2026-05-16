# Boundary Define Hook Failure Policy

## Metadata

- ID: `BOUNDARY-DEFINE-HOOK-FAILURE-POLICY`
- Status: `reviewed`
- Domain: `boundary`
- Depth: `compact`

## Rule

Define hook failure policy.

## Why

Hooks can fail before, during, or after the main operation. If policy is implicit, callers cannot
know whether a failed hook blocks the operation, retries, logs and continues, rolls back, or leaves
partial state.

## Helps

- Makes extension, callback, and automation behavior predictable under failure.

## Limits

Different hooks can have different policies. Name the policy for each hook class instead of forcing
one global answer.

## Agent Instruction

Define hook failure policy because hooks can fail before, during, or after the main operation.

## Mechanisms

Supported by hook result types, retry policy, rollback tests, structured errors, and docs that state
whether hooks are advisory or blocking.

## References

- [Principle: Explicit Boundaries Preserve
  Correctness](../../principles/explicit-boundaries-preserve-correctness.md)
- [Parse, don't validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)
- [Rust API Guidelines: validate arguments and return
  errors](https://rust-lang.github.io/api-guidelines/dependability.html#c-validate)
