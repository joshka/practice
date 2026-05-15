# Rust Shape Expressions For Auditability

## Metadata

- ID: `RUST-SHAPE-EXPRESSIONS-FOR-AUDITABILITY`
- Legacy ID: `none`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Shape Rust expressions so parsing, rendering, state changes, and side effects are easy to audit.

## Why

Dense chains, side-effectful closures, and mixed pure/effect steps can hide the order and meaning of
important work. Named locals, visible branches, whitespace paragraphs, and loops for side effects
make the audit path explicit.

Ed Page's function-structure rules distinguish pure transformations from mutation and recommend
visible grouping for business logic. Rust's iterator and combinator tools are strongest when the
operation is a pure transformation; they become harder to audit when they bury policy, mutation, or
fallible side effects.

## Helps

- Helps reviewers inspect edge cases and side effects without mentally executing dense expressions.

## Limits

Iterator chains are good for clear pure transformations. Do not expand every expression when the
chain is shorter and equally obvious. Expand expressions when a reviewer needs named facts to check
parsing, rendering, policy, ownership, or side-effect order.

## Agent Instruction

Use named locals, visible branches, whitespace paragraphs, and loops for side-effectful Rust logic
when dense expressions would hide audit points.

## Mechanisms

Supported by rustfmt, clippy where useful, source review, and focused refactors before behavior
changes.

## References

- [Rule: RUST-NAME-AUDITABLE-INTERMEDIATES](rust-name-auditable-intermediates.md)
- [Ed Page Rust Style: Function structure](https://epage.github.io/dev/rust-style/#function-structure)
- [Rule: REFACTORING-PREFER-LOOPS-FOR-SIDE-EFFECTS](../refactoring/refactoring-prefer-loops-for-side-effects.md)
- [Rule: REFACTORING-USE-WHITESPACE-AS-FUNCTION-PARAGRAPHS](../refactoring/refactoring-use-whitespace-as-function-paragraphs.md)
