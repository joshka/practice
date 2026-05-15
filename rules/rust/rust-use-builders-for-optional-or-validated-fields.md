# Rust Use Builders For Optional Or Validated Fields

## Metadata

- ID: `RUST-USE-BUILDERS-FOR-OPTIONAL-OR-VALIDATED-FIELDS`
- Legacy ID: `R-0205`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Use builders for many optional fields or cross-field validation.

## Why

Constructors with many optional arguments or cross-field validation become hard to call correctly
and hard to extend compatibly. Builders let callers name choices, preserve defaults, and delay
validation until the full configuration is known.

## Helps

Helps APIs avoid long argument lists while giving validation and cross-field defaults a named home.

## Limits

Do not add builders for simple structs or functions with a few obvious required parameters. Builders
pay off when optional fields, defaults, or validation would otherwise obscure construction.

## Agent Instruction

Use builders for many optional fields or cross-field validation because constructors with many optional
arguments or cross-field validation become hard to call correctly and hard to extend compatibly.

## Mechanisms

Use a builder type for many optional fields, cross-field validation, staged construction, or
fallible finalization. Keep required fields and defaults explicit.

## References

- [Microsoft Pragmatic Rust Guidelines: use builders for
  initialization](https://microsoft.github.io/rust-guidelines/guidelines/libs/ux/#M-INIT-BUILDER)
- [Rust API Guidelines: newtypes provide static
  distinctions](https://rust-lang.github.io/api-guidelines/type-safety.html#c-custom-type)
