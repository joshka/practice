# Tests Should Explain Failures

Test-failure rules cover assertion shape and failure output that help humans and agents diagnose the
failing case quickly.

Use this index to scan the domain and jump to the rule files. The one-line summaries are
for orientation; the rule files hold the rationale, limits, mechanisms, and references.

## Rules

- [`TEST-AVOID-OPAQUE-BOOLEAN-ASSERTIONS`](test-avoid-opaque-boolean-assertions.md). Avoid boolean
  assertions for values with multiple failure causes. An assertion like `assert!(items.contains(x))`
  or `assert!(result.is_ok())` can fail for many reasons while showing little useful state. Helps:
  Makes CI and agent failures easier to diagnose from the first failure message.
- [`TEST-OPTIMIZE-FAILURE-OUTPUT`](test-optimize-failure-output.md). Optimize tests for useful
  failure output. A passing test is useful, but a failing test is where maintainers and agents spend
  repair time. Helps: Shortens repair loops and makes regression failures actionable in CI logs.
- [`TEST-SPLIT-UNRELATED-ASSERTIONS`](test-split-unrelated-assertions.md). Keep unrelated assertions
  separate when failure diagnosis matters. One test that checks parsing, formatting, ordering, error
  display, and cleanup may stop at the first failure and hide the real scope of the regression.
  Helps: Makes failures local to one behavior and prevents one broken check from masking another.
