# Test Cover Navigation Boundaries

## Metadata

- ID: `TEST-COVER-NAVIGATION-BOUNDARIES`
- Name: `Cover Navigation Boundaries`
- Summary: Exercise first, last, empty, oversized, and repeated-navigation states in tests.
  Boundary cases catch cursor and scrolling bugs that polished manual demos often miss.
- Status: `reviewed`
- Domain: `testing`
- Tags: `testing, boundary-correctness, verification`
- Related: `boundary-treat-terminal-ui-as-product-surface, test-cover-local-logic-with-unit-tests`

## Rule

Cover navigation and scroll boundaries in tests.

## Why

Navigation and scrolling bugs usually happen at the edges: empty lists, first item, last item, small
viewport, oversized content, saturating offsets, and repeated key presses. Tests should cover those
boundaries because manual demos often miss them.

## Helps

- Prevents off-by-one and underflow behavior in terminal UI, list, cursor, and paging code.

## Limits

Do not snapshot every visual state when a smaller state assertion proves the boundary. Use snapshots
when layout or rendering is the contract.

## Agent Instruction

Cover navigation and scroll boundaries in tests because navigation and scrolling bugs usually happen
at the edges: empty lists, first item, last item, small viewport, oversized content, saturating
offsets, and repeated key presses.

## Mechanisms

Supported by boundary table tests, snapshot tests, small viewport fixtures, saturating arithmetic
checks, and event-sequence tests.

## References

- [Principle: Tests Should Explain Failures](../../principles/tests-should-explain-failures.md)
- [Rust Book: writing automated tests](https://doc.rust-lang.org/book/ch11-00-testing.html)
- [Rustdoc: documentation
  tests](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html)
