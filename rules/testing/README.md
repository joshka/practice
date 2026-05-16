# Testing And Verification

Testing rules cover risk-based validation, doctests, feature matrices, deterministic tests, parser
samples, command construction, dependency floors, and regressions.

Use this index to scan the domain and jump to the rule files. The one-line summaries are
for orientation; the rule files hold the rationale, limits, mechanisms, and references.

## Rules

- [`TEST-CHECK-IMPORTANT-FEATURE-COMBINATIONS`](test-check-important-feature-combinations.md).
  Exercise default, disabled-default, all-feature, and important feature-pair builds. Feature flags
  change APIs and compile paths, so use a risk-based matrix instead of every combo.
- [`TEST-CHECK-MAINTAINER-COMMANDS-IN-CI`](test-check-maintainer-commands-in-ci.md). Put documented
  maintainer commands, or intentionally stronger equivalents, in CI. This keeps local instructions
  honest while leaving slow or credentialed checks to special jobs.
- [`TEST-CHECK-MSRV-AND-PLATFORMS`](test-check-msrv-and-platforms.md). Run checks for declared Rust
  versions and supported platforms when they are promised. Compatibility claims are public
  contracts, so skip matrices only when no such claim exists.
- [`TEST-CHOOSE-VALIDATION-BY-RISK`](test-choose-validation-by-risk.md). Match the amount and kind
  of validation to the changed surface and failure cost. Cheap checks come first, but risky or
  uncertain behavior needs targeted evidence.
- [`TEST-COVER-ASYNC-ROUTING-EDGE-CASES`](test-cover-async-routing-edge-cases.md). Test late
  replies, unrelated input, timeouts, and unmatched async responses. These cases protect request
  correlation and cleanup without relying on wall-clock luck.
- [`TEST-COVER-LOCAL-LOGIC-WITH-UNIT-TESTS`](test-cover-local-logic-with-unit-tests.md). Use unit
  tests for small local logic such as parsing helpers and policy branches. They give fast precise
  feedback, while boundary behavior still needs higher-level tests.
- [`TEST-COVER-NAVIGATION-BOUNDARIES`](test-cover-navigation-boundaries.md). Exercise first, last,
  empty, oversized, and repeated-navigation states in tests. Boundary cases catch cursor and
  scrolling bugs that polished manual demos often miss.
- [`TEST-COVER-POLICY-OUTCOMES`](test-cover-policy-outcomes.md). Test allowed, denied, redacted,
  fallback, and unsupported policy outcomes. Policy value lives at decision boundaries, so assert
  caller-visible behavior instead of internals.
- [`TEST-COVER-PUBLIC-BOUNDARIES-WITH-INTEGRATION-TESTS`](test-cover-public-boundaries-with-integration-tests.md).
  Use integration tests to prove public module, crate, or adapter boundaries. They catch composition
  failures unit tests miss, while local logic can stay unit-tested.
- [`TEST-COVER-PUBLIC-EXAMPLES-WITH-DOCTESTS`](test-cover-public-examples-with-doctests.md). Compile
  public documentation examples as doctests when they do not need fragile state. Executable examples
  catch stale guidance, reserving no-run or ignored examples for real limits.
- [`TEST-FUZZ-PARSERS-FORMATTERS-AND-STATE-MACHINES`](test-fuzz-parsers-formatters-and-state-machines.md).
  Use fuzzing or property tests for input-heavy parsers, formatters, and state machines. Large input
  spaces hide failures, so keep long fuzzing outside PR gates unless it is stable.
- [`TEST-KEEP-DRIFT-CLAIMS-ALIGNED`](test-keep-drift-claims-aligned.md). Tie support claims,
  fixtures, examples, docs, and API paths to executable drift checks. Stable claims need evidence,
  but wording-only changes should not break broad tests.
- [`TEST-KEEP-SLOW-CHECKS-OUT-OF-PR-CI`](test-keep-slow-checks-out-of-pr-ci.md). Keep long fuzzing,
  exhaustive matrices, and noisy benchmarks out of required PR CI. Fast gates preserve review flow,
  while heavier checks belong in release or scheduled validation.
- [`TEST-MATCH-EVIDENCE-TO-SURFACE`](test-match-evidence-to-surface.md). Validate the actual changed
  surface, such as rendered docs, API behavior, or byte output. The narrowest relevant proof is more
  persuasive than unrelated broad test success.
- [`TEST-PREFER-DETERMINISTIC-TESTS`](test-prefer-deterministic-tests.md). Prefer tests controlled
  by fixed inputs, clocks, ordering, and local state. Deterministic failures are reproducible, while
  real integration checks should be isolated by cost.
- [`TEST-PROVE-COMMAND-CONSTRUCTION-AND-DISPLAY`](test-prove-command-construction-and-display.md).
  Test both executable command shape and displayed command text when users rely on them. Quoting,
  redaction, ordering, and platform formatting can fail even when a local happy path works.
- [`TEST-PROVE-CONTRACTS-NOT-TRIVIA`](test-prove-contracts-not-trivia.md). Write tests around
  observable contracts instead of private helper trivia. This preserves refactoring freedom unless
  the detail is itself the promised behavior.
- [`TEST-RUN-DOCS-AS-FIRST-CLASS-GATE`](test-run-docs-as-first-class-gate.md). Treat documentation
  checks as real validation for examples, links, commands, and claims. Prose-only edits may need
  less proof, but API-facing docs should fail before stale guidance ships.
- [`TEST-RUN-FAST-FORMAT-AND-LINT-GATES-EARLY`](test-run-fast-format-and-lint-gates-early.md). Run
  cheap format and lint gates early in the feedback loop. They remove mechanical failures quickly,
  but they do not replace validation of risky behavior.
- [`TEST-USE-REALISTIC-PARSER-SAMPLES`](test-use-realistic-parser-samples.md). Test parsers with
  representative input, malformed cases, and safe degradation examples. Real samples catch
  compatibility failures, but fixtures should be minimized and scrubbed.
- [`TEST-VALIDATE-DECLARED-MINIMUM-DEPENDENCY-VERSIONS`](test-validate-declared-minimum-dependency-versions.md).
  Check that declared minimum dependency versions still build the supported behavior. Lockfile tests
  can hide newer API usage, so use targeted minimal-version checks when needed.
- [`TEST-WRITE-REGRESSION-TESTS-FOR-BUG-FIXES`](test-write-regression-tests-for-bug-fixes.md). Add a
  test that fails before the bug fix and protects the repaired contract. Skip only when reproduction
  is impractical, and then record the closest trustworthy validation.
