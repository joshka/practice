# Boundary Separate Ui And App State

## Metadata

- Name: `Separate UI And App State`
- ID: `BOUNDARY-SEPARATE-UI-AND-APP-STATE`
- Summary: Keep selection, focus, scroll, expansion, and transient input mode separate from
  application-owned data when they change under different rules. The separation prevents rendering
  concerns from mutating domain state while allowing tiny tools to stay simple until friction
  appears.
- Status: `reviewed`
- Domain: `boundary`
- Depth: `compact`

## Rule

Keep UI state separate from application-owned state.

## Why

UI state such as selection, scroll offset, focus, expanded rows, or transient input mode changes at
a different rate than application-owned data. Mixing them can make rendering events mutate domain
state or make business logic depend on viewport details.

## Helps

- Keeps UI behavior testable and prevents presentation concerns from leaking into core state.

## Limits

Small tools may keep state together until the distinction starts causing bugs or test friction.
Split when UI transitions and app invariants need different owners.

## Agent Instruction

Keep UI state separate from application-owned state because UI state such as selection, scroll offset,
focus, expanded rows, or transient input mode changes at a different rate than application-owned
data.

## Mechanisms

Supported by view-state structs, app-state models, reducer tests, rendering snapshots, and event
handlers that translate UI events into app commands.

## References

- [Principle: Explicit Boundaries Preserve
  Correctness](../../principles/explicit-boundaries-preserve-correctness.md)
- [Parse, don't validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)
- [Rust API Guidelines: validate arguments and return
  errors](https://rust-lang.github.io/api-guidelines/dependability.html#c-validate)
