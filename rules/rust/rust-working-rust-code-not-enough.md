# Rust Working Rust Code Not Enough

## Metadata

- ID: `RUST-WORKING-RUST-CODE-NOT-ENOUGH`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Working Rust code is not enough.

## Why

Rust code can compile while still being hard to read, poorly documented, wrongly public,
feature-fragile, or painful for downstream users. The compiler is necessary proof, but
maintainability and API shape need human design judgment too.

## Helps

Helps review Rust changes for API clarity, docs, errors, tests, feature behavior, module shape, and
downstream compatibility instead of stopping at compilation.

## Limits

Small private scripts may only need to work. Library and long-lived application code should meet a
higher bar because future readers and users inherit the shape.

## Agent Instruction

Working Rust code is not enough because rust code can compile while still being hard to read, poorly
documented, wrongly public, feature-fragile, or painful for downstream users.

## Mechanisms

After `cargo check`, inspect public API, Rustdoc, errors, tests, feature combinations, examples,
dependency floors, and module organization for maintainability problems.

## References

- [Rust API Guidelines: public APIs are stable](https://rust-lang.github.io/api-guidelines/necessities.html#c-stable)
- [Microsoft Pragmatic Rust Guidelines: prefer simple abstractions](https://microsoft.github.io/rust-guidelines/guidelines/libs/ux/#M-SIMPLE-ABSTRACTIONS)
