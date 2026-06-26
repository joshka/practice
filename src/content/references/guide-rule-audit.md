# Guide Rule Audit

This reference records draft rules extracted from guide-level guidance. It keeps the draft review
queue explicit so generated agent packs can remain reviewed-only while guide-to-rule extraction is
still in progress.

## Draft Review Queue

- `DOCS-OWN-AI-ASSISTED-PROSE`: extracted from `guides/documentation-workflow.md` and
  `guides/markdown-documentation.md`; review whether the rule should stay documentation-specific or
  become a broader source-quality rule.
- `OBSERVABILITY-KEEP-RECOVERY-ADVICE-SAFE-AND-HONEST`: extracted from
  `guides/observability-and-failure.md`; review whether recovery guidance needs separate CLI, UI,
  and API examples before promotion.
- `OBSERVABILITY-MATCH-FAILURE-OUTPUT-TO-SURFACE`: extracted from
  `guides/observability-and-failure.md`; review whether the rule has enough accessibility and
  product-surface examples before promotion.

## Extracted Draft Rules

- From `guides/documentation-workflow.md` and `guides/markdown-documentation.md`:
  [`DOCS-OWN-AI-ASSISTED-PROSE`](../rules/documentation/docs-own-ai-assisted-prose.md) captures
  that documentation review treats AI-assisted drafts as raw material that still needs checked
  claims, local voice, evidence, and tradeoff review.
- From `guides/observability-and-failure.md`:
  [`OBSERVABILITY-KEEP-RECOVERY-ADVICE-SAFE-AND-HONEST`](../rules/observability/observability-keep-recovery-advice-safe-and-honest.md)
  captures that failure output should offer recovery advice only when the system can support it
  safely.
- From `guides/observability-and-failure.md`:
  [`OBSERVABILITY-MATCH-FAILURE-OUTPUT-TO-SURFACE`](../rules/observability/observability-match-failure-output-to-surface.md)
  captures that failure output belongs on the surface that matches the audience, consequence, and
  action path.
