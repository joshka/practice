# Rust Format Docs And Comments Consistently

## Metadata

- Name: `Format Docs and Comments Consistently`
- ID: `RUST-FORMAT-DOCS-AND-COMMENTS-CONSISTENTLY`
- Summary: Apply stable formatting to Rustdoc, examples, attributes, and prose comments. Consistent
  source formatting keeps docs readable and prevents noisy future diffs.
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Format Rust docs and comments consistently.

## Why

Rustdoc examples, doc attributes, imports, and prose comments are part of the source readers review.
Inconsistent formatting makes docs harder to scan and creates noisy diffs when future edits run
formatters.

Use the project's formatter support for doc-comment code blocks and doc attribute normalization
when it is stable for the project. Wrap prose comments near the repo's prose line length so source
review remains readable.

## Helps

- Helps Rust docs, examples, imports, and comments produce stable diffs and readable source.

## Limits

Do not force formatter options that are unstable for the project's toolchain or that churn the code
base without a clear benefit.

## Agent Instruction

Format Rust doc-comment code, doc attributes, grouped imports, and prose comments with the
project's formatter conventions.

## Mechanisms

Supported by rustfmt, `format_code_in_doc_comments`, `normalize_doc_attributes`, markdown lint,
and docs builds.

## References

- [rustfmt configuration](https://rust-lang.github.io/rustfmt/)
- [rustdoc book: Documentation tests](https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html)
