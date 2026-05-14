# Rust Maintainability

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

## Rule Inventory

- Working code is not enough; the crate should be easy to understand, audit, extend, and use.
- Prefer obvious, boring, well-factored code over clever abstraction.
- Prefer direct implementation code over framework-shaped code until the framework pays for itself.
- Keep concepts coherent.
- A module should own one recognizable idea.
- Do not use a module as a bucket for loosely related helpers.
- Prefer small functions with meaningful names.
- Prefer narrow structs that own one coherent concept.
- Prefer simple enums for commands and state transitions.
- Prefer named locals when parsing, rendering, or side effects need auditability.
- Avoid broad context objects.
- Avoid callback-heavy control flow.
- Avoid wrappers that exist only to hide one line of code.
- Make side effects explicit in names, call sites, and docs.
- Avoid vague docs.
- Avoid generic examples.
- Avoid unnecessary wrappers.
- Avoid over-commenting trivial code.
- Avoid broad modules.
- Avoid examples that only prove a function can be called.
- Keep public API shape intentional.
- Do not preserve accidental development-era compatibility in pre-release crates.
- Every public item should have a clear owning module.
- Public error enums should be `#[non_exhaustive]` unless exhaustive matching is intentional.
- Error types should implement `Debug`, `Display`, and `std::error::Error` when they cross a public
  or reusable boundary.
- Error `Display` output should be human-oriented and actionable.
- Do not format errors with `Debug` in their `Display` implementation.
- Public types should implement `Debug` unless doing so is unsafe, misleading, or exposes
  confidential material.
- Public APIs should not leak dependency types unless dependency integration is the point of the
  API.
- Panics in public APIs should represent contract violations, not ordinary fallible conditions.
- Document exact panic preconditions when a public API can panic.
- Use `debug_assert!` for internal invariants that should be checked during development without
  becoming ordinary runtime error handling.
- Prefer inherent constructors or trait implementations for construction.
- Prefer regular functions over associated functions when the type name is incidental to the
  operation.
- Use builders when many optional fields or cross-field validation would make constructors hard to
  read.
- Builder `build` methods should validate cross-field invariants and return errors when construction
  can fail.
- Avoid giant crate roots.
- The crate root should teach the crate.
- The crate root should expose the primary path.
- The crate root should point to deeper modules.
- Public facade crates should re-export intentionally.
- Avoid glob re-exports in public facades.
- Use `#[doc(inline)]` when a re-export is the canonical path readers should land on.
- Put the main concept first.
- Reading order should follow execution order or conceptual dependency order.
- Keep helpers near the code that uses them unless they are independently important concepts.
- Prefer caller-before-callee order when it improves top-to-bottom reading.
- Avoid `mod.rs` unless there is a strong reason.
- Prefer feature-oriented modules and named files.
- Prefer `name.rs` over `mod.rs` for module roots unless local convention or tooling gives a strong
  reason otherwise.
- Directory-root modules should usually act as tables of contents.
- Directory-root modules should usually re-export child modules rather than own original logic.
- Prelude modules should only re-export.
- Avoid `#[path]` unless generated code or platform layout makes it the clearest option.
- The public API should be browseable from the file layout.
- Avoid inline modules except for tests, preludes, and generated code.
- Do not split files into a maze of tiny modules.
- Do not default to `pub(crate)`.
- Use `pub` only for intentional crate-root or public library API.
- When an item becomes visible outside its module, its name and docs should make ownership obvious.
- Treat Rustdoc as part of the API, not decoration.
- Start public item docs with a concise sentence that says what the item does or returns.
- Prefer prose for argument docs; avoid parameter tables unless the API truly needs tabular
  reference.
- Write docs for non-linear readers.
- Someone may land on any module, type, example, or guide first.
- Cross-link docs when links improve auditability.
- Document planned behavior as current scope or future work.
- Do not describe unimplemented behavior as available API.
- Compare nearby crates accurately and charitably.
- Explain fit, scope, and tradeoffs instead of claiming universal superiority.
- Prefer direct ownership and boundary statements over apologetic design justifications.
- Markdown docs should hold material that does not fit in Rustdoc or README.
- Tests should prove contracts, not implementation trivia.
- Tests should prove user-visible contracts and local invariants.
- Good tests make the maintenance question obvious.
- A reader should be able to tell what a user or future maintainer would notice if the behavior
  broke.
- Unit tests should cover local logic.
- Co-locate unit tests with the module behavior they prove.
- Integration tests should cover public behavior across module boundaries.
- Use integration tests when a unit test would hide the boundary being exercised.
- Doctests should cover public examples that can compile without fragile environment assumptions.
- Bug fixes should include regression tests unless the issue explains why that is impractical.
- Test error behavior, invalid input, cancellation, drop, cleanup, and boundary conditions.
- Prefer deterministic tests over tests that depend on timing or external state.
- Terminal behavior needs deterministic fixtures or testkit support before claims are broadened.
- Parser tests should use realistic samples.
- Parser tests should cover recognized shapes and safe degradation.
- Parser tests should not be broader than the parser's real contract.
- Parser recovery tests should cover malformed, truncated, unsupported, and mixed input when those
  cases are part of the contract.
- Navigation and scroll tests should cover boundary behavior.
- Command construction tests should prove both construction and display behavior.
- Policy tests should cover allowed, denied, redacted, and fallback behavior when policy affects
  output.
- Query, request, or correlation tests should cover unrelated input, late replies, timeouts, and
  unmatched responses when the API routes asynchronous replies.
- Drift tests should keep support claims, fixtures, docs, examples, and API paths aligned when the
  project has a registry or coverage inventory.
- Conversion and default tests should cover invariants encoded by coordinate, mode, selector, ID, or
  protocol value types.
- Avoid tests that require a real external repository, service, or terminal unless the behavior
  cannot be validated another way.
- Prefer behavior-oriented test names.
- Avoid test names that only repeat the function under test.
- Use fuzzing or property tests for parsers, formatters, protocol decoders, state machines, and
  untrusted input.
- Add benchmarks where performance claims, hot paths, or allocation behavior matter.
- Document blocking behavior, allocation expectations, and important performance constraints when
  callers must plan around them.
- Do not make performance claims without evidence.
- Avoid unnecessary allocations in hot paths.
- Async code that can run for a long time should yield or otherwise make scheduling expectations
  clear.
- Treat CI as part of the library's public quality bar.
- CI should check the same commands maintainers are expected to run locally.
- Prefer fast deterministic CI jobs with clear failure modes.
- Keep required checks strict enough that drift does not accumulate.
- Run formatting and clippy early because they fail fast.
- Run docs as a first-class job, not only as a release task.
- Run tests with all features.
- Run important feature combinations separately.
- Run MSRV checks if the crate declares an MSRV.
- Run platform checks for every supported platform.
- Document manual validation gaps when platform behavior cannot be fully tested in CI.
- Keep slow fuzzing, long benchmarks, and exhaustive compatibility checks out of required PR CI
  unless they are fast and deterministic.
- Add scheduled or manual CI for expensive checks.
- Avoid noisy automation that produces dependency churn or low-signal failures.
- Use lint configuration only when it encodes a durable project rule.
- Do not enable a large pile of strict lints blindly.
- Enable stricter lints when they improve correctness, public API quality, or maintainability.
- Deny accidental unsafe code when the crate does not need unsafe.
- Keep unsafe blocks small and wrapped by safe APIs.
- Explain each unsafe block with a `SAFETY:` comment that states the invariant being relied on.
- Test the safe wrapper around unsafe code rather than only the unsafe internals.
- Consider linting broken Rustdoc links, bare Rustdoc URLs, unreachable public items, unused crate
  dependencies, unexpected cfgs, and missing debug implementations for public types.
- Use `warn(missing_docs)` once the API is ready for that pressure.
- Avoid lint suppressions unless they explain why the exception is correct.
- Never use lint allows as cleanup by silencing.
- Prefer `#[expect]` over `#[allow]` when the suppression should fail after the lint stops firing.
- Keep lint suppression scope as small as the exception permits.
- Make feature flags additive where possible.
- Avoid features that silently change public semantics.
- Keep optional dependencies tied to clearly named features.
- Keep test-only helpers out of the normal public API; use dev-dependencies or an explicit
  `test-util` feature when downstream tests need them.
- Use grouped dependency-update automation to reduce PR noise.
- Treat semver-compatible dependency breakage as a downstream integration concern.
- Use dependency-management commands when they preserve manifest consistency better than hand edits.
- Prefer small shared dependency surfaces in core crates.
- Keep new code and tests inside the crate or module that owns the behavior.
- Avoid adding ad hoc modules under a root facade.
- Avoid cross-crate coupling.
- Expose shared helpers through crate-local modules unless public API is intended.
- Prefer explicit module re-exports for library APIs.
- Avoid broad public `helpers`, `util`, or `common` modules unless they name a user-facing concept.
- Keep imports ordered and minimal.
- Group private imports before public re-exports.
- Keep private imports limited to traits and heavily used items whose meaning remains obvious.
- Prefer module-based grouped imports over one-import-per-line style.
- Group public items before private items when that helps readers find the API first.
- Put the titular or central item first.
- Put a type's inherent impl near the type.
- Put inherent impls before trait impls when inherent methods are the core API.
- Use judgment when file-order rules conflict.
- Prefer explicit types where clarity matters.
- Prefer standard library types that carry meaning, such as `Path`, `PathBuf`, `OsStr`, `OsString`,
  `Duration`, `Instant`, `SystemTime`, `SocketAddr`, `IpAddr`, `RangeBounds`, `Cow`, and
  `NonZero*`.
- Prefer `Send + 'static` errors, futures, and service handles when they cross task or thread
  boundaries.
- Avoid global mutable state.
- Make filesystem, network, time, randomness, process, and other host interactions injectable at a
  boundary when tests or alternate environments need control.
- Use generics over traits for local dependency injection, generic structs when ownership is stored,
  and trait objects only when runtime heterogeneity or object safety is needed.
- Use field init shorthand when it improves ordinary Rust readability.
- Format Rust code in doc comments when the formatter can do so consistently.
- Normalize doc attributes when the project formatter supports it.
- Group imports at module granularity when that keeps import blocks readable.
- Wrap comments and doc comments near the prose line length.
- Scope lint allows narrowly.
- Document the reason for each lint allow.
- Feature flags should match the public capability they enable.
- Feature-gated code paths need tests.
- Feature-gated docs paths need validation.
- Build docs in CI with warnings denied.
- Keep README examples, Rustdoc examples, and example directories aligned.
- Keep generated README content aligned with crate-level Rustdoc.
- Run doctests when editing public Rustdoc.
- Run feature-gated integration tests when changing feature-gated integrations.
- Lint Markdown headings, links, tables, and fenced code blocks.
- Avoid making CI flaky on external link checks.
- Configure docs.rs metadata intentionally.
- Validate package contents before publishing.
- Inspect included docs, examples, license files, README, and generated artifacts before release.
- Ensure changelog, version numbers, crate metadata, docs.rs config, and README support claims agree.
- Do a dry-run publish where possible.
- Tag only after the release artifact is validated.
- Prefer fewer high-signal gates over many noisy gates.
- CI should make quality cheaper, not bury maintainers in ritual.
- Review from the perspective of a future maintainer who did not write the code.
- Look for repeated problems across modules, not only isolated defects.
- Prefer concrete findings with file or module references and proposed fixes.
- Prioritize correctness, public API clarity, documentation truthfulness, and maintainability.
- If a module is hard to read, name the cause: concept mixing, poor ordering, hidden state, vague
  names, or too much abstraction.
- Read the existing code first.
- Keep edits scoped to the owning concept.
- Validate with focused checks while working and fuller checks before declaring completion.
- Call out residual gaps honestly.
- Treat code organization as technical writing for future reviewers and debuggers.
- Lead with the most salient details and let readers dig deeper as needed.
- Guide readers through file structure the way prose guides readers through sections and
  paragraphs.
- Keep weak abstractions close to their use.
- Group related logic with whitespace.
- Treat visual blocks as paragraphs inside functions.
- Open an incremental state-building block with the state being built.
- Use early returns for non-business bookkeeping.
- Keep mutually exclusive business paths visually visible with `if`, `else`, or `match` when that
  highlights the domain rule.
- Do not mix side-effect statements and pure expressions in the same logical step.
- Keep combinator closures free of business-logic side effects.
- Prefer loops over combinators when the operation is performed for side effects.

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

APIs that touch process-wide, runtime-wide, terminal, filesystem, network, global registration,
background-task, or UI state need explicit lifecycle documentation. Call out startup, shutdown,
cleanup, drop behavior, cancellation, ordering, retry expectations, and whether multiple instances
may coexist when those details affect callers.

Fallible APIs should explain what can fail, whether retrying is useful, whether partial state may
have changed, and how callers recover.

Async or concurrent APIs should document runtime assumptions, cancellation, backpressure, capacity,
ordering, cloneability, and producer/consumer lifetime behavior.

Feature-gated APIs should name the feature and explain what it enables: public API, runtime
behavior, dependencies, examples, platform support, or docs.rs coverage. A feature flag is a public
integration surface, not only a build toggle.

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

## Review Questions

- Does this name a real Rust concept or just move code?
- Are ownership and borrowing relationships visible at the call site?
- Does the type make invalid states harder to express?
- Did the change improve locality or fragment understanding?
- Did tests protect observable behavior instead of private shape?
- Are error kinds, context, and recovery paths visible at the boundary?
- Do lifecycle, side effects, feature flags, and platform assumptions appear where callers look?
- Do public examples prove a real integration shape?
- Does validation evidence match the kind of behavior being changed?
- Is a performance-sensitive choice measured or clearly documented?
- Did dependency requirements change only when the minimum truly changed?

## References

| Source                      | Use      | Note                                                        |
| --------------------------- | -------- | ----------------------------------------------------------- |
| [C-VALIDATE][validate]      | `adapts` | Prefer argument types that rule out bad inputs.             |
| [C-CONV-TRAITS][conv]       | `adapts` | Standard conversion traits keep APIs interoperable.         |
| [C-GOOD-ERR][errors]        | `adapts` | Error types should be meaningful and well-behaved.          |
| [M-SIMPLE-ABSTRACTIONS][ms] | `adapts` | Public APIs should avoid exposing nested generic machinery. |
| [epage Rust Style][epage]   | `adapts` | Reader-locality and Rust code-shape guidance.               |

[actionable-errors]: ../patterns/write-actionable-error-messages.md
[conv]: https://rust-lang.github.io/api-guidelines/interoperability.html#c-conv-traits
[commit-history]: ../patterns/commit-messages-for-history.md
[code-shape]: code-shape.md
[epage]: https://epage.github.io/dev/rust-style/
[errors]: https://rust-lang.github.io/api-guidelines/interoperability.html#c-good-err
[error-context]: ../patterns/preserve-error-context.md
[honest-verification]: ../patterns/report-verification-honestly.md
[ms]: https://microsoft.github.io/rust-guidelines/guidelines/libs/ux/#M-SIMPLE-ABSTRACTIONS
[reader-locality]: ../patterns/reader-locality.md
[rust-snippet]: ../snippets/agents/rust.md
[smallest-check]: ../patterns/smallest-trustworthy-verification.md
[structure-behavior]: ../patterns/separate-structure-from-behavior.md
[test-behavior]: ../patterns/test-observable-behavior.md
[validate]: https://rust-lang.github.io/api-guidelines/dependability.html#c-validate
