# Test Fuzz Parsers Formatters And State Machines

## Metadata

- ID: `TEST-FUZZ-PARSERS-FORMATTERS-AND-STATE-MACHINES`
- Name: `Fuzz Parsers, Formatters, and State Machines`
- Summary: Use fuzzing or property tests for input-heavy parsers, formatters, and state machines.
  Large input spaces hide failures, so keep long fuzzing outside PR gates unless it is stable.
- Status: `reviewed`
- Domain: `testing`
- Depth: `compact`

## Rule

Use fuzzing or property tests for parsers, formatters, decoders, state machines, and untrusted
input.

## Why

Parsers, formatters, decoders, and state machines have large input spaces with edge cases humans
will not enumerate. Fuzzing and property tests expose panics, nontermination, invalid round trips,
and transition bugs in untrusted or highly variable input.

## Helps

- Finds edge cases beyond hand-written examples and protects input-facing code from surprising
  shapes.

## Limits

Do not put long fuzzing in required PR CI unless it is fast and deterministic. Keep seed regression
cases for failures found by fuzzing.

## Agent Instruction

Use fuzzing or property tests for parsers, formatters, decoders, state machines, and untrusted input
with large edge-case spaces.

## Mechanisms

Supported by fuzz targets, property tests, corpus fixtures, round-trip assertions, minimized
regression cases, and scheduled or release fuzzing jobs.

## References

- [Principle: Tests Should Explain Failures](../../principles/tests-should-explain-failures.md)
- [Rust Book: writing automated tests](https://doc.rust-lang.org/book/ch11-00-testing.html)
- [Rustdoc: documentation
  tests](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html)
