# Full Software Doctrine Prompt Pack

## Metadata

- Name: `Full Software Doctrine Prompt Pack`
- ID: `agent-full-software-doctrine-prompt-pack`
- Summary: `Large single-file prompt pack that combines the repo's software rules and the reasons
  behind them into one coherent artifact. This version is tuned for Rust-heavy maintenance and
  refactoring work, especially when existing code needs to be reshaped toward better locality,
  coherence, ownership, and documentation.`
- Status: `draft`
- Audience: `agents`
- Topics: `agent-workflow, software-doctrine, rust, refactoring, review, validation, architecture`
- Tags: `agent-workflow, agent-context, source-truth, reviewability, documentation, rust`
- Related: `guides/software-change-preferences.md, guides/coding-agents.md,
  guides/rust-maintainability.md, guides/code-shape.md, guides/boundary-correctness.md,
  agent-reviewed-rule-pack, project-operating-manual`

## Usage

Use this snippet when a project wants one large, coherent prompt or `AGENTS.md` section instead of a
short map plus many linked docs. This pack is intentionally large. It is meant for ongoing
maintenance and refactoring work where preserving coherence matters more than token efficiency.

For ordinary agent sessions, prefer `core.md`, `apply-practice-guidance.md`, one task-specific
snippet, and one generated rule domain. Use this pack when a broad audit, refactor, or applied
project doctrine pass needs one coherent context more than low latency.

```markdown
## Software Refactoring Doctrine

This project prefers software that stays understandable under change. The target is not merely
"working code." The target is code that a future maintainer can modify without accidental
breakage, code whose ownership is visible, code whose boundaries match the domain, code whose docs
tell the truth, and code whose review burden stays proportional to the real risk.

This doctrine is especially for fixing or refactoring code that did not start from these values.
When existing code is tangled, broad, weakly named, or poorly documented, the goal is to move it
toward better locality, coherence, explicitness, and proof without inventing unnecessary
architecture.

Treat these instructions as an engineering constitution, not as a line-by-line checklist. Preserve
intent. If following a rule literally would damage correctness, violate local codebase realities,
or miss the actual user goal, stop and resolve the conflict explicitly.

### What "Good" Means Here

Good software in this project has these properties:

- The important concept is easy to find.
- The important rule has a clear owner.
- A maintainer can understand a local change without reconstructing a hidden system.
- Side effects, policy, and state transitions are visible instead of ambient.
- Docs reduce maintenance burden instead of increasing it.
- Tests pin externally meaningful behavior instead of freezing private shape.
- The code gets more coherent as it evolves instead of more generalized and more tangled.

The project values:

- reader locality over abstraction theater
- coherence over category buckets
- explicit boundaries over ambient behavior
- proof over confidence
- reversible structural moves over premature architecture
- maintenance clarity over local cleverness
- one review question at a time over giant omnibus diffs

### How To Use This Doctrine

- Use it to guide refactors, code review, API changes, module moves, docs changes, and test
  strategy.
- Use it to repair code that is currently too broad, too coupled, too weakly named, or too
  scattered to maintain confidently.
- Use it to shape the next change, not to justify rewriting everything nearby.
- Use it to decide where a concept belongs, how much to split, how much to document, and what proof
  is credible.

If a repo has stronger local conventions that already solve the same maintenance problem well,
respect them. This doctrine is strong opinionated guidance, not a demand to churn good local code
into a new visual style.

## Part I: Core Maintenance Worldview

### 1. Reader locality is a primary design constraint

Every file, function, type, and module imposes a working-memory cost on the next maintainer.
Jumps across weak helpers, generic utility modules, broad context objects, hidden side effects,
and mixed responsibilities all raise that cost.

Code should be arranged so that the reader can answer local questions locally:

- What concept does this module own?
- What state changes here?
- What policy is being applied?
- What side effect happens here?
- Which values matter to this branch?
- What contract is this test proving?

Abstractions are good when they let the reader forget details safely. They are bad when they add a
new concept without removing enough burden to justify the jump.

### 2. Coherence matters more than superficial organization

A module, type, or file should own one recognizable idea. That idea may still be large, but the
reader should be able to say why the code belongs together.

Bad organization often looks tidy from a distance:

- a `utils` module that mixes unrelated helpers
- a `models` directory that holds every data type regardless of ownership
- a `helpers` file that becomes a shadow API
- a `common` crate that grows into accidental infrastructure
- a UI module that owns formatting, policy, state transitions, and persistence because "it was
  convenient"

Group by responsibility and change reason, not merely by technical category. If two pieces change
together for the same domain reason, keeping them together is often clearer than prematurely
decoupling them.

### 3. Coupling is a fact to name, not a sin to hide

Coupling is not automatically bad. Some coupling is the domain model. Some coupling is beneficial
because it makes a relationship direct and legible.

Before adding abstraction or decoupling, name the coupling:

- Do these pieces change together because the domain demands it?
- Or because the current shape accidentally braided them?
- Is the coupling visible and honest?
- Or hidden behind a generic boundary that still forces coordinated edits?

Visible beneficial coupling is better than fake decoupling. Hidden accidental coupling is worse
than direct code. Decouple where a real owning boundary can carry the contract.

### 4. Reversible structure is cheaper than speculative architecture

When the right long-term shape is not proven yet, prefer moves that are easy to undo:

- rename a local helper
- split one function into phases
- extract one policy function
- move one concern toward its owner
- narrow one struct
- group one concept into one module

Avoid early moves that create durable contracts too soon:

- new public APIs
- broad framework layers
- generic extension points
- wide cross-crate utility surfaces
- synchronization or cache machinery before evidence
- long-lived protocol or data-shape changes just to test a refactor idea

Learn through reversible tidying before introducing hard-to-reverse boundaries.

### 5. Review cost is a first-class engineering constraint

A good change has:

- one main reason to exist
- one credible proof story
- one understandable risk surface

If a change mixes behavior, module moves, doc rewrites, dependency churn, and naming cleanup, the
reviewer must prove too many things at once. Split the work where review, rollback, or validation
becomes clearer.

## Part II: Default Approach To Legacy Refactoring

### 6. Characterize before changing risky legacy behavior

When code is under-tested, confusing, or known to have quirks, the first job is not cleanup. The
first job is to learn what callers can observe today.

Before changing risky code:

- identify the user-visible or caller-visible behavior
- add or locate a test that pins that behavior
- mark suspicious behavior honestly if you are preserving it only temporarily

Characterization is a safety move. It separates "this behavior already existed" from "this change
introduced new behavior." Without that separation, refactors depend on confidence rather than
evidence.

Do not overfit characterization tests to private helper calls or incidental formatting unless that
detail is truly part of the external contract.

### 7. Use preparatory refactors to create a landing place

If a requested behavior change has no clear home, do not jam it into tangled code and call the
whole diff "the fix." First make the smallest behavior-preserving structural change that gives the
new rule a clear owner.

Examples of legitimate preparation:

- extracting a policy function from rendering
- moving parsing to the edge before changing validation
- isolating state transition code before adding a new transition
- naming the decision that the next rule will modify
- splitting one large function into obvious phases so only one phase changes next

Preparation is not permission for unrelated cleanup. Prepare only the surface that blocks the
current change.

### 8. Untangle before changing when many concerns are braided together

If one rule currently touches formatting, persistence, policy, and control flow all at once, the
code is telling you it lacks a clear owner. Untangle just enough to make the intended change local.

Useful untangling moves:

- separate pure calculation from I/O or rendering
- move domain policy out of display logic
- split state transition rules from ordinary field mutation
- isolate adapter code from domain logic
- split parser normalization from business interpretation

Untangle the knot that blocks the change. Do not widen into a cleanup campaign unless the user
asked for that campaign explicitly.

### 9. Stop when the next move becomes architecture speculation

Legacy cleanup often tempts maintainers to keep going:

- "while we're here, let's add a general trait"
- "while we're here, let's extract a framework"
- "while we're here, let's move it into a shared crate"
- "while we're here, let's support future modes"

That is usually the moment to stop. Refactoring should reduce change cost for the actual next rule,
not create a theory of all future rules.

## Part III: Rust-Specific Structural Doctrine

### 10. Rust code should be reader-first, not feature-first

Rust gives many ways to express ownership, visibility, conversion, indirection, and genericity.
Use the smallest honest Rust shape that keeps the code obvious.

Prefer Rust that is:

- easy to audit locally
- hard to misuse through types and constructors
- explicit about ownership and effects
- modest in visibility
- honest about public contracts
- simple enough that performance reasoning is still possible

Do not use advanced Rust surface area just because it exists. Lifetimes, traits, macros, builders,
async layers, smart pointers, interior mutability, and generic abstractions should each pay rent in
reduced burden or stronger invariants.

### 11. Modules should own one recognizable idea

A Rust module should usually answer one "why does this code change?" question.

Good module boundaries often group:

- one state machine
- one protocol or file format
- one parser or renderer family
- one domain concept
- one adapter to one external system
- one cohesive API surface

Bad module boundaries often group:

- all helpers of a certain syntax kind
- all types regardless of ownership
- all functions that were convenient to paste nearby
- parsing, rendering, and state mutation for unrelated reasons
- crate-wide "internal" helpers with unclear owners

If a module contains parsing, policy, formatting, transport glue, and shared helpers that change
for different reasons, it is probably too broad even if the line count seems moderate.

If a reader has to understand half the file before knowing where a rule lives, the module is too
broad for that concept.

### 12. Size is about cognitive burden, not line count

Do not optimize for arbitrary numeric limits. Instead use these heuristics:

#### A function is probably too large when:

- it has several distinct phases that could be named
- the normal path is hard to see
- many earlier locals stay relevant far below their declaration
- policy, orchestration, and I/O are mixed together
- a reviewer must keep many flags, branches, or invariants in mind at once
- edge cases are buried inside the main path

#### A struct is probably too broad when:

- its fields change for different reasons
- callers frequently use only one subset of fields
- invariants only apply to part of the state
- different methods conceptually operate on different "sub-objects" inside it
- docs need to explain many unrelated responsibilities

#### An enum is probably too broad when:

- variants represent more than one axis of classification
- matching requires many irrelevant fields or cases at most sites
- unrelated transitions or policies are hanging off the same type

#### A module is probably too broad when:

- it is hard to name in one concept sentence
- neighboring items do not help interpret one another
- edits in one part routinely force readers through unrelated concepts
- it acts as a bucket for shared implementation fragments
- tests for one behavior must import half the module’s unrelated apparatus

Small clear shapes are preferred, but do not shatter cohesive logic into tiny fragments that force
the reader to jump more than think.

### 13. Arrange files and modules for reading

Rust source order is part of the interface for maintainers.

Prefer ordering that helps a reader scan top-to-bottom:

- crate purpose before deep implementation
- public or central item before supporting details
- caller before callee when that makes the story easier to follow
- main concept before helpers
- high-level workflow before special cases

The code should feel like technical writing. Readers should not have to bounce around randomly to
understand the outline.

### 14. Crate roots should teach the crate, not contain the crate

`lib.rs` and `main.rs` are orientation pages, not dumping grounds.

Use crate roots to:

- explain the crate purpose
- show the primary path
- expose the main types, traits, or modules
- mention important feature flags
- give a first example
- route readers to deeper modules

Avoid giant crate roots that carry every concept, helper, and implementation detail. If the root
feels like the whole crate, the reader has lost the map.

### 15. Prefer concept-named module files

Prefer file and path names that carry the concept:

- `parser.rs`
- `session.rs`
- `approval_policy.rs`
- `render.rs`
- `frame_decoder.rs`

Named files improve tabs, search results, grep output, diffs, and code review. Avoid `mod.rs` by
default unless local convention, tooling, or established layout makes it genuinely clearer.

For directory modules, use the directory root as a table of contents:

- docs
- `mod` declarations
- high-level re-exports
- orientation

Keep substantial implementation in named child files.

### 16. Start private and widen visibility deliberately

Do not default to `pub(crate)`. Even crate-local visibility expands the internal contract and lets
modules reach into each other casually.

Prefer:

- private first
- `pub(super)` or narrower visibility when the audience is structurally local
- `pub(crate)` only for deliberate shared internals
- `pub` only for intentional public API

Whenever visibility widens, names and docs should make ownership obvious. If a helper must become
more visible but the docs would mostly apologize for that visibility, the better move may be to
reduce the visibility or move the code.

### 17. Keep crate and workspace boundaries narrow

Do not move code into a shared crate simply because it might be reused. Shared crates create:

- dependency fan-out
- feature pressure
- MSRV pressure
- public concept coupling
- harder review for future changes

Keep behavior and tests in the owning crate or module until there is clear evidence of a stable
shared concept.

Broad "core" crates, broad facades, and catch-all internal crates usually create more maintenance
coupling than they remove.

### 18. Re-export intentionally, never to hide confusion

Re-exports should teach the intended entry path, not conceal muddled ownership.

Use re-exports to:

- expose the canonical public path
- keep the crate root usable
- offer a deliberate facade for common workflows

Do not flatten everything into the root. Re-export the primary path and point to deeper modules for
specialized concerns.

## Part IV: How To Choose The Right Module Or Boundary

### 19. Ask "what changes together for one reason?"

When deciding whether code belongs in the same module, same file, same type, or same crate, ask:

- do these pieces change together for one domain reason?
- does understanding one require understanding the other?
- would separating them reduce or increase jumping?
- would a future maintainer naturally look for them together?

If the answer is yes, keep them together unless a stronger boundary exists.

### 20. Ask "what is the owner of this rule?"

Rules should have owners:

- validation belongs near trusted-boundary construction
- state transitions belong near state ownership
- rendering decisions belong in rendering layers unless they are actually domain policy
- adapter quirks belong at adapter boundaries
- public contract shaping belongs where the public API is defined

If a rule is currently split across layers, move it toward the layer that best explains why it
changes.

### 21. Distinguish concept modules from process pipelines

Some modules own concepts. Others own a workflow or pipeline. Both are valid, but they should not
be muddled.

Concept module examples:

- `session`
- `approval_policy`
- `record_id`
- `frame`

Pipeline module examples:

- `parse`
- `render`
- `reconcile`
- `sync`

If a module tries to be both the concept and every pipeline step around it, it often becomes too
broad.

### 22. Choose neighbors that help interpretation

Good neighboring items help the reader interpret each other. Bad neighboring items share only
syntax or convenience.

Good neighbors:

- a type plus its invariants and inherent methods
- a state type plus named transitions
- a parser plus local parsing helpers
- a rendering function plus formatting helpers
- a facade plus the re-exports it intentionally presents

Bad neighbors:

- unrelated helper functions that happened to be reused
- parsing code beside unrelated I/O because both mention strings
- state mutation beside CLI formatting because both touch the same type

### 23. Prefer visible beneficial coupling over weak abstraction

If two pieces truly belong together, keeping them directly connected may be better than hiding them
behind:

- a trait with one implementation
- a generic helper with many type parameters but one caller
- a context object carrying unrelated services
- a utility module with no domain name
- a shared internal API that mainly exists to avoid duplication of one local rule

Weak abstractions add concepts without reducing burden. Keep them local until the variation is real.

## Part V: Local Expression And Function Shape

### 24. Keep the main path visible

The normal successful path should be easy to spot. Avoid making readers drill through bookkeeping,
error checks, and incidental setup before they can see the real work.

Helpful moves:

- guard clauses for preconditions
- named locals for domain facts
- whitespace paragraphs for phases
- policy extracted from rendering or orchestration
- edge cases made explicit instead of buried

### 25. Keep live context small

Live context means the facts a reader still has to remember at a given line.

Reduce it by:

- moving declaration and initialization together
- naming intermediate values that matter semantically
- limiting parameter lists
- separating unrelated responsibilities
- narrowing struct state
- avoiding broad ambient contexts

If a name is introduced far above its real use, or if many earlier flags might still matter to a
later branch, the local shape is carrying too much burden.

### 26. Extract only real concept boundaries

A helper should usually do at least one of these:

- name a domain rule
- isolate a side effect boundary
- isolate a parse/normalize/convert boundary
- expose a stable local policy
- reduce the live context of the caller

Do not extract helpers merely to shorten the file while forcing the reader to chase the same weak
facts somewhere else.

### 27. Prefer explicit parameters over boolean flags and magic context

Boolean flags often hide a choice the caller should name:

- `render(true)` is weak
- `render_compact()` or `render(RenderMode::Compact)` is clearer

Likewise, avoid function behavior that silently depends on:

- global config
- current time
- current directory
- environment variables
- global mutable caches
- implicit runtime state

Make the choice or dependency visible in the interface.

### 28. Use loops when side effects are the point

Iterator chains are great when they express a pure data transformation. They are worse when the
reader must audit:

- ordering
- mutation
- early exits
- error propagation
- logging
- retries
- partial effect behavior

Use ordinary loops when the point is side effects or orchestration clarity.

## Part VI: Boundaries, State, And Side Effects

### 29. Push uncertainty to the boundary

Raw strings, JSON, CLI args, provider responses, file contents, and external records should become
trusted internal types at the edge.

Prefer parse/normalize/construct at the boundary, then pass trusted values inward. Do not keep raw
input circulating through core logic if the parser already learned something useful.

### 30. Make validation policy explicit

Validation is not one thing. Creation, import, migration, repair, display, and reconciliation may
have different rules.

Do not hide policy behind one generic helper if the caller cannot tell which rule applies.

When the same data has multiple workflows, name the workflow or constructor explicitly.

### 31. State transitions deserve names

Creation, loading, activation, cancellation, retry, compaction, promotion, teardown, and migration
are not ordinary field edits. They are lifecycle transitions with invariants.

Do not let callers mutate lifecycle flags directly when what they really mean is "activate this" or
"promote this staged result." Name the transition and let it own the rule.

### 32. Separate pure policy from effects

If rendering, logging, network calls, filesystem writes, or cache mutation hide the rule being
tested, separate the pure decision from the effectful act.

This is one of the most valuable refactoring moves in messy code:

- first expose the rule
- then keep effects as a translation of that rule

### 33. Make side effects visible

APIs should not look pure while:

- writing disk
- mutating global state
- doing network I/O
- spawning tasks
- retrying hidden operations
- caching behind the scenes
- consuming permissions or quotas

Name side effects in function names, docs, and return contracts when they matter to callers.

### 34. Keep async ownership explicit

Across `await` points, be especially careful about:

- borrowed state
- held locks
- cancellation behavior
- retried work
- ownership of spawned tasks
- ordering assumptions

Async code should not hide who owns the lifecycle of work or who is responsible for cleanup.

## Part VII: Documentation As Maintenance Infrastructure

### 35. Docs are part of the maintenance shape

Documentation is not decoration. It is part of how future maintainers recover intent, ownership,
contracts, and limits after session context disappears.

Good docs reduce maintenance burden by answering:

- what this module or type owns
- what it does not own
- what invariants matter
- what the entry point is
- which neighboring modules exist and why
- what behavior is promised
- what behavior is intentionally unsupported

### 36. Write docs to help maintainers place future changes

For maintainability, the most valuable docs are often not broad tutorials. They are compact
ownership docs.

Useful docs include:

- crate root docs that teach the main path
- module docs that state the concept and boundaries
- type docs that explain invariants and caller obligations
- error docs that explain when a failure mode appears
- refactoring or architecture docs that record why the boundary exists

A good maintenance doc helps the next engineer answer "where should the next rule go?"

### 37. Module docs should explain ownership, not repeat signatures

For nontrivial modules, prefer docs that cover:

- the module's concept
- what kinds of code belong here
- what kinds of code do not belong here
- the public or internal entry points
- important invariants or workflow notes
- links to sibling modules when separation is deliberate

Do not fill module docs with prose that merely paraphrases item names.

### 38. Crate docs should teach the main story

Crate-level docs should:

- explain what the crate is for
- show the intended first path
- explain major feature gates if relevant
- mention important modules or extension points
- show the first meaningful example
- set expectations about error model or ownership model when that matters

The crate root should not force users to infer the main workflow from private layout details.

### 39. Documentation should preserve coherence, not fight it

If the code is reorganized around better ownership, update the docs to reinforce that ownership.
If the docs still describe the old mental model, they create maintenance drift.

Docs should:

- use the current concept names
- describe current behavior, not aspiration
- expose non-goals when that prevents misuse
- distinguish stable contracts from local implementation choices

### 40. Rendered surfaces matter

READMEs, Rustdoc, generated docs, CLI help, and examples are all documentation surfaces. Validate
the rendered surface, not just the Markdown source, when the structure changes.

For maintenance coherence, examples should prove real usage and not just that an API can be called.

## Part VIII: Testing And Proof Doctrine

### 41. Test observable behavior first

Tests should prove contracts that matter to users, callers, downstream crates, or future
maintainers. Avoid freezing private helper shape unless the helper boundary itself is the contract.

Good tests answer:

- what behavior does the caller observe?
- what invariant are we protecting?
- what edge case would matter if it changed?

### 42. Use the smallest trustworthy verification

Not every change needs the full project gate, but every change needs honest proof.

Examples:

- formatting/doc wording: lint and focused render check
- visibility/type/API move: build/type checks
- local behavior change: focused unit or integration test
- risky legacy refactor: characterization test plus focused behavior proof
- generated output change: regenerate and inspect the generated surface

### 43. Match proof to the changed surface

If the user receives:

- rendered docs, inspect rendered docs
- CLI output, inspect CLI output
- terminal UI, inspect terminal behavior
- public crate API, test public boundaries
- generated files, inspect generated files
- parser behavior, use realistic input samples

Do not stop at proving only the underlying source if the user-facing surface could still drift.

### 44. Failure output should help diagnosis

Tests should fail in ways that help maintainers understand what broke. Avoid opaque boolean
assertions when more structured evidence would localize the contract violation better.

When a bug fix lands, prefer a regression test that makes the old failure obvious.

## Part IX: Performance, Dependencies, And Public Surfaces

### 45. Measure before optimizing

Do not add complexity, caching, concurrency, allocation tricks, or generic machinery without
evidence that the changed path matters.

Prefer local improvements that preserve reader locality before introducing long-lived complexity.

### 46. Keep dependency impact intentional

Dependency updates and additions are not free. They affect:

- lockfiles
- build graph
- feature graph
- MSRV
- public dependency coupling
- downstream compatibility

Avoid unnecessary dependency churn. Prefer the widest honest semver-compatible requirement that
preserves intended behavior. Use lockfile updates for newer compatible releases rather than
artificially tightening requirements without need.

### 47. Treat public API as downstream cost

Every public item, trait bound, exposed dependency type, error variant story, and behavior promise
creates downstream maintenance cost.

Avoid speculative public API. Keep public surfaces intentional, documented, and visibly owned.

Panics in public APIs should signal violated contracts, not routine fallibility.

## Part X: Review And Handoff

### 48. Review should focus on one main question

A reviewer should be able to ask:

"Did this change accomplish its stated goal without hidden collateral damage?"

If the change cannot be summarized that way, the batch is probably too broad or too mixed.

### 49. Distinguish structure from behavior in review

When possible, separate:

- module moves
- extraction
- rename
- layout cleanup
- visibility cleanup
- doc reorganization

from:

- semantic behavior changes
- new policy
- compatibility changes
- performance changes
- state machine changes

The reviewer should not have to verify preserved behavior and new behavior simultaneously unless the
scope truly demands one inseparable change.

### 50. Handoffs should report proof, not confidence

Good handoff notes include:

- what changed
- why it changed
- where the important files or boundaries are
- which validation ran
- what did not run
- what residual risk remains
- what follow-up is now easier or still required

Avoid long diaries. Durable reasoning belongs in the code, docs, tests, plans, or ADRs.

## Part XI: Concrete Heuristics For Refactoring Existing Rust Code

### 51. When to split a Rust module

Split a module when most of these are true:

- you cannot summarize its concept in one sentence
- the same file mixes parsing, domain policy, state transitions, rendering, and I/O
- understanding one function requires unrelated helper knowledge
- tests for one concern drag in unrelated setup
- names become generic because the file owns too many things
- code review comments repeatedly ask "why is this here?"

Do not split merely because the file is long. Split when the reader burden or ownership confusion
is high.

### 52. When to keep code together

Keep code together when:

- it changes for the same reason
- it is read together to understand one rule
- splitting would create weak helper jumps
- the extracted boundary would be private and conceptually thin
- the value is in seeing the whole linear story at once

Cohesion beats artificial fragmentation.

### 53. How to choose the right related modules

Neighbor modules should usually be related by one of these:

- same concept, different sub-responsibilities
- same protocol, different stable phases
- same domain object, different owned operations
- same public API area, different focused implementation units

Avoid sibling modules that are related only by technical shape, such as "all formatting helpers" or
"all conversions," unless that technical shape is genuinely the concept readers need.

### 54. How to mechanically arrange Rust files

Within a crate:

- keep `lib.rs` or `main.rs` as a teaching and routing surface
- use named module files for concept recognition
- use directory roots as tables of contents
- put the central type or entry point near the top
- keep helpers near the item they support
- order code for top-to-bottom reading
- start private and widen only with clear ownership
- let public API be browseable from the layout

Within a module file:

- put module docs first when needed
- put central public types or entry points early
- put inherent impls near the type
- group related methods by reader task
- keep local helpers near the callers when they are weak abstractions
- use tests to prove the owned behavior of that module

### 55. How to decide whether to extract a type

Extract a new type when it would:

- carry one coherent invariant
- reduce parameter count or repeated field subsets
- express a state transition more clearly
- give a domain rule a natural owner
- reduce misuse through constructors or methods

Do not extract merely to "organize code" if the type would mostly forward calls or carry no real
concept.

### 56. How to decide whether docs belong in code, module docs, or separate docs

Put guidance in:

- code comments when it explains local invariants, safety reasoning, or non-obvious ordering
- type or function docs when callers need contract information
- module docs when ownership or concept boundaries matter
- crate docs when first-path learning matters
- separate docs when the topic spans several modules, captures a durable design decision, or
  explains maintenance workflow

Do not push important ownership or contract information into a chat transcript or PR thread only.

### 57. How to refactor a broad legacy Rust file

Preferred sequence:

1. Identify the visible behavior and current owner confusion.
2. Add or find characterization tests if behavior risk is real.
3. Name the phases inside the file.
4. Separate structure from behavior.
5. Extract the smallest pure policy or ownership boundary.
6. Move code toward the concept that explains why it changes.
7. Re-run focused proof after each meaningful structural step.
8. Update docs to match the new ownership story.
9. Only then make the actual behavior change, if behavior change was the goal.

### 58. How to spot weak abstractions

Be suspicious of abstractions that:

- have one caller and no stable concept
- mostly rename one line
- require reading both sides to understand anything
- hide side effects behind pure-sounding names
- carry broad context objects
- exist only to avoid duplication of a tiny local expression
- introduce type parameters or traits without real variation pressure

Weak abstractions hide context without removing enough burden.

### 59. How to spot hidden main path problems

The main path is hidden when:

- setup and branching bury the ordinary successful case
- bookkeeping dominates the first read
- error handling encloses the real work
- rendering, policy, and orchestration are intertwined
- the core decision has no name

Use guard clauses, phase grouping, extracted policy, or top-to-bottom ordering to make the normal
story visible.

### 60. How to stop refactoring at the right point

Stop when:

- the next intended behavior change has a clear local home
- the changed concept is easier to see
- the test or proof surface is now credible
- docs and names match the new ownership
- further work would mostly be stylistic churn or speculative architecture

The goal is not maximum tidiness. The goal is lower future change cost for the real work.

## Part XII: Default Decision Rules

When uncertain:

- choose clarity over cleverness
- choose visible ownership over vague reuse
- choose a named local rule over a generic helper
- choose reversible structure over public architecture
- choose one coherent concept over category buckets
- choose direct code over a premature layer
- choose proof over confidence
- choose local convention when it already serves maintainability well
- choose the smallest trustworthy refactor that creates a better landing place

If a fact is uncertain, verify it from code, tests, docs, or primary sources.

If a claim cannot be proven, weaken or remove the claim.

If a decision changes architecture, compatibility, security, or long-term ownership, escalate it
instead of guessing inside the diff.

## Expected End State

The desired outcome is not merely "the diff builds" or "the user request was implemented." The
desired outcome is:

- the code is easier to change than before
- the important concept is easier to find
- the important rule has a clearer owner
- the module and type boundaries make more sense
- the docs better support future maintenance
- the proof matches the real risk
- the review burden is controlled
- future maintainers inherit a more coherent system, not just a passing patch

## Part XIII: Rust Module Surgery Playbook

Use this section when the code clearly needs structural repair but the right move is not obvious.
These are default surgeries for common failure modes in Rust maintenance.

### 61. God module surgery

Symptoms:

- one module mixes feature policy, rendering, parsing, I/O, state mutation, and action wiring
- no one can say what the module owns in one sentence
- tests for one behavior pull in several unrelated concepts
- new work keeps landing there because "everything is already in this file"

Preferred sequence:

1. write or find a short ownership note for what the module currently appears to do
2. characterize risky behavior if callers depend on current output or selection behavior
3. mark the major phases or concern clusters inside the file
4. extract one concern at a time to a clearly named owner
5. leave the root as a table of contents or central concept only if that improves reading

Default split candidates:

- feature view behavior
- row interpretation or parsing
- action target resolution
- command-plan execution
- rendered document helpers
- state transition policy

Do not split into many tiny shards at once. The first move should make one future edit obviously
local.

### 62. Broad context struct surgery

Symptoms:

- one struct carries many services, caches, flags, and optional values
- most methods use only a subset of fields
- callers must construct large fake objects in tests
- unrelated invariants are explained in one type

Preferred moves:

- identify coherent field clusters
- extract a narrower type when it owns one real invariant or sub-concept
- pass a specific dependency explicitly instead of the whole context
- move behavior toward the narrower owner before extracting more layers

Avoid turning one broad context into several vague manager types. The replacement should reduce live
facts, not merely relocate them.

### 63. Mixed parser-renderer-policy surgery

Symptoms:

- one function both interprets data and decides what the UI should do
- parsing rules and display rules are intertwined
- the next behavior change would require editing display formatting and domain rules together

Preferred moves:

- separate parsing or row interpretation from display rendering
- separate pure policy from side effects or widget construction
- give the policy a name the tests can point at
- keep the renderer as a translation of already-decided state where practical

This surgery is especially valuable for TUI, CLI, and formatted-text code.

### 64. Accidental shared helper surgery

Symptoms:

- a shared helper module accumulates one-off functions from several features
- helpers carry feature-specific assumptions but live in a "common" location
- changing one feature requires understanding shared helper behavior that no other feature cares
  about

Preferred moves:

- move helpers back to the owning feature if they are not truly shared
- keep only domain-neutral mechanics in shared modules
- rename the shared module to the mechanic it actually owns
- let duplication remain temporarily when it preserves feature locality until real shared pressure
  appears

Shared code should be shared because the concept is shared, not because the lines look similar.

### 65. Visibility sprawl surgery

Symptoms:

- many `pub(crate)` items with unclear audience
- tests and sibling modules reach into each other casually
- ownership boundaries are hard to infer from imports

Preferred moves:

- start from the feature or concept root and ask which items really need to cross that boundary
- narrow visibility first, then repair callers
- convert helper access into owner methods when that reflects the real concept
- document widened visibility when it remains necessary

If an item can only stay visible because the structure is wrong, fix the structure rather than
normalizing the visibility.

### 66. Test bucket surgery

Symptoms:

- large test files cover many unrelated behaviors
- production modules are short, but test support becomes the real complexity sink
- changing one feature requires reading broad test scaffolding first

Preferred moves:

- colocate tests with the module or feature they prove
- keep focused shared test helpers small and purpose-led
- split giant test packets by user-visible behavior, not by arbitrary file size
- prefer view-level or feature-level tests when that reflects the real contract better than helper
  tests

Do not move tests away from behavior merely to equalize file lengths.

### 67. Documentation drift surgery

Symptoms:

- code ownership changed but docs still describe the old shape
- maintainers still rely on PR or chat context to understand why a boundary exists
- crate docs, module docs, and feature docs tell different stories

Preferred moves:

- update crate and module docs immediately after structural ownership changes
- add short ownership comments where future changes need a map
- remove stale wording that implies broader or different behavior than the code supports
- keep docs at the same abstraction level as the boundary they explain

Documentation is part of the repair, not a follow-up luxury.
```
