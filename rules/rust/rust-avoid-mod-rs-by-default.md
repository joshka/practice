# Rust Avoid Mod Rs By Default

## Metadata

- ID: `RUST-AVOID-MOD-RS-BY-DEFAULT`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Avoid `mod.rs` unless there is a strong reason.

## Why

Named module root files such as `parser.rs` or `transport.rs` make editor tabs, search results, and
diffs easier to scan than many files named `mod.rs`. The file name should carry the module concept
when tooling and local convention allow it.

The Rust Reference supports both `foo.rs` and `foo/mod.rs` module source layouts. This repo prefers
named files because they make file paths and open editor tabs more descriptive, even though Ed Page
argues for `mod.rs` as a way to make split modules feel atomic. The local rule favors scanability
over that atomicity tradeoff.

## Helps

- Helps readers identify module ownership from file paths and editor labels.

## Limits

Use `mod.rs` when local convention, generated layout, edition compatibility, or tooling makes it
the clearer option. Do not churn an established crate layout just to satisfy this preference.

## Agent Instruction

Prefer named Rust module root files over `mod.rs` for module concepts that benefit from a filename.

## Mechanisms

Supported by file layout review and rustfmt-compatible module organization.

## References

- [Rust Reference: module source filenames](https://doc.rust-lang.org/reference/items/modules.html#module-source-filenames)
- [Ed Page Rust Style: Prefer `mod.rs` over `name.rs`](https://epage.github.io/dev/rust-style/#prefer-modrs-over-namers-p-mod)
- [Rule: RUST-PREFER-CONCEPT-OWNED-MODULES-AND-NAMED-FILES](rust-prefer-concept-owned-modules-and-named-files.md)
