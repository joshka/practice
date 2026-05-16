# Local Reasoning And Refactoring

Refactoring rules cover local reasoning, concept helpers, visible linear stories, side-effect loops,
whitespace paragraphs, DRY pressure, and weak abstractions.

Use this index to scan the domain and jump to the rule files. The one-line summaries are
for orientation; the rule files hold the rationale, limits, mechanisms, and references.

## Rules

- [`REFACTORING-ALIGN-SEAMS-WITH-REAL-VARIATION`](refactoring-align-seams-with-real-variation.md).
  Put abstraction seams where code already varies across backends, policies, protocols, tests, or
  ownership boundaries. Avoid adding names and jumps for hypothetical futures unless the next change
  or risk clearly justifies them.
- [`REFACTORING-DO-NOT-OVER-APPLY-DRY`](refactoring-do-not-over-apply-dry.md). Keep similar-looking
  code separate until it has the same meaning and changes together. Premature sharing can couple
  unrelated policies and make later edits harder.
- [`REFACTORING-EXTRACT-CONCEPT-HELPERS`](refactoring-extract-concept-helpers.md). Extract helpers
  when the new function names a real concept boundary with a stable purpose. Hiding a few lines
  behind a weak name adds a jump without reducing the reader's burden.
- [`REFACTORING-KEEP-LINEAR-STORY-VISIBLE`](refactoring-keep-linear-story-visible.md). Keep simple
  ordered workflows inline when the sequence is the clearest explanation. Extract only the substeps
  that carry their own concept, policy, reuse, or test surface.
- [`REFACTORING-KEEP-WEAK-ABSTRACTIONS-CLOSE-TO-THEIR-USE`](refactoring-keep-weak-abstractions-close-to-their-use.md).
  Keep tentative helpers, types, or traits near their first use until the boundary proves itself.
  Local placement makes weak abstractions easier to revise, inline, or delete before other modules
  depend on them.
- [`REFACTORING-MAKE-EDGE-CASES-EXPLICIT`](refactoring-make-edge-cases-explicit.md). Name boundary
  behavior near the branch, calculation, or return that depends on it. This makes policy reviewable
  and shows when stronger types should prevent invalid states instead.
- [`REFACTORING-PREFER-LOCAL-REASONING`](refactoring-prefer-local-reasoning.md). Shape code so
  relevant state, invariants, and effects are visible near the change. Centralize only when it
  reduces total reasoning, because distant reconstruction raises cognitive load and error risk.
- [`REFACTORING-PREFER-LOOPS-FOR-SIDE-EFFECTS`](refactoring-prefer-loops-for-side-effects.md). Use
  ordinary loops when the main purpose is mutation, I/O, logging, or other side effects. Iterator
  chains are better for value transformation; using them for effects can hide order, early exits,
  and error handling.
- [`REFACTORING-USE-WHITESPACE-AS-FUNCTION-PARAGRAPHS`](refactoring-use-whitespace-as-function-paragraphs.md).
  Use blank lines to group related statements inside a function before extracting more names.
  Paragraph-like spacing can reveal the local story while avoiding unnecessary helper jumps.
