# Boundary Ground Integrations In Primary Sources

## Metadata

- Name: `Ground Integrations In Primary Sources`
- ID: `BOUNDARY-GROUND-INTEGRATIONS-IN-PRIMARY-SOURCES`
- Summary: Base adapter behavior on provider docs, specs, or captured API responses before encoding
  local assumptions. When primary sources are incomplete, label observations and inferences so
  guesses do not become fake guarantees.
- Status: `reviewed`
- Domain: `boundary`
- Depth: `compact`

## Rule

Ground integration behavior in primary source documentation.

## Why

Provider and platform behavior changes, and memory of an integration is often wrong. Primary docs,
specs, or observed API responses should define the boundary contract before local wrappers encode
assumptions about names, TTLs, error codes, features, or protocol shapes.

## Helps

- Keeps adapters honest and makes integration limits reviewable.

## Limits

When primary sources are incomplete, record what is observed and label the inference. Do not present
guesses as provider guarantees.

## Agent Instruction

Ground integration behavior in primary source documentation because provider and platform behavior
changes.

## Mechanisms

Supported by source links, captured examples, integration fixtures, adapter docs, and tests that
assert documented provider behavior.

## References

- [Principle: Explicit Boundaries Preserve
  Correctness](../../principles/explicit-boundaries-preserve-correctness.md)
- [Parse, don't validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)
- [Rust API Guidelines: validate arguments and return
  errors](https://rust-lang.github.io/api-guidelines/dependability.html#c-validate)
