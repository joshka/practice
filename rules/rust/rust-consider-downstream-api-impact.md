# Rust Consider Downstream API Impact

## Metadata

- Name: `Consider Downstream API Impact`
- ID: `RUST-CONSIDER-DOWNSTREAM-API-IMPACT`
- Summary: Check public API changes against downstream imports, traits, inference, and examples
  before reshaping them. Additive paths and deprecations often avoid unnecessary breakage.
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Consider downstream impact before changing public API.

## Why

Changing a public Rust API can break external imports, trait impls, type inference, docs, examples,
and semver expectations. Before renaming or replacing public items, consider additive APIs,
deprecations, and external usage evidence.

## Helps

Helps library maintainers avoid turning local cleanup into downstream breakage across imports,
examples, trait impls, type inference, and semver expectations.

## Limits

Breaking changes are sometimes correct when an API is unsound, misleading, or blocking important
design repair. Make the break explicit and provide a migration path when possible.

## Agent Instruction

Consider downstream impact before changing public API because changing a public Rust API can break
external imports, trait impls, type inference, docs, examples, and semver expectations.

## Mechanisms

Prefer additive APIs, deprecations, compatibility shims, release notes, external usage searches,
semver checks, and migration examples before removing or renaming public items.

## References

- [Cargo Book: SemVer compatibility](https://doc.rust-lang.org/cargo/reference/semver.html)
- [Rust API Guidelines: public dependencies are
  stable](https://rust-lang.github.io/api-guidelines/necessities.html#c-stable)
