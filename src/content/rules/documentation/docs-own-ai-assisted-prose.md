# Docs Own AI-Assisted Prose

## Metadata

- Name: `Own AI-Assisted Prose`
- ID: `DOCS-OWN-AI-ASSISTED-PROSE`
- Summary: `AI-generated or AI-assisted docs are reasonable to share when human curation makes them
  author-owned. The published artifact should carry checked claims, reader-sized scope, relevant
  evidence, real tradeoffs, and local voice.`
- Status: `draft`
- Domain: `documentation`
- Tags: `documentation, ai, reviewability, reader-locality`
- Related: `private-context-is-not-shared-context, DOCS-AVOID-GENERATED-PROSE-TELLS,
  DOCS-WRITE-TECHNICAL-PROSE`

## Rule

Own AI-assisted prose before sharing it.

## Personal Standard

This rule is **my** personal authorship standard, not a universal moderation policy. It is
intentionally opinionated because these docs capture the practices I want my own work and agents to
follow. Reasonable people and projects may disagree about where to draw the line for AI-generated
prose, and I am fine with them doing so. That disagreement is part of the point: this rule records
the standard I choose for artifacts that carry my name or steer my agents. It is a standard I keep
in view, not a claim that every sentence will have passed an identical process.

The judgment comes from having worked on AI tooling, using it as part of my own work, and treating
technical writing as engineering work. AI makes text cheaper to produce, but it does not
automatically make text cheaper for another person to receive.

## Why

AI is part of my normal work: exploration, understanding, summarization, writing, coding, critique,
automation, rubber-ducking, and tasks that would otherwise be uneconomic. Substantially
AI-generated docs can still be reasonable to share. The boundary I accept is ownership, not how much
text the model produced: the author should have spent the time to read, test, cut, reshape, and
curate the document before asking others to spend attention on it.

As an open source maintainer, I have also received AI-shaped communication where the submitter did
not seem to understand or control the output. The problem was not model involvement by itself. The
problem was that raw or lightly edited generated prose preserved the model's structure, scope,
hedging, and filler, then shifted the real condensation and coherence work onto the reviewer.

Sharing AI-generated or AI-assisted prose is reasonable when the author has made it their own
artifact. The author should have checked the claims, narrowed the scope to the reader's decision,
removed detail that only exists because generation was cheap, named the evidence and tradeoffs that
matter, and restored the local voice. Disclosure can explain provenance, but it does not replace
curation.

## Helps

- Keeps AI-generated and AI-assisted writing useful without treating all model involvement as
  suspect.
- Preserves reviewer trust by making the author accountable for the artifact's claims and shape.
- Reduces attention cost from long drafts whose quantity outpaces their useful signal.

## Limits

This site will include AI-assisted writing, including substantially AI-written text. That is
compatible with this rule because the published artifact is mine only after I have read it, checked
it against my values and experience, and endorsed it as something I would defend without pointing
back to the tool. A concise, checked, human-curated document from a long AI session can be better
than a transcript or an unassisted memory dump.

The more an artifact affects other people, project direction, or shared review attention, the more
ownership work I owe before publishing it. That includes attribution where attribution is called
for, especially when disclosure would help readers evaluate provenance, trust, or responsibility.

Other people and projects may choose stricter disclosure rules, softer norms, direct use of
AI-generated prose, or outright bans. Follow their rules when contributing there, and respect that
my boundary is not the only reasonable boundary. The boundary I accept in this repo is that
provenance matters less than whether the author has done enough curation to own the artifact.

Very short mechanical rewrites may not need a separate provenance note. The important question is
whether the shared artifact is one the author understands, endorses, and would defend without
pointing back to the model.

## Agent Instruction

Share AI-generated or AI-assisted prose only after reading and curating it into author-owned prose
with checked claims, reader-sized scope, relevant evidence, real tradeoffs, and local voice.

## Mechanisms

Supported by structure passes, generated-prose-tell review, claim-evidence checks, local voice
review, PR templates that ask for rationale and validation, and review comments that ask the author
to state the argument in their own words.

## References

- [Principle: Private Context Is Not Shared
  Context](../../principles/private-context-is-not-shared-context.md)
- [Docs Avoid Generated Prose Tells](docs-avoid-generated-prose-tells.md)
- [Rust Forge PR 1040: Policy on LLM-generated
  text](https://github.com/rust-lang/rust-forge/pull/1040)
- [Rust Forge PR 1040 comment
  mirror](https://triagebot.infra.rust-lang.org/gh-comments/rust-lang/rust-forge/pull/1040)
