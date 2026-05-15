# Rust API And Crate Shape

Generated from the canonical `development-preferences` rule catalog. Do not edit copied rule
text by hand; update the source repo and recopy this file.

## Instructions

- `RUST-ALIGN-RELEASE-SUPPORT-CLAIMS`: Keep release claims aligned across `Cargo.toml`, README,
  Rustdoc, changelog, docs.rs metadata, examples, and CI support matrices.
- `RUST-AVOID-BROAD-CONTEXT-AND-CALLBACKS`: Avoid broad context objects and callback-heavy control
  flow because broad context objects and callback-heavy flows hide which inputs, effects, and
  ordering a function needs.
- `RUST-AVOID-EMPTY-WRAPPER-TYPES`: Avoid wrapper types that add no invariant, behavior, or
  ownership clarity; a wrapper should earn its name.
- `RUST-AVOID-GIANT-CRATE-ROOTS`: Avoid giant crate roots because a giant `lib.rs` or `main.rs`
  makes the crate root carry every concept, helper, import, and re-export.
- `RUST-AVOID-INLINE-MODULES`: Avoid inline modules except for tests, preludes, and generated code
  because named files improve navigation, search, and ownership.
- `RUST-AVOID-PUBLIC-DEPENDENCY-COUPLING`: Avoid leaking dependency types in public APIs unless
  integration is the point; exposed dependency types make downstream users care about that
  dependency's version, features, and semantics.
- `RUST-CENTRAL-ITEM-FIRST`: Put the main Rust type, trait, enum, or function before helpers so
  readers find the module concept first.
- `RUST-CHOOSE-GENERICS-AND-TRAIT-OBJECTS-DELIBERATELY`: Choose generics, stored type parameters,
  and trait objects deliberately because they trade off monomorphization, object safety, compile
  time, and ergonomics.
- `RUST-CONFIGURE-DOCS-RS`: Configure docs.rs metadata intentionally because docs.rs is often the
  rendered documentation users see first.
- `RUST-CONSIDER-DOWNSTREAM-API-IMPACT`: Consider downstream impact before changing public API
  because changing a public Rust API can break external imports, trait impls, type inference, docs,
  examples, and semver expectations.
- `RUST-CONTAIN-UNSAFE`: Keep unsafe small, wrapped, documented, and tested through the safe API
  because unsafe concentrates obligations the compiler cannot check.
- `RUST-DENY-ACCIDENTAL-UNSAFE`: Deny accidental unsafe code in crates that do not need unsafe so
  unsafe blocks fail loudly.
- `RUST-DO-NOT-DEFAULT-PUB-CRATE`: Do not default to `pub(crate)` because crate-wide visibility
  still expands the internal surface and lets modules reach into each other.
- `RUST-DO-NOT-PIN-PATCH-VERSIONS`: Avoid patch-pinned `Cargo.toml` requirements unless the patch
  supplies an API, behavior, or fix the crate actually needs.
- `RUST-DOCUMENT-PERFORMANCE-CONTRACTS`: Document blocking behavior, allocation expectations,
  buffering, clone cost, and runtime constraints that callers may reasonably depend on.
- `RUST-DOCUMENT-PUBLIC-PANIC-CONTRACTS`: Document public panic contracts as precondition violations
  because a public panic is a contract boundary: the caller violated a precondition or the crate has
  a bug.
- `RUST-DOCUMENT-SCHEDULING-FOR-LONG-ASYNC`: Document scheduling expectations for async work that
  can starve executors, ignore cancellation, hold locks, or rely on runtime assumptions.
- `RUST-ENCODE-DURABLE-RULES-IN-LINTS`: Use lint configuration for durable project policy, not
  transient taste or migration states that need frequent exceptions.
- `RUST-GROUP-MODULE-IMPORTS`: Prefer grouped module imports over one-import-per-line style because
  grouped module imports keep related names together and make dependencies easier to scan.
- `RUST-GROUP-PRIVATE-IMPORTS-BEFORE-PUBLIC-RE-EXPORTS`: Group private imports before public
  re-exports because private imports and public re-exports answer different questions.
- `RUST-HIDE-TEST-ONLY-HELPERS`: Keep test-only helpers out of the normal public API because
  test-only helpers should not become production API or crate-wide concepts by accident.
- `RUST-IMPLEMENT-DEBUG-FOR-PUBLIC-TYPES`: Implement `Debug` for public types unless that is unsafe
  or misleading; `Debug` is the baseline diagnostic trait for Rust values.
- `RUST-IMPLEMENT-STANDARD-TRAITS-FOR-PUBLIC-ERRORS`: Implement `Debug`, `Display`, and
  `std::error::Error` for public errors that cross into callers, logs, tests, and user messages.
- `RUST-KEEP-COMPATIBLE-UPDATES-IN-LOCKFILE`: Keep compatible dependency updates in the lockfile,
  not the manifest requirement, unless the crate actually needs the newer version.
- `RUST-KEEP-PUBLIC-API-SHAPE-INTENTIONAL`: Keep public API shape intentional because every public
  item becomes something users can import, name, document, and depend on.
- `RUST-MAKE-FEATURE-FLAGS-ADDITIVE-WHERE-POSSIBLE`: Make feature flags additive where possible
  because Rust feature unification means enabling a feature in one dependency path can affect the
  whole build.
- `RUST-NAME-AUDITABLE-INTERMEDIATES`: Name intermediate Rust values because they expose ownership,
  parsing, validation, rendering, or side-effect policy decisions.
- `RUST-NON-EXHAUSTIVE-PUBLIC-ERRORS`: Use `#[non_exhaustive]` for public error enums unless
  exhaustive matching is intentional; integrations, validation, and provider behavior often add
  variants over time.
- `RUST-PREFER-BORING-DIRECT-CODE`: Prefer boring direct Rust over clever framework-shaped code
  because boring Rust makes ownership, error handling, and control flow visible.
- `RUST-PREFER-CONCEPT-OWNED-MODULES-AND-NAMED-FILES`: Prefer concept-owned modules and named files
  because modules should be owned by concepts, not by miscellaneous implementation layers.
- `RUST-PREFER-CONSTRUCTORS-AND-CONVERSION-TRAITS`: Prefer constructors or conversion traits that
  show whether callers are building, validating, converting, or borrowing values.
- `RUST-PREFER-EXPECT-FOR-LINT-SUPPRESSIONS`: Use `#[expect]` for lint suppressions that should
  disappear once the warning is fixed.
- `RUST-PREFER-SMALL-CLEAR-SHAPES`: Prefer small functions, narrow structs, and simple enums to
  reduce live fields, branches, lifetimes, and invariants.
- `RUST-REEXPORT-FOR-DISCOVERY`: Use re-exports for discovery, not ownership hiding, so users find
  APIs without losing where concepts live.
- `RUST-TEACH-CRATE-FROM-CRATE-ROOT`: Teach the crate from the crate root because the crate root is
  the first Rustdoc page and often the first source file a reader opens.
- `RUST-TIE-OPTIONAL-DEPENDENCIES-TO-NAMED-FEATURES`: Keep optional dependencies tied to clearly
  named features because they become part of the feature contract.
- `RUST-USE-BUILDERS-FOR-OPTIONAL-OR-VALIDATED-FIELDS`: Use builders for many optional fields or
  cross-field validation because constructors with many optional arguments or cross-field validation
  become hard to call correctly and hard to extend compatibly.
- `RUST-USE-DIRECTORY-MODULES-AS-TABLES-OF-CONTENTS`: Use directory-root modules as tables of
  contents because a directory-root module should orient readers to the submodules it owns.
- `RUST-USE-FUNCTIONS-FOR-INCIDENTAL-TYPES`: Prefer regular functions because a type name is
  incidental and does not own the operation or invariant.
- `RUST-USE-HONEST-MINIMUM-DEPENDENCIES`: Use the lowest honest compatible dependency requirement
  because the manifest should state the lowest compatible dependency versions the crate honestly
  supports.
- `RUST-USE-MEANINGFUL-STANDARD-TYPES`: Use standard library types that carry meaning because
  standard library types such as `PathBuf`, `NonZeroUsize`, `Duration`, `Cow`, `Arc`, and `Result`
  carry familiar ownership and invariant signals.
- `RUST-USE-SEND-STATIC-ACROSS-TASKS`: Use `Send + static` bounds for values, futures, errors, and
  handles that cross task or thread boundaries.
- `RUST-VALIDATE-PACKAGE-CONTENTS-BEFORE-RELEASE`: Validate package contents before release because
  the crate package is what users receive, not the working tree.
- `RUST-VALIDATE-SEMVER-BREAKS-AGAINST-EXTERNAL-USE`: Validate semver-breaking changes against real
  external use because semver tools can detect many API breaks, but real downstream code shows how
  the public surface is actually used.
- `RUST-WORKING-RUST-CODE-NOT-ENOUGH`: Working Rust code is not enough because rust code can compile
  while still being hard to read, poorly documented, wrongly public, feature-fragile, or painful for
  downstream users.
- `RUST-WRITE-ACTIONABLE-ERROR-DISPLAY`: Write human-oriented and actionable error `Display` output
  because `Display` is often what users, CLIs, logs, and support messages show.
