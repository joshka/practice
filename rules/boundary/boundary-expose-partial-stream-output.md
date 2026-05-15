# Boundary Expose Partial Stream Output

## Metadata

- ID: `BOUNDARY-EXPOSE-PARTIAL-STREAM-OUTPUT`
- Legacy ID: `R-0321`
- Status: `reviewed`
- Domain: `boundary`
- Depth: `compact`

## Rule

Expose partial provider-stream output without making it authoritative too early.

## Why

Provider streams often deliver partial tokens, chunks, or events before the final authoritative
result. Treating partial output as final can corrupt state; hiding it entirely can make
cancellation, progress, and debugging poor.

## Helps

- Supports progress and diagnostics while keeping final state promotion explicit.

## Limits

Do not expose partial data as if it has passed final validation. Mark it as provisional until
completion, cancellation, or failure policy resolves it.

## Agent Instruction

Expose partial provider-stream output without making it authoritative before the final result
arrives.

## Mechanisms

Supported by stream event types, provisional buffers, completion markers, cancellation tests, and UI
states that distinguish partial from final output.

## References

- [Principle: Explicit Boundaries Preserve
  Correctness](../../principles/explicit-boundaries-preserve-correctness.md)
- [Parse, don't validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)
- [Rust API Guidelines: validate arguments and return
  errors](https://rust-lang.github.io/api-guidelines/dependability.html#c-validate)
