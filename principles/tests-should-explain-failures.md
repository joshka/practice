# Tests Should Explain Failures

## Metadata

- Name: `Tests Should Explain Failures`
- ID: `tests-should-explain-failures`
- Status: `reviewed`
- Audience: `both`
- Topics: `testing, diagnostics, agents`
- Related: `test-observable-behavior, smallest-trustworthy-verification, review-proof-not-just-code`

## Claim

Passing tests prove behavior. Failing tests should explain the broken contract well enough that a
human or agent can move toward the fix without adding debug prints or guessing which cause failed.

## Why I Believe This

Tests are part of the development interface. A vague failure wastes reviewer time, slows agent
repair loops, and makes regressions harder to localize. The goal is not more assertions; the goal
is failures that point at the changed behavior.

Opaque boolean assertions are the common failure. `assert!(predicate(value))` can hide whether the
wrong variant, wrong field, wrong order, wrong message, or wrong collection element caused the
failure. A direct comparison, named table case, snapshot, or domain-specific assertion often gives
the reader the fix path immediately.

## What This Changes

Choose assertion shape by failure quality, not just by whether it expresses the expected behavior.
When a value has several possible failure causes, compare the value itself, the relevant struct, the
error variant, or a snapshot. Split unrelated expectations when one failing assertion would hide
another useful signal.

## Rust-Specific Guidance

- Prefer `assert_eq!` or `assert_ne!` when the compared values have useful `Debug` output.
- Use `assert_matches!` or pattern matching for variants and structured errors.
- Compare whole structs when the full output is the contract.
- Use named table cases when one test body covers many inputs.
- Use snapshots when the output is structured, textual, or easier to review as a whole.
- Write small assertion helpers when the helper can print domain context better than raw asserts.

## Good Uses

- Parser tests that show the input, expected value, and actual error.
- Error tests that compare structured kind, source, and context.
- Snapshot tests for rendered output or serialized data.
- Table tests with case names that appear in the failure output.

## Bad Smells

- `assert!(items.contains(...))` fails without showing the collection.
- One test checks setup, parsing, rendering, and cleanup as unrelated assertions.
- A failure only says "false is not true."
- The agent must rerun the test with prints to see the actual value.

## Mechanisms

- `pretty_assertions`, `similar-asserts`, or built-in structured comparison.
- `insta` snapshots for reviewable structured output.
- Custom assertion helpers that include input names and expected contracts.
- Test harnesses that preserve failing fixtures and command output.

## Rules This Supports

- `TEST-OPTIMIZE-TESTS-FOR-USEFUL-FAILURE-OUTPUT`
- `TEST-AVOID-BOOLEAN-ASSERTIONS-FOR-VALUES-WITH-MULTIPLE-FAILURE-CAUSES`
- `TEST-KEEP-UNRELATED-ASSERTIONS-SEPARATE-WHEN-FAILURE-DIAGNOSIS-MATTERS`

## Agent Consequences

When adding or changing tests, prefer assertions that print the actual broken surface. If a failure
would require manual reproduction to understand, improve the assertion shape before relying on the
test as proof.

## Limits

Tiny tests can stay simple when the failure mode is self-explanatory. Multiple assertions are fine
when they describe one coherent behavior and each failure is easy to interpret.
