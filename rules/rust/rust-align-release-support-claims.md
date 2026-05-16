# Rust Align Release Support Claims

## Metadata

- Name: `Align Release Support Claims`
- ID: `RUST-ALIGN-RELEASE-SUPPORT-CLAIMS`
- Summary: Keep crate metadata, docs, changelogs, and support statements saying the same thing. The
  alignment helps downstream users know which compatibility contract to trust.
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Keep version, changelog, metadata, docs, and support claims aligned.

## Why

Rust releases have several public truth sources: `Cargo.toml`, README, crate Rustdoc, changelog,
docs.rs metadata, examples, and CI support matrices. If they disagree about MSRV, feature flags,
platform support, or version behavior, downstream users cannot tell which contract to trust.

## Helps

Helps release reviewers compare every public claim before publishing and helps downstream users
trust the crate docs, package metadata, and changelog as one contract.

## Limits

Do not block a release on cosmetic duplication between surfaces. Focus on claims that affect
compatibility, support, feature behavior, MSRV, or upgrade decisions.

## Agent Instruction

Keep release claims aligned across `Cargo.toml`, README, Rustdoc, changelog, docs.rs metadata,
examples, and CI support matrices.

## Mechanisms

Check `Cargo.toml`, README, crate-root Rustdoc, changelog, docs.rs metadata, examples, CI matrices,
and release notes during the release pass.

## References

- [Rust API Guidelines: Release notes document breaking
  changes](https://rust-lang.github.io/api-guidelines/documentation.html#c-relnotes)
- [docs.rs: metadata](https://docs.rs/about/metadata)
