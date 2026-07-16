# Code Shape

## Metadata

- Name: `Code Shape`
- ID: `code-shape`
- Summary: Code-shape guidance covers small source-level moves that reduce live context, improve
  reader locality, and keep structure changes reviewable. It focuses on local expression shape,
  cohesion, coupling, reversible structure, and separating behavior from preparation.
- Status: `reviewed`
- Audience: `both`
- Topics: `rust, refactoring, reader-locality, cohesion, review`
- Tags: `reader-locality, refactoring, change-shape, reviewability`
- Related: `reader-locality-reduces-change-cost, reader-locality, separate-structure-from-behavior,
  source-coherence-review`

This guide collects preferences for small source-level moves that make Rust and Rust-adjacent code
easier to read, review, and change. Use it with [Rust Maintainability][rust], not instead of it.

Code shape is about the amount of context a maintainer must hold while changing code. Good shape
does not merely reduce line count or add layers; it makes the relevant facts, relationships, and
change boundaries easier to see.

## Core Preference

Prefer code that keeps the active context small. A reader should be able to inspect a block, helper,
type, or module and know which earlier facts can still affect it.

Use [Limit Live Context][live-context] when a long method or module makes every earlier variable,
flag, calculation, or side effect feel potentially relevant to later code. Use
[Reader Locality][reader-locality] when movement or extraction would force more jumps instead of
reducing the reader's working set.

## Reviewable Structure

Separate preparation from behavior when mixing them would blur review. Structural work is easiest to
trust when it is behavior-preserving, small enough to verify, and clearly aimed at the next change.

Use [Separate Structure From Behavior][structure-behavior] when renames, moves, formatting, or
extractions can be reviewed independently. Use [Cap Change Radius][change-radius] when one rule
starts spreading across files that do not own it. Use [Small Reviewable Chunks][small-chunks] when
the change needs to be split around review decisions.

## Reversible Moves

Prefer reversible structure while evidence is forming. A private helper, local rename, narrowed
scope, or grouped block can be backed out cheaply; a public API, serialization shape, or service
boundary usually cannot.

Use [Keep Structure Reversible][reversible] before creating a durable contract. Use
[Untangle Before Changing][untangle] when the first exploratory pass discovers the structure the
behavior change needed, but leaves a tangled diff behind.

## Cohesion And Coupling

Move code toward the concept that explains why it changes. Do not split or merge code only because a
file is long, a module is small, or an abstraction looks tidy.

### Ownership

- Group code by responsibility, not incidental reuse.
- Keep related behavior together so features are understandable without excessive file-hopping.
- Keep boundaries narrow and explicit.
- Separate responsibilities only when doing so improves clarity.
- Let change patterns guide structure.

### Abstraction Pressure

- Use one level of abstraction per function when practical.
- Prefer local reasoning over indirection.
- Extract helpers only when they reveal a real concept boundary.
- Start with concrete code and let abstractions emerge from real pressure.
- Avoid abstractions thinner than the code they hide.
- Align seams with real variation, not hypothetical variation.
- Do not over-apply DRY.

### Reader Context

- Make data flow and state changes visible.
- Preserve the reader's mental stack.
- Keep the whole story visible when work is linear.

Use [Name Coupling][coupling] before adding a boundary: name the future edit that would force pieces
to move together. Use [Strengthen Cohesion][cohesion] when facts and behavior repeatedly change for
the same reason and need a clear owner. Use [Align Seams With Real Variation][real-variation],
[Do Not Over Apply DRY][dry], [Keep Weak Abstractions Close To Their Use][weak-abstractions], and
[Prefer Local Reasoning][local-reasoning] when abstraction pressure is the main source of shape
risk. Use [Keep Linear Story Visible][linear-story] when extraction would hide the flow a reader
needs to audit.

Use [Source Coherence Review][source-coherence] when the ownership problem spans a module or feature.
Inventory named declarations separately from behavior, then map both lists in both directions. The
pass distinguishes missing owners from names that add navigation without owning behavior.

## Local Expression Shape

Small local moves should reduce what the reader must remember right now. They should not become a
tour of every possible cleanup in the area.

### Function Paragraphs

- Use whitespace to group related logic. Those groups are the paragraphs of a function.
- Open a group that incrementally builds state with the state being built.
- Prefer early returns for non-business bookkeeping.

### Branches And Effects

- Prefer `if`, `else`, and `match` when mutually exclusive business paths are the domain rule a
  reader should see.
- Do not mix side-effect statements and pure expressions in the same logical step.
- Prefer loops over combinators when the body performs business-logic side effects.

Use [Prefer Loops For Side Effects][side-effect-loops] when iterator chains make effects, ordering,
or early exits harder to audit.

### Pure Policy And Edge Cases

- Put calculation-heavy policy into a small pure layer when rendering, I/O, or mutation would
  otherwise hide the rule being tested.
- Keep rendering as a translation of already-computed state when that makes the behavior easier to
  verify.
- Make edge-case behavior explicit for zero-sized, empty, overflow, underflow, and already-complete
  states.

Use [Use Guard Clause][guard] when a precondition encloses the main path. Use
[Use Explaining Variable][explaining-variable] when a local name exposes a domain fact hidden inside
an expression. Use [Chunk Statements][chunk-statements] when whitespace can reveal real phases in a
function.

Use [Move Declaration And Initialization Together][declaration-init] when a name is introduced
before it has a meaningful value. Use [Keep Name Current][name-current] when a stale name would make
future readers trust the wrong concept. Use [Separate Pure Core From Effects][pure-core] when
rendering, I/O, or mutation hides the rule being tested, and use [Make Edge Cases
Explicit][edge-cases] when boundary values should be visible in the local control flow.

## Comments And Names

Prefer code shape that carries the ordinary meaning, and comments that preserve the context code
cannot express. After reshaping code, remove comments that only compensate for the old shape.

If an explanation repeatedly depends on a domain noun that cannot be pointed to in the source, test
whether the source is missing a concept. The smallest useful name may be a local, function, enum,
type, or module. Keep one-off intermediates direct when naming them more durably would not protect an
invariant, own policy, or reduce the reader's live context.

Use [Delete Redundant Comments][delete-comments] when a comment repeats the current code. Keep
comments that explain constraints, compatibility, safety, performance, side effects, or non-obvious
ordering.

## Related Guidance

Use [Local Reasoning And Refactoring Rules][refactoring-rules] for compact source-shape
instructions. Use [Reader Locality Reduces Change Cost][reader-locality-principle] for the deeper
reasoning behind live context, helper extraction, and local reasoning. Use
[Change Shape Rules][change-rules] when a source move affects review boundaries or should be split
from behavior. Use [Source Coherence Review][source-coherence] for the declaration-outline and
behavior-mapping workflow behind a substantial ownership review.

## Review Questions

### Change Shape

- Does this move reduce the live context a reader must hold?
- Is this structure change separate from behavior where review needs that separation?
- Is the move reversible while the design is still uncertain?

### Concepts And Boundaries

- Does this extraction name a real concept or just hide local details?
- Is this boundary aligned with real variation or only incidental reuse?
- Is the whole story still visible when the work is linear?
- Which future edit would make this coupling expensive?
- Did names, comments, and scopes stay current with the new shape?

### Source Model

- Can each important behavior point to one named owner or deliberate coordinator?
- Can each durable source name point back to behavior, an invariant, or reader burden it removes?
- Does repeated explanatory vocabulary reveal a missing concept or only one-off linear work?
- Does apparent module size come from mixed implementation or from focused docs and colocated tests?

### Local Behavior

- Is pure policy separated from rendering or I/O where that makes the rule easier to test?
- Are edge cases visible instead of incidental?
- Do visual groups reveal the function's real phases?
- Are side effects visible instead of hidden in pure-looking expressions or combinators?
- Is the change small enough to verify without trusting intent?

[change-radius]: ../patterns/cap-change-radius.md
[chunk-statements]: ../patterns/chunk-statements.md
[change-rules]: ../rules/change-shape/README.md
[cohesion]: ../patterns/strengthen-cohesion.md
[coupling]: ../patterns/name-coupling.md
[declaration-init]: ../patterns/move-declaration-and-initialization-together.md
[delete-comments]: ../patterns/delete-redundant-comments.md
[edge-cases]: ../rules/refactoring/refactoring-make-edge-cases-explicit.md
[explaining-variable]: ../patterns/use-explaining-variable.md
[guard]: ../patterns/use-guard-clause.md
[dry]: ../rules/refactoring/refactoring-do-not-over-apply-dry.md
[live-context]: ../patterns/limit-live-context.md
[linear-story]: ../rules/refactoring/refactoring-keep-linear-story-visible.md
[local-reasoning]: ../rules/refactoring/refactoring-prefer-local-reasoning.md
[name-current]: ../patterns/keep-name-current.md
[pure-core]: ../rules/boundary/boundary-separate-pure-core-from-effects.md
[reader-locality]: ../patterns/reader-locality.md
[reader-locality-principle]: ../principles/reader-locality-reduces-change-cost.md
[real-variation]: ../rules/refactoring/refactoring-align-seams-with-real-variation.md
[refactoring-rules]: ../rules/refactoring/README.md
[reversible]: ../patterns/keep-structure-reversible.md
[rust]: rust-maintainability.md
[side-effect-loops]: ../rules/refactoring/refactoring-prefer-loops-for-side-effects.md
[small-chunks]: ../patterns/small-reviewable-chunks.md
[source-coherence]: ../mechanisms/source-coherence-review.md
[structure-behavior]: ../patterns/separate-structure-from-behavior.md
[untangle]: ../patterns/untangle-before-changing.md
[weak-abstractions]: ../rules/refactoring/refactoring-keep-weak-abstractions-close-to-their-use.md
