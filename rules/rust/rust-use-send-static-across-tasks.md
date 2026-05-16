# Rust Use Send Static Across Tasks

## Metadata

- ID: `RUST-USE-SEND-STATIC-ACROSS-TASKS`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Use `Send + 'static` errors, futures, and service handles across tasks or threads.

## Why

Values crossing task or thread boundaries often need `Send + 'static` because the executor may move
or retain them beyond the caller's stack frame. Making that requirement explicit avoids APIs that
work locally but fail in real async use.

## Helps

Helps spawned tasks and threads avoid borrowing stack-local values or non-thread-safe state that
cannot outlive the caller.

## Limits

Do not force `Send + 'static` on synchronous or single-threaded APIs that do not spawn. Overly broad
bounds can reject valid local use cases.

## Agent Instruction

Use `Send + static` bounds for values, futures, errors, and handles that cross task or thread
boundaries.

## Mechanisms

Require `Send + 'static` at spawn boundaries, move owned values into tasks, use `Arc` for shared
ownership, and document executor assumptions.

## References

- [Rust Book: Send and
  Sync](https://doc.rust-lang.org/book/ch16-04-extensible-concurrency-sync-and-send.html)
- [Tokio tutorial: spawning](https://tokio.rs/tokio/tutorial/spawning)
