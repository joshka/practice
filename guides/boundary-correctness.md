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

Use [Make Validation Policy Explicit][validation-policy] when the same field has different rules in
different workflows. Use [Prefer Standard Conversions][standard-conversions] when `FromStr`,
`TryFrom`, `From`, `AsRef`, `Borrow`, or iterator traits honestly express the relationship.

## Lifecycle State

State transitions should name the rule they perform. When a transition changes multiple facts, emits
events, writes persistence, or has invalid predecessor states, the transition deserves an owner.
Scattered functions that collectively encode states, events, guards, and transitions may be an
anemic state machine; name the machine before adding more cases.

Use [Make State Transitions Explicit][state-transitions] when callers currently mutate lifecycle
fields directly. Use [Strengthen Cohesion][cohesion] when the state, rule, event, and error should
move toward one concept.

## Explicit Inputs

Hidden inputs make behavior harder to test and review. Environment, configuration, current time,
randomness, global state, and untyped maps should enter at a visible boundary.

Use [Make Parameters Explicit][parameters] when behavior depends on ambient inputs. Use
[Inject Time And Randomness][time-randomness] when deterministic decision logic should receive the
time, generated ID, random choice, or nonce-like value it uses.

## Side Effects And Async

Side effects and suspension points are part of the caller-visible contract when they affect ordering,
failure, cancellation, retries, persistence, observability, or external systems.

Use [Make Side Effects Visible][side-effects] when a public or internal API reads, writes, retries,
persists, emits, spawns, or calls outside memory. Use [Keep Async Boundaries Explicit][async] when
locks, borrows, owned data, retries, or side effects cross `await` points.

## Review Questions

- Where does raw input become trusted data?
- Does the type or constructor preserve the invariant, or does the caller need to remember it?
- Which validation policy applies, and can the caller see that policy?
- Is this lifecycle change represented as a named transition?
- Is a set of helpers acting like a state machine without an owner?
- Are ambient inputs visible in the signature or a cohesive context type?
- Can tests choose time, randomness, IDs, and boundary cases directly?
- What crosses each `await`, and are side effects or cancellation points visible?
- Does the API expose its own errors instead of leaking broad application error aggregation?

[async]: ../patterns/keep-async-boundaries-explicit.md
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
