# Project Operating Manual

Use this template when a repository needs one thorough project-owned artifact that applies broad
software rules to the current codebase. Keep `AGENTS.md` short and route meaningful work here.

## Purpose

Explain what this codebase is optimizing for, which software qualities are non-negotiable, and how
the project applies broad engineering guidance locally.

## How To Use This Document

- Read this before making non-trivial changes.
- Update it when a durable project policy, boundary, workflow, or proof standard changes.
- Link to deeper docs instead of duplicating long catalogs inline.
- Name current exceptions and open questions explicitly.

## Project Doctrine

Summarize the software qualities this repo protects first.

- Example categories: correctness, compatibility, simplicity, latency, privacy, reliability,
  operability, reviewability, docs truthfulness.
- Name the tradeoffs the project will accept and the ones it will not.

## System Mental Model

Describe the current architecture and ownership map.

- Which modules own which concepts?
- Which boundaries are stable and load-bearing?
- Which state machines, data flows, or protocols matter most?
- Which external systems or generated artifacts are part of the product surface?

## Change Policy

State how broad change-shape rules apply in this repo.

- What kinds of work must be separated into their own changes?
- When should structure and behavior changes be split?
- How should generated files, migrations, snapshots, lockfiles, and release artifacts be handled?
- Which changes require design discussion before implementation?

## Proof Matrix

List the validation expected for the major change classes in this repo.

| Change class      | Minimum proof | Stronger proof when risk increases | Notes       |
| ----------------- | ------------- | ---------------------------------- | ----------- |
| Docs only         | `[fill in]`   | `[fill in]`                        | `[fill in]` |
| Behavior change   | `[fill in]`   | `[fill in]`                        | `[fill in]` |
| Public API        | `[fill in]`   | `[fill in]`                        | `[fill in]` |
| Dependency update | `[fill in]`   | `[fill in]`                        | `[fill in]` |
| Generated output  | `[fill in]`   | `[fill in]`                        | `[fill in]` |
| Performance work  | `[fill in]`   | `[fill in]`                        | `[fill in]` |

Add or remove rows so the table matches the repo.

## Current Decisions And Exceptions

Capture the local facts that a generic rule pack cannot infer.

- Compatibility promises that change design choices.
- Known debt the project is intentionally carrying.
- Active exceptions to the usual rules.
- Intentional non-goals.
- Temporary constraints from tooling, platform, staffing, or release timing.

## Operating Workflow

Describe how work moves through this repo.

- How should issues, plans, or ADRs be used?
- What should a good review packet include?
- How should jj changes be shaped and described?
- When should follow-up work stay separate?
- What is the publication policy?

## Open Questions

Keep unresolved architectural or policy decisions visible here so agents and maintainers do not
silently answer them inside ordinary implementation changes.

## References

Link the deeper guidance that supports this manual.

- Global guides or rule packs.
- Local ADRs or architecture docs.
- Operational runbooks.
- Release or compatibility policies.
