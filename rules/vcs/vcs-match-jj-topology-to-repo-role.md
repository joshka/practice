# VCS Match JJ Topology To Repo Role

## Metadata

- ID: `VCS-MATCH-JJ-TOPOLOGY-TO-REPO-ROLE`
- Legacy ID: `R-0726`
- Status: `reviewed`
- Domain: `vcs`
- Depth: `compact`

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
