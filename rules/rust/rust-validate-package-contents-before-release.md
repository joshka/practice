# Rust Validate Package Contents Before Release

## Metadata

- ID: `RUST-VALIDATE-PACKAGE-CONTENTS-BEFORE-RELEASE`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Validate package contents before release.

## Why

The crate package is what users receive, not the working tree. Validate included files, examples,
README, license, generated artifacts, and buildability before release so publishing does not omit
required assets or include local junk.

## Helps

Helps catch missing README files, examples, license files, generated assets, and accidental
inclusions before publishing an immutable crate package.

## Limits

Internal unpublished crates may not need a full package audit. Published crates should validate the
archive because users install exactly that package, not the working tree.

## Agent Instruction

Validate package contents before release because the crate package is what users receive, not the
working tree.

## Mechanisms

Run `cargo package --list`, inspect included files, build from the packaged crate when needed, and
keep include/exclude rules intentional.

## References

- [Cargo Book: cargo package](https://doc.rust-lang.org/cargo/commands/cargo-package.html)
- [Cargo Book: manifest include and
  exclude](https://doc.rust-lang.org/cargo/reference/manifest.html#the-exclude-and-include-fields)
