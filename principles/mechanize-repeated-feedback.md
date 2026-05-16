# Mechanize Repeated Feedback

## Metadata

- Name: `Mechanize Repeated Feedback`
- ID: `mechanize-repeated-feedback`
- Summary: `Repeated corrections should become checks, templates, generators, lints, or reusable
  guidance when the pattern is stable. Mechanizing the feedback moves human attention back to
  judgment instead of recall.`
- Status: `reviewed`
- Audience: `both`
- Topics: `automation, agents, review, tooling`
- Related: `agent-instructions-are-operational-controls`

## Claim

Repeated review feedback should become a check, template, generator, lint, or reusable guide when
the cost of repeating it exceeds the cost of mechanizing it.

## Why This Exists

Human review attention is scarce. If the same issue appears across sessions, relying on memory or
another prompt makes the failure likely to repeat. A mechanism changes the default path: the easy
path becomes the preferred path, and reviewers spend more time on judgment that cannot be automated.

## Good Uses

- Add a script to check generated docs or rule indexes.
- Add a template field that reminds authors to state tradeoffs.
- Add a lint or formatter rule for stable formatting preferences.
- Add a checklist for expensive release or API validation.

## Bad Smells

- The maintainer gives the same correction in several sessions.
- A generated artifact is frequently stale.
- Agents keep producing output that follows an unstated preference only after correction.
- Review comments focus on mechanical formatting instead of design or correctness.

## Limits

Do not mechanize premature or disputed judgment. A check that encodes the wrong rule creates
friction and false confidence. Start with lightweight scripts or templates when the rule is still
settling, then promote to stricter automation when repeated use proves the value.

## Agent Consequences

Turn repeated feedback into durable tooling or templates before relying on another reminder. Report
which mechanism now prevents the repeated failure.
