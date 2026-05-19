# Rust Avoid Overcommenting Trivial Code

## Metadata

- Name: `Avoid Overcommenting Trivial Code`
- ID: `RUST-AVOID-OVERCOMMENTING-TRIVIAL-CODE`
- Summary: Comment Rust code for invariants, contracts, and surprising tradeoffs rather than
  restating obvious operations. This keeps comments useful and less prone to drift.
- Status: `reviewed`
- Domain: `rust`
- Tags: `rust, documentation, reader-locality`
- Related: `delete-redundant-comments, document-errors-panics-safety`

## Rule

Avoid over-commenting trivial Rust code.

## Why

Comments that restate obvious assignments, matches, or function calls add maintenance cost without
adding understanding. When behavior changes, redundant comments drift and make readers wonder
whether the code or prose is authoritative.

Rust already has expressive names, types, pattern matching, and compiler-checked structure. Use
comments for information those mechanisms cannot carry well: why a surprising shape exists, what
external contract forces it, which invariant a block relies on, or why a safety argument is sound.

## Helps

- Helps comments stay reserved for invariants, non-obvious tradeoffs, safety, and contracts.

## Limits

Keep comments that explain why a shape exists, what invariant must hold, or what external behavior
requires a surprising implementation. Keep all `SAFETY:` comments required for unsafe code even
when the surrounding code looks straightforward.

## Agent Instruction

Remove Rust comments that merely restate obvious code; keep comments for invariants, tradeoffs,
contracts, and safety.

## Mechanisms

Supported by review, clippy where applicable, and targeted cleanup during refactors.

## References

- [Pattern: Delete Redundant Comments](../../patterns/delete-redundant-comments.md)
- [Rust API Guidelines: Documentation](https://rust-lang.github.io/api-guidelines/documentation.html)
