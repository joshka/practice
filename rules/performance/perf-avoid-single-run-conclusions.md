# Perf Avoid Single Run Conclusions

## Metadata

- ID: `PERF-AVOID-SINGLE-RUN-CONCLUSIONS`
- Status: `reviewed`
- Domain: `performance`
- Depth: `compact`

## Rule

Do not decide performance from one short benchmark run.

## Why

One short benchmark run can be dominated by warmup, scheduling, cache state, background load, or
measurement noise. Landing a performance change from that evidence risks adding complexity for a
result that will not reproduce.

## Helps

- Keeps performance claims reviewable and avoids optimizing noise.

## Limits

A single run can be useful as a smoke check or exploration signal. Treat it as a prompt for better
measurement, not as landing evidence.

## Agent Instruction

Do not decide performance from one short benchmark run because one short benchmark run can be dominated
by warmup, scheduling, cache state, background load, or measurement noise.

## Mechanisms

Supported by repeated benchmark runs, Criterion reports, `hyperfine`, saved benchmark commands, and
PR notes that include baseline and changed results.

## References

- [Principle: Measure Before Optimizing](../../principles/measure-before-optimizing.md)
- [Microsoft Pragmatic Rust Guidelines: hot path
  performance](https://microsoft.github.io/rust-guidelines/agents/all.txt#M-HOTPATH)
- [Microsoft Pragmatic Rust Guidelines: throughput
  requirements](https://microsoft.github.io/rust-guidelines/agents/all.txt#M-THROUGHPUT)
