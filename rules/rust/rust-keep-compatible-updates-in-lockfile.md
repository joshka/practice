# Rust Keep Compatible Updates In Lockfile

## Metadata

- Name: `Keep Compatible Updates in Lockfile`
- ID: `RUST-KEEP-COMPATIBLE-UPDATES-IN-LOCKFILE`
- Summary: Let lockfiles record newer compatible dependency versions when the manifest floor has
  not changed. This tests fresh releases without narrowing downstream compatibility.
- Status: `reviewed`
- Domain: `rust`
- Tags: `rust, dependencies, verification`
- Related: `keep-public-dependencies-intentional, RUST-DO-NOT-PIN-PATCH-VERSIONS`

## Rule

Keep compatible dependency updates in the lockfile, not the manifest.

## Why

Compatible dependency updates usually belong in the lockfile, not the manifest requirement. Raising
`Cargo.toml` minimums without needing a new API narrows downstream compatibility and can turn
maintenance refreshes into semver-relevant changes.

## Helps

Helps avoid unnecessary downstream minimum-version bumps while still letting this checkout test with
newer compatible releases.

## Limits

Raise `Cargo.toml` requirements when the code uses a newer API, relies on fixed behavior, addresses
security, or changes the supported dependency floor intentionally.

## Agent Instruction

Keep compatible dependency updates in the lockfile, not the manifest requirement, unless the crate
actually needs the newer version.

## Mechanisms

Keep compatible updates in `Cargo.lock`, use minimal-version checks for floors, configure Dependabot
to update lockfiles when appropriate, and separate dependency-floor changes from routine refreshes.

## References

- [Cargo Book: specifying
  dependencies](https://doc.rust-lang.org/cargo/reference/specifying-dependencies.html)
- [Cargo Book: Cargo.lock](https://doc.rust-lang.org/cargo/guide/cargo-toml-vs-cargo-lock.html)
