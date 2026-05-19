# Rust Name Auditable Intermediates

## Metadata

- Name: `Name Auditable Intermediates`
- ID: `RUST-NAME-AUDITABLE-INTERMEDIATES`
- Summary: Introduce named locals where parsing, validation, rendering, ownership, or side-effect
  decisions need review. Avoid naming every trivial expression when it would add ceremony without
  clarifying the boundary.
- Status: `reviewed`
- Domain: `rust`
- Tags: `rust, reader-locality, reviewability, validation-policy`
- Related: `use-explaining-variable, chunk-statements, rust-shape-expressions-for-auditability`

## Rule

Use named locals when parsing, rendering, or side effects need auditability.

## Why

Intermediate variables can make Rust code easier to audit when they name ownership, parsing,
validation, or policy decisions. A named value can show what has become trusted, cloned, normalized,
or borrowed before the next step uses it.

## Helps

Helps reviewers inspect parsing, rendering, validation, and side effects by turning dense
expressions into named facts.

## Limits

Do not name every trivial expression. Add names where they expose intent, separate failure causes,
improve diagnostics, or make a side effect boundary visible.

## Agent Instruction

Name intermediate Rust values because they expose ownership, parsing, validation, rendering, or
side-effect policy decisions.

## Mechanisms

Introduce local variables for parsed values, derived decisions, formatted output, and external
effects. Prefer names that describe the domain role rather than the operation mechanics.

## References

- [Ed Page Rust Style: names and code shape](https://epage.github.io/dev/rust-style/)
