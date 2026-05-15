# Rust Non Exhaustive Public Errors

## Metadata

- ID: `RUST-NON-EXHAUSTIVE-PUBLIC-ERRORS`
- Legacy ID: `R-0216`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Use `#[non_exhaustive]` for public error enums unless exhaustive matching is intentional.

## Why

Public error enums often need new variants as integrations, validation, and provider behavior
expand. `#[non_exhaustive]` preserves room to add variants without breaking downstream exhaustive
matches unless exhaustive matching is the intended contract.

## Helps

Helps libraries add future error cases without forcing every downstream match expression to break at
the next release.

## Limits

Use exhaustive error enums when callers must handle every case and the set is genuinely closed by
the domain contract.

## Agent Instruction

Use `#[non_exhaustive]` for public error enums unless exhaustive matching is intentional; integrations,
validation, and provider behavior often add variants over time.

## Mechanisms

Add `#[non_exhaustive]` to public error enums or variants, provide accessor methods when useful, and
document how callers should handle unknown future cases.

## References

- [Rust Reference: the non_exhaustive
  attribute](https://doc.rust-lang.org/reference/attributes/type_system.html#the-non_exhaustive-attribute)
- [Cargo Book: SemVer compatibility](https://doc.rust-lang.org/cargo/reference/semver.html)
