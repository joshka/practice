# Boundary Identify Anemic State Machines

## Metadata

- ID: `BOUNDARY-IDENTIFY-ANEMIC-STATE-MACHINES`
- Legacy ID: `R-0307`
- Status: `reviewed`
- Domain: `boundary`
- Depth: `compact`

## Rule

Identify anemic state machines.

## Why

Auth flows, UI state, async routing, setup wizards, and lifecycle code often hide a state machine
inside booleans and scattered conditionals. Naming states and transitions exposes illegal
transitions, missing recovery paths, and duplicated policy.

## Helps

- Makes stateful behavior easier to test, extend, and reason about.

## Limits

Do not introduce a formal state machine for simple linear code. Use it when transitions, invalid
states, retries, or concurrent events are already making the code hard to follow.

## Agent Instruction

Identify anemic state machines in auth flows, UI state, async routing, setup wizards, and lifecycle
code.

## Mechanisms

Supported by enums, transition functions, state diagrams, transition table tests, and error types
for invalid transitions.

## References

- [Principle: Explicit Boundaries Preserve
  Correctness](../../principles/explicit-boundaries-preserve-correctness.md)
- [Parse, don't validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)
- [Rust API Guidelines: validate arguments and return
  errors](https://rust-lang.github.io/api-guidelines/dependability.html#c-validate)
