# Document Errors Panics Safety

## Metadata

- Name: `Document Errors Panics Safety`
- ID: `document-errors-panics-safety`
- Summary: Callers need to know which failures are recoverable, which conditions panic, and what
  safety obligations an API imposes. Document those contracts at the public boundary so users can
  compose the API deliberately.
- Status: `reviewed`
- Audience: `both`
- Topics: `rustdoc, errors, safety`
- Tags: `documentation, errors, security-privacy, public-api`
- Related: `preserve-error-context, write-actionable-error-messages`

## Problem

Rust APIs become harder to use safely when fallible behavior, panic conditions, or unsafe caller
obligations are only visible from implementation details. Callers need those contracts at the API
boundary. This is a specialized case of the broader rule that behavior, side effects, and caller
obligations should be documented where readers form their mental model.

## Preferred Move

Document `# Errors`, `# Panics`, and `# Safety` when those behaviors are part of the contract.
Explain the condition, consequence, and caller obligation in the section where Rust readers expect
to find it.

## Tradeoff

Do not add boilerplate sections that say nothing. Omit a section when the behavior is impossible or
irrelevant, unless explicitly saying that prevents a common misunderstanding.

## Agent Instruction

When touching a public Rust API, check whether its error, panic, or safety contract changed. Update
the corresponding Rustdoc section in the same change.

## Examples

Bad: the function is fallible, but the doc only repeats the signature.

```rust
/// Parses a pattern.
pub fn parse_pattern(input: &str) -> Result<Pattern, ParseError> {
    todo!()
}
```

Good: the doc names the failure contract.

```rust
/// Parses a pattern definition.
///
/// # Errors
///
/// Returns an error when the input is empty or contains an unknown field.
pub fn parse_pattern(input: &str) -> Result<Pattern, ParseError> {
    todo!()
}
```

## References

| Source                            | Use        | Note                                                          |
| --------------------------------- | ---------- | ------------------------------------------------------------- |
| [Rust API C-FAILURE][c-failure]   | `supports` | Public function docs should cover errors, panics, and safety. |
| [Rustdoc components][rustdoc]     | `supports` | Rustdoc examples use conventional contract sections.          |

[c-failure]: https://rust-lang.github.io/api-guidelines/documentation.html#c-failure
[rustdoc]: https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html#documenting-components
