# Rust Keep Markdown Outside Rustdoc Purposeful

## Metadata

- ID: `RUST-KEEP-MARKDOWN-OUTSIDE-RUSTDOC-PURPOSEFUL`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Use Markdown docs for Rust material that does not fit in Rustdoc or README.

## Why

Rustdoc is best for API contracts and examples near the items users call. README files are best as
entry points. Standalone Markdown is useful for architecture, contributor workflow, long guides,
release process, design history, or operational notes that would make API docs noisy.

Choosing the wrong home makes docs harder to keep current. API contracts drift when they live only
in prose guides, and long workflow explanations bury item docs when they are forced into Rustdoc.

## Helps

- Helps each Rust documentation surface carry the kind of information readers expect there.

## Limits

Duplicate only the smallest useful summary across surfaces, then link to the canonical detail.
Avoid private or checkout-specific material in shared Markdown docs.

## Agent Instruction

Keep Rust API contracts in Rustdoc, README entry points in README, and use Markdown guides for
long-form workflow, architecture, or process material.

## Mechanisms

Supported by docs maps, README/Rustdoc alignment checks, markdown lint, and rendered docs review.

## References

- [Rule: DOCS-CHOOSE-DOCUMENT-TYPE](../documentation/docs-choose-document-type.md)
- [Rule: DOCS-README-AS-ENTRY-POINT](../documentation/docs-readme-as-entry-point.md)
