# Source Keep Binaries Out Of Source Control

## Metadata

- Name: `Keep Binaries Out of Source Control`
- ID: `SOURCE-KEEP-BINARIES-OUT-OF-SOURCE-CONTROL`
- Summary: Store large or opaque artifacts in systems designed for assets, releases, CI evidence, or
  external data. Keeping source history textual and reviewable avoids clone cost and painful history
  rewrites.
- Status: `reviewed`
- Domain: `source`
- Depth: `expanded`

## Rule

Keep binary artifacts out of source control.

## Why

Git history is optimized for source changes, not large opaque blobs. A compiled binary, archive,
video, large image, dataset, model file, database dump, or generated package can make every clone,
fetch, cache, and history operation more expensive long after the file disappears from the current
tree. Deleting the file in a later commit does not remove the old blob from history; removing it
after publication usually means rewriting history and coordinating every downstream clone.

Binary artifacts also hide review meaning. A reviewer can inspect source, generated text, and small
fixtures in a diff. A binary blob often only says "something changed," which forces trust in the
producer instead of review of the artifact. If the binary is an output, the source, command, and
provenance usually belong in source control, while the built artifact belongs in an artifact store.

Prefer storage that matches the artifact's role:

- Use Git LFS for large versioned assets that must travel with the repository.
- Use release assets for downloadable build outputs, installers, archives, and distributable
  packages.
- Use issue or PR uploads for review-only screenshots, recordings, logs, and one-off evidence.
- Use CI artifacts for temporary build outputs and validation evidence.
- Use object storage, package registries, model registries, or dataset hosting for large external
  assets with their own lifecycle.
- Store the generator, manifest, checksum, URL, or reproduction command in source control when the
  artifact can be rebuilt or fetched.

## Helps

- Keeps clones, fetches, CI caches, and history traversal fast; avoids history rewrites for
  accidental large files; keeps review focused on source and provenance; and separates release,
  PR, CI, and long-lived asset lifecycles from source history.

## Limits

Small stable binary files can belong in source control when they are truly source assets for the
project: icons, tiny fixtures, fonts, golden files, or documentation images that are needed to build,
test, or understand the repo. Make that choice intentionally. Prefer the smallest representative
fixture, document why it is checked in, and avoid frequently changing binary snapshots when text,
structured data, or generated fixtures would prove the same behavior.

Do not replace source-control bloat with inaccessible storage. If an external asset is needed for
builds or tests, document the fetch path, checksum or version, retention expectation, and offline
failure mode.

## Agent Instruction

Keep binary artifacts out of Git history; use Git LFS, release assets, PR uploads, CI artifacts, or
external storage instead.

## Mechanisms

Supported by `.gitignore` entries for build outputs and archives, Git LFS tracking rules in
`.gitattributes`, pre-commit or CI file-size checks, package and release upload workflows, PR or
issue uploads for review evidence, and handoffs that link to artifacts instead of committing them.

## References

- [GitHub Docs: Managing large files](https://docs.github.com/en/repositories/working-with-files/managing-large-files)
- [GitHub Docs: About Git Large File Storage](https://docs.github.com/articles/about-large-file-storage)
- [GitHub Docs: Removing sensitive data from a repository](https://docs.github.com/articles/remove-sensitive-data)
- [GitHub Docs: Attaching files](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/attaching-files)
- [GitHub Docs: About releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)
