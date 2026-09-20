# Report Verification Honestly

## Metadata

- Name: `Report Verification Honestly`
- ID: `report-verification-honestly`
- Summary: Handoffs become risky when verification is overstated, omitted, or blurred with
  assumptions. Report exactly what ran, what passed or failed, what was not checked, and what risk
  remains.
- Status: `reviewed`
- Audience: `both`
- Topics: `testing, workflow, agents`
- Tags: `verification, review-handoff`
- Related: `smallest-trustworthy-verification`

## Problem

A handoff can imply more confidence than the evidence supports. Phrases like "should work" or broad
claims that tests pass are misleading when only a narrow command ran or when checks were skipped.

## Preferred Move

Report the checks that actually ran, their outcome, and any important checks that did not run. Tie
the verification summary to the changed behavior, not only to compilation or formatting.

Separate implementation, observed behavior, and acceptance. Test counts establish the result of
those tests; they do not establish usability, complete platform support, or release readiness.
Name the build or revision, configuration, and workflow when they affect what the evidence proves.
Keep an important limitation beside the completion claim it narrows.

If later feedback contradicts a claim, correct the claim and add the missing check. Do not preserve
an earlier "complete" or "merge-ready" label merely because the original checks passed.

## Tradeoff

Long logs can bury the useful signal. Summarize the relevant command and result, then include only
the failure detail needed for the next person to act.

## Agent Instruction

State what ran and what behavior it demonstrated. Separate implementation from observed acceptance;
mark skipped checks and correct earlier claims when new evidence narrows them.

## Examples

Bad: the handoff implies broader confidence than the checks earned.

```text
Tests pass.
```

Good: the handoff names the check and the untested surface.

```text
Ran markdownlint-cli2 "**/*.md"; passed. Did not run rendered-doc checks.
```

## References

- [W3C preliminary accessibility checks](https://www.w3.org/WAI/test-evaluate/preliminary/): illustrates
  why limited checks must not be presented as comprehensive acceptance evidence.
