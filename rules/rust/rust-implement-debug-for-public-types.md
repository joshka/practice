# Rust Implement Debug For Public Types

## Metadata

- ID: `RUST-IMPLEMENT-DEBUG-FOR-PUBLIC-TYPES`
- Legacy ID: `R-0217`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Implement `Debug` for public types unless that is unsafe or misleading.

## Why

`Debug` is the baseline diagnostic trait for Rust values. Public types without `Debug` make tests,
logs, assertions, and downstream debugging harder unless the type contains sensitive data or cannot
be represented safely.

## Helps

Helps downstream tests, logs, assertions, and diagnostics show useful values without bespoke
formatting.

## Limits

Avoid or customize `Debug` when it would expose secrets, huge data, unstable internals, or
misleading representations.

## Agent Instruction

Implement `Debug` for public types unless that is unsafe or misleading; `Debug` is the baseline
diagnostic trait for Rust values.

## Mechanisms

Derive `Debug` for ordinary public types, write manual implementations for redaction or stable
summaries, and include `Debug` bounds only when the API truly needs them.

## References

- [Rust API Guidelines: common traits are
  implemented](https://rust-lang.github.io/api-guidelines/interoperability.html#c-common-traits)
- [Rust API Guidelines: Debug representation is never
  empty](https://rust-lang.github.io/api-guidelines/debuggability.html#c-debug-nonempty)
