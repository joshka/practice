# Separate Structure From Behavior

## Metadata

- Name: `Separate Structure From Behavior`
- ID: `separate-structure-from-behavior`
- Status: `reviewed`
- Audience: `both`
- Topics: `refactoring, review, workflow`
- Related: `small-reviewable-chunks, smallest-trustworthy-verification`

## Problem

A diff that mixes renames, moves, formatting, and behavior changes is harder to review and harder
to roll back. Reviewers must decide whether a line changed because the structure moved or because
the rule changed.
Behavior is visible through runtime outcomes; structure is visible through the code's relationships
and the future changes those relationships make easier.

## Preferred Move

Separate behavior-preserving structure changes from behavior changes when they can be checked
independently. Land the structure change first when it makes the behavior change easier to see.
Each switch between structural preparation and behavior work should be visible as a review boundary
when the switch is large enough to affect review.

## Tradeoff

Tiny local cleanup can stay with a behavior change when splitting would add process overhead and the
cleanup is inseparable from the same lines. Do not tidy unrelated areas just because they are nearby.
Review latency matters: fast review makes smaller structure-only changes worthwhile; slow review can
push people toward larger mixed changes unless the team deliberately protects small review units.

## Agent Instruction

If a behavior change needs cleanup, separate the behavior-preserving structure change unless the
cleanup is tiny and local. Verify each review unit independently.

## Examples

Bad: this single diff renames `active_patterns` to `visible_patterns` and also changes the rule
from "not archived" to "stable." Reviewers have to separate naming movement from behavior.

```diff
-let active_patterns = patterns.iter().filter(|pattern| !pattern.archived);
+let visible_patterns = patterns
+    .iter()
+    .filter(|pattern| pattern.status == Status::Stable);
```

Good: one review unit performs the behavior-preserving rename while keeping the old predicate.

```diff
-let active_patterns = patterns.iter().filter(|pattern| !pattern.archived);
+let visible_patterns = patterns.iter().filter(|pattern| !pattern.archived);
```

Then a separate review unit changes the behavior.

```diff
-let visible_patterns = patterns.iter().filter(|pattern| !pattern.archived);
+let visible_patterns = patterns
+    .iter()
+    .filter(|pattern| pattern.status == Status::Stable);
```

## References

| Source                          | Use        | Note                                                        |
| ------------------------------- | ---------- | ----------------------------------------------------------- |
| [Fowler definition][fowler]     | `supports` | Refactoring changes structure without changing behavior.    |
| [Fowler book][book]             | `supports` | The refactoring catalog centers behavior-preserving work.   |
| [Tidy First, Ch. 16][tidy-ch16] | `adapts`   | Split preparation from behavior when review needs it.       |
| [Tidy First, Ch. 23][tidy-ch23] | `adapts`   | Runtime outcomes and code shape carry different value.      |

[fowler]: https://martinfowler.com/bliki/DefinitionOfRefactoring.html
[book]: https://martinfowler.com/books/refactoring.html
[tidy-ch16]: https://www.oreilly.com/library/view/tidy-first/9781098151232/ch16.html
[tidy-ch23]: https://www.oreilly.com/library/view/tidy-first/9781098151232/ch23.html
