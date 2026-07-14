# Rust Agent Instructions

## Metadata

- Name: `Rust Agent Instructions`
- ID: `agent-rust-instructions`
- Summary: `Compact Rust maintainability instructions for agents working on APIs, Rustdoc, tests,
  dependencies, and reviewable implementation changes. The snippet routes agents toward reader
  locality, explicit boundaries, documented contracts, validation evidence, and pragmatic
  performance work.`
- Status: `reviewed`
- Audience: `agents`
- Topics: `rust, api-design, maintainability, validation`
- Tags: `rust, public-api, reader-locality, verification, module-layout`
- Related: `guides/rust-maintainability.md, guides/code-shape.md,
  guides/boundary-correctness.md, patterns/run-rustdoc-quality-pass.md,
  mechanisms/rust-tooling-profile.md`

Use this snippet in Rust repos where maintainability, API shape, and reviewability matter.

```markdown
## Rust Work

Follow the repo's Rust maintainability guide before introducing new abstractions. Optimize for
reader locality, clear ownership, explicit side effects, precise boundaries, and small meaningful
types and functions.

For agent efficiency, load the Rust guide or Rust rule domain first. Add `code-shape`,
`boundary-correctness`, `observability-and-failure`, or the Rustdoc quality pass only when the
change touches that concern. Do not load the full software doctrine for a routine localized Rust
edit.

Prefer boring, idiomatic Rust. Use types, constructors, enums, `FromStr`, `TryFrom`, `From`,
`AsRef`, `Borrow`, and iterator traits when they honestly express the contract. Keep visibility
narrow and avoid making dependencies part of the public surface unless that is intentional.
Prefer standard library types that carry meaning. Use builders when optional fields or cross-field
validation make constructors unclear. Avoid wrapper types that add no invariant, behavior, or
ownership clarity.

Keep modules concept-owned. Put the main concept first, keep helpers near their callers, avoid
giant crate roots, and use re-exports for discovery rather than ownership hiding.
Prefer `name.rs` over `mod.rs` unless local convention gives a strong reason otherwise. Directory
root modules and prelude modules should usually only re-export. Avoid `#[path]` except for generated
code or clear platform-layout needs. Do not default to `pub(crate)`. Use `pub` only for intentional
crate-root or public library API.
Keep code and tests inside the crate or module that owns the behavior. Avoid ad hoc modules under a
root facade. Avoid cross-crate coupling unless the coupling is the intended public API.

Prefer module-based grouped imports over one-import-per-line style. Keep private imports limited to
traits and heavily used items whose meaning remains obvious.

When changing public or reusable APIs, update nearby Rustdoc and examples in the same review unit.
Document errors, panics, safety, side effects, and compatibility when callers need that contract.
Prefer additive APIs, deprecations, and migration paths over public renames or replacements unless
the downstream break is justified and validated. Before landing a breaking public API change, look
for external users and report likely migration impact.
Document lifecycle, ownership, feature flags, platform assumptions, and cleanup behavior for APIs
that touch runtime, terminal, filesystem, network, global, background-task, or UI state.
Public errors should implement `Debug`, `Display`, and `std::error::Error` when they cross a public
or reusable boundary. Public types should implement `Debug` unless that is unsafe or leaks
confidential material. Public panics should be contract violations with documented preconditions.
For crate-level or public API documentation work, run a Rustdoc quality pass: check the crate root,
module docs, public contracts, examples, feature notes, and README/Rustdoc alignment instead of
only smoothing prose.

For async or concurrent APIs, document runtime assumptions, cancellation, backpressure, capacity,
ordering, cloneability, and producer/consumer lifetime behavior.

For fallible APIs, document whether retrying is useful, whether partial state may have changed, and
how callers recover.

Keep backend-specific adapters at the edge. Prefer backend-agnostic core types with feature-gated
adapters when event backends, terminals, networks, or runtimes vary.
Avoid global mutable state. Make filesystem, network, time, randomness, process, and other host
interactions injectable when tests or alternate environments need control.
If global mutable state is unavoidable, make the owner, lifecycle, reset policy, and concurrency
model explicit.
Model integrations as the real upstream surface they expose. Do not fake broad support. Reject
unsupported shapes early with clear errors, and document integration or protocol limits near the
adapter, tests, and public docs.
Keep unknown, unsupported, denied, and preserved inputs distinct when callers need compatibility
semantics.

Separate pure computation from rendering, I/O, and mutation when that gives tests a stable surface.
Return explicit commands or values when that is clearer than hidden state mutation.

Public examples should prove real integration shape: ownership, lifecycle, errors, feature flags,
or representative protocol input/output. Avoid examples that only show a constructor can be called.
Examples should be copy-paste friendly and should not rely on undeclared transitive dependencies.
Live-resource examples should make side effects and cleanup visible. Policy-sensitive, persistent,
external, or user-visible side effects should be gated by policy, configuration, or explicit opt-in.
For UI, parser, protocol, formatter, template, or state-machine changes, choose validation evidence
that matches the claim: doctests, snapshots, byte-level assertions, generated reference projects,
manual demos, screenshots, or focused integration tests.
Prefer tests that fail with useful diagnostic output. Compare actual values, structs, variants, or
snapshots instead of opaque booleans when there are multiple possible failure causes.
Do not optimize for performance until the changed code is shown to matter in the relevant workload.
Performance changes need a goal, baseline measurement, changed result, and tradeoff report.

For terminal UI, use stable dimensions and saturating arithmetic. Handle empty content and very
small viewports.

Use whitespace to group related logic. Keep business-logic branches visually visible. Prefer loops
over combinators when the operation has business-logic side effects.

Review snapshot updates before accepting them. For template changes, regenerate affected reference
projects and run checks against the generated output. For visible UI changes, include screenshots,
GIFs, or before/after context when useful.

Avoid lint suppressions unless they explain why the exception is correct. Never use lint allows as
cleanup by silencing.
Prefer `#[expect]` over `#[allow]` when the suppression should fail after the lint stops firing.
Keep unsafe blocks small, wrap them in safe APIs, and explain each one with a `SAFETY:` comment.

Canonical guides:

- `guides/rust-maintainability.md`
- `guides/code-shape.md`
- `guides/boundary-correctness.md`
- `guides/observability-and-failure.md`
- `patterns/run-rustdoc-quality-pass.md`
- `principles/public-api-changes-have-downstream-cost.md`
- `principles/avoid-global-mutable-state.md`
- `principles/tests-should-explain-failures.md`
- `principles/measure-before-optimizing.md`
- `mechanisms/rust-tooling-profile.md`
```
