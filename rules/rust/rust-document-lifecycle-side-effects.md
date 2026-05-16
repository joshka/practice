# Rust Document Lifecycle Side Effects

## Metadata

- Name: `Document Lifecycle Side Effects`
- ID: `RUST-DOCUMENT-LIFECYCLE-SIDE-EFFECTS`
- Summary: Document construction, start, stop, drop, and cleanup behavior when side effects matter.
  Callers need to know when resources are acquired, released, spawned, or blocked.
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Document lifecycle and side effects for APIs that touch runtime, process, host, or UI state.

## Why

APIs that register globally, spawn tasks, mutate process state, touch the filesystem, use the
network, draw terminal UI, or manage runtime resources affect more than their return value. Callers
need startup, shutdown, cleanup, cancellation, retry, ordering, and coexistence expectations.

The Rust API Guidelines require docs to describe failure and panic behavior because those details
shape correct calling code. Lifecycle side effects shape calling code in the same way: callers need
to know whether dropping a handle shuts work down, whether a background task outlives the value,
whether retries are safe, and whether multiple instances can coexist.

## Helps

- Helps callers plan ownership, cleanup, cancellation, retries, and multiple-instance behavior.

## Limits

Simple pure value APIs do not need lifecycle sections. Add this detail when hidden effects would
change caller responsibilities. Avoid boilerplate headings when a concise sentence next to the
method docs would fully explain the lifecycle.

## Agent Instruction

Document startup, shutdown, cleanup, cancellation, ordering, and coexistence for Rust APIs with
host, process, runtime, terminal, network, or UI side effects.

## Mechanisms

Supported by Rustdoc, lifecycle examples, integration tests, and drop/cancellation tests.

## References

- [Pattern: Make Side Effects Visible](../../patterns/make-side-effects-visible.md)
- [Rust API Guidelines: Function docs include error, panic, and safety
  considerations](https://rust-lang.github.io/api-guidelines/documentation.html#c-failure)
- [Rule: RUST-DOCUMENT-SCHEDULING-FOR-LONG-ASYNC](rust-document-scheduling-for-long-async.md)
