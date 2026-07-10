# Docs Avoid Generated Prose Tells

## Metadata

- Name: `Avoid Generated Prose Tells`
- ID: `DOCS-AVOID-GENERATED-PROSE-TELLS`
- Summary: `Replace templated, UI-centered, or polished-but-vague phrasing with concrete behavior.
  Keep the local voice trustworthy without cutting useful explanation.`
- Status: `reviewed`
- Domain: `documentation`
- Tags: `documentation, ai, reader-locality`
- Related: `preserve-local-doc-voice, DOCS-HIDE-CATALOG-MECHANICS`

## Rule

Avoid generated-prose tells.

## Why

Generated prose often sounds polished while hiding that it did not learn the project voice. Phrases
such as "seamless," "robust," repeated summary sentences, teaching-order narration, generic
contrast language, and component-centered navigation copy make technical docs feel less trustworthy
because they avoid naming the concrete behavior.

On documentation sites, generated tells often appear as "cards map," "pages carry," "domains
expose," "the full map," or "how X should be reasoned about." These phrases narrate the catalog or
the UI instead of naming the reader's destination, decision, artifact, or work area.

Use the detailed checklist below during prose review. A single occurrence may be fine; repeated
patterns, clustered patterns, or patterns that replace evidence are the problem.

### Word Choice

- Magic adverbs. Cut adverbs that make ordinary facts sound secretly important, such as claims that
  something quietly, deeply, fundamentally, remarkably, or arguably matters.
- Stock AI verbs and adjectives. Replace "delve," "utilize," "leverage," "robust," "streamline,"
  "harness," and similar defaults with the specific action.
- Ornate domain nouns. Avoid "tapestry," "landscape," "paradigm," "synergy," "ecosystem," or
  "framework" when a simpler domain word is accurate.
- Inflated copulas. Prefer "is" or "are" when grander substitutes like "represents," "marks,"
  "stands as," or "serves as" do not add precision.

### Sentence Structure

- Negative parallelism. Watch repeated `not X, but Y` reframes, causal reversals framed as "not
  for this reason, but for that one," `X, not Y` pivots, and "the question is not X; the question is
  Y" constructions.
- Countdown negation. Avoid stacking negated fragments before the point, such as "not this, not
  that, just the real thing."
- Self-answered questions. Cut rhetorical question fragments that ask and answer a question no
  reader needed answered.
- Repeated openings. Revise runs of sentences that start the same way to create artificial rhythm.
- Rule-of-three padding. Keep triples only when the three items are real and useful; avoid repeated
  three-part phrasing as decoration.
- Empty transitions. Remove "it is worth noting," "importantly," "interestingly," "notably," and
  similar transitions when they do not explain the relationship between ideas.
- Shallow participial analysis. Delete trailing `-ing` phrases that attach vague significance,
  legacy, importance, or broader meaning to a fact.
- False ranges. Avoid `from X to Y` constructions unless the endpoints sit on a real scale with a
  meaningful middle.

### Paragraph Structure

- Punchy fragments. Do not split ordinary explanation into dramatic one-line fragments just to
  manufacture emphasis.
- Disguised listicles. If the paragraph sequence is really "first, second, third," either make it a
  list or rewrite the structure around the actual relationship.

### Tone

- False suspense. Cut "here is the thing," "here is where it gets interesting," "what people miss,"
  and similar setup lines when the next point can stand directly.
- Forced analogy. Use analogies only when they clarify; avoid "think of it as" explanations that
  make an expert topic less precise.
- Speculative invitation. Avoid "imagine a world where" framing when the doc can state current
  behavior, planned behavior, or a concrete example.
- Performative candor. Remove faux vulnerability, fourth-wall asides, and "to be honest" framing
  that tries to sound authentic without adding a concrete constraint.
- Obviousness claims. Do not assert that the truth is simple, clear, obvious, or unambiguous in
  place of proving the point.
- Inflated stakes. Keep the consequence proportional; not every change reshapes an era, defines the
  future, or changes everything.
- Pedagogical filler. Cut "let's break this down," "let's unpack," "let's explore," and similar
  teacher voice unless the doc is intentionally a tutorial.
- Vague attribution. Name the person, document, report, project, or source; do not cite experts,
  observers, reports, or publications without saying which ones.
- Invented concept labels. Do not coin abstract labels such as a trap, paradox, divide, vacuum, or
  inversion unless the concept is defined and then used precisely.

### Formatting

- Dash pivots. Avoid repeated dash asides, dramatic pauses, and pivot clauses when commas,
  parentheses, semicolons, or shorter sentences would be clearer.
- Bold-first bullets. Do not default every list item to a bold lead-in. Use bold labels only when
  the list is genuinely a field list or glossary-like structure.
- Decorative Unicode. Avoid arrows, smart quotes, and special symbols when project style expects
  plain typed characters or ASCII examples.

### Composition

- Fractal summaries. Do not introduce, summarize, and re-summarize every section. Keep summaries for
  real orientation or handoff value.
- Exhausted metaphor. Use a metaphor once if it helps, then return to the system. Do not make the
  whole page carry the same metaphor.
- Historical analogy stacking. Avoid rapid lists of companies, eras, or technology waves as a
  substitute for direct evidence.
- One-point dilution. If a draft repeats one thesis through many phrasings, collapse it to the
  strongest claim and add evidence or examples.
- Content duplication. Check long AI-assisted drafts for repeated paragraphs, repeated sections, and
  near-duplicate sentences.
- Signposted endings. Avoid "in conclusion," "to sum up," and "in summary" unless the phrase is
  part of a real procedural or report structure.
- Formulaic concession. Watch for "despite these challenges" paragraphs that acknowledge problems
  only to dismiss them with an optimistic ending.

### Additional Review Checks

- Hedged neutrality. Replace vague balance language with the actual uncertainty, tradeoff, or
  decision. Do not smooth a contested claim until it no longer says what the author thinks.
- Comprehensive padding. Cut checklist items, caveats, or "complete" coverage claims that add bulk
  without changing the reader's decision.
- Unsupported precision. Remove exact-looking numbers, rankings, timelines, or categories unless
  the doc shows where they came from.
- Apology and permission phrasing. Cut "sorry," "just," "hopefully," "feel free," and similar
  softeners unless the page is intentionally interpersonal.
- Vague action verbs. Replace "ensure," "handle," "support," "manage," and similar verbs with the
  concrete behavior, command, validation, or ownership boundary.

## Helps

- Preserves local voice, keeps docs dense, and makes claims easier to verify.

## Limits

Do not remove useful friendliness or explanation just because a sentence is smooth. Cut the
generated tell when it replaces concrete behavior, evidence, tradeoff language, or a direct
navigation label.

## Agent Instruction

Avoid generated-prose tells, including component-centered navigation copy, that replace concrete
behavior, evidence, tradeoffs, or direct labels. During prose review, check word choice, sentence
templates, paragraph shape, tone, formatting, and repeated composition patterns.

## Mechanisms

Supported by prose review passes, local style guides, examples from accepted docs, and review
checklists that call out vague or templated wording.

## References

- [Principle: Docs Are Contracts](../../principles/docs-are-contracts.md)
- [Docs Hide Catalog Mechanics](docs-hide-catalog-mechanics.md)
- [tropes.md: AI Writing Tropes to Avoid](https://tropes.fyi/tropes-md)
- [Diataxis: how to use Diataxis](https://diataxis.fr/how-to-use-diataxis/)
- [Rustdoc: how to write
  documentation](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html)
