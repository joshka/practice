# Rust Validate Rust Docs As Code

## Metadata

- Name: `Validate Rust Docs As Code`
- ID: `RUST-VALIDATE-RUST-DOCS-AS-CODE`
- Summary: Treat Rust documentation examples, links, feature assumptions, and generated README
  content as code that must be checked. Use docs builds, doctests, feature-gated checks, and
  Markdown lint according to the changed surface.
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Validate Rust docs as code.

## Why

Rust documentation often contains imports, feature assumptions, examples, generated README content,
and links that users copy directly. Docs drift when they are only rendered at release time or when
feature-gated examples are never built with the feature they describe.

Build docs in CI with warnings denied when the project is ready for that bar. Run doctests when
editing public Rustdoc, run feature-gated integration tests when changing integrations, and lint
Markdown structure so docs remain readable.

## Helps

- Helps Rust documentation stay executable, linked, and aligned with the crate's public behavior.

## Limits

Some examples require external services or platforms. Mark noncompiling examples honestly and cover
the behavior with integration or manual validation where practical.

## Agent Instruction

After Rust documentation changes, run the relevant docs build, doctests, feature-gated checks, and
Markdown lint for the changed surface.

## Mechanisms

Supported by `cargo doc`, `RUSTDOCFLAGS=-D warnings`, doctests, feature-gated tests,
`markdownlint-cli2`, and README generation checks.

## References

- [rustdoc book: Documentation tests](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html)
- [Rule: TEST-RUN-DOCS-AS-FIRST-CLASS-GATE](../testing/test-run-docs-as-first-class-gate.md)
- [Rule: DOCS-KEEP-MARKDOWN-LINTABLE](../documentation/docs-keep-markdown-lintable.md)
