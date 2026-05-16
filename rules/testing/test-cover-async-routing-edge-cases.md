# Test Cover Async Routing Edge Cases

## Metadata

- ID: `TEST-COVER-ASYNC-ROUTING-EDGE-CASES`
- Status: `reviewed`
- Domain: `testing`
- Depth: `compact`

## Rule

Cover unrelated input, late replies, timeouts, and unmatched responses in async routing tests.

## Why

Async routing bugs often appear when replies arrive late, time out, match the wrong request, or
include unrelated input. Happy-path tests can pass while the system leaks waiters, resolves the
wrong caller, or drops important errors under concurrency.

## Helps

- Protects request/response correlation, timeout behavior, and cleanup in async systems.

## Limits

Do not make async tests depend on wall-clock luck. Prefer controlled clocks, channels, deterministic
schedulers, or small timeouts only when the test remains stable.

## Agent Instruction

Cover async routing cases for unrelated input, late replies, timeouts, unmatched responses, and
wrong-request matches.

## Mechanisms

Supported by fake clocks, controlled channels, task handles, deterministic timeout tests,
unmatched-response fixtures, and state assertions after cancellation.

## References

- [Principle: Tests Should Explain Failures](../../principles/tests-should-explain-failures.md)
- [Rust Book: writing automated tests](https://doc.rust-lang.org/book/ch11-00-testing.html)
- [Rustdoc: documentation
  tests](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html)
