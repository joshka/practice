# Rust Use Field Init Shorthand

## Metadata

- Name: `Use Field Init Shorthand`
- ID: `RUST-USE-FIELD-INIT-SHORTHAND`
- Summary: Use field init shorthand when variable names already match struct fields so initialization
  stays compact and familiar. Spell fields out when renaming, conversion, or policy deserves visible
  attention.
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Use field init shorthand when it improves ordinary Rust readability.

## Why

Rust readers expect `Self { name, path, count }` when local variable names already match field
names. Repeating `name: name` adds noise without adding meaning.

The Rust Book presents field init shorthand as ordinary struct construction syntax. Use it as an
idiom, not as a clever compression trick: it works best when the local variable name already states
the field's meaning.

## Helps

- Helps struct construction stay concise and idiomatic when names already carry meaning.

## Limits

Use explicit `field: value` syntax when the value expression differs, when renaming improves
clarity, or when repeated names would hide an important conversion. Avoid renaming locals solely to
enable shorthand if the old local name carried better context.

## Agent Instruction

Use Rust field init shorthand for same-name fields unless explicit mapping clarifies conversion or
meaning.

## Mechanisms

Supported by rustfmt, clippy style lints where enabled, and source review.

## References

- [Rust Book: using field init shorthand](https://doc.rust-lang.org/book/ch05-01-defining-structs.html#using-the-field-init-shorthand)
