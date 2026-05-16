# Boundary Separate Pure Core From Effects

## Metadata

- ID: `BOUNDARY-SEPARATE-PURE-CORE-FROM-EFFECTS`
- Status: `reviewed`
- Domain: `boundary`
- Depth: `compact`

## Rule

Separate pure computation from rendering, I/O, or mutation when that gives tests a stable surface.

## Why

Rendering, filesystem access, network calls, terminal mutation, and global state make behavior
harder to test. Separating a pure core from effects gives tests a stable surface and lets adapters
handle side effects explicitly.

## Helps

- Improves testability and keeps domain decisions visible without running the environment.

## Limits

Do not split code when the separation adds indirection without a useful test or ownership boundary.
Use it when effects obscure the core decision.

## Agent Instruction

Separate pure computation from I/O, rendering, mutation, and global state because that gives tests a
stable behavior surface.

## Mechanisms

Supported by pure functions, command objects, adapter layers, fixtures, snapshot tests, and
integration tests for the effect boundary.

## References

- [Principle: Explicit Boundaries Preserve
  Correctness](../../principles/explicit-boundaries-preserve-correctness.md)
- [Parse, don't validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)
- [Rust API Guidelines: validate arguments and return
  errors](https://rust-lang.github.io/api-guidelines/dependability.html#c-validate)
