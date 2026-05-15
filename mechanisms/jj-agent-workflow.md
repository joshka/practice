# JJ Agent Workflow

## Metadata

- Name: `JJ Agent Workflow`
- ID: `jj-agent-workflow`
- Status: `reviewed`
- Audience: `agent`
- Topics: `jj, git, workspaces, agents, vcs`
- Related: `jj-topology-is-repo-role-dependent, private-context-is-not-shared-context`

## Purpose

Make jujutsu predictable for unattended agent work. Agents do better when the source-control tool
behaves noninteractively, the current change has a clear purpose, and publication topology is
explicit instead of inferred from Git defaults.

This mechanism keeps local workflow choices from leaking into shared artifacts. It is reasonable for
one checkout to use jj, local override notes, or ignored planning files, but commits, PRs, and
issues still need to explain the change in terms that downstream reviewers can understand without
private session context.

## Supported Principles

- [JJ Topology Is Repo Role Dependent](../principles/jj-topology-is-repo-role-dependent.md)
- [Private Context Is Not Shared Context](../principles/private-context-is-not-shared-context.md)
- [Change Shape Controls Review Cost](../principles/change-shape-controls-review-cost.md)

## Local Configuration

- Set a noninteractive pager for agent-run commands.

```bash
export JJ_PAGER=cat
```

- In repos where signing prompts block jj rewrites, use repo-scoped signing behavior only after
  confirming the repo policy.

```bash
jj --no-pager config set --repo signing.behavior drop
```

- Put local-only notes in ignored files such as `AGENTS.override.md` and add the filename to a
  global ignore or exclude configuration.

## Command Shape

- Use `jj --no-pager status`, `jj --no-pager log`, and `jj --no-pager diff` for inspection.
- Start separate reviewable work with `jj --no-pager new`.
- Describe meaningful changes early with `jj --no-pager desc --message`.
- Use `jj --no-pager absorb` when a small follow-up clearly belongs in an earlier stack layer.
- Use `jj --no-pager op log` and `jj --no-pager undo` for recovery instead of repeating failed
  mutations.

## Remote Topology

Owned repos, maintainer repos, and contributor-with-fork repos can all have different correct remote
layouts. Confirm which remote is the source of truth before creating bookmarks, pushing, or telling
reviewers what changed. In forked GitHub repos, `origin` may be the fork while `upstream` is the
project; in owned repos, `origin` may be correct.

## What It Cannot Catch

This mechanism does not replace judgment about stack shape. A command can be jj-native and still be
the wrong operation if it combines unrelated work, rewrites someone else's changes, or publishes to
the wrong remote.
