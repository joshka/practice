# VCS Avoid Interactive JJ In Agent Work

## Metadata

- ID: `VCS-AVOID-INTERACTIVE-JJ-IN-AGENT-WORK`
- Name: `Avoid Interactive JJ in Agent Work`
- Summary: Use noninteractive jj commands with explicit messages, targets, and files in agent work.
  Interactive editors, prompts, merge tools, and pagers can hang unattended sessions.
- Status: `reviewed`
- Domain: `vcs`
- Tags: `vcs-jj, agent-workflow, tooling, automation`
- Related: `boundary-make-exec-tools-noninteractive, vcs-run-jj-mutations-sequentially`

## Rule

Avoid interactive-by-default jj commands in unattended agent work.

## Why

Interactive jj commands can open editors, prompts, merge tools, or pagers that unattended agents
cannot handle reliably. Noninteractive commands make the intended message, target, and files
explicit and avoid hanging the session.

## Helps

- Keeps agent source-control operations repeatable and reviewable.

## Limits

Interactive tools are fine for humans. Agents should use them only when the workflow explicitly
provides the required input or the user asks for that interaction.

## Agent Instruction

Avoid interactive-by-default jj commands in unattended agent work because interactive jj commands can
open editors, prompts, merge tools, or pagers that unattended agents cannot handle reliably.

## Mechanisms

Supported by `--message`, explicit revsets, path arguments, `--no-pager`, configured editors, and
reading `jj help` before unfamiliar commands.

## References

- [Principle: JJ Topology Is Repo Role
  Dependent](../../principles/jj-topology-is-repo-role-dependent.md)
- [Jujutsu docs: working copy](https://docs.jj-vcs.dev/latest/working-copy/)
- [Jujutsu docs: bookmarks](https://docs.jj-vcs.dev/latest/bookmarks/)
