# VCS Match JJ Topology To Repo Role

## Metadata

- ID: `VCS-MATCH-JJ-TOPOLOGY-TO-REPO-ROLE`
- Name: `Match JJ Topology to Repo Role`
- Summary: Align fetch remotes, push remotes, tracked bookmarks, aliases, and PR bases to repo role.
  Owned, maintainer, and fork-only workflows need different topology assumptions.
- Status: `reviewed`
- Domain: `vcs`
- Depth: `compact`
- Related: `jj-topology-is-repo-role-dependent, vcs-confirm-github-remote-topology`

## Rule

Match jj remote topology to the repository role.

## Why

Owned repos, maintainer-access repos, and fork-only contributor repos need different remote and
bookmark topology. Fetch remote, push remote, `trunk()`, tracked bookmarks, and PR base should match
the role instead of assuming GitHub's default names.

## Helps

- Keeps local jj aliases and publication behavior aligned with the actual collaboration model.

## Limits

Topology can be simple in personal repos. Reevaluate when the repo is forked, transferred, cloned
with `gh`, or used for contributor work without push access.

## Agent Instruction

Match jj remote topology to the repository role because owned repos, maintainer-access repos, and
fork-only contributor repos need different remote and bookmark topology.

## Mechanisms

Supported by remote inspection, repo role notes, `jj config get revset-aliases.trunk`, tracked
bookmark checks, and explicit repair steps after user approval.

## References

- [Principle: JJ Topology Is Repo Role
  Dependent](../../principles/jj-topology-is-repo-role-dependent.md)
- [Jujutsu docs: working copy](https://docs.jj-vcs.dev/latest/working-copy/)
- [Jujutsu docs: bookmarks](https://docs.jj-vcs.dev/latest/bookmarks/)
