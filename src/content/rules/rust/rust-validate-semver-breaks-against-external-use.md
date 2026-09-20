# Rust Validate Semver Breaks Against External Use

## Metadata

- Name: `Validate Semver Breaks Against External Use`
- ID: `RUST-VALIDATE-SEMVER-BREAKS-AGAINST-EXTERNAL-USE`
- Summary: Check semver-breaking changes against real examples, dependents, or migration paths
  before treating an API cleanup as cheap. External evidence informs the cost even when security,
  soundness, or design repair still justify the break.
- Status: `reviewed`
- Domain: `rust`
- Tags: `rust, public-api, verification, release`
- Related: `public-api-changes-have-downstream-cost, rust-consider-downstream-api-impact`

## Rule

Classify compatibility against supported external use before recommending a release increment.

## Why

Semver tools can detect many API breaks, but real downstream code shows how the public surface is
actually used. Validate breaking changes against external examples or known users before assuming
migration cost is acceptable.

Name the baseline release, affected crate, target, enabled features, and downstream use before
calling a change breaking. Compare the same consumer on both versions. Public trait guarantees,
including auto-traits arising from private fields, belong in this comparison.

A target that already fails to compile on the baseline does not by itself demonstrate a new
regression. Check earlier supported releases in the same compatibility line when a recent
regression may have hidden an established contract. Distinguish a proven break from a preference
for consistent APIs on newly supported targets.

Every library PR review should state breaking, non-breaking, or uncertain, the affected crates,
and the release consequence under repository policy. Explain uncertainty with the missing baseline
or consumer check. For pre-1.0 crates, use the project's compatibility policy and Cargo's version
resolution conventions rather than assuming that all changes require a major-version increment.

## Helps

Helps distinguish theoretical API cleanup from real downstream breakage, especially for library
crates with examples, tutorials, and external dependents.

## Limits

External usage searches are evidence, not veto power. Security, soundness, correctness, or strategic
API repair can justify a break with clear release notes.

A minimal legal downstream example can demonstrate a contract break; finding a named production
consumer is not required. Conversely, a search that finds no consumers does not prove compatibility.

## Agent Instruction

State breaking, non-breaking, or uncertain, affected crates, and release impact under project policy.
Compare supported baseline and candidate consumer configurations, including target, features, and
auto-traits; separate demonstrated regressions from design preferences and missing evidence.

## Mechanisms

Use public API diff tools, crater-like checks where available, reverse-dependency searches, example
builds, migration notes, and explicit semver labeling.

## References

- [Cargo Book: SemVer compatibility](https://doc.rust-lang.org/cargo/reference/semver.html)
- [cargo-semver-checks README](https://github.com/obi1kenobi/cargo-semver-checks#readme)
