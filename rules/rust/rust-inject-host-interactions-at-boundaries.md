# Rust Inject Host Interactions At Boundaries

## Metadata

- ID: `RUST-INJECT-HOST-INTERACTIONS-AT-BOUNDARIES`
- Legacy ID: `none`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Make filesystem, network, time, randomness, process, and other host interactions injectable at a
boundary when tests or alternate environments need control.

## Why

Ambient host interactions make Rust code harder to test and harder to run in alternate
environments. Passing a clock, random source, process runner, filesystem adapter, or network client
at the boundary keeps the pure core deterministic.

Microsoft's Pragmatic Rust checklist calls out mockable I/O and system calls for resilience. The
important shape is not "mock everything"; it is to keep nondeterministic host behavior at the edge
so tests can exercise policy and parsing without depending on the current machine, network, clock,
or process table.

## Helps

- Helps tests control nondeterminism and keeps host effects at explicit boundaries.

## Limits

Do not over-abstract one-off private scripts. Inject host dependencies when determinism, reuse, or
alternate environments matter. Prefer concrete boundary structs or small traits over broad context
objects that hide which host capabilities a function uses.

## Agent Instruction

Inject Rust host dependencies at boundaries when tests or alternate environments need deterministic
control.

## Mechanisms

Supported by adapter traits, concrete boundary structs, test doubles, temporary directories, fake
clocks, and seeded random sources.

## References

- [Pattern: Inject Time And Randomness](../../patterns/inject-time-and-randomness.md)
- [Microsoft Pragmatic Rust Guidelines:
  Checklist](https://microsoft.github.io/rust-guidelines/guidelines/checklist/index.html)
- [Rule: BOUNDARY-MAKE-AMBIENT-INPUTS-EXPLICIT](../boundary/boundary-make-ambient-inputs-explicit.md)
