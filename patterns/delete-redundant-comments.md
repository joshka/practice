# Delete Redundant Comments

## Metadata

- Name: `Delete Redundant Comments`
- ID: `delete-redundant-comments`
- Status: `reviewed`
- Audience: `both`
- Topics: `documentation, comments, readability`
- Related: `write-docs-as-contracts`

## Problem

Comments that restate names or ordinary control flow make files longer without reducing reader
burden. They also create drift risk because future code changes must update text that never carried
real intent.

## Preferred Move

Delete comments that only repeat the code. Keep or add comments when they explain purpose,
constraints, invariants, edge cases, side effects, or non-obvious tradeoffs.
After cleanup makes intent obvious in code, remove comments that were only compensating for the old
shape.

## Tradeoff

A simple-looking line can still deserve a comment when it encodes a compatibility rule, security
constraint, performance tradeoff, or surprising ordering requirement. Do not delete intent just
because the syntax is obvious.

## Agent Instruction

When editing comments, remove line-by-line narration and preserve comments that explain why the code
has this shape. If intent is unclear, do not invent it.

## Examples

Bad: the comment repeats the statement.

```rust
// Increment the retry count.
retry_count += 1;
```

Good: the comment explains the constraint.

```rust
// Retry once after token refresh; more attempts can replay non-idempotent requests.
retry_count += 1;
```

## References

| Source                                 | Use      | Note                                                               |
| -------------------------------------- | -------- | ------------------------------------------------------------------ |
| [Tidy First, Ch. 15][tidy-ch15]        | `adapts` | Delete comments that no longer add information beyond the code.    |
| [Rust API examples][rust-api-examples] | `adapts` | Documentation should explain purpose rather than restating syntax. |

[tidy-ch15]: https://www.oreilly.com/library/view/tidy-first/9781098151232/ch15.html
[rust-api-examples]: https://rust-lang.github.io/api-guidelines/documentation.html#c-example
