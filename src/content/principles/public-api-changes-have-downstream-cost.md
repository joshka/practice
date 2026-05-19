# Public API Changes Have Downstream Cost

## Metadata

- Name: `Public API Changes Have Downstream Cost`
- ID: `public-api-changes-have-downstream-cost`
- Summary: `Public API edits impose migration, semver, documentation, and integration costs beyond
  the local diff. Prefer additive paths and explicit migration proof when a break is justified.`
- Status: `reviewed`
- Audience: `both`
- Topics: `rust, api, semver, libraries`
- Tags: `public-api, dependencies, release, rust`
- Related: `keep-public-dependencies-intentional, document-errors-panics-safety`

## Claim

Public API changes consume downstream attention even when the local diff is small. Prefer additive
APIs, deprecations, and migration paths over renames or replacements unless the break is justified
and validated.

## Why I Believe This

Maintained libraries are used in contexts the maintainer does not see. Local tests can miss example
crates, tutorials, downstream integrations, feature combinations, and users who rely on a type or
module name as part of their own public surface. A small cleanup in one crate can become broad
churn elsewhere.

Semver is the floor, not the whole responsibility. A change can be technically allowed and still be
unhelpful if it forces migration work without enough benefit.

## What This Changes

Before changing public names, modules, errors, features, dependency exposure, or behavior:

1. Identify whether the API is stable, experimental, or pre-1.0.
1. Prefer additive alternatives when the old API can remain.
1. Use deprecation when users need time to migrate.
1. Search for real external use when the break may be meaningful.
1. Validate examples, docs, reverse dependencies, and public API reports.
1. Explain the migration impact in the change or release notes.

## Rust-Specific Guidance

Public Rust API includes more than functions. Types, trait impls, error variants, feature flags,
module paths, dependency types, docs examples, auto traits, MSRV, and minimum dependency versions
can all affect downstream code. Treat them as part of the public contract when maintaining a
library.

## Good Uses

- Add a new constructor while keeping the old one deprecated.
- Introduce a wrapper type before exposing a dependency type directly.
- Keep a compatibility feature while migrating examples.
- Run public API and semver checks before release.
- Build known downstream examples when a break is intentional.

## Bad Smells

- A rename lands because the new name is nicer, without migration value.
- A public dependency type leaks through an API by convenience.
- Examples fail after a dependency update and are treated as local cleanup only.
- A semver break lands with no external-user search or migration note.
- `Cargo.toml` minimums rise just because the lockfile was refreshed.

## Mechanisms

- `cargo-semver-checks`.
- `cargo public-api` snapshots or reports.
- Reverse-dependency builds and known downstream examples.
- GitHub search for public API use.
- Release notes and deprecation messages.
- Minimal-version checks for dependency lower bounds.

## Rules This Supports

- `RUST-KEEP-PUBLIC-API-SHAPE-INTENTIONAL`
- `RUST-AVOID-PUBLIC-DEPENDENCY-COUPLING`
- `RUST-CONSIDER-DOWNSTREAM-API-IMPACT`
- `RUST-VALIDATE-SEMVER-BREAKS-AGAINST-EXTERNAL-USE`
- `RUST-USE-HONEST-MINIMUM-DEPENDENCIES`
- `RUST-KEEP-COMPATIBLE-UPDATES-IN-LOCKFILE`

## Agent Consequences

Before changing public API, identify downstream impact and prefer additive or deprecation-first
paths. For breaking changes, report external-use checks, semver evidence, examples built, and the
recommended migration path.

## Limits

Private crates and explicitly experimental APIs can move faster. Even then, name the scope so the
future reader knows the break was intentional rather than accidental.

## References

| Source                                      | Use        | Note                                             |
| ------------------------------------------- | ---------- | ------------------------------------------------ |
| [Rust API C-STABLE][rust-api-stable]        | `supports` | Public crates should preserve stable contracts.  |
| [Cargo SemVer compatibility][cargo-semver]  | `supports` | Cargo defines compatibility expectations.        |
| [Rust API C-RELNOTES][rust-api-relnotes]    | `supports` | Breaking changes need migration communication.   |

[rust-api-stable]: https://rust-lang.github.io/api-guidelines/necessities.html#c-stable
[cargo-semver]: https://doc.rust-lang.org/cargo/reference/semver.html
[rust-api-relnotes]: https://rust-lang.github.io/api-guidelines/documentation.html#c-relnotes
