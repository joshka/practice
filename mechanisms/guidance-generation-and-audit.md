# Guidance Generation And Audit

## Metadata

- Name: `Guidance Generation And Audit`
- ID: `guidance-generation-and-audit`
- Status: `reviewed`
- Audience: `both`
- Topics: `guidance, rules, agents, generated-artifacts, markdown`
- Related: `agent-instructions-are-operational-controls, mechanize-repeated-feedback`

## Purpose

Use generators and audits for guidance surfaces that must stay synchronized. A guidance repo can
accumulate drift in several places at once: rule files, indexes, compressed agent snippets,
templates, and README maps. The cheapest reliable fix is to make the repeated surfaces generated or
checked, then keep the authored content in one durable source.

This mechanism exists because agent-facing rules are especially sensitive to small wording mistakes.
Links, repeated rule text, vague triggers, or formulaic phrasing can all shape future sessions badly.
The audit should catch those mechanical issues so review attention stays on judgment.

## Supported Principles

- [Agent Instructions Are Operational Controls](../principles/agent-instructions-are-operational-controls.md)
- [Mechanize Repeated Feedback](../principles/mechanize-repeated-feedback.md)
- [Private Context Is Not Shared Context](../principles/private-context-is-not-shared-context.md)

## Checks

- Run the guidance audit before handing off rule or template changes.

```bash
python3 scripts/audit_guidance.py --quality
```

- Check that generated rule indexes match the rule files.

```bash
python3 scripts/generate_rule_indexes.py --check
```

- Check that the compressed agent rule pack is current.

```bash
python3 scripts/generate_agent_rules.py --check
```

- Lint Markdown after generated surfaces are updated.

```bash
markdownlint-cli2 "**/*.md"
```

## What It Catches

- Missing required rule sections.
- Draft or needs-work rules in a release-facing catalog.
- Compressed agent rules that link back to detailed files.
- Agent instructions that merely repeat the rule title.
- Generated indexes or snippets that are stale.
- Markdown formatting drift that makes review noisier.

## What It Cannot Catch

The audit cannot prove that a rule is correct, broadly useful, or written at the right depth. It only
keeps mechanical quality from stealing review attention. Maintainer review still decides whether a
rule belongs in the durable catalog and whether the explanation is concrete enough.

## Use

Use this mechanism whenever changing rule files, rule templates, rule indexes, or compressed agent
snippets. If the same review comment appears repeatedly, prefer adding a check, template field, or
generator rule over repeating the comment in future sessions.
