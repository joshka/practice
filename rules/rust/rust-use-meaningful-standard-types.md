# Rust Use Meaningful Standard Types

## Metadata

- ID: `RUST-USE-MEANINGFUL-STANDARD-TYPES`
- Legacy ID: `R-0204`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

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
