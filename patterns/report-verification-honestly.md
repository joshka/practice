# Report Verification Honestly

## Metadata

- Name: `Report Verification Honestly`
- ID: `report-verification-honestly`
- Status: `draft`
- Audience: `both`
- Topics: `testing, workflow, agents`
- Related: `smallest-trustworthy-verification`

## Problem

A handoff can imply more confidence than the evidence supports. Phrases like "should work" or broad
claims that tests pass are misleading when only a narrow command ran or when checks were skipped.

## Preferred Move

Report the checks that actually ran, their outcome, and any important checks that did not run. Tie
the verification summary to the changed behavior, not only to compilation or formatting.

## Tradeoff

Long logs can bury the useful signal. Summarize the relevant command and result, then include only
the failure detail needed for the next person to act.

## Agent Instruction

State exactly what verification ran. Mark skipped checks as not run and name the remaining risk
instead of implying unearned confidence.

## References

- Link: `AGENTS.md`
- Use: `supports`
- Note: The repo handoff requires reporting validation honestly, including unavailable tools.
