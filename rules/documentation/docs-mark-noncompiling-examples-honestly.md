# Docs Mark Noncompiling Examples Honestly

## Metadata

- Name: `Mark Noncompiling Examples Honestly`
- ID: `DOCS-MARK-NONCOMPILING-EXAMPLES-HONESTLY`
- Summary: `Label examples that are sketches, partial snippets, or intentionally not run. Honest
  labels keep readers from treating illustrative code as a supported copy-paste contract.`
- Status: `reviewed`
- Domain: `documentation`
- Depth: `compact`

## Rule

Prefer examples that compile, and mark noncompiling examples honestly.

## Why

Rust examples are often copied directly into user projects or enforced as doctests. A noncompiling
snippet that looks complete wastes user time and can train agents on impossible code. If an example
is intentionally partial, it should say so through Rustdoc attributes or surrounding prose.

## Helps

- Keeps examples trustworthy and lets doctests protect public API usage where possible.

## Limits

Use noncompiling snippets for sketches, unsafe setup, external services, or omitted boilerplate when
a compiling example would obscure the point. Mark the reason honestly.

## Agent Instruction

Prefer compiling Rust examples, and mark noncompiling examples honestly because users and doctests
often copy them directly.

## Mechanisms

Supported by doctests, Rustdoc code-block attributes such as `no_run` or `ignore`, `cargo test
--doc`, and rendered-doc review.

## References

- [Principle: Docs Are Contracts](../../principles/docs-are-contracts.md)
- [Diataxis: how to use Diataxis](https://diataxis.fr/how-to-use-diataxis/)
- [Rustdoc: how to write
  documentation](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html)
