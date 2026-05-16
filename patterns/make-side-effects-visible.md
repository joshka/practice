# Make Side Effects Visible

## Metadata

- Name: `Make Side Effects Visible`
- ID: `make-side-effects-visible`
- Summary: Callers need to know when an operation touches persistence, networks, time, global state,
  caches, metrics, processes, or other external systems. Make caller-relevant effects visible in
  names, docs, or examples without documenting implementation noise.
- Status: `reviewed`
- Audience: `both`
- Topics: `documentation, api-design, side-effects`
- Related: `write-docs-as-contracts, preserve-error-context`

## Problem

Code becomes harder to use safely when persistence, network calls, retries, time, global state,
logging, metrics, cache mutation, or external process effects are hidden behind neutral names or
undocumented APIs. Callers need to know what can happen before they compose the operation.

## Preferred Move

Make important side effects visible at the boundary. Prefer names, docs, and examples that expose
what the operation reads, writes, starts, stops, retries, persists, or sends. Put the contract where
callers make the decision to use the API.

## Tradeoff

Do not document implementation noise as a public side effect. Focus on behavior that changes caller
obligations, ordering, failure handling, observability, performance expectations, or external
systems.

## Agent Instruction

When adding or changing an API with meaningful side effects, make those effects visible in the name,
Rustdoc, README, or guide. Report which side effects are part of the caller-visible contract.

## Examples

Bad: the public doc hides persistence and observability effects.

```rust
/// Refreshes the project state.
pub fn refresh(&mut self) -> Result<(), RefreshError> {
    self.store.write_snapshot(&self.project)?;
    self.metrics.increment("project.refresh");
    Ok(())
}
```

Good: the boundary doc tells callers what the operation does outside memory.

```rust
/// Refreshes the project state and writes a new snapshot to the store.
///
/// This also emits the `project.refresh` metric after the snapshot write succeeds.
pub fn refresh(&mut self) -> Result<(), RefreshError> {
    self.store.write_snapshot(&self.project)?;
    self.metrics.increment("project.refresh");
    Ok(())
}
```

## References

| Source                        | Use        | Note                                                        |
| ----------------------------- | ---------- | ----------------------------------------------------------- |
| [Rust API C-CTOR][c-ctor]     | `adapts`   | Resource-affecting constructors should have distinct shape. |
| [Rustdoc components][rustdoc] | `supports` | Public docs are where callers inspect API behavior.         |

[c-ctor]: https://rust-lang.github.io/api-guidelines/predictability.html#c-ctor
[rustdoc]: https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html#documenting-components
