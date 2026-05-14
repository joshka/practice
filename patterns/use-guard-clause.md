# Use Guard Clause

## Metadata

- Name: `Use Guard Clause`
- ID: `use-guard-clause`
- Status: `reviewed`
- Audience: `both`
- Topics: `rust, control-flow, readability`
- Related: `reader-locality, make-invalid-states-hard-to-express`

## Problem

The normal path becomes harder to see when it is indented under empty cases, unsupported modes, or
validation failures. Readers carry a condition while trying to understand the main behavior.
This is especially expensive when the condition gates the rest of the routine rather than a small
local branch.

## Preferred Move

Exit early for boring preconditions that are not the main story. Put guards in the order the reader
must rule them out, then leave the ordinary behavior flat and visible.

Apply this move when the conditional wraps the remainder of the routine. If only the next few lines
are conditional, extract or reshape in smaller steps before forcing a guard clause.

## Tradeoff

Too many guards can hide a missing parser or input type. Repeated validation may belong at a
construction boundary instead of at the top of every function. A long run of guards is usually a
sign that the routine has too many responsibilities or that the preconditions deserve a named type.

## Agent Instruction

Use a guard clause when an empty case, validation failure, unsupported mode, or no-op would
otherwise indent the rest of the routine. Do not manufacture guard clauses for small local branches;
reshape in smaller steps first. Keep cleanup, locks, and required side effects explicit.

## Examples

Bad: the main path is nested under the precondition.

```rust
if !input.trim().is_empty() {
    let name = PatternName::parse(input)?;
    publish(name)?;
}
```

Good: the guard gets the boring case out of the way.

```rust
if input.trim().is_empty() {
    return Err(PatternNameError::Empty);
}

let name = PatternName::parse(input)?;
publish(name)?;
```

## References

| Source                          | Use        | Note                                                       |
| ------------------------------- | ---------- | ---------------------------------------------------------- |
| [Tidy First, Ch. 1][tidy-guard] | `adapts`   | Guard early when one condition encloses the main path.     |
| [Guard Clauses][guard-clauses]  | `supports` | Flatten nested conditional paths around the main behavior. |
| [Dramatiq PR 470][dramatiq-470] | `supports` | Shows a focused guard-clause cleanup in a real change.     |

[tidy-guard]: https://www.oreilly.com/library/view/tidy-first/9781098151232/ch01.html
[guard-clauses]: https://refactoring.com/catalog/replaceNestedConditionalWithGuardClauses.html
[dramatiq-470]: https://github.com/Bogdanp/dramatiq/pull/470
