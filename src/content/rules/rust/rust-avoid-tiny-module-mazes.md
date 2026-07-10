# Rust Avoid Tiny Module Mazes

## Metadata

- Name: `Avoid Tiny Module Mazes`
- ID: `RUST-AVOID-TINY-MODULE-MAZES`
- Summary: Keep small helper code near its use unless a separate module owns a real concept. This
  reduces file-jumping and preserves reader locality.
- Status: `reviewed`
- Domain: `rust`
- Tags: `rust, reader-locality, ownership, module-layout`
- Related: `reader-locality, limit-live-context, RUST-KEEP-CONCEPTS-COHERENT`

## Rule

Do not split Rust files into a maze of tiny modules.

## Why

Small modules are useful when each module owns a concept. Tiny modules that only hide a few private
helpers force readers to jump between files while holding the same local context in memory.

This is the counterweight to "split large files." Ed Page's reader-locality principle says weaker
abstractions should stay close to their use. A helper-only module is a weak abstraction unless its
name, tests, feature gate, or boundary explains why it deserves a separate place.

## Helps

- Helps keep local reasoning cheap and prevents structure from obscuring simple code.

## Limits

Split small modules when each one has a stable concept, independent tests, platform boundary,
feature gate, or public ownership reason. Do not merge modules that are already meaningful just to
reduce file count.

## Agent Instruction

Keep Rust helpers near their use unless splitting a file gives a real concept its own home.

## Mechanisms

Supported by module review, search/navigation checks, and refactors that merge helper-only modules
back into the owning file.

## References

- [Pattern: Limit Live Context](../../patterns/limit-live-context.md)
- [Ed Page Rust Style: Principles](https://epage.github.io/dev/rust-style/#principles)
- [Rule: RUST-PREFER-CONCEPT-OWNED-MODULES-AND-NAMED-FILES](rust-prefer-concept-owned-modules-and-named-files.md)
