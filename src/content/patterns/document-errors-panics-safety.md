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

Keep the safety surfaces distinct:

- An unsafe function's `# Safety` section states every precondition the caller must establish.
- A comment on an unsafe operation explains why facts available at that operation satisfy the
  language or library contract, or links to the precise invariant owned by the surrounding type or
  module.
- A safe wrapper explains the invariant it enforces. It cannot shift an unexpressed validity or
  lifetime obligation onto safe callers.
- If a safe signature permits use that violates the proposed safety argument, document the
  unresolved soundness boundary and the narrower current-use discipline instead of presenting the
  discipline as proof.

## Tradeoff

Do not add boilerplate sections that say nothing. Omit a section when the behavior is impossible or
irrelevant, unless explicitly saying that prevents a common misunderstanding. Consolidate a safety
argument shared by many low-level helpers at the nearest stable owner; keep a local section only when
the helper adds a caller obligation or operation-specific proof.

## Agent Instruction

When touching a Rust API or unsafe operation, check whether its error, panic, caller-safety, wrapper,
or operation-level proof changed. Update the narrowest owning Rustdoc or safety comment in the same
change, and do not use current caller behavior as proof that a broader safe signature is sound.

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
