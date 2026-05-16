# Rust Avoid Vague Docs And Generic Examples

## Metadata

- ID: `RUST-AVOID-VAGUE-DOCS-AND-GENERIC-EXAMPLES`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Avoid vague Rustdoc and examples that only prove an item can be called.

## Why

Docs that say an item is useful, flexible, simple, or convenient do not tell callers what behavior
they can depend on. Examples that only construct a value prove syntax, not ownership, errors,
feature flags, lifecycle, or integration shape.

The Rust API Guidelines note that examples should often show why someone would use an item, not
only how to invoke it. A good crate example should therefore carry a real scenario: a fallible path,
a feature-gated integration, a conversion, a lifecycle step, or the relationship between neighboring
types.

## Helps

- Helps examples demonstrate real use and helps docs answer caller questions directly.

## Limits

Small syntax examples are fine when the syntax is the hard part. Prefer richer examples when the
API has invariants, side effects, feature gates, errors, or lifecycle behavior. Link to a richer
example instead of repeating it when duplication would drift.

## Agent Instruction

Replace vague Rustdoc and generic examples with contract details and examples that prove realistic
use.

## Mechanisms

Supported by doctests, example review, README/Rustdoc alignment checks, and documentation linting.

## References

- [Rust API Guidelines: All items have a rustdoc
  example](https://rust-lang.github.io/api-guidelines/documentation.html#c-example)
- [Rule: DOCS-PROVE-REAL-USE-WITH-EXAMPLES](../documentation/docs-prove-real-use-with-examples.md)
