# Rust Validate Unsafe Through Safe API

## Metadata

- Name: `Validate Unsafe Through Safe API`
- ID: `RUST-VALIDATE-UNSAFE-THROUGH-SAFE-API`
- Summary: Test unsafe internals through the safe API wrapper that callers rely on. Internal unsafe
  tests and tools such as Miri should support, not replace, proof that safe calls uphold the
  contract.
- Status: `reviewed`
- Domain: `rust`
- Tags: `rust, testing, boundary-correctness, security-privacy`
- Related: `rust-contain-unsafe, rust-deny-accidental-unsafe`

## Rule

Test unsafe behavior through the safe wrapper.

## Why

Unsafe internals matter because of the safe API contract they support. Tests that only exercise
private unsafe pieces can miss whether the safe wrapper enforces preconditions, owns lifetimes, and
prevents callers from reaching invalid states.

The Pragmatic Rust safety guidance says unsafe abstractions must be minimal, testable, accompanied
by safety reasoning, and checked with tools such as Miri where practical. Testing through the safe
wrapper proves the part callers actually rely on: that safe Rust cannot trigger undefined behavior
through the exposed API.

## Helps

- Helps unsafe invariants stay connected to the public or crate-local safe contract.

## Limits

Targeted tests for unsafe internals can be useful for narrow edge cases. They should supplement,
not replace, safe-wrapper tests. If the wrapper cannot make all valid safe calls sound, expose an
unsafe API with documented caller obligations instead of pretending it is safe.

## Agent Instruction

Validate Rust unsafe code through its safe API wrapper, with internal tests only as supporting
evidence.

## Mechanisms

Supported by safety comments, safe API tests, Miri where practical, fuzzing for unsafe parsers, and
review of wrapper invariants.

## References

- [Rustonomicon](https://doc.rust-lang.org/nomicon/)
- [Microsoft Pragmatic Rust Guidelines: Safety](https://microsoft.github.io/rust-guidelines/guidelines/safety/)
- [Rule: RUST-CONTAIN-UNSAFE](rust-contain-unsafe.md)
