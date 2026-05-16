# Docs Are Contracts

Documentation rules cover docs-as-contracts, rendered docs, examples, reviewability, source links,
concrete prose, and drift checks.

Use this index to scan the domain and jump to the rule files. The one-line summaries are
for orientation; the rule files hold the rationale, limits, mechanisms, and references.

## Rules

- [`DOCS-ALIGN-README-AND-CRATE-RUSTDOC`](docs-align-readme-and-crate-rustdoc.md). Keep README and
  crate-level Rustdoc consistent where users learn setup and supported behavior. Let the pages serve
  different tasks, but prevent conflicting contracts.
- [`DOCS-AVOID-GENERATED-PROSE-TELLS`](docs-avoid-generated-prose-tells.md). Replace templated,
  UI-centered, or polished-but-vague phrasing with concrete behavior. Keep the local voice
  trustworthy without cutting useful explanation.
- [`DOCS-AVOID-UNEARNED-PRAISE`](docs-avoid-unearned-praise.md). Replace vague ranking words with
  observable behavior, evidence, or tradeoffs. Use evaluative claims only when the basis is explicit
  enough for readers to verify.
- [`DOCS-BUILD-DOCS-LIKE-USERS-READ-THEM`](docs-build-docs-like-users-read-them.md). Review rendered
  Rust documentation, links, cfg behavior, and examples in the modes users see. Match validation
  depth to the risk of feature, metadata, or public example changes.
- [`DOCS-CHOOSE-DOCUMENT-TYPE`](docs-choose-document-type.md). Pick the dominant document mode
  before editing so the page serves one reader task well. Link out to secondary modes instead of
  blending tutorial, reference, decisions, and changelog.
- [`DOCS-COMPARE-LIBRARIES-ACCURATELY`](docs-compare-libraries-accurately.md). Check current
  upstream behavior before comparing nearby libraries or crates. Charitable, source-backed
  comparisons preserve trust while still helping users choose.
- [`DOCS-DISTINGUISH-EXAMPLE-ROLES`](docs-distinguish-example-roles.md). Name whether an example is
  focused, canonical, survey, integration, or showcase work. That role controls how complete,
  copyable, and validated the example must be.
- [`DOCS-DOCUMENT-LIFECYCLE-AND-SIDE-EFFECTS`](docs-document-lifecycle-and-side-effects.md).
  Document caller-visible lifecycle, ownership, platform, feature, and side-effect obligations. Skip
  internal narration, but make operational responsibilities clear.
- [`DOCS-EXPOSE-MOVE-RISK-AND-EXAMPLE-IN-PATTERNS`](docs-expose-move-risk-and-example-in-patterns.md).
  Give pattern guidance a recognizable trigger, preferred move, risk, example, and agent
  instruction. The extra structure makes repeatable advice easier to cite and apply.
- [`DOCS-FRONT-LOAD-USEFUL-POINT`](docs-front-load-useful-point.md). Put the decision, command,
  invariant, or warning before broad setup. Readers and agents can then use the page without hunting
  through introductory prose.
- [`DOCS-GROUP-RELATED-LIST-ITEMS`](docs-group-related-list-items.md). Cluster long lists under
  useful names when the relationships matter. Keep short or causal material flat or in prose so
  structure does not add noise.
- [`DOCS-HIDE-CATALOG-MECHANICS`](docs-hide-catalog-mechanics.md). Lead user-facing copy with work
  areas, artifacts, and destinations instead of IDs or generated structure. Mention catalog
  mechanics only when citation or contribution work needs them.
- [`DOCS-KEEP-MARKDOWN-LINTABLE`](docs-keep-markdown-lintable.md). Use project Markdown style so
  formatting stays enforceable and review noise stays low. Treat lint exceptions as intentional
  local choices, not accumulated drift.
- [`DOCS-MAKE-GUIDANCE-REVIEW-STATE-VISIBLE`](docs-make-guidance-review-state-visible.md). Mark
  guidance maturity so readers know whether a rule is draft, reviewed, or ready for reuse. Visible
  state prevents tentative advice from becoming an accidental standard.
- [`DOCS-MAKE-REVIEW-EASY-TO-INSPECT`](docs-make-review-easy-to-inspect.md). Package documentation
  changes so reviewers can see scope, evidence, and rendered impact quickly. Small inspectable
  changes reduce hidden drift and style-only review loops.
- [`DOCS-MARK-NONCOMPILING-EXAMPLES-HONESTLY`](docs-mark-noncompiling-examples-honestly.md). Label
  examples that are sketches, partial snippets, or intentionally not run. Honest labels keep readers
  from treating illustrative code as a supported copy-paste contract.
- [`DOCS-MATCH-PAGE-SHAPE-TO-READER-TASK`](docs-match-page-shape-to-reader-task.md). Shape pages
  around the reader's task, such as learning, choosing, reference, or review. The right structure
  lowers scan cost without forcing one page to do every job.
- [`DOCS-NAME-DESTINATION-NOT-DIRECTION`](docs-name-destination-not-direction.md). Use labels that
  name the section, object, or decision the reader will reach. Directional labels make readers
  follow the page order before knowing whether it is relevant.
- [`DOCS-ONE-DOMINANT-MODE-PER-PAGE`](docs-one-dominant-mode-per-page.md). Let each page have one
  primary mode and move competing material behind links. This keeps readers from paying for
  tutorial, reference, explanation, and policy at once.
- [`DOCS-PROSE-FOR-RELATIONSHIPS-LISTS-FOR-ENUMERATION`](docs-prose-for-relationships-lists-for-enumeration.md).
  Use prose when causality, contrast, or priority matters, and lists when enumerating parallel
  items. The shape should reveal the relationship instead of hiding it in bullets.
- [`DOCS-PROVE-REAL-USE-WITH-EXAMPLES`](docs-prove-real-use-with-examples.md). Use examples that
  show realistic ownership, errors, lifecycle, configuration, or integration shape. Keep them
  focused, but make them strong enough to prove the contract.
- [`DOCS-PUT-UNCERTAINTY-IN-TRACKED-PLACES`](docs-put-uncertainty-in-tracked-places.md). Keep user
  docs focused on current truth and move unresolved direction to issues, ADRs, or roadmaps. Track
  speculation where it can be decided instead of implying a promise.
- [`DOCS-README-AS-ENTRY-POINT`](docs-readme-as-entry-point.md). Use README files to orient readers
  to purpose, setup, first useful use, and deeper docs. Split out manual-level detail when it hides
  the starting path.
- [`DOCS-REVIEW-CORRECTNESS-AND-RISK-FIRST`](docs-review-correctness-and-risk-first.md). Lead
  documentation review with false contracts, drift, operability, and unsupported claims before style
  polish. This separates blocking risk from wording cleanup.
- [`DOCS-SHOW-SIDE-EFFECTS-IN-LIVE-EXAMPLES`](docs-show-side-effects-in-live-examples.md). Show
  setup, visible effects, and cleanup when examples touch live resources or persistent state. Gate
  costly or externally visible actions so examples stay honest and safe to adapt.
- [`DOCS-STATE-CURRENT-BEHAVIOR-NOT-ASPIRATION`](docs-state-current-behavior-not-aspiration.md).
  Describe what the system does now and label limitations or future plans separately. Otherwise
  roadmap language becomes a false contract for readers and agents.
- [`DOCS-TREAT-DOCS-AS-CONTRACTS`](docs-treat-docs-as-contracts.md). Treat supported behavior,
  commands, errors, and examples in docs as promises readers may rely on. Separate normative claims
  from background, examples, and future plans.
- [`DOCS-USE-CONCRETE-DETAILS`](docs-use-concrete-details.md). Name real commands, paths, defaults,
  types, examples, and work areas when they clarify scope. Concrete detail removes guesswork without
  overloading prose with incidental facts.
- [`DOCS-USE-DESCRIPTIVE-HEADINGS`](docs-use-descriptive-headings.md). Write headings that name the
  section content, destination, or decision area. Reserve imperative headings for procedures where
  the section is truly a step.
- [`DOCS-USE-SOURCE-LINKS-AS-SUPPORT`](docs-use-source-links-as-support.md). Use references to
  verify, frame, or contrast local guidance instead of supplying the wording. This keeps the repo
  voice original while still making claims checkable.
- [`DOCS-VERIFY-COMMANDS-PATHS-AND-LINKS`](docs-verify-commands-paths-and-links.md). Check commands,
  file paths, and linked references because readers treat them as executable instructions. Note
  assumptions when credentials, services, or platforms prevent a full run.
- [`DOCS-WRITE-FOR-NON-LINEAR-READERS`](docs-write-for-non-linear-readers.md). Give sections enough
  local context to work when reached from search, links, review, or retrieval. Avoid repeating the
  whole introduction; add only the subject and prerequisite needed.
- [`DOCS-WRITE-TECHNICAL-PROSE`](docs-write-technical-prose.md). Use direct technical language that
  carries contracts, commands, evidence, and tradeoffs. Cut marketing, coaching, chat, and page
  narration when they do not explain the system.
