# Explicit Boundaries Preserve Correctness

Boundary rules cover parsing, validation policy, explicit inputs, state transitions, provider
diagnostics, effect boundaries, and external reconciliation.

Use this index to scan the domain and jump to the rule files. The one-line summaries are
for orientation; the rule files hold the rationale, limits, mechanisms, and references.

## Rules

- [`BOUNDARY-AVOID-GLOBAL-MUTABLE-STATE`](boundary-avoid-global-mutable-state.md). Avoid global
  mutable state. Global mutable state hides ownership, ordering, reset, and concurrency
  requirements. Helps: Improves test isolation, explicit lifecycle management, and reasoning about
  shared state.
- [`BOUNDARY-CHOOSE-RESOURCE-IDENTITY-MODEL`](boundary-choose-resource-identity-model.md). Choose
  the resource identity model up front. A system that mutates individual records behaves differently
  from one that mutates record sets, files, sessions, handles, or whole documents. Helps: Prevents
  reconciliation bugs caused by comparing or mutating the wrong unit of state.
- [`BOUNDARY-DEFINE-COMPACTION-INVARIANTS`](boundary-define-compaction-invariants.md). Define
  explicit budget and cut-point invariants for compaction. Compaction deletes, summarizes, or moves
  information. Helps: Makes summarization, pruning, and context-window management testable and
  reviewable.
- [`BOUNDARY-DEFINE-HOOK-FAILURE-POLICY`](boundary-define-hook-failure-policy.md). Define hook
  failure policy. Hooks can fail before, during, or after the main operation. Helps: Makes
  extension, callback, and automation behavior predictable under failure.
- [`BOUNDARY-DISTINGUISH-INPUT-CLASSES`](boundary-distinguish-input-classes.md). Keep unknown,
  unsupported, denied, and preserved inputs distinct. Unknown, unsupported, denied, and preserved
  inputs require different treatment. Helps: Preserves compatibility semantics and gives callers
  actionable errors.
- [`BOUNDARY-EXPOSE-PARTIAL-STREAM-OUTPUT`](boundary-expose-partial-stream-output.md). Expose
  partial provider-stream output without making it authoritative too early. Provider streams often
  deliver partial tokens, chunks, or events before the final authoritative result. Helps: Supports
  progress and diagnostics while keeping final state promotion explicit.
- [`BOUNDARY-GIVE-TOOLS-IDENTITY-POLICY-AND-LIMITS`](boundary-give-tools-identity-policy-and-limits.md).
  Give tool boundaries typed identity, policy, cancellation, and output limits. Tool calls need
  typed identity, authorization policy, cancellation behavior, and output limits because they cross
  from controlled code into filesystem, shell, network, provider, or user-visible effects. Helps:
  Reduces tool blast radius and makes execution, cancellation, and diagnostics predictable.
- [`BOUNDARY-GROUND-INTEGRATIONS-IN-PRIMARY-SOURCES`](boundary-ground-integrations-in-primary-sources.md).
  Ground integration behavior in primary source documentation. Provider and platform behavior
  changes, and memory of an integration is often wrong. Helps: Keeps adapters honest and makes
  integration limits reviewable.
- [`BOUNDARY-IDENTIFY-ANEMIC-STATE-MACHINES`](boundary-identify-anemic-state-machines.md). Identify
  anemic state machines. Auth flows, UI state, async routing, setup wizards, and lifecycle code
  often hide a state machine inside booleans and scattered conditionals. Helps: Makes stateful
  behavior easier to test, extend, and reason about.
- [`BOUNDARY-KEEP-BACKEND-ADAPTERS-AT-EDGE`](boundary-keep-backend-adapters-at-edge.md). Keep
  backend adapters at the edge. Backend-specific APIs for terminals, storage, network providers, or
  runtimes spread quickly if they enter core logic. Helps: Reduces coupling to specific providers
  and makes alternate backends easier to test or add.
- [`BOUNDARY-MAKE-AMBIENT-INPUTS-EXPLICIT`](boundary-make-ambient-inputs-explicit.md). Make ambient
  inputs explicit. Time, randomness, environment variables, current directories, locale, terminal
  size, network clients, and process state can change behavior without appearing in function
  signatures. Helps: Makes nondeterminism injectable and reduces hidden dependencies.
- [`BOUNDARY-MAKE-DYNAMIC-CONFLICTS-DETERMINISTIC`](boundary-make-dynamic-conflicts-deterministic.md).
  Make dynamic registration conflicts deterministic and explicit. Dynamic registration from plugins,
  generated code, guests, or config can produce duplicate names, ordering conflicts, or shadowed
  handlers. Helps: Makes extension systems predictable and diagnosable.
- [`BOUNDARY-MAKE-EXEC-TOOLS-NONINTERACTIVE`](boundary-make-exec-tools-noninteractive.md). Make
  exec-like tools noninteractive by default. Exec-like tools called by agents, CI, or background
  tasks cannot safely wait for prompts, editors, pagers, or credential UI. Helps: Prevents stuck
  jobs and makes tool execution reproducible in automation.
- [`BOUNDARY-MODEL-REAL-UPSTREAM-SURFACE`](boundary-model-real-upstream-surface.md). Model each
  integration as the real upstream surface it exposes. Adapters should not pretend a provider
  supports a cleaner or broader API than it actually does. Helps: Prevents local APIs from promising
  behavior the upstream cannot provide.
- [`BOUNDARY-NAME-LIFECYCLE-TRANSITIONS`](boundary-name-lifecycle-transitions.md). Treat lifecycle
  transitions as named operations. Creation, activation, cancellation, teardown, reload, and
  promotion are different operations with different invariants. Helps: Makes lifecycle behavior
  explicit and keeps invalid ordering visible.
- [`BOUNDARY-PARSE-UNCERTAINTY-AT-EDGE`](boundary-parse-uncertainty-at-edge.md). Push uncertainty to
  the boundary, then pass trusted values inward. Raw strings, JSON, CLI args, provider responses,
  and user input contain uncertainty. Helps: Concentrates validation policy and reduces invalid
  states in core logic.
- [`BOUNDARY-READ-NORMALIZE-COMPARE-MUTATE`](boundary-read-normalize-compare-mutate.md). Reconcile
  external state by reading, normalizing, comparing, and then mutating. External state may be
  formatted differently, reordered, defaulted, or partially managed by another actor. Helps: Makes
  reconciliation idempotent and safer against provider drift.
- [`BOUNDARY-REJECT-UNSUPPORTED-SHAPES`](boundary-reject-unsupported-shapes.md). Reject unsupported
  shapes early with clear errors. Unsupported names, values, TTLs, targets, record families,
  protocols, or config modes should fail at the boundary with a clear error. Helps: Makes
  unsupported behavior explicit and prevents partial internal handling of invalid shapes.
- [`BOUNDARY-REPORT-PROVIDER-DIAGNOSTICS`](boundary-report-provider-diagnostics.md). Report
  freshness, permissions, budget, and load diagnostics from resource providers. When data comes from
  a provider, callers need to know whether it is fresh, partial, permission-limited, rate-limited,
  cached, or degraded. Helps: Helps users and agents interpret provider-backed results safely.
- [`BOUNDARY-SEPARATE-PURE-CORE-FROM-EFFECTS`](boundary-separate-pure-core-from-effects.md).
  Separate pure computation from rendering, I/O, or mutation when that gives tests a stable surface.
  Rendering, filesystem access, network calls, terminal mutation, and global state make behavior
  harder to test. Helps: Improves testability and keeps domain decisions visible without running the
  environment.
- [`BOUNDARY-SEPARATE-UI-AND-APP-STATE`](boundary-separate-ui-and-app-state.md). Keep UI state
  separate from application-owned state. UI state such as selection, scroll offset, focus, expanded
  rows, or transient input mode changes at a different rate than application-owned data. Helps:
  Keeps UI behavior testable and prevents presentation concerns from leaking into core state.
- [`BOUNDARY-STAGE-GENERATED-BEHAVIOR`](boundary-stage-generated-behavior.md). Stage generated or
  reloadable behavior before promotion. Generated, reloadable, or plugin-provided behavior can be
  malformed, stale, or incompatible with the current runtime. Helps: Makes dynamic behavior safer
  and more recoverable.
- [`BOUNDARY-TRACK-DYNAMIC-REGISTRATION-PROVENANCE`](boundary-track-dynamic-registration-provenance.md).
  Track provenance for registrations from extensions, guests, or generated code. When extensions,
  guests, generated code, or config register handlers, commands, routes, or tools, later conflicts
  and failures need to identify where each registration came from. Helps: Makes dynamic systems
  auditable and easier to debug after registration conflicts or failures.
- [`BOUNDARY-TREAT-TERMINAL-UI-AS-PRODUCT-SURFACE`](boundary-treat-terminal-ui-as-product-surface.md).
  Treat terminal UI as a product surface with platform-specific contracts. Terminal UI is not just
  debug output. Helps: Makes terminal behavior reviewable and protects users from layout and
  interaction regressions.
- [`BOUNDARY-USE-CONSERVATIVE-TERMINAL-DEFAULTS`](boundary-use-conservative-terminal-defaults.md).
  Use conservative terminal defaults. Terminals vary in color support, width, input behavior, fonts,
  and accessibility settings. Helps: Improves first-run usability and cross-terminal compatibility.
