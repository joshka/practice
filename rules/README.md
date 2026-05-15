# Rules

Rules are compact instructions supported by the guides, principles, patterns, and
mechanisms in this repo. Each rule has its own file so it can be reviewed, deepened, linked,
and extracted into compressed agent instructions independently.

## Rule File Shape

Each rule file should keep these sections:

- `Metadata`: stable ID, legacy ID, status, domain, and depth.
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

- [Agent Workflow](agent-workflow/README.md). 25 rules. Agent workflow rules cover objectives,
  scoped capabilities, durable context, review packets, security proof, feedback loops, and concrete
  next choices.
- [Explicit Boundaries Preserve Correctness](boundary/README.md). 25 rules. Boundary rules cover
  parsing, validation policy, explicit inputs, state transitions, provider diagnostics, effect
  boundaries, and external reconciliation.
- [Change Shape](change-shape/README.md). 11 rules. Change-shape rules cover one-purpose changes,
  small follow-ups, generated artifacts, dependency churn, ownership, and structure-versus-behavior
  review boundaries.
- [Docs Are Contracts](documentation/README.md). 26 rules. Documentation rules cover
  docs-as-contracts, rendered docs, examples, reviewability, source links, concrete prose, and drift
  checks.
- [Observability And Failure](observability/README.md). 5 rules. Observability rules cover owned
  logging boundaries, durable failure visibility, diagnostic context, failure states, and safe
  telemetry retention.
- [Measure Before Optimizing](performance/README.md). 7 rules. Performance rules cover measuring
  before optimizing, benchmark provenance, single-run skepticism, correctness gates, and the cost of
  complexity or dependency churn.
- [Local Reasoning And Refactoring](refactoring/README.md). 8 rules. Refactoring rules cover local
  reasoning, concept helpers, visible linear stories, side-effect loops, whitespace paragraphs, DRY
  pressure, and weak abstractions.
- [Private Context And Review Artifacts](review/README.md). 6 rules. Review artifact rules cover
  issue slices, PR narratives, ADRs, speculation labels, thread ownership, and artifacts that stand
  alone without private session context.
- [Rust API And Crate Shape](rust/README.md). 46 rules. Rust rules cover public API shape, crate
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

- [`AGENT-BUDGET-FOR-FEEDBACK-LOOPS`](agent-workflow/agent-budget-for-feedback-loops.md). Budget
  tokens and time for feedback loops. Agent work needs room for reading, editing, running checks,
  inspecting failures, and reporting proof. Helps: Prevents premature handoff and makes validation
  failures part of the planned work instead of a surprise.
- [`AGENT-DEFINE-GOOD-BEFORE-JUDGMENT-HEAVY-WORK`](agent-workflow/agent-define-good-before-judgment-heavy-work.md).
  Define good before judgment-heavy work. Agents are weak at guessing taste after the fact. Helps:
  Produces better first-pass output and reduces rewrites caused by hidden taste criteria.
- [`AGENT-DISTILL-FROM-BLESSED-ARTIFACTS`](agent-workflow/agent-distill-from-blessed-artifacts.md).
  Distill from blessed artifacts. Existing accepted code, docs, tests, PRs, and review comments are
  often denser than a new prompt. Helps: Preserves local voice and implementation style while
  reducing repeated human steering.
- [`AGENT-ENCODE-NONFUNCTIONAL-REQUIREMENTS`](agent-workflow/agent-encode-nonfunctional-requirements.md).
  Encode nonfunctional requirements. Requirements such as latency, accessibility, reviewability,
  security, privacy, determinism, and downstream compatibility are easy for agents to miss because
  they may not appear in the immediate diff. Helps: Keeps invisible constraints from being
  discovered only during review or production use.
- [`AGENT-GIVE-OBJECTIVES-WITH-BOUNDARIES`](agent-workflow/agent-give-objectives-with-boundaries.md).
  Give agents objectives with boundaries, not brittle step lists. A brittle step list can make an
  agent follow the wrong route even after the codebase shows a better one. Helps: Preserves intent
  while letting the agent adapt to real repo structure and discovered constraints.
- [`AGENT-GRANT-SCOPED-CAPABILITIES`](agent-workflow/agent-grant-scoped-capabilities.md). Grant
  scoped agent capabilities. Agents with broad authority can accidentally mutate external systems,
  publish state, delete files, or read secrets unrelated to the task. Helps: Reduces blast radius
  and makes permission boundaries auditable.
- [`AGENT-ISOLATE-WORKSPACES-BY-TASK`](agent-workflow/agent-isolate-workspaces-by-task.md). Isolate
  agent workspaces by task. Parallel agent tasks can overwrite each other, mix unrelated diffs, or
  make validation ambiguous when they share one working copy. Helps: Keeps concurrent work
  reviewable and prevents one task from inheriting another task's partial edits.
- [`AGENT-KEEP-DURABLE-CONTEXT-ON-DISK`](agent-workflow/agent-keep-durable-context-on-disk.md). Keep
  durable context on disk. Prompt context disappears, compacts, or becomes invisible to future
  sessions. Helps: Prevents accepted guidance from being trapped in one chat and makes long-running
  work resumable.
- [`AGENT-KEEP-SECRETS-OUT-OF-CONTEXT`](agent-workflow/agent-keep-secrets-out-of-context.md). Keep
  secrets out of context. Secrets pasted into prompts, docs, logs, or test output can be retained,
  repeated, or committed accidentally. Helps: Reduces credential leakage and keeps shared artifacts
  safe to publish.
- [`AGENT-MAKE-BAD-OUTPUT-HARD`](agent-workflow/agent-make-bad-output-hard.md). Make bad output
  mechanically hard. Repeated prompt reminders are weaker than a repo that rejects bad output
  mechanically. Helps: Turns recurring review feedback into enforcement and lowers the cost of good
  output.
- [`AGENT-PREFER-BUILD-PRESERVING-EDITS`](agent-workflow/agent-prefer-build-preserving-edits.md).
  Prefer build-preserving edits when the route stays natural. A long period of broken build state
  hides which edit caused the failure and makes agent recovery harder. Helps: Improves
  bisectability, local recovery, and confidence during multi-step edits.
- [`AGENT-PREFER-IN-DISTRIBUTION-TOOLS`](agent-workflow/agent-prefer-in-distribution-tools.md).
  Prefer in-distribution tools for agent-facing work. Agents are more reliable with tools that match
  their trained and tested workflow. Helps: Reduces tool misuse and makes commands easier for humans
  to rerun.
- [`AGENT-PREFER-TOOLS-OVER-PROMPTS`](agent-workflow/agent-prefer-tools-over-prompts.md). Prefer
  tools and checks over repeated prompting. If the same instruction must be repeated to every agent,
  it belongs in a tool, check, template, or guide. Helps: Converts repeated steering into durable
  enforcement and frees human attention for ambiguous decisions.
- [`AGENT-PRESENT-CONCRETE-NEXT-OPTIONS`](agent-workflow/agent-present-concrete-next-options.md).
  Present concrete next options after validated chunks. After a validated chunk, the maintainer
  needs to decide what happens next, not decode vague choices such as "continue" or "more cleanup."
  Naming the next chunk and why to choose it makes review flow cheap and keeps scope under human
  control. Helps: Makes iterative work easy to steer and prevents agents from silently choosing
  preference-sensitive follow-ups.
- [`AGENT-PRESERVE-HUMAN-WORK`](agent-workflow/agent-preserve-human-work.md). Preserve unrelated
  human work. Agents share a working tree with human edits and sometimes other agents. Helps:
  Protects user work and keeps diffs limited to the task the agent owns.
- [`AGENT-PRESERVE-INTENT`](agent-workflow/agent-preserve-intent.md). Preserve intent over
  literalism. Literal execution can satisfy the words while missing the goal. Helps: Keeps agent
  work aligned with the user's real objective instead of producing brittle literal compliance.
- [`AGENT-PRODUCE-REVIEW-PACKETS`](agent-workflow/agent-produce-review-packets.md). Produce review
  packets for agent output. Agent output often spans code, docs, generated artifacts, and validation
  logs. Helps: Makes agent output reviewable and reduces trust gaps around what was actually
  checked.
- [`AGENT-PROVE-SECURITY-IMPACT`](agent-workflow/agent-prove-security-impact.md). Prove security
  impact separately from hypotheses. Security claims are easy to overstate. Helps: Makes security
  review concrete and keeps mitigations tied to demonstrated risk.
- [`AGENT-REPORT-PROOF-IN-HANDOFFS`](agent-workflow/agent-report-proof-in-handoffs.md). Report
  proof, not confidence, in agent handoffs. Confidence language is not evidence. Helps: Improves
  handoff quality and makes residual risk visible.
- [`AGENT-SEPARATE-NOTES-FROM-CORRECTIONS`](agent-workflow/agent-separate-notes-from-corrections.md).
  Separate note capture from correction during fast review. During fast review, it is tempting for
  an agent to fix each note immediately. Helps: Preserves review signal and turns clustered feedback
  into better guidance or cleaner edits.
- [`AGENT-SPEND-HUMAN-ATTENTION-ON-AMBIGUITY`](agent-workflow/agent-spend-human-attention-on-ambiguity.md).
  Spend human attention on ambiguity. Agents can spend a lot of effort executing through an
  unresolved decision. Helps: Uses human attention where it changes direction and lets agents handle
  the well-bounded work after that.
- [`AGENT-SUGGEST-LOCAL-OVERRIDE-FILES`](agent-workflow/agent-suggest-local-override-files.md).
  Suggest ignored agent override files for local-only repo context. Some agent instructions are true
  only for one checkout: local jj topology, ignored plan directories, machine-specific paths, or
  temporary repo notes. Helps: Separates local steering from shared policy and reduces accidental
  leakage of machine-specific state.
- [`AGENT-TURN-FEEDBACK-INTO-GUIDANCE`](agent-workflow/agent-turn-feedback-into-guidance.md). Turn
  repeated feedback into durable guidance. Repeated corrections such as "show why," "name the next
  thing," or "do not use abstract rule names" are process bugs. Helps: Converts review friction into
  durable improvement of the workflow.
- [`AGENT-USE-AGENTS-MD-AS-MAP`](agent-workflow/agent-use-agents-md-as-map.md). Use `AGENTS.md` as a
  map, not the whole manual. `AGENTS.md` becomes hard to use when it tries to contain every rule,
  example, and exception. Helps: Keeps agent instructions scannable and reduces context bloat
  without losing durable guidance.
- [`AGENT-VERIFY-RISKY-CHANGES-WITH-CANARIES`](agent-workflow/agent-verify-risky-changes-with-canaries.md).
  Verify risky changes with canaries before cutover. Some changes can pass local tests and still
  fail when exposed to real traffic, real docs rendering, real provider state, or real users. Helps:
  Reduces blast radius for deployment, integration, migration, and generated-behavior changes.

### Explicit Boundaries Preserve Correctness

- [`BOUNDARY-AVOID-GLOBAL-MUTABLE-STATE`](boundary/boundary-avoid-global-mutable-state.md). Avoid
  global mutable state. Global mutable state hides ownership, ordering, reset, and concurrency
  requirements. Helps: Improves test isolation, explicit lifecycle management, and reasoning about
  shared state.
- [`BOUNDARY-CHOOSE-RESOURCE-IDENTITY-MODEL`](boundary/boundary-choose-resource-identity-model.md).
  Choose the resource identity model up front. A system that mutates individual records behaves
  differently from one that mutates record sets, files, sessions, handles, or whole documents.
  Helps: Prevents reconciliation bugs caused by comparing or mutating the wrong unit of state.
- [`BOUNDARY-DEFINE-COMPACTION-INVARIANTS`](boundary/boundary-define-compaction-invariants.md).
  Define explicit budget and cut-point invariants for compaction. Compaction deletes, summarizes, or
  moves information. Helps: Makes summarization, pruning, and context-window management testable and
  reviewable.
- [`BOUNDARY-DEFINE-HOOK-FAILURE-POLICY`](boundary/boundary-define-hook-failure-policy.md). Define
  hook failure policy. Hooks can fail before, during, or after the main operation. Helps: Makes
  extension, callback, and automation behavior predictable under failure.
- [`BOUNDARY-DISTINGUISH-INPUT-CLASSES`](boundary/boundary-distinguish-input-classes.md). Keep
  unknown, unsupported, denied, and preserved inputs distinct. Unknown, unsupported, denied, and
  preserved inputs require different treatment. Helps: Preserves compatibility semantics and gives
  callers actionable errors.
- [`BOUNDARY-EXPOSE-PARTIAL-STREAM-OUTPUT`](boundary/boundary-expose-partial-stream-output.md).
  Expose partial provider-stream output without making it authoritative too early. Provider streams
  often deliver partial tokens, chunks, or events before the final authoritative result. Helps:
  Supports progress and diagnostics while keeping final state promotion explicit.
- [`BOUNDARY-GIVE-TOOLS-IDENTITY-POLICY-AND-LIMITS`](boundary/boundary-give-tools-identity-policy-and-limits.md).
  Give tool boundaries typed identity, policy, cancellation, and output limits. Tool calls need
  typed identity, authorization policy, cancellation behavior, and output limits because they cross
  from controlled code into filesystem, shell, network, provider, or user-visible effects. Helps:
  Reduces tool blast radius and makes execution, cancellation, and diagnostics predictable.
- [`BOUNDARY-GROUND-INTEGRATIONS-IN-PRIMARY-SOURCES`](boundary/boundary-ground-integrations-in-primary-sources.md).
  Ground integration behavior in primary source documentation. Provider and platform behavior
  changes, and memory of an integration is often wrong. Helps: Keeps adapters honest and makes
  integration limits reviewable.
- [`BOUNDARY-IDENTIFY-ANEMIC-STATE-MACHINES`](boundary/boundary-identify-anemic-state-machines.md).
  Identify anemic state machines. Auth flows, UI state, async routing, setup wizards, and lifecycle
  code often hide a state machine inside booleans and scattered conditionals. Helps: Makes stateful
  behavior easier to test, extend, and reason about.
- [`BOUNDARY-KEEP-BACKEND-ADAPTERS-AT-EDGE`](boundary/boundary-keep-backend-adapters-at-edge.md).
  Keep backend adapters at the edge. Backend-specific APIs for terminals, storage, network
  providers, or runtimes spread quickly if they enter core logic. Helps: Reduces coupling to
  specific providers and makes alternate backends easier to test or add.
- [`BOUNDARY-MAKE-AMBIENT-INPUTS-EXPLICIT`](boundary/boundary-make-ambient-inputs-explicit.md). Make
  ambient inputs explicit. Time, randomness, environment variables, current directories, locale,
  terminal size, network clients, and process state can change behavior without appearing in
  function signatures. Helps: Makes nondeterminism injectable and reduces hidden dependencies.
- [`BOUNDARY-MAKE-DYNAMIC-CONFLICTS-DETERMINISTIC`](boundary/boundary-make-dynamic-conflicts-deterministic.md).
  Make dynamic registration conflicts deterministic and explicit. Dynamic registration from plugins,
  generated code, guests, or config can produce duplicate names, ordering conflicts, or shadowed
  handlers. Helps: Makes extension systems predictable and diagnosable.
- [`BOUNDARY-MAKE-EXEC-TOOLS-NONINTERACTIVE`](boundary/boundary-make-exec-tools-noninteractive.md).
  Make exec-like tools noninteractive by default. Exec-like tools called by agents, CI, or
  background tasks cannot safely wait for prompts, editors, pagers, or credential UI. Helps:
  Prevents stuck jobs and makes tool execution reproducible in automation.
- [`BOUNDARY-MODEL-REAL-UPSTREAM-SURFACE`](boundary/boundary-model-real-upstream-surface.md). Model
  each integration as the real upstream surface it exposes. Adapters should not pretend a provider
  supports a cleaner or broader API than it actually does. Helps: Prevents local APIs from promising
  behavior the upstream cannot provide.
- [`BOUNDARY-NAME-LIFECYCLE-TRANSITIONS`](boundary/boundary-name-lifecycle-transitions.md). Treat
  lifecycle transitions as named operations. Creation, activation, cancellation, teardown, reload,
  and promotion are different operations with different invariants. Helps: Makes lifecycle behavior
  explicit and keeps invalid ordering visible.
- [`BOUNDARY-PARSE-UNCERTAINTY-AT-EDGE`](boundary/boundary-parse-uncertainty-at-edge.md). Push
  uncertainty to the boundary, then pass trusted values inward. Raw strings, JSON, CLI args,
  provider responses, and user input contain uncertainty. Helps: Concentrates validation policy and
  reduces invalid states in core logic.
- [`BOUNDARY-READ-NORMALIZE-COMPARE-MUTATE`](boundary/boundary-read-normalize-compare-mutate.md).
  Reconcile external state by reading, normalizing, comparing, and then mutating. External state may
  be formatted differently, reordered, defaulted, or partially managed by another actor. Helps:
  Makes reconciliation idempotent and safer against provider drift.
- [`BOUNDARY-REJECT-UNSUPPORTED-SHAPES`](boundary/boundary-reject-unsupported-shapes.md). Reject
  unsupported shapes early with clear errors. Unsupported names, values, TTLs, targets, record
  families, protocols, or config modes should fail at the boundary with a clear error. Helps: Makes
  unsupported behavior explicit and prevents partial internal handling of invalid shapes.
- [`BOUNDARY-REPORT-PROVIDER-DIAGNOSTICS`](boundary/boundary-report-provider-diagnostics.md). Report
  freshness, permissions, budget, and load diagnostics from resource providers. When data comes from
  a provider, callers need to know whether it is fresh, partial, permission-limited, rate-limited,
  cached, or degraded. Helps: Helps users and agents interpret provider-backed results safely.
- [`BOUNDARY-SEPARATE-PURE-CORE-FROM-EFFECTS`](boundary/boundary-separate-pure-core-from-effects.md).
  Separate pure computation from rendering, I/O, or mutation when that gives tests a stable surface.
  Rendering, filesystem access, network calls, terminal mutation, and global state make behavior
  harder to test. Helps: Improves testability and keeps domain decisions visible without running the
  environment.
- [`BOUNDARY-SEPARATE-UI-AND-APP-STATE`](boundary/boundary-separate-ui-and-app-state.md). Keep UI
  state separate from application-owned state. UI state such as selection, scroll offset, focus,
  expanded rows, or transient input mode changes at a different rate than application-owned data.
  Helps: Keeps UI behavior testable and prevents presentation concerns from leaking into core state.
- [`BOUNDARY-STAGE-GENERATED-BEHAVIOR`](boundary/boundary-stage-generated-behavior.md). Stage
  generated or reloadable behavior before promotion. Generated, reloadable, or plugin-provided
  behavior can be malformed, stale, or incompatible with the current runtime. Helps: Makes dynamic
  behavior safer and more recoverable.
- [`BOUNDARY-TRACK-DYNAMIC-REGISTRATION-PROVENANCE`](boundary/boundary-track-dynamic-registration-provenance.md).
  Track provenance for registrations from extensions, guests, or generated code. When extensions,
  guests, generated code, or config register handlers, commands, routes, or tools, later conflicts
  and failures need to identify where each registration came from. Helps: Makes dynamic systems
  auditable and easier to debug after registration conflicts or failures.
- [`BOUNDARY-TREAT-TERMINAL-UI-AS-PRODUCT-SURFACE`](boundary/boundary-treat-terminal-ui-as-product-surface.md).
  Treat terminal UI as a product surface with platform-specific contracts. Terminal UI is not just
  debug output. Helps: Makes terminal behavior reviewable and protects users from layout and
  interaction regressions.
- [`BOUNDARY-USE-CONSERVATIVE-TERMINAL-DEFAULTS`](boundary/boundary-use-conservative-terminal-defaults.md).
  Use conservative terminal defaults. Terminals vary in color support, width, input behavior, fonts,
  and accessibility settings. Helps: Improves first-run usability and cross-terminal compatibility.

### Change Shape

- [`CHANGE-AVOID-UNNECESSARY-DEPENDENCY-CHURN`](change-shape/change-avoid-unnecessary-dependency-churn.md).
  Do not include dependency churn unless it is necessary for the task. Dependency updates change
  lockfiles, feature graphs, minimum versions, build output, and downstream compatibility. Helps:
  Keeps dependency risk reviewable and prevents unrelated lockfile movement from obscuring the task.
- [`CHANGE-IDENTIFY-OWNING-MODULE-BEFORE-EDITING`](change-shape/change-identify-owning-module-before-editing.md).
  Identify the owning module before editing. Editing the first file that mentions a behavior can put
  new logic in a caller, facade, test helper, or adapter that does not own the concept. Helps:
  Reduces scattered fixes and makes future readers find the behavior where they expect it.
- [`CHANGE-ISOLATE-CONTROVERSIAL-CHANGES`](change-shape/change-isolate-controversial-changes.md).
  Isolate controversial changes. Formatting, renames, API breaks, dependency changes, unsafe code,
  large rewrites, and behavior changes all invite different review questions. Helps: Keeps
  contentious decisions explicit and makes reverting or revising them cheaper.
- [`CHANGE-MINIMAL-BUT-COMPLETE`](change-shape/change-minimal-but-complete.md). Keep each change
  minimal but complete. A change that is too large hides risk, but a change that is too small can
  leave reviewers with an unexplained half-step. Helps: Gives reviewers a coherent unit that can be
  understood, validated, and reverted.
- [`CHANGE-PIN-BEHAVIOR-WITH-EARLY-TESTS`](change-shape/change-pin-behavior-with-early-tests.md).
  Use early test changes to pin existing behavior when that makes behavior changes easier to review.
  Before changing messy behavior, an early test can document what the system currently does. Helps:
  Makes behavior changes safer and clarifies whether later diffs preserve or intentionally change
  existing behavior.
- [`CHANGE-PREFER-SMALL-FOLLOW-UPS`](change-shape/change-prefer-small-follow-ups.md). Prefer small
  follow-up changes over overloaded changes. When a change uncovers adjacent cleanup, docs drift,
  naming issues, or broader refactoring, folding all of it into the current diff can hide the
  original purpose. Helps: Preserves review focus while still capturing useful nearby work.
- [`CHANGE-PRESERVE-UNOWNED-WORK`](change-shape/change-preserve-unowned-work.md). Preserve unowned
  work. A working tree can contain edits from the user, another agent, generated state, or an
  earlier in-progress change. Helps: Protects parallel work and keeps the current diff accountable
  for only the files it owns.
- [`CHANGE-SEPARATE-STRUCTURE-FROM-BEHAVIOR`](change-shape/change-separate-structure-from-behavior.md).
  Keep structure changes separate from behavior changes when the combined diff obscures review.
  Structure changes ask reviewers to confirm the code means the same thing; behavior changes ask
  them to confirm the system now does the right new thing. Helps: Makes reviews sharper and makes
  structure-only changes easier to revert if they were wrong.
- [`CHANGE-SYNC-GENERATED-ARTIFACTS`](change-shape/change-sync-generated-artifacts.md). Keep
  generated artifacts in sync when they are part of the review surface. Generated files, lockfiles,
  snapshots, API listings, and agent packs are part of the review surface when they are checked into
  the repo. Helps: Prevents drift between source inputs and generated outputs.
- [`CHANGE-TREAT-AND-AS-SCOPE-WARNING`](change-shape/change-treat-and-as-scope-warning.md). Treat
  `and` in a change description as a scope warning. A change titled "fix parser and update docs and
  clean API" often contains multiple review units. Helps: Catches accidental scope creep before the
  diff becomes hard to split.
- [`CHANGE-USE-ONE-PURPOSE-PER-CHANGE`](change-shape/change-use-one-purpose-per-change.md). Use one
  purpose per change. One-purpose changes let reviewers ask one main question: did this accomplish
  the stated goal? Helps: Improves review speed, revertability, and historical understanding of why
  code changed.

### Docs Are Contracts

- [`DOCS-ALIGN-README-AND-CRATE-RUSTDOC`](documentation/docs-align-readme-and-crate-rustdoc.md).
  Keep crate README and crate-level Rustdoc aligned. Crate users often meet the README on GitHub and
  the crate-level Rustdoc on docs.rs. Helps: Keeps the two main Rust entry points coherent and
  reduces drift between examples, feature flags, and public API claims.
- [`DOCS-AVOID-GENERATED-PROSE-TELLS`](documentation/docs-avoid-generated-prose-tells.md). Avoid
  generated-prose tells. Generated prose often sounds polished while hiding that it did not learn
  the project voice. Helps: Preserves local voice, keeps docs dense, and makes claims easier to
  verify.
- [`DOCS-AVOID-UNEARNED-PRAISE`](documentation/docs-avoid-unearned-praise.md). Avoid unearned
  ranking and vague praise. Words such as "simple," "powerful," "best," and "easy" are often
  unearned unless the doc states the comparison or tradeoff. Helps: Keeps claims credible and
  replaces praise with observable behavior, constraints, or tradeoffs.
- [`DOCS-BUILD-DOCS-LIKE-USERS-READ-THEM`](documentation/docs-build-docs-like-users-read-them.md).
  Build Rust docs the way users will read them. Rust docs are consumed through rendered Rustdoc,
  docs.rs feature configuration, intra-doc links, search, and examples. Helps: Catches rendered-doc
  failures and makes documentation review match the user-facing artifact.
- [`DOCS-CHOOSE-DOCUMENT-TYPE`](documentation/docs-choose-document-type.md). Choose the document
  type before editing. A page that mixes tutorial, reference, explanation, decision record, and
  changelog work makes every reader pay for every mode. Helps: Keeps docs navigable and prevents
  local edits from expanding into accidental page rewrites.
- [`DOCS-COMPARE-LIBRARIES-ACCURATELY`](documentation/docs-compare-libraries-accurately.md). Compare
  nearby libraries accurately and charitably. Comparisons with nearby libraries affect trust. Helps:
  Makes comparison docs credible and helps users choose based on real constraints instead of
  positioning language.
- [`DOCS-DOCUMENT-LIFECYCLE-AND-SIDE-EFFECTS`](documentation/docs-document-lifecycle-and-side-effects.md).
  Document lifecycle, ownership, side effects, feature flags, platform assumptions, and
  compatibility when callers need them. APIs that open files, spawn tasks, touch terminals, allocate
  resources, mutate global state, enable feature flags, or depend on platform behavior create
  obligations for callers. Helps: Makes caller obligations visible and reduces misuse around
  runtime, platform, feature, and cleanup behavior.
- [`DOCS-EXPOSE-MOVE-RISK-AND-EXAMPLE-IN-PATTERNS`](documentation/docs-expose-move-risk-and-example-in-patterns.md).
  Expose symptom, move, risk, example, and agent instruction in pattern-style guidance.
  Pattern-style guidance is useful when a reader can recognize the situation and apply the move.
  Helps: Makes patterns reviewable, teachable, and usable as agent instructions instead of vague
  slogans.
- [`DOCS-FRONT-LOAD-USEFUL-POINT`](documentation/docs-front-load-useful-point.md). Front-load the
  useful point. Readers scan docs for the decision, command, invariant, or warning that matters.
  Helps: Improves scanning and makes important commands, contracts, and caveats harder to miss.
- [`DOCS-KEEP-MARKDOWN-LINTABLE`](documentation/docs-keep-markdown-lintable.md). Keep Markdown
  lintable. Formatting drift adds review noise and makes generated or agent-edited docs harder to
  maintain. Helps: Keeps documentation diffs clean and makes style expectations enforceable by
  tools.
- [`DOCS-MAKE-REVIEW-EASY-TO-INSPECT`](documentation/docs-make-review-easy-to-inspect.md). Make
  documentation review easy to inspect. Docs are often reviewed as Markdown diffs even though users
  read rendered pages, generated Rustdoc, examples, screenshots, or command output. Helps: Speeds
  review and makes documentation proof concrete rather than confidence-based.
- [`DOCS-MARK-NONCOMPILING-EXAMPLES-HONESTLY`](documentation/docs-mark-noncompiling-examples-honestly.md).
  Prefer examples that compile, and mark noncompiling examples honestly. Rust examples are often
  copied directly into user projects or enforced as doctests. Helps: Keeps examples trustworthy and
  lets doctests protect public API usage where possible.
- [`DOCS-ONE-DOMINANT-MODE-PER-PAGE`](documentation/docs-one-dominant-mode-per-page.md). Pick one
  dominant documentation mode per page. A page with competing modes forces readers to switch mental
  models. Helps: Keeps each page useful for its main reader and moves secondary detail to
  better-linked places.
- [`DOCS-PROSE-FOR-RELATIONSHIPS-LISTS-FOR-ENUMERATION`](documentation/docs-prose-for-relationships-lists-for-enumeration.md).
  Use prose for relationships and lists for enumeration. Lists are good for fields, steps, options,
  and checks, but weak for explaining causality. Helps: Makes explanations coherent while keeping
  procedural or enumerated material easy to scan.
- [`DOCS-PROVE-REAL-USE-WITH-EXAMPLES`](documentation/docs-prove-real-use-with-examples.md). Prove
  real use with examples. Examples that only construct a type or call the happy-path function do not
  prove that the API works in the way users need. Helps: Turns examples into contract evidence and
  prevents shallow examples from hiding missing integration details.
- [`DOCS-PUT-UNCERTAINTY-IN-TRACKED-PLACES`](documentation/docs-put-uncertainty-in-tracked-places.md).
  Put uncertainty in issues, ADRs, or roadmaps rather than burying it in user docs. User docs should
  describe what is true now. Helps: Keeps user docs authoritative while preserving uncertainty in
  places where it can be tracked and resolved.
- [`DOCS-README-AS-ENTRY-POINT`](documentation/docs-readme-as-entry-point.md). Keep README files as
  entry points. A README is usually the first page for humans and agents. Helps: Gives new readers a
  reliable starting path without duplicating every reference detail.
- [`DOCS-SHOW-SIDE-EFFECTS-IN-LIVE-EXAMPLES`](documentation/docs-show-side-effects-in-live-examples.md).
  Show side effects and cleanup in live-resource examples. Examples that create files, hit networks,
  write DNS records, open terminals, spawn tasks, or mutate external services can look harmless
  while leaving persistent state or requiring cleanup. Helps: Reduces unsafe copy-paste behavior and
  makes live-resource examples honest about their effects.
- [`DOCS-STATE-CURRENT-BEHAVIOR-NOT-ASPIRATION`](documentation/docs-state-current-behavior-not-aspiration.md).
  State current behavior, not aspiration. Docs that describe intended behavior as if it already
  exists become false contracts. Helps: Keeps docs trustworthy and prevents roadmaps from
  masquerading as API or behavior guarantees.
- [`DOCS-TREAT-DOCS-AS-CONTRACTS`](documentation/docs-treat-docs-as-contracts.md). Treat docs as
  contracts. Docs increasingly guide both humans and agents. Helps: Aligns code, tests, examples,
  and agent behavior around explicit English-language contracts.
- [`DOCS-USE-CONCRETE-DETAILS`](documentation/docs-use-concrete-details.md). Use concrete nouns and
  real paths, defaults, commands, and examples. Abstract nouns make readers infer the actual object.
  Helps: Makes guidance easier to apply, review, and encode for agents.
- [`DOCS-USE-DESCRIPTIVE-HEADINGS`](documentation/docs-use-descriptive-headings.md). Use headings
  that describe the section content instead of slogan-like instructions. Headings are navigation.
  Helps: Makes pages easier to skim, search, link, and navigate non-linearly.
- [`DOCS-USE-SOURCE-LINKS-AS-SUPPORT`](documentation/docs-use-source-links-as-support.md). Use
  source links as support, not as wording supply. External sources should help a reader verify a
  claim or compare judgment, not supply phrasing. Helps: Keeps guidance original, source-backed
  where useful, and free of accidental paraphrase or citation theater.
- [`DOCS-VERIFY-COMMANDS-PATHS-AND-LINKS`](documentation/docs-verify-commands-paths-and-links.md).
  Verify example commands, file paths, and linked references. Commands, paths, and links are
  executable instructions in disguise. Helps: Keeps docs operationally accurate and reduces repair
  time for readers following examples.
- [`DOCS-WRITE-FOR-NON-LINEAR-READERS`](documentation/docs-write-for-non-linear-readers.md). Write
  docs for non-linear readers. Many readers do not read documentation front to back. Helps: Makes
  sections useful when linked directly and improves agent retrieval quality.
- [`DOCS-WRITE-TECHNICAL-PROSE`](documentation/docs-write-technical-prose.md). Write technical docs,
  not marketing, coaching, or chat. Technical docs should help readers make correct decisions.
  Helps: Keeps documentation direct, actionable, and grounded in behavior rather than persuasion.

### Observability And Failure

- [`OBSERVABILITY-DISTINGUISH-FAILURE-STATES`](observability/observability-distinguish-failure-states.md).
  Distinguish partial, aborted, timed-out, denied, failed, and completed states. A timeout,
  permission denial, user abort, partial write, and provider failure need different recovery paths.
  Helps: Improves retry behavior, user support, and post-failure diagnosis.
- [`OBSERVABILITY-KEEP-DIAGNOSTICS-RETENTION-SAFE`](observability/observability-keep-diagnostics-retention-safe.md).
  Keep diagnostics safe for their retention boundary. Diagnostics that are safe in a local debug log
  may be unsafe in long-lived telemetry, CI artifacts, PR comments, or user-visible error reports.
  Helps: Keeps debugging useful while reducing privacy, compliance, and accidental disclosure risk.
- [`OBSERVABILITY-LOG-AT-OWNED-BOUNDARIES`](observability/observability-log-at-owned-boundaries.md).
  Log at owned boundaries. The best diagnostic point is usually where code still knows the
  operation, caller intent, input class, and external system boundary. Helps: Produces logs that
  identify the responsible operation without duplicating noise at every layer.
- [`OBSERVABILITY-PRESERVE-OPERATION-CONTEXT-IN-ERRORS`](observability/observability-preserve-operation-context-in-errors.md).
  Preserve operation context in errors. An error such as "not found" or "permission denied" is
  rarely enough. Helps: Shortens debugging by carrying the missing operation and resource context
  with the failure.
- [`OBSERVABILITY-SURFACE-DURABLE-FAILURES`](observability/observability-surface-durable-failures.md).
  Do not hide durable failures only in UI logs. A durable failure that only appears in an ephemeral
  UI log can disappear before a maintainer or user can act. Helps: Makes persistent failures visible
  after the immediate UI event is gone.

### Measure Before Optimizing

- [`PERF-AVOID-SINGLE-RUN-CONCLUSIONS`](performance/perf-avoid-single-run-conclusions.md). Do not
  decide performance from one short benchmark run. One short benchmark run can be dominated by
  warmup, scheduling, cache state, background load, or measurement noise. Helps: Keeps performance
  claims reviewable and avoids optimizing noise.
- [`PERF-JUSTIFY-COMPLEXITY-CHURN-AND-DEPENDENCIES`](performance/perf-justify-complexity-churn-and-dependencies.md).
  Justify complexity, churn, and dependency cost in performance wins. Performance changes often buy
  speed by adding branches, unsafe code, caching, data structure churn, or dependencies. Helps:
  Keeps performance improvements proportional to their maintenance and downstream costs.
- [`PERF-MEASURE-GOAL-CHANGE-COMPARE`](performance/perf-measure-goal-change-compare.md). Performance
  changes need goal, measurement, change, and comparison. A performance patch is hard to review
  without knowing the goal, baseline, change, and comparison. Helps: Gives reviewers the evidence
  needed to accept or reject a performance tradeoff.
- [`PERF-OPTIMIZE-MEASURED-HOTSPOTS`](performance/perf-optimize-measured-hotspots.md). Optimize
  measured hotspots, not interesting code. Speeding up code that runs once, is not on the critical
  path, or is not visible to users usually wastes review attention. Helps: Focuses optimization on
  code whose runtime contribution justifies changing its shape.
- [`PERF-RECORD-BENCHMARK-PROVENANCE`](performance/perf-record-benchmark-provenance.md). Record
  benchmark provenance. Benchmark numbers without provenance are hard to compare later. Helps: Makes
  performance evidence repeatable enough for future review and regression analysis.
- [`PERF-RUN-CORRECTNESS-FIRST`](performance/perf-run-correctness-first.md). Run correctness before
  performance timing. Fast wrong code is still wrong, and correctness failures can invalidate timing
  data. Helps: Keeps performance work grounded in behavior preservation before speed claims.
- [`PERF-RUN-TIMING-BENCHMARKS-SEQUENTIALLY`](performance/perf-run-timing-benchmarks-sequentially.md).
  Never run timing benchmarks in parallel when timing data matters. Parallel timing benchmarks
  compete for CPU, cache, memory bandwidth, disk, and thermal headroom. Helps: Produces timing data
  that reviewers can treat as meaningful.

### Local Reasoning And Refactoring

- [`REFACTORING-ALIGN-SEAMS-WITH-REAL-VARIATION`](refactoring/refactoring-align-seams-with-real-variation.md).
  Align seams with real variation, not hypothetical variation. A seam is useful when the code
  actually varies there: different backends, policies, protocols, test doubles, or ownership
  boundaries. Helps: Keeps abstractions tied to observed change pressure and avoids speculative
  indirection.
- [`REFACTORING-DO-NOT-OVER-APPLY-DRY`](refactoring/refactoring-do-not-over-apply-dry.md). Do not
  over-apply DRY. Two blocks that look similar may change for different reasons. Helps: Preserves
  useful duplication until the shared concept and change pattern are real.
- [`REFACTORING-EXTRACT-CONCEPT-HELPERS`](refactoring/refactoring-extract-concept-helpers.md).
  Extract helpers only when they reveal a real concept boundary. A helper should reduce the reader's
  burden by naming a concept, not merely hide three lines. Helps: Improves local reasoning by
  replacing low-level steps with a meaningful name.
- [`REFACTORING-KEEP-LINEAR-STORY-VISIBLE`](refactoring/refactoring-keep-linear-story-visible.md).
  Keep the whole story visible when work is linear. Some logic is easiest to understand as a
  straight narrative: read input, validate, transform, emit result. Helps: Preserves readability
  when the order of operations is the main concept.
- [`REFACTORING-KEEP-WEAK-ABSTRACTIONS-CLOSE-TO-THEIR-USE`](refactoring/refactoring-keep-weak-abstractions-close-to-their-use.md).
  Keep weak abstractions close to their use. New abstractions are often tentative. Helps: Limits
  coupling from premature abstractions and keeps experiments reversible.
- [`REFACTORING-PREFER-LOCAL-REASONING`](refactoring/refactoring-prefer-local-reasoning.md). Prefer
  local reasoning over distant reconstruction. Code is easier to change when the reader can see the
  relevant state, invariants, and effects nearby. Helps: Reduces cognitive load and makes behavior
  changes less error-prone.
- [`REFACTORING-PREFER-LOOPS-FOR-SIDE-EFFECTS`](refactoring/refactoring-prefer-loops-for-side-effects.md).
  Prefer loops over combinators for business-logic side effects. Iterator chains are compact, but
  business-logic side effects often need named steps, early exits, logging, error handling, or
  comments. Helps: Keeps side effects and branch behavior readable in review.
- [`REFACTORING-USE-WHITESPACE-AS-FUNCTION-PARAGRAPHS`](refactoring/refactoring-use-whitespace-as-function-paragraphs.md).
  Use whitespace as function paragraphs. Blank lines can show that a function has phases: gather
  inputs, validate, calculate, perform effects, return. Helps: Improves scanability without
  introducing new names or control flow.

### Private Context And Review Artifacts

- [`REVIEW-DEFINE-SLICES-IN-ISSUES`](review/review-define-slices-in-issues.md). Define review-sized
  slices in issues. Issues are often the first place a future PR gets shaped. Helps: Keeps issues
  actionable, prevents accidental scope creep, and gives agents a clear unit of work.
- [`REVIEW-EXPLAIN-PR-PROBLEM-MODEL-AND-PROOF`](review/review-explain-pr-problem-model-and-proof.md).
  Explain the problem, mental model, tradeoffs, validation, and docs impact in PR descriptions.
  Reviewers should not have to reverse-engineer the intent from the diff. Helps: Reduces reviewer
  guesswork, speeds review, and leaves future maintainers a useful explanation of why the change
  exists.
- [`REVIEW-LABEL-SPECULATION-AS-INFERRED-OR-UNKNOWN`](review/review-label-speculation-as-inferred-or-unknown.md).
  Label speculation as inferred or unknown. Review notes often mix facts, traces, guesses, and
  model-based conclusions. Helps: Makes risk visible, keeps review discussion precise, and helps
  future readers decide what still needs verification.
- [`REVIEW-LET-REVIEWERS-RESOLVE-THREADS`](review/review-let-reviewers-resolve-threads.md). Let
  reviewers resolve review threads unless resolution is unambiguous. Resolving a review thread is a
  communication act, not just a UI cleanup. Helps: Preserves reviewer trust and prevents important
  concerns from disappearing before they are rechecked.
- [`REVIEW-MAKE-REVIEW-ARTIFACTS-STANDALONE`](review/review-make-review-artifacts-standalone.md).
  Make issues, PRs, commit messages, and review handoffs stand alone. Issues, PR descriptions,
  commit messages, and agent handoffs are read by people who did not see the chat, scratch notes,
  local plan, or discarded attempts. Helps: Makes review possible without private context and leaves
  durable reasoning for future debugging, archaeology, and follow-up work.
- [`REVIEW-USE-ADRS-FOR-BOUNDARIES-AND-OWNERSHIP`](review/review-use-adrs-for-boundaries-and-ownership.md).
  Use ADRs for durable boundary and ownership decisions. Some decisions outlive the PR that
  introduces them: module ownership, public API boundaries, storage formats, source-control
  topology, runtime responsibility, and service or crate boundaries. Helps: Preserves architectural
  context, reduces repeated debate, and gives future changes a decision to affirm, revise, or
  replace.

### Rust API And Crate Shape

- [`RUST-ALIGN-RELEASE-SUPPORT-CLAIMS`](rust/rust-align-release-support-claims.md). Keep version,
  changelog, metadata, docs, and support claims aligned. Rust releases have several public truth
  sources: `Cargo.toml`, README, crate Rustdoc, changelog, docs.rs metadata, examples, and CI
  support matrices. Helps: Helps release reviewers compare every public claim before publishing and
  helps downstream users trust the crate docs, package metadata, and changelog as one contract.
- [`RUST-AVOID-BROAD-CONTEXT-AND-CALLBACKS`](rust/rust-avoid-broad-context-and-callbacks.md). Avoid
  broad context objects and callback-heavy control flow. Broad context objects and callback-heavy
  flows hide which inputs, effects, and ordering a function needs. Helps: Helps readers see a
  function's real inputs, outputs, lifetimes, and side effects without tracing a context bag or
  callback chain through distant code.
- [`RUST-AVOID-EMPTY-WRAPPER-TYPES`](rust/rust-avoid-empty-wrapper-types.md). Avoid wrapper types
  that add no invariant, behavior, or ownership clarity. A wrapper type should earn its name by
  adding an invariant, behavior, ownership boundary, or API meaning. Helps: Helps keep the type
  system meaningful by reserving new names for real invariants, ownership boundaries, validation
  rules, or domain concepts.
- [`RUST-AVOID-GIANT-CRATE-ROOTS`](rust/rust-avoid-giant-crate-roots.md). Avoid giant crate roots. A
  giant `lib.rs` or `main.rs` makes the crate root carry every concept, helper, import, and
  re-export. Helps: Helps the crate root teach users the public shape while letting maintainers find
  implementation concepts in focused modules.
- [`RUST-AVOID-INLINE-MODULES`](rust/rust-avoid-inline-modules.md). Avoid inline modules except for
  tests, preludes, and generated code. Inline modules hide file boundaries and make navigation,
  search, and ownership harder in larger Rust crates. Helps: Helps search, review, ownership, and
  navigation by giving each nontrivial module a stable file path.
- [`RUST-AVOID-PUBLIC-DEPENDENCY-COUPLING`](rust/rust-avoid-public-dependency-coupling.md). Avoid
  leaking dependency types in public APIs unless integration is the point. Public APIs that expose
  dependency types force downstream users to care about that dependency version, feature set, and
  semantics. Helps: Helps preserve semver freedom by keeping implementation dependencies from
  becoming downstream compile-time, feature, and version requirements.
- [`RUST-CENTRAL-ITEM-FIRST`](rust/rust-central-item-first.md). Put the central item first and keep
  inherent impls near the type. A Rust module is easier to read when the main type, trait, enum, or
  function appears before helpers. Helps: Helps readers open a module and immediately find the type,
  trait, enum, or function the file exists to define.
- [`RUST-CHOOSE-GENERICS-AND-TRAIT-OBJECTS-DELIBERATELY`](rust/rust-choose-generics-and-trait-objects-deliberately.md).
  Use generics, stored generic parameters, and trait objects deliberately. Generics, stored type
  parameters, and trait objects trade off monomorphization, API complexity, object safety, compile
  times, and caller ergonomics. Helps: Helps APIs expose the right kind of variation without
  surprising callers with compile-time cost, object-safety constraints, allocation, or lifetime
  complexity.
- [`RUST-CONFIGURE-DOCS-RS`](rust/rust-configure-docs-rs.md). Configure docs.rs metadata
  intentionally. docs.rs is often the rendered documentation users see first. Helps: Helps users see
  the same features, cfg-gated items, and documentation warnings that the crate expects to support
  on docs.rs.
- [`RUST-CONSIDER-DOWNSTREAM-API-IMPACT`](rust/rust-consider-downstream-api-impact.md). Consider
  downstream impact before changing public API. Changing a public Rust API can break external
  imports, trait impls, type inference, docs, examples, and semver expectations. Helps: Helps
  library maintainers avoid turning local cleanup into downstream breakage across imports, examples,
  trait impls, type inference, and semver expectations.
- [`RUST-CONTAIN-UNSAFE`](rust/rust-contain-unsafe.md). Keep unsafe small, wrapped, documented, and
  tested through the safe API. Unsafe code concentrates obligations the compiler cannot check.
  Helps: Helps reviewers audit safety invariants locally and lets most tests exercise the unsafe
  behavior through a safe public contract.
- [`RUST-DENY-ACCIDENTAL-UNSAFE`](rust/rust-deny-accidental-unsafe.md). Deny accidental unsafe code
  when the crate does not need unsafe. If a crate does not need unsafe, accidental unsafe blocks
  should fail loudly. Helps: Helps crates that intend to be safe Rust catch accidental unsafe
  introductions during review and CI.
- [`RUST-DO-NOT-DEFAULT-PUB-CRATE`](rust/rust-do-not-default-pub-crate.md). Do not default to
  `pub(crate)`. `pub(crate)` looks safe because it is not public API, but it still expands the
  crate-wide surface and lets modules reach into each other. Helps: Helps keep internal APIs narrow
  so modules can change independently and readers can tell which items are truly shared
  implementation surface.
- [`RUST-DO-NOT-PIN-PATCH-VERSIONS`](rust/rust-do-not-pin-patch-versions.md). Do not pin patch
  versions in `Cargo.toml` unless the patch is required. A patch-pinned dependency requirement in
  `Cargo.toml` raises the minimum version for every downstream resolver even when any compatible
  patch would work. Helps: Helps downstream users keep compatible dependency graphs flexible and
  avoids raising minimum versions just because local lockfiles are newer.
- [`RUST-DOCUMENT-PERFORMANCE-CONTRACTS`](rust/rust-document-performance-contracts.md). Document
  blocking behavior, allocation expectations, and performance constraints. Blocking behavior,
  allocation expectations, buffering, clone cost, and runtime constraints can be part of a Rust API
  contract. Helps: Helps callers understand hidden costs such as allocation, blocking, complexity,
  caching, and large-data behavior before they choose an API.
- [`RUST-DOCUMENT-PUBLIC-PANIC-CONTRACTS`](rust/rust-document-public-panic-contracts.md). Document
  public panic contracts as precondition violations. A public panic is a contract boundary: the
  caller violated a precondition or the crate has a bug. Helps: Helps callers distinguish misuse
  preconditions from ordinary recoverable errors and makes panic behavior testable in public APIs.
- [`RUST-DOCUMENT-SCHEDULING-FOR-LONG-ASYNC`](rust/rust-document-scheduling-for-long-async.md).
  Document scheduling expectations for async code that can run for a long time. Long-running async
  work can starve executors, ignore cancellation, hold locks across await points, or surprise
  callers with runtime assumptions. Helps: Helps async callers reason about executor occupancy,
  cancellation, backpressure, blocking work, and fairness.
- [`RUST-ENCODE-DURABLE-RULES-IN-LINTS`](rust/rust-encode-durable-rules-in-lints.md). Use lint
  configuration only for durable project rules. Lints are useful when they encode durable project
  policy, not transient taste. Helps: Helps CI enforce policies that are stable enough to automate,
  reducing review noise and making agent output easier to validate mechanically.
- [`RUST-GROUP-MODULE-IMPORTS`](rust/rust-group-module-imports.md). Prefer grouped module imports
  over one-import-per-line style. Grouped module imports keep related names together and make
  dependencies easier to scan. Helps: Helps readers see dependency shape by module and reduces churn
  from one-import-per-line edits.
- [`RUST-GROUP-PRIVATE-IMPORTS-BEFORE-PUBLIC-RE-EXPORTS`](rust/rust-group-private-imports-before-public-re-exports.md).
  Group private imports before public re-exports. Private imports and public re-exports answer
  different questions. Helps: Helps separate implementation dependencies from the public discovery
  surface exposed through `pub use`.
- [`RUST-HIDE-TEST-ONLY-HELPERS`](rust/rust-hide-test-only-helpers.md). Keep test-only helpers out
  of the normal public API. Test-only helpers should not become production API or crate-wide
  concepts by accident. Helps: Helps keep normal APIs free of fixtures, shortcuts, and constructors
  that exist only to make tests convenient.
- [`RUST-IMPLEMENT-DEBUG-FOR-PUBLIC-TYPES`](rust/rust-implement-debug-for-public-types.md).
  Implement `Debug` for public types unless that is unsafe or misleading. `Debug` is the baseline
  diagnostic trait for Rust values. Helps: Helps downstream tests, logs, assertions, and diagnostics
  show useful values without bespoke formatting.
- [`RUST-IMPLEMENT-STANDARD-TRAITS-FOR-PUBLIC-ERRORS`](rust/rust-implement-standard-traits-for-public-errors.md).
  Implement `Debug`, `Display`, and `std::error::Error` for reusable public errors. Public errors
  cross boundaries into callers, logs, tests, and user messages. Helps: Helps public errors work
  with `?`, error chains, logs, test output, and common error-reporting libraries.
- [`RUST-KEEP-COMPATIBLE-UPDATES-IN-LOCKFILE`](rust/rust-keep-compatible-updates-in-lockfile.md).
  Keep compatible dependency updates in the lockfile, not the manifest. Compatible dependency
  updates usually belong in the lockfile, not the manifest requirement. Helps: Helps avoid
  unnecessary downstream minimum-version bumps while still letting this checkout test with newer
  compatible releases.
- [`RUST-KEEP-PUBLIC-API-SHAPE-INTENTIONAL`](rust/rust-keep-public-api-shape-intentional.md). Keep
  public API shape intentional. Every public item becomes something users can import, name,
  document, and depend on. Helps: Helps prevent accidental semver commitments through visibility,
  type aliases, features, re-exports, trait bounds, and error variants.
- [`RUST-MAKE-FEATURE-FLAGS-ADDITIVE-WHERE-POSSIBLE`](rust/rust-make-feature-flags-additive-where-possible.md).
  Make feature flags additive where possible. Rust feature unification means enabling a feature in
  one dependency path can affect the whole build. Helps: Helps dependency unification behave
  predictably when multiple downstream crates enable different feature sets.
- [`RUST-NAME-AUDITABLE-INTERMEDIATES`](rust/rust-name-auditable-intermediates.md). Use named locals
  when parsing, rendering, or side effects need auditability. Intermediate variables can make Rust
  code easier to audit when they name ownership, parsing, validation, or policy decisions. Helps:
  Helps reviewers inspect parsing, rendering, validation, and side effects by turning dense
  expressions into named facts.
- [`RUST-NON-EXHAUSTIVE-PUBLIC-ERRORS`](rust/rust-non-exhaustive-public-errors.md). Use
  `#[non_exhaustive]` for public error enums unless exhaustive matching is intentional. Public error
  enums often need new variants as integrations, validation, and provider behavior expand. Helps:
  Helps libraries add future error cases without forcing every downstream match expression to break
  at the next release.
- [`RUST-PREFER-BORING-DIRECT-CODE`](rust/rust-prefer-boring-direct-code.md). Prefer boring direct
  Rust over clever framework-shaped code. Boring Rust makes ownership, error handling, and control
  flow visible. Helps: Helps maintainers and agents reason about ownership, control flow, and errors
  without learning an avoidable framework-shaped abstraction first.
- [`RUST-PREFER-CONCEPT-OWNED-MODULES-AND-NAMED-FILES`](rust/rust-prefer-concept-owned-modules-and-named-files.md).
  Prefer concept-owned modules and named files. Modules should be owned by concepts, not by
  miscellaneous implementation layers. Helps: Helps readers find the code for a domain concept
  without translating through arbitrary layers such as helpers, utils, types, or misc.
- [`RUST-PREFER-CONSTRUCTORS-AND-CONVERSION-TRAITS`](rust/rust-prefer-constructors-and-conversion-traits.md).
  Prefer inherent constructors or trait implementations for construction. Construction should tell
  callers whether they are building a new value, validating input, converting between
  representations, or borrowing a view. Helps: Helps callers discover how values are created and
  whether construction validates, converts, borrows, allocates, or can fail.
- [`RUST-PREFER-EXPECT-FOR-LINT-SUPPRESSIONS`](rust/rust-prefer-expect-for-lint-suppressions.md).
  Prefer `#[expect]` over `#[allow]` when suppression should be revisited. `#[allow]` can silently
  outlive the reason it was added. Helps: Helps suppressions fail when they stop being needed,
  preventing stale `allow` attributes from hiding fixed warnings forever.
- [`RUST-PREFER-SMALL-CLEAR-SHAPES`](rust/rust-prefer-small-clear-shapes.md). Prefer small
  functions, narrow structs, and simple enums. Small functions, narrow structs, and simple enums
  reduce the number of fields, branches, lifetimes, and invariants a reader must hold at once.
  Helps: Helps keep the number of live fields, branches, parameters, and invariants small enough for
  readers to understand locally.
- [`RUST-REEXPORT-FOR-DISCOVERY`](rust/rust-reexport-for-discovery.md). Use re-exports for
  discovery, not ownership hiding. Re-exports help users find the public API from the crate root or
  module facade, but they should not obscure where the concept is owned. Helps: Helps users find the
  intended API from the crate root or module facade while preserving clear implementation ownership.
- [`RUST-TEACH-CRATE-FROM-CRATE-ROOT`](rust/rust-teach-crate-from-crate-root.md). Teach the crate
  from the crate root. The crate root is the first Rustdoc page and often the first source file a
  reader opens. Helps: Helps new users learn the crate purpose, main types, feature flags, and first
  example before they browse module details.
- [`RUST-TIE-OPTIONAL-DEPENDENCIES-TO-NAMED-FEATURES`](rust/rust-tie-optional-dependencies-to-named-features.md).
  Keep optional dependencies tied to clearly named features. Optional dependencies become part of
  the feature contract. Helps: Helps downstream users understand why an optional dependency exists
  and how enabling it changes compile time, platform support, and API surface.
- [`RUST-USE-BUILDERS-FOR-OPTIONAL-OR-VALIDATED-FIELDS`](rust/rust-use-builders-for-optional-or-validated-fields.md).
  Use builders for many optional fields or cross-field validation. Constructors with many optional
  arguments or cross-field validation become hard to call correctly and hard to extend compatibly.
  Helps: Helps APIs avoid long argument lists while giving validation and cross-field defaults a
  named home.
- [`RUST-USE-DIRECTORY-MODULES-AS-TABLES-OF-CONTENTS`](rust/rust-use-directory-modules-as-tables-of-contents.md).
  Use directory-root modules as tables of contents. A directory-root module should orient readers to
  the submodules it owns. Helps: Helps directory modules orient readers to submodules and public
  exports instead of hiding implementation in a large `mod.rs`.
- [`RUST-USE-FUNCTIONS-FOR-INCIDENTAL-TYPES`](rust/rust-use-functions-for-incidental-types.md).
  Prefer regular functions over associated functions when the type name is incidental. Associated
  functions imply the type owns the operation. Helps: Helps callers avoid chasing an irrelevant type
  just to find a stateless operation or one-off transformation.
- [`RUST-USE-HONEST-MINIMUM-DEPENDENCIES`](rust/rust-use-honest-minimum-dependencies.md). Use the
  lowest honest compatible dependency requirement. The manifest should state the lowest compatible
  dependency versions the crate honestly supports. Helps: Helps downstream users with older
  compatible dependency graphs build the crate without unnecessary version pressure.
- [`RUST-USE-MEANINGFUL-STANDARD-TYPES`](rust/rust-use-meaningful-standard-types.md). Use standard
  library types that carry meaning. Standard library types such as `PathBuf`, `NonZeroUsize`,
  `Duration`, `Cow`, `Arc`, and `Result` carry familiar ownership and invariant signals. Helps:
  Helps encode units, ownership, paths, durations, nonzero constraints, borrowing, and optionality
  directly in function signatures.
- [`RUST-USE-SEND-STATIC-ACROSS-TASKS`](rust/rust-use-send-static-across-tasks.md). Use `Send +
  'static` errors, futures, and service handles across tasks or threads. Values crossing task or
  thread boundaries often need `Send + 'static` because the executor may move or retain them beyond
  the caller's stack frame. Helps: Helps spawned tasks and threads avoid borrowing stack-local
  values or non-thread-safe state that cannot outlive the caller.
- [`RUST-VALIDATE-PACKAGE-CONTENTS-BEFORE-RELEASE`](rust/rust-validate-package-contents-before-release.md).
  Validate package contents before release. The crate package is what users receive, not the working
  tree. Helps: Helps catch missing README files, examples, license files, generated assets, and
  accidental inclusions before publishing an immutable crate package.
- [`RUST-VALIDATE-SEMVER-BREAKS-AGAINST-EXTERNAL-USE`](rust/rust-validate-semver-breaks-against-external-use.md).
  Validate semver-breaking changes against real external use. Semver tools can detect many API
  breaks, but real downstream code shows how the public surface is actually used. Helps: Helps
  distinguish theoretical API cleanup from real downstream breakage, especially for library crates
  with examples, tutorials, and external dependents.
- [`RUST-WORKING-RUST-CODE-NOT-ENOUGH`](rust/rust-working-rust-code-not-enough.md). Working Rust
  code is not enough. Rust code can compile while still being hard to read, poorly documented,
  wrongly public, feature-fragile, or painful for downstream users. Helps: Helps review Rust changes
  for API clarity, docs, errors, tests, feature behavior, module shape, and downstream compatibility
  instead of stopping at compilation.
- [`RUST-WRITE-ACTIONABLE-ERROR-DISPLAY`](rust/rust-write-actionable-error-display.md). Write
  human-oriented and actionable error `Display` output. `Display` is often what users, CLIs, logs,
  and support messages show. Helps: Helps users and agents fix failures from the message they
  actually see in CLI output, logs, test diffs, and error reports.

### Source And Context Hygiene

- [`SOURCE-GENERALIZE-PROJECT-SPECIFIC-RULES`](source/source-generalize-project-specific-rules.md).
  Generalize project-specific rules before promotion. Local mining often starts from one repository,
  tool, provider, or incident. Helps: Keeps public guidance broadly reusable while preserving narrow
  lessons for the places where they actually apply.
- [`SOURCE-KEEP-BINARIES-OUT-OF-SOURCE-CONTROL`](source/source-keep-binaries-out-of-source-control.md).
  Keep binary artifacts out of source control. Git history is optimized for source changes, not
  large opaque blobs. Helps: Keeps clones, fetches, CI caches, and history traversal fast; avoids
  history rewrites for accidental large files; keeps review focused on source and provenance; and
  separates release, PR, CI, and long-lived asset lifecycles from source history.
- [`SOURCE-MAKE-SHARED-ARTIFACTS-STANDALONE`](source/source-make-shared-artifacts-standalone.md).
  Make issues, PRs, commit messages, docs, and handoffs stand alone. Shared artifacts often leave
  the development session with missing context. Helps: Makes shared work reviewable, auditable, and
  useful to future readers without local source material.
- [`SOURCE-PREFER-PRIMARY-STABLE-SOURCES`](source/source-prefer-primary-stable-sources.md). Prefer
  primary or stable sources for durable guidance. External references are most useful when they help
  a reader verify, compare, or challenge a rule. Helps: Makes rules easier to audit, easier to
  justify in review, and less dependent on private memory.

### Tests Should Explain Failures

- [`TEST-AVOID-OPAQUE-BOOLEAN-ASSERTIONS`](test-failures/test-avoid-opaque-boolean-assertions.md).
  Avoid boolean assertions for values with multiple failure causes. An assertion like
  `assert!(items.contains(x))` or `assert!(result.is_ok())` can fail for many reasons while showing
  little useful state. Helps: Makes CI and agent failures easier to diagnose from the first failure
  message.
- [`TEST-OPTIMIZE-FAILURE-OUTPUT`](test-failures/test-optimize-failure-output.md). Optimize tests
  for useful failure output. A passing test is useful, but a failing test is where maintainers and
  agents spend repair time. Helps: Shortens repair loops and makes regression failures actionable in
  CI logs.
- [`TEST-SPLIT-UNRELATED-ASSERTIONS`](test-failures/test-split-unrelated-assertions.md). Keep
  unrelated assertions separate when failure diagnosis matters. One test that checks parsing,
  formatting, ordering, error display, and cleanup may stop at the first failure and hide the real
  scope of the regression. Helps: Makes failures local to one behavior and prevents one broken check
  from masking another.

### Testing And Verification

- [`TEST-CHECK-IMPORTANT-FEATURE-COMBINATIONS`](testing/test-check-important-feature-combinations.md).
  Test all features and important feature combinations. Rust feature flags can change public API,
  optional dependencies, cfg-gated docs, and compile paths. Helps: Catches feature-gated regressions
  before downstream users combine features differently than the maintainer did.
- [`TEST-CHECK-MAINTAINER-COMMANDS-IN-CI`](testing/test-check-maintainer-commands-in-ci.md). Check
  the same commands in CI that maintainers are expected to run locally. If the README or maintainer
  guide says to run `cargo test`, `cargo doc`, `markdownlint-cli2`, or a release check, CI should
  exercise the same command or an intentionally stronger equivalent. Helps: Keeps contributor
  instructions honest and prevents maintainers from relying on checks that CI never runs.
- [`TEST-CHECK-MSRV-AND-PLATFORMS`](testing/test-check-msrv-and-platforms.md). Run MSRV and platform
  checks when the crate declares them. MSRV and platform support are public compatibility claims.
  Helps: Keeps support claims aligned with reality and catches accidental platform or toolchain
  regressions.
- [`TEST-CHOOSE-VALIDATION-BY-RISK`](testing/test-choose-validation-by-risk.md). Choose validation
  by risk. Different changes need different proof. Helps: Avoids both under-testing risky work and
  over-testing low-risk edits.
- [`TEST-COVER-ASYNC-ROUTING-EDGE-CASES`](testing/test-cover-async-routing-edge-cases.md). Cover
  unrelated input, late replies, timeouts, and unmatched responses in async routing tests. Async
  routing bugs often appear when replies arrive late, time out, match the wrong request, or include
  unrelated input. Helps: Protects request/response correlation, timeout behavior, and cleanup in
  async systems.
- [`TEST-COVER-LOCAL-LOGIC-WITH-UNIT-TESTS`](testing/test-cover-local-logic-with-unit-tests.md).
  Cover local logic with unit tests. Small pure logic is cheapest to test close to where it lives.
  Helps: Gives fast, precise feedback for local contracts and edge cases.
- [`TEST-COVER-NAVIGATION-BOUNDARIES`](testing/test-cover-navigation-boundaries.md). Cover
  navigation and scroll boundaries in tests. Navigation and scrolling bugs usually happen at the
  edges: empty lists, first item, last item, small viewport, oversized content, saturating offsets,
  and repeated key presses. Helps: Prevents off-by-one and underflow behavior in terminal UI, list,
  cursor, and paging code.
- [`TEST-COVER-POLICY-OUTCOMES`](testing/test-cover-policy-outcomes.md). Cover allowed, denied,
  redacted, and fallback behavior in policy tests. Policy code is most useful at its decision
  boundaries: allowed, denied, redacted, fallback, preserved, and unsupported. Helps: Makes access,
  privacy, compatibility, and fallback behavior explicit and reviewable.
- [`TEST-COVER-PUBLIC-BOUNDARIES-WITH-INTEGRATION-TESTS`](testing/test-cover-public-boundaries-with-integration-tests.md).
  Cover public behavior across module boundaries with integration tests. Public behavior can break
  across module, crate, feature, or adapter boundaries even when unit tests pass. Helps: Catches
  wiring, visibility, feature, and cross-module regressions at the user-facing boundary.
- [`TEST-COVER-PUBLIC-EXAMPLES-WITH-DOCTESTS`](testing/test-cover-public-examples-with-doctests.md).
  Cover public examples with doctests when they can compile without fragile assumptions. Public
  examples teach users and agents how to call the API. Helps: Keeps documentation examples
  executable and aligned with public API shape.
- [`TEST-FUZZ-PARSERS-FORMATTERS-AND-STATE-MACHINES`](testing/test-fuzz-parsers-formatters-and-state-machines.md).
  Use fuzzing or property tests for parsers, formatters, decoders, state machines, and untrusted
  input. Parsers, formatters, decoders, and state machines have large input spaces with edge cases
  humans will not enumerate. Helps: Finds edge cases beyond hand-written examples and protects
  input-facing code from surprising shapes.
- [`TEST-KEEP-DRIFT-CLAIMS-ALIGNED`](testing/test-keep-drift-claims-aligned.md). Keep support
  claims, fixtures, docs, examples, and API paths aligned with drift tests. Support matrices,
  fixtures, docs, examples, and public API paths often drift independently. Helps: Keeps user-facing
  support claims tied to executable evidence.
- [`TEST-KEEP-SLOW-CHECKS-OUT-OF-PR-CI`](testing/test-keep-slow-checks-out-of-pr-ci.md). Keep slow
  fuzzing, long benchmarks, and exhaustive compatibility checks out of required PR CI unless they
  are fast and deterministic. Required PR CI should give fast, reliable feedback. Helps: Keeps
  normal review fast while preserving heavier checks for release or scheduled validation.
- [`TEST-MATCH-EVIDENCE-TO-SURFACE`](testing/test-match-evidence-to-surface.md). Match validation
  evidence to the changed surface. A change to rendered docs, terminal layout, parser output, public
  API, or performance needs evidence from that surface. Helps: Makes validation persuasive because
  the proof matches what changed.
- [`TEST-PREFER-DETERMINISTIC-TESTS`](testing/test-prefer-deterministic-tests.md). Prefer
  deterministic tests over timing or external-state tests. Tests that depend on timing, network
  state, random ordering, real clocks, or external services fail for reasons unrelated to the code
  under review. Helps: Reduces flaky CI and makes failures actionable.
- [`TEST-PROVE-COMMAND-CONSTRUCTION-AND-DISPLAY`](testing/test-prove-command-construction-and-display.md).
  Prove command construction and display behavior in tests. Command-building code can be wrong in
  quoting, argument order, display redaction, environment handling, or platform formatting while
  still invoking a happy path locally. Helps: Prevents shell, display, redaction, and platform bugs
  in command-facing code.
- [`TEST-PROVE-CONTRACTS-NOT-TRIVIA`](testing/test-prove-contracts-not-trivia.md). Prove contracts
  with tests, not implementation trivia. Tests that lock down private helper order, incidental
  formatting, or intermediate variables make refactoring expensive without proving user-visible
  behavior. Helps: Keeps tests useful through refactoring and focused on behavior that matters.
- [`TEST-RUN-DOCS-AS-FIRST-CLASS-GATE`](testing/test-run-docs-as-first-class-gate.md). Run docs as a
  first-class validation job. Docs contain commands, examples, feature claims, public API paths, and
  Rustdoc links. Helps: Keeps documentation, examples, and public API contracts aligned with code.
- [`TEST-RUN-FAST-FORMAT-AND-LINT-GATES-EARLY`](testing/test-run-fast-format-and-lint-gates-early.md).
  Run formatting and clippy early because they fail fast. Formatting and lint failures are cheap to
  find and noisy to review. Helps: Shortens feedback loops and keeps review focused on behavior
  instead of mechanics.
- [`TEST-USE-REALISTIC-PARSER-SAMPLES`](testing/test-use-realistic-parser-samples.md). Use realistic
  samples and safe degradation cases in parser tests. Parser tests built only from idealized
  examples miss real whitespace, ordering, partial data, unknown fields, legacy formats, invalid
  input, and safe degradation behavior. Helps: Catches parsing regressions and documents how
  malformed or unexpected input is handled.
- [`TEST-VALIDATE-DECLARED-MINIMUM-DEPENDENCY-VERSIONS`](testing/test-validate-declared-minimum-dependency-versions.md).
  Validate declared minimum dependency versions. Cargo manifests communicate the minimum compatible
  versions a downstream project may resolve. Helps: Keeps dependency requirements honest and
  protects downstream minimal-version builds.
- [`TEST-WRITE-REGRESSION-TESTS-FOR-BUG-FIXES`](testing/test-write-regression-tests-for-bug-fixes.md).
  Write regression tests for bug fixes unless impractical. A bug fix without a regression test can
  silently revert later, especially when the original failure was an edge case, integration path, or
  user-reported behavior. Helps: Preserves user-reported fixes and gives future maintainers a
  precise failure when the bug returns.

### JJ Topology And Source Control

- [`VCS-ASK-BEFORE-REPAIRING-JJ-ALIASES`](vcs/vcs-ask-before-repairing-jj-aliases.md). Ask the user
  to repair jj aliases when topology and aliases disagree. Aliases such as `trunk()` or publish
  helpers encode assumptions about remotes and bookmarks. Helps: Keeps user-level jj configuration
  deliberate and prevents agents from rewriting source-control policy unexpectedly.
- [`VCS-AVOID-INTERACTIVE-JJ-IN-AGENT-WORK`](vcs/vcs-avoid-interactive-jj-in-agent-work.md). Avoid
  interactive-by-default jj commands in unattended agent work. Interactive jj commands can open
  editors, prompts, merge tools, or pagers that unattended agents cannot handle reliably. Helps:
  Keeps agent source-control operations repeatable and reviewable.
- [`VCS-CONFIGURE-JJ-PAGER`](vcs/vcs-configure-jj-pager.md). Configure `JJ_PAGER` for agent tooling
  when available. Paged output can block or truncate agent command results. Helps: Prevents stuck
  commands and makes source-control evidence visible in handoffs.
- [`VCS-CONFIRM-BROAD-JJ-OPERATIONS`](vcs/vcs-confirm-broad-jj-operations.md). Treat broad jj
  operations as confirmation-worthy. Commands that abandon, rebase, squash, split, restore, publish,
  or affect many revisions can rewrite a large part of the graph. Helps: Reduces accidental history
  reshaping and publication mistakes.
- [`VCS-CONFIRM-GITHUB-REMOTE-TOPOLOGY`](vcs/vcs-confirm-github-remote-topology.md). Confirm GitHub
  `origin` and `upstream` topology before publication. Forks and GitHub defaults can make `origin`
  mean the user fork while `upstream` means the canonical repo, or vice versa in owned repos. Helps:
  Keeps push remote, PR head, PR base, and tracked bookmarks aligned.
- [`VCS-CREATE-OPERATION-LOG-POINT-BEFORE-RESHAPING`](vcs/vcs-create-operation-log-point-before-reshaping.md).
  Use harmless jj inspection to create an operation-log point before risky reshaping. JJ can recover
  through the operation log, but recovery is easier when there is a recent known point before a
  risky stack reshape. Helps: Makes recovery from a bad reshape faster and easier to explain.
- [`VCS-DO-NOT-FALL-BACK-TO-GIT-FOR-JJ-ISSUES`](vcs/vcs-do-not-fall-back-to-git-for-jj-issues.md).
  Do not switch to Git because a jj command hits a transient lock or sandbox issue. In a jj repo,
  Git does not represent the full working-copy and change graph semantics. Helps: Keeps jj as the
  source of truth and avoids mixed-tool corruption or confusion.
- [`VCS-DRY-RUN-SURPRISING-PUBLICATION`](vcs/vcs-dry-run-surprising-publication.md). Use dry-run for
  surprising or ambiguous remote publication, not routine latency. Dry-run is most valuable when
  publication would be surprising: ambiguous remote, new bookmark, force-like update, fork topology,
  or unclear PR base. Helps: Applies extra verification where publication risk is real.
- [`VCS-DUPLICATE-FOR-ALTERNATIVE-CANDIDATES`](vcs/vcs-duplicate-for-alternative-candidates.md). Use
  `jj duplicate` for safe alternative candidates. When comparing two possible fixes or refactor
  shapes, mutating the only candidate makes it hard to return to the original. Helps: Makes
  experiments reversible and keeps competing designs reviewable.
- [`VCS-INSPECT-SPARSE-STATE`](vcs/vcs-inspect-sparse-state.md). Inspect sparse state before
  treating a missing path as missing history. In sparse checkouts, a missing file may be outside the
  sparse patterns rather than deleted from history. Helps: Prevents false conclusions about
  repository contents in sparse workspaces.
- [`VCS-INSPECT-STATE-BEFORE-MUTATING`](vcs/vcs-inspect-state-before-mutating.md). Inspect
  working-copy and stack state before mutating. Before creating, squashing, rebasing, publishing, or
  editing files, the agent needs to know the current working copy, parent, bookmarks, conflicts, and
  unowned changes. Helps: Keeps changes scoped and avoids surprises from hidden graph or
  working-copy state.
- [`VCS-JJ-AS-SOURCE-OF-TRUTH`](vcs/vcs-jj-as-source-of-truth.md). Use `jj` as the source of truth
  in `.jj` repositories. A `.jj` repo has jj changes, operation log, working-copy state, and
  bookmarks layered over Git storage. Helps: Prevents Git commands from bypassing jj semantics and
  confusing the change graph.
- [`VCS-JJ-NEW-FOR-REVIEW-LANES`](vcs/vcs-jj-new-for-review-lanes.md). Use `jj new` for separate
  review lanes. A new task needs a separate review lane before unrelated edits accumulate. Helps:
  Keeps review units atomic and prevents unrelated work from piling into one change.
- [`VCS-MAKE-GITHUB-HANDOFF-EXPLICIT`](vcs/vcs-make-github-handoff-explicit.md). Make GitHub handoff
  explicit after jj state is coherent. JJ state and GitHub state are related but not identical.
  Helps: Makes PR publication reproducible and avoids confusing branch or fork inference.
- [`VCS-MATCH-JJ-TOPOLOGY-TO-REPO-ROLE`](vcs/vcs-match-jj-topology-to-repo-role.md). Match jj remote
  topology to the repository role. Owned repos, maintainer-access repos, and fork-only contributor
  repos need different remote and bookmark topology. Helps: Keeps local jj aliases and publication
  behavior aligned with the actual collaboration model.
- [`VCS-NAME-EXACT-JJ-MUTATION-TARGETS`](vcs/vcs-name-exact-jj-mutation-targets.md). Name exact
  targets for mutating jj commands. Mutating commands that rely on defaults can target the wrong
  revision, fileset, bookmark, or destination when the stack is not what the agent assumes. Helps:
  Reduces accidental rewrites and makes command effects easier to audit.
- [`VCS-QUOTE-REVSETS-AND-SHELL-SYNTAX`](vcs/vcs-quote-revsets-and-shell-syntax.md). Quote revsets
  and shell-sensitive syntax. Revsets and bookmark syntax often contain characters such as `@`, `|`,
  `&`, `~`, parentheses, or spaces that shells can interpret. Helps: Prevents shell parsing bugs in
  jj examples, scripts, and agent commands.
- [`VCS-RECOVER-WITH-OPERATION-LOG`](vcs/vcs-recover-with-operation-log.md). Use operation-log
  recovery instead of destructive cleanup. JJ records repository operations so many mistakes are
  recoverable without destructive Git reset or stash habits. Helps: Makes recovery safer and avoids
  destroying unrelated local work.
- [`VCS-REPAIR-REMOTE-TOPOLOGY-COHERENTLY`](vcs/vcs-repair-remote-topology-coherently.md). Repair
  remote topology coherently. Remote topology has several coupled pieces: fetch remote, push remote,
  tracked bookmark, trunk alias, PR base, and PR head. Helps: Keeps jj, GitHub, and local aliases
  consistent after topology drift.
- [`VCS-RUN-JJ-MUTATIONS-SEQUENTIALLY`](vcs/vcs-run-jj-mutations-sequentially.md). Run jj mutations
  sequentially. JJ mutating commands update working-copy and operation state. Helps: Keeps
  source-control state coherent and avoids avoidable lock contention.
- [`VCS-SCOPE-JJ-FILE-TRACKING`](vcs/vcs-scope-jj-file-tracking.md). Scope jj file track and untrack
  commands to intended paths. `jj file track` and `jj file untrack` can affect more files than
  intended if paths are omitted or globbed too broadly. Helps: Prevents accidental publication or
  removal of local-only and unrelated files.
- [`VCS-STOP-REPEATED-JJ-RETRIES-AND-LOCALIZE-STATE`](vcs/vcs-stop-repeated-jj-retries-and-localize-state.md).
  Stop repeated jj retries and localize state. Repeating a failing jj command without new
  information usually compounds confusion. Helps: Turns source-control failures into diagnosis
  instead of command spam.
- [`VCS-TRACK-REMOTES-EXPLICITLY`](vcs/vcs-track-remotes-explicitly.md). Track remotes explicitly
  when bookmark names exist on multiple remotes. When the same bookmark name exists on multiple
  remotes, implicit tracking can choose the wrong source or make publication ambiguous. Helps:
  Prevents fetch, rebase, and publication confusion in fork and upstream workflows.
- [`VCS-TREAT-BOOKMARK-REMOTE-SYNTAX-AS-VERSION-SENSITIVE`](vcs/vcs-treat-bookmark-remote-syntax-as-version-sensitive.md).
  Treat `bookmark@remote` command syntax as version-sensitive. JJ command syntax around
  `bookmark@remote` and remote bookmark handling can vary by version and command. Helps: Keeps jj
  guidance accurate across version differences and reduces command-shape failures.
- [`VCS-USE-EVOLOG-AND-OPERATION-LOG`](vcs/vcs-use-evolog-and-operation-log.md). Use `jj evolog` for
  one change's evolution and `jj op log` for repository operations. `jj evolog` answers how one
  change evolved; `jj op log` answers how the repository state changed. Helps: Makes diagnosis
  faster by choosing the log that matches the question.
- [`VCS-USE-GIT-FORMATTED-DIFFS-FOR-AGENTS`](vcs/vcs-use-git-formatted-diffs-for-agents.md). Prefer
  Git-formatted diffs when agents need to interpret patch text. Many agents and review tools
  understand Git patch format better than native jj summaries. Helps: Makes diffs easier for agents
  and humans to inspect, quote, and apply.
- [`VCS-USE-IGNORE-WORKING-COPY-CAREFULLY`](vcs/vcs-use-ignore-working-copy-carefully.md). Use
  `--ignore-working-copy` only for lock-safe inspection or intended metadata updates.
  `--ignore-working-copy` can be useful when the working copy is locked or when only metadata is
  needed, but it also means jj may not snapshot current file changes before answering. Helps: Avoids
  stale reads and accidental metadata changes during lock recovery.
- [`VCS-WORKSPACE-ADD-FOR-SECOND-CHECKOUTS`](vcs/vcs-workspace-add-for-second-checkouts.md). Use `jj
  workspace add` only when a second filesystem checkout is needed. `jj new` creates another change
  in the current checkout; `jj workspace add` creates another filesystem checkout. Helps: Avoids
  unnecessary checkout proliferation while preserving isolation when filesystem state matters.
