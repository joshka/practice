# Software Change Preferences

This guide collects broad preferences for shaping software changes. Use it when choosing the size,
structure, tests, and handoff for a change. More specific Rust, code-shape, documentation, and jj
guidance can add detail later without duplicating these defaults.

## Core Preference

Prefer changes that reduce reader burden while preserving behavior. A good change makes the
important concept, boundary, or rule easier to see from the code and easier to verify from the
handoff.

Optimize for:

- Local reasoning over distant reconstruction.
- Observable behavior over private implementation shape.
- Small reviewable chunks over broad mixed diffs.
- Explicit tradeoffs over unspoken cleverness.
- Honest verification over implied confidence.

## Change Shape

Start by identifying the smallest coherent unit that can be reviewed on its own. A chunk can be a
structure-preserving refactor, a behavior change, a documentation update, or a pattern entry, but it
should not mix unrelated decisions.

Use [Small Reviewable Chunks][small-chunks] when a change could grow into multiple review concerns.
When structure and behavior can be separated cleanly, land the structure change first and verify it
before changing behavior.
Use [Code Shape][code-shape] when the main decision is how to reduce live context, limit change
radius, preserve reversibility, or clarify cohesion and coupling.

## Local Context

Read the repo before applying general preferences. Local instructions, existing helpers, naming
schemes, tests, and version-control workflow usually contain information that a general guide cannot
know.

Use [Follow Local Conventions][local-conventions] when general guidance and project shape might
conflict. Use [Separate Discovery From Editing][discovery-editing] when the local shape is not clear
enough to edit confidently.

## Working Copy Care

Assume unowned edits belong to someone. Do not revert, rewrite, or absorb work just because it makes
the current diff look cleaner.

Use [Preserve Unowned Work][preserve-work] when a shared working copy has pre-existing edits or
changes appear while work is in progress.

## Verification

Choose verification by the risk of the change. Formatting changes need formatting checks, signature
changes need type or build checks, behavior changes need tests or smoke checks that exercise the
changed path.

Use [Smallest Trustworthy Verification][smallest-check] to choose the cheapest credible check. Use
[Report Verification Honestly][honest-verification] to distinguish what ran, what failed, and what
was not checked.

## Commit History

Commit messages and jj descriptions are part of the change. They should help future readers
understand why the change exists and what decision it captured.

Use [Commit Messages For History][commit-history] when setting jj descriptions or preparing
published commits. Follow the repository's commit convention; use Conventional Commits only where
the repo has already adopted that spec.

## Review Questions

- Does this change have one coherent purpose?
- Did it reduce what a reader must remember?
- Did it preserve behavior or name the behavior change clearly?
- Did it follow local project conventions before general preference?
- Did it avoid overwriting unowned work?
- Did verification target the likely failure?
- Does the handoff say what actually ran?

[commit-history]: ../patterns/commit-messages-for-history.md
[code-shape]: code-shape.md
[discovery-editing]: ../patterns/separate-discovery-from-editing.md
[honest-verification]: ../patterns/report-verification-honestly.md
[local-conventions]: ../patterns/follow-local-conventions.md
[preserve-work]: ../patterns/preserve-unowned-work.md
[small-chunks]: ../patterns/small-reviewable-chunks.md
[smallest-check]: ../patterns/smallest-trustworthy-verification.md
