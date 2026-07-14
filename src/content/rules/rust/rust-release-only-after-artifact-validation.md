# Rust Release Only After Artifact Validation

## Metadata

- Name: `Release Only After Artifact Validation`
- ID: `RUST-RELEASE-ONLY-AFTER-ARTIFACT-VALIDATION`
- Summary: Validate the actual release artifact before publishing instead of trusting the working
  tree. This catches missing files, stale generated content, and packaging mistakes while the
  release can still be fixed.
- Status: `reviewed`
- Domain: `rust`
- Tags: `rust, release, verification`
- Related: `rust-validate-package-contents-before-release, report-verification-honestly`

## Rule

Release and tag Rust crates only after validating the package artifact.

## Why

The crate package is the artifact users receive. A working tree can contain files that `cargo
package` excludes, generated content that was not updated, or metadata that disagrees with README,
Rustdoc, changelog, license files, docs.rs config, and support claims.

Dry-run the publish where possible, inspect included artifacts, and tag after the release artifact
is validated. Tagging first makes it harder to repair a bad package without confusing history.

## Helps

- Helps Rust releases avoid missing docs, stale generated files, wrong metadata, and premature tags.

## Limits

Emergency releases may compress the checklist, but they still need artifact validation before
publication whenever possible.

## Agent Instruction

Before publishing or tagging a Rust release, dry-run and inspect the package artifact, metadata,
docs, examples, license files, and generated content.

## Mechanisms

Supported by `cargo package --list`, `cargo publish --dry-run`, docs.rs metadata checks, changelog
review, and release CI.

## References

- [Cargo Book: Publishing on crates.io](https://doc.rust-lang.org/cargo/reference/publishing.html)
- [Rule: RUST-VALIDATE-PACKAGE-CONTENTS-BEFORE-RELEASE](rust-validate-package-contents-before-release.md)
- [Rule: RUST-ALIGN-RELEASE-SUPPORT-CLAIMS](rust-align-release-support-claims.md)
