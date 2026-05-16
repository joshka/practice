# Rust Keep Lints Actionable

## Metadata

- Name: `Keep Lints Actionable`
- ID: `RUST-KEEP-LINTS-ACTIONABLE`
- Summary: Enforce lints that improve correctness, API quality, docs, portability, or maintenance
  in ways reviewers want automated. Scope suppressions tightly so exceptions stay visible.
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Keep Rust lints actionable and scoped.

## Why

Lint configuration should encode durable project policy, not a large pile of taste preferences that
developers learn to silence. A strict lint earns its place when it improves correctness, public API
quality, documentation quality, portability, or maintainability in a way reviewers want enforced
mechanically.

Suppressions are part of the same policy. An `allow` or `expect` should explain why the exception is
correct, sit at the smallest practical scope, and disappear when the exception no longer applies.

## Helps

- Helps lint failures stay meaningful and keeps suppressions from becoming invisible cleanup debt.

## Limits

Experimental or temporary lint hardening can be useful during cleanup, but do not land broad strict
lint sets as permanent policy without a clear maintenance reason.

## Agent Instruction

Enable Rust lints only for durable policy, and keep suppressions narrow with a reason.

## Mechanisms

Supported by clippy, rustdoc lints, `unexpected_cfgs`, `unused_crate_dependencies` where available,
`#[expect]`, and CI lint gates.

## References

- [Rule: RUST-ENCODE-DURABLE-RULES-IN-LINTS](rust-encode-durable-rules-in-lints.md)
- [Rule: RUST-PREFER-EXPECT-FOR-LINT-SUPPRESSIONS](rust-prefer-expect-for-lint-suppressions.md)
- [Clippy documentation](https://doc.rust-lang.org/clippy/)
