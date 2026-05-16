# Private Context Is Not Shared Context

## Metadata

- Name: `Private Context Is Not Shared Context`
- ID: `private-context-is-not-shared-context`
- Summary: `Shared artifacts must carry the reasoning that downstream readers did not see in the
  private session. Issues, PRs, commits, guides, and review packets should restate the decision
  context that matters.`
- Status: `reviewed`
- Audience: `both`
- Topics: `agents, review, communication, provenance`
- Related: `write-pr-narrative, produce-review-packets, prefer-durable-summaries`

## Claim

Shared artifacts must reestablish the context that downstream readers need. Agent sessions,
scratch files, local findings, discarded options, and steering instructions are private context
unless they are deliberately written into the issue, PR, commit, guide, or review packet.

## Why I Believe This

Agentic tooling can produce work that is guided by strong private reasoning while failing to
communicate that reasoning externally. To the user who saw the session, the result may feel obvious.
To a reviewer, maintainer, or future reader, the same result can look unsupported or arbitrary.

Good shared artifacts make the contribution trustworthy. They restate the problem, explain the
chosen approach, summarize relevant investigation, name paths not taken when they matter, and show
validation. This is not filler; it is the public reasoning surface for work that was privately
steered.

## What This Changes

Write issues, PRs, commits, release notes, and durable docs as if the reader has not seen the
agent session. Do not refer to "as discussed above" or rely on local-only plan files. Bring forward
the rationale that matters and omit private details that do not affect the shared decision.

## Good Uses

- A PR explains why a smaller additive API was chosen over a breaking rename.
- A commit message states the behavior-level reason for a change, not the session transcript.
- A guide captures the durable rule that came from a local review pattern.
- A review packet reports what was investigated and what validation ran.

## Bad Smells

- The PR only says "agent cleanup" or "apply feedback."
- The explanation assumes the reviewer saw the chat.
- A public doc references local mining state or temporary plan files.
- An agent final answer says a decision is principled but does not state the principle.
- A commit message lists mechanics without the reason a future reader needs.

## Mechanisms

- PR templates with summary, rationale, validation, and risk.
- Commit-message guidance that requires context in the body when needed.
- Review packets that name changed behavior, commands run, and residual risk.
- Local-only `AGENTS.override.md` files for checkout facts that must not be committed.
- Source hygiene checks that remove private-source narration from durable docs.

## Rules This Supports

- `REVIEW-MAKE-REVIEW-ARTIFACTS-STANDALONE`
- `SOURCE-MAKE-SHARED-ARTIFACTS-STANDALONE`
- `SOURCE-GENERALIZE-PROJECT-SPECIFIC-RULES`

## Agent Consequences

Before producing a shared artifact, ask what the downstream reader can actually see. Restate the
problem, rationale, choices made, evidence, validation, and remaining risk without leaking private
session details.

## Limits

Do not dump every path explored. Omit sensitive details, irrelevant exploration, and local-only
process notes that do not affect the shared decision.

## References

| Source                         | Use        | Note                                           |
| ------------------------------ | ---------- | ---------------------------------------------- |
| [Ed Page PR style][ed-page-pr] | `supports` | PRs should prepare reviewers with context.     |

[ed-page-pr]: https://epage.github.io/dev/pr-style/
