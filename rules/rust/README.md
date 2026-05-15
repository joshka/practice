# Rust API And Crate Shape

Rust rules cover public API shape, crate layout, dependency policy, docs.rs behavior, feature flags,
public errors, unsafe boundaries, and release checks.

Use this index to scan the domain and jump to the rule files. The one-line summaries are
for orientation; the rule files hold the rationale, limits, mechanisms, and references.

## Rules

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
- [`RUST-AVOID-INLINE-MODULES`](rust-avoid-inline-modules.md). Avoid inline modules except for
  tests, preludes, and generated code. Inline modules hide file boundaries and make navigation,
  search, and ownership harder in larger Rust crates. Helps: Helps search, review, ownership, and
  navigation by giving each nontrivial module a stable file path.
- [`RUST-AVOID-PUBLIC-DEPENDENCY-COUPLING`](rust-avoid-public-dependency-coupling.md). Avoid leaking
  dependency types in public APIs unless integration is the point. Public APIs that expose
  dependency types force downstream users to care about that dependency version, feature set, and
  semantics. Helps: Helps preserve semver freedom by keeping implementation dependencies from
  becoming downstream compile-time, feature, and version requirements.
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
- [`RUST-ENCODE-DURABLE-RULES-IN-LINTS`](rust-encode-durable-rules-in-lints.md). Use lint
  configuration only for durable project rules. Lints are useful when they encode durable project
  policy, not transient taste. Helps: Helps CI enforce policies that are stable enough to automate,
  reducing review noise and making agent output easier to validate mechanically.
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
- [`RUST-KEEP-COMPATIBLE-UPDATES-IN-LOCKFILE`](rust-keep-compatible-updates-in-lockfile.md). Keep
  compatible dependency updates in the lockfile, not the manifest. Compatible dependency updates
  usually belong in the lockfile, not the manifest requirement. Helps: Helps avoid unnecessary
  downstream minimum-version bumps while still letting this checkout test with newer compatible
  releases.
- [`RUST-KEEP-PUBLIC-API-SHAPE-INTENTIONAL`](rust-keep-public-api-shape-intentional.md). Keep public
  API shape intentional. Every public item becomes something users can import, name, document, and
  depend on. Helps: Helps prevent accidental semver commitments through visibility, type aliases,
  features, re-exports, trait bounds, and error variants.
- [`RUST-MAKE-FEATURE-FLAGS-ADDITIVE-WHERE-POSSIBLE`](rust-make-feature-flags-additive-where-possible.md).
  Make feature flags additive where possible. Rust feature unification means enabling a feature in
  one dependency path can affect the whole build. Helps: Helps dependency unification behave
  predictably when multiple downstream crates enable different feature sets.
- [`RUST-NAME-AUDITABLE-INTERMEDIATES`](rust-name-auditable-intermediates.md). Use named locals when
  parsing, rendering, or side effects need auditability. Intermediate variables can make Rust code
  easier to audit when they name ownership, parsing, validation, or policy decisions. Helps: Helps
  reviewers inspect parsing, rendering, validation, and side effects by turning dense expressions
  into named facts.
- [`RUST-NON-EXHAUSTIVE-PUBLIC-ERRORS`](rust-non-exhaustive-public-errors.md). Use
  `#[non_exhaustive]` for public error enums unless exhaustive matching is intentional. Public error
  enums often need new variants as integrations, validation, and provider behavior expand. Helps:
  Helps libraries add future error cases without forcing every downstream match expression to break
  at the next release.
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
- [`RUST-REEXPORT-FOR-DISCOVERY`](rust-reexport-for-discovery.md). Use re-exports for discovery, not
  ownership hiding. Re-exports help users find the public API from the crate root or module facade,
  but they should not obscure where the concept is owned. Helps: Helps users find the intended API
  from the crate root or module facade while preserving clear implementation ownership.
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
- [`RUST-USE-DIRECTORY-MODULES-AS-TABLES-OF-CONTENTS`](rust-use-directory-modules-as-tables-of-contents.md).
  Use directory-root modules as tables of contents. A directory-root module should orient readers to
  the submodules it owns. Helps: Helps directory modules orient readers to submodules and public
  exports instead of hiding implementation in a large `mod.rs`.
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
- [`RUST-VALIDATE-PACKAGE-CONTENTS-BEFORE-RELEASE`](rust-validate-package-contents-before-release.md).
  Validate package contents before release. The crate package is what users receive, not the working
  tree. Helps: Helps catch missing README files, examples, license files, generated assets, and
  accidental inclusions before publishing an immutable crate package.
- [`RUST-VALIDATE-SEMVER-BREAKS-AGAINST-EXTERNAL-USE`](rust-validate-semver-breaks-against-external-use.md).
  Validate semver-breaking changes against real external use. Semver tools can detect many API
  breaks, but real downstream code shows how the public surface is actually used. Helps: Helps
  distinguish theoretical API cleanup from real downstream breakage, especially for library crates
  with examples, tutorials, and external dependents.
- [`RUST-WORKING-RUST-CODE-NOT-ENOUGH`](rust-working-rust-code-not-enough.md). Working Rust code is
  not enough. Rust code can compile while still being hard to read, poorly documented, wrongly
  public, feature-fragile, or painful for downstream users. Helps: Helps review Rust changes for API
  clarity, docs, errors, tests, feature behavior, module shape, and downstream compatibility instead
  of stopping at compilation.
- [`RUST-WRITE-ACTIONABLE-ERROR-DISPLAY`](rust-write-actionable-error-display.md). Write
  human-oriented and actionable error `Display` output. `Display` is often what users, CLIs, logs,
  and support messages show. Helps: Helps users and agents fix failures from the message they
  actually see in CLI output, logs, test diffs, and error reports.
