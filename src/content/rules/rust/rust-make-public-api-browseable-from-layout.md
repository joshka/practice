# Rust Make Public API Browseable From Layout

## Metadata

- Name: `Make Public API Browseable From Layout`
- ID: `RUST-MAKE-PUBLIC-API-BROWSEABLE-FROM-LAYOUT`
- Summary: Align public modules, re-exports, and source files so readers can navigate from API to
  ownership without translation. Facades are fine when they improve discovery and still point toward
  the owning concept.
- Status: `reviewed`
- Domain: `rust`
- Tags: `rust, public-api, reader-locality, ownership`
- Related: `rust-reexport-for-discovery, rust-expose-primary-path-from-crate-root, reader-locality`

## Rule

Make the public API browseable from the file layout.

## Why

When public modules, re-exports, and files disagree, users and maintainers must translate between
Rustdoc paths and source paths. A browseable layout lets readers move from crate root to module to
owned concept without chasing hidden facades or arbitrary helper buckets.

Ed Page's Rust style guide phrases this as the API being a subset of the file layout: what users know
from the public API should help them browse toward the code or at least the parent directory that
owns it. That does not mean every private implementation path is public; it means the public map and
source map should not contradict each other.

## Helps

- Helps source browsing, Rustdoc navigation, and review align around the same conceptual map.

## Limits

Implementation details do not need to mirror every public path. Facades are useful when they
improve discovery and still preserve clear ownership. Compatibility facades can preserve older
paths, but they should point toward the owning module instead of becoming a second owner.

## Agent Instruction

Align Rust public modules, files, and re-exports so readers can browse from public API to owning
source without translation.

## Mechanisms

Supported by crate-root docs, module docs, explicit re-exports, and public API review.

## References

- [Ed Page Rust Style: API is a subset of file layout](https://epage.github.io/dev/rust-style/#api-is-a-subset-of-file-layout-p-api)
- [rustdoc book: Re-exports](https://doc.rust-lang.org/rustdoc/write-documentation/re-exports.html)
- [Rule: RUST-REEXPORT-FOR-DISCOVERY](rust-reexport-for-discovery.md)
