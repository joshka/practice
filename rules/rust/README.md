# Rust API And Crate Shape

Rust rules cover public API shape, crate layout, dependency policy, docs.rs behavior, feature flags,
public errors, unsafe boundaries, and release checks.

Use this index to scan the domain and jump to the rule files. The one-line summaries are
for orientation; the rule files hold the rationale, limits, mechanisms, and references.

## Rules

- [`RUST-ADD-BENCHMARKS-FOR-PERFORMANCE-CLAIMS`](rust-add-benchmarks-for-performance-claims.md). Use
  benchmarks when Rust changes rely on speed, allocation, or hot-path claims. The evidence makes
  performance tradeoffs reviewable instead of relying on intuition.
- [`RUST-ALIGN-RELEASE-SUPPORT-CLAIMS`](rust-align-release-support-claims.md). Keep crate metadata,
  docs, changelogs, and support statements saying the same thing. The alignment helps downstream
  users know which compatibility contract to trust.
- [`RUST-AVOID-BROAD-CONTEXT-AND-CALLBACKS`](rust-avoid-broad-context-and-callbacks.md). Pass
  explicit inputs and keep control flow local instead of hiding it in context bags or callbacks.
  This makes ownership, effects, and ordering easier to audit.
- [`RUST-AVOID-EMPTY-WRAPPER-TYPES`](rust-avoid-empty-wrapper-types.md). Add a wrapper type only
  when it carries an invariant, behavior, or ownership boundary. Otherwise it adds conversions and
  concepts without improving correctness.
- [`RUST-AVOID-GIANT-CRATE-ROOTS`](rust-avoid-giant-crate-roots.md). Use the crate root to teach the
  public shape and route readers to focused modules. This keeps `lib.rs` or `main.rs` from becoming
  the whole implementation surface.
- [`RUST-AVOID-GLOB-REEXPORTS`](rust-avoid-glob-reexports.md). Re-export public facade names
  explicitly instead of using globs. This prevents accidental API expansion and makes exported names
  visible during review.
- [`RUST-AVOID-INLINE-MODULES`](rust-avoid-inline-modules.md). Put nontrivial modules in named files
  unless tests, preludes, or generated code justify inline layout. Stable paths make search, review,
  and ownership clearer.
- [`RUST-AVOID-MOD-RS-BY-DEFAULT`](rust-avoid-mod-rs-by-default.md). Prefer named module files when
  they make tabs, paths, and search results clearer. Reserve `mod.rs` for cases where local
  convention or layout makes it the better signal.
- [`RUST-AVOID-OVERCOMMENTING-TRIVIAL-CODE`](rust-avoid-overcommenting-trivial-code.md). Comment
  Rust code for invariants, contracts, and surprising tradeoffs rather than restating obvious
  operations. This keeps comments useful and less prone to drift.
- [`RUST-AVOID-PATH-ATTRIBUTE`](rust-avoid-path-attribute.md). Use normal Rust module lookup unless
  generated or platform-specific layout needs `#[path]`. Predictable file paths make navigation and
  ownership easier to infer.
- [`RUST-AVOID-PUBLIC-DEPENDENCY-COUPLING`](rust-avoid-public-dependency-coupling.md). Keep
  dependency types out of public APIs unless interoperability is the purpose. This preserves semver
  freedom and avoids forcing downstream users onto implementation choices.
- [`RUST-AVOID-TINY-MODULE-MAZES`](rust-avoid-tiny-module-mazes.md). Keep small helper code near its
  use unless a separate module owns a real concept. This reduces file-jumping and preserves reader
  locality.
- [`RUST-AVOID-VAGUE-DOCS-AND-GENERIC-EXAMPLES`](rust-avoid-vague-docs-and-generic-examples.md).
  Write Rustdoc and examples around real caller scenarios, not generic claims of usefulness.
  Concrete examples expose ownership, errors, features, and lifecycle expectations.
- [`RUST-CENTRAL-ITEM-FIRST`](rust-central-item-first.md). Put the main type, trait, enum, or
  function before supporting details. Readers can learn the module's purpose before chasing helpers
  and adapters.
- [`RUST-CHOOSE-GENERICS-AND-TRAIT-OBJECTS-DELIBERATELY`](rust-choose-generics-and-trait-objects-deliberately.md).
  Pick generics, stored type parameters, or trait objects for the variation they actually model. The
  choice affects compile cost, object safety, lifetimes, and caller ergonomics.
- [`RUST-COMPARE-CRATES-BY-FIT-AND-TRADEOFF`](rust-compare-crates-by-fit-and-tradeoff.md). Compare
  adjacent crates by intended fit, scope, and constraints instead of broad superiority claims. This
  helps users choose without turning docs into brittle marketing.
- [`RUST-CONFIGURE-DOCS-RS`](rust-configure-docs-rs.md). Configure docs.rs metadata when features,
  cfgs, or rustdoc flags affect rendered API docs. Users should see the documentation surface the
  crate expects to support.
- [`RUST-CONSIDER-DOWNSTREAM-API-IMPACT`](rust-consider-downstream-api-impact.md). Check public API
  changes against downstream imports, traits, inference, and examples before reshaping them.
  Additive paths and deprecations often avoid unnecessary breakage.
- [`RUST-CONTAIN-UNSAFE`](rust-contain-unsafe.md). Keep unsafe blocks small, wrapped by safe APIs,
  documented, and tested through safe behavior. Localized obligations make the safety argument
  auditable.
- [`RUST-DENY-ACCIDENTAL-UNSAFE`](rust-deny-accidental-unsafe.md). Use a crate-level lint when a
  crate intends to avoid unsafe code entirely. Executable policy catches accidental unsafe before it
  becomes normal implementation detail.
- [`RUST-DO-NOT-DEFAULT-PUB-CRATE`](rust-do-not-default-pub-crate.md). Start items private and widen
  to `pub(crate)` only for deliberate shared internals. This keeps modules independent and makes
  crate-local contracts visible.
- [`RUST-DO-NOT-PIN-PATCH-VERSIONS`](rust-do-not-pin-patch-versions.md). Keep manifest requirements
  as wide as the crate honestly supports. Patch pins belong in `Cargo.toml` only when code depends
  on that patch's API, fix, or behavior.
- [`RUST-DOCUMENT-CURRENT-IMPLEMENTED-BEHAVIOR`](rust-document-current-implemented-behavior.md).
  Document what the crate does today instead of presenting future plans as available contract. Clear
  tense and labels prevent callers from relying on unimplemented behavior.
- [`RUST-DOCUMENT-FEATURE-CONTRACTS`](rust-document-feature-contracts.md). Explain what each feature
  flag enables, requires, and promises. Feature contracts help users choose combinations without
  guessing from dependency names.
- [`RUST-DOCUMENT-LIFECYCLE-SIDE-EFFECTS`](rust-document-lifecycle-side-effects.md). Document
  construction, start, stop, drop, and cleanup behavior when side effects matter. Callers need to
  know when resources are acquired, released, spawned, or blocked.
- [`RUST-DOCUMENT-PERFORMANCE-CONTRACTS`](rust-document-performance-contracts.md). State meaningful
  performance expectations when callers may design around them. Clear limits keep complexity and
  optimization claims tied to supported behavior.
- [`RUST-DOCUMENT-PUBLIC-PANIC-CONTRACTS`](rust-document-public-panic-contracts.md). Document when
  public APIs can panic and what callers can do to avoid it. Panic contracts keep recoverable
  errors, invariants, and misuse boundaries explicit.
- [`RUST-DOCUMENT-SCHEDULING-FOR-LONG-ASYNC`](rust-document-scheduling-for-long-async.md). Explain
  executor, cancellation, blocking, and fairness expectations for async work that can run long.
  Callers need those constraints to avoid starvation and runtime surprises.
- [`RUST-DOCUMENT-VISIBILITY-OWNERSHIP`](rust-document-visibility-ownership.md). Pair widened
  visibility with names and docs that identify the owning concept. This prevents shared internals
  from looking like accidental stable API.
- [`RUST-ENCODE-DURABLE-RULES-IN-LINTS`](rust-encode-durable-rules-in-lints.md). Use lint
  configuration for project policies stable enough to automate. Durable lints catch repeated
  mistakes without turning subjective taste into CI noise.
- [`RUST-EXPOSE-PRIMARY-PATH-FROM-CRATE-ROOT`](rust-expose-primary-path-from-crate-root.md). Make
  the crate root show the main workflow, types, and import path. Users should not have to infer the
  intended entry point from private layout details.
- [`RUST-FORMAT-DOCS-AND-COMMENTS-CONSISTENTLY`](rust-format-docs-and-comments-consistently.md).
  Apply stable formatting to Rustdoc, examples, attributes, and prose comments. Consistent source
  formatting keeps docs readable and prevents noisy future diffs.
- [`RUST-GROUP-MODULE-IMPORTS`](rust-group-module-imports.md). Group related imports by module when
  that matches local style. This makes dependency shape easier to scan and avoids churn from
  one-import-per-line edits.
- [`RUST-GROUP-PRIVATE-IMPORTS-BEFORE-PUBLIC-RE-EXPORTS`](rust-group-private-imports-before-public-re-exports.md).
  Separate implementation imports from public re-exports in module prologues. The grouping lets
  readers distinguish internal dependencies from the API surface being presented.
- [`RUST-HIDE-TEST-ONLY-HELPERS`](rust-hide-test-only-helpers.md). Keep fixtures and shortcuts
  behind test-only modules, features, or support crates unless they are deliberate API. This
  prevents scaffolding from leaking into production contracts.
- [`RUST-IMPLEMENT-DEBUG-FOR-PUBLIC-TYPES`](rust-implement-debug-for-public-types.md). Provide
  `Debug` for public types unless it would expose secrets or mislead callers. The trait is baseline
  support for tests, assertions, logs, and downstream diagnostics.
- [`RUST-IMPLEMENT-STANDARD-TRAITS-FOR-PUBLIC-ERRORS`](rust-implement-standard-traits-for-public-errors.md).
  Make reusable public errors implement the standard diagnostic traits where appropriate. This lets
  callers compose, display, chain, and inspect errors in ordinary Rust workflows.
- [`RUST-INJECT-HOST-INTERACTIONS-AT-BOUNDARIES`](rust-inject-host-interactions-at-boundaries.md).
  Pass filesystem, network, time, randomness, and process behavior through boundaries when tests or
  alternate environments need control. This keeps the core deterministic and effects explicit.
- [`RUST-KEEP-CI-HIGH-SIGNAL`](rust-keep-ci-high-signal.md). Keep required Rust checks strict, fast,
  deterministic, and actionable. Slow or flaky ritual trains maintainers to ignore failures while
  real drift accumulates.
- [`RUST-KEEP-COMPATIBLE-UPDATES-IN-LOCKFILE`](rust-keep-compatible-updates-in-lockfile.md). Let
  lockfiles record newer compatible dependency versions when the manifest floor has not changed.
  This tests fresh releases without narrowing downstream compatibility.
- [`RUST-KEEP-CONCEPTS-COHERENT`](rust-keep-concepts-coherent.md). Give each module, type, or helper
  one recognizable idea to own. Coherent ownership keeps readers from carrying unrelated parsing,
  state, rendering, and policy facts at once.
- [`RUST-KEEP-CRATE-BOUNDARIES-NARROW`](rust-keep-crate-boundaries-narrow.md). Put behavior and
  tests in the crate or module that owns them before extracting shared helpers. Narrow boundaries
  reduce dependency fan-out, feature pressure, and hidden coupling.
- [`RUST-KEEP-DEPENDENCY-UPDATES-INTENTIONAL`](rust-keep-dependency-updates-intentional.md).
  Separate maintenance-only dependency refreshes from updates that change behavior, features, MSRV,
  or integration. Reviewable grouping lowers noise without hiding downstream risk.
- [`RUST-KEEP-EDITS-SCOPED-TO-OWNING-CONCEPT`](rust-keep-edits-scoped-to-owning-concept.md). Change
  the module, crate, feature, or facade that owns the behavior being fixed. Scoped edits keep
  reviews atomic and prevent nearby files from pulling in unrelated concepts.
- [`RUST-KEEP-LINTS-ACTIONABLE`](rust-keep-lints-actionable.md). Enforce lints that improve
  correctness, API quality, docs, portability, or maintenance in ways reviewers want automated.
  Scope suppressions tightly so exceptions stay visible.
- [`RUST-KEEP-MARKDOWN-OUTSIDE-RUSTDOC-PURPOSEFUL`](rust-keep-markdown-outside-rustdoc-purposeful.md).
  Use standalone Markdown for architecture, workflow, release, or operational guidance that would
  make API docs noisy. Choosing the right surface keeps contracts and long-form context current.
- [`RUST-KEEP-PRE-RELEASE-COMPATIBILITY-INTENTIONAL`](rust-keep-pre-release-compatibility-intentional.md).
  Preserve pre-release compatibility only when it reflects a chosen contract. Early cleanup is often
  cheaper than freezing accidental names, re-exports, features, or variants.
- [`RUST-KEEP-PRELUDES-REEXPORT-ONLY`](rust-keep-preludes-reexport-only.md). Put only re-exports in
  prelude modules and keep original behavior in its owning module. Users expect preludes to aid
  imports, not hide implementation ownership.
- [`RUST-KEEP-PUBLIC-API-SHAPE-INTENTIONAL`](rust-keep-public-api-shape-intentional.md). Make public
  visibility, aliases, features, re-exports, bounds, and variants reflect intended commitments.
  Published surface area becomes something downstream users can depend on.
- [`RUST-KEEP-RUSTDOC-AND-README-EXAMPLES-ALIGNED`](rust-keep-rustdoc-and-readme-examples-aligned.md).
  Keep README, Rustdoc, generated docs, and example directories teaching the same current usage
  contract. Aligned examples prevent users from guessing which import path or lifecycle is correct.
- [`RUST-MAKE-FEATURE-FLAGS-ADDITIVE-WHERE-POSSIBLE`](rust-make-feature-flags-additive-where-possible.md).
  Design feature flags as additive capabilities whenever possible so Cargo feature unification does
  not surprise downstream builds. Make incompatible combinations explicit when addition cannot model
  the real choice.
- [`RUST-MAKE-PUBLIC-API-BROWSEABLE-FROM-LAYOUT`](rust-make-public-api-browseable-from-layout.md).
  Align public modules, re-exports, and source files so readers can navigate from API to ownership
  without translation. Facades are fine when they improve discovery and still point toward the
  owning concept.
- [`RUST-MAKE-SIDE-EFFECTS-EXPLICIT`](rust-make-side-effects-explicit.md). Put mutation, I/O,
  registration, cleanup, and background work in names, call sites, or docs when callers must account
  for them. Keep tiny private helpers plain when the surrounding code already makes the effect
  obvious.
- [`RUST-NAME-AUDITABLE-INTERMEDIATES`](rust-name-auditable-intermediates.md). Introduce named
  locals where parsing, validation, rendering, ownership, or side-effect decisions need review.
  Avoid naming every trivial expression when it would add ceremony without clarifying the boundary.
- [`RUST-NAME-TESTS-BY-BEHAVIOR`](rust-name-tests-by-behavior.md). Name tests after the behavior,
  boundary, or regression they protect so failure output is useful before a reader opens the body.
  Keep names concise and let module context carry repeated setup details.
- [`RUST-NON-EXHAUSTIVE-PUBLIC-ERRORS`](rust-non-exhaustive-public-errors.md). Mark public error
  enums non-exhaustive unless exhaustive matching is part of the contract. This preserves room for
  future integration, validation, or provider failures without needless downstream breakage.
- [`RUST-ORDER-CODE-FOR-READING`](rust-order-code-for-reading.md). Arrange code so central items,
  callers, or public API appear before supporting helpers when that makes the file readable top to
  bottom. Prefer the order that reduces reader jumping over mechanical rearrangement.
- [`RUST-ORDER-ITEMS-FOR-API-READING`](rust-order-items-for-api-reading.md). Order imports, public
  items, impls, trait impls, and helpers so the API story is easy to scan. Respect macros, generated
  code, and local convention when another order communicates better.
- [`RUST-PREFER-BORING-DIRECT-CODE`](rust-prefer-boring-direct-code.md). Prefer explicit Rust
  control flow, types, and error handling over clever framework-shaped indirection. Use macros or
  abstractions when they remove real repetition or enforce real invariants.
- [`RUST-PREFER-CONCEPT-OWNED-MODULES-AND-NAMED-FILES`](rust-prefer-concept-owned-modules-and-named-files.md).
  Organize modules around domain concepts and give important concepts named files that own their
  types, invariants, tests, and docs. Use infrastructure modules only when the cross-cutting concept
  is real and bounded.
- [`RUST-PREFER-CONSTRUCTORS-AND-CONVERSION-TRAITS`](rust-prefer-constructors-and-conversion-traits.md).
  Use inherent constructors and standard conversion traits to show whether construction builds,
  validates, converts, borrows, allocates, or can fail. Prefer public fields only when direct
  construction is truly part of the contract.
- [`RUST-PREFER-EXPECT-FOR-LINT-SUPPRESSIONS`](rust-prefer-expect-for-lint-suppressions.md). Use
  `#[expect]` for targeted lint suppressions that should disappear when the warning is fixed.
  Reserve broad `allow` attributes for deliberate policy choices that are not expected to expire.
- [`RUST-PREFER-SMALL-CLEAR-SHAPES`](rust-prefer-small-clear-shapes.md). Favor small functions,
  narrow structs, and simple enums that keep live facts local for readers. Do not split cohesive
  logic into fragments that force more navigation than understanding.
- [`RUST-PRESERVE-ERROR-CONTEXT`](rust-preserve-error-context.md). Wrap and model errors so callers
  can see the operation, relevant input, source cause, and recovery signal. Avoid flattening
  failures into broad strings or generic variants that remove actionable context.
- [`RUST-PRESERVE-VALID-STATE-ON-FAILURE`](rust-preserve-valid-state-on-failure.md). Keep values
  valid when fallible operations return errors so callers can retry, inspect, or drop them
  predictably. Use transactional updates or staging when partial mutation would expose a broken
  state.
- [`RUST-REEXPORT-FOR-DISCOVERY`](rust-reexport-for-discovery.md). Re-export public items where
  callers naturally look so the crate surface is discoverable without hiding ownership. Keep
  canonical definitions and docs clear so re-exports do not become competing homes.
- [`RUST-RELEASE-ONLY-AFTER-ARTIFACT-VALIDATION`](rust-release-only-after-artifact-validation.md).
  Validate the actual release artifact before publishing instead of trusting the working tree. This
  catches missing files, stale generated content, and packaging mistakes while the release can still
  be fixed.
- [`RUST-REVIEW-AS-FUTURE-MAINTAINER`](rust-review-as-future-maintainer.md). Review Rust changes for
  the reader who will debug, extend, or release the code later, not only for immediate correctness.
  Favor maintainable API shape, docs, tests, and error behavior over changes that merely compile.
- [`RUST-RUN-FEATURE-GATED-VALIDATION`](rust-run-feature-gated-validation.md). Exercise the feature
  combinations touched by a Rust change so gated code, docs, and integrations actually build. Choose
  representative combinations when exhaustive feature matrices would be too expensive.
- [`RUST-SHAPE-EXPRESSIONS-FOR-AUDITABILITY`](rust-shape-expressions-for-auditability.md). Shape
  complex expressions so ownership, validation, error handling, and side effects can be audited at
  the point they occur. Break chains or introduce names when density hides a decision readers must
  verify.
- [`RUST-TEACH-CRATE-FROM-CRATE-ROOT`](rust-teach-crate-from-crate-root.md). Use crate-root docs and
  exports to teach the crate's main concepts, entry points, and common paths. Keep the root focused
  enough to orient readers without duplicating every item-level contract.
- [`RUST-TIE-OPTIONAL-DEPENDENCIES-TO-NAMED-FEATURES`](rust-tie-optional-dependencies-to-named-features.md).
  Connect optional dependencies to clear feature names that explain the capability callers enable.
  Avoid leaking dependency names as the public feature design when the capability needs a more
  stable contract.
- [`RUST-USE-BUILDERS-FOR-OPTIONAL-OR-VALIDATED-FIELDS`](rust-use-builders-for-optional-or-validated-fields.md).
  Use builders when construction has many optional inputs or cross-field validation that would make
  constructors hard to read. Avoid builder APIs for simple values where direct construction
  communicates the contract better.
- [`RUST-USE-DEBUG-ASSERT-FOR-INTERNAL-INVARIANTS`](rust-use-debug-assert-for-internal-invariants.md).
  Use debug assertions for internal invariants that should hold if nearby code is correct. Do not
  use them for caller validation or safety requirements that must be enforced in release builds.
- [`RUST-USE-DIRECTORY-MODULES-AS-TABLES-OF-CONTENTS`](rust-use-directory-modules-as-tables-of-contents.md).
  Let directory module files introduce, organize, and re-export the concepts owned by that
  directory. Keep substantial implementation in named child files so the module remains a readable
  table of contents.
- [`RUST-USE-DOC-INLINE-FOR-CANONICAL-REEXPORTS`](rust-use-doc-inline-for-canonical-reexports.md).
  Use `#[doc(inline)]` when a re-export should be the canonical place readers encounter an item.
  Avoid inlining re-exports that would obscure the owning module or create duplicate-looking
  documentation.
- [`RUST-USE-FIELD-INIT-SHORTHAND`](rust-use-field-init-shorthand.md). Use field init shorthand when
  variable names already match struct fields so initialization stays compact and familiar. Spell
  fields out when renaming, conversion, or policy deserves visible attention.
- [`RUST-USE-FUNCTIONS-FOR-INCIDENTAL-TYPES`](rust-use-functions-for-incidental-types.md). Prefer
  free or module functions when a type does not own the operation or invariant. Move behavior onto a
  type when the method relationship clarifies state, policy, or trait design.
- [`RUST-USE-HONEST-MINIMUM-DEPENDENCIES`](rust-use-honest-minimum-dependencies.md). Set dependency
  requirements to the lowest compatible versions the crate actually supports. Raise minimums only
  for required APIs, fixes, features, security needs, or MSRV interactions.
- [`RUST-USE-MEANINGFUL-STANDARD-TYPES`](rust-use-meaningful-standard-types.md). Prefer standard or
  ecosystem types that encode ownership, units, paths, durations, optionality, and invariants better
  than raw strings or integers. Use domain newtypes when the standard type cannot prevent meaningful
  mixups.
- [`RUST-USE-SEND-STATIC-ACROSS-TASKS`](rust-use-send-static-across-tasks.md). Require owned `Send +
  'static` values, futures, errors, and handles when they cross spawn or thread boundaries. Avoid
  imposing those bounds on local synchronous APIs where they would reject valid use.
- [`RUST-VALIDATE-BUILDERS-ON-BUILD`](rust-validate-builders-on-build.md). Validate cross-field
  builder invariants in `build` where partial configuration becomes a usable value. Keep `build`
  infallible only when defaults and setters make invalid states impossible.
- [`RUST-VALIDATE-PACKAGE-CONTENTS-BEFORE-RELEASE`](rust-validate-package-contents-before-release.md).
  Inspect and build the package users will receive, not just the repository checkout. This catches
  missing assets, accidental inclusions, README drift, and include/exclude mistakes before
  publication.
- [`RUST-VALIDATE-RUST-DOCS-AS-CODE`](rust-validate-rust-docs-as-code.md). Treat Rust documentation
  examples, links, feature assumptions, and generated README content as code that must be checked.
  Use docs builds, doctests, feature-gated checks, and Markdown lint according to the changed
  surface.
- [`RUST-VALIDATE-SEMVER-BREAKS-AGAINST-EXTERNAL-USE`](rust-validate-semver-breaks-against-external-use.md).
  Check semver-breaking changes against real examples, dependents, or migration paths before
  treating an API cleanup as cheap. External evidence informs the cost even when security,
  soundness, or design repair still justify the break.
- [`RUST-VALIDATE-UNSAFE-THROUGH-SAFE-API`](rust-validate-unsafe-through-safe-api.md). Test unsafe
  internals through the safe API wrapper that callers rely on. Internal unsafe tests and tools such
  as Miri should support, not replace, proof that safe calls uphold the contract.
- [`RUST-WORKING-RUST-CODE-NOT-ENOUGH`](rust-working-rust-code-not-enough.md). Treat compilation as
  necessary but insufficient evidence for long-lived Rust code. Review API shape, docs, errors,
  tests, features, dependencies, and module organization because users and maintainers inherit those
  choices.
- [`RUST-WRITE-ACTIONABLE-ERROR-DISPLAY`](rust-write-actionable-error-display.md). Write `Display`
  messages that tell humans what failed and what useful next action or context exists. Keep
  structured state in error fields, sources, diagnostics, or `Debug` instead of dumping internals
  into the user-facing string.
- [`RUST-WRITE-PUBLIC-DOCS-FOR-CALLER-TASKS`](rust-write-public-docs-for-caller-tasks.md). Write
  public Rustdoc around what callers are trying to decide, do, and rely on. Start with concise
  behavior and add arguments, failures, lifecycle, features, links, or examples only when they help
  the task.
- [`RUST-WRITE-RUSTDOC-AS-API-CONTRACT`](rust-write-rustdoc-as-api-contract.md). Use Rustdoc to
  state caller-facing behavior, invariants, failures, side effects, and compatibility promises.
  Leave private implementation detail in comments unless it helps maintain the public contract.
