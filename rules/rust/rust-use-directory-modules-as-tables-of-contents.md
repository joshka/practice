# Rust Use Directory Modules As Tables Of Contents

## Metadata

- Name: `Use Directory Modules As Tables Of Contents`
- ID: `RUST-USE-DIRECTORY-MODULES-AS-TABLES-OF-CONTENTS`
- Summary: Let directory module files introduce, organize, and re-export the concepts owned by that
  directory. Keep substantial implementation in named child files so the module remains a readable
  table of contents.
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Use directory-root modules as tables of contents.

## Why

A directory-root module should orient readers to the submodules it owns. Keeping it as a table of
contents, facade, or small coordinator prevents it from becoming another giant module hidden inside
a directory.

## Helps

Helps directory modules orient readers to submodules and public exports instead of hiding
implementation in a large `mod.rs`.

## Limits

Small directory roots can contain a little glue. Move real behavior into named files once the root
stops acting like a map.

## Agent Instruction

Use directory-root modules as tables of contents because a directory-root module should orient readers
to the submodules it owns.

## Mechanisms

Keep directory-root modules focused on docs, `mod` declarations, facade re-exports, and high-level
orientation. Put implementation in named sibling files.

## References

- [Rust Reference: modules and source files](https://doc.rust-lang.org/reference/items/modules.html)
- [Rust API Guidelines: crate-level docs are
  thorough](https://rust-lang.github.io/api-guidelines/documentation.html#c-crate-doc)
