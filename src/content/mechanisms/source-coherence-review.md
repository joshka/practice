# Source Coherence Review

## Metadata

- Name: `Source Coherence Review`
- ID: `source-coherence-review`
- Summary: Source-coherence review inventories named declarations separately from behavior, maps
  both inventories in both directions, and inspects the declaration outline before implementation
  detail. The pass finds unnamed owners, unjustified abstractions, split facts, misleading modules,
  and line-count concerns that disappear once docs and tests are distinguished from implementation.
- Status: `draft`
- Audience: `both`
- Topics: `rust, refactoring, architecture, review`
- Tags: `rust, reader-locality, reviewability, ownership, module-layout`
- Related: `strengthen-cohesion, name-coupling,
  BOUNDARY-KEEP-ONE-AUTHORITATIVE-OWNER-PER-FACT, RUST-KEEP-CONCEPTS-COHERENT,
  RUST-AVOID-TINY-MODULE-MAZES, RUST-ORDER-CODE-FOR-READING,
  REFACTORING-KEEP-LINEAR-STORY-VISIBLE`

## Purpose

Locally readable code can still present an incoherent source model. A behavior may have no named
owner, one fact may be represented in several places, or a tidy module name may describe no concept
that the implementation actually owns. Reading implementations in file order makes those gaps easy
to normalize because each local step seems reasonable.

Use two independent inventories before proposing structure. One records the names the source asks a
reader to learn. The other records the behavior the system must preserve. Mapping them in both
directions tests whether each behavior has an owner and whether each named abstraction earns its
place.

## Supported Guidance

- [Strengthen Cohesion](../patterns/strengthen-cohesion.md)
- [Name Coupling](../patterns/name-coupling.md)
- [Keep One Authoritative Owner Per Fact](../rules/boundary/boundary-keep-one-authoritative-owner-per-fact.md)
- [Keep Concepts Coherent](../rules/rust/rust-keep-concepts-coherent.md)
- [Avoid Tiny Module Mazes](../rules/rust/rust-avoid-tiny-module-mazes.md)
- [Order Code For Reading](../rules/rust/rust-order-code-for-reading.md)
- [Keep Linear Story Visible](../rules/refactoring/refactoring-keep-linear-story-visible.md)

## Declaration Outline

Scan the source outline before reading every implementation. For Rust, a first pass can use a search
such as:

```bash
rg -n \
  -e '^\s*(pub[^ ]*\s+)?(mod|struct|enum|trait|type|impl|const|static|fn)\b' \
  -e '^\s*(pub[^ ]*\s+)?(async|unsafe|const)\s+fn\b' \
  src
```

Record the modules, types, resources, enums, constants, and important functions. Include private
items that define the module's reading model; omit mechanical helpers once their lack of independent
meaning is clear.

The outline can reveal:

- the central item, or its absence;
- unrelated declaration clusters;
- a filename whose noun has no corresponding model;
- important behavior represented only by free functions or orchestration;
- helpers that belong beside a stronger owner;
- reading order that hides the primary path.

Treat line count as an attention trigger. Check where docs and tests begin and which declarations
occupy the implementation before deciding that a file is broad. Commands such as `wc -l` and a
search for module docs, item docs, and `#[cfg(test)]` boundaries help explain the total. A long file
with one central type, focused documentation, and colocated tests may be coherent; a shorter file can
still mix unrelated policy, rendering, I/O, and state transitions.

## Two Inventories

Build the source-model inventory without inferring that every declaration is justified:

| Named source element | Kind   | Behavior or invariant it claims | Evidence that it owns the claim         |
| -------------------- | ------ | ------------------------------- | --------------------------------------- |
| `JobState`           | enum   | Job lifecycle                   | Transitions reject invalid predecessors |
| `worker_loop`        | module | Runtime orchestration           | Owns ordering, timing, and cancellation |

Build the behavior inventory separately. Include rules, use cases, state transitions, qualities,
constraints, and edge cases even when the source has no name for them:

| Behavior or constraint              | Current owner | Source evidence             | Ownership gap     |
| ----------------------------------- | ------------- | --------------------------- | ----------------- |
| Retry only idempotent requests      | none          | Repeated caller checks      | Rule has no owner |
| Refresh symbol lookup after edits   | `SymbolIndex` | `apply_edit` invalidates it | None              |

Then map both ways:

1. For every behavior, point to the declaration that owns or deliberately coordinates it.
1. For every named source element, point to the behavior, invariant, boundary, or reader burden that
   justifies learning its name.

## Mismatch Signals

Investigate these mismatches rather than treating them as automatic refactor commands:

- Behavior has no named owner.
- One concept is split across several owners that must stay synchronized.
- A name, type, or module has no behavior or boundary that justifies it.
- A type groups fields but protects no invariant and only forwards access.
- A rule exists only in prose, call-site convention, or unrelated orchestration.
- An abstraction adds a name or jump but removes no detail the reader can safely forget.
- A query-looking function consumes input, mutates state, or performs another hidden effect.
- Rendering, adapters, or layout code decide policy owned by the domain concept they project.

A repeated domain noun is a useful naming signal. If reviewers repeatedly need a noun such as
"lease", "movement snapshot", or "retry window" but cannot point to that concept in the source, the
source may be missing an explaining local, function, enum, type, or module. Choose the smallest name
that owns the rule.

The signal is not a command to make a type for every temporary value. Keep a parser or transformation
pipeline linear when its one-off intermediates carry no invariant, reusable policy, lifecycle, or
independent contract. Keep small private helpers beside a strong central owner when the helpers have
no meaning away from it.

## Choosing The Move

Use the mismatch to choose the smallest repair:

- Derive a cheap fact instead of storing it beside its source.
- Move a transition or policy toward the state or concept that explains why it changes.
- Extract a type when related fields protect one invariant through constructors or methods.
- Rename or dissolve a module whose title promises an owner it does not contain.
- Keep an orchestration module when ordering, timing, cancellation, or cross-concept coordination is
  its recognizable behavior. Move domain, input, and rendering policy back out when it becomes a
  horizontal systems bucket.
- Keep direct local variants when a generic abstraction would replace obvious repetition with more
  parameters, modes, and caller-side decoding.
- Keep a cached projection when performance evidence justifies it and one update or invalidation
  boundary keeps it subordinate to the authoritative model.

After the edit, repeat both mappings. The review is complete when important behavior has a definite
owner, every durable name removes reader burden or protects a contract, and the remaining direct code
is easier to understand in place than behind another boundary.

## Agent Consequences

Before a substantial structure review, report the declaration outline, the separate behavior
inventory, and the mismatches found in each mapping direction. Propose types or modules only when
they protect an invariant, own behavior, or remove enough reader burden to justify another name.

## Limits

Macros, generated code, conditional compilation, framework registration, and runtime discovery can
hide declarations from a text outline. Supplement the scan with build output, expanded source, or
runtime inspection when those mechanisms define the real model.

The review exposes ownership hypotheses; tests and behavior evidence still decide whether moving a
rule is safe. Do not turn the inventory into a numerical score, a module-size limit, or a requirement
that every behavior have its own type or file.

## References

- [Rust Reference: Names](https://doc.rust-lang.org/reference/names.html)
- [Ed Page Rust Style: File structure](https://epage.github.io/dev/rust-style/#file-structure)
