# Rust Implement Standard Traits For Public Errors

## Metadata

- ID: `RUST-IMPLEMENT-STANDARD-TRAITS-FOR-PUBLIC-ERRORS`
- Legacy ID: `R-0202`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Implement `Debug`, `Display`, and `std::error::Error` for reusable public errors.

## Why

Public errors cross boundaries into callers, logs, tests, and user messages. Implementing `Debug`,
`Display`, and `std::error::Error` when appropriate makes errors composable and inspectable in
standard Rust workflows.

## Helps

Helps public errors work with `?`, error chains, logs, test output, and common error-reporting
libraries.

## Limits

Application-internal errors can be simpler. Public library errors should avoid losing sources or
forcing callers to parse strings.

## Agent Instruction

Implement `Debug`, `Display`, and `std::error::Error` for public errors that cross into callers,
logs, tests, and user messages.

## Mechanisms

Implement or derive `Debug`, write actionable `Display`, implement `std::error::Error`, expose
sources, and consider `thiserror` when it reduces boilerplate without hiding policy.

## References

- [Rust API Guidelines: errors implement standard
  traits](https://rust-lang.github.io/api-guidelines/interoperability.html#c-good-err)
- [Microsoft Pragmatic Rust Guidelines: canonical error
  structures](https://microsoft.github.io/rust-guidelines/guidelines/libs/ux/#M-ERRORS-CANONICAL-STRUCTS)
