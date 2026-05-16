# Rust Use Meaningful Standard Types

## Metadata

- Name: `Use Meaningful Standard Types`
- ID: `RUST-USE-MEANINGFUL-STANDARD-TYPES`
- Summary: Prefer standard or ecosystem types that encode ownership, units, paths, durations,
  optionality, and invariants better than raw strings or integers. Use domain newtypes when the
  standard type cannot prevent meaningful mixups.
- Status: `reviewed`
- Domain: `rust`
- Tags: `rust, validation-policy, public-api, reader-locality`
- Related: `prefer-standard-conversions, make-invalid-states-hard-to-express`

## Rule

Use standard library types that carry meaning.

## Why

Standard library types such as `PathBuf`, `NonZeroUsize`, `Duration`, `Cow`, `Arc`, and `Result`
carry familiar ownership and invariant signals. Use them when they communicate the contract better
than a custom type.

## Helps

Helps encode units, ownership, paths, durations, nonzero constraints, borrowing, and optionality
directly in function signatures.

## Limits

Domain-specific newtypes are better when the standard type cannot express the invariant or when
mixing values would be dangerous.

## Agent Instruction

Use standard library types that carry meaning because standard library types such as `PathBuf`,
`NonZeroUsize`, `Duration`, `Cow`, `Arc`, and `Result` carry familiar ownership and invariant
signals.

## Mechanisms

Prefer `Path`, `Duration`, `NonZero*`, `Cow`, `OsStr`, `SocketAddr`, `Url`-like ecosystem types, and
other meaningful types over raw strings and integers.

## References

- [Rust API Guidelines: newtypes provide static
  distinctions](https://rust-lang.github.io/api-guidelines/type-safety.html#c-custom-type)
- [Rust Standard Library: std::path](https://doc.rust-lang.org/std/path/)
