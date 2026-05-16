# Docs Make Guidance Review State Visible

## Metadata

- Name: `Make Guidance Review State Visible`
- ID: `DOCS-MAKE-GUIDANCE-REVIEW-STATE-VISIBLE`
- Summary: `Mark guidance maturity so readers know whether a rule is draft, reviewed, or ready for
  reuse. Visible state prevents tentative advice from becoming an accidental standard.`
- Status: `reviewed`
- Domain: `documentation`
- Tags: `documentation, reviewability, source-truth`
- Related: `make-plans-versioned-artifacts, DOCS-PUT-UNCERTAINTY-IN-TRACKED-PLACES`

## Rule

Make reusable guidance review state visible in the guidance artifact.

## Why

Reusable guidance changes how future agents and maintainers work. A rule, pattern, principle, or
mechanism that has only been drafted should not look the same as maintainer-accepted guidance.
Visible status lets readers distinguish a captured idea from an accepted preference, and it keeps
agent packs from treating unreviewed judgment as operational instruction.

## Helps

- Prevents draft guidance from entering copied instructions as if it were accepted policy.
- Makes maintainer review queues explicit instead of hidden in chat, plans, or memory.
- Lets generated surfaces include drafts for review while keeping execution snippets limited to
  reviewed guidance.

## Limits

Do not use status metadata as a substitute for clear prose. A `reviewed` status means the guidance
was accepted, not that it is exhaustive, permanent, or automatically applicable to every project.

## Agent Instruction

Keep guidance status visible on reusable rules, patterns, principles, and mechanisms; route drafts
to review queues before copying them into execution packs.

## Mechanisms

Supported by status metadata, domain indexes, draft review queues, generator filters that emit only
reviewed rules into agent packs, and audits that reject unknown or missing statuses.

## References

- [GitHub Docs: About pull request
  reviews](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews)
- [Guidance Generation And Audit](../../mechanisms/guidance-generation-and-audit.md)
- [Docs Use Source Links As Support](docs-use-source-links-as-support.md)
