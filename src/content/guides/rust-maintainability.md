# Rust Maintainability

## Metadata

- Name: `Rust Maintainability`
- ID: `rust-maintainability`
- Summary: Rust maintainability guidance applies the repo's software-change preferences to Rust
  code, APIs, modules, errors, tests, dependencies, documentation, and release risk. It favors Rust
  that is easy to read locally, hard to misuse, and honest about public behavior.
- Status: `reviewed`
- Audience: `both`
- Topics: `rust, api, modules, errors, testing, dependencies, release`
- Tags: `rust, public-api, reader-locality, testing, dependencies, release`
- Related: `reader-locality-reduces-change-cost, public-api-changes-have-downstream-cost,
  rust-api-and-release-checks`

This guide applies the repo's software-change preferences to Rust code. Prefer Rust that is easy to
read locally, hard to misuse, and honest about behavior, performance, and error boundaries.

Use this guide with [Software Change Preferences](software-change-preferences.md) and
[Code Shape](code-shape.md), not instead of them.

## Core Preference

Prefer reader-first Rust that still respects ownership, performance, and API compatibility. A Rust
change is better when it reduces the number of concepts, fields, lifetimes, jumps, and hidden
invariants a maintainer must hold at once.

Use [Reader Locality][reader-locality] when extraction, module movement, or helper placement affects
how much context a reader must reconstruct.
Use [Code Shape][code-shape] when the change is primarily about live context, extraction,
structure/behavior separation, reversible structure, cohesion, coupling, naming, or local
expression shape.

## Rust Review Checklist

Use this checklist to review Rust changes without flattening every preference into a separate
reviewed rule file. Some checklist items already have durable rule pages in
[Rust API And Crate Shape Rules](../rules/rust/README.md); other items are narrower prompts that
should stay here until they prove reusable enough to promote.

### Core Maintainability

- [Working code is not enough][rule-working-code]; the crate should be easy to understand, audit,
  extend, and use.
- [Prefer obvious, boring, well-factored code][rule-boring-code] over clever abstraction.
- [Prefer direct implementation code over framework-shaped code][rule-boring-code] until the
  framework pays for itself.
- [Keep concepts coherent][rule-coherent-concepts].
- [A module should own one recognizable idea][rule-coherent-concepts].
- [Do not use a module as a bucket for loosely related helpers][rule-coherent-concepts].
- [Prefer small functions with meaningful names][rule-small-shapes].
- [Prefer narrow structs that own one coherent concept][rule-small-shapes].
- [Prefer simple enums for commands and state transitions][rule-small-shapes].
- [Prefer named locals][rule-auditable-intermediates] when parsing, rendering, or side effects need
  auditability.
- [Avoid broad context objects][rule-context-callbacks].
- [Avoid callback-heavy control flow][rule-context-callbacks].
- [Avoid wrappers that exist only to hide one line of code][rule-empty-wrappers].
- [Make side effects explicit in names, call sites, and docs][rule-explicit-effects].
- [Avoid vague docs][rule-vague-docs].
- [Avoid generic examples][rule-vague-docs].
- [Avoid unnecessary wrappers][rule-empty-wrappers].
- [Avoid over-commenting trivial code][rule-overcommenting].
- [Avoid broad modules][rule-coherent-concepts].
- [Avoid examples that only prove a function can be called][rule-vague-docs].

### Public API Shape

- [Keep public API shape intentional][rule-api-shape].
- [Do not preserve accidental development-era compatibility in pre-release
  crates][rule-pre-release-compat].
- [Every public item should have a clear owning module][rule-visibility-ownership].
- [Public error enums should be `#[non_exhaustive]`][rule-non-exhaustive-errors] unless exhaustive
  matching is intentional.
- [Error types should implement `Debug`, `Display`, and `std::error::Error`][rule-error-traits]
  when they cross a public or reusable boundary.
- [Error `Display` output should be human-oriented and actionable][rule-error-display].
- [Do not format errors with `Debug`][rule-error-display] in their `Display` implementation.
- [Public types should implement `Debug`][rule-debug-public-types] unless doing so is unsafe,
  misleading, or exposes confidential material.
- [Public APIs should not leak dependency types][rule-public-dependency-coupling] unless dependency
  integration is the point of the API.
- [Panics in public APIs should represent contract violations][rule-panic-contracts], not ordinary
  fallible conditions.
- [Document exact panic preconditions][rule-panic-contracts] when a public API can panic.
- [Use `debug_assert!` for internal invariants][rule-debug-assert] that should be checked during
  development without becoming ordinary runtime error handling.
- [Prefer inherent constructors or trait implementations][rule-constructors] for construction.
- [Prefer regular functions over associated functions][rule-incidental-functions] when the type name
  is incidental to the operation.
- [Use builders][rule-builders] when many optional fields or cross-field validation would make
  constructors hard to read.
- Builder [`build` methods should validate cross-field invariants][rule-builder-validation] and
  return errors when construction can fail.

### Crate Roots, Modules, And Re-exports

- [Avoid giant crate roots][rule-giant-roots].
- [The crate root should teach the crate][rule-teach-crate-root].
- [The crate root should expose the primary path][rule-primary-crate-path].
- [The crate root should point to deeper modules][rule-primary-crate-path].
- Public facade crates should [re-export intentionally][rule-reexport-discovery].
- [Avoid glob re-exports in public facades][rule-glob-reexports].
- [Use `#[doc(inline)]`][rule-doc-inline] when a re-export is the canonical path readers should
  land on.
- [Put the main concept first][rule-central-item-first].
- [Reading order should follow execution order or conceptual dependency order][rule-reading-order].
- [Keep helpers near the code that uses them][rule-tiny-module-mazes] unless they are independently
  important concepts.
- [Prefer caller-before-callee order][rule-order-items] when it improves top-to-bottom reading.
- [Avoid `mod.rs` unless there is a strong reason][rule-mod-rs].
- [Prefer feature-oriented modules and named files][rule-concept-modules].
- [Prefer `name.rs` over `mod.rs`][rule-mod-rs] for module roots unless local convention or tooling
  gives a strong reason otherwise.
- [Directory-root modules should usually act as tables of contents][rule-directory-tocs].
- [Directory-root modules should usually re-export child modules][rule-directory-tocs] rather than
  own original logic.
- [Prelude modules should only re-export][rule-prelude-reexports].
- [Avoid `#[path]`][rule-path-attribute] unless generated code or platform layout makes it the
  clearest option.
- [The public API should be browseable from the file layout][rule-browseable-layout].
- [Avoid inline modules][rule-inline-modules] except for tests, preludes, and generated code.
- [Do not split files into a maze of tiny modules][rule-tiny-module-mazes].
- [Do not default to `pub(crate)`][rule-pub-crate].
- [Use `pub` only for intentional crate-root or public library API][rule-visibility-ownership].
- [When an item becomes visible outside its module][rule-visibility-ownership], its name and docs
  should make ownership obvious.

### Rustdoc And Written API Contracts

- [Treat Rustdoc as part of the API, not decoration][rule-rustdoc-contract].
- [Start public item docs with a concise sentence][rule-public-docs] that says what the item does or
  returns.
- [Prefer prose for argument docs][rule-public-docs]; avoid parameter tables unless the API truly
  needs tabular reference.
- [Write docs for non-linear readers][rule-public-docs].
- [Someone may land on any module, type, example, or guide first][rule-public-docs].
- [Cross-link docs when links improve auditability][rule-public-docs].
- [Document planned behavior as current scope or future work][rule-current-behavior].
- [Do not describe unimplemented behavior as available API][rule-current-behavior].
- [Run a bounded Rustdoc quality pass][rustdoc-pass] when crate-root teaching, item contracts,
  example placement, and README/Rustdoc/example alignment need to be checked together.
- [Compare nearby crates accurately and charitably][rule-crate-comparisons].
- [Explain fit, scope, and tradeoffs][rule-crate-comparisons] instead of claiming universal
  superiority.
- [Prefer direct ownership and boundary statements][rule-public-docs] over apologetic design
  justifications.
- [Markdown docs should hold material][rule-markdown-purpose] that does not fit in Rustdoc or
  README.

### Tests And Evidence

- [Tests should prove contracts, not implementation trivia][rule-test-contracts].
- [Tests should prove user-visible contracts and local invariants][rule-test-contracts].
- [Good tests make the maintenance question obvious][rule-test-contracts].
- [A reader should be able to tell what a user or future maintainer would
  notice][rule-test-contracts] if the behavior broke.
- [Unit tests should cover local logic][rule-unit-tests].
- [Co-locate unit tests with the module behavior they prove][rule-unit-tests].
- [Integration tests should cover public behavior across module boundaries][rule-integration-tests].
- [Use integration tests when a unit test would hide the boundary being
  exercised][rule-integration-tests].
- [Doctests should cover public examples][rule-doctests] that can compile without fragile
  environment assumptions.
- [Bug fixes should include regression tests][rule-regression-tests] unless the issue explains why
  that is impractical.
- [Test error behavior, invalid input, cancellation, drop, cleanup, and boundary
  conditions][rule-test-evidence-surface].
- [Prefer deterministic tests][rule-deterministic-tests] over tests that depend on timing or
  external state.
- [Terminal behavior needs deterministic fixtures or testkit support][rule-deterministic-tests]
  before claims are broadened.
- [Parser tests should use realistic samples][rule-parser-samples].
- [Parser tests should cover recognized shapes and safe degradation][rule-parser-samples].
- [Parser tests should not be broader than the parser's real contract][rule-parser-samples].
- [Parser recovery tests should cover malformed, truncated, unsupported, and mixed
  input][rule-parser-samples] when those cases are part of the contract.
- [Navigation and scroll tests should cover boundary behavior][rule-navigation-tests].
- [Command construction tests should prove both construction and display behavior][rule-command-tests].
- [Policy tests should cover allowed, denied, redacted, and fallback behavior][rule-policy-tests]
  when policy affects output.
- [Query, request, or correlation tests should cover unrelated input, late replies, timeouts, and
  unmatched responses][rule-async-routing-tests] when the API routes asynchronous replies.
- [Drift tests should keep support claims, fixtures, docs, examples, and API paths
  aligned][rule-drift-tests] when the project has a registry or coverage inventory.
- [Conversion and default tests should cover invariants][rule-test-evidence-surface] encoded by
  coordinate, mode, selector, ID, or protocol value types.
- [Avoid tests that require a real external repository, service, or terminal][rule-host-injection]
  unless the behavior cannot be validated another way.
- [Prefer behavior-oriented test names][rule-test-names].
- [Avoid test names that only repeat the function under test][rule-test-names].
- [Use fuzzing or property tests][rule-fuzz-tests] for parsers, formatters, protocol decoders, state
  machines, and untrusted input.

### Performance And Async Behavior

- [Add benchmarks where performance claims, hot paths, or allocation behavior
  matter][rule-benchmark-claims].
- [Document blocking behavior, allocation expectations, and important performance
  constraints][rule-performance-contracts] when callers must plan around them.
- [Do not make performance claims without evidence][rule-benchmark-claims].
- [Avoid unnecessary allocations in hot paths][rule-benchmark-claims].
- [Async code that can run for a long time][rule-async-scheduling] should yield or otherwise make
  scheduling expectations clear.

### CI, Lints, And Unsafe Code

- [Treat CI as part of the library's public quality bar][rule-ci-signal].
- [CI should check the same commands maintainers are expected to run locally][rule-ci-signal].
- [Prefer fast deterministic CI jobs with clear failure modes][rule-ci-signal].
- [Keep required checks strict enough that drift does not accumulate][rule-ci-signal].
- [Run formatting and clippy early][rule-ci-signal] because they fail fast.
- [Run docs as a first-class job][rule-docs-ci], not only as a release task.
- [Run tests with all features][rule-feature-validation].
- [Run important feature combinations separately][rule-feature-combinations].
- [Run MSRV checks if the crate declares an MSRV][rule-msrv-platforms].
- [Run platform checks for every supported platform][rule-msrv-platforms].
- [Document manual validation gaps][rule-msrv-platforms] when platform behavior cannot be fully
  tested in CI.
- [Keep slow fuzzing, long benchmarks, and exhaustive compatibility checks out of required PR
  CI][rule-slow-ci] unless they are fast and deterministic.
- [Add scheduled or manual CI for expensive checks][rule-slow-ci].
- [Avoid noisy automation][rule-ci-signal] that produces dependency churn or low-signal failures.
- [Use lint configuration only when it encodes a durable project rule][rule-durable-lints].
- [Do not enable a large pile of strict lints blindly][rule-actionable-lints].
- [Enable stricter lints][rule-actionable-lints] when they improve correctness, public API quality,
  or maintainability.
- [Deny accidental unsafe code][rule-deny-unsafe] when the crate does not need unsafe.
- [Keep unsafe blocks small and wrapped by safe APIs][rule-contain-unsafe].
- [Explain each unsafe block with a `SAFETY:` comment][rule-contain-unsafe] that states the
  invariant being relied on.
- [Test the safe wrapper around unsafe code][rule-unsafe-safe-api] rather than only the unsafe
  internals.
- [Consider linting broken Rustdoc links, bare Rustdoc URLs, unreachable public items, unused crate
  dependencies, unexpected cfgs, and missing debug implementations][rule-actionable-lints] for
  public types.
- [Use `warn(missing_docs)` once the API is ready for that pressure][rule-actionable-lints].
- [Avoid lint suppressions unless they explain why the exception is correct][rule-actionable-lints].
- [Never use lint allows as cleanup by silencing][rule-actionable-lints].
- [Prefer `#[expect]` over `#[allow]`][rule-expect-lints] when the suppression should fail after the
  lint stops firing.
- [Keep lint suppression scope as small as the exception permits][rule-actionable-lints].

### Feature Flags And Dependency Policy

- [Make feature flags additive where possible][rule-additive-features].
- [Avoid features that silently change public semantics][rule-additive-features].
- [Keep optional dependencies tied to clearly named features][rule-optional-dependencies].
- [Keep test-only helpers out of the normal public API][rule-test-only-helpers]; use
  dev-dependencies or an explicit `test-util` feature when downstream tests need them.
- [Use grouped dependency-update automation][rule-dependency-updates] to reduce PR noise.
- [Treat semver-compatible dependency breakage as a downstream integration
  concern][rule-dependency-updates].
- [Use dependency-management commands][rule-dependency-updates] when they preserve manifest
  consistency better than hand edits.

### Workspace And Crate Boundaries

- [Prefer small shared dependency surfaces in core crates][rule-crate-boundaries].
- [Keep new code and tests inside the crate or module that owns the behavior][rule-crate-boundaries].
- [Avoid adding ad hoc modules under a root facade][rule-crate-boundaries].
- [Avoid cross-crate coupling][rule-crate-boundaries].
- [Expose shared helpers through crate-local modules][rule-crate-boundaries] unless public API is
  intended.
- [Prefer explicit module re-exports][rule-reexport-discovery] for library APIs.
- [Avoid broad public `helpers`, `util`, or `common` modules][rule-concept-modules] unless they name
  a user-facing concept.

### Imports, Ordering, And Types

- [Keep imports ordered and minimal][rule-order-items].
- [Group private imports before public re-exports][rule-private-imports].
- [Keep private imports limited to traits and heavily used items][rule-order-items] whose meaning
  remains obvious.
- [Prefer module-based grouped imports][rule-module-imports] over one-import-per-line style.
- [Group public items before private items][rule-order-items] when that helps readers find the API
  first.
- [Put the titular or central item first][rule-central-item-first].
- [Put a type's inherent impl near the type][rule-order-items].
- [Put inherent impls before trait impls][rule-order-items] when inherent methods are the core API.
- [Use judgment when file-order rules conflict][rule-order-items].
- [Prefer explicit types where clarity matters][rule-standard-types].
- [Prefer standard library types that carry meaning][rule-standard-types], such as `Path`,
  `PathBuf`, `OsStr`, `OsString`, `Duration`, `Instant`, `SystemTime`, `SocketAddr`, `IpAddr`,
  `RangeBounds`, `Cow`, and `NonZero*`.
- [Prefer `Send + 'static` errors, futures, and service handles][rule-send-static] when they cross
  task or thread boundaries.
- [Avoid global mutable state][rule-global-mutable-state].
- [Make filesystem, network, time, randomness, process, and other host interactions
  injectable][rule-host-injection] at a boundary when tests or alternate environments need control.
- [Use generics, stored generic parameters, and trait objects deliberately][rule-generics-traits].
  Use generics over traits for local dependency injection, generic structs when ownership is stored,
  and trait objects only when runtime heterogeneity or object safety is needed.

### Local Style And Documentation Hygiene

- [Use field init shorthand][rule-field-shorthand] when it improves ordinary Rust readability.
- [Format Rust code in doc comments][rule-format-docs-comments] when the formatter can do so
  consistently.
- [Normalize doc attributes][rule-format-docs-comments] when the project formatter supports it.
- [Group imports at module granularity][rule-format-docs-comments] when that keeps import blocks
  readable.
- [Wrap comments and doc comments][rule-format-docs-comments] near the prose line length.
- [Scope lint allows narrowly][rule-actionable-lints].
- [Document the reason for each lint allow][rule-actionable-lints].
- [Feature flags should match the public capability they enable][rule-document-feature-contracts].
- [Feature-gated code paths need tests][rule-feature-validation].
- [Feature-gated docs paths need validation][rule-feature-validation].
- [Build docs in CI with warnings denied][rule-validate-rust-docs].
- [Keep README examples, Rustdoc examples, and example directories
  aligned][rule-doc-example-alignment].
- [Keep generated README content aligned with crate-level Rustdoc][rule-doc-example-alignment].
- [Run doctests when editing public Rustdoc][rule-validate-rust-docs].
- [Run feature-gated integration tests][rule-feature-validation] when changing feature-gated
  integrations.
- [Lint Markdown headings, links, tables, and fenced code blocks][rule-validate-rust-docs].
- [Avoid making CI flaky on external link checks][rule-validate-rust-docs].

### Release Checks

- [Configure docs.rs metadata intentionally][rule-docs-rs].
- [Validate package contents before publishing][rule-package-contents].
- [Inspect included docs, examples, license files, README, and generated artifacts before
  release][rule-release-artifact].
- [Ensure changelog, version numbers, crate metadata, docs.rs config, and README support claims
  agree][rule-release-claims].
- [Do a dry-run publish where possible][rule-release-artifact].
- [Tag only after the release artifact is validated][rule-release-artifact].
- [Prefer fewer high-signal gates over many noisy gates][rule-ci-signal].
- [CI should make quality cheaper][rule-ci-signal], not bury maintainers in ritual.

### Review Practice

- [Review from the perspective of a future maintainer][rule-future-maintainer] who did not write
  the code.
- [Look for repeated problems across modules][rule-future-maintainer], not only isolated defects.
- [Prefer concrete findings with file or module references and proposed fixes][rule-future-maintainer].
- [Prioritize correctness, public API clarity, documentation truthfulness, and
  maintainability][rule-future-maintainer].
- [If a module is hard to read, name the cause][rule-future-maintainer]: concept mixing, poor
  ordering, hidden state, vague names, or too much abstraction.
- [Read the existing code first][rule-future-maintainer].
- [Keep edits scoped to the owning concept][rule-scoped-rust-edits].
- [Validate with focused checks while working][rule-future-maintainer] and fuller checks before
  declaring completion.
- [Call out residual gaps honestly][rule-future-maintainer].
- [Treat code organization as technical writing][rule-future-maintainer] for future reviewers and
  debuggers.
- [Lead with the most salient details][rule-future-maintainer] and let readers dig deeper as needed.
- [Guide readers through file structure][rule-future-maintainer] the way prose guides readers
  through sections and paragraphs.

### Expression Shape

- [Keep weak abstractions close to their use][rule-expression-auditability].
- [Group related logic with whitespace][rule-expression-auditability].
- [Treat visual blocks as paragraphs inside functions][rule-expression-auditability].
- [Open an incremental state-building block with the state being built][rule-expression-auditability].
- [Use early returns for non-business bookkeeping][rule-expression-auditability].
- [Keep mutually exclusive business paths visually visible][rule-expression-auditability] with `if`,
  `else`, or `match` when that highlights the domain rule.
- [Do not mix side-effect statements and pure expressions][rule-expression-auditability] in the same
  logical step.
- [Keep combinator closures free of business-logic side effects][rule-expression-auditability].
- [Prefer loops over combinators][rule-expression-auditability] when the operation is performed for
  side effects.

[rule-additive-features]: ../rules/rust/rust-make-feature-flags-additive-where-possible.md
[rule-api-shape]: ../rules/rust/rust-keep-public-api-shape-intentional.md
[rule-async-routing-tests]: ../rules/testing/test-cover-async-routing-edge-cases.md
[rule-async-scheduling]: ../rules/rust/rust-document-scheduling-for-long-async.md
[rule-auditable-intermediates]: ../rules/rust/rust-name-auditable-intermediates.md
[rule-benchmark-claims]: ../rules/rust/rust-add-benchmarks-for-performance-claims.md
[rule-boring-code]: ../rules/rust/rust-prefer-boring-direct-code.md
[rule-browseable-layout]: ../rules/rust/rust-make-public-api-browseable-from-layout.md
[rule-builder-validation]: ../rules/rust/rust-validate-builders-on-build.md
[rule-builders]: ../rules/rust/rust-use-builders-for-optional-or-validated-fields.md
[rule-central-item-first]: ../rules/rust/rust-central-item-first.md
[rule-ci-signal]: ../rules/rust/rust-keep-ci-high-signal.md
[rule-coherent-concepts]: ../rules/rust/rust-keep-concepts-coherent.md
[rule-command-tests]: ../rules/testing/test-prove-command-construction-and-display.md
[rule-concept-modules]: ../rules/rust/rust-prefer-concept-owned-modules-and-named-files.md
[rule-constructors]: ../rules/rust/rust-prefer-constructors-and-conversion-traits.md
[rule-contain-unsafe]: ../rules/rust/rust-contain-unsafe.md
[rule-context-callbacks]: ../rules/rust/rust-avoid-broad-context-and-callbacks.md
[rule-crate-boundaries]: ../rules/rust/rust-keep-crate-boundaries-narrow.md
[rule-crate-comparisons]: ../rules/rust/rust-compare-crates-by-fit-and-tradeoff.md
[rule-current-behavior]: ../rules/rust/rust-document-current-implemented-behavior.md
[rule-debug-public-types]: ../rules/rust/rust-implement-debug-for-public-types.md
[rule-debug-assert]: ../rules/rust/rust-use-debug-assert-for-internal-invariants.md
[rule-deny-unsafe]: ../rules/rust/rust-deny-accidental-unsafe.md
[rule-dependency-updates]: ../rules/rust/rust-keep-dependency-updates-intentional.md
[rule-deterministic-tests]: ../rules/testing/test-prefer-deterministic-tests.md
[rule-directory-tocs]: ../rules/rust/rust-use-directory-modules-as-tables-of-contents.md
[rule-doc-example-alignment]: ../rules/rust/rust-keep-rustdoc-and-readme-examples-aligned.md
[rule-doc-inline]: ../rules/rust/rust-use-doc-inline-for-canonical-reexports.md
[rule-document-feature-contracts]: ../rules/rust/rust-document-feature-contracts.md
[rule-document-lifecycle-effects]: ../rules/rust/rust-document-lifecycle-side-effects.md
[rule-docs-rs]: ../rules/rust/rust-configure-docs-rs.md
[rule-docs-ci]: ../rules/testing/test-run-docs-as-first-class-gate.md
[rule-doctests]: ../rules/testing/test-cover-public-examples-with-doctests.md
[rule-drift-tests]: ../rules/testing/test-keep-drift-claims-aligned.md
[rule-durable-lints]: ../rules/rust/rust-encode-durable-rules-in-lints.md
[rule-empty-wrappers]: ../rules/rust/rust-avoid-empty-wrapper-types.md
[rule-error-display]: ../rules/rust/rust-write-actionable-error-display.md
[rule-error-traits]: ../rules/rust/rust-implement-standard-traits-for-public-errors.md
[rule-expect-lints]: ../rules/rust/rust-prefer-expect-for-lint-suppressions.md
[rule-explicit-effects]: ../rules/rust/rust-make-side-effects-explicit.md
[rule-expression-auditability]: ../rules/rust/rust-shape-expressions-for-auditability.md
[rule-feature-combinations]: ../rules/testing/test-check-important-feature-combinations.md
[rule-feature-validation]: ../rules/rust/rust-run-feature-gated-validation.md
[rule-field-shorthand]: ../rules/rust/rust-use-field-init-shorthand.md
[rule-format-docs-comments]: ../rules/rust/rust-format-docs-and-comments-consistently.md
[rule-future-maintainer]: ../rules/rust/rust-review-as-future-maintainer.md
[rule-fuzz-tests]: ../rules/testing/test-fuzz-parsers-formatters-and-state-machines.md
[rule-generics-traits]: ../rules/rust/rust-choose-generics-and-trait-objects-deliberately.md
[rule-giant-roots]: ../rules/rust/rust-avoid-giant-crate-roots.md
[rule-glob-reexports]: ../rules/rust/rust-avoid-glob-reexports.md
[rule-global-mutable-state]: ../rules/boundary/boundary-avoid-global-mutable-state.md
[rule-host-injection]: ../rules/rust/rust-inject-host-interactions-at-boundaries.md
[rule-incidental-functions]: ../rules/rust/rust-use-functions-for-incidental-types.md
[rule-integration-tests]: ../rules/testing/test-cover-public-boundaries-with-integration-tests.md
[rule-inline-modules]: ../rules/rust/rust-avoid-inline-modules.md
[rule-actionable-lints]: ../rules/rust/rust-keep-lints-actionable.md
[rule-markdown-purpose]: ../rules/rust/rust-keep-markdown-outside-rustdoc-purposeful.md
[rule-mod-rs]: ../rules/rust/rust-avoid-mod-rs-by-default.md
[rule-module-imports]: ../rules/rust/rust-group-module-imports.md
[rule-msrv-platforms]: ../rules/testing/test-check-msrv-and-platforms.md
[rule-navigation-tests]: ../rules/testing/test-cover-navigation-boundaries.md
[rule-non-exhaustive-errors]: ../rules/rust/rust-non-exhaustive-public-errors.md
[rule-optional-dependencies]: ../rules/rust/rust-tie-optional-dependencies-to-named-features.md
[rule-order-items]: ../rules/rust/rust-order-items-for-api-reading.md
[rule-overcommenting]: ../rules/rust/rust-avoid-overcommenting-trivial-code.md
[rule-package-contents]: ../rules/rust/rust-validate-package-contents-before-release.md
[rule-panic-contracts]: ../rules/rust/rust-document-public-panic-contracts.md
[rule-path-attribute]: ../rules/rust/rust-avoid-path-attribute.md
[rule-parser-samples]: ../rules/testing/test-use-realistic-parser-samples.md
[rule-performance-contracts]: ../rules/rust/rust-document-performance-contracts.md
[rule-policy-tests]: ../rules/testing/test-cover-policy-outcomes.md
[rule-pre-release-compat]: ../rules/rust/rust-keep-pre-release-compatibility-intentional.md
[rule-prelude-reexports]: ../rules/rust/rust-keep-preludes-reexport-only.md
[rule-preserve-error-context]: ../rules/rust/rust-preserve-error-context.md
[rule-private-imports]: ../rules/rust/rust-group-private-imports-before-public-re-exports.md
[rule-primary-crate-path]: ../rules/rust/rust-expose-primary-path-from-crate-root.md
[rule-pub-crate]: ../rules/rust/rust-do-not-default-pub-crate.md
[rule-public-dependency-coupling]: ../rules/rust/rust-avoid-public-dependency-coupling.md
[rule-public-docs]: ../rules/rust/rust-write-public-docs-for-caller-tasks.md
[rule-reading-order]: ../rules/rust/rust-order-code-for-reading.md
[rule-reexport-discovery]: ../rules/rust/rust-reexport-for-discovery.md
[rule-regression-tests]: ../rules/testing/test-write-regression-tests-for-bug-fixes.md
[rule-release-claims]: ../rules/rust/rust-align-release-support-claims.md
[rule-release-artifact]: ../rules/rust/rust-release-only-after-artifact-validation.md
[rule-rustdoc-contract]: ../rules/rust/rust-write-rustdoc-as-api-contract.md
[rule-scoped-rust-edits]: ../rules/rust/rust-keep-edits-scoped-to-owning-concept.md
[rule-send-static]: ../rules/rust/rust-use-send-static-across-tasks.md
[rule-small-shapes]: ../rules/rust/rust-prefer-small-clear-shapes.md
[rule-slow-ci]: ../rules/testing/test-keep-slow-checks-out-of-pr-ci.md
[rule-standard-types]: ../rules/rust/rust-use-meaningful-standard-types.md
[rule-teach-crate-root]: ../rules/rust/rust-teach-crate-from-crate-root.md
[rule-test-contracts]: ../rules/testing/test-prove-contracts-not-trivia.md
[rule-test-evidence-surface]: ../rules/testing/test-match-evidence-to-surface.md
[rule-test-names]: ../rules/rust/rust-name-tests-by-behavior.md
[rule-test-only-helpers]: ../rules/rust/rust-hide-test-only-helpers.md
[rule-tiny-module-mazes]: ../rules/rust/rust-avoid-tiny-module-mazes.md
[rule-unit-tests]: ../rules/testing/test-cover-local-logic-with-unit-tests.md
[rule-unsafe-safe-api]: ../rules/rust/rust-validate-unsafe-through-safe-api.md
[rule-validate-rust-docs]: ../rules/rust/rust-validate-rust-docs-as-code.md
[rule-vague-docs]: ../rules/rust/rust-avoid-vague-docs-and-generic-examples.md
[rule-visibility-ownership]: ../rules/rust/rust-document-visibility-ownership.md
[rule-working-code]: ../rules/rust/rust-working-rust-code-not-enough.md

## Concepts And Types

Extract a type or helper when it names a real concept and reduces downstream reasoning. Avoid
wrapper types, tuple structs, or parameter bags that are constructed only to be immediately
destructured.

Prefer types that make invalid states hard to express when the invariant is repeated, meaningful,
and useful across a boundary. Keep a guard clause or local validation when the rule is one-off and a
new type would add ceremony without reducing risk.

Prefer concrete structs and enums before traits when the concept is still local. Introduce traits,
generic layers, callbacks, or framework-shaped abstractions only after a real variation point earns
the extra concept a reader must understand.

Use [Test Observable Behavior][test-behavior] before trusting a refactor that moves concepts around.

## Functions And Control Flow

Keep functions small enough to fit in a maintainer's head. Longer functions are acceptable when
their visual paragraphs map directly to meaningful phases.

Prefer named locals for important calls, side-effectful operations, and values whose role matters to
the reader. Use iterators for pure transformations and explicit loops for mutation, control flow, or
important side effects.

Do not compress navigation, parsing, rendering, or stateful control flow into dense iterator chains
when named locals would make edge cases easier to audit.

Use [Separate Structure From Behavior][structure-behavior] when a rename, move, extraction, or
formatting pass can be reviewed independently from a behavior change.

## Modules And Visibility

Modules should represent concepts, not arbitrary file-size cuts. Put the central type, trait, or
workflow near the top, keep inherent impls close to their type, and make re-exports deliberate.

Arrange modules in the order a reader needs the concepts: public or central types first, core
methods near their type, helpers near their callers, and tests near the behavior they prove. Split a
file when it lowers the number of live facts a reader must hold, not merely because a file crossed a
line-count threshold.

Use the smallest visibility that protects real invariants and keeps refactors cheap. Avoid
visibility ceremony that only makes the code look more layered.

Re-exports should improve discovery and preserve a clear owner. Do not use a facade module to hide
which module owns a concept or to make accidental internals feel stable.

## API Boundaries

Public APIs should be predictable, narrow, and hard to misuse. Prefer standard conversion traits
over ad hoc conversion names when the standard trait expresses the relationship. Keep dependencies
out of public types unless the dependency is part of the abstraction.

Rustdoc is part of the public API. Public modules, types, fields, functions, errors, feature flags,
and examples should document caller-facing contracts: what the item represents, who owns or mutates
state, what invariants hold, what can fail, and what compatibility the caller may rely on.

Public modules should answer what concept they own, the main workflow, related modules, and what
they intentionally do not own.

Public types should explain who should construct them, what invariants they preserve, lifecycle or
ownership behavior, concurrency expectations, and how they relate to neighboring types.

Public fields should document meaning, valid values, default behavior, invariants, and interactions
with other fields.

Public functions should document caller-facing behavior, state changes, side effects, and
allocation, blocking, I/O, global registration, or background work when relevant.

Use `From`, `TryFrom`, `Default`, `Display`, and common derives when they make value types easier
and safer to use without weakening invariants.

[APIs that touch process-wide, runtime-wide, terminal, filesystem, network, global registration,
background-task, or UI state need explicit lifecycle documentation][rule-document-lifecycle-effects].
Call out startup, shutdown, cleanup, drop behavior, cancellation, ordering, retry expectations, and
whether multiple instances may coexist when those details affect callers.

Fallible APIs should explain what can fail, whether retrying is useful, whether partial state may
have changed, and how callers recover.

Async or concurrent APIs should document runtime assumptions, cancellation, backpressure, capacity,
ordering, cloneability, and producer/consumer lifetime behavior.

[Feature-gated APIs should name the feature and explain what it
enables][rule-document-feature-contracts]: public API, runtime behavior, dependencies, examples,
platform support, or docs.rs coverage. A feature flag is a public integration surface, not only a
build toggle.

Use Conventional Commits only when the repo already follows that spec; otherwise keep jj
descriptions and commits in the canonical Chris Beams and Tim Pope style from
[Commit Messages For History][commit-history].

## Errors

Rust error types should preserve enough context for callers to act. Application boundaries may use
broad error types; reusable libraries should expose intentional errors with stable kinds and
recoverable context.

Handle fallible side effects near the boundary or surface them to the caller. Do not swallow
failures unless the ignored failure is intentional and obvious.

Keep partial-state updates conservative. Preserve the current usable state when refresh, parsing,
I/O, or rendering preparation fails and the previous state is still valid.

Use [Preserve Error Context][error-context] when wrapping or mapping errors. Use
[Write Actionable Error Messages][actionable-errors] when the visible message needs to help a user,
operator, caller, or support person make progress.

## Testing

Tests should protect observable behavior rather than private implementation shape. Prefer focused
unit tests, golden tests, round trips, property tests, or integration checks based on the changed
surface and likely failure.

New public API slices should usually include a practical example or doctest. Use examples to prove
ownership, lifecycle, errors, feature flags, or integration shape; avoid examples that only show a
constructor can be called.

For UI, terminal, protocol, parser, formatter, or state-machine behavior, pick evidence that matches
the claim. Snapshot tests, rendered fixtures, byte-level assertions, deterministic integration
tests, manual demos, screenshots, or generated reference projects can all be appropriate when they
prove the changed surface.

Review snapshot updates before accepting them. A snapshot change should represent intentional
behavior, not incidental formatting churn.

For scrollable or terminal UI, prefer stable dimensions and saturating arithmetic. Calculations
involving terminal height, line count, selected row, or scroll offset should handle empty content
and very small viewports.

When interactive behavior lacks automated coverage, document the manual verification that exercised
it.

Use [Smallest Trustworthy Verification][smallest-check] to pick the cheapest credible check and
[Report Verification Honestly][honest-verification] in the handoff.

## Performance

Prefer clarity first, then measure. Do not add caching, concurrency, allocation tricks, or unsafe
code from a guess alone. Keep hot-path changes small enough to benchmark directly, and document
intentional performance-sensitive shapes where future maintainers will see them.

Unsafe code should have a narrow purpose, a nearby safety argument, and tests or review evidence
that protect the invariant.

## Dependency Changes

Prefer the widest honest semver-compatible requirement that preserves the crate's intended behavior
and downstream integration shape. Use lockfile updates for newer compatible releases, and raise
`Cargo.toml` minimums only when a newer minimum is actually required.

Keep maintenance-only dependency updates separate from changes that may alter parsing, trait
behavior, MSRV, feature behavior, or public API semantics.

## Agent Snippet

For copyable `AGENTS.md` guidance, use [Rust Agent Instructions][rust-snippet].

## Related Guidance

Use [Rust API And Crate Shape Rules][rust-rules] for compact Rust instructions. Use
[Public API Changes Have Downstream Cost][api-cost] for API compatibility reasoning and
[Reader Locality Reduces Change Cost][reader-locality-principle] for source-shape reasoning. Use
[Rust API And Release Checks][api-release], [Rust Docs Validation][docs-validation], and
[Rust Lints And Formatting][rust-lints] when the guidance should be backed by tooling.

## Review Questions

- [Does this name a real Rust concept][rule-coherent-concepts] or just move code?
- [Are ownership and borrowing relationships visible at the call site][rule-standard-types]?
- [Does the type make invalid states harder to express][rule-small-shapes]?
- [Did the change improve locality or fragment understanding][rule-tiny-module-mazes]?
- [Did tests protect observable behavior instead of private shape][rule-test-contracts]?
- [Are error kinds, context, and recovery paths visible at the boundary][rule-preserve-error-context]?
- [Do lifecycle, side effects, feature flags, and platform assumptions appear where callers
  look][rule-document-lifecycle-effects]?
- [Do public examples prove a real integration shape][rule-vague-docs]?
- [Does validation evidence match the kind of behavior being changed][rule-test-evidence-surface]?
- [Is a performance-sensitive choice measured or clearly documented][rule-benchmark-claims]?
- [Did dependency requirements change only when the minimum truly changed][rule-dependency-updates]?

## References

| Source                         | Use      | Note                                                        |
| ------------------------------ | -------- | ----------------------------------------------------------- |
| [C-VALIDATE][validate]         | `adapts` | Prefer argument types that rule out bad inputs.             |
| [C-CONV-TRAITS][conv]          | `adapts` | Standard conversion traits keep APIs interoperable.         |
| [C-GOOD-ERR][errors]           | `adapts` | Error types should be meaningful and well-behaved.          |
| [M-SIMPLE-ABSTRACTIONS][ms]    | `adapts` | Public APIs should avoid exposing nested generic machinery. |
| [Ed Page Rust Style][ed-page]  | `adapts` | Reader-locality and Rust code-shape guidance.               |

[actionable-errors]: ../patterns/write-actionable-error-messages.md
[api-cost]: ../principles/public-api-changes-have-downstream-cost.md
[api-release]: ../mechanisms/rust-api-and-release-checks.md
[conv]: https://rust-lang.github.io/api-guidelines/interoperability.html#c-conv-traits
[commit-history]: ../patterns/commit-messages-for-history.md
[code-shape]: code-shape.md
[ed-page]: https://epage.github.io/dev/rust-style/
[errors]: https://rust-lang.github.io/api-guidelines/interoperability.html#c-good-err
[error-context]: ../patterns/preserve-error-context.md
[docs-validation]: ../mechanisms/rust-docs-validation.md
[honest-verification]: ../patterns/report-verification-honestly.md
[ms]: https://microsoft.github.io/rust-guidelines/guidelines/libs/ux/#M-SIMPLE-ABSTRACTIONS
[reader-locality]: ../patterns/reader-locality.md
[reader-locality-principle]: ../principles/reader-locality-reduces-change-cost.md
[rust-lints]: ../mechanisms/rust-lints-and-formatting.md
[rustdoc-pass]: ../patterns/run-rustdoc-quality-pass.md
[rust-rules]: ../rules/rust/README.md
[rust-snippet]: ../snippets/agents/rust.md
[smallest-check]: ../patterns/smallest-trustworthy-verification.md
[structure-behavior]: ../patterns/separate-structure-from-behavior.md
[test-behavior]: ../patterns/test-observable-behavior.md
[validate]: https://rust-lang.github.io/api-guidelines/dependability.html#c-validate
