# Full Documentation Doctrine Prompt Pack

## Metadata

- Name: `Full Documentation Doctrine Prompt Pack`
- ID: `agent-full-documentation-doctrine-prompt-pack`
- Summary: `Large single-file prompt pack for long-term documentation maintenance. It combines the
  repo's docs rules with writing, review, anti-drift, and anti-AI-slop lessons drawn from this
  repo, TidySrc, jk, and Komodo-style documentation cleanup work.`
- Status: `draft`
- Audience: `agents`
- Topics: `documentation, writing, review, maintenance, ai-assisted-prose, information-architecture`
- Tags: `documentation, agent-context, source-truth, reviewability, ai`
- Related: `guides/markdown-documentation.md, guides/documentation-workflow.md,
  principles/docs-are-contracts.md, agent-markdown-docs-instructions,
  agent-full-software-doctrine-prompt-pack`

## Usage

Use this snippet when a project wants one large, coherent prompt or `AGENTS.md` section focused on
documentation quality, maintenance, and de-AI-ification rather than software refactoring. It is
intentionally large. It is meant for ongoing documentation work where long-term readability,
truthfulness, and drift resistance matter more than token efficiency.

For ordinary agent sessions, prefer `markdown-docs.md`,
`apply-practice-guidance.md`, and the generated documentation rule domain. Use this pack when a
single large context is cheaper than repeated steering across a broad documentation rewrite, audit,
or operating-manual pass.

```markdown
## Documentation Doctrine

This project treats documentation as part of the product and part of the maintenance surface.
The goal is not merely polished prose. The goal is documentation that helps a future reader find the
right concept quickly, understand the system without needless indirection, trust what the page says,
and continue maintaining both the docs and the product without rediscovering intent from scratch.

This doctrine is especially for revising documentation that is currently too smooth, too generic,
too AI-shaped, too padded, too index-like, too self-narrating, or too detached from real product
behavior. The task is not to make docs "sound nicer." The task is to make them more truthful, more
concrete, more locally coherent, and more useful under real reading and maintenance pressure.

Treat these instructions as a documentation constitution, not as a mechanical checklist. Preserve
intent. If a literal reading of one rule would make the page less accurate, less useful, or less
true to the local product, resolve that conflict explicitly instead of forcing the text into a style
template.

### What "Good" Means Here

Good documentation in this project has these properties:

- The page has one dominant job.
- The point appears early.
- The reader can tell what is true now, what is a tradeoff, and what is merely context.
- The prose explains the system, not the page.
- Lists are used because enumeration helps, not because prose got skipped.
- Headings mark real topic clusters rather than one-sentence fragments.
- Examples prove real use instead of decorating the page.
- Links send the reader somewhere useful without becoming navigation chatter.
- The current structure, commands, paths, and contracts match reality.
- The writing preserves local product voice instead of collapsing into generic AI-safe prose.

The project values:

- truth over polish theater
- reader task over template obedience
- concrete detail over abstract smoothing
- prose continuity over bullet spam
- durable guidance over chat memory
- current behavior over aspiration
- anti-drift discipline over post-hoc cleanup
- explainable tradeoffs over recommendation words

### How To Use This Doctrine

- Use it to guide page rewrites, docs cleanup, README work, command reference edits, architecture
  notes, onboarding surfaces, examples, changelog prose, review notes, and `AGENTS.md`-style
  guidance.
- Use it when a repo's docs need de-AI-ification, stronger local voice, or more durable
  maintenance truth.
- Use it to choose page mode, page depth, heading density, example style, and proof expectations.
- Use it to decide what belongs in prose, what belongs in lists, what belongs in a different page,
  and what should not be documented at all.

If a repo already has strong local documentation conventions that solve the same problem well,
respect them. This doctrine is strong opinionated guidance, not permission to rewrite good local
docs into a new accent.

## Part I: Core Documentation Worldview

### 1. Optimize for correct future reading

Readers do not encounter documentation in ideal order. They arrive from search, a command error, a
review comment, a copied link, a support thread, a code comment, or a half-remembered earlier skim.
The documentation should still work when read non-linearly.

Optimize the docs so a reader can answer local questions locally:

- What is this thing?
- Why would I use it?
- What does it change?
- What does it depend on?
- What does it not do?
- What should I read next only if I need more detail?

Do not optimize primarily for:

- sounding comprehensive while staying vague
- sounding helpful while avoiding commitment
- page symmetry for its own sake
- sections that exist only because the template had them
- dense navigation language that explains where to click more than what matters

### 2. Docs are contracts, not atmosphere

English around code, commands, APIs, paths, modes, or workflows is often the first contract a human
maintainer sees. Treat it with the same seriousness as a type, test, or CLI surface.

A doc is broken when it:

- describes planned behavior as current behavior
- keeps old paths or old owners in active guidance
- implies a guarantee the product does not provide
- uses recommendation language without the tradeoff that earns it
- hides a limitation behind vague reassurance
- names a command, config key, or mode without proving where it fits

Fix stale documentation, remove it, or mark the follow-up explicitly. Do not leave attractive
broken contracts in place.

### 3. Every page needs one dominant mode

Before editing, decide the page's main job:

- explanation
- setup
- how-to
- reference
- repo map
- review handoff
- decision record

Keep one dominant mode per page unless a narrow local exception is clearly more useful.

Mode confusion causes many weak docs:

- explanation pages that keep coaching the reader through steps
- reference pages that drift into long historical narrative
- how-to pages that hide the actual steps under architecture exposition
- landing pages that try to teach the entire product instead of routing by task

Choose the job first. Then shape the page for that job.

### 4. Reader task matters more than information architecture purity

The point is not to satisfy a documentation taxonomy. The point is to help the reader succeed.

Some pages are transactional:

- command reference
- field definitions
- flags and config tables
- install steps
- checklists

Some pages are explanatory:

- architecture
- mental model
- workflow shape
- comparison and tradeoff pages
- product model guides

Transactional pages benefit from fast scanning and denser enumeration.
Explanatory pages need prose continuity and clearer conceptual progression.

Do not flatten both into the same style.

### 5. Local voice is part of accuracy

Generic generated prose often sounds acceptable while quietly deleting what made the original docs
useful:

- specific product vocabulary
- the repo's actual level of directness
- the right amount of skepticism
- the way tradeoffs are usually named
- the concrete examples maintainers actually use

Preserve local voice when revising. That does not mean imitating every sentence. It means keeping
the repo's way of explaining reality.

Good local voice usually looks like:

- direct claims instead of motivational framing
- concrete nouns instead of abstract summaries
- real paths, defaults, commands, files, errors, and examples
- explicit product boundaries
- low tolerance for filler and recommendation inflation

## Part II: Writing Shape And Prose Discipline

### 6. Front-load the point

Put the useful point early in the sentence, paragraph, and section.

Readers should not have to wait for the real claim until after:

- throat-clearing
- anticipatory framing
- contrast-template staging
- meta commentary about how to think about the topic
- repetitive scene-setting

Front-loading does not mean shortening every sentence. It means placing the load-bearing claim where
the reader can find it quickly.

### 7. Use prose for relationships and lists for enumeration

Use prose when the reader needs:

- causality
- contrast
- tradeoffs
- ownership explanation
- product model explanation
- boundary explanation
- why a recommendation exists

Use lists when the reader needs:

- steps
- flags
- fields
- options
- signals
- checks
- grouped commands
- short sets of conditions

Do not convert explanation into bullets just because bullets look neat. Bullet-heavy drafts often
hide missing reasoning.

### 8. Keep paragraphs cohesive

Each paragraph should carry one idea, but let that idea develop.

Common failure modes:

- one-sentence paragraphs stacked for rhythm rather than meaning
- every sentence becoming a fresh sub-point
- three adjacent paragraphs restating the same thing at different temperatures
- a paragraph that mixes explanation, caveat, recommendation, navigation, and apology

The fix is usually:

- merge fragments
- split mixed-burden paragraphs
- cut repeated framing
- replace bullet-shaped prose with a real explanatory paragraph

### 9. Use headings to mark content clusters, not micro-points

Good headings help orientation by naming real topic clusters.

Weak heading patterns include:

- `Overview`
- `General`
- `More details`
- `Why this matters` when the section only restates the lead
- several headings in a row with one sentence each

Prefer fewer, denser sections. A heading should earn its scan cost.

### 10. Name the actor and the artifact

Technical prose gets clearer when it names:

- who does the thing
- what command runs
- what file changes
- what path exists
- what service responds
- what output appears

Prefer:

- `discrawl init writes config.toml`
- `the reader machine runs subscribe`
- `the crawler stores guild history in SQLite`

Over:

- `configuration is created`
- `the archive can be initialized`
- `data may be available`

### 11. Avoid recommendation inflation

Do not use words like:

- best
- easiest
- simplest
- fastest
- safest
- usually
- for most users
- recommended

unless the page states the concrete property that earns the claim.

Replace ranking language with the actual tradeoff:

- fewer required inputs
- less manual key management
- fewer moving parts
- narrower failure surface
- direct host access
- better recovery behavior
- no Discord credentials on reader machines

### 12. Cut page narration and teaching-order commentary

Do not narrate the document with lines like:

- this page covers
- use this page when
- the rest of this page
- why this page exists
- first thing to understand
- start with
- next
- later
- once the basic model is in place

unless the page is an actual procedure and that staging is essential.

Explain the system, command, workflow, or contract directly.

### 13. Remove stock AI patterns aggressively

Watch for generated-prose tells such as:

- stock AI verbs and adjectives such as `delve`, `leverage`, `robust`, and `streamline`
- ornate domain nouns such as `landscape`, `ecosystem`, `framework`, and `paradigm`
- contrast templates such as `not X, but Y`, countdown negation, and self-answered questions
- repeated sentence openings, rule-of-three padding, and empty transitions
- shallow `-ing` analysis that attaches importance, legacy, or broader meaning without evidence
- false ranges that list unrelated ideas as if they were a spectrum
- punchy fragments, disguised listicles, mini-intros, and mini-summaries
- false suspense, forced analogies, imagined futures, performative candor, and teacher voice
- claims of obviousness, inflated stakes, vague attribution, and invented concept labels
- repeated dash pivots, bold-first bullets, and decorative Unicode
- repeated summaries, exhausted metaphors, analogy stacks, duplicated sections, and signposted
  endings
- hedged neutrality, comprehensive padding, unsupported precision, apology phrasing, permission
  phrasing, and vague action verbs

When in doubt, cut the sentence and ask whether any meaning was lost. Often none was.

### 14. Prefer concrete details over abstract smoothing

Replace vague terms like:

- powerful
- flexible
- robust
- meaningful
- seamless
- modern
- intuitive
- user-friendly

with concrete specifics:

- command names
- path names
- token sources
- refresh intervals
- sync modes
- permission requirements
- file layout
- visible failure behavior
- actual scope limits

If the concrete detail is unavailable, the page may not be ready to make the claim.

## Part III: Information Architecture And Page Ownership

### 15. Build docs like readers read them

Repository docs need a small reliable map before they need a big tree.

Make the first reading path obvious:

- what this product is
- which path the reader is on
- what matters first
- what can wait
- where command reference starts
- where deeper background lives

Do not make the reader assemble the basic flow from many sibling pages when one clear landing page
could carry it.

### 16. Landing pages are routing surfaces, not essay dumps

A README, docs index, or command map should:

- orient the reader quickly
- help them choose a path
- front-load the product model
- show the most important commands or flows first
- link to deeper pages cleanly

It should not:

- summarize every child page at equal depth
- narrate the site structure more than the product
- become a giant prose slab that duplicates the whole docs tree

### 17. Active guidance and history are different layers

This matters for both code docs and docs-process docs.

Active guidance should describe:

- the current structure
- current owners
- current paths
- current workflow
- current command shape
- current validation expectations

Historical material may preserve:

- old paths
- packet logs
- migration notes
- prior ownership
- earlier cleanup reasoning

Do not let active docs drift because a historical artifact still exists.

### 18. Keep maintainer context behind the first reading path

User docs should not open with internal process, generation notes, or repo mechanics unless the
page is itself maintainer-facing.

Hide:

- source layout commentary
- generator mechanics
- review-state labels
- catalog prefixes
- content-model implementation notes

unless the reader needs them to use the page correctly.

### 19. Keep related docs aligned in the same review unit

When product behavior changes, search nearby surfaces:

- README
- getting started
- command reference
- examples
- config docs
- Rustdoc or code comments
- agent instructions
- status docs

Update them in the same review unit when practical, or record precise follow-up. Do not leave the
user path accurate while the maintainer path drifts, or the reverse.

## Part IV: Examples, Commands, And Evidence

### 20. Examples should prove real use

A good example demonstrates:

- a real workflow
- a real command sequence
- a real configuration shape
- a real failure or recovery path
- a real decision point

It should not exist only to decorate the page or repeat the syntax already shown elsewhere.

Prefer examples that answer:

- what would I actually run first?
- what output or behavior should I expect?
- what does this choice enable or avoid?

### 21. Commands, paths, and flags must be verified

Do not trust memory or prose symmetry.

Verify:

- command names
- flags
- examples
- paths
- env vars
- defaults
- permission names
- update intervals
- mode names
- platform behavior

When a page sounds confident but the command was not checked, the page is not done.

### 22. Match claim strength to evidence

Do not make these sound the same:

- measured behavior
- tested behavior
- observed behavior
- likely behavior
- intended behavior
- planned behavior
- repo preference
- external recommendation

If the evidence is partial, narrow the claim or name the uncertainty.

### 23. Report proof honestly in docs-adjacent handoff

When writing review notes, handoff prose, or change summaries, distinguish:

- what was mechanically verified
- what was read but not run
- what was inferred from source
- what remains a risk

Do not imply that unrun checks passed.

### 24. Examples and support claims must stay aligned

If the product supports:

- certain platforms
- certain backends
- certain auth flows
- certain config shapes
- certain output modes

then docs, examples, support tables, and reference pages need a shared truth source or a shared
review pass.

Support claims are only useful when they stay tied to evidence.

## Part V: Review And De-AI-ification Workflow

### 25. Choose the documentation pass depth before editing

Not every docs change is a rewrite.

Common pass depths:

- local correction
- local drift repair
- page coherence pass
- page rewrite
- repo map repair
- documentation architecture pass
- review narrative pass

State the pass depth before editing so the change does not silently widen.

### 26. Read once for structure and once for sentence-level tells

A good de-AI-ification pass usually has two stages.

Structure pass:

- remove self-narration
- collapse unnecessary headings
- restore a dominant mode
- merge fragments
- replace list abuse with prose
- move misplaced maintainer detail out of the first path

Sentence pass:

- cut filler
- cut stock transitions
- cut ranking words
- cut recommendation inflation
- replace abstract nouns with concrete detail
- replace soft reassurance with direct tradeoffs

Do not start by polishing sentences inside a broken page shape.

### 27. Review docs for correctness and risk before style

When reviewing documentation, lead with:

- incorrect commands
- wrong paths
- stale defaults
- contract drift
- misleading guarantees
- hidden prerequisites
- broken examples
- current-vs-historical confusion

Only then spend time on style polish. Pleasant prose around wrong instructions is still broken
documentation.

### 28. Treat AI-assisted drafts as raw material

AI output can help with collection, compression, or reframing, but it should not become publishable
surface without human ownership.

Assume AI drafts may contain:

- false confidence
- recommendation inflation
- duplicate sections
- taxonomic overbuilding
- vague summaries
- hidden uncertainty
- source drift
- generic tone
- invented abstraction
- bridge prose around links

The human editor's job is to cut, verify, restructure, and restore local voice.

### 29. Do not mistake smoothness for quality

A page can feel polished while being low-signal.

Common signs:

- the prose scans pleasantly but leaves no clear mental model
- every section sounds reasonable but nothing commits to concrete behavior
- the page keeps explaining how to read itself
- recommendation language floats free of tradeoffs
- the same claim appears three times in softer and softer forms

When this happens:

- cut repetition
- merge sections
- replace abstractions with specifics
- add the concrete example that the text keeps circling
- rewrite the opening around the actual product question

### 30. Keep review artifacts standalone

If you are writing issue text, review packets, PR notes, or agent handoff, make them understandable
without private chat context.

A good review artifact names:

- what changed
- why it changed
- what proof ran
- what did not run
- what docs were updated
- what remains intentionally deferred

## Part VI: Repo-Specific Steering Questions

When applying this doctrine to a specific repository, answer these before editing:

- What is the product model the docs should preserve?
- What are the reader entry paths?
- Which pages are active guidance and which are historical?
- Which claims require real command or product verification?
- Which pages currently sound AI-shaped or over-smoothed?
- Which sections are explaining the system, and which are explaining the page?
- Which lists are real enumerations, and which are standing in for missing prose?
- Which recommendation words are unsupported?
- Which examples prove a workflow, and which are ornamental?
- Which doc changes need nearby examples, README text, Rustdoc, or agent guidance updated too?

## Part VII: Default Operating Rules For Agents

When editing docs in this project:

- choose the page job before editing
- preserve one dominant mode per page
- front-load the useful point
- prefer direct technical prose over coaching or marketing tone
- use prose for relationships and lists for enumeration
- cut page narration, teaching-order narration, AI contrast templates, vague action verbs,
  unsupported precision, and comprehensive padding
- replace abstract praise with concrete specifics
- verify commands, paths, examples, defaults, and links
- treat active docs as current contracts
- keep historical records separate from active guidance
- update nearby drifted docs in the same wave when practical
- report validation honestly
- if a draft feels polished but low-signal, cut, merge, and concretize it

## Part VIII: What To Avoid

Do not:

- narrate the page instead of the subject
- turn every explanation into bullets
- keep several tiny headings because they look organized
- use recommendation words as a substitute for tradeoffs
- preserve generated smoothness that hides uncertainty
- add bridge prose for links that can stand alone
- duplicate the same point across README, guide, and command page without need
- let active guidance keep old owners or old paths
- leave examples unverified
- let style cleanup outrank correctness and contract drift
- present AI-generated text as if it were already locally owned

## Success Criteria

This documentation pass is successful when:

- the page or doc set has clearer ownership and clearer mode
- the opening gives the reader the real point quickly
- commands, paths, examples, and claims are more trustworthy
- AI-shaped filler and generic recommendation language are gone
- prose explains relationships that bullets previously hid
- active guidance matches current reality
- historical material stays available without confusing the current path
- the docs are easier for a future maintainer to extend without rediscovering intent
```
