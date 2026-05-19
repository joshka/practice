# JJ Topology Is Repo Role Dependent

## Metadata

- Name: `JJ Topology Is Repo Role Dependent`
- ID: `jj-topology-is-repo-role-dependent`
- Summary: `JJ publication behavior depends on whether the checkout is owned, maintained, or
  fork-based. Align remotes, bookmarks, trunk, and GitHub handoff with that role before mutating
  public state.`
- Status: `reviewed`
- Audience: `both`
- Topics: `jj, github, remotes, publishing`
- Tags: `vcs-jj, tooling, review-handoff`
- Related: `commit-messages-for-history, preserve-unowned-work`

## Claim

Before publishing or repairing jj remote state, identify whether the checkout is an owned repo, a
maintainer clone, or a fork-based contributor clone. Align fetch remotes, push remotes, tracked
bookmarks, PR base/head, and `trunk()` with that role.

## Why I Believe This

Remote names encode assumptions. In a simple owned repo, `origin` may be the canonical remote and
`main@origin` may be the right base. In a fork workflow, GitHub tooling can make `origin` point to
the user's fork and `upstream` point to the source repo. A stale `trunk()` alias or tracked bookmark
can make ordinary commands rebase, compare, or publish against the wrong base.

JJ makes local change management pleasant, but GitHub publication still depends on the real remote
topology. Agents should make that topology explicit instead of relying on default remote names.

## Common Repo Roles

- User-owned repo: fetch, track, and publish through the user's canonical remote, often `origin`.
- Maintainer clone with access: fetch and track the canonical repo; push may go directly to the
  same remote or to a personal namespace depending on project policy.
- Contributor without access: fetch and track the upstream source repo; push to the user's fork;
  open PRs from fork head to upstream base.

## What To Align

- fetch remote;
- push remote;
- tracked `main` or `master` bookmark;
- `trunk()` revset alias;
- PR base repository and branch;
- PR head repository and bookmark;
- `gh` repository inference.

## Good Uses

- Set repo-local `trunk()` to `main@upstream` in a fork-based contributor checkout.
- Confirm `gh repo view` before opening a PR from a jj bookmark.
- Ask before rewriting repo or user config when aliases disagree with intended topology.
- Repair fetch, push, tracking, and `trunk()` together when topology changed.

## Bad Smells

- `origin` and `upstream` exist but no one checked which one is canonical.
- `trunk()` resolves to a fork branch while the PR base is upstream.
- An agent pushes broadly before confirming publication target.
- A remote repair updates fetch config but leaves tracked bookmarks stale.
- A user-level alias is silently rewritten for one repo's needs.

## Mechanisms

- `jj git remote list`.
- `jj bookmark list --all`.
- `jj log -r 'trunk()'`.
- `jj config get 'revset-aliases."trunk()"'`.
- `jj config set --repo 'revset-aliases."trunk()"' 'main@upstream'` when appropriate.
- `gh repo view` and explicit `gh` base/head arguments for non-trivial topology.

## Rules This Supports

- `VCS-CONFIRM-GITHUB-REMOTE-TOPOLOGY`
- `VCS-REPAIR-REMOTE-TOPOLOGY-COHERENTLY`
- `VCS-MATCH-JJ-TOPOLOGY-TO-REPO-ROLE`
- `VCS-ASK-BEFORE-REPAIRING-JJ-ALIASES`

## Agent Consequences

Do not infer publication topology from remote names alone. Inspect the repo role, explain any
mismatch, and ask before repo-scoped or user-scoped config changes unless the user explicitly
requested the repair and the target is unambiguous.

## Limits

Simple single-remote repos can use defaults after inspection confirms they match the real topology.
Use `master` when it is the actual canonical branch.

## References

| Source                              | Use        | Note                                             |
| ----------------------------------- | ---------- | ------------------------------------------------ |
| [jj revset aliases][jj-aliases]     | `supports` | Revset aliases encode reusable base assumptions. |

[jj-aliases]: https://jj-vcs.github.io/jj/latest/revsets/#aliases
