# Smallest Trustworthy Verification

## Metadata

- Name: `Smallest Trustworthy Verification`
- ID: `smallest-trustworthy-verification`
- Status: `draft`
- Audience: `both`
- Topics: `testing, workflow, review`
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

## References

- Link: `patterns/report-verification-honestly.md`
- Use: `supports`
- Note: Verification choice and verification reporting are separate but linked obligations.
