# Rust Prefer Boring Direct Code

## Metadata

- Name: `Prefer Boring Direct Code`
- ID: `RUST-PREFER-BORING-DIRECT-CODE`
- Summary: Prefer explicit Rust control flow, types, and error handling over clever framework-shaped
  indirection. Use macros or abstractions when they remove real repetition or enforce real
  invariants.
- Status: `reviewed`
- Domain: `rust`
- Tags: `rust, reader-locality, reviewability`
- Related: `reader-locality, limit-live-context, refactoring-prefer-local-reasoning`

## Rule

Prefer boring direct Rust over clever framework-shaped code.

## Why

Boring Rust makes ownership, error handling, and control flow visible. Framework-shaped or clever
code can hide the simple path behind macros, callbacks, type tricks, or indirection that future
maintainers must learn before changing behavior.

## Helps

Helps maintainers and agents reason about ownership, control flow, and errors without learning an
avoidable framework-shaped abstraction first.

## Limits

Use macros, frameworks, or clever abstractions when they remove real repetition, enforce invariants,
or match established ecosystem practice better than direct code.

## Agent Instruction

Prefer boring direct Rust over clever framework-shaped code because boring Rust makes ownership, error
handling, and control flow visible.

## Mechanisms

Prefer explicit functions, structs, enums, and matches. Introduce abstraction only after the
repeated shape and its invariant are visible in working code.

## References

- [Microsoft Pragmatic Rust Guidelines: prefer simple
  abstractions](https://microsoft.github.io/rust-guidelines/guidelines/libs/ux/#M-SIMPLE-ABSTRACTIONS)
