# VCS Dry Run Surprising Publication

## Metadata

- ID: `VCS-DRY-RUN-SURPRISING-PUBLICATION`
- Name: `Dry Run Surprising Publication`
- Summary: Use dry-run for ambiguous or surprising remote publication, not every routine push.
  Extra verification pays off when remotes, bookmarks, force-like updates, or PR bases are unclear.
- Status: `reviewed`
- Domain: `vcs`
- Depth: `compact`

## Rule

Use dry-run for surprising or ambiguous remote publication, not routine latency.

## Why

Dry-run is most valuable when publication would be surprising: ambiguous remote, new bookmark,
force-like update, fork topology, or unclear PR base. Using it for every routine push adds latency
without improving safety.

## Helps

- Applies extra verification where publication risk is real.

## Limits

Skip dry-run for already-understood routine publication. Use it when the command would create, move,
or publish something the user has not seen.

## Agent Instruction

Use dry-run for surprising jj publication: ambiguous remote, new bookmark, force-like update, fork
topology, or unclear PR base.

## Mechanisms

Supported by dry-run flags, explicit bookmark names, remote inspection, PR base/head checks, and
publication summaries.

## References

- [Principle: JJ Topology Is Repo Role
  Dependent](../../principles/jj-topology-is-repo-role-dependent.md)
- [Jujutsu docs: working copy](https://docs.jj-vcs.dev/latest/working-copy/)
- [Jujutsu docs: bookmarks](https://docs.jj-vcs.dev/latest/bookmarks/)
