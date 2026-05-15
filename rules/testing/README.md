# Testing And Verification

Testing rules cover risk-based validation, doctests, feature matrices, deterministic tests, parser
samples, command construction, dependency floors, and regressions.

Use this index to scan the domain and jump to the rule files. The one-line summaries are
for orientation; the rule files hold the rationale, limits, mechanisms, and references.

## Rules

- [`TEST-CHECK-IMPORTANT-FEATURE-COMBINATIONS`](test-check-important-feature-combinations.md). Test
  all features and important feature combinations. Rust feature flags can change public API,
  optional dependencies, cfg-gated docs, and compile paths. Helps: Catches feature-gated regressions
  before downstream users combine features differently than the maintainer did.
- [`TEST-CHECK-MAINTAINER-COMMANDS-IN-CI`](test-check-maintainer-commands-in-ci.md). Check the same
  commands in CI that maintainers are expected to run locally. If the README or maintainer guide
  says to run `cargo test`, `cargo doc`, `markdownlint-cli2`, or a release check, CI should exercise
  the same command or an intentionally stronger equivalent. Helps: Keeps contributor instructions
  honest and prevents maintainers from relying on checks that CI never runs.
- [`TEST-CHECK-MSRV-AND-PLATFORMS`](test-check-msrv-and-platforms.md). Run MSRV and platform checks
  when the crate declares them. MSRV and platform support are public compatibility claims. Helps:
  Keeps support claims aligned with reality and catches accidental platform or toolchain
  regressions.
- [`TEST-CHOOSE-VALIDATION-BY-RISK`](test-choose-validation-by-risk.md). Choose validation by risk.
  Different changes need different proof. Helps: Avoids both under-testing risky work and
  over-testing low-risk edits.
- [`TEST-COVER-ASYNC-ROUTING-EDGE-CASES`](test-cover-async-routing-edge-cases.md). Cover unrelated
  input, late replies, timeouts, and unmatched responses in async routing tests. Async routing bugs
  often appear when replies arrive late, time out, match the wrong request, or include unrelated
  input. Helps: Protects request/response correlation, timeout behavior, and cleanup in async
  systems.
- [`TEST-COVER-LOCAL-LOGIC-WITH-UNIT-TESTS`](test-cover-local-logic-with-unit-tests.md). Cover local
  logic with unit tests. Small pure logic is cheapest to test close to where it lives. Helps: Gives
  fast, precise feedback for local contracts and edge cases.
- [`TEST-COVER-NAVIGATION-BOUNDARIES`](test-cover-navigation-boundaries.md). Cover navigation and
  scroll boundaries in tests. Navigation and scrolling bugs usually happen at the edges: empty
  lists, first item, last item, small viewport, oversized content, saturating offsets, and repeated
  key presses. Helps: Prevents off-by-one and underflow behavior in terminal UI, list, cursor, and
  paging code.
- [`TEST-COVER-POLICY-OUTCOMES`](test-cover-policy-outcomes.md). Cover allowed, denied, redacted,
  and fallback behavior in policy tests. Policy code is most useful at its decision boundaries:
  allowed, denied, redacted, fallback, preserved, and unsupported. Helps: Makes access, privacy,
  compatibility, and fallback behavior explicit and reviewable.
- [`TEST-COVER-PUBLIC-BOUNDARIES-WITH-INTEGRATION-TESTS`](test-cover-public-boundaries-with-integration-tests.md).
  Cover public behavior across module boundaries with integration tests. Public behavior can break
  across module, crate, feature, or adapter boundaries even when unit tests pass. Helps: Catches
  wiring, visibility, feature, and cross-module regressions at the user-facing boundary.
- [`TEST-COVER-PUBLIC-EXAMPLES-WITH-DOCTESTS`](test-cover-public-examples-with-doctests.md). Cover
  public examples with doctests when they can compile without fragile assumptions. Public examples
  teach users and agents how to call the API. Helps: Keeps documentation examples executable and
  aligned with public API shape.
- [`TEST-FUZZ-PARSERS-FORMATTERS-AND-STATE-MACHINES`](test-fuzz-parsers-formatters-and-state-machines.md).
  Use fuzzing or property tests for parsers, formatters, decoders, state machines, and untrusted
  input. Parsers, formatters, decoders, and state machines have large input spaces with edge cases
  humans will not enumerate. Helps: Finds edge cases beyond hand-written examples and protects
  input-facing code from surprising shapes.
- [`TEST-KEEP-DRIFT-CLAIMS-ALIGNED`](test-keep-drift-claims-aligned.md). Keep support claims,
  fixtures, docs, examples, and API paths aligned with drift tests. Support matrices, fixtures,
  docs, examples, and public API paths often drift independently. Helps: Keeps user-facing support
  claims tied to executable evidence.
- [`TEST-KEEP-SLOW-CHECKS-OUT-OF-PR-CI`](test-keep-slow-checks-out-of-pr-ci.md). Keep slow fuzzing,
  long benchmarks, and exhaustive compatibility checks out of required PR CI unless they are fast
  and deterministic. Required PR CI should give fast, reliable feedback. Helps: Keeps normal review
  fast while preserving heavier checks for release or scheduled validation.
- [`TEST-MATCH-EVIDENCE-TO-SURFACE`](test-match-evidence-to-surface.md). Match validation evidence
  to the changed surface. A change to rendered docs, terminal layout, parser output, public API, or
  performance needs evidence from that surface. Helps: Makes validation persuasive because the proof
  matches what changed.
- [`TEST-PREFER-DETERMINISTIC-TESTS`](test-prefer-deterministic-tests.md). Prefer deterministic
  tests over timing or external-state tests. Tests that depend on timing, network state, random
  ordering, real clocks, or external services fail for reasons unrelated to the code under review.
  Helps: Reduces flaky CI and makes failures actionable.
- [`TEST-PROVE-COMMAND-CONSTRUCTION-AND-DISPLAY`](test-prove-command-construction-and-display.md).
  Prove command construction and display behavior in tests. Command-building code can be wrong in
  quoting, argument order, display redaction, environment handling, or platform formatting while
  still invoking a happy path locally. Helps: Prevents shell, display, redaction, and platform bugs
  in command-facing code.
- [`TEST-PROVE-CONTRACTS-NOT-TRIVIA`](test-prove-contracts-not-trivia.md). Prove contracts with
  tests, not implementation trivia. Tests that lock down private helper order, incidental
  formatting, or intermediate variables make refactoring expensive without proving user-visible
  behavior. Helps: Keeps tests useful through refactoring and focused on behavior that matters.
- [`TEST-RUN-DOCS-AS-FIRST-CLASS-GATE`](test-run-docs-as-first-class-gate.md). Run docs as a
  first-class validation job. Docs contain commands, examples, feature claims, public API paths, and
  Rustdoc links. Helps: Keeps documentation, examples, and public API contracts aligned with code.
- [`TEST-RUN-FAST-FORMAT-AND-LINT-GATES-EARLY`](test-run-fast-format-and-lint-gates-early.md). Run
  formatting and clippy early because they fail fast. Formatting and lint failures are cheap to find
  and noisy to review. Helps: Shortens feedback loops and keeps review focused on behavior instead
  of mechanics.
- [`TEST-USE-REALISTIC-PARSER-SAMPLES`](test-use-realistic-parser-samples.md). Use realistic samples
  and safe degradation cases in parser tests. Parser tests built only from idealized examples miss
  real whitespace, ordering, partial data, unknown fields, legacy formats, invalid input, and safe
  degradation behavior. Helps: Catches parsing regressions and documents how malformed or unexpected
  input is handled.
- [`TEST-VALIDATE-DECLARED-MINIMUM-DEPENDENCY-VERSIONS`](test-validate-declared-minimum-dependency-versions.md).
  Validate declared minimum dependency versions. Cargo manifests communicate the minimum compatible
  versions a downstream project may resolve. Helps: Keeps dependency requirements honest and
  protects downstream minimal-version builds.
- [`TEST-WRITE-REGRESSION-TESTS-FOR-BUG-FIXES`](test-write-regression-tests-for-bug-fixes.md). Write
  regression tests for bug fixes unless impractical. A bug fix without a regression test can
  silently revert later, especially when the original failure was an edge case, integration path, or
  user-reported behavior. Helps: Preserves user-reported fixes and gives future maintainers a
  precise failure when the bug returns.
