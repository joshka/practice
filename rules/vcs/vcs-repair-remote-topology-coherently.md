# VCS Repair Remote Topology Coherently

## Metadata

- ID: `VCS-REPAIR-REMOTE-TOPOLOGY-COHERENTLY`
- Name: `Repair Remote Topology Coherently`
- Summary: Repair fetch, push, tracking, trunk alias, PR base, and PR head assumptions together.
  Remote topology is coupled, so partial fixes can leave publication commands half-correct.
- Status: `reviewed`
- Domain: `vcs`
- Depth: `compact`

## Rule

Repair remote topology coherently.

## Why

Remote topology has several coupled pieces: fetch remote, push remote, tracked bookmark, trunk
alias, PR base, and PR head. Repairing one without the others can leave commands half-correct and
fail later during publication.

## Helps

- Keeps jj, GitHub, and local aliases consistent after topology drift.

## Limits

Do not repair topology from guesses. Inspect repo role and ask before changing user-level config or
publication defaults.

## Agent Instruction

Repair remote topology coherently because remote topology has several coupled pieces: fetch remote,
push remote, tracked bookmark, trunk alias, PR base, and PR head.

## Mechanisms

Supported by remote lists, bookmark tracking checks, revset alias inspection, GitHub repo metadata,
dry-run publication, and documented repair steps.

## References

- [Principle: JJ Topology Is Repo Role
  Dependent](../../principles/jj-topology-is-repo-role-dependent.md)
- [Jujutsu docs: working copy](https://docs.jj-vcs.dev/latest/working-copy/)
- [Jujutsu docs: bookmarks](https://docs.jj-vcs.dev/latest/bookmarks/)
