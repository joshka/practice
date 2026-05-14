# Documentation Workflow

Status: `reviewed`

This guide collects preferences for deciding what documentation work belongs in a change, how deep
the edit should go, and how review-facing prose should carry evidence. Use it with
[Markdown And Documentation][markdown-docs], [Coding Agents][agents], and
[Software Change Preferences][change].

Documentation workflow is about scope control. Good docs should explain the current system, preserve
useful reasoning, and help reviewers decide without turning every edit into a full rewrite.

## Core Preference

Choose the documentation job before editing. A typo fix, API contract repair, page rewrite, repo map,
and PR handoff all have different review costs.

Use [Choose Doc Pass Depth][pass-depth] when an edit could expand from local correctness into page
coherence or documentation architecture. Use [Choose Doc Type][doc-type] when the page is mixing
task, reference, explanation, or decision-record work.

## Evidence And Claims

Docs should state current behavior and match their certainty to the evidence. Contracts, tests,
measurements, observations, project preferences, and external sources should not sound identical.

Use [Label Doc Claims By Evidence][evidence] when prose uses strong claims, ranking words, or broad
guarantees. Use [Report Verification Honestly][verification] when handoff notes must distinguish
run checks, skipped checks, assumptions, and remaining risk.

## Voice And Shape

Documentation should preserve the useful local voice of a project: its directness, terms, examples,
heading density, and level of formality. Generated prose often becomes smooth while losing the
project's actual way of explaining tradeoffs.

Use [Preserve Local Doc Voice][voice] when revising existing prose. Use
[Preserve Intent Over Literalism][intent] when a requested rewrite would keep words but lose the
decision the original text was carrying.

## Repo Maps And Layers

Repository docs need a small reliable map before they need a large tree. Separate user entry points,
maintainer details, reference material, and durable decisions so readers meet depth when they need
it.

Use [Bootstrap Repo Docs][bootstrap] when creating or reorganizing project docs. Use
[Use AGENTS.md As Map][agents-map] when agent instructions should point to canonical guides instead
of becoming a long standalone manual.

## Review Narrative

Describing the change is part of the work. PRs, review packets, and jj descriptions should help a
reviewer understand purpose, user-facing surface, decisions, validation, deferred work, and the best
path through the diff.

Use [Write PR Narrative][pr-narrative] when a change needs a review guide. Use
[Produce Review Packets][review-packets] when the handoff should bundle summary, proof, artifacts,
and known risks.

## Drift Remediation

Docs drift when behavior changes without nearby explanation changing with it. Treat stale docs as
broken contracts: fix them, remove them, or explicitly record the follow-up.

Use [Remediate Doc Drift][doc-drift] when behavior, examples, command output, public API, or agent
instructions no longer match reality. Use [Keep Docs Near Their Subject][doc-locality] when drift
keeps recurring because the doc is too far from the thing it describes.

## Review Questions

- What documentation job is this change doing?
- Is the pass depth explicit and small enough for the review unit?
- Does the prose state current behavior instead of aspiration?
- Are strong claims backed by contracts, tests, measurements, or sources?
- Does the edit preserve the local voice and density?
- Are user, maintainer, reference, and decision docs in the right layer?
- Does the review narrative explain purpose, surface, validation, and follow-up?
- Did behavior changes update nearby docs, examples, and agent instructions?

[agents]: coding-agents.md
[agents-map]: ../patterns/use-agents-md-as-map.md
[bootstrap]: ../patterns/bootstrap-repo-docs.md
[change]: software-change-preferences.md
[doc-drift]: ../patterns/remediate-doc-drift.md
[doc-locality]: ../patterns/keep-docs-near-their-subject.md
[doc-type]: ../patterns/choose-doc-type.md
[evidence]: ../patterns/label-doc-claims-by-evidence.md
[intent]: ../patterns/preserve-intent-over-literalism.md
[markdown-docs]: markdown-documentation.md
[pass-depth]: ../patterns/choose-doc-pass-depth.md
[pr-narrative]: ../patterns/write-pr-narrative.md
[review-packets]: ../patterns/produce-review-packets.md
[verification]: ../patterns/report-verification-honestly.md
[voice]: ../patterns/preserve-local-doc-voice.md
