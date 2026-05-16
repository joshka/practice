# Refactoring Make Edge Cases Explicit

## Metadata

- ID: `REFACTORING-MAKE-EDGE-CASES-EXPLICIT`
- Status: `reviewed`
- Domain: `refactoring`
- Depth: `compact`

## Rule

Make edge-case behavior explicit in the local control flow.

## Why

Boundary values such as empty input, zero sizes, overflow, underflow, duplicates, missing fields,
and already-complete states often decide whether a change is correct. When those cases are hidden
inside incidental arithmetic, default fallbacks, or distant helpers, reviewers have to infer policy
from mechanics.

Naming the edge case near the branch, calculation, or return makes the policy reviewable. It also
shows whether the behavior is intentional, accidental, unhandled, or better expressed by a type that
cannot represent the invalid state.

## Helps

- Makes boundary behavior visible during review.
- Reduces accidental changes to empty, zero, overflow, and already-complete cases.

## Limits

Do not add defensive branches for impossible states without first asking whether the type or parser
should make the state impossible. Keep rare edge cases local when they matter only to one operation;
promote them to a named type, constructor, or state transition when many callers need the same
policy.

## Agent Instruction

Make edge-case behavior visible near correctness-sensitive branches, calculations, or returns;
prefer stronger types for reusable invariants.

## Mechanisms

Supported by guard clauses, named local variables, explicit match arms, focused tests for boundary
values, and types or constructors that prevent invalid states from entering trusted code.

## References

- [Pattern: Reader Locality](../../patterns/reader-locality.md)
- [Pattern: Make Invalid States Hard To Express](../../patterns/make-invalid-states-hard-to-express.md)
- [Rust API Guidelines: validate arguments and return
  errors](https://rust-lang.github.io/api-guidelines/dependability.html#c-validate)
