# Local Reasoning And Refactoring

Refactoring rules cover local reasoning, concept helpers, visible linear stories, side-effect loops,
whitespace paragraphs, DRY pressure, and weak abstractions.

Use this index to scan the domain and jump to the rule files. The one-line summaries are
for orientation; the rule files hold the rationale, limits, mechanisms, and references.

## Rules

- [`REFACTORING-ALIGN-SEAMS-WITH-REAL-VARIATION`](refactoring-align-seams-with-real-variation.md).
  Align seams with real variation, not hypothetical variation. A seam is useful when the code
  actually varies there: different backends, policies, protocols, test doubles, or ownership
  boundaries. Helps: Keeps abstractions tied to observed change pressure and avoids speculative
  indirection.
- [`REFACTORING-DO-NOT-OVER-APPLY-DRY`](refactoring-do-not-over-apply-dry.md). Do not over-apply
  DRY. Two blocks that look similar may change for different reasons. Helps: Preserves useful
  duplication until the shared concept and change pattern are real.
- [`REFACTORING-EXTRACT-CONCEPT-HELPERS`](refactoring-extract-concept-helpers.md). Extract helpers
  only when they reveal a real concept boundary. A helper should reduce the reader's burden by
  naming a concept, not merely hide three lines. Helps: Improves local reasoning by replacing
  low-level steps with a meaningful name.
- [`REFACTORING-KEEP-LINEAR-STORY-VISIBLE`](refactoring-keep-linear-story-visible.md). Keep the
  whole story visible when work is linear. Some logic is easiest to understand as a straight
  narrative: read input, validate, transform, emit result. Helps: Preserves readability when the
  order of operations is the main concept.
- [`REFACTORING-KEEP-WEAK-ABSTRACTIONS-CLOSE-TO-THEIR-USE`](refactoring-keep-weak-abstractions-close-to-their-use.md).
  Keep weak abstractions close to their use. New abstractions are often tentative. Helps: Limits
  coupling from premature abstractions and keeps experiments reversible.
- [`REFACTORING-PREFER-LOCAL-REASONING`](refactoring-prefer-local-reasoning.md). Prefer local
  reasoning over distant reconstruction. Code is easier to change when the reader can see the
  relevant state, invariants, and effects nearby. Helps: Reduces cognitive load and makes behavior
  changes less error-prone.
- [`REFACTORING-PREFER-LOOPS-FOR-SIDE-EFFECTS`](refactoring-prefer-loops-for-side-effects.md).
  Prefer loops over combinators for business-logic side effects. Iterator chains are compact, but
  business-logic side effects often need named steps, early exits, logging, error handling, or
  comments. Helps: Keeps side effects and branch behavior readable in review.
- [`REFACTORING-USE-WHITESPACE-AS-FUNCTION-PARAGRAPHS`](refactoring-use-whitespace-as-function-paragraphs.md).
  Use whitespace as function paragraphs. Blank lines can show that a function has phases: gather
  inputs, validate, calculate, perform effects, return. Helps: Improves scanability without
  introducing new names or control flow.
