# Boundary Separate Pure Core From Effects

## Metadata

- Name: `Separate Pure Core From Effects`
- ID: `BOUNDARY-SEPARATE-PURE-CORE-FROM-EFFECTS`
- Summary: Move domain computation away from rendering, I/O, mutation, and global state when effects
  obscure the decision being tested. The split gives tests a stable surface, but should be skipped
  when it adds indirection without a useful boundary.
- Status: `reviewed`
- Domain: `boundary`
- Tags: `boundary-correctness, side-effects, testing, reader-locality`
- Related: `make-side-effects-visible, inject-time-and-randomness, test-observable-behavior`

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
