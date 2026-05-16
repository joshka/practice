# Rust Document Performance Contracts

## Metadata

- Name: `Document Performance Contracts`
- ID: `RUST-DOCUMENT-PERFORMANCE-CONTRACTS`
- Summary: State meaningful performance expectations when callers may design around them. Clear
  limits keep complexity and optimization claims tied to supported behavior.
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Document blocking behavior, allocation expectations, and performance constraints.

## Why

Blocking behavior, allocation expectations, buffering, clone cost, and runtime constraints can be
part of a Rust API contract. Callers need those facts when using the API in async tasks, hot paths,
terminal rendering, or resource-constrained contexts.

## Helps

Helps callers understand hidden costs such as allocation, blocking, complexity, caching, and
large-data behavior before they choose an API.

## Limits

Do not over-specify incidental implementation details. Document costs that callers reasonably depend
on or that would surprise them in normal use.

## Agent Instruction

Document blocking behavior, allocation expectations, buffering, clone cost, and runtime constraints
that callers may reasonably depend on.

## Mechanisms

Add Rustdoc notes for blocking behavior, allocation expectations, complexity, cache behavior,
streaming limits, and benchmark-backed claims where performance is part of the API.

## References

- [Rust API Guidelines: functions document error, panic, and safety
  considerations](https://rust-lang.github.io/api-guidelines/documentation.html#c-failure)
- [Microsoft Pragmatic Rust Guidelines: throughput
  requirements](https://microsoft.github.io/rust-guidelines/agents/all.txt#M-THROUGHPUT)
