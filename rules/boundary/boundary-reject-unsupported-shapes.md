# Boundary Reject Unsupported Shapes

## Metadata

- Name: `Reject Unsupported Shapes`
- ID: `BOUNDARY-REJECT-UNSUPPORTED-SHAPES`
- Summary: Fail unsupported names, values, TTLs, targets, record families, protocols, or modes at
  the boundary with clear errors. Preserve unknown data only when compatibility requires
  round-tripping and the system can do so safely.
- Status: `reviewed`
- Domain: `boundary`
- Depth: `compact`

## Rule

Reject unsupported shapes early with clear errors.

## Why

Unsupported names, values, TTLs, targets, record families, protocols, or config modes should fail at
the boundary with a clear error. Letting them pass inward creates later failures that are harder to
connect to the original input.

## Helps

- Makes unsupported behavior explicit and prevents partial internal handling of invalid shapes.

## Limits

Preserve unknown inputs when compatibility requires round-tripping. Reject inputs when the system
cannot safely preserve, ignore, or act on them.

## Agent Instruction

Reject unsupported shapes early with clear errors because unsupported names, values, TTLs, targets,
record families, protocols, or config modes should fail at the boundary with a clear error.

## Mechanisms

Supported by validation errors, capability checks, parser fixtures, schema tests, and docs that list
unsupported shapes.

## References

- [Principle: Explicit Boundaries Preserve
  Correctness](../../principles/explicit-boundaries-preserve-correctness.md)
- [Parse, don't validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)
- [Rust API Guidelines: validate arguments and return
  errors](https://rust-lang.github.io/api-guidelines/dependability.html#c-validate)
