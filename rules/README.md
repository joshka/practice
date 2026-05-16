# Rules

Rules are compact instructions supported by the guides, principles, patterns, and
mechanisms in this repo. Each rule has its own file so it can be reviewed, deepened, linked,
and extracted into compressed agent instructions independently.

## Rule File Shape

Each rule file should keep these sections:

- `Metadata`: stable ID, portable name, summary, status, domain, and depth.
- `Rule`: the direct human-readable instruction.
- `Why`: rationale when the rule needs justification or tradeoff framing.
- `Helps`: concrete development outcomes the rule improves.
- `Limits`: exceptions, costs, or counter-signals.
- `Agent Instruction`: compressed wording suitable for agent execution packs.
- `Mechanisms`: lints, formatters, CI checks, commands, or workflows that support the rule.
- `References`: durable sources that support, adapt, or contrast the rule in a useful way.

Rules can stay compact when the rationale is obvious, but compact should still mean finished.
A rule should explain the failure mode, tradeoff, or design pressure well enough that a
reviewer does not need the original source material to understand why it exists. Prefer
concrete surfaces and examples over abstract categories when the reader would otherwise have
to infer applicability.

Agent instructions are not repeated titles. They should encode the trigger, failure mode, or
useful constraint that helps an agent apply the rule without blindly doing the literal
shortest version of the instruction.

## Naming

Use uppercase, dash-separated IDs:

```text
DOCS-TREAT-DOCS-AS-CONTRACTS
RUST-KEEP-PUBLIC-API-SHAPE-INTENTIONAL
VCS-JJ-AS-SOURCE-OF-TRUTH
TEST-OPTIMIZE-FAILURE-OUTPUT
OBSERVABILITY-PRESERVE-OPERATION-CONTEXT-IN-ERRORS
```

Do not abbreviate broad family names in public rule IDs. Use `OBSERVABILITY`, not `OBS`.

Rule IDs are handles, not compressed titles. A good ID is short enough to cite in reviews,
preserves the rule's real concept, and keeps connector words when dropping them would change
the meaning. Prefer a verb-oriented handle when the rule is an action, and use domain nouns
plus a decisive verb and object. Write titles as direct instructions when possible.

## Domains

- [Agent Workflow](agent-workflow/README.md). 26 rules. Agent workflow rules cover objectives,
  scoped capabilities, durable context, review packets, security proof, feedback loops, and concrete
  next choices.
- [Explicit Boundaries Preserve Correctness](boundary/README.md). 26 rules. Boundary rules cover
  parsing, validation policy, explicit inputs, state transitions, provider diagnostics, effect
  boundaries, and external reconciliation.
- [Change Shape](change-shape/README.md). 13 rules. Change-shape rules cover one-purpose changes,
  small follow-ups, generated artifacts, dependency churn, ownership, and structure-versus-behavior
  review boundaries.
- [Docs Are Contracts](documentation/README.md). 33 rules. Documentation rules cover
  docs-as-contracts, rendered docs, examples, reviewability, source links, concrete prose, and drift
  checks.
- [Observability And Failure](observability/README.md). 5 rules. Observability rules cover owned
  logging boundaries, durable failure visibility, diagnostic context, failure states, and safe
  telemetry retention.
- [Measure Before Optimizing](performance/README.md). 7 rules. Performance rules cover measuring
  before optimizing, benchmark provenance, single-run skepticism, correctness gates, and the cost of
  complexity or dependency churn.
- [Local Reasoning And Refactoring](refactoring/README.md). 9 rules. Refactoring rules cover local
  reasoning, concept helpers, visible linear stories, side-effect loops, whitespace paragraphs, DRY
  pressure, and weak abstractions.
- [Private Context And Review Artifacts](review/README.md). 11 rules. Review artifact rules cover
  issue slices, PR narratives, ADRs, speculation labels, thread ownership, and artifacts that stand
  alone without private session context.
- [Rust API And Crate Shape](rust/README.md). 90 rules. Rust rules cover public API shape, crate
  layout, dependency policy, docs.rs behavior, feature flags, public errors, unsafe boundaries, and
  release checks.
- [Source And Context Hygiene](source/README.md). 4 rules. Source hygiene rules cover turning mined
  lessons into public guidance, preferring stable sources, keeping binary artifacts out of history,
  and keeping local or private context out of shared artifacts.
- [Tests Should Explain Failures](test-failures/README.md). 3 rules. Test-failure rules cover
  assertion shape and failure output that help humans and agents diagnose the failing case quickly.
- [Testing And Verification](testing/README.md). 22 rules. Testing rules cover risk-based
  validation, doctests, feature matrices, deterministic tests, parser samples, command construction,
  dependency floors, and regressions.
- [JJ Topology And Source Control](vcs/README.md). 28 rules. VCS rules cover jj-first source-control
  work, remote topology, operation-log recovery, workspaces, publication safety, and file-tracking
  decisions.

## All Rules

### Agent Workflow

- [`AGENT-BUDGET-FOR-FEEDBACK-LOOPS`](agent-workflow/agent-budget-for-feedback-loops.md). Reserve
  enough time and tokens for checks, failure inspection, and handoff proof. Planning for the
  feedback loop keeps validation from being squeezed out after the first edit.
- [`AGENT-DEFINE-GOOD-BEFORE-JUDGMENT-HEAVY-WORK`](agent-workflow/agent-define-good-before-judgment-heavy-work.md).
  State the quality bar before work where taste, naming, API shape, or review expectations matter.
  Clear criteria give the agent goalposts before it creates a large speculative diff.
- [`AGENT-DISTILL-FROM-BLESSED-ARTIFACTS`](agent-workflow/agent-distill-from-blessed-artifacts.md).
  Study accepted code, docs, tests, and reviews first. Adapt local convention to this task.
- [`AGENT-ENCODE-NONFUNCTIONAL-REQUIREMENTS`](agent-workflow/agent-encode-nonfunctional-requirements.md).
  Put invisible constraints such as security, accessibility, latency, and compatibility near the
  task. Encoding them upfront makes those requirements part of the implementation target.
- [`AGENT-GIVE-OBJECTIVES-WITH-BOUNDARIES`](agent-workflow/agent-give-objectives-with-boundaries.md).
  Describe the outcome, scope, non-goals, forbidden moves, and proof instead of handing over brittle
  steps. Boundaries preserve intent while leaving room for local implementation choices.
- [`AGENT-GRANT-SCOPED-CAPABILITIES`](agent-workflow/agent-grant-scoped-capabilities.md). Give
  agents only the permissions and external authority the task actually needs. Scoped capability
  keeps progress possible while reducing accidental mutation, publication, or exposure.
- [`AGENT-ISOLATE-WORKSPACES-BY-TASK`](agent-workflow/agent-isolate-workspaces-by-task.md). Put
  separable or parallel agent work in its own workspace or source-control lane. Isolation keeps
  diffs, validation, and ownership clear when multiple changes are in flight.
- [`AGENT-KEEP-DURABLE-CONTEXT-ON-DISK`](agent-workflow/agent-keep-durable-context-on-disk.md).
  Store project facts, accepted decisions, and long-lived operating notes in files instead of
  relying on chat context. Durable context makes future sessions and reviews resumable.
- [`AGENT-KEEP-SECRETS-OUT-OF-CONTEXT`](agent-workflow/agent-keep-secrets-out-of-context.md). Avoid
  putting real credentials or sensitive values into prompts, docs, logs, and tests. Keeping secrets
  out of context reduces leakage through retained, repeated, or committed text.
- [`AGENT-MAKE-BAD-OUTPUT-HARD`](agent-workflow/agent-make-bad-output-hard.md). Turn recurring bad
  agent output into scripts, templates, lint, or checks that fail fast. Mechanical enforcement
  lowers review cost more reliably than repeated prompt reminders.
- [`AGENT-PREFER-BUILD-PRESERVING-EDITS`](agent-workflow/agent-prefer-build-preserving-edits.md).
  Make multi-step edits in slices that keep compilation or tests close to green when the route
  allows it. Build-preserving work keeps failures close to the edit that caused them.
- [`AGENT-PREFER-IN-DISTRIBUTION-TOOLS`](agent-workflow/agent-prefer-in-distribution-tools.md). Use
  standard project commands, supported CLIs, and documented workflows before inventing ad hoc tool
  paths. Familiar tools reduce misuse and make agent output easier to rerun.
- [`AGENT-PREFER-TOOLS-OVER-PROMPTS`](agent-workflow/agent-prefer-tools-over-prompts.md). Move
  repeated instructions into tools, checks, templates, or durable guides. Tooling catches failures
  even when prompts are short, compacted, or interpreted differently.
- [`AGENT-PRESENT-CONCRETE-NEXT-OPTIONS`](agent-workflow/agent-present-concrete-next-options.md).
  After a validated chunk, offer specific follow-up chunks with their tradeoffs. Concrete options
  let the maintainer steer scope without decoding vague requests to continue.
- [`AGENT-PRESERVE-HUMAN-WORK`](agent-workflow/agent-preserve-human-work.md). Inspect and protect
  unrelated local edits before changing files. Preserving human work keeps the task diff focused and
  avoids destroying unfinished or intentional changes.
- [`AGENT-PRESERVE-INTENT`](agent-workflow/agent-preserve-intent.md). Optimize for the user's
  underlying objective when literal wording would miss the point. Intent-preserving work keeps
  changes aligned with the real readability, review, or behavior goal.
- [`AGENT-PRODUCE-REVIEW-PACKETS`](agent-workflow/agent-produce-review-packets.md). Hand off agent
  work with purpose, changed files, evidence, skipped checks, risks, and follow-ups. A review packet
  lets maintainers inspect the output without replaying the session.
- [`AGENT-PROVE-SECURITY-IMPACT`](agent-workflow/agent-prove-security-impact.md). Separate security
  hypotheses from proof of reachability, exploitability, assets, and user impact. This keeps
  prioritization and mitigation tied to demonstrated risk.
- [`AGENT-REPORT-PROOF-IN-HANDOFFS`](agent-workflow/agent-report-proof-in-handoffs.md). Replace
  confidence language with the exact checks, inspection, screenshots, and skipped validation behind
  a handoff. Proof lets reviewers decide what to trust and what remains risky.
- [`AGENT-REVIEW-OUTPUT-AS-FUTURE-MAINTAINER`](agent-workflow/agent-review-output-as-future-maintainer.md).
  Review agent output as someone who will not have the chat transcript. This keeps attention on
  durable code, docs, tests, validation proof, and residual risk.
- [`AGENT-SEPARATE-NOTES-FROM-CORRECTIONS`](agent-workflow/agent-separate-notes-from-corrections.md).
  Capture fast-review notes before fixing them when there are multiple comments or unclear patterns.
  Separating capture from correction preserves signal and supports coherent follow-up.
- [`AGENT-SPEND-HUMAN-ATTENTION-ON-AMBIGUITY`](agent-workflow/agent-spend-human-attention-on-ambiguity.md).
  Ask for human judgment where product behavior, API compatibility, naming, or security posture is
  still ambiguous. Resolving direction early prevents large speculative diffs.
- [`AGENT-SUGGEST-LOCAL-OVERRIDE-FILES`](agent-workflow/agent-suggest-local-override-files.md). Put
  checkout-only facts in ignored override files instead of shared guidance. Local overrides keep
  machine-specific steering useful without leaking it to every contributor.
- [`AGENT-TURN-FEEDBACK-INTO-GUIDANCE`](agent-workflow/agent-turn-feedback-into-guidance.md).
  Convert repeated review corrections into rules, templates, snippets, or checks. Durable guidance
  fixes the workflow problem instead of requiring the same steering again.
- [`AGENT-USE-AGENTS-MD-AS-MAP`](agent-workflow/agent-use-agents-md-as-map.md). Keep `AGENTS.md`
  compact by using it to route agents to deeper guides and mechanisms. Treating it as a map
  preserves startup context without losing durable project guidance.
- [`AGENT-VERIFY-RISKY-CHANGES-WITH-CANARIES`](agent-workflow/agent-verify-risky-changes-with-canaries.md).
  Use staged rollout, shadowing, dry runs, or partial publication for changes that can fail only
  under real conditions. Canaries reduce blast radius while evidence accumulates.

### Explicit Boundaries Preserve Correctness

- [`BOUNDARY-AVOID-GLOBAL-MUTABLE-STATE`](boundary/boundary-avoid-global-mutable-state.md). Keep
  shared process state behind explicit owners, handles, synchronization, and reset policy. This
  preserves test isolation and lifecycle reasoning while still allowing deliberate globals such as
  caches or registries when their contract is visible.
- [`BOUNDARY-CHOOSE-RESOURCE-IDENTITY-MODEL`](boundary/boundary-choose-resource-identity-model.md).
  Decide whether the boundary mutates records, sets, files, sessions, handles, or whole documents
  before designing reconciliation. The chosen unit controls idempotency, matching, conflict
  handling, and the cost of later migration.
- [`BOUNDARY-DEFINE-COMPACTION-INVARIANTS`](boundary/boundary-define-compaction-invariants.md).
  State the budget and cut-point rules before deleting, summarizing, or moving context. Explicit
  invariants make compaction reviewable and reduce the risk that later work treats lossy or
  nondeterministic summaries as authoritative.
- [`BOUNDARY-DEFINE-HOOK-FAILURE-POLICY`](boundary/boundary-define-hook-failure-policy.md). Specify
  whether each hook class blocks, retries, logs and continues, rolls back, or leaves partial state.
  This gives extension points predictable failure behavior without forcing one global answer onto
  every hook.
- [`BOUNDARY-DISTINGUISH-INPUT-CLASSES`](boundary/boundary-distinguish-input-classes.md). Keep
  unknown, unsupported, denied, and preserved inputs in separate result or error paths. The
  distinction protects compatibility, authorization messaging, and recovery behavior while allowing
  small internal parsers to stay simpler.
- [`BOUNDARY-EXPOSE-PARTIAL-STREAM-OUTPUT`](boundary/boundary-expose-partial-stream-output.md).
  Surface streaming tokens, chunks, or events as provisional output until completion promotes a
  final result. Callers get progress and diagnostics without corrupting authoritative state with
  partial provider data.
- [`BOUNDARY-GIVE-TOOLS-IDENTITY-POLICY-AND-LIMITS`](boundary/boundary-give-tools-identity-policy-and-limits.md).
  Give effectful callable units typed identity, authorization policy, cancellation, and bounded
  output. The added ceremony is reserved for real tool boundaries where auditability, recovery, and
  blast-radius control matter.
- [`BOUNDARY-GROUND-INTEGRATIONS-IN-PRIMARY-SOURCES`](boundary/boundary-ground-integrations-in-primary-sources.md).
  Base adapter behavior on provider docs, specs, or captured API responses before encoding local
  assumptions. When primary sources are incomplete, label observations and inferences so guesses do
  not become fake guarantees.
- [`BOUNDARY-IDENTIFY-ANEMIC-STATE-MACHINES`](boundary/boundary-identify-anemic-state-machines.md).
  Replace scattered booleans and conditionals with named states and transitions when lifecycle
  behavior is already complex. The move exposes illegal transitions and missing recovery paths
  without over-formalizing simple linear code.
- [`BOUNDARY-KEEP-BACKEND-ADAPTERS-AT-EDGE`](boundary/boundary-keep-backend-adapters-at-edge.md).
  Keep provider-specific terminal, storage, network, and runtime APIs in adapter layers at the
  boundary. Core logic stays stable and testable while real backend differences remain modeled
  instead of hidden behind a false common API.
- [`BOUNDARY-MAKE-AMBIENT-INPUTS-EXPLICIT`](boundary/boundary-make-ambient-inputs-explicit.md). Pass
  time, randomness, environment, locale, terminal size, network clients, and process state through
  visible inputs when they affect behavior. Injecting only the relevant ambient values improves
  tests and portability without spreading oversized context objects.
- [`BOUNDARY-MAKE-DYNAMIC-CONFLICTS-DETERMINISTIC`](boundary/boundary-make-dynamic-conflicts-deterministic.md).
  Define stable ordering, duplicate handling, priority, or override policy for dynamic
  registrations. Deterministic conflict behavior prevents hash order or load timing from changing
  which plugin, guest, generated item, or handler wins.
- [`BOUNDARY-MAKE-EXEC-TOOLS-NONINTERACTIVE`](boundary/boundary-make-exec-tools-noninteractive.md).
  Default agent, CI, and background exec paths away from prompts, editors, pagers, and credential
  UI. Commands then fail or complete predictably, while human interactive modes remain explicit
  opt-ins.
- [`BOUNDARY-MAKE-POLICY-BOUNDARIES-EXPLICIT`](boundary/boundary-make-policy-boundaries-explicit.md).
  Route writes, network calls, shell execution, publication, telemetry, redaction, and credential
  use through a visible policy decision before effects run. Callers can then understand allowed,
  denied, redacted, fallback, preserved, and unsupported outcomes.
- [`BOUNDARY-MODEL-REAL-UPSTREAM-SURFACE`](boundary/boundary-model-real-upstream-surface.md). Shape
  local integration APIs around the provider's actual records, pages, permissions, rate limits, and
  consistency behavior. Wrappers may simplify common paths, but they should not promise capabilities
  the upstream cannot provide.
- [`BOUNDARY-NAME-LIFECYCLE-TRANSITIONS`](boundary/boundary-name-lifecycle-transitions.md). Model
  creation, activation, cancellation, teardown, reload, and promotion as named operations when they
  carry different invariants. This keeps ordering, cleanup, retry, and recovery rules visible
  without adding ceremony to simple constructed values.
- [`BOUNDARY-PARSE-UNCERTAINTY-AT-EDGE`](boundary/boundary-parse-uncertainty-at-edge.md). Parse and
  validate raw strings, JSON, CLI args, provider responses, and user input at the boundary before
  passing values inward. Core logic receives typed invariants, while domain-specific checks that
  require later context remain explicit policy decisions.
- [`BOUNDARY-READ-NORMALIZE-COMPARE-MUTATE`](boundary/boundary-read-normalize-compare-mutate.md).
  Reconcile external state by reading the current provider view, normalizing it, comparing intent,
  and mutating only the real difference. The loop avoids destructive or noisy writes when
  formatting, defaults, ordering, or outside actors create drift.
- [`BOUNDARY-REJECT-UNSUPPORTED-SHAPES`](boundary/boundary-reject-unsupported-shapes.md). Fail
  unsupported names, values, TTLs, targets, record families, protocols, or modes at the boundary
  with clear errors. Preserve unknown data only when compatibility requires round-tripping and the
  system can do so safely.
- [`BOUNDARY-REPORT-PROVIDER-DIAGNOSTICS`](boundary/boundary-report-provider-diagnostics.md). Return
  freshness, permission, budget, load, cache, partial-result, and degradation signals with
  provider-backed data. These diagnostics help callers decide trust, retry, display, and support
  behavior without exposing unactionable internals.
- [`BOUNDARY-SEPARATE-PURE-CORE-FROM-EFFECTS`](boundary/boundary-separate-pure-core-from-effects.md).
  Move domain computation away from rendering, I/O, mutation, and global state when effects obscure
  the decision being tested. The split gives tests a stable surface, but should be skipped when it
  adds indirection without a useful boundary.
- [`BOUNDARY-SEPARATE-UI-AND-APP-STATE`](boundary/boundary-separate-ui-and-app-state.md). Keep
  selection, focus, scroll, expansion, and transient input mode separate from application-owned data
  when they change under different rules. The separation prevents rendering concerns from mutating
  domain state while allowing tiny tools to stay simple until friction appears.
- [`BOUNDARY-STAGE-GENERATED-BEHAVIOR`](boundary/boundary-stage-generated-behavior.md). Validate
  generated, reloadable, or plugin-provided behavior in a staging path before promoting it over
  known-good behavior. Staging adds recovery cost only where runtime-loaded or generated artifacts
  can fail after deployment.
- [`BOUNDARY-TRACK-DYNAMIC-REGISTRATION-PROVENANCE`](boundary/boundary-track-dynamic-registration-provenance.md).
  Store stable source names, versions, paths, owners, or generated identifiers for extension, guest,
  generated-code, and config registrations. Provenance makes conflicts and failures diagnosable
  while avoiding sensitive source details.
- [`BOUNDARY-TREAT-TERMINAL-UI-AS-PRODUCT-SURFACE`](boundary/boundary-treat-terminal-ui-as-product-surface.md).
  Treat terminal layout, input, scroll behavior, color, viewport size, and platform differences as a
  user-facing contract when people rely on the interface. This makes regressions reviewable without
  requiring full visual testing for every tiny internal tool.
- [`BOUNDARY-USE-CONSERVATIVE-TERMINAL-DEFAULTS`](boundary/boundary-use-conservative-terminal-defaults.md).
  Choose first-run terminal behavior that works with limited color, small viewports, ordinary
  keyboard input, and varied fonts or accessibility settings. Advanced styling can remain opt-in or
  capability-detected after the baseline is readable and usable.

### Change Shape

- [`CHANGE-AVOID-SPECULATIVE-PUBLIC-API`](change-shape/change-avoid-speculative-public-api.md). Add
  public surfaces only when current or accepted callers need them. Waiting for concrete pressure
  keeps compatibility commitments smaller and easier to validate.
- [`CHANGE-AVOID-UNNECESSARY-DEPENDENCY-CHURN`](change-shape/change-avoid-unnecessary-dependency-churn.md).
  Keep package, manifest, and lockfile movement out of unrelated work. Separate dependency changes
  make build, compatibility, and downstream risk reviewable on their own.
- [`CHANGE-IDENTIFY-OWNING-MODULE-BEFORE-EDITING`](change-shape/change-identify-owning-module-before-editing.md).
  Find the component that owns the concept before adding or moving logic. That keeps invariants,
  tests, and future maintenance close to the responsible code.
- [`CHANGE-ISOLATE-CONTROVERSIAL-CHANGES`](change-shape/change-isolate-controversial-changes.md).
  Put risky or contentious moves in their own review unit when they can stand alone. This lets
  reviewers approve, reject, or revise the decision without incidental cleanup attached.
- [`CHANGE-MINIMAL-BUT-COMPLETE`](change-shape/change-minimal-but-complete.md). Keep the diff as
  small as the purpose allows while including the evidence that purpose needs. Reviewers should see
  one coherent unit they can understand, validate, and revert.
- [`CHANGE-PIN-BEHAVIOR-WITH-EARLY-TESTS`](change-shape/change-pin-behavior-with-early-tests.md).
  Add characterization tests before changing messy behavior when the existing contract is unclear.
  The baseline separates intentional behavior changes from accidental drift.
- [`CHANGE-PREFER-SMALL-FOLLOW-UPS`](change-shape/change-prefer-small-follow-ups.md). Move adjacent
  cleanup or broader improvements into focused follow-up changes when the current diff can stand
  alone. This preserves review focus while still capturing useful work.
- [`CHANGE-PRESERVE-UNOWNED-WORK`](change-shape/change-preserve-unowned-work.md). Treat nearby edits
  from users, agents, generators, or earlier changes as outside your ownership unless the task says
  otherwise. Adapting around them protects parallel work and context.
- [`CHANGE-RESPECT-GENERATED-ARTIFACT-OWNERSHIP`](change-shape/change-respect-generated-artifact-ownership.md).
  Fix generated outputs through their source inputs, templates, metadata, or generator configuration
  whenever those own the result. Hand edits are durable only when the tool workflow explicitly
  supports curation.
- [`CHANGE-SEPARATE-STRUCTURE-FROM-BEHAVIOR`](change-shape/change-separate-structure-from-behavior.md).
  Split refactoring or layout changes from behavior changes when the combined diff obscures intent.
  Separate review units make meaning preservation and new behavior easier to check.
- [`CHANGE-SYNC-GENERATED-ARTIFACTS`](change-shape/change-sync-generated-artifacts.md). Update
  checked-in generated outputs when their source inputs change and they are part of review. Keeping
  them aligned prevents consumers from seeing stale artifacts.
- [`CHANGE-TREAT-AND-AS-SCOPE-WARNING`](change-shape/change-treat-and-as-scope-warning.md). Use
  compound change descriptions as a prompt to inspect whether the work has more than one purpose.
  The word is not a rule, but it catches scope creep while splitting is still cheap.
- [`CHANGE-USE-ONE-PURPOSE-PER-CHANGE`](change-shape/change-use-one-purpose-per-change.md). Shape
  each change around one review question and one reason for existing. Related tests, docs, and
  generated files can travel with it when they support that same purpose.

### Docs Are Contracts

- [`DOCS-ALIGN-README-AND-CRATE-RUSTDOC`](documentation/docs-align-readme-and-crate-rustdoc.md).
  Keep README and crate-level Rustdoc consistent where users learn setup and supported behavior. Let
  the pages serve different tasks, but prevent conflicting contracts.
- [`DOCS-AVOID-GENERATED-PROSE-TELLS`](documentation/docs-avoid-generated-prose-tells.md). Replace
  templated, UI-centered, or polished-but-vague phrasing with concrete behavior. Keep the local
  voice trustworthy without cutting useful explanation.
- [`DOCS-AVOID-UNEARNED-PRAISE`](documentation/docs-avoid-unearned-praise.md). Replace vague ranking
  words with observable behavior, evidence, or tradeoffs. Use evaluative claims only when the basis
  is explicit enough for readers to verify.
- [`DOCS-BUILD-DOCS-LIKE-USERS-READ-THEM`](documentation/docs-build-docs-like-users-read-them.md).
  Review rendered Rust documentation, links, cfg behavior, and examples in the modes users see.
  Match validation depth to the risk of feature, metadata, or public example changes.
- [`DOCS-CHOOSE-DOCUMENT-TYPE`](documentation/docs-choose-document-type.md). Pick the dominant
  document mode before editing so the page serves one reader task well. Link out to secondary modes
  instead of blending tutorial, reference, decisions, and changelog.
- [`DOCS-COMPARE-LIBRARIES-ACCURATELY`](documentation/docs-compare-libraries-accurately.md). Check
  current upstream behavior before comparing nearby libraries or crates. Charitable, source-backed
  comparisons preserve trust while still helping users choose.
- [`DOCS-DISTINGUISH-EXAMPLE-ROLES`](documentation/docs-distinguish-example-roles.md). Name whether
  an example is focused, canonical, survey, integration, or showcase work. That role controls how
  complete, copyable, and validated the example must be.
- [`DOCS-DOCUMENT-LIFECYCLE-AND-SIDE-EFFECTS`](documentation/docs-document-lifecycle-and-side-effects.md).
  Document caller-visible lifecycle, ownership, platform, feature, and side-effect obligations. Skip
  internal narration, but make operational responsibilities clear.
- [`DOCS-EXPOSE-MOVE-RISK-AND-EXAMPLE-IN-PATTERNS`](documentation/docs-expose-move-risk-and-example-in-patterns.md).
  Give pattern guidance a recognizable trigger, preferred move, risk, example, and agent
  instruction. The extra structure makes repeatable advice easier to cite and apply.
- [`DOCS-FRONT-LOAD-USEFUL-POINT`](documentation/docs-front-load-useful-point.md). Put the decision,
  command, invariant, or warning before broad setup. Readers and agents can then use the page
  without hunting through introductory prose.
- [`DOCS-GROUP-RELATED-LIST-ITEMS`](documentation/docs-group-related-list-items.md). Cluster long
  lists under useful names when the relationships matter. Keep short or causal material flat or in
  prose so structure does not add noise.
- [`DOCS-HIDE-CATALOG-MECHANICS`](documentation/docs-hide-catalog-mechanics.md). Lead user-facing
  copy with work areas, artifacts, and destinations instead of IDs or generated structure. Mention
  catalog mechanics only when citation or contribution work needs them.
- [`DOCS-KEEP-MARKDOWN-LINTABLE`](documentation/docs-keep-markdown-lintable.md). Use project
  Markdown style so formatting stays enforceable and review noise stays low. Treat lint exceptions
  as intentional local choices, not accumulated drift.
- [`DOCS-MAKE-GUIDANCE-REVIEW-STATE-VISIBLE`](documentation/docs-make-guidance-review-state-visible.md).
  Mark guidance maturity so readers know whether a rule is draft, reviewed, or ready for reuse.
  Visible state prevents tentative advice from becoming an accidental standard.
- [`DOCS-MAKE-REVIEW-EASY-TO-INSPECT`](documentation/docs-make-review-easy-to-inspect.md). Package
  documentation changes so reviewers can see scope, evidence, and rendered impact quickly. Small
  inspectable changes reduce hidden drift and style-only review loops.
- [`DOCS-MARK-NONCOMPILING-EXAMPLES-HONESTLY`](documentation/docs-mark-noncompiling-examples-honestly.md).
  Label examples that are sketches, partial snippets, or intentionally not run. Honest labels keep
  readers from treating illustrative code as a supported copy-paste contract.
- [`DOCS-MATCH-PAGE-SHAPE-TO-READER-TASK`](documentation/docs-match-page-shape-to-reader-task.md).
  Shape pages around the reader's task, such as learning, choosing, reference, or review. The right
  structure lowers scan cost without forcing one page to do every job.
- [`DOCS-NAME-DESTINATION-NOT-DIRECTION`](documentation/docs-name-destination-not-direction.md). Use
  labels that name the section, object, or decision the reader will reach. Directional labels make
  readers follow the page order before knowing whether it is relevant.
- [`DOCS-ONE-DOMINANT-MODE-PER-PAGE`](documentation/docs-one-dominant-mode-per-page.md). Let each
  page have one primary mode and move competing material behind links. This keeps readers from
  paying for tutorial, reference, explanation, and policy at once.
- [`DOCS-PROSE-FOR-RELATIONSHIPS-LISTS-FOR-ENUMERATION`](documentation/docs-prose-for-relationships-lists-for-enumeration.md).
  Use prose when causality, contrast, or priority matters, and lists when enumerating parallel
  items. The shape should reveal the relationship instead of hiding it in bullets.
- [`DOCS-PROVE-REAL-USE-WITH-EXAMPLES`](documentation/docs-prove-real-use-with-examples.md). Use
  examples that show realistic ownership, errors, lifecycle, configuration, or integration shape.
  Keep them focused, but make them strong enough to prove the contract.
- [`DOCS-PUT-UNCERTAINTY-IN-TRACKED-PLACES`](documentation/docs-put-uncertainty-in-tracked-places.md).
  Keep user docs focused on current truth and move unresolved direction to issues, ADRs, or
  roadmaps. Track speculation where it can be decided instead of implying a promise.
- [`DOCS-README-AS-ENTRY-POINT`](documentation/docs-readme-as-entry-point.md). Use README files to
  orient readers to purpose, setup, first useful use, and deeper docs. Split out manual-level detail
  when it hides the starting path.
- [`DOCS-REVIEW-CORRECTNESS-AND-RISK-FIRST`](documentation/docs-review-correctness-and-risk-first.md).
  Lead documentation review with false contracts, drift, operability, and unsupported claims before
  style polish. This separates blocking risk from wording cleanup.
- [`DOCS-SHOW-SIDE-EFFECTS-IN-LIVE-EXAMPLES`](documentation/docs-show-side-effects-in-live-examples.md).
  Show setup, visible effects, and cleanup when examples touch live resources or persistent state.
  Gate costly or externally visible actions so examples stay honest and safe to adapt.
- [`DOCS-STATE-CURRENT-BEHAVIOR-NOT-ASPIRATION`](documentation/docs-state-current-behavior-not-aspiration.md).
  Describe what the system does now and label limitations or future plans separately. Otherwise
  roadmap language becomes a false contract for readers and agents.
- [`DOCS-TREAT-DOCS-AS-CONTRACTS`](documentation/docs-treat-docs-as-contracts.md). Treat supported
  behavior, commands, errors, and examples in docs as promises readers may rely on. Separate
  normative claims from background, examples, and future plans.
- [`DOCS-USE-CONCRETE-DETAILS`](documentation/docs-use-concrete-details.md). Name real commands,
  paths, defaults, types, examples, and work areas when they clarify scope. Concrete detail removes
  guesswork without overloading prose with incidental facts.
- [`DOCS-USE-DESCRIPTIVE-HEADINGS`](documentation/docs-use-descriptive-headings.md). Write headings
  that name the section content, destination, or decision area. Reserve imperative headings for
  procedures where the section is truly a step.
- [`DOCS-USE-SOURCE-LINKS-AS-SUPPORT`](documentation/docs-use-source-links-as-support.md). Use
  references to verify, frame, or contrast local guidance instead of supplying the wording. This
  keeps the repo voice original while still making claims checkable.
- [`DOCS-VERIFY-COMMANDS-PATHS-AND-LINKS`](documentation/docs-verify-commands-paths-and-links.md).
  Check commands, file paths, and linked references because readers treat them as executable
  instructions. Note assumptions when credentials, services, or platforms prevent a full run.
- [`DOCS-WRITE-FOR-NON-LINEAR-READERS`](documentation/docs-write-for-non-linear-readers.md). Give
  sections enough local context to work when reached from search, links, review, or retrieval. Avoid
  repeating the whole introduction; add only the subject and prerequisite needed.
- [`DOCS-WRITE-TECHNICAL-PROSE`](documentation/docs-write-technical-prose.md). Use direct technical
  language that carries contracts, commands, evidence, and tradeoffs. Cut marketing, coaching, chat,
  and page narration when they do not explain the system.

### Observability And Failure

- [`OBSERVABILITY-DISTINGUISH-FAILURE-STATES`](observability/observability-distinguish-failure-states.md).
  Preserve status distinctions that change recovery, messaging, metrics, or debugging. Collapsing
  timeouts, denials, aborts, partial work, and failures makes callers guess.
- [`OBSERVABILITY-KEEP-DIAGNOSTICS-RETENTION-SAFE`](observability/observability-keep-diagnostics-retention-safe.md).
  Match diagnostic detail to its audience and retention period. Redact or summarize sensitive values
  while preserving enough operation context to debug.
- [`OBSERVABILITY-LOG-AT-OWNED-BOUNDARIES`](observability/observability-log-at-owned-boundaries.md).
  Emit logs where the code still knows the operation, intent, input class, and external boundary.
  That placement gives useful context without duplicating noise through every layer.
- [`OBSERVABILITY-PRESERVE-OPERATION-CONTEXT-IN-ERRORS`](observability/observability-preserve-operation-context-in-errors.md).
  Carry the operation, resource, provider, input class, and policy context that explain a failure.
  Stable identifiers and sanitized summaries shorten debugging without exposing payloads.
- [`OBSERVABILITY-SURFACE-DURABLE-FAILURES`](observability/observability-surface-durable-failures.md).
  Give persistent failures a stable status, error surface, or retry path instead of only an
  ephemeral UI log. Users and maintainers need something actionable after the moment passes.

### Measure Before Optimizing

- [`PERF-AVOID-SINGLE-RUN-CONCLUSIONS`](performance/perf-avoid-single-run-conclusions.md). Do not
  land performance conclusions from one short benchmark run. Repeat and contextualize timing
  evidence because warmup, scheduling, cache state, and background load can make a single result
  non-reproducible.
- [`PERF-JUSTIFY-COMPLEXITY-CHURN-AND-DEPENDENCIES`](performance/perf-justify-complexity-churn-and-dependencies.md).
  Explain why a performance win justifies added complexity, churn, unsafe code, caching, or
  dependencies. Measured speedups still need to pay for the maintenance cost every future reader
  inherits.
- [`PERF-MEASURE-GOAL-CHANGE-COMPARE`](performance/perf-measure-goal-change-compare.md). State the
  performance goal, baseline measurement, implementation change, and comparison result together.
  Those pieces let reviewers judge whether the patch improved the relevant workload enough to
  justify its tradeoffs.
- [`PERF-OPTIMIZE-MEASURED-HOTSPOTS`](performance/perf-optimize-measured-hotspots.md). Optimize code
  that measurement shows is on the important runtime path. This keeps review attention on changes
  whose user-visible impact justifies altering the code shape.
- [`PERF-RECORD-BENCHMARK-PROVENANCE`](performance/perf-record-benchmark-provenance.md). Record the
  commands, inputs, tool versions, build profile, and runner conditions behind benchmark numbers.
  Provenance makes future comparisons meaningful and helps separate real changes from environment
  drift.
- [`PERF-RUN-CORRECTNESS-FIRST`](performance/perf-run-correctness-first.md). Run relevant
  correctness checks before interpreting performance timing. Fast code that changes behavior
  invalidates the benchmark claim and wastes review effort.
- [`PERF-RUN-TIMING-BENCHMARKS-SEQUENTIALLY`](performance/perf-run-timing-benchmarks-sequentially.md).
  Serialize timing-sensitive benchmarks when their numbers will be used as evidence. Concurrent runs
  compete for shared resources and can make the comparison describe the runner more than the code.

### Local Reasoning And Refactoring

- [`REFACTORING-ALIGN-SEAMS-WITH-REAL-VARIATION`](refactoring/refactoring-align-seams-with-real-variation.md).
  Put abstraction seams where code already varies across backends, policies, protocols, tests, or
  ownership boundaries. Avoid adding names and jumps for hypothetical futures unless the next change
  or risk clearly justifies them.
- [`REFACTORING-DO-NOT-OVER-APPLY-DRY`](refactoring/refactoring-do-not-over-apply-dry.md). Keep
  similar-looking code separate until it has the same meaning and changes together. Premature
  sharing can couple unrelated policies and make later edits harder.
- [`REFACTORING-EXTRACT-CONCEPT-HELPERS`](refactoring/refactoring-extract-concept-helpers.md).
  Extract helpers when the new function names a real concept boundary with a stable purpose. Hiding
  a few lines behind a weak name adds a jump without reducing the reader's burden.
- [`REFACTORING-KEEP-LINEAR-STORY-VISIBLE`](refactoring/refactoring-keep-linear-story-visible.md).
  Keep simple ordered workflows inline when the sequence is the clearest explanation. Extract only
  the substeps that carry their own concept, policy, reuse, or test surface.
- [`REFACTORING-KEEP-WEAK-ABSTRACTIONS-CLOSE-TO-THEIR-USE`](refactoring/refactoring-keep-weak-abstractions-close-to-their-use.md).
  Keep tentative helpers, types, or traits near their first use until the boundary proves itself.
  Local placement makes weak abstractions easier to revise, inline, or delete before other modules
  depend on them.
- [`REFACTORING-MAKE-EDGE-CASES-EXPLICIT`](refactoring/refactoring-make-edge-cases-explicit.md).
  Name boundary behavior near the branch, calculation, or return that depends on it. This makes
  policy reviewable and shows when stronger types should prevent invalid states instead.
- [`REFACTORING-PREFER-LOCAL-REASONING`](refactoring/refactoring-prefer-local-reasoning.md). Shape
  code so relevant state, invariants, and effects are visible near the change. Centralize only when
  it reduces total reasoning, because distant reconstruction raises cognitive load and error risk.
- [`REFACTORING-PREFER-LOOPS-FOR-SIDE-EFFECTS`](refactoring/refactoring-prefer-loops-for-side-effects.md).
  Use ordinary loops when the main purpose is mutation, I/O, logging, or other side effects.
  Iterator chains are better for value transformation; using them for effects can hide order, early
  exits, and error handling.
- [`REFACTORING-USE-WHITESPACE-AS-FUNCTION-PARAGRAPHS`](refactoring/refactoring-use-whitespace-as-function-paragraphs.md).
  Use blank lines to group related statements inside a function before extracting more names.
  Paragraph-like spacing can reveal the local story while avoiding unnecessary helper jumps.

### Private Context And Review Artifacts

- [`REVIEW-ANSWER-QUESTIONS-BEFORE-CODE`](review/review-answer-questions-before-code.md). Answer
  reviewer questions before or alongside the code changes that address them. This keeps intent,
  tradeoffs, and unresolved choices visible instead of burying the reasoning in a new patch.
- [`REVIEW-CLASSIFY-PROTOTYPE-REUSE`](review/review-classify-prototype-reuse.md). Classify whether a
  rebuild is reusing behavior, evidence, replaceable internal shape, or load-bearing boundaries.
  That separation helps preserve proven compatibility while discarding prototype scaffolding.
- [`REVIEW-DEFINE-SLICES-IN-ISSUES`](review/review-define-slices-in-issues.md). Shape issues around
  review-sized slices with clear outcomes. Coherent slices reduce scope creep and give maintainers
  or agents a practical unit of work without losing the larger purpose.
- [`REVIEW-EXPLAIN-CONTROVERSIAL-CHOICES-INLINE`](review/review-explain-controversial-choices-inline.md).
  Put short rationale near surprising dependencies, unsafe blocks, generated artifacts, policy
  exceptions, or compatibility choices. Local explanation prevents reviewers and future readers from
  rediscovering the same concern.
- [`REVIEW-EXPLAIN-PR-PROBLEM-MODEL-AND-PROOF`](review/review-explain-pr-problem-model-and-proof.md).
  Use PR descriptions to explain the problem, mental model, tradeoffs, validation, and documentation
  impact. Reviewers can then evaluate the diff against stated intent instead of reverse-engineering
  it.
- [`REVIEW-LABEL-SPECULATION-AS-INFERRED-OR-UNKNOWN`](review/review-label-speculation-as-inferred-or-unknown.md).
  Mark review claims as observed, inferred, assumed, or unknown when the evidence level matters.
  Clear labels keep guesses from hardening into false project knowledge.
- [`REVIEW-LET-REVIEWERS-RESOLVE-THREADS`](review/review-let-reviewers-resolve-threads.md). Leave
  nontrivial review threads for the reviewer to resolve after they confirm the concern was
  addressed. Authors should only close unambiguous mechanical threads, because resolution carries
  communication ownership.
- [`REVIEW-MAKE-REVIEW-ARTIFACTS-STANDALONE`](review/review-make-review-artifacts-standalone.md).
  Put the needed problem, decision, context, validation, and risk in the issue, PR, commit, or
  handoff itself. Standalone artifacts make review and future debugging possible without private
  session context.
- [`REVIEW-SEPARATE-DISCOVERY-SELECTION-IMPLEMENTATION`](review/review-separate-discovery-selection-implementation.md).
  Split problem discovery, solution selection, and implementation review when they require different
  decisions. This keeps design debate out of patch correctness review once scope or direction is
  still unsettled.
- [`REVIEW-UPDATE-SOURCE-OF-TRUTH`](review/review-update-source-of-truth.md). Put durable status
  changes in the owning issue, PR description, checklist, plan, or handoff instead of posting
  low-signal comments. Updating the source of truth reduces notification churn and makes the current
  state discoverable.
- [`REVIEW-USE-ADRS-FOR-BOUNDARIES-AND-OWNERSHIP`](review/review-use-adrs-for-boundaries-and-ownership.md).
  Record durable ownership, API, storage, topology, runtime, or service-boundary decisions in ADRs.
  A decision record gives later contributors a stable tradeoff to affirm, revise, or replace.

### Rust API And Crate Shape

- [`RUST-ADD-BENCHMARKS-FOR-PERFORMANCE-CLAIMS`](rust/rust-add-benchmarks-for-performance-claims.md).
  Use benchmarks when Rust changes rely on speed, allocation, or hot-path claims. The evidence makes
  performance tradeoffs reviewable instead of relying on intuition.
- [`RUST-ALIGN-RELEASE-SUPPORT-CLAIMS`](rust/rust-align-release-support-claims.md). Keep crate
  metadata, docs, changelogs, and support statements saying the same thing. The alignment helps
  downstream users know which compatibility contract to trust.
- [`RUST-AVOID-BROAD-CONTEXT-AND-CALLBACKS`](rust/rust-avoid-broad-context-and-callbacks.md). Pass
  explicit inputs and keep control flow local instead of hiding it in context bags or callbacks.
  This makes ownership, effects, and ordering easier to audit.
- [`RUST-AVOID-EMPTY-WRAPPER-TYPES`](rust/rust-avoid-empty-wrapper-types.md). Add a wrapper type
  only when it carries an invariant, behavior, or ownership boundary. Otherwise it adds conversions
  and concepts without improving correctness.
- [`RUST-AVOID-GIANT-CRATE-ROOTS`](rust/rust-avoid-giant-crate-roots.md). Use the crate root to
  teach the public shape and route readers to focused modules. This keeps `lib.rs` or `main.rs` from
  becoming the whole implementation surface.
- [`RUST-AVOID-GLOB-REEXPORTS`](rust/rust-avoid-glob-reexports.md). Re-export public facade names
  explicitly instead of using globs. This prevents accidental API expansion and makes exported names
  visible during review.
- [`RUST-AVOID-INLINE-MODULES`](rust/rust-avoid-inline-modules.md). Put nontrivial modules in named
  files unless tests, preludes, or generated code justify inline layout. Stable paths make search,
  review, and ownership clearer.
- [`RUST-AVOID-MOD-RS-BY-DEFAULT`](rust/rust-avoid-mod-rs-by-default.md). Prefer named module files
  when they make tabs, paths, and search results clearer. Reserve `mod.rs` for cases where local
  convention or layout makes it the better signal.
- [`RUST-AVOID-OVERCOMMENTING-TRIVIAL-CODE`](rust/rust-avoid-overcommenting-trivial-code.md).
  Comment Rust code for invariants, contracts, and surprising tradeoffs rather than restating
  obvious operations. This keeps comments useful and less prone to drift.
- [`RUST-AVOID-PATH-ATTRIBUTE`](rust/rust-avoid-path-attribute.md). Use normal Rust module lookup
  unless generated or platform-specific layout needs `#[path]`. Predictable file paths make
  navigation and ownership easier to infer.
- [`RUST-AVOID-PUBLIC-DEPENDENCY-COUPLING`](rust/rust-avoid-public-dependency-coupling.md). Keep
  dependency types out of public APIs unless interoperability is the purpose. This preserves semver
  freedom and avoids forcing downstream users onto implementation choices.
- [`RUST-AVOID-TINY-MODULE-MAZES`](rust/rust-avoid-tiny-module-mazes.md). Keep small helper code
  near its use unless a separate module owns a real concept. This reduces file-jumping and preserves
  reader locality.
- [`RUST-AVOID-VAGUE-DOCS-AND-GENERIC-EXAMPLES`](rust/rust-avoid-vague-docs-and-generic-examples.md).
  Write Rustdoc and examples around real caller scenarios, not generic claims of usefulness.
  Concrete examples expose ownership, errors, features, and lifecycle expectations.
- [`RUST-CENTRAL-ITEM-FIRST`](rust/rust-central-item-first.md). Put the main type, trait, enum, or
  function before supporting details. Readers can learn the module's purpose before chasing helpers
  and adapters.
- [`RUST-CHOOSE-GENERICS-AND-TRAIT-OBJECTS-DELIBERATELY`](rust/rust-choose-generics-and-trait-objects-deliberately.md).
  Pick generics, stored type parameters, or trait objects for the variation they actually model. The
  choice affects compile cost, object safety, lifetimes, and caller ergonomics.
- [`RUST-COMPARE-CRATES-BY-FIT-AND-TRADEOFF`](rust/rust-compare-crates-by-fit-and-tradeoff.md).
  Compare adjacent crates by intended fit, scope, and constraints instead of broad superiority
  claims. This helps users choose without turning docs into brittle marketing.
- [`RUST-CONFIGURE-DOCS-RS`](rust/rust-configure-docs-rs.md). Configure docs.rs metadata when
  features, cfgs, or rustdoc flags affect rendered API docs. Users should see the documentation
  surface the crate expects to support.
- [`RUST-CONSIDER-DOWNSTREAM-API-IMPACT`](rust/rust-consider-downstream-api-impact.md). Check public
  API changes against downstream imports, traits, inference, and examples before reshaping them.
  Additive paths and deprecations often avoid unnecessary breakage.
- [`RUST-CONTAIN-UNSAFE`](rust/rust-contain-unsafe.md). Keep unsafe blocks small, wrapped by safe
  APIs, documented, and tested through safe behavior. Localized obligations make the safety argument
  auditable.
- [`RUST-DENY-ACCIDENTAL-UNSAFE`](rust/rust-deny-accidental-unsafe.md). Use a crate-level lint when
  a crate intends to avoid unsafe code entirely. Executable policy catches accidental unsafe before
  it becomes normal implementation detail.
- [`RUST-DO-NOT-DEFAULT-PUB-CRATE`](rust/rust-do-not-default-pub-crate.md). Start items private and
  widen to `pub(crate)` only for deliberate shared internals. This keeps modules independent and
  makes crate-local contracts visible.
- [`RUST-DO-NOT-PIN-PATCH-VERSIONS`](rust/rust-do-not-pin-patch-versions.md). Keep manifest
  requirements as wide as the crate honestly supports. Patch pins belong in `Cargo.toml` only when
  code depends on that patch's API, fix, or behavior.
- [`RUST-DOCUMENT-CURRENT-IMPLEMENTED-BEHAVIOR`](rust/rust-document-current-implemented-behavior.md).
  Document what the crate does today instead of presenting future plans as available contract. Clear
  tense and labels prevent callers from relying on unimplemented behavior.
- [`RUST-DOCUMENT-FEATURE-CONTRACTS`](rust/rust-document-feature-contracts.md). Explain what each
  feature flag enables, requires, and promises. Feature contracts help users choose combinations
  without guessing from dependency names.
- [`RUST-DOCUMENT-LIFECYCLE-SIDE-EFFECTS`](rust/rust-document-lifecycle-side-effects.md). Document
  construction, start, stop, drop, and cleanup behavior when side effects matter. Callers need to
  know when resources are acquired, released, spawned, or blocked.
- [`RUST-DOCUMENT-PERFORMANCE-CONTRACTS`](rust/rust-document-performance-contracts.md). State
  meaningful performance expectations when callers may design around them. Clear limits keep
  complexity and optimization claims tied to supported behavior.
- [`RUST-DOCUMENT-PUBLIC-PANIC-CONTRACTS`](rust/rust-document-public-panic-contracts.md). Document
  when public APIs can panic and what callers can do to avoid it. Panic contracts keep recoverable
  errors, invariants, and misuse boundaries explicit.
- [`RUST-DOCUMENT-SCHEDULING-FOR-LONG-ASYNC`](rust/rust-document-scheduling-for-long-async.md).
  Explain executor, cancellation, blocking, and fairness expectations for async work that can run
  long. Callers need those constraints to avoid starvation and runtime surprises.
- [`RUST-DOCUMENT-VISIBILITY-OWNERSHIP`](rust/rust-document-visibility-ownership.md). Pair widened
  visibility with names and docs that identify the owning concept. This prevents shared internals
  from looking like accidental stable API.
- [`RUST-ENCODE-DURABLE-RULES-IN-LINTS`](rust/rust-encode-durable-rules-in-lints.md). Use lint
  configuration for project policies stable enough to automate. Durable lints catch repeated
  mistakes without turning subjective taste into CI noise.
- [`RUST-EXPOSE-PRIMARY-PATH-FROM-CRATE-ROOT`](rust/rust-expose-primary-path-from-crate-root.md).
  Make the crate root show the main workflow, types, and import path. Users should not have to infer
  the intended entry point from private layout details.
- [`RUST-FORMAT-DOCS-AND-COMMENTS-CONSISTENTLY`](rust/rust-format-docs-and-comments-consistently.md).
  Apply stable formatting to Rustdoc, examples, attributes, and prose comments. Consistent source
  formatting keeps docs readable and prevents noisy future diffs.
- [`RUST-GROUP-MODULE-IMPORTS`](rust/rust-group-module-imports.md). Group related imports by module
  when that matches local style. This makes dependency shape easier to scan and avoids churn from
  one-import-per-line edits.
- [`RUST-GROUP-PRIVATE-IMPORTS-BEFORE-PUBLIC-RE-EXPORTS`](rust/rust-group-private-imports-before-public-re-exports.md).
  Separate implementation imports from public re-exports in module prologues. The grouping lets
  readers distinguish internal dependencies from the API surface being presented.
- [`RUST-HIDE-TEST-ONLY-HELPERS`](rust/rust-hide-test-only-helpers.md). Keep fixtures and shortcuts
  behind test-only modules, features, or support crates unless they are deliberate API. This
  prevents scaffolding from leaking into production contracts.
- [`RUST-IMPLEMENT-DEBUG-FOR-PUBLIC-TYPES`](rust/rust-implement-debug-for-public-types.md). Provide
  `Debug` for public types unless it would expose secrets or mislead callers. The trait is baseline
  support for tests, assertions, logs, and downstream diagnostics.
- [`RUST-IMPLEMENT-STANDARD-TRAITS-FOR-PUBLIC-ERRORS`](rust/rust-implement-standard-traits-for-public-errors.md).
  Make reusable public errors implement the standard diagnostic traits where appropriate. This lets
  callers compose, display, chain, and inspect errors in ordinary Rust workflows.
- [`RUST-INJECT-HOST-INTERACTIONS-AT-BOUNDARIES`](rust/rust-inject-host-interactions-at-boundaries.md).
  Pass filesystem, network, time, randomness, and process behavior through boundaries when tests or
  alternate environments need control. This keeps the core deterministic and effects explicit.
- [`RUST-KEEP-CI-HIGH-SIGNAL`](rust/rust-keep-ci-high-signal.md). Keep required Rust checks strict,
  fast, deterministic, and actionable. Slow or flaky ritual trains maintainers to ignore failures
  while real drift accumulates.
- [`RUST-KEEP-COMPATIBLE-UPDATES-IN-LOCKFILE`](rust/rust-keep-compatible-updates-in-lockfile.md).
  Let lockfiles record newer compatible dependency versions when the manifest floor has not changed.
  This tests fresh releases without narrowing downstream compatibility.
- [`RUST-KEEP-CONCEPTS-COHERENT`](rust/rust-keep-concepts-coherent.md). Give each module, type, or
  helper one recognizable idea to own. Coherent ownership keeps readers from carrying unrelated
  parsing, state, rendering, and policy facts at once.
- [`RUST-KEEP-CRATE-BOUNDARIES-NARROW`](rust/rust-keep-crate-boundaries-narrow.md). Put behavior and
  tests in the crate or module that owns them before extracting shared helpers. Narrow boundaries
  reduce dependency fan-out, feature pressure, and hidden coupling.
- [`RUST-KEEP-DEPENDENCY-UPDATES-INTENTIONAL`](rust/rust-keep-dependency-updates-intentional.md).
  Separate maintenance-only dependency refreshes from updates that change behavior, features, MSRV,
  or integration. Reviewable grouping lowers noise without hiding downstream risk.
- [`RUST-KEEP-EDITS-SCOPED-TO-OWNING-CONCEPT`](rust/rust-keep-edits-scoped-to-owning-concept.md).
  Change the module, crate, feature, or facade that owns the behavior being fixed. Scoped edits keep
  reviews atomic and prevent nearby files from pulling in unrelated concepts.
- [`RUST-KEEP-LINTS-ACTIONABLE`](rust/rust-keep-lints-actionable.md). Enforce lints that improve
  correctness, API quality, docs, portability, or maintenance in ways reviewers want automated.
  Scope suppressions tightly so exceptions stay visible.
- [`RUST-KEEP-MARKDOWN-OUTSIDE-RUSTDOC-PURPOSEFUL`](rust/rust-keep-markdown-outside-rustdoc-purposeful.md).
  Use standalone Markdown for architecture, workflow, release, or operational guidance that would
  make API docs noisy. Choosing the right surface keeps contracts and long-form context current.
- [`RUST-KEEP-PRE-RELEASE-COMPATIBILITY-INTENTIONAL`](rust/rust-keep-pre-release-compatibility-intentional.md).
  Preserve pre-release compatibility only when it reflects a chosen contract. Early cleanup is often
  cheaper than freezing accidental names, re-exports, features, or variants.
- [`RUST-KEEP-PRELUDES-REEXPORT-ONLY`](rust/rust-keep-preludes-reexport-only.md). Put only
  re-exports in prelude modules and keep original behavior in its owning module. Users expect
  preludes to aid imports, not hide implementation ownership.
- [`RUST-KEEP-PUBLIC-API-SHAPE-INTENTIONAL`](rust/rust-keep-public-api-shape-intentional.md). Make
  public visibility, aliases, features, re-exports, bounds, and variants reflect intended
  commitments. Published surface area becomes something downstream users can depend on.
- [`RUST-KEEP-RUSTDOC-AND-README-EXAMPLES-ALIGNED`](rust/rust-keep-rustdoc-and-readme-examples-aligned.md).
  Keep README, Rustdoc, generated docs, and example directories teaching the same current usage
  contract. Aligned examples prevent users from guessing which import path or lifecycle is correct.
- [`RUST-MAKE-FEATURE-FLAGS-ADDITIVE-WHERE-POSSIBLE`](rust/rust-make-feature-flags-additive-where-possible.md).
  Design feature flags as additive capabilities whenever possible so Cargo feature unification does
  not surprise downstream builds. Make incompatible combinations explicit when addition cannot model
  the real choice.
- [`RUST-MAKE-PUBLIC-API-BROWSEABLE-FROM-LAYOUT`](rust/rust-make-public-api-browseable-from-layout.md).
  Align public modules, re-exports, and source files so readers can navigate from API to ownership
  without translation. Facades are fine when they improve discovery and still point toward the
  owning concept.
- [`RUST-MAKE-SIDE-EFFECTS-EXPLICIT`](rust/rust-make-side-effects-explicit.md). Put mutation, I/O,
  registration, cleanup, and background work in names, call sites, or docs when callers must account
  for them. Keep tiny private helpers plain when the surrounding code already makes the effect
  obvious.
- [`RUST-NAME-AUDITABLE-INTERMEDIATES`](rust/rust-name-auditable-intermediates.md). Introduce named
  locals where parsing, validation, rendering, ownership, or side-effect decisions need review.
  Avoid naming every trivial expression when it would add ceremony without clarifying the boundary.
- [`RUST-NAME-TESTS-BY-BEHAVIOR`](rust/rust-name-tests-by-behavior.md). Name tests after the
  behavior, boundary, or regression they protect so failure output is useful before a reader opens
  the body. Keep names concise and let module context carry repeated setup details.
- [`RUST-NON-EXHAUSTIVE-PUBLIC-ERRORS`](rust/rust-non-exhaustive-public-errors.md). Mark public
  error enums non-exhaustive unless exhaustive matching is part of the contract. This preserves room
  for future integration, validation, or provider failures without needless downstream breakage.
- [`RUST-ORDER-CODE-FOR-READING`](rust/rust-order-code-for-reading.md). Arrange code so central
  items, callers, or public API appear before supporting helpers when that makes the file readable
  top to bottom. Prefer the order that reduces reader jumping over mechanical rearrangement.
- [`RUST-ORDER-ITEMS-FOR-API-READING`](rust/rust-order-items-for-api-reading.md). Order imports,
  public items, impls, trait impls, and helpers so the API story is easy to scan. Respect macros,
  generated code, and local convention when another order communicates better.
- [`RUST-PREFER-BORING-DIRECT-CODE`](rust/rust-prefer-boring-direct-code.md). Prefer explicit Rust
  control flow, types, and error handling over clever framework-shaped indirection. Use macros or
  abstractions when they remove real repetition or enforce real invariants.
- [`RUST-PREFER-CONCEPT-OWNED-MODULES-AND-NAMED-FILES`](rust/rust-prefer-concept-owned-modules-and-named-files.md).
  Organize modules around domain concepts and give important concepts named files that own their
  types, invariants, tests, and docs. Use infrastructure modules only when the cross-cutting concept
  is real and bounded.
- [`RUST-PREFER-CONSTRUCTORS-AND-CONVERSION-TRAITS`](rust/rust-prefer-constructors-and-conversion-traits.md).
  Use inherent constructors and standard conversion traits to show whether construction builds,
  validates, converts, borrows, allocates, or can fail. Prefer public fields only when direct
  construction is truly part of the contract.
- [`RUST-PREFER-EXPECT-FOR-LINT-SUPPRESSIONS`](rust/rust-prefer-expect-for-lint-suppressions.md).
  Use `#[expect]` for targeted lint suppressions that should disappear when the warning is fixed.
  Reserve broad `allow` attributes for deliberate policy choices that are not expected to expire.
- [`RUST-PREFER-SMALL-CLEAR-SHAPES`](rust/rust-prefer-small-clear-shapes.md). Favor small functions,
  narrow structs, and simple enums that keep live facts local for readers. Do not split cohesive
  logic into fragments that force more navigation than understanding.
- [`RUST-PRESERVE-ERROR-CONTEXT`](rust/rust-preserve-error-context.md). Wrap and model errors so
  callers can see the operation, relevant input, source cause, and recovery signal. Avoid flattening
  failures into broad strings or generic variants that remove actionable context.
- [`RUST-PRESERVE-VALID-STATE-ON-FAILURE`](rust/rust-preserve-valid-state-on-failure.md). Keep
  values valid when fallible operations return errors so callers can retry, inspect, or drop them
  predictably. Use transactional updates or staging when partial mutation would expose a broken
  state.
- [`RUST-REEXPORT-FOR-DISCOVERY`](rust/rust-reexport-for-discovery.md). Re-export public items where
  callers naturally look so the crate surface is discoverable without hiding ownership. Keep
  canonical definitions and docs clear so re-exports do not become competing homes.
- [`RUST-RELEASE-ONLY-AFTER-ARTIFACT-VALIDATION`](rust/rust-release-only-after-artifact-validation.md).
  Validate the actual release artifact before publishing instead of trusting the working tree. This
  catches missing files, stale generated content, and packaging mistakes while the release can still
  be fixed.
- [`RUST-REVIEW-AS-FUTURE-MAINTAINER`](rust/rust-review-as-future-maintainer.md). Review Rust
  changes for the reader who will debug, extend, or release the code later, not only for immediate
  correctness. Favor maintainable API shape, docs, tests, and error behavior over changes that
  merely compile.
- [`RUST-RUN-FEATURE-GATED-VALIDATION`](rust/rust-run-feature-gated-validation.md). Exercise the
  feature combinations touched by a Rust change so gated code, docs, and integrations actually
  build. Choose representative combinations when exhaustive feature matrices would be too expensive.
- [`RUST-SHAPE-EXPRESSIONS-FOR-AUDITABILITY`](rust/rust-shape-expressions-for-auditability.md).
  Shape complex expressions so ownership, validation, error handling, and side effects can be
  audited at the point they occur. Break chains or introduce names when density hides a decision
  readers must verify.
- [`RUST-TEACH-CRATE-FROM-CRATE-ROOT`](rust/rust-teach-crate-from-crate-root.md). Use crate-root
  docs and exports to teach the crate's main concepts, entry points, and common paths. Keep the root
  focused enough to orient readers without duplicating every item-level contract.
- [`RUST-TIE-OPTIONAL-DEPENDENCIES-TO-NAMED-FEATURES`](rust/rust-tie-optional-dependencies-to-named-features.md).
  Connect optional dependencies to clear feature names that explain the capability callers enable.
  Avoid leaking dependency names as the public feature design when the capability needs a more
  stable contract.
- [`RUST-USE-BUILDERS-FOR-OPTIONAL-OR-VALIDATED-FIELDS`](rust/rust-use-builders-for-optional-or-validated-fields.md).
  Use builders when construction has many optional inputs or cross-field validation that would make
  constructors hard to read. Avoid builder APIs for simple values where direct construction
  communicates the contract better.
- [`RUST-USE-DEBUG-ASSERT-FOR-INTERNAL-INVARIANTS`](rust/rust-use-debug-assert-for-internal-invariants.md).
  Use debug assertions for internal invariants that should hold if nearby code is correct. Do not
  use them for caller validation or safety requirements that must be enforced in release builds.
- [`RUST-USE-DIRECTORY-MODULES-AS-TABLES-OF-CONTENTS`](rust/rust-use-directory-modules-as-tables-of-contents.md).
  Let directory module files introduce, organize, and re-export the concepts owned by that
  directory. Keep substantial implementation in named child files so the module remains a readable
  table of contents.
- [`RUST-USE-DOC-INLINE-FOR-CANONICAL-REEXPORTS`](rust/rust-use-doc-inline-for-canonical-reexports.md).
  Use `#[doc(inline)]` when a re-export should be the canonical place readers encounter an item.
  Avoid inlining re-exports that would obscure the owning module or create duplicate-looking
  documentation.
- [`RUST-USE-FIELD-INIT-SHORTHAND`](rust/rust-use-field-init-shorthand.md). Use field init shorthand
  when variable names already match struct fields so initialization stays compact and familiar.
  Spell fields out when renaming, conversion, or policy deserves visible attention.
- [`RUST-USE-FUNCTIONS-FOR-INCIDENTAL-TYPES`](rust/rust-use-functions-for-incidental-types.md).
  Prefer free or module functions when a type does not own the operation or invariant. Move behavior
  onto a type when the method relationship clarifies state, policy, or trait design.
- [`RUST-USE-HONEST-MINIMUM-DEPENDENCIES`](rust/rust-use-honest-minimum-dependencies.md). Set
  dependency requirements to the lowest compatible versions the crate actually supports. Raise
  minimums only for required APIs, fixes, features, security needs, or MSRV interactions.
- [`RUST-USE-MEANINGFUL-STANDARD-TYPES`](rust/rust-use-meaningful-standard-types.md). Prefer
  standard or ecosystem types that encode ownership, units, paths, durations, optionality, and
  invariants better than raw strings or integers. Use domain newtypes when the standard type cannot
  prevent meaningful mixups.
- [`RUST-USE-SEND-STATIC-ACROSS-TASKS`](rust/rust-use-send-static-across-tasks.md). Require owned
  `Send + 'static` values, futures, errors, and handles when they cross spawn or thread boundaries.
  Avoid imposing those bounds on local synchronous APIs where they would reject valid use.
- [`RUST-VALIDATE-BUILDERS-ON-BUILD`](rust/rust-validate-builders-on-build.md). Validate cross-field
  builder invariants in `build` where partial configuration becomes a usable value. Keep `build`
  infallible only when defaults and setters make invalid states impossible.
- [`RUST-VALIDATE-PACKAGE-CONTENTS-BEFORE-RELEASE`](rust/rust-validate-package-contents-before-release.md).
  Inspect and build the package users will receive, not just the repository checkout. This catches
  missing assets, accidental inclusions, README drift, and include/exclude mistakes before
  publication.
- [`RUST-VALIDATE-RUST-DOCS-AS-CODE`](rust/rust-validate-rust-docs-as-code.md). Treat Rust
  documentation examples, links, feature assumptions, and generated README content as code that must
  be checked. Use docs builds, doctests, feature-gated checks, and Markdown lint according to the
  changed surface.
- [`RUST-VALIDATE-SEMVER-BREAKS-AGAINST-EXTERNAL-USE`](rust/rust-validate-semver-breaks-against-external-use.md).
  Check semver-breaking changes against real examples, dependents, or migration paths before
  treating an API cleanup as cheap. External evidence informs the cost even when security,
  soundness, or design repair still justify the break.
- [`RUST-VALIDATE-UNSAFE-THROUGH-SAFE-API`](rust/rust-validate-unsafe-through-safe-api.md). Test
  unsafe internals through the safe API wrapper that callers rely on. Internal unsafe tests and
  tools such as Miri should support, not replace, proof that safe calls uphold the contract.
- [`RUST-WORKING-RUST-CODE-NOT-ENOUGH`](rust/rust-working-rust-code-not-enough.md). Treat
  compilation as necessary but insufficient evidence for long-lived Rust code. Review API shape,
  docs, errors, tests, features, dependencies, and module organization because users and maintainers
  inherit those choices.
- [`RUST-WRITE-ACTIONABLE-ERROR-DISPLAY`](rust/rust-write-actionable-error-display.md). Write
  `Display` messages that tell humans what failed and what useful next action or context exists.
  Keep structured state in error fields, sources, diagnostics, or `Debug` instead of dumping
  internals into the user-facing string.
- [`RUST-WRITE-PUBLIC-DOCS-FOR-CALLER-TASKS`](rust/rust-write-public-docs-for-caller-tasks.md).
  Write public Rustdoc around what callers are trying to decide, do, and rely on. Start with concise
  behavior and add arguments, failures, lifecycle, features, links, or examples only when they help
  the task.
- [`RUST-WRITE-RUSTDOC-AS-API-CONTRACT`](rust/rust-write-rustdoc-as-api-contract.md). Use Rustdoc to
  state caller-facing behavior, invariants, failures, side effects, and compatibility promises.
  Leave private implementation detail in comments unless it helps maintain the public contract.

### Source And Context Hygiene

- [`SOURCE-GENERALIZE-PROJECT-SPECIFIC-RULES`](source/source-generalize-project-specific-rules.md).
  Extract the portable failure mode before promoting local lessons into shared guidance. Provider,
  repo, or tool details should stay local unless they clarify the durable rule.
- [`SOURCE-KEEP-BINARIES-OUT-OF-SOURCE-CONTROL`](source/source-keep-binaries-out-of-source-control.md).
  Store large or opaque artifacts in systems designed for assets, releases, CI evidence, or external
  data. Keeping source history textual and reviewable avoids clone cost and painful history
  rewrites.
- [`SOURCE-MAKE-SHARED-ARTIFACTS-STANDALONE`](source/source-make-shared-artifacts-standalone.md).
  Restate the problem, rationale, evidence, and tradeoffs in artifacts that leave the local session.
  Future readers should not need private notes or transcripts to trust the result.
- [`SOURCE-PREFER-PRIMARY-STABLE-SOURCES`](source/source-prefer-primary-stable-sources.md). Anchor
  durable guidance in sources readers can inspect, compare, and challenge. Use links to clarify
  judgment, not to decorate rules or depend on private memory.

### Tests Should Explain Failures

- [`TEST-AVOID-OPAQUE-BOOLEAN-ASSERTIONS`](test-failures/test-avoid-opaque-boolean-assertions.md).
  Prefer comparisons or richer assertions when many causes can make a boolean false. The first
  failure should show the actual state needed to diagnose the regression.
- [`TEST-OPTIMIZE-FAILURE-OUTPUT`](test-failures/test-optimize-failure-output.md). Design tests so
  failures include expected values, actual values, inputs, and contract context where that helps
  repair. Useful output shortens CI and agent debugging loops.
- [`TEST-SPLIT-UNRELATED-ASSERTIONS`](test-failures/test-split-unrelated-assertions.md). Split
  assertions that diagnose different behaviors when one failure would hide another. Keep checks
  together only when they express one contract more clearly as a group.

### Testing And Verification

- [`TEST-CHECK-IMPORTANT-FEATURE-COMBINATIONS`](testing/test-check-important-feature-combinations.md).
  Exercise default, disabled-default, all-feature, and important feature-pair builds. Feature flags
  change APIs and compile paths, so use a risk-based matrix instead of every combo.
- [`TEST-CHECK-MAINTAINER-COMMANDS-IN-CI`](testing/test-check-maintainer-commands-in-ci.md). Put
  documented maintainer commands, or intentionally stronger equivalents, in CI. This keeps local
  instructions honest while leaving slow or credentialed checks to special jobs.
- [`TEST-CHECK-MSRV-AND-PLATFORMS`](testing/test-check-msrv-and-platforms.md). Run checks for
  declared Rust versions and supported platforms when they are promised. Compatibility claims are
  public contracts, so skip matrices only when no such claim exists.
- [`TEST-CHOOSE-VALIDATION-BY-RISK`](testing/test-choose-validation-by-risk.md). Match the amount
  and kind of validation to the changed surface and failure cost. Cheap checks come first, but risky
  or uncertain behavior needs targeted evidence.
- [`TEST-COVER-ASYNC-ROUTING-EDGE-CASES`](testing/test-cover-async-routing-edge-cases.md). Test late
  replies, unrelated input, timeouts, and unmatched async responses. These cases protect request
  correlation and cleanup without relying on wall-clock luck.
- [`TEST-COVER-LOCAL-LOGIC-WITH-UNIT-TESTS`](testing/test-cover-local-logic-with-unit-tests.md). Use
  unit tests for small local logic such as parsing helpers and policy branches. They give fast
  precise feedback, while boundary behavior still needs higher-level tests.
- [`TEST-COVER-NAVIGATION-BOUNDARIES`](testing/test-cover-navigation-boundaries.md). Exercise first,
  last, empty, oversized, and repeated-navigation states in tests. Boundary cases catch cursor and
  scrolling bugs that polished manual demos often miss.
- [`TEST-COVER-POLICY-OUTCOMES`](testing/test-cover-policy-outcomes.md). Test allowed, denied,
  redacted, fallback, and unsupported policy outcomes. Policy value lives at decision boundaries, so
  assert caller-visible behavior instead of internals.
- [`TEST-COVER-PUBLIC-BOUNDARIES-WITH-INTEGRATION-TESTS`](testing/test-cover-public-boundaries-with-integration-tests.md).
  Use integration tests to prove public module, crate, or adapter boundaries. They catch composition
  failures unit tests miss, while local logic can stay unit-tested.
- [`TEST-COVER-PUBLIC-EXAMPLES-WITH-DOCTESTS`](testing/test-cover-public-examples-with-doctests.md).
  Compile public documentation examples as doctests when they do not need fragile state. Executable
  examples catch stale guidance, reserving no-run or ignored examples for real limits.
- [`TEST-FUZZ-PARSERS-FORMATTERS-AND-STATE-MACHINES`](testing/test-fuzz-parsers-formatters-and-state-machines.md).
  Use fuzzing or property tests for input-heavy parsers, formatters, and state machines. Large input
  spaces hide failures, so keep long fuzzing outside PR gates unless it is stable.
- [`TEST-KEEP-DRIFT-CLAIMS-ALIGNED`](testing/test-keep-drift-claims-aligned.md). Tie support claims,
  fixtures, examples, docs, and API paths to executable drift checks. Stable claims need evidence,
  but wording-only changes should not break broad tests.
- [`TEST-KEEP-SLOW-CHECKS-OUT-OF-PR-CI`](testing/test-keep-slow-checks-out-of-pr-ci.md). Keep long
  fuzzing, exhaustive matrices, and noisy benchmarks out of required PR CI. Fast gates preserve
  review flow, while heavier checks belong in release or scheduled validation.
- [`TEST-MATCH-EVIDENCE-TO-SURFACE`](testing/test-match-evidence-to-surface.md). Validate the actual
  changed surface, such as rendered docs, API behavior, or byte output. The narrowest relevant proof
  is more persuasive than unrelated broad test success.
- [`TEST-PREFER-DETERMINISTIC-TESTS`](testing/test-prefer-deterministic-tests.md). Prefer tests
  controlled by fixed inputs, clocks, ordering, and local state. Deterministic failures are
  reproducible, while real integration checks should be isolated by cost.
- [`TEST-PROVE-COMMAND-CONSTRUCTION-AND-DISPLAY`](testing/test-prove-command-construction-and-display.md).
  Test both executable command shape and displayed command text when users rely on them. Quoting,
  redaction, ordering, and platform formatting can fail even when a local happy path works.
- [`TEST-PROVE-CONTRACTS-NOT-TRIVIA`](testing/test-prove-contracts-not-trivia.md). Write tests
  around observable contracts instead of private helper trivia. This preserves refactoring freedom
  unless the detail is itself the promised behavior.
- [`TEST-RUN-DOCS-AS-FIRST-CLASS-GATE`](testing/test-run-docs-as-first-class-gate.md). Treat
  documentation checks as real validation for examples, links, commands, and claims. Prose-only
  edits may need less proof, but API-facing docs should fail before stale guidance ships.
- [`TEST-RUN-FAST-FORMAT-AND-LINT-GATES-EARLY`](testing/test-run-fast-format-and-lint-gates-early.md).
  Run cheap format and lint gates early in the feedback loop. They remove mechanical failures
  quickly, but they do not replace validation of risky behavior.
- [`TEST-USE-REALISTIC-PARSER-SAMPLES`](testing/test-use-realistic-parser-samples.md). Test parsers
  with representative input, malformed cases, and safe degradation examples. Real samples catch
  compatibility failures, but fixtures should be minimized and scrubbed.
- [`TEST-VALIDATE-DECLARED-MINIMUM-DEPENDENCY-VERSIONS`](testing/test-validate-declared-minimum-dependency-versions.md).
  Check that declared minimum dependency versions still build the supported behavior. Lockfile tests
  can hide newer API usage, so use targeted minimal-version checks when needed.
- [`TEST-WRITE-REGRESSION-TESTS-FOR-BUG-FIXES`](testing/test-write-regression-tests-for-bug-fixes.md).
  Add a test that fails before the bug fix and protects the repaired contract. Skip only when
  reproduction is impractical, and then record the closest trustworthy validation.

### JJ Topology And Source Control

- [`VCS-ASK-BEFORE-REPAIRING-JJ-ALIASES`](vcs/vcs-ask-before-repairing-jj-aliases.md). Ask before
  changing jj aliases when they disagree with the observed repository topology. Aliases encode
  workflow policy, so silent repairs can alter future user commands.
- [`VCS-AVOID-INTERACTIVE-JJ-IN-AGENT-WORK`](vcs/vcs-avoid-interactive-jj-in-agent-work.md). Use
  noninteractive jj commands with explicit messages, targets, and files in agent work. Interactive
  editors, prompts, merge tools, and pagers can hang unattended sessions.
- [`VCS-CONFIGURE-JJ-PAGER`](vcs/vcs-configure-jj-pager.md). Scope pager control with `--no-pager`,
  `JJ_PAGER=cat`, or session configuration. Direct output keeps source-control evidence visible
  without changing the user's global pager.
- [`VCS-CONFIRM-BROAD-JJ-OPERATIONS`](vcs/vcs-confirm-broad-jj-operations.md). Confirm jj operations
  that abandon, rebase, squash, split, restore, publish, or go broad. Confirmation protects
  unrelated work when a command can reshape history or public state.
- [`VCS-CONFIRM-GITHUB-REMOTE-TOPOLOGY`](vcs/vcs-confirm-github-remote-topology.md). Inspect
  `origin`, `upstream`, push remote, PR base, and PR head before publication. Fork and owned-repo
  layouts differ, so defaults can push or target the wrong repository.
- [`VCS-CREATE-OPERATION-LOG-POINT-BEFORE-RESHAPING`](vcs/vcs-create-operation-log-point-before-reshaping.md).
  Create a recent jj operation boundary before risky stack reshaping. Recovery is easier when there
  is a known point before rebases, splits, squashes, or repairs.
- [`VCS-DO-NOT-FALL-BACK-TO-GIT-FOR-JJ-ISSUES`](vcs/vcs-do-not-fall-back-to-git-for-jj-issues.md).
  Diagnose jj locks, pager issues, and state problems through jj before switching tools. Git
  bypasses jj change-graph semantics, so use it only for transport after jj state is coherent.
- [`VCS-DRY-RUN-SURPRISING-PUBLICATION`](vcs/vcs-dry-run-surprising-publication.md). Use dry-run for
  ambiguous or surprising remote publication, not every routine push. Extra verification pays off
  when remotes, bookmarks, force-like updates, or PR bases are unclear.
- [`VCS-DUPLICATE-FOR-ALTERNATIVE-CANDIDATES`](vcs/vcs-duplicate-for-alternative-candidates.md). Use
  `jj duplicate` when two plausible fixes or refactors need independent validation. Separate
  candidate changes preserve comparison and recovery without mutating the only option.
- [`VCS-INSPECT-SPARSE-STATE`](vcs/vcs-inspect-sparse-state.md). Check sparse checkout state before
  treating a missing path as absent from history. Sparse patterns can hide files, so inspection
  prevents recreating or editing the wrong path.
- [`VCS-INSPECT-STATE-BEFORE-MUTATING`](vcs/vcs-inspect-state-before-mutating.md). Inspect
  working-copy, stack, bookmark, conflict, and unowned state before mutation. Current state keeps
  edits scoped and avoids rewriting work the agent did not inspect.
- [`VCS-JJ-AS-SOURCE-OF-TRUTH`](vcs/vcs-jj-as-source-of-truth.md). Use jj for local workflow in
  repositories with `.jj` state. This preserves descriptions, stack shape, operation-log recovery,
  and bookmark semantics.
- [`VCS-JJ-NEW-FOR-REVIEW-LANES`](vcs/vcs-jj-new-for-review-lanes.md). Start unrelated review units
  with `jj new` before edits accumulate. Separate changes keep review atomic while leaving later
  squash or absorb decisions easy.
- [`VCS-MAKE-GITHUB-HANDOFF-EXPLICIT`](vcs/vcs-make-github-handoff-explicit.md). Name bookmark,
  remote, base, head, and repo when handing coherent jj state to GitHub. Explicit publication avoids
  host-tool inference mistakes in forks, stacks, and multi-remote repos.
- [`VCS-MATCH-JJ-TOPOLOGY-TO-REPO-ROLE`](vcs/vcs-match-jj-topology-to-repo-role.md). Align fetch
  remotes, push remotes, tracked bookmarks, aliases, and PR bases to repo role. Owned, maintainer,
  and fork-only workflows need different topology assumptions.
- [`VCS-NAME-EXACT-JJ-MUTATION-TARGETS`](vcs/vcs-name-exact-jj-mutation-targets.md). Specify
  revisions, filesets, bookmarks, and destinations for mutating jj commands. Explicit targets make
  intent reviewable and prevent defaults from acting on surprising state.
- [`VCS-QUOTE-REVSETS-AND-SHELL-SYNTAX`](vcs/vcs-quote-revsets-and-shell-syntax.md). Quote jj
  revsets, bookmark syntax, and other shell-sensitive command fragments. Shell metacharacters can
  alter commands, so examples should prefer simple safe quoting.
- [`VCS-RECOVER-WITH-OPERATION-LOG`](vcs/vcs-recover-with-operation-log.md). Use jj operation-log
  recovery before destructive cleanup habits. The operation log preserves recoverable graph states,
  but inspect the target before restoring.
- [`VCS-REPAIR-REMOTE-TOPOLOGY-COHERENTLY`](vcs/vcs-repair-remote-topology-coherently.md). Repair
  fetch, push, tracking, trunk alias, PR base, and PR head assumptions together. Remote topology is
  coupled, so partial fixes can leave publication commands half-correct.
- [`VCS-RUN-JJ-MUTATIONS-SEQUENTIALLY`](vcs/vcs-run-jj-mutations-sequentially.md). Do not overlap jj
  commands that write repo, working-copy, bookmark, or config state. Sequential mutations avoid
  locks, stale reads, and confusing operation order.
- [`VCS-SCOPE-JJ-FILE-TRACKING`](vcs/vcs-scope-jj-file-tracking.md). Pass intended paths to `jj file
  track` and `jj file untrack`. Scoped tracking keeps local-only, generated, or unrelated files out
  of publication state.
- [`VCS-STOP-REPEATED-JJ-RETRIES-AND-LOCALIZE-STATE`](vcs/vcs-stop-repeated-jj-retries-and-localize-state.md).
  Stop repeating a failing jj command after a transient retry and inspect relevant state. Diagnosis
  beats command spam when locks, sparse paths, bookmarks, or remotes disagree.
- [`VCS-TRACK-REMOTES-EXPLICITLY`](vcs/vcs-track-remotes-explicitly.md). Set explicit remote
  tracking when the same bookmark name exists on multiple remotes. This prevents fetch, rebase, and
  publication ambiguity in fork and upstream workflows.
- [`VCS-TREAT-BOOKMARK-REMOTE-SYNTAX-AS-VERSION-SENSITIVE`](vcs/vcs-treat-bookmark-remote-syntax-as-version-sensitive.md).
  Verify `bookmark@remote` and remote-bookmark syntax against the installed jj version. Durable
  guidance should avoid assuming one spelling works across commands and releases.
- [`VCS-USE-EVOLOG-AND-OPERATION-LOG`](vcs/vcs-use-evolog-and-operation-log.md). Use `jj evolog` for
  a change's evolution and `jj op log` for repository operations. Picking the right log
  distinguishes rewrite history from workspace, bookmark, and import events.
- [`VCS-USE-GIT-FORMATTED-DIFFS-FOR-AGENTS`](vcs/vcs-use-git-formatted-diffs-for-agents.md). Prefer
  `jj diff --git` when agents or patch-oriented tools need diff text. Git patch format preserves
  hunks and paths in a shape those consumers can parse reliably.
- [`VCS-USE-IGNORE-WORKING-COPY-CAREFULLY`](vcs/vcs-use-ignore-working-copy-carefully.md). Use
  `--ignore-working-copy` only for understood lock-safe inspection or metadata work. It may read
  stale file state, so do not use it to bypass normal synchronization before edits.
- [`VCS-WORKSPACE-ADD-FOR-SECOND-CHECKOUTS`](vcs/vcs-workspace-add-for-second-checkouts.md). Use `jj
  workspace add` only when a task needs another filesystem checkout. Ordinary review separation
  should use `jj new`; workspaces fit clean validation or parallelism.
