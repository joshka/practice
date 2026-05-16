# Docs Are Contracts

## Metadata

- Name: `Docs Are Contracts`
- ID: `docs-are-contracts`
- Summary: `Documentation near code is part of the supported behavior surface. Keep prose,
  examples, and implementation aligned so humans and agents can rely on the same contract.`
- Status: `reviewed`
- Audience: `both`
- Topics: `documentation, rustdoc, agents, contracts`
- Related: `write-docs-as-contracts, remediate-doc-drift, keep-docs-near-their-subject`

## Claim

English descriptions near code are part of the system contract. They are not decoration around the
real implementation; they are a durable statement of intended behavior that code, tests, examples,
and agents can work against.

## Why I Believe This

The older objection to prose-heavy development was documentation drift. Humans wrote comments,
changed code later, and left the explanation behind. That failure mode is real, but it is no longer
the whole tradeoff. Agentic tooling makes English descriptions more valuable because agents can
implement against them, update them while changing behavior, and validate them with doctests,
examples, snapshots, and behavior tests.

Readable code still matters. The point is that some contracts are easier to state in English than
to infer from implementation shape: caller obligations, lifecycle expectations, side effects,
security boundaries, compatibility promises, and reasons for unusual tradeoffs. Hiding those
contracts inside code forces every future reader to rediscover intent.

## What This Changes

When behavior changes, nearby docs are part of the change surface. Rustdoc, README examples, guide
text, agent instructions, and comments that describe the changed contract should be updated in the
same review unit. If the docs and code disagree, decide which side represents the intended
contract, then fix the other side deliberately.

This also changes how to use agents. Do not ask agents only to write code and then hope the docs
stay true. Give agents the English contract, ask them to make implementation match it, and require
validation that exercises the documented behavior.

## Rust-Specific Guidance

Put public contracts where Rust readers look first:

- crate-level Rustdoc for crate purpose, feature shape, and primary examples;
- item Rustdoc for public types, functions, errors, panics, safety, and lifecycle;
- doctests or example crates for public usage that should stay compiling;
- README content for orientation and links, not a second drifting manual;
- module docs when a module owns a boundary, state model, or integration policy.

## Good Uses

- Document a parser's accepted and rejected input classes.
- State whether an API is additive, deprecated, experimental, or stable.
- Explain lifecycle operations such as start, reload, flush, close, and shutdown.
- Put feature-flag behavior next to the APIs or examples it affects.
- Record a side effect that callers cannot infer from a signature.

## Bad Smells

- A behavior change lands without updating Rustdoc that describes the old behavior.
- A README example compiles but no longer represents the recommended use.
- A comment says what the code does mechanically but not why the contract exists.
- A guide promises future behavior without labeling it as roadmap or design intent.
- An agent final answer relies on private session context instead of updating shared docs.

## Mechanisms

- `cargo test --doc` for Rustdoc examples.
- `cargo doc --open` for reviewing rendered docs locally.
- docs.rs-parity builds for release-facing Rustdoc.
- Markdown linting, link checks, and generated README checks where available.
- Snapshot or integration tests that compare documented behavior with observed behavior.

## Rules This Supports

- `DOCS-TREAT-DOCS-AS-CONTRACTS`
- `DOCS-STATE-CURRENT-BEHAVIOR-NOT-ASPIRATION`
- `DOCS-PROVE-REAL-USE-WITH-EXAMPLES`
- `DOCS-BUILD-DOCS-LIKE-USERS-READ-THEM`
- `DOCS-MAKE-REVIEW-EASY-TO-INSPECT`

## Agent Consequences

When changing behavior, scan nearby docs, examples, Rustdoc, and agent instructions for contract
drift. Update shared prose that describes the behavior being changed. If uncertainty remains, report
it and name the doc that needs maintainer review.

## Limits

Do not turn every implementation detail into prose. Documentation should capture stable contracts,
intent, side effects, and tradeoffs. Clearly labeled roadmap or design notes may describe future
behavior, but available behavior must not be written as aspiration.

## References

| Source                                      | Use        | Note                                                   |
| ------------------------------------------- | ---------- | ------------------------------------------------------ |
| [Rust API documentation][rust-api-docs]     | `supports` | Public Rust APIs should carry useful documentation.    |
| [Microsoft canonical docs][ms-docs]         | `supports` | Canonical docs should describe behavior intentionally. |

[rust-api-docs]: https://rust-lang.github.io/api-guidelines/documentation.html
[ms-docs]: https://microsoft.github.io/rust-guidelines/agents/all.txt#M-CANONICAL-DOCS
