# Boundary Report Provider Diagnostics

## Metadata

- ID: `BOUNDARY-REPORT-PROVIDER-DIAGNOSTICS`
- Status: `reviewed`
- Domain: `boundary`
- Depth: `compact`

## Rule

Report freshness, permissions, budget, and load diagnostics from resource providers.

## Why

When data comes from a provider, callers need to know whether it is fresh, partial,
permission-limited, rate-limited, cached, or degraded. Without those diagnostics, stale or
incomplete data can look authoritative.

## Helps

- Helps users and agents interpret provider-backed results safely.

## Limits

Do not expose noisy internals that callers cannot act on. Report diagnostics that change trust,
retry, display, or support behavior.

## Agent Instruction

Report provider freshness, permissions, budget, load, cache, and degradation diagnostics so callers
know how trustworthy the data is.

## Mechanisms

Supported by freshness timestamps, permission summaries, budget fields, load status, partial-result
flags, and provider health tests.

## References

- [Principle: Explicit Boundaries Preserve
  Correctness](../../principles/explicit-boundaries-preserve-correctness.md)
- [Parse, don't validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)
- [Rust API Guidelines: validate arguments and return
  errors](https://rust-lang.github.io/api-guidelines/dependability.html#c-validate)
