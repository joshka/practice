# Tests Should Explain Failures

Generated from the canonical `joshka/practice` rule catalog. Do not edit copied rule
text by hand; update the source repo and recopy this file.

## Instructions

- `TEST-AVOID-OPAQUE-BOOLEAN-ASSERTIONS`: Use boolean assertions when the boolean is the useful
  actual value. When a predicate hides diagnostic state, choose a comparison, snapshot, contextual
  predicate, or small domain assertion helper that exposes the relevant actual value without
  printing excessive or sensitive data.
- `TEST-OPTIMIZE-FAILURE-OUTPUT`: Optimize tests for useful failure output because a passing test is
  useful, but a failing test is where maintainers and agents spend repair time.
- `TEST-SPLIT-UNRELATED-ASSERTIONS`: Split unrelated assertions because one failing check would hide
  the real scope or cause of a regression.
