# Test Use Realistic Parser Samples

## Metadata

- ID: `TEST-USE-REALISTIC-PARSER-SAMPLES`
- Name: `Use Realistic Parser Samples`
- Summary: Test parsers with representative input, malformed cases, and safe degradation examples.
  Real samples catch compatibility failures, but fixtures should be minimized and scrubbed.
- Status: `reviewed`
- Domain: `testing`
- Tags: `testing, boundary-correctness, examples, validation-policy`
- Related: `parse-dont-validate, test-fuzz-parsers-formatters-and-state-machines`

## Rule

Use realistic samples and safe degradation cases in parser tests.

## Why

Parser tests built only from idealized examples miss real whitespace, ordering, partial data,
unknown fields, legacy formats, invalid input, and safe degradation behavior. Realistic samples keep
compatibility and error behavior grounded in the inputs users actually have.

## Helps

- Catches parsing regressions and documents how malformed or unexpected input is handled.

## Limits

Do not copy sensitive or huge production data into fixtures. Minimize realistic samples to the
fields and failure modes that matter.

## Agent Instruction

Use realistic samples and safe degradation cases in parser tests because parser tests built only from
idealized examples miss real whitespace, ordering, partial data, unknown fields, legacy formats,
invalid input, and safe degradation behavior.

## Mechanisms

Supported by curated fixtures, golden files, malformed-input cases, round-trip tests, minimized bug
samples, and compatibility fixture inventories.

## References

- [Principle: Tests Should Explain Failures](../../principles/tests-should-explain-failures.md)
- [Rust Book: writing automated tests](https://doc.rust-lang.org/book/ch11-00-testing.html)
- [Rustdoc: documentation
  tests](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html)
