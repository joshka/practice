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

## Preferred Move

Separate behavior-preserving structure changes from behavior changes when they can be checked
independently. Land the structure change first when it makes the behavior change easier to see.

## Tradeoff

Tiny local cleanup can stay with a behavior change when splitting would add process overhead and the
cleanup is inseparable from the same lines. Do not tidy unrelated areas just because they are nearby.

## Agent Instruction

If a behavior change needs tidying, separate the behavior-preserving structure change unless the
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

| Source                | Use        | Note                                                      |
| --------------------- | ---------- | --------------------------------------------------------- |
| [Refactoring][fowler] | `supports` | Refactoring changes structure without changing behavior.  |
| [Fowler book][book]   | `supports` | The refactoring catalog centers behavior-preserving work. |
| [Tidy First][tidy]    | `adapts`   | Tidying and behavior changes are separate decisions.      |

[fowler]: https://refactoring.com/
[book]: https://martinfowler.com/books/refactoring.html
[tidy]: https://books.google.com/books/about/Tidy_First.html?id=-WndEAAAQBAJ
