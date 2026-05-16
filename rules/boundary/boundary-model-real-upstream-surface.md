# Boundary Model Real Upstream Surface

## Metadata

- ID: `BOUNDARY-MODEL-REAL-UPSTREAM-SURFACE`
- Status: `reviewed`
- Domain: `boundary`
- Depth: `compact`

## Rule

Model each integration as the real upstream surface it exposes.

## Why

Adapters should not pretend a provider supports a cleaner or broader API than it actually does. If
the upstream exposes records, pages, eventual consistency, rate limits, or partial permissions, the
local model must either expose or deliberately handle those constraints.

## Helps

- Prevents local APIs from promising behavior the upstream cannot provide.

## Limits

A wrapper can simplify the common case, but it should still document or return clear errors for
unsupported upstream shapes.

## Agent Instruction

Model each integration as the real upstream surface it exposes because adapters should not pretend a
provider supports a cleaner or broader API than it actually does.

## Mechanisms

Supported by adapter docs, capability types, unsupported-shape errors, provider fixtures, and
integration tests against real or recorded upstream behavior.

## References

- [Principle: Explicit Boundaries Preserve
  Correctness](../../principles/explicit-boundaries-preserve-correctness.md)
- [Parse, don't validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)
- [Rust API Guidelines: validate arguments and return
  errors](https://rust-lang.github.io/api-guidelines/dependability.html#c-validate)
