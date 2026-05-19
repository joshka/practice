# Prove Security Impact

## Metadata

- Name: `Prove Security Impact`
- ID: `prove-security-impact`
- Summary: Security reports create noise when they imply exploitability without showing reachability
  or consequence. Prove the attacker path and impact, or clearly label the finding as an unproven
  hypothesis.
- Status: `reviewed`
- Audience: `agents`
- Topics: `agents, security, review`
- Tags: `security-privacy, verification, review-handoff`
- Related: `report-verification-honestly, smallest-trustworthy-verification`

## Problem

Security reviews become noisy when agents report theoretical issues without exploitability,
reachability, or impact. Maintainers then spend attention triaging guesses instead of fixing proven
risks.

## Preferred Move

For security findings, prove the impact or clearly label the finding as unproven. Show the reachable
path, attacker capability, failing invariant, concrete consequence, and the smallest evidence that
demonstrates the issue.

## Tradeoff

Some early security exploration should keep hypotheses visible. Separate hypotheses from confirmed
findings so the handoff does not imply more certainty than the evidence supports.

## Agent Instruction

When red-teaming a repo, do not report a vulnerability as real until you can show impact or
exploitability. Include the proof, or place the item in an unproven hypothesis section.

## Examples

Bad: the report asserts risk from a code smell.

```text
This parser might allow path traversal because it joins user input with a base path.
```

Good: the report proves the failing boundary.

```text
`../../secrets.toml` reaches outside the workspace because `normalize_path` cleans the path before
checking the prefix. The added test fails on main and passes after the boundary check moves after
normalization.
```
