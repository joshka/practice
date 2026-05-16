# Rust Make Side Effects Explicit

## Metadata

- Name: `Make Side Effects Explicit`
- ID: `RUST-MAKE-SIDE-EFFECTS-EXPLICIT`
- Summary: Put mutation, I/O, registration, cleanup, and background work in names, call sites, or
  docs when callers must account for them. Keep tiny private helpers plain when the surrounding code
  already makes the effect obvious.
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Make side effects explicit in names, call sites, and docs.

## Why

Rust's ownership model makes many data-flow effects visible, but I/O, global registration,
background tasks, process state, logging, caches, and mutation through shared handles can still be
hidden behind innocent-looking calls. Hidden effects make tests brittle and make callers guess what
can change.

The Rust API Guidelines treat error, panic, and safety behavior as function documentation concerns
because those behaviors affect caller obligations. Side effects deserve the same treatment when they
change lifecycle, cleanup, ordering, retry, or global-state responsibilities.

## Helps

- Helps callers and reviewers see mutation, I/O, registration, cleanup, and background work.

## Limits

Tiny private helpers do not need ceremonial names when the surrounding block already makes the
effect obvious. Public and boundary-crossing APIs should carry the effect in the contract. Avoid
names like `prepare` or `load` when the function actually mutates global state, starts a task, or
performs irreversible I/O.

## Agent Instruction

Expose Rust side effects in names, call sites, and Rustdoc for calls that mutate state, perform I/O,
register globally, or start background work.

## Mechanisms

Supported by Rustdoc review, behavior-oriented names, boundary tests, and API examples that show
state changes or cleanup.

## References

- [Pattern: Make Side Effects Visible](../../patterns/make-side-effects-visible.md)
- [Rust API Guidelines: Function docs include error, panic, and safety
  considerations](https://rust-lang.github.io/api-guidelines/documentation.html#c-failure)
