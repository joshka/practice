# Rust Do Not Pin Patch Versions

## Metadata

- ID: `RUST-DO-NOT-PIN-PATCH-VERSIONS`
- Legacy ID: `R-0244`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Do not pin patch versions in `Cargo.toml` unless the patch is required.

## Why

A patch-pinned dependency requirement in `Cargo.toml` raises the minimum version for every
downstream resolver even when any compatible patch would work. Use the widest honest semver
requirement and let lockfiles carry newer compatible releases.

## Helps

Helps downstream users keep compatible dependency graphs flexible and avoids raising minimum
versions just because local lockfiles are newer.

## Limits

Pin or require a patch version when the crate uses an API, behavior fix, security fix, or
compatibility change introduced in that patch.

## Agent Instruction

Avoid patch-pinned `Cargo.toml` requirements unless the patch supplies an API, behavior, or fix the
crate actually needs.

## Mechanisms

Express the lowest honest manifest requirement, let lockfiles carry newer compatible releases, and
validate with minimal-version checks when dependency floors matter.

## References

- [Cargo Book: specifying
  dependencies](https://doc.rust-lang.org/cargo/reference/specifying-dependencies.html)
- [Cargo Book: SemVer compatibility](https://doc.rust-lang.org/cargo/reference/semver.html)
