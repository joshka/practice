# Guidance Generation And Audit

## Metadata

- Name: `Guidance Generation And Audit`
- ID: `guidance-generation-and-audit`
- Summary: Generators and audits keep rule indexes, compressed agent snippets, downstream
  templates, and Markdown synchronized. The checks catch recurring drift so review attention stays
  on judgment instead of mechanical bookkeeping.
- Status: `reviewed`
- Audience: `both`
- Topics: `guidance, rules, agents, generated-artifacts, markdown`
- Tags: `tooling, automation, documentation, source-truth, generated-artifacts`
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

- Check that the downstream adoption template is current.

```bash
python3 scripts/generate_downstream_template.py --check
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
- Downstream adoption templates that no longer contain every reviewed rule.
- Draft rules that are missing from the guide-rule review queue, stale non-drafts left in that
  queue, or queue entries that drop origin context.
- Extracted draft-rule evidence that names unknown or non-draft rules, omits origin guides, or falls
  out of sync with the review queue.
- Draft rules that lack at least one external reference.
- Non-Rust guide pages that rebuild long flat top-level bullet lists without named grouping.
- Guide pages that drop their related-guidance or review-question sections.
- Non-Rust guide review questions that stop using named subgroups.
- Related-guidance sections that stop linking to a rule artifact.
- Core agent instructions that stop pointing to the guide set or reviewed rule pack.
- Markdown formatting drift that makes review noisier.

## What It Cannot Catch

The audit cannot prove that a rule is correct, broadly useful, or written at the right depth. It only
keeps mechanical quality from stealing review attention. Maintainer review still decides whether a
rule belongs in the durable catalog and whether the explanation is concrete enough.

## Use Cases

Use this mechanism whenever changing rule files, rule templates, rule indexes, or compressed agent
snippets. Use the downstream template when another repo should carry every reviewed rule without
hand-copying from this repo:

```bash
python3 scripts/generate_downstream_template.py --output /path/to/target-repo
```

If the same review comment appears repeatedly, prefer adding a check, template field, or generator
rule over repeating the comment in future sessions.
