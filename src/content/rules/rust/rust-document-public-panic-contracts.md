# Rust Document Public Panic Contracts

## Metadata

- Name: `Document Public Panic Contracts`
- ID: `RUST-DOCUMENT-PUBLIC-PANIC-CONTRACTS`
- Summary: Document when public APIs can panic and what callers can do to avoid it. Panic contracts
  keep recoverable errors, invariants, and misuse boundaries explicit.
- Status: `reviewed`
- Domain: `rust`
- Tags: `rust, documentation, errors, validation-policy`
- Related: `document-errors-panics-safety, make-validation-policy-explicit`

## Rule

Document public panic contracts as precondition violations.

## Why

A public panic is a contract boundary: the caller violated a precondition or the crate has a bug.
Documenting panic conditions makes panic behavior intentional and prevents users from mistaking
hidden validation policy for ordinary errors.

## Helps

Helps callers distinguish misuse preconditions from ordinary recoverable errors and makes panic
behavior testable in public APIs.

## Limits

Private helper panics usually do not need public docs. Public panics caused by impossible internal
bugs should be fixed or converted to errors rather than documented as normal behavior.

## Agent Instruction

Document public panic contracts as precondition violations because a public panic is a contract
boundary: the caller violated a precondition or the crate has a bug.

## Mechanisms

Add `# Panics` Rustdoc sections for public functions, state preconditions plainly, prefer `Result`
for recoverable failures, and test documented panic cases when useful.

## References

- [Rust API Guidelines: functions document error, panic, and safety
  considerations](https://rust-lang.github.io/api-guidelines/documentation.html#c-failure)
- [Rustdoc: documenting
  components](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html#documenting-components)
