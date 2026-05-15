# Rust Document Scheduling For Long Async

## Metadata

- ID: `RUST-DOCUMENT-SCHEDULING-FOR-LONG-ASYNC`
- Legacy ID: `R-0240`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Document scheduling expectations for async code that can run for a long time.

## Why

Long-running async work can starve executors, ignore cancellation, hold locks across await points,
or surprise callers with runtime assumptions. Document scheduling expectations when callers need to
know how the future behaves under load.

## Helps

Helps async callers reason about executor occupancy, cancellation, backpressure, blocking work, and
fairness.

## Limits

Short async wrappers may not need scheduling notes. Add them when work can run long, block, spawn
tasks, hold locks across await points, or require cancellation policy.

## Agent Instruction

Document scheduling expectations for async work that can starve executors, ignore cancellation, hold
locks, or rely on runtime assumptions.

## Mechanisms

Document whether the function blocks, yields, spawns, holds resources across awaits, observes
cancellation, or expects callers to use a blocking pool or timeout.

## References

- [Rust Async Book: async/await
  primer](https://rust-lang.github.io/async-book/01_getting_started/04_async_await_primer.html)
- [Rust Async Book: pinning](https://rust-lang.github.io/async-book/04_pinning/01_chapter.html)
