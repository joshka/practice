# Untangle Before Changing

## Metadata

- Name: `Untangle Before Changing`
- ID: `untangle-before-changing`
- Summary: Behavior changes become risky when policy, formatting, validation, persistence, and side
  effects are braided together. Untangle only enough structure to give the new behavior a clear
  owner, then keep the behavior change reviewable.
- Status: `reviewed`
- Audience: `both`
- Topics: `rust, refactoring, workflow`
- Tags: `change-shape, reader-locality, reviewability`
- Related: `separate-structure-from-behavior, cap-change-radius`

## Problem

A behavior change becomes risky when formatting, validation, persistence, side effects, and domain
policy are braided together. The intended rule has no clear place to land.
The first pass often teaches the real shape of both the behavior change and the cleanup it needed,
leaving a working but tangled diff.

## Preferred Move

Untangle only enough structure to give the behavior change an owner. Move rendering away from
policy, parsing away from use, or side effects away from pure decisions, then make the behavior
change in a separate reviewable unit when practical.

If the exploratory pass produced a knot of structure and behavior, prefer rebuilding the coherent
sequence over shipping the knot. Keep passing tests and notes as evidence, but do not let sunk cost
make an incoherent review unit look acceptable.

## Tradeoff

Do not turn untangling into broad cleanup. Move the knot that blocks the current change; leave
unrelated architecture for a later chunk.
Untangling can cost more than the original change. If the behavior fix is urgent, small, and already
safe to review, ship it and record the structural follow-up instead.

## Agent Instruction

Before making a risky behavior change in tangled code, create the smallest structure that gives the
change a clear owner. If discovery creates a tangled work-in-progress, preserve the learned tests
and facts, then rebuild the change as a clearer sequence.

## Examples

Bad: changing publish policy also requires editing response rendering.

```rust
let label = if pattern.examples().is_empty() {
    "missing examples"
} else {
    "ready to publish"
};
```

Good: policy and rendering have separate owners.

```rust
let decision = publish_policy.evaluate(pattern);
let label = render_publish_decision(decision);
```

## References

| Source                          | Use      | Note                                                       |
| ------------------------------- | -------- | ---------------------------------------------------------- |
| [Tidy First, Ch. 20][tidy-ch20] | `adapts` | Rebuild a tangled discovery pass into a coherent sequence. |
| [Tidy First, Ch. 21][tidy-ch21] | `adapts` | Choose cleanup timing by cost, confidence, and reuse.      |
| [Fowler definition][ref]        | `adapts` | Structure-only edits should preserve observable behavior.  |

[ref]: https://martinfowler.com/bliki/DefinitionOfRefactoring.html
[tidy-ch20]: https://www.oreilly.com/library/view/tidy-first/9781098151232/ch20.html
[tidy-ch21]: https://www.oreilly.com/library/view/tidy-first/9781098151232/ch21.html
