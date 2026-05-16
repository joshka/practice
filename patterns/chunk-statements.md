# Chunk Statements

## Metadata

- Name: `Chunk Statements`
- ID: `chunk-statements`
- Summary: Dense prose asks readers to hold too many claims at once and hides which idea needs
  review. Split statements into coherent chunks so each paragraph, bullet, or sentence carries one
  inspectable purpose.
- Status: `reviewed`
- Audience: `both`
- Topics: `rust, readability, formatting`
- Related: `reader-locality, use-explaining-variable`

## Problem

A function can be short but still read as one uninterrupted wall of work. Setup, filtering,
mutation, validation, and return assembly blur together, so reviewers must simulate the whole
function line by line.

## Preferred Move

Use blank lines to separate meaningful phases: setup, decision, mutation, side effect,
verification, or return assembly.
Treat this as the smallest possible structure move: expose the shape you already had to infer before
deciding whether a stronger extraction is worthwhile.

## Tradeoff

Blank lines should reveal structure, not decorate every statement. If every paragraph needs a
heading comment, the function may need a stronger extraction or a named concept.
Chunking often exposes the next cleanup step. Stop when the current behavior change is easier; do
not follow every newly visible opportunity immediately.

## Agent Instruction

When a function is correct but hard to scan, group statements into logic paragraphs. Use whitespace
only where the reader crosses a real phase boundary.

## Examples

Bad: every phase is pressed together.

```rust
let parsed = parse_files(files)?;
let valid = parsed.into_iter().filter(|item| item.is_valid()).collect::<Vec<_>>();
let index = build_index(&valid);
Ok(Catalog { items: valid, index })
```

Good: the visual paragraphs match the workflow phases.

```rust
let parsed = parse_files(files)?;
let valid = parsed
    .into_iter()
    .filter(|item| item.is_valid())
    .collect::<Vec<_>>();

let index = build_index(&valid);

Ok(Catalog { items: valid, index })
```

## References

| Source                           | Use      | Note                                              |
| -------------------------------- | -------- | ------------------------------------------------- |
| [Tidy First, Ch. 11][tidy-ch11]  | `adapts` | Whitespace can reveal phases inside a routine.    |
| [Ed Page][ed-page]               | `adapts` | Rust style should optimize for local readability. |

[tidy-ch11]: https://www.oreilly.com/library/view/tidy-first/9781098151232/ch11.html
[ed-page]: https://epage.github.io/dev/rust-style/
