# Rust Keep Dependency Updates Intentional

## Metadata

- ID: `RUST-KEEP-DEPENDENCY-UPDATES-INTENTIONAL`
- Legacy ID: `none`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Keep Rust dependency updates intentional and low-noise.

## Why

Dependency updates can change parsing behavior, trait implementations, feature resolution, MSRV,
platform support, compile time, and downstream integration even when the manifest requirement looks
semver-compatible. Maintenance-only updates should be easy to review, while behavior-affecting
updates deserve their own validation and release notes.

Grouped automation reduces review noise, but it should not hide semver-incompatible behavior or
raise minimum versions without a reason. Use dependency-management commands when they keep
`Cargo.toml`, lockfiles, and feature metadata consistent better than hand edits.

## Helps

- Helps dependency maintenance stay reviewable without surprising downstream users.

## Limits

Security fixes, yanked versions, and ecosystem breakage may require focused urgent updates. Keep the
reason visible and validate the affected public surface.

## Agent Instruction

Group routine Rust dependency updates, separate behavior-affecting updates, and use Cargo-aware
commands to preserve manifest consistency.

## Mechanisms

Supported by `cargo update`, `cargo add`, dependency bots, lockfile review, MSRV checks, feature
matrix checks, and semver or downstream tests.

## References

- [Cargo Book: specifying dependencies](https://doc.rust-lang.org/cargo/reference/specifying-dependencies.html)
- [Rule: RUST-KEEP-COMPATIBLE-UPDATES-IN-LOCKFILE](rust-keep-compatible-updates-in-lockfile.md)
- [Rule: RUST-USE-HONEST-MINIMUM-DEPENDENCIES](rust-use-honest-minimum-dependencies.md)
