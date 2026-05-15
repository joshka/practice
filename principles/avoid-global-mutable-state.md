# Avoid Global Mutable State

## Metadata

- Name: `Avoid Global Mutable State`
- ID: `avoid-global-mutable-state`
- Status: `reviewed`
- Audience: `both`
- Topics: `state, rust, lifecycle, testing`
- Related: `inject-time-and-randomness, make-state-transitions-explicit, make-side-effects-visible`

## Claim

Avoid global mutable state unless the owner, lifecycle, reset policy, and concurrency model are
explicit.

## Why I Believe This

Global mutation hides who owns a value, when it is initialized, who can change it, and what order
changes must happen in. That makes tests, concurrency, reload, shutdown, and debugging harder than
the call sites suggest. It also gives agents and reviewers fewer local facts: the important state
may be affected by code that is nowhere near the change.

The problem is not global names by themselves. Immutable constants and lookup tables can make code
clearer. The problem is ambient mutation that quietly changes behavior across calls, tests, tasks,
or threads.

## Preferred Direction

- Pass state through explicit owners.
- Put process-wide services behind handles.
- Inject clocks, randomness, configuration, clients, and environment access.
- Keep caches scoped to the owner that can invalidate or reset them.
- Model lifecycle with named start, reload, flush, close, and shutdown operations.
- Isolate unavoidable globals behind a small module with documented policy.

## Rust-Specific Guidance

`const` and immutable `static` values are usually fine. `OnceLock` and `LazyLock` are reasonable for
immutable process-wide initialization when the value does not need reset or reload. `Mutex` and
`RwLock` globals need a clear owner, lock-order story, failure policy, and test reset plan.
`thread_local!` can be useful, but it still hides context and can be surprising with async runtimes
or pooled workers.

For library crates, be especially cautious. A global cache, registry, or default client can become
a public behavior contract even if it is not exposed in the type signature.

## Good Uses

- Immutable lookup tables.
- Process metadata loaded once and never changed.
- Metrics registries with documented labels and lifecycle.
- Bounded caches with explicit invalidation and memory policy.
- Test-only fixtures guarded by reset helpers or serial execution notes.

## Bad Smells

- Tests must run serially because state leaks between cases.
- Callers cannot tell where a value comes from.
- Reload or shutdown order is unclear.
- Mutation is hidden behind convenience helpers.
- Async tasks observe surprising stale state.
- A cache can grow without an owner responsible for limits.

## Mechanisms

- Dependency injection for clocks, randomness, config, I/O, and clients.
- Owned structs and capability handles.
- Explicit reset APIs for test-only globals.
- `OnceLock` or `LazyLock` for immutable initialization.
- Clippy or custom lint policy only when it catches real project failures.

## Rules This Supports

- `BOUNDARY-MAKE-AMBIENT-INPUTS-EXPLICIT`
- `BOUNDARY-AVOID-GLOBAL-MUTABLE-STATE`
- `BOUNDARY-NAME-LIFECYCLE-TRANSITIONS`
- `BOUNDARY-IDENTIFY-ANEMIC-STATE-MACHINES`

## Agent Consequences

Do not introduce process-wide mutable state for convenience. If existing global mutation is involved
in a change, identify the owner, lifecycle, reset policy, and concurrency model before extending it.

## Limits

Some programs genuinely need process-level coordination. Use global mutable state when the global
scope is the actual domain model and when the policy is explicit enough for tests, reload, shutdown,
and concurrency review.

## References

| Source                                  | Use        | Note                                                    |
| --------------------------------------- | ---------- | ------------------------------------------------------- |
| [Microsoft avoid statics][ms-statics]   | `supports` | Static process state should be avoided or constrained.  |

[ms-statics]: https://microsoft.github.io/rust-guidelines/agents/all.txt#M-AVOID-STATICS
