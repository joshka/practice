# Source And Context Hygiene

Source hygiene rules cover turning mined lessons into public guidance, preferring stable sources,
keeping binary artifacts out of history, and keeping local or private context out of shared
artifacts.

Use this index to scan the domain and jump to the rule files. The one-line summaries are
for orientation; the rule files hold the rationale, limits, mechanisms, and references.

## Rules

- [`SOURCE-GENERALIZE-PROJECT-SPECIFIC-RULES`](source-generalize-project-specific-rules.md). Extract
  the portable failure mode before promoting local lessons into shared guidance. Provider, repo, or
  tool details should stay local unless they clarify the durable rule.
- [`SOURCE-KEEP-BINARIES-OUT-OF-SOURCE-CONTROL`](source-keep-binaries-out-of-source-control.md).
  Store large or opaque artifacts in systems designed for assets, releases, CI evidence, or external
  data. Keeping source history textual and reviewable avoids clone cost and painful history
  rewrites.
- [`SOURCE-MAKE-SHARED-ARTIFACTS-STANDALONE`](source-make-shared-artifacts-standalone.md). Restate
  the problem, rationale, evidence, and tradeoffs in artifacts that leave the local session. Future
  readers should not need private notes or transcripts to trust the result.
- [`SOURCE-PREFER-PRIMARY-STABLE-SOURCES`](source-prefer-primary-stable-sources.md). Anchor durable
  guidance in sources readers can inspect, compare, and challenge. Use links to clarify judgment,
  not to decorate rules or depend on private memory.
