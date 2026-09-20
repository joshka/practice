# Tests Should Explain Failures

Test-failure rules cover assertion shape and failure output that help humans and agents diagnose the
failing case quickly.

Use this index to scan the domain and jump to the rule files. The one-line summaries are
for orientation; the rule files hold the rationale, limits, mechanisms, and references.

## Rules

- [`TEST-AVOID-OPAQUE-BOOLEAN-ASSERTIONS`](test-avoid-opaque-boolean-assertions.md). Prefer
  comparisons or richer assertions when a predicate hides state needed to diagnose the failure. The
  first failure should show the useful actual value.
- [`TEST-OPTIMIZE-FAILURE-OUTPUT`](test-optimize-failure-output.md). Design tests so failures
  include expected values, actual values, inputs, and contract context where that helps repair.
  Useful output shortens CI and agent debugging loops.
- [`TEST-SPLIT-UNRELATED-ASSERTIONS`](test-split-unrelated-assertions.md). Split assertions that
  diagnose different behaviors when one failure would hide another. Keep checks together only when
  they express one contract more clearly as a group.
