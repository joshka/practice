# Keep Async Boundaries Explicit

## Metadata

- Name: `Keep Async Boundaries Explicit`
- ID: `keep-async-boundaries-explicit`
- Summary: Hidden async work obscures cancellation, ordering, resource ownership, and failure
  behavior. Make task spawning, awaiting, retries, and background ownership visible at the boundary
  where callers need to reason about them.
- Status: `reviewed`
- Audience: `both`
- Topics: `rust, async, api-design`
- Related: `make-side-effects-visible, make-parameters-explicit`

## Problem

Async code hides important boundaries when locks, borrows, cancellation, retries, or I/O are spread
across `await` points without a clear owner. Callers and reviewers need to know what is held, what
can be cancelled, and what external work may already have happened.

## Preferred Move

Make async boundaries visible. Gather synchronous inputs before `await`, keep locks and temporary
borrows out of awaited regions when practical, and name operations that perform I/O, retry, spawn,
or observe cancellation.

## Tradeoff

Do not split every awaited line into a helper. Async structure should clarify ownership,
cancellation, and side effects; it should not turn a linear workflow into a maze of weak wrappers.

## Agent Instruction

When editing async Rust, identify what crosses each `await`: owned data, borrows, locks, retries,
side effects, and cancellation points. Reshape the code when an `await` hides those obligations from
the API or review.

## Examples

Bad: a mutable borrow is held while the function performs network I/O.

```rust
pub async fn refresh(project: &mut Project, client: &Client) -> Result<(), RefreshError> {
    let config = project.config_mut();
    let remote = client.fetch_config(config.remote_id()).await?;
    config.apply(remote);
    Ok(())
}
```

Good: the awaited work uses owned inputs, then the mutation resumes after the boundary.

```rust
pub async fn refresh(project: &mut Project, client: &Client) -> Result<(), RefreshError> {
    let remote_id = project.config().remote_id().to_owned();
    let remote = client.fetch_config(&remote_id).await?;

    project.config_mut().apply(remote);
    Ok(())
}
```

## References

| Source                      | Use      | Note                                                      |
| --------------------------- | -------- | --------------------------------------------------------- |
| [Async book][async-await]   | `adapts` | Async functions expose suspension points in the workflow. |
| [Rust reference][functions] | `adapts` | Async function bodies capture arguments into a future.    |

[async-await]: https://rust-lang.github.io/async-book/part-guide/async-await.html
[functions]: https://doc.rust-lang.org/reference/items/functions.html
