# Rust API And Crate Shape

Rust rules cover public API shape, crate layout, dependency policy, docs.rs behavior, feature flags,
public errors, unsafe boundaries, and release checks.

Use this index to scan the domain and jump to the rule files. The one-line summaries are
for orientation; the rule files hold the rationale, limits, mechanisms, and references.

## Rules

- [`RUST-ADD-BENCHMARKS-FOR-PERFORMANCE-CLAIMS`](rust-add-benchmarks-for-performance-claims.md). Add
  benchmarks where Rust performance claims, hot paths, or allocation behavior matter.
  Performance-sensitive Rust changes are easy to justify from intuition and hard to validate by
  inspection. Helps: Helps performance-sensitive changes carry evidence instead of folklore.
- [`RUST-ALIGN-RELEASE-SUPPORT-CLAIMS`](rust-align-release-support-claims.md). Keep version,
  changelog, metadata, docs, and support claims aligned. Rust releases have several public truth
  sources: `Cargo.toml`, README, crate Rustdoc, changelog, docs.rs metadata, examples, and CI
  support matrices. Helps: Helps release reviewers compare every public claim before publishing and
  helps downstream users trust the crate docs, package metadata, and changelog as one contract.
- [`RUST-AVOID-BROAD-CONTEXT-AND-CALLBACKS`](rust-avoid-broad-context-and-callbacks.md). Avoid broad
  context objects and callback-heavy control flow. Broad context objects and callback-heavy flows
  hide which inputs, effects, and ordering a function needs. Helps: Helps readers see a function's
  real inputs, outputs, lifetimes, and side effects without tracing a context bag or callback chain
  through distant code.
- [`RUST-AVOID-EMPTY-WRAPPER-TYPES`](rust-avoid-empty-wrapper-types.md). Avoid wrapper types that
  add no invariant, behavior, or ownership clarity. A wrapper type should earn its name by adding an
  invariant, behavior, ownership boundary, or API meaning. Helps: Helps keep the type system
  meaningful by reserving new names for real invariants, ownership boundaries, validation rules, or
  domain concepts.
- [`RUST-AVOID-GIANT-CRATE-ROOTS`](rust-avoid-giant-crate-roots.md). Avoid giant crate roots. A
  giant `lib.rs` or `main.rs` makes the crate root carry every concept, helper, import, and
  re-export. Helps: Helps the crate root teach users the public shape while letting maintainers find
  implementation concepts in focused modules.
- [`RUST-AVOID-GLOB-REEXPORTS`](rust-avoid-glob-reexports.md). Avoid glob re-exports in public
  facades. `pub use module::*` hides which names the facade intends to expose. Helps: Helps public
  API review see every re-exported name and avoid accidental facade expansion.
- [`RUST-AVOID-INLINE-MODULES`](rust-avoid-inline-modules.md). Avoid inline modules except for
  tests, preludes, and generated code. Inline modules hide file boundaries and make navigation,
  search, and ownership harder in larger Rust crates. Helps: Helps search, review, ownership, and
  navigation by giving each nontrivial module a stable file path.
- [`RUST-AVOID-MOD-RS-BY-DEFAULT`](rust-avoid-mod-rs-by-default.md). Avoid `mod.rs` unless there is
  a strong reason. Named module root files such as `parser.rs` or `transport.rs` make editor tabs,
  search results, and diffs easier to scan than many files named `mod.rs`. Helps: Helps readers
  identify module ownership from file paths and editor labels.
- [`RUST-AVOID-OVERCOMMENTING-TRIVIAL-CODE`](rust-avoid-overcommenting-trivial-code.md). Avoid
  over-commenting trivial Rust code. Comments that restate obvious assignments, matches, or function
  calls add maintenance cost without adding understanding. Helps: Helps comments stay reserved for
  invariants, non-obvious tradeoffs, safety, and contracts.
- [`RUST-AVOID-PATH-ATTRIBUTE`](rust-avoid-path-attribute.md). Avoid `#[path]` unless generated code
  or platform layout makes it the clearest option. `#[path]` breaks the ordinary relationship
  between module names and file paths. Helps: Helps module paths remain predictable for readers,
  tools, and code review.
- [`RUST-AVOID-PUBLIC-DEPENDENCY-COUPLING`](rust-avoid-public-dependency-coupling.md). Avoid leaking
  dependency types in public APIs unless integration is the point. Public APIs that expose
  dependency types force downstream users to care about that dependency version, feature set, and
  semantics. Helps: Helps preserve semver freedom by keeping implementation dependencies from
  becoming downstream compile-time, feature, and version requirements.
- [`RUST-AVOID-TINY-MODULE-MAZES`](rust-avoid-tiny-module-mazes.md). Do not split Rust files into a
  maze of tiny modules. Small modules are useful when each module owns a concept. Helps: Helps keep
  local reasoning cheap and prevents structure from obscuring simple code.
- [`RUST-AVOID-VAGUE-DOCS-AND-GENERIC-EXAMPLES`](rust-avoid-vague-docs-and-generic-examples.md).
  Avoid vague Rustdoc and examples that only prove an item can be called. Docs that say an item is
  useful, flexible, simple, or convenient do not tell callers what behavior they can depend on.
  Helps: Helps examples demonstrate real use and helps docs answer caller questions directly.
- [`RUST-CENTRAL-ITEM-FIRST`](rust-central-item-first.md). Put the central item first and keep
  inherent impls near the type. A Rust module is easier to read when the main type, trait, enum, or
  function appears before helpers. Helps: Helps readers open a module and immediately find the type,
  trait, enum, or function the file exists to define.
- [`RUST-CHOOSE-GENERICS-AND-TRAIT-OBJECTS-DELIBERATELY`](rust-choose-generics-and-trait-objects-deliberately.md).
  Use generics, stored generic parameters, and trait objects deliberately. Generics, stored type
  parameters, and trait objects trade off monomorphization, API complexity, object safety, compile
  times, and caller ergonomics. Helps: Helps APIs expose the right kind of variation without
  surprising callers with compile-time cost, object-safety constraints, allocation, or lifetime
  complexity.
- [`RUST-COMPARE-CRATES-BY-FIT-AND-TRADEOFF`](rust-compare-crates-by-fit-and-tradeoff.md). Compare
  nearby Rust crates by fit, scope, and tradeoff. Rust ecosystems often have several crates solving
  adjacent problems. Helps: Helps users understand when this crate is the right tool without
  misrepresenting alternatives.
- [`RUST-CONFIGURE-DOCS-RS`](rust-configure-docs-rs.md). Configure docs.rs metadata intentionally.
  docs.rs is often the rendered documentation users see first. Helps: Helps users see the same
  features, cfg-gated items, and documentation warnings that the crate expects to support on
  docs.rs.
- [`RUST-CONSIDER-DOWNSTREAM-API-IMPACT`](rust-consider-downstream-api-impact.md). Consider
  downstream impact before changing public API. Changing a public Rust API can break external
  imports, trait impls, type inference, docs, examples, and semver expectations. Helps: Helps
  library maintainers avoid turning local cleanup into downstream breakage across imports, examples,
  trait impls, type inference, and semver expectations.
- [`RUST-CONTAIN-UNSAFE`](rust-contain-unsafe.md). Keep unsafe small, wrapped, documented, and
  tested through the safe API. Unsafe code concentrates obligations the compiler cannot check.
  Helps: Helps reviewers audit safety invariants locally and lets most tests exercise the unsafe
  behavior through a safe public contract.
- [`RUST-DENY-ACCIDENTAL-UNSAFE`](rust-deny-accidental-unsafe.md). Deny accidental unsafe code when
  the crate does not need unsafe. If a crate does not need unsafe, accidental unsafe blocks should
  fail loudly. Helps: Helps crates that intend to be safe Rust catch accidental unsafe introductions
  during review and CI.
- [`RUST-DO-NOT-DEFAULT-PUB-CRATE`](rust-do-not-default-pub-crate.md). Do not default to
  `pub(crate)`. `pub(crate)` looks safe because it is not public API, but it still expands the
  crate-wide surface and lets modules reach into each other. Helps: Helps keep internal APIs narrow
  so modules can change independently and readers can tell which items are truly shared
  implementation surface.
- [`RUST-DO-NOT-PIN-PATCH-VERSIONS`](rust-do-not-pin-patch-versions.md). Do not pin patch versions
  in `Cargo.toml` unless the patch is required. A patch-pinned dependency requirement in
  `Cargo.toml` raises the minimum version for every downstream resolver even when any compatible
  patch would work. Helps: Helps downstream users keep compatible dependency graphs flexible and
  avoids raising minimum versions just because local lockfiles are newer.
- [`RUST-DOCUMENT-CURRENT-IMPLEMENTED-BEHAVIOR`](rust-document-current-implemented-behavior.md).
  Document current implemented Rust behavior, not aspirations. Rustdoc and README examples are part
  of a crate's public contract. Helps: Helps crate docs stay truthful about what users can depend on
  today.
- [`RUST-DOCUMENT-FEATURE-CONTRACTS`](rust-document-feature-contracts.md). Document each feature
  flag as a public contract. Feature flags can add public API, change runtime behavior, enable
  optional dependencies, affect platform support, and alter docs.rs output. Helps: Helps users
  choose features intentionally and helps maintainers test feature-gated behavior.
- [`RUST-DOCUMENT-LIFECYCLE-SIDE-EFFECTS`](rust-document-lifecycle-side-effects.md). Document
  lifecycle and side effects for APIs that touch runtime, process, host, or UI state. APIs that
  register globally, spawn tasks, mutate process state, touch the filesystem, use the network, draw
  terminal UI, or manage runtime resources affect more than their return value. Helps: Helps callers
  plan ownership, cleanup, cancellation, retries, and multiple-instance behavior.
- [`RUST-DOCUMENT-PERFORMANCE-CONTRACTS`](rust-document-performance-contracts.md). Document blocking
  behavior, allocation expectations, and performance constraints. Blocking behavior, allocation
  expectations, buffering, clone cost, and runtime constraints can be part of a Rust API contract.
  Helps: Helps callers understand hidden costs such as allocation, blocking, complexity, caching,
  and large-data behavior before they choose an API.
- [`RUST-DOCUMENT-PUBLIC-PANIC-CONTRACTS`](rust-document-public-panic-contracts.md). Document public
  panic contracts as precondition violations. A public panic is a contract boundary: the caller
  violated a precondition or the crate has a bug. Helps: Helps callers distinguish misuse
  preconditions from ordinary recoverable errors and makes panic behavior testable in public APIs.
- [`RUST-DOCUMENT-SCHEDULING-FOR-LONG-ASYNC`](rust-document-scheduling-for-long-async.md). Document
  scheduling expectations for async code that can run for a long time. Long-running async work can
  starve executors, ignore cancellation, hold locks across await points, or surprise callers with
  runtime assumptions. Helps: Helps async callers reason about executor occupancy, cancellation,
  backpressure, blocking work, and fairness.
- [`RUST-DOCUMENT-VISIBILITY-OWNERSHIP`](rust-document-visibility-ownership.md). When a Rust item
  becomes visible outside its module, its name and docs should make ownership obvious. Widening
  visibility creates a new surface for other modules or downstream users to depend on. Helps: Helps
  prevent accidental shared APIs and makes ownership clear at call sites.
- [`RUST-ENCODE-DURABLE-RULES-IN-LINTS`](rust-encode-durable-rules-in-lints.md). Use lint
  configuration only for durable project rules. Lints are useful when they encode durable project
  policy, not transient taste. Helps: Helps CI enforce policies that are stable enough to automate,
  reducing review noise and making agent output easier to validate mechanically.
- [`RUST-EXPOSE-PRIMARY-PATH-FROM-CRATE-ROOT`](rust-expose-primary-path-from-crate-root.md). Expose
  the crate's primary path from the crate root. The crate root is the landing page for Rustdoc and
  the first import path many users try. Helps: Helps users find the intended starting point and
  helps maintainers keep facade shape intentional.
- [`RUST-FORMAT-DOCS-AND-COMMENTS-CONSISTENTLY`](rust-format-docs-and-comments-consistently.md).
  Format Rust docs and comments consistently. Rustdoc examples, doc attributes, imports, and prose
  comments are part of the source readers review. Helps: Helps Rust docs, examples, imports, and
  comments produce stable diffs and readable source.
- [`RUST-GROUP-MODULE-IMPORTS`](rust-group-module-imports.md). Prefer grouped module imports over
  one-import-per-line style. Grouped module imports keep related names together and make
  dependencies easier to scan. Helps: Helps readers see dependency shape by module and reduces churn
  from one-import-per-line edits.
- [`RUST-GROUP-PRIVATE-IMPORTS-BEFORE-PUBLIC-RE-EXPORTS`](rust-group-private-imports-before-public-re-exports.md).
  Group private imports before public re-exports. Private imports and public re-exports answer
  different questions. Helps: Helps separate implementation dependencies from the public discovery
  surface exposed through `pub use`.
- [`RUST-HIDE-TEST-ONLY-HELPERS`](rust-hide-test-only-helpers.md). Keep test-only helpers out of the
  normal public API. Test-only helpers should not become production API or crate-wide concepts by
  accident. Helps: Helps keep normal APIs free of fixtures, shortcuts, and constructors that exist
  only to make tests convenient.
- [`RUST-IMPLEMENT-DEBUG-FOR-PUBLIC-TYPES`](rust-implement-debug-for-public-types.md). Implement
  `Debug` for public types unless that is unsafe or misleading. `Debug` is the baseline diagnostic
  trait for Rust values. Helps: Helps downstream tests, logs, assertions, and diagnostics show
  useful values without bespoke formatting.
- [`RUST-IMPLEMENT-STANDARD-TRAITS-FOR-PUBLIC-ERRORS`](rust-implement-standard-traits-for-public-errors.md).
  Implement `Debug`, `Display`, and `std::error::Error` for reusable public errors. Public errors
  cross boundaries into callers, logs, tests, and user messages. Helps: Helps public errors work
  with `?`, error chains, logs, test output, and common error-reporting libraries.
- [`RUST-INJECT-HOST-INTERACTIONS-AT-BOUNDARIES`](rust-inject-host-interactions-at-boundaries.md).
  Make filesystem, network, time, randomness, process, and other host interactions injectable at a
  boundary when tests or alternate environments need control. Ambient host interactions make Rust
  code harder to test and harder to run in alternate environments. Helps: Helps tests control
  nondeterminism and keeps host effects at explicit boundaries.
- [`RUST-KEEP-CI-HIGH-SIGNAL`](rust-keep-ci-high-signal.md). Keep Rust CI strict, fast,
  deterministic, and high-signal. CI should make quality cheaper. Helps: Helps required checks catch
  real regressions without burying maintainers in ritual.
- [`RUST-KEEP-COMPATIBLE-UPDATES-IN-LOCKFILE`](rust-keep-compatible-updates-in-lockfile.md). Keep
  compatible dependency updates in the lockfile, not the manifest. Compatible dependency updates
  usually belong in the lockfile, not the manifest requirement. Helps: Helps avoid unnecessary
  downstream minimum-version bumps while still letting this checkout test with newer compatible
  releases.
- [`RUST-KEEP-CONCEPTS-COHERENT`](rust-keep-concepts-coherent.md). Keep Rust concepts coherent. A
  module, type, or helper should own one recognizable idea. Helps: Helps readers find the owner of a
  behavior and change it without learning unrelated concepts.
- [`RUST-KEEP-CRATE-BOUNDARIES-NARROW`](rust-keep-crate-boundaries-narrow.md). Keep Rust crate
  boundaries and shared dependency surfaces narrow. Every cross-crate helper, shared dependency,
  root facade, and crate-local utility module becomes a coupling point. Helps: Helps workspaces
  avoid accidental coupling, dependency fan-out, and facade modules that hide ownership.
- [`RUST-KEEP-DEPENDENCY-UPDATES-INTENTIONAL`](rust-keep-dependency-updates-intentional.md). Keep
  Rust dependency updates intentional and low-noise. Dependency updates can change parsing behavior,
  trait implementations, feature resolution, MSRV, platform support, compile time, and downstream
  integration even when the manifest requirement looks semver-compatible. Helps: Helps dependency
  maintenance stay reviewable without surprising downstream users.
- [`RUST-KEEP-EDITS-SCOPED-TO-OWNING-CONCEPT`](rust-keep-edits-scoped-to-owning-concept.md). Keep
  Rust edits scoped to the owning concept. Rust crates often make it easy to touch nearby modules,
  re-exports, features, and examples while solving one issue. Helps: Helps changes stay atomic and
  lets reviewers verify the behavior in the module that owns it.
- [`RUST-KEEP-LINTS-ACTIONABLE`](rust-keep-lints-actionable.md). Keep Rust lints actionable and
  scoped. Lint configuration should encode durable project policy, not a large pile of taste
  preferences that developers learn to silence. Helps: Helps lint failures stay meaningful and keeps
  suppressions from becoming invisible cleanup debt.
- [`RUST-KEEP-MARKDOWN-OUTSIDE-RUSTDOC-PURPOSEFUL`](rust-keep-markdown-outside-rustdoc-purposeful.md).
  Use Markdown docs for Rust material that does not fit in Rustdoc or README. Rustdoc is best for
  API contracts and examples near the items users call. Helps: Helps each Rust documentation surface
  carry the kind of information readers expect there.
- [`RUST-KEEP-PRE-RELEASE-COMPATIBILITY-INTENTIONAL`](rust-keep-pre-release-compatibility-intentional.md).
  Do not preserve accidental development-era compatibility in pre-release crates. Before a crate
  commits to stable public API, preserving accidental names, re-exports, features, or error variants
  can freeze poor shapes early. Helps: Helps pre-release crates converge on intentional public shape
  before semver compatibility hardens.
- [`RUST-KEEP-PRELUDES-REEXPORT-ONLY`](rust-keep-preludes-reexport-only.md). Keep prelude modules
  re-export only. A prelude is a convenience import surface, not an owner of behavior. Helps: Helps
  users import common names without obscuring where those names are defined.
- [`RUST-KEEP-PUBLIC-API-SHAPE-INTENTIONAL`](rust-keep-public-api-shape-intentional.md). Keep public
  API shape intentional. Every public item becomes something users can import, name, document, and
  depend on. Helps: Helps prevent accidental semver commitments through visibility, type aliases,
  features, re-exports, trait bounds, and error variants.
- [`RUST-KEEP-RUSTDOC-AND-README-EXAMPLES-ALIGNED`](rust-keep-rustdoc-and-readme-examples-aligned.md).
  Keep README examples, Rustdoc examples, generated README content, and example directories aligned.
  Rust crates often teach the same API in several places. Helps: Helps public documentation present
  one coherent usage contract.
- [`RUST-MAKE-FEATURE-FLAGS-ADDITIVE-WHERE-POSSIBLE`](rust-make-feature-flags-additive-where-possible.md).
  Make feature flags additive where possible. Rust feature unification means enabling a feature in
  one dependency path can affect the whole build. Helps: Helps dependency unification behave
  predictably when multiple downstream crates enable different feature sets.
- [`RUST-MAKE-PUBLIC-API-BROWSEABLE-FROM-LAYOUT`](rust-make-public-api-browseable-from-layout.md).
  Make the public API browseable from the file layout. When public modules, re-exports, and files
  disagree, users and maintainers must translate between Rustdoc paths and source paths. Helps:
  Helps source browsing, Rustdoc navigation, and review align around the same conceptual map.
- [`RUST-MAKE-SIDE-EFFECTS-EXPLICIT`](rust-make-side-effects-explicit.md). Make side effects
  explicit in names, call sites, and docs. Rust's ownership model makes many data-flow effects
  visible, but I/O, global registration, background tasks, process state, logging, caches, and
  mutation through shared handles can still be hidden behind innocent-looking calls. Helps: Helps
  callers and reviewers see mutation, I/O, registration, cleanup, and background work.
- [`RUST-NAME-AUDITABLE-INTERMEDIATES`](rust-name-auditable-intermediates.md). Use named locals when
  parsing, rendering, or side effects need auditability. Intermediate variables can make Rust code
  easier to audit when they name ownership, parsing, validation, or policy decisions. Helps: Helps
  reviewers inspect parsing, rendering, validation, and side effects by turning dense expressions
  into named facts.
- [`RUST-NAME-TESTS-BY-BEHAVIOR`](rust-name-tests-by-behavior.md). Name Rust tests by the behavior
  they protect. Test names are the first diagnostic readers see when a Rust test fails. Helps: Helps
  test output explain the broken behavior before a reader opens the test body.
- [`RUST-NON-EXHAUSTIVE-PUBLIC-ERRORS`](rust-non-exhaustive-public-errors.md). Use
  `#[non_exhaustive]` for public error enums unless exhaustive matching is intentional. Public error
  enums often need new variants as integrations, validation, and provider behavior expand. Helps:
  Helps libraries add future error cases without forcing every downstream match expression to break
  at the next release.
- [`RUST-ORDER-CODE-FOR-READING`](rust-order-code-for-reading.md). Order Rust code by execution
  order or conceptual dependency order. File order is a reading interface. Helps: Helps modules read
  top-to-bottom and keeps helpers in context.
- [`RUST-ORDER-ITEMS-FOR-API-READING`](rust-order-items-for-api-reading.md). Order Rust items so the
  API is easy to read. Item order is part of source readability. Helps: Helps readers scan modules
  for API, implementation, and type behavior without jumping around.
- [`RUST-PREFER-BORING-DIRECT-CODE`](rust-prefer-boring-direct-code.md). Prefer boring direct Rust
  over clever framework-shaped code. Boring Rust makes ownership, error handling, and control flow
  visible. Helps: Helps maintainers and agents reason about ownership, control flow, and errors
  without learning an avoidable framework-shaped abstraction first.
- [`RUST-PREFER-CONCEPT-OWNED-MODULES-AND-NAMED-FILES`](rust-prefer-concept-owned-modules-and-named-files.md).
  Prefer concept-owned modules and named files. Modules should be owned by concepts, not by
  miscellaneous implementation layers. Helps: Helps readers find the code for a domain concept
  without translating through arbitrary layers such as helpers, utils, types, or misc.
- [`RUST-PREFER-CONSTRUCTORS-AND-CONVERSION-TRAITS`](rust-prefer-constructors-and-conversion-traits.md).
  Prefer inherent constructors or trait implementations for construction. Construction should tell
  callers whether they are building a new value, validating input, converting between
  representations, or borrowing a view. Helps: Helps callers discover how values are created and
  whether construction validates, converts, borrows, allocates, or can fail.
- [`RUST-PREFER-EXPECT-FOR-LINT-SUPPRESSIONS`](rust-prefer-expect-for-lint-suppressions.md). Prefer
  `#[expect]` over `#[allow]` when suppression should be revisited. `#[allow]` can silently outlive
  the reason it was added. Helps: Helps suppressions fail when they stop being needed, preventing
  stale `allow` attributes from hiding fixed warnings forever.
- [`RUST-PREFER-SMALL-CLEAR-SHAPES`](rust-prefer-small-clear-shapes.md). Prefer small functions,
  narrow structs, and simple enums. Small functions, narrow structs, and simple enums reduce the
  number of fields, branches, lifetimes, and invariants a reader must hold at once. Helps: Helps
  keep the number of live fields, branches, parameters, and invariants small enough for readers to
  understand locally.
- [`RUST-PRESERVE-ERROR-CONTEXT`](rust-preserve-error-context.md). Preserve enough Rust error
  context for callers to act. Mapping every failure to a broad string or generic variant loses the
  operation, input, source error, and recovery signal. Helps: Helps callers diagnose failures and
  preserve error chains without depending on private details.
- [`RUST-PRESERVE-VALID-STATE-ON-FAILURE`](rust-preserve-valid-state-on-failure.md). Preserve the
  current usable state when refresh, parsing, I/O, or rendering preparation fails. Partially applied
  failure paths can leave callers with neither the old valid state nor the new state. Helps: Helps
  stateful Rust code avoid corrupting usable state after fallible work.
- [`RUST-REEXPORT-FOR-DISCOVERY`](rust-reexport-for-discovery.md). Use re-exports for discovery, not
  ownership hiding. Re-exports help users find the public API from the crate root or module facade,
  but they should not obscure where the concept is owned. Helps: Helps users find the intended API
  from the crate root or module facade while preserving clear implementation ownership.
- [`RUST-RELEASE-ONLY-AFTER-ARTIFACT-VALIDATION`](rust-release-only-after-artifact-validation.md).
  Release and tag Rust crates only after validating the package artifact. The crate package is the
  artifact users receive. Helps: Helps Rust releases avoid missing docs, stale generated files,
  wrong metadata, and premature tags.
- [`RUST-REVIEW-AS-FUTURE-MAINTAINER`](rust-review-as-future-maintainer.md). Review Rust changes
  from the perspective of a future maintainer who did not write the code. Rust changes can compile
  and pass tests while leaving future readers with vague ownership, surprising visibility, hidden
  side effects, unclear errors, or brittle feature behavior. Helps: Helps review prioritize
  correctness, public API clarity, documentation truth, and maintainability.
- [`RUST-RUN-FEATURE-GATED-VALIDATION`](rust-run-feature-gated-validation.md). Run feature-gated
  tests and docs when changing feature-gated Rust integrations. Feature-gated code can compile,
  document, and behave differently from the default build. Helps: Helps optional integrations stay
  buildable, documented, and behaviorally covered.
- [`RUST-SHAPE-EXPRESSIONS-FOR-AUDITABILITY`](rust-shape-expressions-for-auditability.md). Shape
  Rust expressions so parsing, rendering, state changes, and side effects are easy to audit. Dense
  chains, side-effectful closures, and mixed pure/effect steps can hide the order and meaning of
  important work. Helps: Helps reviewers inspect edge cases and side effects without mentally
  executing dense expressions.
- [`RUST-TEACH-CRATE-FROM-CRATE-ROOT`](rust-teach-crate-from-crate-root.md). Teach the crate from
  the crate root. The crate root is the first Rustdoc page and often the first source file a reader
  opens. Helps: Helps new users learn the crate purpose, main types, feature flags, and first
  example before they browse module details.
- [`RUST-TIE-OPTIONAL-DEPENDENCIES-TO-NAMED-FEATURES`](rust-tie-optional-dependencies-to-named-features.md).
  Keep optional dependencies tied to clearly named features. Optional dependencies become part of
  the feature contract. Helps: Helps downstream users understand why an optional dependency exists
  and how enabling it changes compile time, platform support, and API surface.
- [`RUST-USE-BUILDERS-FOR-OPTIONAL-OR-VALIDATED-FIELDS`](rust-use-builders-for-optional-or-validated-fields.md).
  Use builders for many optional fields or cross-field validation. Constructors with many optional
  arguments or cross-field validation become hard to call correctly and hard to extend compatibly.
  Helps: Helps APIs avoid long argument lists while giving validation and cross-field defaults a
  named home.
- [`RUST-USE-DEBUG-ASSERT-FOR-INTERNAL-INVARIANTS`](rust-use-debug-assert-for-internal-invariants.md).
  Use `debug_assert!` for internal invariants that should be checked during development. Some
  invariants indicate programmer mistakes inside the crate rather than ordinary caller-facing
  errors. Helps: Helps distinguish internal correctness assumptions from recoverable public errors.
- [`RUST-USE-DIRECTORY-MODULES-AS-TABLES-OF-CONTENTS`](rust-use-directory-modules-as-tables-of-contents.md).
  Use directory-root modules as tables of contents. A directory-root module should orient readers to
  the submodules it owns. Helps: Helps directory modules orient readers to submodules and public
  exports instead of hiding implementation in a large `mod.rs`.
- [`RUST-USE-DOC-INLINE-FOR-CANONICAL-REEXPORTS`](rust-use-doc-inline-for-canonical-reexports.md).
  Use `#[doc(inline)]` when a re-export is the canonical path readers should land on. Rustdoc can
  show a re-export as a link away from the facade or inline the item's documentation at the facade.
  Helps: Helps Rustdoc present canonical public paths without hiding implementation ownership in
  source.
- [`RUST-USE-FIELD-INIT-SHORTHAND`](rust-use-field-init-shorthand.md). Use field init shorthand when
  it improves ordinary Rust readability. Rust readers expect `Self { name, path, count }` when local
  variable names already match field names. Helps: Helps struct construction stay concise and
  idiomatic when names already carry meaning.
- [`RUST-USE-FUNCTIONS-FOR-INCIDENTAL-TYPES`](rust-use-functions-for-incidental-types.md). Prefer
  regular functions over associated functions when the type name is incidental. Associated functions
  imply the type owns the operation. Helps: Helps callers avoid chasing an irrelevant type just to
  find a stateless operation or one-off transformation.
- [`RUST-USE-HONEST-MINIMUM-DEPENDENCIES`](rust-use-honest-minimum-dependencies.md). Use the lowest
  honest compatible dependency requirement. The manifest should state the lowest compatible
  dependency versions the crate honestly supports. Helps: Helps downstream users with older
  compatible dependency graphs build the crate without unnecessary version pressure.
- [`RUST-USE-MEANINGFUL-STANDARD-TYPES`](rust-use-meaningful-standard-types.md). Use standard
  library types that carry meaning. Standard library types such as `PathBuf`, `NonZeroUsize`,
  `Duration`, `Cow`, `Arc`, and `Result` carry familiar ownership and invariant signals. Helps:
  Helps encode units, ownership, paths, durations, nonzero constraints, borrowing, and optionality
  directly in function signatures.
- [`RUST-USE-SEND-STATIC-ACROSS-TASKS`](rust-use-send-static-across-tasks.md). Use `Send + 'static`
  errors, futures, and service handles across tasks or threads. Values crossing task or thread
  boundaries often need `Send + 'static` because the executor may move or retain them beyond the
  caller's stack frame. Helps: Helps spawned tasks and threads avoid borrowing stack-local values or
  non-thread-safe state that cannot outlive the caller.
- [`RUST-VALIDATE-BUILDERS-ON-BUILD`](rust-validate-builders-on-build.md). Builder `build` methods
  should validate cross-field invariants and return errors when construction can fail. Builders
  spread configuration across multiple calls. Helps: Helps keep partially configured builders
  flexible while keeping constructed values valid.
- [`RUST-VALIDATE-PACKAGE-CONTENTS-BEFORE-RELEASE`](rust-validate-package-contents-before-release.md).
  Validate package contents before release. The crate package is what users receive, not the working
  tree. Helps: Helps catch missing README files, examples, license files, generated assets, and
  accidental inclusions before publishing an immutable crate package.
- [`RUST-VALIDATE-RUST-DOCS-AS-CODE`](rust-validate-rust-docs-as-code.md). Validate Rust docs as
  code. Rust documentation often contains imports, feature assumptions, examples, generated README
  content, and links that users copy directly. Helps: Helps Rust documentation stay executable,
  linked, and aligned with the crate's public behavior.
- [`RUST-VALIDATE-SEMVER-BREAKS-AGAINST-EXTERNAL-USE`](rust-validate-semver-breaks-against-external-use.md).
  Validate semver-breaking changes against real external use. Semver tools can detect many API
  breaks, but real downstream code shows how the public surface is actually used. Helps: Helps
  distinguish theoretical API cleanup from real downstream breakage, especially for library crates
  with examples, tutorials, and external dependents.
- [`RUST-VALIDATE-UNSAFE-THROUGH-SAFE-API`](rust-validate-unsafe-through-safe-api.md). Test unsafe
  behavior through the safe wrapper. Unsafe internals matter because of the safe API contract they
  support. Helps: Helps unsafe invariants stay connected to the public or crate-local safe contract.
- [`RUST-WORKING-RUST-CODE-NOT-ENOUGH`](rust-working-rust-code-not-enough.md). Working Rust code is
  not enough. Rust code can compile while still being hard to read, poorly documented, wrongly
  public, feature-fragile, or painful for downstream users. Helps: Helps review Rust changes for API
  clarity, docs, errors, tests, feature behavior, module shape, and downstream compatibility instead
  of stopping at compilation.
- [`RUST-WRITE-ACTIONABLE-ERROR-DISPLAY`](rust-write-actionable-error-display.md). Write
  human-oriented and actionable error `Display` output. `Display` is often what users, CLIs, logs,
  and support messages show. Helps: Helps users and agents fix failures from the message they
  actually see in CLI output, logs, test diffs, and error reports.
- [`RUST-WRITE-PUBLIC-DOCS-FOR-CALLER-TASKS`](rust-write-public-docs-for-caller-tasks.md). Write
  public Rust docs around caller tasks. Public Rustdoc should help a caller decide what an item is
  for, how to use it, and what contract it creates. Helps: Helps public item docs answer caller
  questions without bloated reference tables or vague prose.
- [`RUST-WRITE-RUSTDOC-AS-API-CONTRACT`](rust-write-rustdoc-as-api-contract.md). Write Rustdoc as an
  API contract. Rustdoc is often the first and most durable public view of a crate. Helps: Helps
  downstream users understand behavior without reading private implementation details.
