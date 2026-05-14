# Explicit Boundaries Preserve Correctness

## Metadata

- Name: `Explicit Boundaries Preserve Correctness`
- ID: `explicit-boundaries-preserve-correctness`
- Status: `reviewed`
- Audience: `both`
- Topics: `boundaries, parsing, validation, state, side effects`
- Related: `parse-dont-validate, make-validation-policy-explicit, make-parameters-explicit`

## Claim

Push uncertainty to the boundary, then pass trusted values inward. External input, provider quirks,
ambient dependencies, lifecycle transitions, and side effects should become explicit before they
reach core logic.

## Why I Believe This

Most correctness bugs are cheaper to reason about when the uncertain part is named. Raw strings,
environment variables, provider responses, implicit clocks, global config, and scattered lifecycle
flags make every downstream function ask the same questions again. Once the boundary has parsed,
normalized, rejected, preserved, or named the uncertainty, the rest of the code can work with a
smaller set of facts.

This is especially important for agentic development. Agents can change core logic more safely when
input classes, state transitions, side effects, and provider limits are visible in types, functions,
tests, and docs.

## What This Changes

At boundaries:

- parse raw data into domain values;
- normalize only when normalization is part of the contract;
- reject unsupported modes and shapes with clear errors;
- preserve unknown data only when preservation is intentional;
- pass time, randomness, config, and environment through explicit inputs;
- name lifecycle transitions instead of scattering field mutation;
- keep side effects visible at the workflow owner.

## Rust-Specific Guidance

Prefer `FromStr`, `TryFrom`, constructors, enums, newtypes, and owned error types when they make
boundary policy visible. Use narrow context objects only when they model a cohesive capability.
Avoid broad parameter bags that hide which data is required.

When a set of helpers collectively encodes states, events, guards, and transitions, consider
whether the code is an anemic state machine. Auth flows, UI state, protocol handlers, and lifecycle
code often become clearer when the state owner is named.

## Good Uses

- Parse a user-provided identifier once, then pass an `Id` value inward.
- Reject unsupported provider record shapes at the adapter boundary.
- Represent lifecycle state with an enum and named transition function.
- Inject a clock into code that computes time-sensitive results.
- Keep logging and redaction policy where the workflow owns the context.

## Bad Smells

- Core logic repeatedly checks whether raw input is valid.
- Unknown, unsupported, denied, and preserved inputs collapse into one error.
- A provider adapter silently accepts a shape it cannot round-trip.
- Tests patch environment variables or globals instead of passing inputs.
- State transitions are spread across unrelated helpers and boolean flags.

## Mechanisms

- Typed constructors and parser tests.
- Integration tests that exercise the boundary, not only internals.
- Fuzzing or property tests for parsers, decoders, and state machines.
- Structured errors that preserve input class and source context.
- Docs that state accepted, rejected, normalized, and preserved shapes.

## Rules This Supports

- `BOUNDARY-PUSH-UNCERTAINTY-TO-THE-BOUNDARY-THEN-PASS-TRUSTED-VALUES-INWARD`
- `BOUNDARY-KEEP-UNKNOWN-UNSUPPORTED-DENIED-AND-PRESERVED-INPUTS-DISTINCT`
- `BOUNDARY-REJECT-UNSUPPORTED-SHAPES-EARLY-WITH-CLEAR-ERRORS`
- `BOUNDARY-MAKE-AMBIENT-INPUTS-EXPLICIT`
- `BOUNDARY-TREAT-LIFECYCLE-TRANSITIONS-AS-NAMED-OPERATIONS`
- `BOUNDARY-IDENTIFY-ANEMIC-STATE-MACHINES`

## Agent Consequences

When changing boundary code, name the input class and policy. Do not smear validation throughout
the implementation. Add tests and docs that prove the boundary accepts, rejects, normalizes, or
preserves the intended shapes.

## Limits

Tiny local code can stay direct when invalid states are impossible or harmless. Do not introduce a
formal state machine when a simple enum and one transition function are enough.
