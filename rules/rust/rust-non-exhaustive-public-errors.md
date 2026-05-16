# Rust Non Exhaustive Public Errors

## Metadata

- Name: `Non Exhaustive Public Errors`
- ID: `RUST-NON-EXHAUSTIVE-PUBLIC-ERRORS`
- Summary: Mark public error enums non-exhaustive unless exhaustive matching is part of the contract.
  This preserves room for future integration, validation, or provider failures without needless
  downstream breakage.
- Status: `reviewed`
- Domain: `rust`
- Tags: `rust, errors, public-api`
- Related: `rust-preserve-error-context, public-api-changes-have-downstream-cost`

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
