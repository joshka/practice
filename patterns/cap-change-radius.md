# Cap Change Radius

## Metadata

- Name: `Cap Change Radius`
- ID: `cap-change-radius`
- Summary: Broad diffs increase review cost and make unrelated regressions harder to isolate. Keep
  the change radius aligned with the requested behavior, using separate chunks for cleanup or
  adjacent improvements.
- Status: `reviewed`
- Audience: `both`
- Topics: `rust, refactoring, review`
- Related: `reader-locality, separate-structure-from-behavior`

## Problem

A small rule change can spread across files, call sites, tests, builders, and docs that do not own
the behavior. Reviewers then have to find the real rule change inside mechanical fallout.
When structure and behavior spread together, review becomes slower and less precise, which creates
pressure for even larger future changes.

## Preferred Move

Find the boundary that should own the rule before broadening the patch. Keep the change inside the
smallest coherent set of files, concepts, and contracts that can carry it. If a wider radius is a
real public API or compatibility cost, name that explicitly.

If the behavior change needs structural preparation, make the smallest structure-only change that
lets the behavior change read cleanly. Prefer several reviewable steps over one diff that requires
the reviewer to reconstruct which edits changed runtime behavior.
Do not reshape code for a speculative future. Stop once the next behavior change has a clear,
reviewable path.

## Tradeoff

Some changes legitimately have a large radius, especially public API changes, serialization changes,
or type changes that reveal real coupling. Do not create a central dumping ground just to reduce the
number of touched files.
Batches that are too small can waste review attention, but batches that are too large increase the
chance of conflicts, hidden behavior changes, and cleanup that is no longer serving the current
decision.

## Agent Instruction

Before editing many files for one rule, identify the owner of the rule. Keep the radius small or
explain why the wider radius is a real contract change. Separate structure-only preparation from the
behavior change when mixing them would slow or blur review.

## Examples

Bad: a validation change also renames helper functions, rewrites unrelated call sites, updates
formatting across the module, and refreshes docs that do not describe the changed contract.
Reviewers have to reconstruct which edits changed behavior and which were incidental fallout.

Good: one structure-only change moves validation into the boundary that owns it. The next change
updates the rule at that boundary, adjusts the directly affected tests, and names any public
compatibility impact explicitly.

## References

| Source                            | Use      | Note                                                         |
| --------------------------------- | -------- | ------------------------------------------------------------ |
| [Tidy First, Ch. 16][tidy-ch16]   | `adapts` | Keep structural preparation visible as its own review unit.  |
| [Tidy First, Ch. 18][tidy-ch18]   | `adapts` | Size preparation around current need and integration risk.   |
| [Fowler definition][ref]          | `adapts` | Structure-only edits should preserve observable behavior.    |

[ref]: https://martinfowler.com/bliki/DefinitionOfRefactoring.html
[tidy-ch16]: https://www.oreilly.com/library/view/tidy-first/9781098151232/ch16.html
[tidy-ch18]: https://www.oreilly.com/library/view/tidy-first/9781098151232/ch18.html
