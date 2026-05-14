# Guidance Plan

This plan names the durable documentation this repo should grow into. It is greenfield: describe
the desired shape, not a comparison against prior local sources.

The center of gravity is Rust-first software-development judgment: maintainable code, trustworthy
APIs, clear docs, testable behavior, and reviewable change. Agentic workflow matters because agents
apply these rules at scale; it should serve the development principles rather than replace them as
the organizing idea.

The repo is becoming a practical pattern language that can be referenced in review, agent
instructions, and conversations with collaborators. Guides explain the map. Rules provide compact
instructions. Principles justify durable beliefs. Patterns carry reusable review moves. Mechanisms
capture tooling support. Snippets provide compact agent-facing excerpts.

## Guide Set

| Guide                                   | Purpose                                                      | Status   |
| --------------------------------------- | ------------------------------------------------------------ | -------- |
| `guides/rust-maintainability.md`        | Rust reader-locality, API, errors, tests, performance.       | reviewed |
| `guides/software-change-preferences.md` | Broad defaults for change shape, review, verification.       | reviewed |
| `guides/code-shape.md`                  | Small source moves that reduce reader burden.                | reviewed |
| `guides/boundary-correctness.md`        | Trust boundaries, validation, state, side effects, async.    | reviewed |
| `guides/observability-and-failure.md`   | Failure visibility, logs, metrics, tracing, privacy.         | reviewed |
| `guides/markdown-documentation.md`      | Markdown style, docs as contracts, Rustdoc, examples.        | reviewed |
| `guides/documentation-workflow.md`      | Choosing depth, evidence, voice, PR docs, drift remediation. | reviewed |
| `guides/coding-agents.md`               | Agent objectives, context, tooling, workspaces, review.      | reviewed |
| `guides/jj-workflow.md`                 | jj changes, descriptions, bookmarks, remotes, recovery.      | reviewed |

## Rule Set

Rules are grouped by the principle or judgment area that best explains why the rule exists. Public
rule IDs use uppercase, dash-separated names such as `DOCS-TREAT-DOCS-AS-CONTRACTS`. Legacy `R-*`
IDs are retained only as migration aliases in `rules/README.md`.

Expected owner: `rules/README.md`.

## Principle Set

Principles are deeper reasoning notes for accepted rules that need durable justification. They are
not all patterns. A principle can explain why a rule is worth having, what tradeoff it accepts, and
where the rule stops applying.

Reviewed principles:

- `avoid-global-mutable-state`
- `docs-are-contracts`
- `explicit-boundaries-preserve-correctness`
- `jj-topology-is-repo-role-dependent`
- `measure-before-optimizing`
- `private-context-is-not-shared-context`
- `public-api-changes-have-downstream-cost`
- `tests-should-explain-failures`

Expected owner: `principles/README.md`.

## Pattern Families

### Rust Maintainability And Code Shape

Use this family for source-level moves that make Rust and Rust-adjacent code easier to read,
review, and change without inventing broad architecture. These patterns should be useful in other
languages, but Rust should be the reference point for examples, API tradeoffs, and naming.

Reviewed patterns:

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

Reviewed patterns:

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

Reviewed patterns:

- `make-failures-observable`
- `contain-observability-policy`
- `log-at-owned-boundaries`
- `avoid-secret-or-private-log-context`
- `return-structured-errors`

Expected guide owner: `guides/observability-and-failure.md`.

### Documentation And Explanation

Use this family for Rustdoc, Markdown, design notes, PR narrative, and choosing how much
documentation work to do for a change.

Reviewed patterns:

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

Accepted snippets:

- `snippets/agents/core.md`
- `snippets/agents/rust.md`
- `snippets/agents/markdown-docs.md`
- `snippets/agents/coding-agents.md`
- `snippets/agents/jj.md`

## Mechanism Set

Mechanisms are lints, formatter settings, cargo commands, CI checks, jj defaults, local agent
configuration, templates, and generated artifacts that make preferred behavior easier.

Reviewed mechanisms:

- `mechanisms/rust-tooling-profile.md`

## Remaining Work

The first reviewed guide, pattern, and snippet set is in place. Useful next work includes:

- Add an external references ledger if source tracking becomes too scattered across pattern files.
- Distill reviewed principles into shorter agent and maintainer profiles.
- Split additional tooling profiles out of the Rust tooling profile when repeated use proves a
  narrower profile is useful.
- Extract more examples from real review comments when a pattern needs sharper recognition.
- Add project-specific snippet variants only after copy/paste use exposes repeated adaptation work.

## Completed Delivery Order

1. Add the Rust Maintainability And Code Shape pattern batch.
1. Add `guides/code-shape.md`.
1. Add the Rust API And Boundary Correctness pattern batch.
1. Add `guides/boundary-correctness.md`.
1. Add the Errors, Observability, And Failure pattern batch.
1. Add `guides/observability-and-failure.md`.
1. Add the Documentation And Explanation pattern batch.
1. Add `guides/documentation-workflow.md`.
1. Add compact agent snippets.
1. Add the first principle expansion layer.
1. Add the first mechanism profile.

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

Each new principle should:

- state the claim directly;
- explain why the belief exists;
- name good uses, bad smells, mechanisms, and limits where relevant;
- link the rules it supports;
- include agent consequences;
- use references only where they help support or contrast the principle.

Each new mechanism should:

- name the rules or principles it supports;
- include concrete command or configuration shapes where stable;
- explain what the mechanism catches and what it cannot catch;
- avoid heavy checks in the normal edit loop unless their cost is justified.

Each new guide should:

- explain the domain map;
- link to canonical patterns instead of duplicating them;
- state review questions;
- stay concise enough to be useful from `AGENTS.md`;
- avoid local-source narration.
