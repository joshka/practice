# Guidance Content Model Stewardship

## Metadata

- Name: `Guidance Content Model Stewardship`
- ID: `guidance-content-model-stewardship`
- Summary: Content-model stewardship keeps guides, rules, patterns, principles, mechanisms,
  references, snippets, and downstream templates in distinct roles. The mechanism combines
  mechanical inventory checks with maintainer review queues for overlap, thin guidance, noisy tags,
  and subjective content-quality decisions.
- Status: `reviewed`
- Audience: `both`
- Topics: `guidance, information-architecture, metadata, review`
- Tags: `documentation, source-truth, reviewability, automation, agent-workflow`
- Related: `guidance-generation-and-audit, optimize-for-long-term-coherence,
  mechanize-repeated-feedback`

## Purpose

Keep the guidance catalog coherent as it grows. This repository uses several durable guidance
shapes, and each shape should have a distinct job:

- Guides map a work area and route readers to the right deeper artifacts.
- Rules give compact, action-oriented instructions with enough rationale and limits to apply them.
- Patterns name repeatable situations and review moves.
- Principles explain durable beliefs, tradeoffs, and stopping points.
- Mechanisms name commands, generators, checks, and workflows that make guidance cheaper to follow.
- References collect stable external source families that frame or contrast the guidance.
- Agent snippets provide compact execution surfaces for `AGENTS.md` and downstream adoption.
- Downstream templates carry shared guidance into another repo without overwriting local policy.

The content model is healthy when those shapes reinforce each other instead of duplicating the same
idea in multiple places with different names. Mechanical checks can prove metadata, links, generated
artifacts, and tag vocabulary. Maintainer review still has to decide whether two items should
merge, whether a rule is too thin, or whether a tag cluster is meaningful.

## Current Inventory

The current public catalog has:

- 9 guides.
- 277 reviewed rules.
- 92 patterns.
- 12 principles.
- 8 mechanisms.
- 6 agent snippets.
- 1 reference index.

Every durable guidance item currently has structured metadata, a stable ID, status, tags, and
related links where the shape supports them. The guidance audit checks that structure, while the
rendered site now exposes tags across guides, rules, patterns, principles, mechanisms, and agent
snippets.

## Stewardship Checks

Use this pass after adding a new guidance family, promoting many rules, changing tag vocabulary, or
rewriting guide maps:

1. Inventory the catalog by kind and status.
1. Confirm every durable item has a stable ID, useful summary, status, tags, and related links.
1. Check that each item's kind matches its job: instruction as rule, reusable situation as pattern,
   rationale as principle, command or generator as mechanism, and navigation as guide.
1. Look for duplicate concepts by title, ID, summary, and related-link clusters.
1. Review tag counts for clusters that are too broad to help scanning or too narrow to justify a
   global tag.
1. Inspect representative rendered pages for each layout family: homepage, section index, tag page,
   rule domain, guidance detail, agent snippet, and mechanism page.
1. Record subjective follow-ups instead of silently rewriting local voice when the right move needs
   maintainer judgment.

## Current Follow-Up Queues

These queues are intentionally review-oriented rather than automatic changes:

- Content overlap and depth. The catalog is mechanically complete, but large clusters such as
  `verification`, `documentation`, `rust`, and `reviewability` should be sampled for duplicate
  phrasing, thin rules, and rules that would be clearer as patterns or principles.
- Tag information architecture. Broad tags are useful as search facets, but tag pages with dozens
  of items may need grouping or narrower subclusters before they are ideal browsing surfaces.
- Rendered site rhythm. The site now has breadcrumbs, mobile navigation, related links, tags,
  feedback links, copy actions, and search checks. Remaining review should focus on representative
  page rhythm, tag-page density, search-modal accessibility, and whether large index pages need
  local grouping.
- Downstream canaries. A temp downstream adoption pass preserves an existing `AGENTS.md` and
  renders the copied rule pack, but a real downstream repo canary is still a publication decision.
- Publication. Local validated jj changes still need maintainer review before pushing to `main`.

## What It Cannot Catch

No audit can prove that the guidance is the best possible wording or that every future reader will
choose the right page. This mechanism keeps the catalog inspectable and names the review questions
that remain human judgment: merge, split, promote, demote, narrow, or leave alone.
