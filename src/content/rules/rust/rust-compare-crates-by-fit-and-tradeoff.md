# Rust Compare Crates By Fit And Tradeoff

## Metadata

- Name: `Compare Crates by Fit and Tradeoff`
- ID: `RUST-COMPARE-CRATES-BY-FIT-AND-TRADEOFF`
- Summary: Compare adjacent crates by intended fit, scope, and constraints instead of broad
  superiority claims. This helps users choose without turning docs into brittle marketing.
- Status: `reviewed`
- Domain: `rust`
- Tags: `rust, dependencies, documentation, source-truth`
- Related: `label-doc-claims-by-evidence, SOURCE-PREFER-PRIMARY-STABLE-SOURCES`

## Rule

Compare nearby Rust crates by fit, scope, and tradeoff.

## Why

Rust ecosystems often have several crates solving adjacent problems. Public docs that claim a crate
is simply better, simpler, faster, or more modern than alternatives make users distrust the page and
age poorly as dependencies evolve.

Useful comparisons name the intended fit: supported platforms, feature policy, dependency surface,
performance tradeoffs, API style, maintenance scope, and interoperability. That helps users choose
without turning documentation into marketing.

## Helps

- Helps users understand when this crate is the right tool without misrepresenting alternatives.

## Limits

Do not add comparison sections when they are not part of the reader's decision. Keep comparisons
short, charitable, and source-backed when factual claims are likely to change.

## Agent Instruction

Compare Rust crates accurately and charitably by fit, scope, and tradeoff, not universal
superiority.

## Mechanisms

Supported by documentation review, source-backed claims, example matrices, and release review when
comparison claims mention versioned behavior.

## References

- [Rule: DOCS-COMPARE-LIBRARIES-ACCURATELY](../documentation/docs-compare-libraries-accurately.md)
- [Rule: DOCS-AVOID-UNEARNED-PRAISE](../documentation/docs-avoid-unearned-praise.md)
