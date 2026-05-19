# Smallest Trustworthy Verification

## Metadata

- Name: `Smallest Trustworthy Verification`
- ID: `smallest-trustworthy-verification`
- Summary: Verification is weak when it is either skipped or broad without covering the likely
  failure. Run the cheapest check that could catch the risk introduced by the change, broadening
  only when shared contracts or user-visible behavior require it.
- Status: `reviewed`
- Audience: `both`
- Topics: `testing, workflow, review`
- Tags: `verification, testing, reviewability`
- Related: `report-verification-honestly`

## Problem

A change can be marked done after either no verification or an expensive check that does not cover
the actual risk. Both outcomes leave the reviewer guessing whether the likely failure was tested.

## Preferred Move

Run the cheapest check that could catch the likely failure introduced by the change. Use formatting
checks for Markdown shape, type checks for signature movement, focused tests for behavior, and
broader suites when shared contracts changed.

## Tradeoff

A cheap check is not trustworthy when it would pass despite the likely bug. Broaden verification
when the change crosses modules, public behavior, generated artifacts, or user-visible workflows.

## Agent Instruction

Before calling work complete, run the smallest check that can catch the likely failure. Report what
ran and do not imply broader verification than you performed.

## Examples

Bad: the check is broad-sounding but not tied to the changed surface.

```text
Looks good.
```

Good: the check can fail for the changed Markdown rules.

```text
Ran markdownlint-cli2 "**/*.md"; passed.
```
