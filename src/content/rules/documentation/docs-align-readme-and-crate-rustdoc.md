# Docs Align Readme And Crate Rustdoc

## Metadata

- Name: `Align README and Crate Rustdoc`
- ID: `DOCS-ALIGN-README-AND-CRATE-RUSTDOC`
- Summary: `Keep README and crate-level Rustdoc consistent where users learn setup and supported
  behavior. Let the pages serve different tasks, but prevent conflicting contracts.`
- Status: `reviewed`
- Domain: `documentation`
- Tags: `documentation, rustdoc, source-truth, public-api`
- Related: `docs-are-contracts, write-docs-as-contracts, remediate-doc-drift`

## Rule

Keep crate README and crate-level Rustdoc aligned.

## Why

Crate users often meet the README on GitHub and the crate-level Rustdoc on docs.rs. If those two
entry points disagree about features, examples, support status, or the recommended starting API,
users and agents will choose whichever page they saw first and may cargo-cult stale setup code.

## Helps

- Keeps the two main Rust entry points coherent and reduces drift between examples, feature flags,
  and public API claims.

## Limits

The README and crate root do not need identical prose. The README can stay task-first while
crate-level Rustdoc carries API orientation, but they should not contradict each other about current
behavior or setup.

## Agent Instruction

Keep crate README and crate-level Rustdoc aligned because crate users often meet the README on GitHub
and the crate-level Rustdoc on docs.rs.

## Mechanisms

Supported by README/Rustdoc review, doctests for shared examples, docs.rs-style builds, link checks,
and release checks that inspect rendered crate documentation.

## References

- [Principle: Docs Are Contracts](../../principles/docs-are-contracts.md)
- [Diataxis: how to use Diataxis](https://diataxis.fr/how-to-use-diataxis/)
- [Rustdoc: how to write
  documentation](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html)
