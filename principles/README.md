# Principles

Principles are durable reasoning notes. They explain why a set of rules exists, where the rules
apply, where they stop applying, and what an agent or maintainer should do with the judgment.

Use a principle when the topic is broader than a single repeatable move. Use a pattern when the
idea has a recognizable "when you see this, do that" shape. Use a mechanism when the important
thing is a lint, formatter, command, CI check, or tool configuration.

## Reviewed Principles

- [`agent-instructions-are-operational-controls`](agent-instructions-are-operational-controls.md):
  Agent rules should shape behavior with compact trigger and purpose context, not repeat titles.
- [`avoid-global-mutable-state`](avoid-global-mutable-state.md): Global mutation hides ownership,
  lifecycle, reset, ordering, and concurrency policy.
- [`change-shape-controls-review-cost`](change-shape-controls-review-cost.md): Change boundaries
  affect review, validation, revert cost, and reviewer trust.
- [`docs-are-contracts`](docs-are-contracts.md): Documentation states behavior that humans and
  agents use as a supported contract.
- [`explicit-boundaries-preserve-correctness`](explicit-boundaries-preserve-correctness.md): Clear
  boundaries turn raw input, state, and side effects into reviewable policy.
- [`jj-topology-is-repo-role-dependent`](jj-topology-is-repo-role-dependent.md): Correct jj remote
  and bookmark behavior depends on owned, maintainer, or forked repo topology.
- [`measure-before-optimizing`](measure-before-optimizing.md): Performance changes need evidence,
  goals, comparison, and provenance before added complexity.
- [`mechanize-repeated-feedback`](mechanize-repeated-feedback.md): Repeated review feedback should
  become checks, templates, generators, lints, or reusable guides.
- [`private-context-is-not-shared-context`](private-context-is-not-shared-context.md): Shared
  artifacts must restate rationale that only existed in private sessions or local notes.
- [`public-api-changes-have-downstream-cost`](public-api-changes-have-downstream-cost.md): Public
  API changes impose downstream migration, semver, feature, and behavior costs.
- [`reader-locality-reduces-change-cost`](reader-locality-reduces-change-cost.md): Code is cheaper
  to change when readers need fewer distant facts in their head.
- [`tests-should-explain-failures`](tests-should-explain-failures.md): Tests should fail with
  information that makes the broken contract easy to diagnose.
