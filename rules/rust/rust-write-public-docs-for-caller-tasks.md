# Rust Write Public Docs For Caller Tasks

## Metadata

- Name: `Write Public Docs For Caller Tasks`
- ID: `RUST-WRITE-PUBLIC-DOCS-FOR-CALLER-TASKS`
- Summary: Write public Rustdoc around what callers are trying to decide, do, and rely on. Start
  with concise behavior and add arguments, failures, lifecycle, features, links, or examples only
  when they help the task.
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Write public Rust docs around caller tasks.

## Why

Public Rustdoc should help a caller decide what an item is for, how to use it, and what contract it
creates. Start with a concise sentence that says what the item does or returns, then add argument,
failure, lifecycle, feature, and example details only when they help the caller's task.

Rustdoc readers often arrive from search, IDE hovers, compiler diagnostics, or a direct item link.
They may not have read the crate root first, so public docs need enough local context to stand on
their own while still linking to the broader concept when that improves auditability.

## Helps

- Helps public item docs answer caller questions without bloated reference tables or vague prose.

## Limits

Use tables when the API truly has tabular reference data, such as feature matrices, protocol fields,
or many related parameters. Do not force every short item into a full tutorial.

## Agent Instruction

Write Rustdoc for caller tasks: begin with a concise behavior sentence, use prose for arguments, and
cross-link only to improve understanding or auditability.

## Mechanisms

Supported by `cargo doc`, rustdoc link checking, doctests, API review, and rendered documentation
review.

## References

- [Rust API Guidelines: Documentation](https://rust-lang.github.io/api-guidelines/documentation.html)
- [rustdoc book: How to write documentation](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html)
- [Rule: DOCS-WRITE-FOR-NON-LINEAR-READERS](../documentation/docs-write-for-non-linear-readers.md)
