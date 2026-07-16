# Boundary Correctness

## Metadata

- Name: `Boundary Correctness`
- ID: `boundary-correctness`
- Summary: Boundary-correctness guidance covers APIs and internal boundaries where uncertain input
  becomes trusted data, state changes, ambient inputs enter the system, or async work crosses an
  ownership boundary. It favors visible caller obligations, typed transitions, explicit policy, and
  provider behavior modeled as it really exists.
- Status: `reviewed`
- Audience: `both`
- Topics: `rust, api, validation, state, side-effects, async`
- Tags: `boundary-correctness, validation-policy, state-transitions, side-effects, async`
- Related: `explicit-boundaries-preserve-correctness, parse-dont-validate,
  make-validation-policy-explicit, BOUNDARY-KEEP-ONE-AUTHORITATIVE-OWNER-PER-FACT`

This guide collects preferences for Rust APIs and internal boundaries where uncertain input becomes
trusted data, domain state changes, ambient inputs enter the system, or async work crosses an
ownership boundary. Use it with [Rust Maintainability][rust], [Code Shape][code-shape], and
[Software Change Preferences][change].

Boundary correctness is about making caller obligations visible. A good boundary lets downstream
code rely on types, constructors, function signatures, and named transitions instead of remembering
process rules from surrounding code.

## Core Preference

Prefer APIs that make the correct path natural and the invalid path hard to express. Push uncertainty
to the boundary, then pass trusted values inward.

Use [Make Invalid States Hard To Express][invalid-states] when repeated checks protect the same
invariant. Use [Parse Dont Validate][parse] when validation would otherwise discard what it learned
and leave raw input in circulation.

## Validation And Policy

Validation is not one-size-fits-all. Creation, import, migration, repair, search, and display can
have different rules. Callers should not have to infer which policy a generic helper applies.

### Integration Shape

Model each integration as the real surface it actually exposes. When an upstream system only
supports a narrow shape, document and enforce that narrow support instead of pretending the adapter
has broader semantics. Prefer conservative support over guessed capability, and reject unsupported
inputs, operations, modes, resources, or protocol shapes early at the adapter boundary with clear
errors.

Use [Model Real Upstream Surface][real-upstream] and [Reject Unsupported Shapes][unsupported]
when an adapter is tempted to smooth over provider limits.

### Resource Identity

Choose the resource identity model up front. Whether an API mutates one object, a grouped object,
a session, a file, a handle, or a whole document affects idempotency, matching, update strategy, and
error recovery.
For external state reconciliation, read the current state, normalize it into the local model, compare
desired state to actual state, and mutate by a stable upstream identity when the upstream system does
not provide a safer atomic operation.

Use [Choose Resource Identity Model][resource-identity] before designing reconciliation behavior,
and use [Read Normalize Compare Mutate][read-normalize] when external state updates need
idempotency.

### Dynamic Behavior

When a system has a stable host and reloadable, generated, plugin, or guest behavior, keep
durability, lifecycle, permissions, provider adapters, tool registry ownership, promotion, rollback,
and diagnostics in the stable host. Let reloadable code own behavior, prompts, policy hints,
planning, and declared capabilities behind a narrow contract.

Do not let reloadable code mutate host registries directly. Registrations should be declarative,
host-validated, provenance-carrying, conflict-checked, and revocable.

Use [Stage Generated Behavior][stage-generated], [Track Dynamic Registration
Provenance][registration-provenance], and [Make Dynamic Conflicts Deterministic][dynamic-conflicts]
when generated, plugin, or reloadable behavior crosses into host-owned state.

Use [Make Validation Policy Explicit][validation-policy] when the same field has different rules in
different workflows. Use [Prefer Standard Conversions][standard-conversions] when `FromStr`,
`TryFrom`, `From`, `AsRef`, `Borrow`, or iterator traits honestly express the relationship.

## Lifecycle State

State transitions should name the rule they perform. When a transition changes multiple facts, emits
events, writes persistence, or has invalid predecessor states, the transition deserves an owner.
Scattered functions that collectively encode states, events, guards, and transitions may be an
anemic state machine; name the machine before adding more cases.

Use [Identify Anemic State Machines][anemic-state] when lifecycle facts are scattered across helper
functions, flags, or callbacks.

Give each fact one authoritative owner. Derive cheap state from that source, route runtime mutation
through one owner, and treat UI, adapters, snapshots, and caches as projections rather than
independent authorities. Duplicate a fact only with an explicit refresh, invalidation, staleness, or
reconciliation contract.

Use [Keep One Authoritative Owner Per Fact][authoritative-owner] when a flag, timer, status variant,
cache, adapter, or stored derivative can answer the same question in conflicting ways.

For session-like systems, use an append-only event or entry model with stable IDs, parent links,
schema versions, provenance, explicit active leaves, and visible terminal states. Reject or repair
illegal transitions at the boundary instead of letting later code infer whether a transcript,
stream, or session is valid.

Treat compaction, reload, retry, abort, and tool execution as first-class transitions, not text
cleanup or UI states. Define safe cut points before summarizing, replaying, restoring, or promoting
state. Do not split required call/result pairs, active tool executions, provider streams, pending
reload promotion, or queued user intent across a destructive boundary.

Keep application-owned state separate from rendering state. A widget, parser, adapter, or helper
should not store stale caller-owned geometry, offsets, handles, or configuration when the caller can
pass the current values at the boundary.

Use [Separate UI And App State][ui-state] when rendering state starts owning application state or
stale caller-owned context.

Make state updates visible by returning explicit commands, new values, or transition results when
that is clearer than mutating hidden internal state.

Keep interaction state minimal. Store only the capture, drag, cursor, subscription, or lifecycle
facts the component truly owns.

Use [Make State Transitions Explicit][state-transitions] when callers currently mutate lifecycle
fields directly. Use [Strengthen Cohesion][cohesion] when the state, rule, event, and error should
move toward one concept.

## Explicit Inputs

Hidden inputs make behavior harder to test and review. Environment, configuration, current time,
randomness, global state, and untyped maps should enter at a visible boundary.

Avoid global mutable state. If code touches the filesystem, network, clock, randomness, process
state, platform APIs, or other host resources, make that interaction injectable where tests,
alternate environments, or policy layers need control.

Builders are useful at boundaries when many optional fields, defaults, or cross-field invariants
make a direct constructor hard to read. Keep builder defaults visible, and validate cross-field
rules in `build` instead of letting partially valid values circulate.

Use [Make Parameters Explicit][parameters] when behavior depends on ambient inputs. Use
[Inject Time And Randomness][time-randomness] when deterministic decision logic should receive the
time, generated ID, random choice, or nonce-like value it uses.

## Side Effects And Async

Side effects and suspension points are part of the caller-visible contract when they affect ordering,
failure, cancellation, retries, persistence, observability, or external systems.

### Integration Sources

Ground integration behavior in primary source documentation before relying on wrappers or borrowed
implementations. Secondary implementations are useful cross-checks, but they should not become the
authority for an adapter contract. Keep upstream documentation links near the adapter, tests, or repo
docs so behavior can be validated later; when the upstream docs are weak or ambiguous, leave
unsupported behavior unsupported and document why.

Use [Ground Integrations In Primary Sources][primary-sources] before treating provider behavior as a
contract.

### Adapters And Pure Core

Keep backend adapters at the edge. Prefer backend-agnostic core types and feature-gated adapters
when integration crates, event backends, terminals, networks, or runtimes vary.

Separate pure computation from rendering, I/O, or mutation when the separation gives tests a stable
surface and callers a clearer contract.

Use [Keep Backend Adapters At Edge][backend-edge] and [Separate Pure Core From Effects][pure-core]
when integration details are spreading into core logic.

Policy-sensitive side effects should pass through an explicit policy boundary.

### Tool Execution

Tool boundaries should have stable tool identity, source, schema version, structured input schema,
permission policy, execution mode, timeout behavior, cancellation behavior, and output limits.
Validate paths, encodings, line endings, glob or regex scope, occurrence counts, environment access,
shell metacharacters, and binary/text mode before execution.

Exec-like tools should be noninteractive by default, have explicit working directories and
environment policy, stream output as events, clean up process groups on abort where the platform
allows it, and require approval for full-screen or externally visible behavior.

Denial, redaction, or fallback messages should point to the policy or profile that caused the
decision when that helps callers recover.

Unknown, unsupported, denied, and preserved inputs are different states; model or document the
difference when callers need to reason about compatibility.

Use [Give Tools Identity Policy And Limits][tool-identity], [Make Exec Tools
Noninteractive][exec-tools], and [Distinguish Input Classes][input-classes] when tool calls cross
permission, compatibility, or execution boundaries.

### Provider Streams And Promotion

Provider adapters should normalize streams into typed events with partial and terminal states.
Preserve provider-specific diagnostics, but keep provider wire formats out of durable session state
unless wire compatibility is the contract being tested.

Use [Expose Partial Stream Output][partial-stream] and [Report Provider
Diagnostics][provider-diagnostics] when streams, freshness, permissions, budget, or load affect how
callers should interpret provider output.

Replay and rollback tests should use fake providers, fake tools, staged artifacts, snapshots, and
golden diagnostics to prove invalid streams, orphaned tool results, failed reloads, and policy
denials fail before promotion.

UI should be a client of events, not the source of truth. A TUI, JSON mode, browser UI, RPC server,
or worker loop should reconstruct state from the same core events without owning durable session
state.

Use [Separate UI And App State][ui-state] when presentation layers begin owning durable session
truth.

Use [Make Side Effects Visible][side-effects] when a public or internal API reads, writes, retries,
persists, emits, spawns, or calls outside memory. Use [Keep Async Boundaries Explicit][async] when
locks, borrows, owned data, retries, or side effects cross `await` points. Use [Make Policy
Boundaries Explicit][policy-boundaries] when side effects need allow, deny, redact, fallback, or
approval decisions before execution.

## Related Guidance

Use [Boundary Rules][boundary-rules] for compact instructions about parsing, validation, explicit
inputs, state transitions, side effects, async boundaries, and provider diagnostics. Use
[Explicit Boundaries Preserve Correctness][boundary-principle] for the deeper design reason. Use
[Rust API And Release Checks][api-release] when boundary changes affect public Rust APIs or release
surfaces. Use [Source Coherence Review][source-coherence] when ownership gaps span types or modules.

## Review Questions

### Input And Validation

- Where does raw input become trusted data?
- Does the type or constructor preserve the invariant, or does the caller need to remember it?
- Which validation policy applies, and can the caller see that policy?

### State And Ownership

- Is this lifecycle change represented as a named transition?
- Which representation is authoritative for each fact, and do duplicate views have a visible
  refresh, invalidation, or reconciliation rule?
- Is a set of helpers acting like a state machine without an owner?
- Are compaction, reload, retry, abort, and tool execution represented as transitions with safe cut
  points?
- Does the component own the state it stores?
- Would returning a command or value make the state update clearer than hidden mutation?
- Does reloadable or generated code declare capabilities instead of mutating host registries?

### Effects And Inputs

- Is pure computation separated from rendering, I/O, or backend adaptation where that helps tests?
- Are ambient inputs visible in the signature or a cohesive context type?
- Are host interactions injectable where tests or policy need control?
- Does a builder validate cross-field invariants before trusted values enter the system?
- Can tests choose time, randomness, IDs, and boundary cases directly?
- Are tool inputs, permissions, execution mode, cancellation, and output limits validated before the
  tool runs?
- What crosses each `await`, and are side effects or cancellation points visible?

### Integrations

- Does the API expose its own errors instead of leaking broad application error aggregation?
- Is the integration modeled as its real upstream surface?
- Which primary source backs the boundary behavior?
- Are unsupported shapes rejected and documented near the adapter?
- Can replay or rollback prove that invalid generated behavior fails before promotion?

[async]: ../patterns/keep-async-boundaries-explicit.md
[api-release]: ../mechanisms/rust-api-and-release-checks.md
[anemic-state]: ../rules/boundary/boundary-identify-anemic-state-machines.md
[authoritative-owner]: ../rules/boundary/boundary-keep-one-authoritative-owner-per-fact.md
[backend-edge]: ../rules/boundary/boundary-keep-backend-adapters-at-edge.md
[boundary-principle]: ../principles/explicit-boundaries-preserve-correctness.md
[boundary-rules]: ../rules/boundary/README.md
[change]: software-change-preferences.md
[code-shape]: code-shape.md
[cohesion]: ../patterns/strengthen-cohesion.md
[dynamic-conflicts]: ../rules/boundary/boundary-make-dynamic-conflicts-deterministic.md
[exec-tools]: ../rules/boundary/boundary-make-exec-tools-noninteractive.md
[invalid-states]: ../patterns/make-invalid-states-hard-to-express.md
[input-classes]: ../rules/boundary/boundary-distinguish-input-classes.md
[parameters]: ../patterns/make-parameters-explicit.md
[partial-stream]: ../rules/boundary/boundary-expose-partial-stream-output.md
[policy-boundaries]: ../rules/boundary/boundary-make-policy-boundaries-explicit.md
[parse]: ../patterns/parse-dont-validate.md
[primary-sources]: ../rules/boundary/boundary-ground-integrations-in-primary-sources.md
[provider-diagnostics]: ../rules/boundary/boundary-report-provider-diagnostics.md
[pure-core]: ../rules/boundary/boundary-separate-pure-core-from-effects.md
[read-normalize]: ../rules/boundary/boundary-read-normalize-compare-mutate.md
[real-upstream]: ../rules/boundary/boundary-model-real-upstream-surface.md
[registration-provenance]: ../rules/boundary/boundary-track-dynamic-registration-provenance.md
[resource-identity]: ../rules/boundary/boundary-choose-resource-identity-model.md
[rust]: rust-maintainability.md
[side-effects]: ../patterns/make-side-effects-visible.md
[source-coherence]: ../mechanisms/source-coherence-review.md
[stage-generated]: ../rules/boundary/boundary-stage-generated-behavior.md
[standard-conversions]: ../patterns/prefer-standard-conversions.md
[state-transitions]: ../patterns/make-state-transitions-explicit.md
[time-randomness]: ../patterns/inject-time-and-randomness.md
[tool-identity]: ../rules/boundary/boundary-give-tools-identity-policy-and-limits.md
[ui-state]: ../rules/boundary/boundary-separate-ui-and-app-state.md
[unsupported]: ../rules/boundary/boundary-reject-unsupported-shapes.md
[validation-policy]: ../patterns/make-validation-policy-explicit.md
