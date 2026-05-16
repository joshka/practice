# Boundary Distinguish Input Classes

## Metadata

- ID: `BOUNDARY-DISTINGUISH-INPUT-CLASSES`
- Status: `reviewed`
- Domain: `boundary`
- Depth: `compact`

## Rule

Keep unknown, unsupported, denied, and preserved inputs distinct.

## Why

Unknown, unsupported, denied, and preserved inputs require different treatment. A future-compatible
unknown field may be preserved, an unsupported protocol shape should error, and denied input may
need an authorization message. Collapsing them breaks compatibility and recovery.

## Helps

- Preserves compatibility semantics and gives callers actionable errors.

## Limits

For small internal parsers, one error class may be enough. Preserve distinctions when callers,
compatibility, security, or migration behavior depends on them.

## Agent Instruction

Keep unknown, unsupported, denied, and preserved inputs distinct because each class needs different
treatment.

## Mechanisms

Supported by typed parse results, error enums, compatibility fixtures, authorization tests, and docs
that name preserved versus rejected input.

## References

- [Principle: Explicit Boundaries Preserve
  Correctness](../../principles/explicit-boundaries-preserve-correctness.md)
- [Parse, don't validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)
- [Rust API Guidelines: validate arguments and return
  errors](https://rust-lang.github.io/api-guidelines/dependability.html#c-validate)
