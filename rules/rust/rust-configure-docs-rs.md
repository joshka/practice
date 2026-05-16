# Rust Configure Docs rs

## Metadata

- Name: `Configure docs.rs`
- ID: `RUST-CONFIGURE-DOCS-RS`
- Summary: Configure docs.rs metadata when features, cfgs, or rustdoc flags affect rendered API
  docs. Users should see the documentation surface the crate expects to support.
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Configure docs.rs metadata intentionally.

## Why

docs.rs is often the rendered documentation users see first. Feature flags, cfg docs, metadata,
all-features builds, and rustdoc warnings need intentional configuration so docs.rs shows the public
API the crate actually supports.

## Helps

Helps users see the same features, cfg-gated items, and documentation warnings that the crate
expects to support on docs.rs.

## Limits

Simple crates may need no custom docs.rs metadata. Add configuration when feature combinations,
platform cfgs, or rustdoc flags materially change the rendered docs.

## Agent Instruction

Configure docs.rs metadata intentionally because docs.rs is often the rendered documentation users
see first.

## Mechanisms

Use `[package.metadata.docs.rs]`, `all-features` or explicit features, rustdoc cfg flags, and local
`cargo +nightly doc` checks that approximate docs.rs.

## References

- [docs.rs: metadata](https://docs.rs/about/metadata)
- [Rustdoc: documenting
  components](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html#documenting-components)
