# Docs Are Contracts

Documentation rules cover docs-as-contracts, rendered docs, examples, reviewability, source links,
concrete prose, and drift checks.

Use this index to scan the domain and jump to the rule files. The one-line summaries are
for orientation; the rule files hold the rationale, limits, mechanisms, and references.

## Rules

- [`DOCS-ALIGN-README-AND-CRATE-RUSTDOC`](docs-align-readme-and-crate-rustdoc.md). Keep crate README
  and crate-level Rustdoc aligned. Crate users often meet the README on GitHub and the crate-level
  Rustdoc on docs.rs. Helps: Keeps the two main Rust entry points coherent and reduces drift between
  examples, feature flags, and public API claims.
- [`DOCS-AVOID-GENERATED-PROSE-TELLS`](docs-avoid-generated-prose-tells.md). Avoid generated-prose
  tells. Generated prose often sounds polished while hiding that it did not learn the project voice.
  Helps: Preserves local voice, keeps docs dense, and makes claims easier to verify.
- [`DOCS-AVOID-UNEARNED-PRAISE`](docs-avoid-unearned-praise.md). Avoid unearned ranking and vague
  praise. Words such as "simple," "powerful," "best," and "easy" are often unearned unless the doc
  states the comparison or tradeoff. Helps: Keeps claims credible and replaces praise with
  observable behavior, constraints, or tradeoffs.
- [`DOCS-BUILD-DOCS-LIKE-USERS-READ-THEM`](docs-build-docs-like-users-read-them.md). Build Rust docs
  the way users will read them. Rust docs are consumed through rendered Rustdoc, docs.rs feature
  configuration, intra-doc links, search, and examples. Helps: Catches rendered-doc failures and
  makes documentation review match the user-facing artifact.
- [`DOCS-CHOOSE-DOCUMENT-TYPE`](docs-choose-document-type.md). Choose the document type before
  editing. A page that mixes tutorial, reference, explanation, decision record, and changelog work
  makes every reader pay for every mode. Helps: Keeps docs navigable and prevents local edits from
  expanding into accidental page rewrites.
- [`DOCS-COMPARE-LIBRARIES-ACCURATELY`](docs-compare-libraries-accurately.md). Compare nearby
  libraries accurately and charitably. Comparisons with nearby libraries affect trust. Helps: Makes
  comparison docs credible and helps users choose based on real constraints instead of positioning
  language.
- [`DOCS-DOCUMENT-LIFECYCLE-AND-SIDE-EFFECTS`](docs-document-lifecycle-and-side-effects.md).
  Document lifecycle, ownership, side effects, feature flags, platform assumptions, and
  compatibility when callers need them. APIs that open files, spawn tasks, touch terminals, allocate
  resources, mutate global state, enable feature flags, or depend on platform behavior create
  obligations for callers. Helps: Makes caller obligations visible and reduces misuse around
  runtime, platform, feature, and cleanup behavior.
- [`DOCS-EXPOSE-MOVE-RISK-AND-EXAMPLE-IN-PATTERNS`](docs-expose-move-risk-and-example-in-patterns.md).
  Expose symptom, move, risk, example, and agent instruction in pattern-style guidance.
  Pattern-style guidance is useful when a reader can recognize the situation and apply the move.
  Helps: Makes patterns reviewable, teachable, and usable as agent instructions instead of vague
  slogans.
- [`DOCS-FRONT-LOAD-USEFUL-POINT`](docs-front-load-useful-point.md). Front-load the useful point.
  Readers scan docs for the decision, command, invariant, or warning that matters. Helps: Improves
  scanning and makes important commands, contracts, and caveats harder to miss.
- [`DOCS-KEEP-MARKDOWN-LINTABLE`](docs-keep-markdown-lintable.md). Keep Markdown lintable.
  Formatting drift adds review noise and makes generated or agent-edited docs harder to maintain.
  Helps: Keeps documentation diffs clean and makes style expectations enforceable by tools.
- [`DOCS-MAKE-REVIEW-EASY-TO-INSPECT`](docs-make-review-easy-to-inspect.md). Make documentation
  review easy to inspect. Docs are often reviewed as Markdown diffs even though users read rendered
  pages, generated Rustdoc, examples, screenshots, or command output. Helps: Speeds review and makes
  documentation proof concrete rather than confidence-based.
- [`DOCS-MARK-NONCOMPILING-EXAMPLES-HONESTLY`](docs-mark-noncompiling-examples-honestly.md). Prefer
  examples that compile, and mark noncompiling examples honestly. Rust examples are often copied
  directly into user projects or enforced as doctests. Helps: Keeps examples trustworthy and lets
  doctests protect public API usage where possible.
- [`DOCS-MATCH-PAGE-SHAPE-TO-READER-TASK`](docs-match-page-shape-to-reader-task.md). Match each
  rendered documentation page shape to the reader task it serves. A documentation site can use
  Markdown as its source without making every page feel like raw Markdown. Helps: Keeps navigation
  pages from turning into README dumps. - Makes links, tags, cards, rows, code blocks, and source
  metadata behave consistently. - Gives first-time readers a clear answer to where they are, what
  the page is for, and what to click next.
- [`DOCS-ONE-DOMINANT-MODE-PER-PAGE`](docs-one-dominant-mode-per-page.md). Pick one dominant
  documentation mode per page. A page with competing modes forces readers to switch mental models.
  Helps: Keeps each page useful for its main reader and moves secondary detail to better-linked
  places.
- [`DOCS-PROSE-FOR-RELATIONSHIPS-LISTS-FOR-ENUMERATION`](docs-prose-for-relationships-lists-for-enumeration.md).
  Use prose for relationships and lists for enumeration. Lists are good for fields, steps, options,
  and checks, but weak for explaining causality. Helps: Makes explanations coherent while keeping
  procedural or enumerated material easy to scan.
- [`DOCS-PROVE-REAL-USE-WITH-EXAMPLES`](docs-prove-real-use-with-examples.md). Prove real use with
  examples. Examples that only construct a type or call the happy-path function do not prove that
  the API works in the way users need. Helps: Turns examples into contract evidence and prevents
  shallow examples from hiding missing integration details.
- [`DOCS-PUT-UNCERTAINTY-IN-TRACKED-PLACES`](docs-put-uncertainty-in-tracked-places.md). Put
  uncertainty in issues, ADRs, or roadmaps rather than burying it in user docs. User docs should
  describe what is true now. Helps: Keeps user docs authoritative while preserving uncertainty in
  places where it can be tracked and resolved.
- [`DOCS-README-AS-ENTRY-POINT`](docs-readme-as-entry-point.md). Keep README files as entry points.
  A README is usually the first page for humans and agents. Helps: Gives new readers a reliable
  starting path without duplicating every reference detail.
- [`DOCS-SHOW-SIDE-EFFECTS-IN-LIVE-EXAMPLES`](docs-show-side-effects-in-live-examples.md). Show side
  effects and cleanup in live-resource examples. Examples that create files, hit networks, write DNS
  records, open terminals, spawn tasks, or mutate external services can look harmless while leaving
  persistent state or requiring cleanup. Helps: Reduces unsafe copy-paste behavior and makes
  live-resource examples honest about their effects.
- [`DOCS-STATE-CURRENT-BEHAVIOR-NOT-ASPIRATION`](docs-state-current-behavior-not-aspiration.md).
  State current behavior, not aspiration. Docs that describe intended behavior as if it already
  exists become false contracts. Helps: Keeps docs trustworthy and prevents roadmaps from
  masquerading as API or behavior guarantees.
- [`DOCS-TREAT-DOCS-AS-CONTRACTS`](docs-treat-docs-as-contracts.md). Treat docs as contracts. Docs
  increasingly guide both humans and agents. Helps: Aligns code, tests, examples, and agent behavior
  around explicit English-language contracts.
- [`DOCS-USE-CONCRETE-DETAILS`](docs-use-concrete-details.md). Use concrete nouns and real paths,
  defaults, commands, and examples. Abstract nouns make readers infer the actual object. Helps:
  Makes guidance easier to apply, review, and encode for agents.
- [`DOCS-USE-DESCRIPTIVE-HEADINGS`](docs-use-descriptive-headings.md). Use headings that describe
  the section content instead of slogan-like instructions. Headings are navigation. Helps: Makes
  pages easier to skim, search, link, and navigate non-linearly.
- [`DOCS-USE-SOURCE-LINKS-AS-SUPPORT`](docs-use-source-links-as-support.md). Use source links as
  support, not as wording supply. External sources should help a reader verify a claim or compare
  judgment, not supply phrasing. Helps: Keeps guidance original, source-backed where useful, and
  free of accidental paraphrase or citation theater.
- [`DOCS-VERIFY-COMMANDS-PATHS-AND-LINKS`](docs-verify-commands-paths-and-links.md). Verify example
  commands, file paths, and linked references. Commands, paths, and links are executable
  instructions in disguise. Helps: Keeps docs operationally accurate and reduces repair time for
  readers following examples.
- [`DOCS-WRITE-FOR-NON-LINEAR-READERS`](docs-write-for-non-linear-readers.md). Write docs for
  non-linear readers. Many readers do not read documentation front to back. Helps: Makes sections
  useful when linked directly and improves agent retrieval quality.
- [`DOCS-WRITE-TECHNICAL-PROSE`](docs-write-technical-prose.md). Write technical docs, not
  marketing, coaching, or chat. Technical docs should help readers make correct decisions. Helps:
  Keeps documentation direct, actionable, and grounded in behavior rather than persuasion.
