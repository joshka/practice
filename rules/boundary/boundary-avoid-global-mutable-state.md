# Boundary Avoid Global Mutable State

## Metadata

- ID: `BOUNDARY-AVOID-GLOBAL-MUTABLE-STATE`
- Legacy ID: `R-0305`
- Status: `reviewed`
- Domain: `boundary`
- Depth: `compact`

## Rule

Avoid global mutable state.

## Why

Global mutable state hides ownership, ordering, reset, and concurrency requirements. In Rust apps it
can make tests order-dependent, make alternate runtimes hard to inject, and make agents miss that
changing one path affects unrelated callers.

## Helps

- Improves test isolation, explicit lifecycle management, and reasoning about shared state.

## Limits

Caches, registries, metrics handles, and process-level coordination can be global when owner, reset
policy, synchronization, and caller contract are explicit.

## Agent Instruction

Avoid global mutable state because it hides ownership, ordering, reset, and concurrency
requirements.

## Mechanisms

Supported by dependency injection, owned handles, `OnceLock` with explicit policy, test reset hooks,
narrow visibility, and concurrency tests.

## References

- [Principle: Explicit Boundaries Preserve
  Correctness](../../principles/explicit-boundaries-preserve-correctness.md)
- [Parse, don't validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)
- [Rust API Guidelines: validate arguments and return
  errors](https://rust-lang.github.io/api-guidelines/dependability.html#c-validate)
