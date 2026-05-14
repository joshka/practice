# Guidance Plan

This plan names the durable documentation this repo should grow into. It is greenfield: describe
the desired shape, not a comparison against prior local sources.

The center of gravity is Rust-first software-development judgment: maintainable code, trustworthy
APIs, clear docs, testable behavior, and reviewable change. Agentic workflow matters because agents
apply these rules at scale; it should serve the development principles rather than replace them as
the organizing idea.

The repo should become a practical pattern language that can be referenced in review, agent
instructions, and conversations with collaborators. Guides explain the map. Patterns carry reusable
review moves. Snippets later provide compact agent-facing excerpts.

## Guide Set

| Guide                                   | Purpose                                                      | Status   |
| --------------------------------------- | ------------------------------------------------------------ | -------- |
| `guides/rust-maintainability.md`        | Rust reader-locality, API, errors, tests, performance.       | reviewed |
| `guides/software-change-preferences.md` | Broad defaults for change shape, review, verification.       | reviewed |
| `guides/code-shape.md`                  | Small source moves that reduce reader burden.                | reviewed |
| `guides/boundary-correctness.md`        | Trust boundaries, validation, state, side effects, async.    | planned  |
| `guides/observability-and-failure.md`   | Failure visibility, logs, metrics, tracing, privacy.         | planned  |
| `guides/markdown-documentation.md`      | Markdown style, docs as contracts, Rustdoc, examples.        | reviewed |
| `guides/documentation-workflow.md`      | Choosing depth, evidence, voice, PR docs, drift remediation. | planned  |
| `guides/coding-agents.md`               | Agent objectives, context, tooling, workspaces, review.      | reviewed |
| `guides/jj-workflow.md`                 | jj changes, descriptions, bookmarks, remotes, recovery.      | reviewed |

## Pattern Families

### Rust Maintainability And Code Shape

Use this family for source-level moves that make Rust and Rust-adjacent code easier to read,
review, and change without inventing broad architecture. These patterns should be useful in other
languages, but Rust should be the reference point for examples, API tradeoffs, and naming.

Planned patterns:

- `cap-change-radius`
- `keep-structure-reversible`
- `strengthen-cohesion`
- `name-coupling`
- `untangle-before-changing`
- `use-explaining-variable`
- `use-guard-clause`
- `chunk-statements`
- `move-declaration-and-initialization-together`
- `keep-name-current`

Expected guide owner: `guides/code-shape.md`.

### Rust API And Boundary Correctness

Use this family for public APIs, internal boundaries, and workflow boundaries where raw input becomes
trusted data, lifecycle state changes, ambient dependencies become explicit, or async work crosses
ownership boundaries.

Rust examples should prefer precise types, enums, constructors, `FromStr`, `TryFrom`, owned error
types, and explicit side-effect boundaries where those concepts apply.

Planned patterns:

- `parse-dont-validate`
- `make-validation-policy-explicit`
- `make-state-transitions-explicit`
- `make-parameters-explicit`
- `inject-time-and-randomness`
- `keep-async-boundaries-explicit`

Expected guide owner: `guides/boundary-correctness.md`.

### Errors, Observability, And Failure

Use this family for behavior that callers, operators, support people, and future maintainers need to
observe when something fails or crosses a production boundary.

Rust examples should distinguish library error types from application error aggregation, and should
avoid exposing broad application errors such as `anyhow::Error` from reusable library APIs.

Planned patterns:

- `make-failures-observable`
- `contain-observability-policy`
- `log-at-owned-boundaries`
- `avoid-secret-or-private-log-context`
- `return-structured-errors`

Expected guide owner: `guides/observability-and-failure.md`.

### Documentation And Explanation

Use this family for Rustdoc, Markdown, design notes, PR narrative, and choosing how much
documentation work to do for a change.

Planned patterns:

- `label-doc-claims-by-evidence`
- `choose-doc-pass-depth`
- `preserve-local-doc-voice`
- `write-pr-narrative`
- `bootstrap-repo-docs`
- `remediate-doc-drift`

Expected guide owner: `guides/documentation-workflow.md`.

### Agent Snippets

Snippets should be compact reusable excerpts for `AGENTS.md` files. They should tell agents how to
apply the Rust-first rules, not create a separate agent-only philosophy. Snippets should link back
to guides instead of duplicating long guidance.

Planned snippets:

- `snippets/agents/core.md`
- `snippets/agents/rust.md`
- `snippets/agents/markdown-docs.md`
- `snippets/agents/coding-agents.md`
- `snippets/agents/jj.md`

## Delivery Order

1. Add the Rust Maintainability And Code Shape pattern batch.
1. Add `guides/code-shape.md`.
1. Add the Rust API And Boundary Correctness pattern batch.
1. Add `guides/boundary-correctness.md`.
1. Add the Errors, Observability, And Failure pattern batch.
1. Add `guides/observability-and-failure.md`.
1. Add the Documentation And Explanation pattern batch.
1. Add `guides/documentation-workflow.md`.
1. Add compact agent snippets.

## Acceptance Bar

Each new pattern should have:

- stable ID and human-readable name;
- `draft` status until reviewed;
- concrete problem;
- preferred move;
- tradeoff;
- compact agent instruction;
- example only when the problem is obvious from the snippet;
- durable references where they help support, adapt, or contrast the guidance.

Each new guide should:

- explain the domain map;
- link to canonical patterns instead of duplicating them;
- state review questions;
- stay concise enough to be useful from `AGENTS.md`;
- avoid local-source narration.
