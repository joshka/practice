# Use Explaining Variable

## Metadata

- Name: `Use Explaining Variable`
- ID: `use-explaining-variable`
- Status: `reviewed`
- Audience: `both`
- Topics: `rust, readability, naming`
- Related: `reader-locality, chunk-statements`

## Problem

Important decisions can disappear inside nested expressions, chained calls, or repeated boolean
conditions. The reader has to evaluate mechanics before seeing the domain fact.

## Preferred Move

Introduce a local variable when the name makes the following branch, call, or return read in domain
terms. Spend the name on the fact the reader needs, not on the syntax of the expression.
Use the name to preserve the local insight you just gained before making the behavior change.

## Tradeoff

Do not name values that are already obvious from the next line. If the same named fact appears in
several places, promote it to a real API instead of copying local variables with drifting meaning.
If the right-hand side deserves a reusable name beyond this routine, extract a helper in a separate
cleanup step instead of growing local ceremony.

## Agent Instruction

Introduce an explaining variable when a local name makes the following line easier to read. Do not
extract a helper unless the concept has meaning beyond this local use.

## Examples

Bad: the retry decision is hidden inside one condition.

```rust
if (err.is_timeout() || err.is_rate_limited()) && attempts < policy.max_attempts() {
    retry(request);
}
```

Good: local names expose the domain facts.

```rust
let retryable_error = err.is_timeout() || err.is_rate_limited();
let retry_budget_available = attempts < policy.max_attempts();

if retryable_error && retry_budget_available {
    retry(request);
}
```

## References

| Source                            | Use        | Note                                                   |
| --------------------------------- | ---------- | ------------------------------------------------------ |
| [Tidy First, Ch. 8][tidy-ch8]     | `adapts`   | Name local expressions after the intent they expose.   |
| [Extract Variable][extract-var]   | `supports` | Naming an expression can make intent easier to see.    |
| [epage][epage]                    | `adapts`   | Reader locality favors clarity at the point of use.    |

[tidy-ch8]: https://www.oreilly.com/library/view/tidy-first/9781098151232/ch08.html
[extract-var]: https://refactoring.com/catalog/extractVariable.html
[epage]: https://epage.github.io/dev/rust-style/
