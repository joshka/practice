# Boundary Stage Generated Behavior

## Metadata

- Name: `Stage Generated Behavior`
- ID: `BOUNDARY-STAGE-GENERATED-BEHAVIOR`
- Summary: Validate generated, reloadable, or plugin-provided behavior in a staging path before
  promoting it over known-good behavior. Staging adds recovery cost only where runtime-loaded or
  generated artifacts can fail after deployment.
- Status: `reviewed`
- Domain: `boundary`
- Depth: `compact`

## Rule

Stage generated or reloadable behavior before promotion.

## Why

Generated, reloadable, or plugin-provided behavior can be malformed, stale, or incompatible with the
current runtime. Staging it before promotion lets the system validate, inspect, and roll back
instead of replacing known-good behavior immediately.

## Helps

- Makes dynamic behavior safer and more recoverable.

## Limits

Do not stage trivial generated artifacts that are already fully validated at build time. Stage
runtime-loaded behavior or generated code that can fail after deployment.

## Agent Instruction

Stage generated or reloadable behavior before promotion because generated, reloadable, or
plugin-provided behavior can be malformed, stale, or incompatible with the current runtime.

## Mechanisms

Supported by staging directories, validation passes, checksums, promotion markers, rollback records,
and tests for invalid generated input.

## References

- [Principle: Explicit Boundaries Preserve
  Correctness](../../principles/explicit-boundaries-preserve-correctness.md)
- [Parse, don't validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)
- [Rust API Guidelines: validate arguments and return
  errors](https://rust-lang.github.io/api-guidelines/dependability.html#c-validate)
