# Rust Keep Concepts Coherent

## Metadata

- Name: `Keep Concepts Coherent`
- ID: `RUST-KEEP-CONCEPTS-COHERENT`
- Summary: Give each module, type, or helper one recognizable idea to own. Coherent ownership keeps
  readers from carrying unrelated parsing, state, rendering, and policy facts at once.
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Keep Rust concepts coherent.

## Why

A module, type, or helper should own one recognizable idea. When unrelated parsing, state,
rendering, transport, and policy logic share a home, readers must keep too many invariants and
failure modes in mind before they can make a small change.

This adapts the Rust API Guidelines' emphasis on predictable APIs to source organization: callers
and maintainers should be able to guess where a concept lives and what neighboring code is likely to
mean. It also follows Ed Page's code-as-technical-writing framing: code structure should guide the
reader through important details instead of forcing them to reconstruct a hidden outline.

## Helps

- Helps readers find the owner of a behavior and change it without learning unrelated concepts.

## Limits

Do not split code so aggressively that the concept becomes harder to see. Small private helpers can
stay near their caller when they do not name an independent idea. Generated modules, protocol
modules, and platform modules may group code by external shape when that is the concept readers
must understand.

## Agent Instruction

Keep Rust modules, types, and helpers centered on one recognizable concept so readers can find the
owner of behavior.

## Mechanisms

Supported by module review, file naming, crate docs, and refactors that move unrelated helpers back
to their owning concept.

## References

- [Ed Page Rust Style: Principles](https://epage.github.io/dev/rust-style/#principles)
- [Rust API Guidelines: Predictability](https://rust-lang.github.io/api-guidelines/predictability.html)
- [Pattern: Strengthen Cohesion](../../patterns/strengthen-cohesion.md)
