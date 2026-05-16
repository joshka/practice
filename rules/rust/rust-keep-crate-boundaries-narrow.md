# Rust Keep Crate Boundaries Narrow

## Metadata

- Name: `Keep Crate Boundaries Narrow`
- ID: `RUST-KEEP-CRATE-BOUNDARIES-NARROW`
- Summary: Put behavior and tests in the crate or module that owns them before extracting shared
  helpers. Narrow boundaries reduce dependency fan-out, feature pressure, and hidden coupling.
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Keep Rust crate boundaries and shared dependency surfaces narrow.

## Why

Every cross-crate helper, shared dependency, root facade, and crate-local utility module becomes a
coupling point. Broad core crates are especially expensive because many downstream crates inherit
their dependencies, features, MSRV pressure, and public concepts.

New code and tests should usually live in the crate or module that owns the behavior. Shared helpers
belong behind crate-local modules until there is a clear public API reason to expose them.

## Helps

- Helps workspaces avoid accidental coupling, dependency fan-out, and facade modules that hide
  ownership.

## Limits

Shared crates are useful for stable cross-cutting concepts, protocol types, or APIs intentionally
used by several crates. Keep those crates small and explicit about what they own.

## Agent Instruction

Put Rust code and tests in the owning crate or module, and expose shared helpers only for
intentional shared concepts.

## Mechanisms

Supported by workspace dependency review, crate ownership docs, public API review, and dependency
graph checks.

## References

- [Rule: RUST-AVOID-PUBLIC-DEPENDENCY-COUPLING](rust-avoid-public-dependency-coupling.md)
- [Rule: CHANGE-IDENTIFY-OWNING-MODULE-BEFORE-EDITING](../change-shape/change-identify-owning-module-before-editing.md)
