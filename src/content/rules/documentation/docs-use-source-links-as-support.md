# Docs Use Source Links As Support

## Metadata

- Name: `Use Source Links as Support`
- ID: `DOCS-USE-SOURCE-LINKS-AS-SUPPORT`
- Summary: `Use references to verify, frame, or contrast local guidance instead of supplying the
  wording. This keeps the repo voice original while still making claims checkable.`
- Status: `reviewed`
- Domain: `documentation`
- Tags: `documentation, source-truth, verification`
- Related: `label-doc-claims-by-evidence, SOURCE-PREFER-PRIMARY-STABLE-SOURCES`

## Rule

Use source links as support, not as wording supply.

## Why

External sources should help a reader verify a claim or compare judgment, not supply phrasing.
Copying source-like wording weakens this repo's own voice and can accidentally import assumptions
that do not match the local preference.

The local explanation should remain usable when a reader cannot open the source. Link directly to a
stable section, change, test, or discussion when it materially supports the claim. Do not expose the
search tool, archive layout, or private research process merely to prove that research happened.

## Helps

- Keeps guidance original, source-backed where useful, and free of accidental paraphrase or citation
  theater.

## Limits

Directly quote only when the exact wording matters and the quote is short. Most guidance should
summarize the local rule, then cite sources as support, contrast, or adaptation. Private or unstable
sources can inform the explanation, but they should not become required context for readers who
cannot access them.

## Agent Instruction

Write a locally sufficient explanation, then use direct stable links to help readers verify or
compare judgment. Do not make discovery tools, private archives, or inaccessible discussion part of
the reader's required path.

## Mechanisms

Supported by source-link cleanup passes, reference tables that state use, and review that checks for
broad root links or source-shaped prose.

## References

- [Principle: Docs Are Contracts](../../principles/docs-are-contracts.md)
- [Diataxis: how to use Diataxis](https://diataxis.fr/how-to-use-diataxis/)
- [Rustdoc: how to write
  documentation](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html)
