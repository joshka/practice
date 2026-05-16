# Guidance Kind Disambiguation

This note rationalizes the site's guidance kinds from the reader's point of view. The goal is not
to defend taxonomy for its own sake. The goal is to make each kind answer a distinct reader task so
the site stays useful as the catalog grows.

## Core Site Claim

The site is a task router, not just a catalog. Each guidance kind should answer a different question
for a human reviewer, maintainer, agent author, or coding agent.

- Guides answer: where do I start for this work area?
- Rules answer: what should I do?
- Patterns answer: what situation am I seeing, and what move fits it?
- Principles answer: why does this judgment hold, and where does it stop?
- Mechanisms answer: what tool, check, command, or workflow makes this cheaper to follow?
- Agent snippets answer: what compact instruction should an agent actually load?
- References answer: what durable external source supports, frames, or contrasts the local claim?
- Tags answer: what cross-cutting cluster am I browsing?

The kinds are reasonable when they reduce search and review cost. They become unreasonable when the
reader has to understand the taxonomy before they can find the guidance.

## Why The Kinds Exist

A single flat catalog would blur several different jobs.

A reviewer often needs a short citation: that is usually a rule or pattern. A maintainer deciding
whether a rule belongs needs rationale and limits: that is usually a principle. A contributor
trying to work in an area needs a map: that is a guide. An agent needs compact executable wording:
that is an agent snippet. A repo needs checks and commands: that is a mechanism. A skeptical reader
needs inspectable support: that is a reference.

These jobs pull in different directions. A good rule is compact and directive. A good principle is
slower and more explanatory. A good guide is navigational and contextual. A good mechanism is
operational. Trying to make one artifact do all of those jobs usually creates either an overlong
rule or a guide full of hidden rules.

## Reader Tests

Use these tests when deciding which kind a new idea should become.

### Guide

Choose a guide when the reader needs orientation across a work area.

A guide should:

- Map the territory.
- Name the important decisions.
- Route readers to rules, patterns, principles, mechanisms, and references.
- Explain how the pieces fit during real work.

A guide should not be the only home for reusable instructions. If a paragraph says "always,"
"prefer," "avoid," "when," or "do not" and the advice applies outside that guide, extract a rule,
pattern, or principle and link to it.

Site promise: clicking `Guides` should help a reader decide where to go next.

### Rule

Choose a rule when the idea is an action-oriented instruction that should be cited, checked, or
compressed for agents.

A rule should:

- Tell the reader what to do.
- Name the failure mode or tradeoff enough to prevent blind application.
- Include limits.
- Have compact agent wording.
- Fit a domain where review and downstream copying make sense.

Rules are the executable layer of the guidance system. They are not necessarily shallow, but their
center of gravity is instruction.

Site promise: clicking `Rules` should give compact directives with enough context to apply them.

### Pattern

Choose a pattern when the idea has a recognizable situation and a preferred move.

A pattern should:

- Help the reader recognize a repeated shape.
- Name the move that usually works.
- State the tradeoff or counter-signal.
- Work well as review vocabulary.
- Often include a small example.

Patterns are especially useful when the same move appears in several domains, or when the advice is
more like "when you see this pressure, use this move" than "always do this."

Site promise: clicking `Patterns` should give reusable review language for repeated situations.

### Principle

Choose a principle when the idea explains why several rules, patterns, or mechanisms exist.

A principle should:

- State a durable belief or tradeoff.
- Explain why it matters.
- Describe what changes because of it.
- Name good uses, bad smells, mechanisms, and limits.
- Support more specific rules without replacing them.

Principles are the reasoning layer. They should help maintainers decide whether a new rule belongs
and help reviewers know when a rule should bend.

Site promise: clicking `Principles` should explain the judgment behind concrete guidance.

### Mechanism

Choose a mechanism when the important artifact is a tool, command, generated file, CI check,
configuration, or workflow.

A mechanism should:

- Name the repeated failure it prevents or makes cheaper to catch.
- List the commands, checks, configuration, or workflow steps.
- Say which principles or rules it supports.
- Explain what it cannot prove.

Mechanisms should not pretend that tooling replaces judgment. They make preferred behavior easier
and recurring drift more visible.

Site promise: clicking `Mechanisms` should show how guidance becomes operational.

### Agent Snippet

Choose an agent snippet when the guidance needs to be loaded or copied into an agent's operating
context.

An agent snippet should:

- Be compact enough to use in real task context.
- Prefer action and trigger over explanation.
- Route to deeper guides or rules instead of copying all rationale.
- Stay synchronized with reviewed guidance when generated.

Agent snippets are not the source of truth for the full argument. They are execution surfaces.

Site promise: clicking `Agents` should give copyable instructions and packs, not essays.

### Reference

Choose a reference when the site needs durable external support, contrast, or framing.

A reference should:

- Point to stable sources readers can inspect.
- Explain how the source supports, adapts, or differs from local guidance.
- Avoid acting as outsourced prose for the repo.

References are evidence and framing. They are not local guidance by themselves.

Site promise: clicking `References` should help readers check claims without drowning the guidance
pages in source lists.

### Tag

Use tags when the reader needs a cross-cutting browse path.

A tag should:

- Connect related items across kinds.
- Be broad enough to be useful.
- Be narrow enough to distinguish a meaningful cluster.
- Not replace kind or domain.

Tags are facets, not guidance artifacts.

Site promise: clicking `Tags` should reveal clusters that are hard to see from the main sections.

## Decision Order

When classifying a new mined idea, ask these questions in order.

1. Is the main value a command, check, generator, config, or workflow?
   If yes, start with a mechanism.

1. Is the main value a compact instruction pack for agents?
   If yes, start with an agent snippet.

1. Is the main value an external source or source family?
   If yes, start with a reference.

1. Is the reader trying to navigate a work area?
   If yes, start with a guide.

1. Is the idea primarily "do this" or "avoid this"?
   If yes, start with a rule.

1. Is the idea primarily "when you see this situation, use this move"?
   If yes, start with a pattern.

1. Is the idea primarily "this is why several moves are correct, and here are the limits"?
   If yes, start with a principle.

If more than one answer fits, choose the artifact that gives the reader the missing layer. A
principle can support several rules. A pattern can operationalize a principle. A mechanism can
support both. A guide can route to all of them.

## Promotion And Demotion Rules

Use promotion when an idea has outgrown its current kind.

- Promote a guide paragraph to a rule when it is reusable instruction hidden inside navigation.
- Promote repeated rule rationale to a principle when several rules rely on the same tradeoff.
- Promote a repeated review move to a pattern when reviewers need a stable term for it.
- Promote recurring manual correction to a mechanism when a check or template can catch it.

Use demotion or merging when an artifact is carrying the wrong job.

- Demote a principle to a rule when it only says one action and does not explain broader judgment.
- Demote a pattern to a rule when the trigger is incidental and the instruction is the real value.
- Merge a mechanism into a rule when it is just one supporting command, not a reusable tool profile.
- Merge a guide-only section into a guide when the idea is only local orientation.
- Convert a reference-heavy rule into local prose plus references when the source links are carrying
  the argument instead of supporting it.

## Borderline Examples From The Current Mining Pass

`Shared Artifacts Stand Alone` probably wants to be a principle if it explains review, source,
agent, and downstream rules together. If the useful action is only "put context in PRs," then it is
a rule or pattern instead.

`Keep Review Evidence Close` is probably a pattern. It has a visible trigger: evidence exists but
is not where the reviewer is deciding. The preferred move is to place the right proof near the
decision surface.

`Shape Content To Reader Task` probably wants to be a principle. It explains why several
documentation rules exist and when one page should link out instead of absorbing another mode.

`Mechanize Surface Checks` is only a mechanism if it names concrete checks or routes to existing
checks. If it stays abstract, it is probably just a consequence of `Validate The Changed Surface`.

`Keep Derived Artifacts Synchronized` is likely a mechanism, but it may be redundant with
`guidance-generation-and-audit`. It should exist only if the general generated-artifact contract is
useful beyond this repo's current guidance scripts.

`Prefer Inspectable Evidence Over Internal Proxies` is probably a pattern if review comments need a
short move. If not, it should fold into `Validate The Changed Surface`.

`Validate The Changed Surface` is probably a principle. It explains why rendered docs, package
artifacts, public APIs, generated behavior, and canaries sometimes need different proof than local
source inspection.

`Ground Claims In Inspectable Sources` is probably a principle if it stays distinct from shared
context. Its focus should be evidence quality, not artifact completeness.

## Site-Level Implications

The site should make the kind distinction visible without requiring a theory lesson.

Homepage cards should describe the reader task, not just the artifact name. A reader should
understand that `Rules` means "compact instructions," `Patterns` means "repeated situation and
move," and `Principles` means "reasoning and limits."

Section index pages should reinforce the same promise. The intro for each section should answer why
someone would click that section instead of a neighboring one.

Detail pages should preserve kind-specific actions:

- Rules, patterns, and principles get `Copy review note` because they are review-citable.
- Guides, mechanisms, and agent snippets get `Copy citation` because they route, support, or
  execute guidance.
- Feedback links belong on guide, rule, pattern, principle, and mechanism pages because those are
  local guidance artifacts.

Related links should show the layer relationship, not random adjacency:

- Rules should link to supporting principles, patterns, and mechanisms.
- Patterns should link to related rules and principles.
- Principles should link to supported rules and relevant mechanisms.
- Mechanisms should link to the principles and rules they support.
- Guides should link to the most important rules, patterns, principles, and mechanisms in the work
  area.
- References should be linked from the artifacts that use them, but should not become the main
  reader path.

Search results should eventually expose kind as a meaningful filter. A query such as "standalone
artifact" may need a rule for action, a principle for rationale, and a pattern for review language.
The site should make those differences obvious in result snippets.

## Warning Signs

Watch for these failures during content review.

- A rule needs three pages of rationale before the instruction makes sense.
- A principle supports only one narrow action.
- A pattern has no recognizable trigger.
- A guide contains reusable instructions that cannot be cited directly.
- A mechanism has no command, check, config, or workflow.
- A reference is used as decoration instead of evidence.
- A tag is just a synonym for a kind or domain.
- An agent snippet carries nuanced judgment that should live in a rule, pattern, or principle.

## Proposed Durable Move

The durable guidance system probably needs one canonical "guidance kinds" explanation. The best
home is likely `mechanisms/guidance-content-model-stewardship.md`, because this is stewardship of
the catalog rather than a user-facing work guide.

That mechanism should grow a short decision table and promotion rules. The current definitions are
correct but too compact for mining work. The site can keep the short descriptions, while the source
mechanism carries the full classification logic.

After that, review the eight mined candidates against this rubric before promoting any of them.
