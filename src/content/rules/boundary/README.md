# Explicit Boundaries Preserve Correctness

Boundary rules cover parsing, validation policy, explicit inputs, state transitions, provider
diagnostics, effect boundaries, and external reconciliation.

Use this index to scan the domain and jump to the rule files. The one-line summaries are
for orientation; the rule files hold the rationale, limits, mechanisms, and references.

## Rules

- [`BOUNDARY-AVOID-GLOBAL-MUTABLE-STATE`](boundary-avoid-global-mutable-state.md). Keep shared
  process state behind explicit owners, handles, synchronization, and reset policy. This preserves
  test isolation and lifecycle reasoning while still allowing deliberate globals such as caches or
  registries when their contract is visible.
- [`BOUNDARY-CHOOSE-RESOURCE-IDENTITY-MODEL`](boundary-choose-resource-identity-model.md). Decide
  whether the boundary mutates records, sets, files, sessions, handles, or whole documents before
  designing reconciliation. The chosen unit controls idempotency, matching, conflict handling, and
  the cost of later migration.
- [`BOUNDARY-DEFINE-COMPACTION-INVARIANTS`](boundary-define-compaction-invariants.md). State the
  budget and cut-point rules before deleting, summarizing, or moving context. Explicit invariants
  make compaction reviewable and reduce the risk that later work treats lossy or nondeterministic
  summaries as authoritative.
- [`BOUNDARY-DEFINE-HOOK-FAILURE-POLICY`](boundary-define-hook-failure-policy.md). Specify whether
  each hook class blocks, retries, logs and continues, rolls back, or leaves partial state. This
  gives extension points predictable failure behavior without forcing one global answer onto every
  hook.
- [`BOUNDARY-DISTINGUISH-INPUT-CLASSES`](boundary-distinguish-input-classes.md). Keep unknown,
  unsupported, denied, and preserved inputs in separate result or error paths. The distinction
  protects compatibility, authorization messaging, and recovery behavior while allowing small
  internal parsers to stay simpler.
- [`BOUNDARY-EXPOSE-PARTIAL-STREAM-OUTPUT`](boundary-expose-partial-stream-output.md). Surface
  streaming tokens, chunks, or events as provisional output until completion promotes a final
  result. Callers get progress and diagnostics without corrupting authoritative state with partial
  provider data.
- [`BOUNDARY-GIVE-TOOLS-IDENTITY-POLICY-AND-LIMITS`](boundary-give-tools-identity-policy-and-limits.md).
  Give effectful callable units typed identity, authorization policy, cancellation, and bounded
  output. The added ceremony is reserved for real tool boundaries where auditability, recovery, and
  blast-radius control matter.
- [`BOUNDARY-GROUND-INTEGRATIONS-IN-PRIMARY-SOURCES`](boundary-ground-integrations-in-primary-sources.md).
  Base adapter behavior on provider docs, specs, or captured API responses before encoding local
  assumptions. When primary sources are incomplete, label observations and inferences so guesses do
  not become fake guarantees.
- [`BOUNDARY-IDENTIFY-ANEMIC-STATE-MACHINES`](boundary-identify-anemic-state-machines.md). Replace
  scattered booleans and conditionals with named states and transitions when lifecycle behavior is
  already complex. The move exposes illegal transitions and missing recovery paths without
  over-formalizing simple linear code.
- [`BOUNDARY-KEEP-BACKEND-ADAPTERS-AT-EDGE`](boundary-keep-backend-adapters-at-edge.md). Keep
  provider-specific terminal, storage, network, and runtime APIs in adapter layers at the boundary.
  Core logic stays stable and testable while real backend differences remain modeled instead of
  hidden behind a false common API.
- [`BOUNDARY-MAKE-AMBIENT-INPUTS-EXPLICIT`](boundary-make-ambient-inputs-explicit.md). Pass time,
  randomness, environment, locale, terminal size, network clients, and process state through visible
  inputs when they affect behavior. Injecting only the relevant ambient values improves tests and
  portability without spreading oversized context objects.
- [`BOUNDARY-MAKE-DYNAMIC-CONFLICTS-DETERMINISTIC`](boundary-make-dynamic-conflicts-deterministic.md).
  Define stable ordering, duplicate handling, priority, or override policy for dynamic
  registrations. Deterministic conflict behavior prevents hash order or load timing from changing
  which plugin, guest, generated item, or handler wins.
- [`BOUNDARY-MAKE-EXEC-TOOLS-NONINTERACTIVE`](boundary-make-exec-tools-noninteractive.md). Default
  agent, CI, and background exec paths away from prompts, editors, pagers, and credential UI.
  Commands then fail or complete predictably, while human interactive modes remain explicit opt-ins.
- [`BOUNDARY-MAKE-POLICY-BOUNDARIES-EXPLICIT`](boundary-make-policy-boundaries-explicit.md). Route
  writes, network calls, shell execution, publication, telemetry, redaction, and credential use
  through a visible policy decision before effects run. Callers can then understand allowed, denied,
  redacted, fallback, preserved, and unsupported outcomes.
- [`BOUNDARY-MODEL-REAL-UPSTREAM-SURFACE`](boundary-model-real-upstream-surface.md). Shape local
  integration APIs around the provider's actual records, pages, permissions, rate limits, and
  consistency behavior. Wrappers may simplify common paths, but they should not promise capabilities
  the upstream cannot provide.
- [`BOUNDARY-NAME-LIFECYCLE-TRANSITIONS`](boundary-name-lifecycle-transitions.md). Model creation,
  activation, cancellation, teardown, reload, and promotion as named operations when they carry
  different invariants. This keeps ordering, cleanup, retry, and recovery rules visible without
  adding ceremony to simple constructed values.
- [`BOUNDARY-PARSE-UNCERTAINTY-AT-EDGE`](boundary-parse-uncertainty-at-edge.md). Parse and validate
  raw strings, JSON, CLI args, provider responses, and user input at the boundary before passing
  values inward. Core logic receives typed invariants, while domain-specific checks that require
  later context remain explicit policy decisions.
- [`BOUNDARY-READ-NORMALIZE-COMPARE-MUTATE`](boundary-read-normalize-compare-mutate.md). Reconcile
  external state by reading the current provider view, normalizing it, comparing intent, and
  mutating only the real difference. The loop avoids destructive or noisy writes when formatting,
  defaults, ordering, or outside actors create drift.
- [`BOUNDARY-REJECT-UNSUPPORTED-SHAPES`](boundary-reject-unsupported-shapes.md). Fail unsupported
  names, values, TTLs, targets, record families, protocols, or modes at the boundary with clear
  errors. Preserve unknown data only when compatibility requires round-tripping and the system can
  do so safely.
- [`BOUNDARY-REPORT-PROVIDER-DIAGNOSTICS`](boundary-report-provider-diagnostics.md). Return
  freshness, permission, budget, load, cache, partial-result, and degradation signals with
  provider-backed data. These diagnostics help callers decide trust, retry, display, and support
  behavior without exposing unactionable internals.
- [`BOUNDARY-SEPARATE-PURE-CORE-FROM-EFFECTS`](boundary-separate-pure-core-from-effects.md). Move
  domain computation away from rendering, I/O, mutation, and global state when effects obscure the
  decision being tested. The split gives tests a stable surface, but should be skipped when it adds
  indirection without a useful boundary.
- [`BOUNDARY-SEPARATE-UI-AND-APP-STATE`](boundary-separate-ui-and-app-state.md). Keep selection,
  focus, scroll, expansion, and transient input mode separate from application-owned data when they
  change under different rules. The separation prevents rendering concerns from mutating domain
  state while allowing tiny tools to stay simple until friction appears.
- [`BOUNDARY-STAGE-GENERATED-BEHAVIOR`](boundary-stage-generated-behavior.md). Validate generated,
  reloadable, or plugin-provided behavior in a staging path before promoting it over known-good
  behavior. Staging adds recovery cost only where runtime-loaded or generated artifacts can fail
  after deployment.
- [`BOUNDARY-TRACK-DYNAMIC-REGISTRATION-PROVENANCE`](boundary-track-dynamic-registration-provenance.md).
  Store stable source names, versions, paths, owners, or generated identifiers for extension, guest,
  generated-code, and config registrations. Provenance makes conflicts and failures diagnosable
  while avoiding sensitive source details.
- [`BOUNDARY-TREAT-TERMINAL-UI-AS-PRODUCT-SURFACE`](boundary-treat-terminal-ui-as-product-surface.md).
  Treat terminal layout, input, scroll behavior, color, viewport size, and platform differences as a
  user-facing contract when people rely on the interface. This makes regressions reviewable without
  requiring full visual testing for every tiny internal tool.
- [`BOUNDARY-USE-CONSERVATIVE-TERMINAL-DEFAULTS`](boundary-use-conservative-terminal-defaults.md).
  Choose first-run terminal behavior that works with limited color, small viewports, ordinary
  keyboard input, and varied fonts or accessibility settings. Advanced styling can remain opt-in or
  capability-detected after the baseline is readable and usable.
