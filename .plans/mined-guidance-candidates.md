# Mined Guidance Candidates

<!-- markdownlint-disable MD024 -->

This review packet records candidate guidance artifacts found by scanning repeated ideas across
rules, patterns, principles, and mechanisms. These are not accepted guidance yet. Use this file to
accept, reject, merge, rename, or defer each candidate before creating durable principle, pattern,
or mechanism files.

## Review Criteria

Accept a candidate when it does at least one of these jobs:

- Names a repeated idea that currently appears in several rule families.
- Explains a tradeoff that individual rules rely on but do not fully state.
- Gives reviewers and agents a better citation handle than a domain-specific rule.
- Reduces duplication without flattening useful domain differences.

Reject or defer a candidate when it mostly renames existing guidance, creates a vague umbrella, or
would make the catalog harder to navigate.

## Candidate 1: Shared Artifacts Stand Alone

- Proposed kind: `principle`
- Proposed ID: `shared-artifacts-stand-alone`
- Candidate status: `review`
- Main cluster: review artifacts, source hygiene, agent handoffs, downstream templates

### Core Claim

Any artifact that leaves the private working context should carry the problem, decision, rationale,
evidence, and remaining risk needed by its next reader. Issues, PRs, commits, handoffs, templates,
generated packs, and downstream guidance should not require chat history, local notes, or memory to
be trusted.

### Why It Might Belong

This is broader than the current review and source rules. The same failure appears in review
packets, source hygiene, downstream templates, commit messages, and agent final answers: the work
may be correct, but the artifact does not explain itself to someone who did not see the session.

As a principle, this would explain why several domain rules exist and where they stop. The principle
would not replace the rules; it would give them a shared rationale and a better citation handle.

### Evidence In Existing Guidance

- `private-context-is-not-shared-context`
- `REVIEW-MAKE-REVIEW-ARTIFACTS-STANDALONE`
- `SOURCE-MAKE-SHARED-ARTIFACTS-STANDALONE`
- `AGENT-PRODUCE-REVIEW-PACKETS`
- `AGENT-REVIEW-OUTPUT-AS-FUTURE-MAINTAINER`
- `write-pr-narrative`
- `produce-review-packets`
- `prefer-durable-summaries`

### Rejection Signals

Reject this if `private-context-is-not-shared-context` already covers the whole idea clearly enough.
Also reject it if the proposed name sounds like a rule rather than a durable belief. A narrower
rename or expansion of the existing principle may be better than adding a second principle.

### Likely Follow-Up

Either promote this as a new principle and link the source/review/agent rules to it, or expand
`private-context-is-not-shared-context` to explicitly cover generated packs, templates, and
downstream artifacts.

## Candidate 2: Shape Content To Reader Task

- Proposed kind: `principle`
- Proposed ID: `shape-content-to-reader-task`
- Candidate status: `review`
- Main cluster: documentation structure, page mode, site IA, examples

### Core Claim

Documentation should be shaped around the reader's task: orienting, learning, deciding, applying,
checking, reviewing, or referencing. A page should have one dominant mode, and secondary modes
should move behind links or clearly named sections.

### Why It Might Belong

Several documentation rules repeat this idea from different angles. The current rule set covers
document type, page shape, headings, README role, catalog mechanics, examples, and front-loaded
decisions. A principle would explain the common judgment behind those moves: structure is not
cosmetic; it controls how much work the reader has to do.

This candidate is useful because it can guide new pages before there is a specific rule violation.
It also gives agents a compact reason to avoid blending tutorial, reference, roadmap, generated
catalog, and review-note material on one page.

### Evidence In Existing Guidance

- `DOCS-CHOOSE-DOCUMENT-TYPE`
- `DOCS-MATCH-PAGE-SHAPE-TO-READER-TASK`
- `DOCS-ONE-DOMINANT-MODE-PER-PAGE`
- `DOCS-FRONT-LOAD-USEFUL-POINT`
- `DOCS-README-AS-ENTRY-POINT`
- `DOCS-HIDE-CATALOG-MECHANICS`
- `DOCS-NAME-DESTINATION-NOT-DIRECTION`
- `DOCS-WRITE-FOR-NON-LINEAR-READERS`
- `choose-doc-type`
- `choose-doc-pass-depth`

### Rejection Signals

Reject this if it would duplicate `docs-are-contracts` or if the catalog benefits more from keeping
these ideas as operational rules. It may also be too broad if it cannot state clear limits for pages
that intentionally mix modes, such as a README that must orient and route.

### Likely Follow-Up

Create a principle if the maintainer wants a broad citation handle. Otherwise, add a short "reader
task" paragraph to `guides/documentation-workflow.md` and keep the individual rules as the primary
surface.

## Candidate 3: Validate The Changed Surface

- Proposed kind: `principle`
- Proposed ID: `validate-the-changed-surface`
- Candidate status: `review`
- Main cluster: testing, rendered docs, release artifacts, generated behavior, canaries

### Core Claim

Validation should exercise the surface that actually changed, not merely a nearby implementation
proxy. If the changed surface is rendered documentation, a release package, a generated artifact, a
public API, a command line, or live provider behavior, the proof should reach that surface.

### Why It Might Belong

The catalog repeatedly warns against trusting indirect evidence. Unit tests can miss integration
breakage. Source review can miss rendered documentation problems. Working-tree checks can miss
package contents. Local behavior can miss provider or rollout failures.

This is a strong principle candidate because it explains how to choose proof across many domains.
It complements `tests-should-explain-failures`: one principle says failures should be useful, while
this one says evidence should target the right surface.

### Evidence In Existing Guidance

- `TEST-MATCH-EVIDENCE-TO-SURFACE`
- `DOCS-BUILD-DOCS-LIKE-USERS-READ-THEM`
- `RUST-RELEASE-ONLY-AFTER-ARTIFACT-VALIDATION`
- `RUST-VALIDATE-PACKAGE-CONTENTS-BEFORE-RELEASE`
- `BOUNDARY-STAGE-GENERATED-BEHAVIOR`
- `AGENT-VERIFY-RISKY-CHANGES-WITH-CANARIES`
- `verify-with-canaries-before-cutover`
- `smallest-trustworthy-verification`
- `review-proof-not-just-code`

### Rejection Signals

Reject this if `smallest-trustworthy-verification` can carry the same idea after a small expansion.
Also reject it if the principle becomes an excuse for always running broad checks. The useful
version must preserve the idea that the smallest relevant proof is often better than broad unrelated
proof.

### Likely Follow-Up

Promote this as a principle and link testing, docs, Rust release, boundary, and agent rules to it.
Add limits that distinguish "changed surface" validation from expensive blanket validation.

## Candidate 4: Ground Claims In Inspectable Sources

- Proposed kind: `principle`
- Proposed ID: `ground-claims-in-inspectable-sources`
- Candidate status: `review`
- Main cluster: source hygiene, integrations, review evidence, documentation claims

### Core Claim

Durable claims should be backed by sources that future readers can inspect, compare, and challenge.
When a claim rests on observation, provider behavior, benchmark output, or maintainer judgment, the
artifact should say what evidence exists and what is inferred.

### Why It Might Belong

The repo has many rules about primary sources, source links, observed versus inferred claims,
provider documentation, benchmark provenance, and review proof. The repeated concern is not just
citation style; it is preventing private memory, stale summaries, and unverified assumptions from
becoming durable guidance.

This candidate would give source-backed guidance a general principle that applies beyond
documentation. It would also clarify that links support local judgment; they do not supply the
repo's voice or replace review.

### Evidence In Existing Guidance

- `SOURCE-PREFER-PRIMARY-STABLE-SOURCES`
- `BOUNDARY-GROUND-INTEGRATIONS-IN-PRIMARY-SOURCES`
- `DOCS-USE-SOURCE-LINKS-AS-SUPPORT`
- `REVIEW-LABEL-SPECULATION-AS-INFERRED-OR-UNKNOWN`
- `REVIEW-EXPLAIN-PR-PROBLEM-MODEL-AND-PROOF`
- `PERF-RECORD-BENCHMARK-PROVENANCE`
- `AGENT-REPORT-PROOF-IN-HANDOFFS`
- `label-doc-claims-by-evidence`
- `report-verification-honestly`

### Rejection Signals

Reject this if it overlaps too much with `private-context-is-not-shared-context`. The distinction
has to be clear: private context is about whether an artifact carries enough rationale; inspectable
sources are about whether the factual claims can be checked.

### Likely Follow-Up

Create a principle if this distinction is useful. Otherwise, expand `SOURCE-PREFER-PRIMARY-STABLE-
SOURCES` and link more rules to it as the source-family anchor.

## Candidate 5: Keep Review Evidence Close

- Proposed kind: `pattern`
- Proposed ID: `keep-review-evidence-close`
- Candidate status: `review`
- Main cluster: PR descriptions, review packets, inline rationale, agent handoffs

### Core Claim

When review depends on evidence, put the evidence where the reviewer is already deciding: the PR
description, issue slice, commit message, inline comment, handoff, or checklist. Avoid making the
reviewer reconstruct proof from a terminal transcript, hidden plan, or unrelated status comment.

### Why It Might Belong

This is more operational than `Shared Artifacts Stand Alone`. It names the move to make during
review preparation: keep proof adjacent to the decision. It would be useful as a pattern because it
has a recognizable trigger: a reviewer needs evidence to evaluate a change, and the evidence exists
somewhere else.

The pattern would help avoid bulky artifacts too. It should say to put the right proof near the
decision, not to paste every command output into every PR.

### Evidence In Existing Guidance

- `REVIEW-EXPLAIN-PR-PROBLEM-MODEL-AND-PROOF`
- `REVIEW-MAKE-REVIEW-ARTIFACTS-STANDALONE`
- `REVIEW-EXPLAIN-CONTROVERSIAL-CHOICES-INLINE`
- `AGENT-PRODUCE-REVIEW-PACKETS`
- `AGENT-REPORT-PROOF-IN-HANDOFFS`
- `write-pr-narrative`
- `produce-review-packets`
- `review-proof-not-just-code`

### Rejection Signals

Reject this if it is just a narrower restatement of `produce-review-packets`. A distinct pattern
should focus on evidence placement, not the whole review packet shape.

### Likely Follow-Up

Create as a pattern only if review comments need this citation often. Otherwise, add an evidence
placement note to `produce-review-packets` or `write-pr-narrative`.

## Candidate 6: Mechanize Surface Checks

- Proposed kind: `mechanism`
- Proposed ID: `mechanize-surface-checks`
- Candidate status: `review`
- Main cluster: rendered docs, search, package artifacts, generated pages, canaries

### Core Claim

Use tools that check the user-facing or consumer-facing surface when that surface is prone to
drift. Rendered documentation, search indexes, package contents, generated pages, and release
artifacts should have repeatable checks when source review alone is not enough.

### Why It Might Belong

The existing mechanisms cover guidance generation, Rust docs, Rust release, and testing. This
candidate cuts across them with a narrower purpose: automate checks for surfaces that users or
downstream consumers actually touch.

It may be useful if the repo wants a named mechanism for site search checks, rendered docs, package
artifact validation, and canaries. It should not replace existing domain mechanisms; it would route
readers to the right one.

### Evidence In Existing Guidance

- `guidance-generation-and-audit`
- `rust-docs-validation`
- `rust-api-and-release-checks`
- `testing-and-benchmarking`
- `DOCS-BUILD-DOCS-LIKE-USERS-READ-THEM`
- `TEST-MATCH-EVIDENCE-TO-SURFACE`
- `RUST-RELEASE-ONLY-AFTER-ARTIFACT-VALIDATION`
- `AGENT-VERIFY-RISKY-CHANGES-WITH-CANARIES`

### Rejection Signals

Reject this if it becomes a vague umbrella over existing mechanisms. It should only exist if the
maintainer wants a cross-domain command/check map for surface validation. Otherwise, the current
mechanisms are more precise.

### Likely Follow-Up

Defer unless a repeated review problem appears where contributors run implementation checks but
miss rendered, generated, package, or downstream surfaces. If accepted, write it as a short routing
mechanism with links to existing checks.

## Candidate 7: Keep Derived Artifacts Synchronized

- Proposed kind: `mechanism`
- Proposed ID: `keep-derived-artifacts-synchronized`
- Candidate status: `review`
- Main cluster: generated indexes, agent snippets, downstream templates, rule packs

### Core Claim

When one source of truth produces several review or execution surfaces, make the derived artifacts
generated, checked, or explicitly refreshed. Stale indexes, snippets, templates, README maps, and
downstream packs should fail checks before they mislead readers or agents.

### Why It Might Belong

This idea is already strong in the repo, especially in guidance generation. A separate mechanism
would be useful only if the repo wants to name the general generated-artifact contract independent
of the current guidance-specific scripts.

The candidate is probably lower priority because `guidance-generation-and-audit` already covers the
local implementation well. It might still be a good abstraction if future non-guidance generated
artifacts need the same treatment.

### Evidence In Existing Guidance

- `guidance-generation-and-audit`
- `CHANGE-SYNC-GENERATED-ARTIFACTS`
- `CHANGE-RESPECT-GENERATED-ARTIFACT-OWNERSHIP`
- `AGENT-MAKE-BAD-OUTPUT-HARD`
- `AGENT-PREFER-TOOLS-OVER-PROMPTS`
- `RUST-RELEASE-ONLY-AFTER-ARTIFACT-VALIDATION`
- `keep-automations-repo-owned`
- `make-bad-output-mechanically-hard`

### Rejection Signals

Reject this if it duplicates `guidance-generation-and-audit`. The main reason to keep it would be a
desire for a general mechanism that can outlive this repo's current scripts.

### Likely Follow-Up

Most likely defer. If accepted, write it as a mechanism for generated artifacts generally, then let
`guidance-generation-and-audit` remain the repo-specific implementation.

## Candidate 8: Prefer Inspectable Evidence Over Internal Proxies

- Proposed kind: `pattern`
- Proposed ID: `prefer-inspectable-evidence-over-internal-proxies`
- Candidate status: `review`
- Main cluster: validation, review proof, release checks, rendered output

### Core Claim

When a reviewer needs confidence in a claim, prefer evidence they can inspect at the relevant
boundary over an internal proxy that only suggests the claim is true. Examples include rendered docs
instead of Markdown source alone, package contents instead of working-tree presence, public API
reports instead of private module review, and command output instead of confidence language.

### Why It Might Belong

This is the pattern-shaped version of `Validate The Changed Surface`. It is useful when the
reviewer is deciding what proof to ask for. The pattern can be cited in review comments without
requiring a broad principle discussion.

It may be redundant if `Validate The Changed Surface` becomes a principle. The two could coexist if
the principle explains why and the pattern explains the review move.

### Evidence In Existing Guidance

- `TEST-MATCH-EVIDENCE-TO-SURFACE`
- `AGENT-REPORT-PROOF-IN-HANDOFFS`
- `REVIEW-EXPLAIN-PR-PROBLEM-MODEL-AND-PROOF`
- `DOCS-BUILD-DOCS-LIKE-USERS-READ-THEM`
- `RUST-VALIDATE-RUST-DOCS-AS-CODE`
- `RUST-VALIDATE-PACKAGE-CONTENTS-BEFORE-RELEASE`
- `smallest-trustworthy-verification`
- `report-verification-honestly`

### Rejection Signals

Reject this if the principle is enough. Also reject it if the name is too long to cite in reviews.
A shorter name such as `Prefer Boundary Evidence` may be better if accepted.

### Likely Follow-Up

Keep as a pattern candidate if review comments often need a concise move. Otherwise, fold the idea
into `Validate The Changed Surface`.

## Suggested Initial Decisions

The strongest candidates for promotion are:

1. `Shared Artifacts Stand Alone`
1. `Shape Content To Reader Task`
1. `Validate The Changed Surface`
1. `Ground Claims In Inspectable Sources`

The candidates most likely to be merged or deferred are:

1. `Keep Review Evidence Close`
1. `Mechanize Surface Checks`
1. `Keep Derived Artifacts Synchronized`
1. `Prefer Inspectable Evidence Over Internal Proxies`

The first group provides broader reasoning handles. The second group is useful, but each item may
be better as a supporting paragraph inside an accepted principle, pattern, or existing mechanism.
