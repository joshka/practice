# Rust Keep Preludes Reexport Only

## Metadata

- Name: `Keep Preludes Re-Export Only`
- ID: `RUST-KEEP-PRELUDES-REEXPORT-ONLY`
- Summary: Put only re-exports in prelude modules and keep original behavior in its owning module.
  Users expect preludes to aid imports, not hide implementation ownership.
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Keep prelude modules re-export only.

## Why

A prelude is a convenience import surface, not an owner of behavior. Putting original logic in a
prelude makes ownership hard to discover because readers expect preludes to gather common names from
the real modules.

Ed Page's Rust style guide states this directly: preludes are import conveniences, so users do not
expect original logic there. The Rust Reference also treats preludes as names that are made
available to modules, which reinforces the idea that a project prelude is about discovery, not
ownership.

## Helps

- Helps users import common names without obscuring where those names are defined.

## Limits

Generated or compatibility preludes may need narrow glue, but that glue should still point back to
the owning modules. Keep the prelude small enough that users can predict what importing it brings
into scope.

## Agent Instruction

Keep Rust prelude modules as import surfaces that re-export owned items from their real modules.

## Mechanisms

Supported by facade review, explicit `pub use`, and source layout checks.

## References

- [Rust Reference: preludes](https://doc.rust-lang.org/reference/names/preludes.html)
- [Ed Page Rust Style: Prelude module only re-exports](https://epage.github.io/dev/rust-style/#prelude-module-only-re-exports-p-prelude-mod)
- [Rule: RUST-REEXPORT-FOR-DISCOVERY](rust-reexport-for-discovery.md)
