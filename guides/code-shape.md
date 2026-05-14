# Code Shape

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

Use [Name Coupling][coupling] before adding a boundary: name the future edit that would force pieces
to move together. Use [Strengthen Cohesion][cohesion] when facts and behavior repeatedly change for
the same reason and need a clear owner.

## Local Expression Shape

Small local moves should reduce what the reader must remember right now. They should not become a
tour of every possible cleanup in the area.

Use [Use Guard Clause][guard] when a precondition encloses the main path. Use
[Use Explaining Variable][explaining-variable] when a local name exposes a domain fact hidden inside
an expression. Use [Chunk Statements][chunk-statements] when whitespace can reveal real phases in a
function.

Use [Move Declaration And Initialization Together][declaration-init] when a name is introduced
before it has a meaningful value. Use [Keep Name Current][name-current] when a stale name would make
future readers trust the wrong concept.

## Comments And Names

Prefer code shape that carries the ordinary meaning, and comments that preserve the context code
cannot express. After reshaping code, remove comments that only compensate for the old shape.

Use [Delete Redundant Comments][delete-comments] when a comment repeats the current code. Keep
comments that explain constraints, compatibility, safety, performance, side effects, or non-obvious
ordering.

## Review Questions

- Does this move reduce the live context a reader must hold?
- Is this structure change separate from behavior where review needs that separation?
- Is the move reversible while the design is still uncertain?
- Does this extraction name a real concept or just hide local details?
- Which future edit would make this coupling expensive?
- Did names, comments, and scopes stay current with the new shape?
- Is the change small enough to verify without trusting intent?

[change-radius]: ../patterns/cap-change-radius.md
[chunk-statements]: ../patterns/chunk-statements.md
[cohesion]: ../patterns/strengthen-cohesion.md
[coupling]: ../patterns/name-coupling.md
[declaration-init]: ../patterns/move-declaration-and-initialization-together.md
[delete-comments]: ../patterns/delete-redundant-comments.md
[explaining-variable]: ../patterns/use-explaining-variable.md
[guard]: ../patterns/use-guard-clause.md
[live-context]: ../patterns/limit-live-context.md
[name-current]: ../patterns/keep-name-current.md
[reader-locality]: ../patterns/reader-locality.md
[reversible]: ../patterns/keep-structure-reversible.md
[rust]: rust-maintainability.md
[small-chunks]: ../patterns/small-reviewable-chunks.md
[structure-behavior]: ../patterns/separate-structure-from-behavior.md
[untangle]: ../patterns/untangle-before-changing.md
