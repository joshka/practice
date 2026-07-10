# Rust Expose Primary Path From Crate Root

## Metadata

- Name: `Expose Primary Path from Crate Root`
- ID: `RUST-EXPOSE-PRIMARY-PATH-FROM-CRATE-ROOT`
- Summary: Make the crate root show the main workflow, types, and import path. Users should not
  have to infer the intended entry point from private layout details.
- Status: `reviewed`
- Domain: `rust`
- Tags: `rust, public-api, reader-locality, rustdoc, module-layout`
- Related: `RUST-TEACH-CRATE-FROM-CRATE-ROOT, RUST-REEXPORT-FOR-DISCOVERY`

## Rule

Expose the crate's primary path from the crate root.

## Why

The crate root is the landing page for Rustdoc and the first import path many users try. It should
show the main workflow, primary types, feature flags, and pointers to deeper modules instead of
forcing users to discover the crate through private layout details.

The Rust API Guidelines call for thorough crate-level docs with examples. That only works when the
crate root also exposes the intended path: the primary type, trait, function, or module should be
visible enough that the first example and the public facade tell the same story.

## Helps

- Helps users find the intended starting point and helps maintainers keep facade shape intentional.

## Limits

Do not flatten every module into the crate root. Re-export the canonical entry points and link to
deeper modules for specialized behavior. Leave niche integrations and low-level extension points in
their owning modules when root-level exposure would make the API look broader than it is.

## Agent Instruction

Make `lib.rs` teach and expose the primary crate path while pointing readers to deeper modules.

## Mechanisms

Supported by crate-level Rustdoc, intentional `pub use`, examples, and docs.rs rendering checks.

## References

- [Rust API Guidelines: Crate level docs are thorough and include
  examples](https://rust-lang.github.io/api-guidelines/documentation.html#c-crate-doc)
- [Rule: RUST-TEACH-CRATE-FROM-CRATE-ROOT](rust-teach-crate-from-crate-root.md)
