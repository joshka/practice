# Boundary Correctness

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

Model each integration as the real surface it actually exposes.
Do not pretend a narrow integration has broader semantics than the upstream system supports.
Document and enforce narrow support instead of faking capability.
Prefer conservative support over guessed support.
Reject unsupported shapes early at the adapter boundary.
Return clear errors for unsupported inputs, operations, modes, resource shapes, or protocol shapes.
Choose the resource identity model up front. Whether an API mutates one object, a grouped object,
a session, a file, a handle, or a whole document affects idempotency, matching, update strategy, and
error recovery.
For external state reconciliation, read the current state, normalize it into the local model, compare
desired state to actual state, and mutate by a stable upstream identity when the upstream system does
not provide a safer atomic operation.

When a system has a stable host and reloadable, generated, plugin, or guest behavior, keep
durability, lifecycle, permissions, provider adapters, tool registry ownership, promotion, rollback,
and diagnostics in the stable host. Let reloadable code own behavior, prompts, policy hints,
planning, and declared capabilities behind a narrow contract.

Do not let reloadable code mutate host registries directly. Registrations should be declarative,
host-validated, provenance-carrying, conflict-checked, and revocable.

Use [Make Validation Policy Explicit][validation-policy] when the same field has different rules in
different workflows. Use [Prefer Standard Conversions][standard-conversions] when `FromStr`,
`TryFrom`, `From`, `AsRef`, `Borrow`, or iterator traits honestly express the relationship.

## Lifecycle State

State transitions should name the rule they perform. When a transition changes multiple facts, emits
events, writes persistence, or has invalid predecessor states, the transition deserves an owner.
Scattered functions that collectively encode states, events, guards, and transitions may be an
anemic state machine; name the machine before adding more cases.

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

Ground integration behavior in primary source documentation before relying on wrappers or borrowed
implementations.
Use secondary implementations as cross-checks, not as the authority.
Capture upstream documentation links near the adapter, tests, or repo docs so behavior can be
validated later.
If upstream docs are weak or ambiguous, leave unsupported behavior unsupported and document why.

Keep backend adapters at the edge. Prefer backend-agnostic core types and feature-gated adapters
when integration crates, event backends, terminals, networks, or runtimes vary.

Separate pure computation from rendering, I/O, or mutation when the separation gives tests a stable
surface and callers a clearer contract.

Policy-sensitive side effects should pass through an explicit policy boundary.

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

Provider adapters should normalize streams into typed events with partial and terminal states.
Preserve provider-specific diagnostics, but keep provider wire formats out of durable session state
unless wire compatibility is the contract being tested.

Replay and rollback tests should use fake providers, fake tools, staged artifacts, snapshots, and
golden diagnostics to prove invalid streams, orphaned tool results, failed reloads, and policy
denials fail before promotion.

UI should be a client of events, not the source of truth. A TUI, JSON mode, browser UI, RPC server,
or worker loop should reconstruct state from the same core events without owning durable session
state.

Use [Make Side Effects Visible][side-effects] when a public or internal API reads, writes, retries,
persists, emits, spawns, or calls outside memory. Use [Keep Async Boundaries Explicit][async] when
locks, borrows, owned data, retries, or side effects cross `await` points.

## Related Guidance Layers

Use [Boundary Rules][boundary-rules] for compact instructions about parsing, validation, explicit
inputs, state transitions, side effects, async boundaries, and provider diagnostics. Use
[Explicit Boundaries Preserve Correctness][boundary-principle] for the deeper design reason. Use
[Rust API And Release Checks][api-release] when boundary changes affect public Rust APIs or release
surfaces.

## Review Questions

- Where does raw input become trusted data?
- Does the type or constructor preserve the invariant, or does the caller need to remember it?
- Which validation policy applies, and can the caller see that policy?
- Is this lifecycle change represented as a named transition?
- Is a set of helpers acting like a state machine without an owner?
- Are compaction, reload, retry, abort, and tool execution represented as transitions with safe cut
  points?
- Does the component own the state it stores?
- Would returning a command or value make the state update clearer than hidden mutation?
- Does reloadable or generated code declare capabilities instead of mutating host registries?
- Is pure computation separated from rendering, I/O, or backend adaptation where that helps tests?
- Are ambient inputs visible in the signature or a cohesive context type?
- Are host interactions injectable where tests or policy need control?
- Does a builder validate cross-field invariants before trusted values enter the system?
- Can tests choose time, randomness, IDs, and boundary cases directly?
- Are tool inputs, permissions, execution mode, cancellation, and output limits validated before the
  tool runs?
- What crosses each `await`, and are side effects or cancellation points visible?
- Does the API expose its own errors instead of leaking broad application error aggregation?
- Is the integration modeled as its real upstream surface?
- Which primary source backs the boundary behavior?
- Are unsupported shapes rejected and documented near the adapter?
- Can replay or rollback prove that invalid generated behavior fails before promotion?

[async]: ../patterns/keep-async-boundaries-explicit.md
[api-release]: ../mechanisms/rust-api-and-release-checks.md
[boundary-principle]: ../principles/explicit-boundaries-preserve-correctness.md
[boundary-rules]: ../rules/boundary/README.md
[change]: software-change-preferences.md
[code-shape]: code-shape.md
[cohesion]: ../patterns/strengthen-cohesion.md
[invalid-states]: ../patterns/make-invalid-states-hard-to-express.md
[parameters]: ../patterns/make-parameters-explicit.md
[parse]: ../patterns/parse-dont-validate.md
[rust]: rust-maintainability.md
[side-effects]: ../patterns/make-side-effects-visible.md
[standard-conversions]: ../patterns/prefer-standard-conversions.md
[state-transitions]: ../patterns/make-state-transitions-explicit.md
[time-randomness]: ../patterns/inject-time-and-randomness.md
[validation-policy]: ../patterns/make-validation-policy-explicit.md
