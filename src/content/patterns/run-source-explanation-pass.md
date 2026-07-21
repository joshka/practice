# Run Source Explanation Pass

## Metadata

- Name: `Run Source Explanation Pass`
- ID: `run-source-explanation-pass`
- Summary: Turn a source tree into a self-contained reading environment by recovering its mental
  models, fundamentals, decisions, constraints, and edge cases. Establish the system map before item
  detail, audit every relevant helper and path, and measure success through reader comprehension
  rather than comment count.
- Status: `reviewed`
- Audience: `both`
- Topics: `documentation, source-comments, workflow, review`
- Tags: `documentation, reader-locality, source-truth, ai`
- Related: `reconstruct-rationale-before-writing, keep-docs-near-their-subject,
  DOCS-WRITE-FOR-NON-LINEAR-READERS, delete-redundant-comments`

## Problem

Repository-wide comment work can raise comment density without raising understanding. Generated or
hurried passes often restate conditions, skip small helpers, describe a value as tuned without
explaining its effect, or descend into arithmetic before establishing the concept. A reader can see
what each line does and still be unable to predict behavior or change it safely.

Sampling compounds the problem. Small functions, trait implementations, constants, and wrappers can
encode conventions that are obvious only after reading their callers and producers. Newcomers and
agents do not know which small decisions are material, so the audit must establish that rather than
assuming it.

## Reading Contract

Define what readers should be able to learn from the checkout before deciding what to comment. For a
deep source-explanation pass, a new developer or coding agent should be able to understand:

- what the system does and how its major parts cooperate;
- the domain concepts needed to read this implementation;
- each subsystem's purpose, state, lifecycle, and ownership boundaries;
- the rationale behind important representations, policies, ordering, and optimizations;
- the invariants, edge cases, external constraints, and past failures that affect changes; and
- where evidence ends and an explanation remains uncertain.

Treat the source as the canonical home for stable implementation knowledge. A reader should not have
to repeat repository archaeology, search old discussions, or infer a domain model from optimized code
to answer an ordinary maintenance question.

Self-contained does not mean reproducing every specification, paper, or domain textbook. Explain the
concept and the local implementation far enough that the nearby code makes sense, then link to
external material for provenance, formal detail, or optional depth. A familiar name or external link
is not a substitute when the audience may be encountering the domain for the first time.

Name the intended readers and their decisions. A newcomer needs vocabulary and the general model. A
maintainer needs rationale, constraints, failed alternatives, and change hazards. A performance,
security, or reliability specialist needs evidence and the boundaries of measured claims. These
needs overlap, so comments should establish context before offering specialist depth.

## Preferred Move

Define the pass as explanatory coverage, not a target number of comments. State scope, exclusions,
behavior-change constraints, evidence sources, validation, and completion criteria before editing.
For a long pass, keep plans, progress, and research notes outside the published change unless the
process itself is durable project documentation.

Work in reader-sized waves. Small foundational files often provide useful vocabulary and broad
coverage before large central subsystems. Within each area, read the complete file, its owning
module, important producers and consumers, tests, and scoped history before marking it complete.
Track both files completed and a size-weighted measure so many tiny files do not overstate progress.

Build a working knowledge inventory by module and concept. Record unanswered reader questions,
missing mental models and contracts, relevant tests and changes, external constraints, useful
measurements or discussions, and claims that need maintainer confirmation. Organizing the inventory
only by filename can hide a concept that crosses several modules.

For every relevant module, type, item, field, constant, branch, or algorithm phase, ask:

- What role does it play in the larger system?
- How does the operation, state transition, or lifecycle work?
- What does it own, borrow, derive, cache, publish, or mutate?
- Which preconditions, invariants, ordering constraints, and postconditions matter?
- Why does this representation, formula, threshold, ordering, or optimization have this form?
- Which plausible simplifications would change correctness, performance, compatibility, or safety?
- Which edge cases, failure paths, platform differences, or past regressions are hard to infer?
- Which facts are contracts, derived values, empirical choices, conventions, observations, or
  unresolved inferences?

Do not require a comment for every line. Require an answer for every material reader question.

## Establish The System Map First

Document the end-to-end path and the main ownership boundaries before lower-level comments depend on
them. The map should let a reader follow an input, request, event, or data value through the system's
major stages and know which module owns each transition.

Use crate, package, component, or module introductions to establish:

- the system's purpose and primary flow;
- shared vocabulary and domain concepts;
- state ownership and lifecycle;
- relationships between neighboring subsystems;
- important external boundaries; and
- the next source area to read for deeper detail.

Choose the work order by conceptual dependency rather than repository listing. Small foundational
types and modules can establish broad vocabulary early, while large central algorithms often become
easier to explain after their data structures and supporting policies are documented. Explicitly
exclude generated, vendored, or externally owned source instead of silently skipping it.

## Reader Path And Placement

Assume readers arrive non-linearly. Establish the local subject and general concept before explaining
the project's representation or arithmetic. Keep each comment independently useful enough for its
likely entry point, then link to the nearest broader explanation instead of repeating it.

Apply documentation gravity. Put shared mental models on the module or type that owns them. Keep
local contracts, exceptions, edge cases, and operation-specific warnings beside the relevant item or
block. Separate changes of subject, explanatory level, evidence type, and maintainer warning into
paragraphs with blank lines.

Match comment depth to the source boundary:

- Package, crate, and module docs establish purpose, vocabulary, ownership, and subsystem flow.
- Type and item docs explain responsibilities, contracts, distinctions, lifecycle, and invariants.
- Block comments explain algorithm phases, state transitions, and ordering dependencies.
- Inline comments explain a specific expression, bit layout, bound, caveat, or surprising choice.

Significant private items deserve the same reader test as public APIs. Visibility determines who can
call an item, not whether its convention is difficult to reconstruct.

## Depth Checks

Challenge comments that only:

- translate syntax or restate a condition;
- list consumers without explaining the relationship;
- call a choice efficient, tuned, safe, or conventional without evidence or mechanism;
- name a concept without establishing enough context for a first-time reader; or
- report history that does not help explain or change the present system.

For formulas, trace each term's meaning, direction, units, range, clamp, and final conversion. Explain
where each constant comes from: a representation constraint, a calculation from other values,
measurement or tuning, an external specification, or a capacity limit. Calculate the possible signs
and ranges instead of trusting names such as `bonus`, `penalty`, or `weight`.

## Trace Claims Through Behavior

Follow the complete behavior behind a documentation claim instead of naming a local expression and
assuming the surrounding contract:

- Trace every parser, constructor, mutation path, wrapper, trait implementation, and intermediate
  publication before claiming an invariant. State which operation enforces the condition and which
  operations merely inherit it.
- Trace early returns, terminal inputs, feature gates, failures, interruption, and cleanup ownership
  before claiming that an operation always updates state, emits output, or finalizes work.
- Distinguish generated, accepted, considered, skipped, processed, retried, and completed items before
  explaining a counter or threshold. A weighted, decayed, signed, or saturating statistic is not an
  event count unless its updates make it one.
- Distinguish direct mutation from indirect effects through time, scheduling, I/O, shared counters,
  caches, callbacks, or concurrency.
- Separate a cached result from associated metadata, replacement policy, and the hint used to
  prioritize later work. Evidence for one does not automatically prove the others.
- When code uses a simple condition as a stand-in for a broader risk, document the exact condition
  and its counterexamples before describing the risk it approximates.
- Do not call a marker, token, index, or wrapper a proof or capability unless its construction
  establishes the claimed invariant.
- For FFI and platform-specific paths, trace initialized regions, ownership, thread safety, global
  lifecycle, target features, data layout, and which guarantees differ by runtime or architecture.

When a result is ignored but prose claims that the call initializes or mutates state, inspect every
return path. If some paths have no effect, document the actual sequencing or unresolved reason rather
than preserving a historical explanation that no longer matches the callee.

Do not transfer a textbook guarantee to an implementation that skips work, uses approximations, or
accepts stale, partial, or concurrently mixed data. Describe the guarantee over the work and state
the implementation actually observes.

## Safety Claims

For unsafe or low-level code, distinguish the full safety contract from the discipline followed by
current callers. Do not turn an unresolved soundness assumption into a `SAFETY` proof. Consolidate a
shared contract at its stable owner, while keeping additional local obligations at each operation.

## Review Loop

At each wave boundary, run separate sweeps for:

1. context and non-linear readability;
1. rationale depth and evidence scope;
1. branches, producers, returns, and side effects;
1. terminology and current-behavior accuracy;
1. generated-prose tells, repetition, and paragraph structure; and
1. mechanical validation, links, wrapping, and allowed diff scope.

When review finds a systematic error, add it to the checklist and repeat that sweep across every
completed area. A file is complete because it passes the coverage and review gates, not because it
received comments.

For long-running work, report progress without waiting to be asked. Give file count, weighted
coverage, completed subsystem, material findings, open uncertainty, and the next reading area after
small batches and at wave boundaries.

## Completion Proof

Prepare comprehension questions from the reading contract and answer them using only the checkout.
A useful completion audit asks a reader to trace the main system flow, explain subsystem ownership,
follow a nontrivial algorithm, identify important invariants and risky change boundaries, and tell
which claims are measured, specified, conventional, or uncertain.

Also verify that:

- every in-scope first-party module has a useful mental-model introduction;
- important types, fields, helpers, formulas, and representations explain their role and constraints;
- external references supplement explanations rather than replace them;
- exclusions such as generated or vendored code are recorded;
- the diff respects any declared behavior-, API-, layout-, or generated-output constraints;
- a documentation-only pass has not changed executable tokens, configuration, generated artifacts,
  or formatting outside the declared scope; use a language-aware comparison when practical rather
  than relying only on visual diff review;
- documentation builds, links, formatting, examples, and relevant configuration or platform paths
  were checked; and
- unavailable checks are reported as unavailable rather than treated as passing.

Comment totals can demonstrate that an initially sparse source tree changed. Manual comprehension and
correctness review must still establish that the new lines carry knowledge rather than padding.

## Tradeoff

This is intentionally heavier than ordinary API documentation. Use it for undocumented,
performance-sensitive, stateful, unsafe, historically evolved, or domain-heavy systems where future
readers would otherwise reconstruct the design repeatedly. Narrower changes should use a local
contract or coherence pass instead.

Over-documentation can be a reasonable temporary bias when the audience is new to the domain, but
the review still removes prose that adds no reasoning value. Familiarity to an expert is not enough
reason to omit a project-specific convention; obvious syntax is not enough reason to keep a comment.

## Agent Instruction

For a source-explanation pass, audit every relevant item and helper against context, mechanism,
rationale, invariants, edge paths, evidence, and maintainer risk. Work in scoped waves, explain
fundamentals before local representation, track breadth and weighted progress, and repeat any newly
discovered systematic review check across completed areas. Treat the checkout as the stable home for
the recovered explanation, with external sources providing evidence and optional depth. Keep local
plans and research notes out of the published change, report progress proactively, and verify any
documentation-only constraint independently of prose quality.

## References

| Source                                             | Use        | Note                                                           |
| -------------------------------------------------- | ---------- | -------------------------------------------------------------- |
| [Rustdoc: how to write documentation][rustdoc]     | `supports` | Source documentation has item and module ownership boundaries. |
| [Diataxis: reference][reference]                   | `adapts`   | Reference should follow the structure of the machinery.        |
| [Google developer documentation style][google]     | `supports` | Clear, direct prose improves technical source explanations.    |

[google]: https://developers.google.com/style
[reference]: https://diataxis.fr/reference/
[rustdoc]: https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html
