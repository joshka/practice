# Source And Context Hygiene

Source hygiene rules cover turning mined lessons into public guidance, preferring stable sources,
keeping binary artifacts out of history, and keeping local or private context out of shared
artifacts.

Use this index to scan the domain and jump to the rule files. The one-line summaries are
for orientation; the rule files hold the rationale, limits, mechanisms, and references.

## Rules

- [`SOURCE-GENERALIZE-PROJECT-SPECIFIC-RULES`](source-generalize-project-specific-rules.md).
  Generalize project-specific rules before promotion. Local mining often starts from one repository,
  tool, provider, or incident. Helps: Keeps public guidance broadly reusable while preserving narrow
  lessons for the places where they actually apply.
- [`SOURCE-KEEP-BINARIES-OUT-OF-SOURCE-CONTROL`](source-keep-binaries-out-of-source-control.md).
  Keep binary artifacts out of source control. Git history is optimized for source changes, not
  large opaque blobs. Helps: Keeps clones, fetches, CI caches, and history traversal fast; avoids
  history rewrites for accidental large files; keeps review focused on source and provenance; and
  separates release, PR, CI, and long-lived asset lifecycles from source history.
- [`SOURCE-MAKE-SHARED-ARTIFACTS-STANDALONE`](source-make-shared-artifacts-standalone.md). Make
  issues, PRs, commit messages, docs, and handoffs stand alone. Shared artifacts often leave the
  development session with missing context. Helps: Makes shared work reviewable, auditable, and
  useful to future readers without local source material.
- [`SOURCE-PREFER-PRIMARY-STABLE-SOURCES`](source-prefer-primary-stable-sources.md). Prefer primary
  or stable sources for durable guidance. External references are most useful when they help a
  reader verify, compare, or challenge a rule. Helps: Makes rules easier to audit, easier to justify
  in review, and less dependent on private memory.
