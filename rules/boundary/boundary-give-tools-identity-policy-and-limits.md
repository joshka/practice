# Boundary Give Tools Identity Policy And Limits

## Metadata

- ID: `BOUNDARY-GIVE-TOOLS-IDENTITY-POLICY-AND-LIMITS`
- Status: `reviewed`
- Domain: `boundary`
- Depth: `compact`

## Rule

Give tool boundaries typed identity, policy, cancellation, and output limits.

## Why

Tool calls need typed identity, authorization policy, cancellation behavior, and output limits
because they cross from controlled code into filesystem, shell, network, provider, or user-visible
effects. Unbounded or anonymous tools are hard to audit and recover from.

## Helps

- Reduces tool blast radius and makes execution, cancellation, and diagnostics predictable.

## Limits

Do not burden tiny pure helpers with tool-boundary ceremony. Apply this where a callable unit can
perform effects, consume resources, or expose data.

## Agent Instruction

Give tool boundaries typed identity, authorization policy, cancellation, and output limits before
crossing into filesystem, shell, network, provider, or user-visible effects.

## Mechanisms

Supported by tool schemas, operation IDs, policy checks, timeout and output caps, cancellation
tokens, structured errors, and audit logs.

## References

- [Principle: Explicit Boundaries Preserve
  Correctness](../../principles/explicit-boundaries-preserve-correctness.md)
- [Parse, don't validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)
- [Rust API Guidelines: validate arguments and return
  errors](https://rust-lang.github.io/api-guidelines/dependability.html#c-validate)
