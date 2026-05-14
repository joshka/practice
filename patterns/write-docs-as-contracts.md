# Write Docs As Contracts

## Metadata

- Name: `Write Docs As Contracts`
- ID: `write-docs-as-contracts`
- Status: `reviewed`
- Audience: `both`
- Topics: `documentation, review, drift`
- Related: `delete-redundant-comments, document-errors-panics-safety`

## Problem

Behavior, side effects, and caller obligations become harder to anticipate when they are only
discoverable by reading implementation details. A stale comment, README claim, or Rustdoc section
can also become a false contract that misleads the next maintainer.

## Preferred Move

Treat docs as part of the change surface. Capture contracts, side effects, invariants, lifecycle
rules, and non-obvious behavior where readers look for them. When behavior changes, update nearby
docs in the same review unit. When a doc contradicts the code, decide whether the doc is the
intended contract or the code is the source of truth, then fix one side deliberately.

Prefer capturing stable rationale while producing the code. A short durable note can replace
repeated rediscovery by future maintainers and agents.

## Tradeoff

Do not expand docs just because a file was touched. Add or update documentation where it prevents
rediscovery, records a contract, exposes a side effect, or makes a risky change easier to review.

## Agent Instruction

After changing behavior, scan nearby README, guide, Rustdoc, and comments for drift. Update docs
that describe the changed contract, side effect, or mental model. Report uncertainty instead of
inventing rationale.

## Examples

Bad: the behavior changes but the documented contract stays stale.

```diff
-/// Empty names are accepted and normalized later.
+/// Empty names are accepted and normalized later.
 pub fn parse_name(input: &str) -> Result<Name, NameError> {
-    Ok(Name::new(input))
+    Name::parse_non_empty(input)
 }
```

Good: the doc changes with the behavior.

```diff
-/// Empty names are accepted and normalized later.
+/// Empty names are rejected at the parse boundary.
 pub fn parse_name(input: &str) -> Result<Name, NameError> {
-    Ok(Name::new(input))
+    Name::parse_non_empty(input)
 }
```

## References

| Source                                   | Use        | Note                                                               |
| ---------------------------------------- | ---------- | ------------------------------------------------------------------ |
| [Rustdoc components][rustdoc-components] | `supports` | Public docs should describe the item in the place readers inspect. |
| [Rust API examples][rust-api-examples]   | `adapts`   | Examples and docs should communicate purpose, not just mechanics.  |

[rustdoc-components]: https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html#documenting-components
[rust-api-examples]: https://rust-lang.github.io/api-guidelines/documentation.html#c-example
