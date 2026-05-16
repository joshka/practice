# Rust Encode Durable Rules In Lints

## Metadata

- ID: `RUST-ENCODE-DURABLE-RULES-IN-LINTS`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Use lint configuration only for durable project rules.

## Why

Lints are useful when they encode durable project policy, not transient taste. A lint config should
prevent repeated mistakes such as accidental unsafe, stale expectations, or missing public docs
without turning every preference into CI noise.

## Helps

Helps CI enforce policies that are stable enough to automate, reducing review noise and making agent
output easier to validate mechanically.

## Limits

Avoid linting subjective taste, transient migration states, or policies that frequently need
exceptions. A noisy lint trains people and agents to ignore the signal.

## Agent Instruction

Use lint configuration for durable project policy, not transient taste or migration states that need
frequent exceptions.

## Mechanisms

Use rustfmt, clippy, rustdoc lints, deny/expect policies, cargo-deny, and repo configs for rules
that have clear mechanical checks and low false-positive rates.

## References

- [Rust Reference: lint check
  attributes](https://doc.rust-lang.org/reference/attributes/diagnostics.html#lint-check-attributes)
- [Clippy: configuration](https://doc.rust-lang.org/clippy/configuration.html)
