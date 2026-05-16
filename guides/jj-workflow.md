# JJ Workflow

## Metadata

- Name: `JJ Workflow`
- ID: `jj-workflow`
- Summary: JJ workflow guidance covers source-control inspection, reviewable changes, descriptions,
  bookmarks, publication, and recovery in jujutsu repositories. It keeps agents and maintainers
  thinking in jj changes and operations instead of Git-shaped habits.
- Status: `reviewed`
- Audience: `both`
- Topics: `jj, vcs, changes, bookmarks, recovery, github`
- Tags: `vcs-jj, change-shape, reviewability, tooling`
- Related: `jj-topology-is-repo-role-dependent, jj-agent-workflow, vcs-jj-as-source-of-truth`

This guide covers jujutsu workflow preferences for source-control inspection, reviewable changes,
commit descriptions, and publication.

Use this guide with [Software Change Preferences](software-change-preferences.md). The goal is not
to teach all of jj; it is to keep local work reviewable, recoverable, and aligned with jj's change
model.

## Core Preference

In a jj repo, think in changes, revisions, workspaces, bookmarks, and operations. Do not translate
the workflow into Git habits unless the task is actually about Git transport.

Optimize for:

### Local State

- Fresh changes for separate review units.
- Clear descriptions early in meaningful editing work.
- Sequential source-control mutations.
- Scoped inspection before reshaping history.
- Pager behavior configured for non-interactive tooling.
- Shell quoting that preserves the exact arguments jj receives.

### Publication And Recovery

- Bookmarks only when something needs a stable publication name.
- Operation-log recovery instead of destructive cleanup.

## Inspect Before Changing

Start by understanding the current working copy and stack:

```bash
jj --no-pager status
jj --no-pager log -r 'main..@'
jj --no-pager diff --git --stat
```

For agent tooling, prefer configuring `JJ_PAGER=cat` once so jj output is never trapped in a pager.
Use `--no-pager` as the per-command fallback when the environment is not configured or when
supporting older jj versions. Do not run jj mutations in parallel.

Use [Preserve Unowned Work][preserve-work] when the working copy contains changes you did not make,
and read `--help` before mutating the repo when command shape is unfamiliar.
Use [Inspect State Before Mutating][inspect-state], [Configure JJ Pager][jj-pager-rule], and
[Run JJ Mutations Sequentially][sequential-mutations] when setting up agent-safe jj inspection.

Most jj commands snapshot local file changes into the current change before they run. This is useful
for agents because ordinary inspection and workflow commands create operation-log points without
leaving the current change. Before risky reshaping, it can be reasonable to run a harmless jj
inspection command intentionally so there is a clean operation to restore to later.

Use [Create Operation Log Point Before Reshaping][op-point] before risky stack edits.

When Codex or another agent needs to interpret patch text, prefer Git-formatted diffs:

```bash
jj diff --git
jj show --git <revision>
```

Jujutsu's default diff format is useful, but Git-formatted diffs are more in-distribution for coding
agents, review tools, and patch-oriented reasoning. Use the default format when a human specifically
wants jj's native presentation.

Use [Use Git Formatted Diffs For Agents][git-diffs] when patch interpretation depends on agent,
review, or diff-tool compatibility.

## Reviewable Work

Use a fresh change for a separate review unit:

```bash
jj new
jj describe --message "Add focused workflow guide"
```

Use the current working copy only when the new edit is clearly part of the same atomic change.
Prefer `jj new` before exploratory follow-up work; it is usually easier to squash or absorb a small
related child later than to split an overloaded change after unrelated edits accumulate.

When the new change belongs before or after existing work, use explicit insertion:

```bash
jj new --insert-before <revision>
jj new --insert-after <revision>
```

Use `jj workspace add` only when the task needs a second filesystem checkout: long-running
validation, a clean comparison tree, a separate sparse view, or parallel local work that cannot
share one working directory. Use `jj new` when the task only needs another review lane in the same
checkout.

For safe alternatives to an existing change, consider `jj duplicate` instead of rewriting the
original or rebuilding the context manually. Keep sibling candidates separately described until the
choice is clear.

Use [JJ New For Review Lanes][jj-new-rule], [Workspace Add For Second Checkouts][workspace-add], and
[Duplicate For Alternative Candidates][duplicate-candidates] when choosing the local shape of
parallel or follow-up work.

## Describe The Change

Set a description early for real edits, and keep it aligned with the final scope. Use
[Commit Messages For History][commit-history] for both jj descriptions and published commits.

For multi-line descriptions, use real newlines:

```bash
jj describe --message "Add jj workflow guide

Capture the repo's jj-first source-control preferences as a compact
canonical guide. Link it from top-level docs so future agent snippets
can reference the guide instead of duplicating the full workflow."
```

Do not pass escaped `\n` sequences unless you have verified the shell expands them before jj
receives the argument. When exact formatting matters, prefer `--stdin`.

Use [Quote Revsets And Shell Syntax][quote-syntax] when revsets, bookmark names, descriptions, or
shell-sensitive characters appear in agent-generated commands.

## Preserve Shell Arguments

Be careful with shell escapes in agent-generated commands. It is easy to write a command that looks
right in Markdown or JSON but passes different bytes to the shell or to jj.

Prefer command shapes where the final shell argument is unambiguous:

- Use single quotes around revsets and filesets unless interpolation is intentional.
- Quote revset functions such as `trunk()`, `root()`, `all()`, and `ancestors(@)`; unquoted
  parentheses can be interpreted by the shell before jj sees them.
- Use real newlines for multi-line descriptions, not escaped `\n` text.
- Prefer `--stdin` for descriptions or input where exact formatting matters.
- Avoid relying on shell-specific escape expansion unless the shell behavior is the point.
- Inspect the stored description or command result when quoting was non-trivial.

Example:

```bash
jj describe --stdin <<'EOF'
Add jj workflow guide

Capture the repo's jj-first source-control preferences as a compact
canonical guide.
EOF
jj log -r @ -T 'description'
```

## Small Changes

Keep one coherent purpose per change. Use child changes for follow-up chunks and reshape later only
when the relationship is clear.

Common choices:

- `jj new`: start a new review unit.
- `jj squash`: fold an obviously inseparable follow-up into its parent.
- `jj absorb`: move small fixups into the changes that introduced the touched lines.
- `jj split`: split an overloaded change deliberately.
- `jj duplicate`: try an alternative without disturbing the original.
- `jj restore`: undo file content in the current change.
- `jj revert`: create an inverse change that preserves history.

Avoid editor-driven or interactive jj flows unless the task needs them and the workflow is
deterministic enough to report cleanly.

Do not rely on default revision selection for mutating commands when the target matters. Spell out
the intended revision, destination, fileset, bookmark, or remote instead of assuming `@`, the
nearest parent, or the closest bookmark is the right target.

If repeated `status`, `show`, or near-identical failed commands are not adding information, stop and
localize the state with the graph, operation log, help output, or the relevant workspace/bookmark
inspection command before mutating again.

Commands that can prompt or open an editor by default need special care in agent tooling:

| Command       | Interactive risk                                   | Non-interactive shape                           |
| ------------- | -------------------------------------------------- | ----------------------------------------------- |
| `jj describe` | Opens an editor without `--message` or `--stdin`.  | Use `--message` or `--stdin`.                   |
| `jj split`    | Opens a diff editor when no filesets are provided. | Provide filesets and `--message`.               |
| `jj squash`   | Can prompt to combine non-empty descriptions.      | Use `--message` or `--use-destination-message`. |
| `jj commit`   | Acts like describe plus new; may need a message.   | Use `--message`; avoid `--interactive`.         |

Read `--help` before using a reshaping command in a script or agent run. Prefer explicit revsets,
filesets, and messages over prompts that require a human editor.

Treat `jj next` and `jj prev` as mutating navigation unless you have confirmed the installed
non-mutating form you intend to use.

For file state, scope commands to the intended paths. Do not run broad `jj file track` to pick up
all untracked files. Add ignore rules before `jj file untrack`, keep the file on disk when that is
the intended outcome, and verify final tracked state instead of trusting one warning line.

Use [Avoid Interactive JJ In Agent Work][avoid-interactive], [Name Exact JJ Mutation
Targets][exact-targets], [Stop Repeated JJ Retries And Localize State][stop-retries], and [Scope JJ
File Tracking][scope-files] when command shape or file state could surprise the working copy.

## Publish With Bookmarks

Bookmarks are publication names, not the current branch. There is no active bookmark in jj. Create
or move a bookmark when a remote branch or review boundary needs a stable name.

For this repo, personal bookmark names should use the `joshka/` prefix unless the task is updating
the shared `main` bookmark.

Typical reviewed-stack publication to `main`:

```bash
jj bookmark set main -r @-
jj git push --remote origin --bookmark main
```

Use `--dry-run` when the remote move is surprising, broad, or not already approved. For a routine
reviewed-stack push, avoid the extra dry-run round trip once local state and publication intent are
clear. Ask before publishing unless the repo policy explicitly allows the push.

For GitHub CLI handoff, keep jj as the source of truth first. Inspect bookmarks and remotes, publish
only the intended bookmark, then pass explicit `gh` parameters such as `--repo`, `--head`, and
`--base` when topology is non-trivial.

Use [Dry Run Surprising Publication][dry-run], [Confirm GitHub Remote Topology][github-topology],
and [Make GitHub Handoff Explicit][github-handoff] before moving public review state.

## Track Remotes Explicitly

Jujutsu stores last-seen remote bookmark positions, such as `main@origin`, and a local bookmark can
track one or more remote bookmarks with the same name. Tracking metadata helps jj reconcile local
and remote bookmark movement, but it does not replace explicit publication intent.

Inspect remote state before remote-sensitive work:

```bash
jj bookmark list --all-remotes
jj git remote list
```

When tracking or untracking a bookmark, prefer the syntax shown by the installed jj version's
`--help`. This area is version-sensitive: recent jj releases deprecated some old
`<bookmark>@<remote>` command-argument forms in favor of separate `--remote` flags, while the
`bookmark@remote` notation still expresses a remembered remote bookmark position and is expected to
remain useful because it matches user intent. Do not silently rewrite a user's remote target; verify
the installed command shape before changing tracking.

When a bookmark name exists on multiple remotes, include the remote explicitly:

```bash
jj bookmark track main --remote origin
jj bookmark untrack main --remote origin
```

Fetch from the remote that owns the state you are reasoning about:

```bash
jj git fetch --remote upstream
jj bookmark list --all-remotes
```

GitHub CLI defaults can affect remote naming, so confirm the topology before publishing. For
example, `gh repo fork` normally makes the fork `origin` and renames an existing `origin` to
`upstream`; in that layout, `origin` is usually the writable fork and `upstream` is usually the
canonical source repository. Confirm with `jj git remote list` instead of assuming the names.

Repair remotes, fetch configuration, push configuration, `trunk()`, and tracked bookmarks together
when a host tool has changed repo topology. Do not let a forge command infer targets from stale jj
topology.

Use [Track Remotes Explicitly][track-remotes], [Treat Bookmark Remote Syntax As Version
Sensitive][bookmark-syntax], [Match JJ Topology To Repo Role][match-topology], and [Repair Remote
Topology Coherently][repair-topology] when remote names, tracked bookmarks, or host-tool defaults
shape publication.

## Git Transport Boundary

In a jj repo, do not use Git for normal local workflow. Use Git only when the remaining operation is
transport-level behavior that jj does not cover in the current workflow, and keep jj as the source
of truth.

Prefer jj-native inspection and mutation commands:

- `jj status`, not `git status`.
- `jj diff`, not `git diff`.
- `jj log`, not `git log`.
- `jj bookmark`, not local branch commands.
- `jj git fetch` and `jj git push` for Git remotes.

Use [JJ As Source Of Truth][jj-source] and [Do Not Fall Back To Git For JJ Issues][no-git-fallback]
when deciding whether a command belongs in jj or Git.

## Recover Deliberately

Do not use destructive cleanup commands to get unstuck. Inspect the operation log and recover through
jj's model:

```bash
jj op log
jj op show <operation>
jj op restore <operation>
```

When a risky sequence is about to start, note the current operation or create a fresh one with a
harmless command such as `jj status`. That gives `jj op restore` a clear target if the reshape goes
wrong.

Use [Preserve Unowned Work][preserve-work] before undoing, abandoning, restoring, or squashing
anything that might contain someone else's edits.

Use `jj evolog` when the question is about the evolution of one rewritten change. Use `jj op log`
when the question is about repository operations or recovering from a mistaken operation. Do not
restore the whole repository operation when a narrow change-evolution repair is enough.

Use broad operation restore only after inspecting the operation and confirming that later intended
work will not be discarded. Ask for confirmation when a recovery could rewrite or discard unrelated
work.

If a workspace is stale because another workspace rewrote its working-copy commit, inspect workspace
state and use the jj workspace recovery path instead of cloning, resetting, or mutating the stale
checkout blindly.

Use [Recover With Operation Log][recover-oplog] and [Use Evolog And Operation Log][evolog-oplog]
when recovery needs jj history instead of destructive cleanup.

## Agent Snippet

For copyable `AGENTS.md` guidance, use [Jujutsu Agent Instructions][jj-snippet].

## Related Guidance

Use [JJ Topology And Source Control Rules][vcs-rules] for compact jj and publication instructions.
Use [JJ Topology Is Repo Role Dependent][jj-topology] for the reasoning behind owned, maintainer,
and forked remote layouts. Use [JJ Agent Workflow][jj-agent-workflow] for noninteractive jj
configuration and agent-safe command shapes.

## Review Questions

### Local Change

- Is this a separate review unit that deserves `jj new`?
- Does this task need another filesystem checkout, or only another change lane?
- Does the working-copy change have one coherent purpose?
- Is the description useful as future history?
- Did source-control mutations run sequentially?
- Did mutating commands name the exact revision, destination, bookmark, remote, or fileset?
- Are unowned edits preserved?

### Publication

- Does a bookmark need to move, or is this still local-only work?
- Are forge commands receiving explicit repo/head/base values when inference is risky?
- Was publication intent explicit, and was any high-risk remote move dry-run first?

## References

| Source                    | Use        | Note                                                     |
| ------------------------- | ---------- | -------------------------------------------------------- |
| [Working copy][working]   | `supports` | jj models the working copy as a commit that snapshots.   |
| [Bookmarks][bookmarks]    | `supports` | Bookmarks are named revision pointers, not branches.     |
| [GitHub workflow][github] | `adapts`   | jj publishes Git-backed review work through bookmarks.   |
| [jj changelog][changelog] | `supports` | Bookmark tracking syntax is currently version-sensitive. |
| [gh repo fork][gh-fork]   | `supports` | GitHub CLI may rename `origin` and `upstream` remotes.   |
| [JJ_PAGER PR][jj-pager]   | `adapts`   | Agent tooling can configure jj-specific pager behavior.  |
| [CLI reference][cli]      | `supports` | Command behavior and push safety checks.                 |

[bookmarks]: https://docs.jj-vcs.dev/latest/bookmarks/
[avoid-interactive]: ../rules/vcs/vcs-avoid-interactive-jj-in-agent-work.md
[bookmark-syntax]: ../rules/vcs/vcs-treat-bookmark-remote-syntax-as-version-sensitive.md
[changelog]: https://github.com/jj-vcs/jj/blob/main/CHANGELOG.md
[cli]: https://docs.jj-vcs.dev/latest/cli-reference/
[commit-history]: ../patterns/commit-messages-for-history.md
[dry-run]: ../rules/vcs/vcs-dry-run-surprising-publication.md
[duplicate-candidates]: ../rules/vcs/vcs-duplicate-for-alternative-candidates.md
[evolog-oplog]: ../rules/vcs/vcs-use-evolog-and-operation-log.md
[exact-targets]: ../rules/vcs/vcs-name-exact-jj-mutation-targets.md
[gh-fork]: https://cli.github.com/manual/gh_repo_fork
[github]: https://docs.jj-vcs.dev/latest/github/
[github-handoff]: ../rules/vcs/vcs-make-github-handoff-explicit.md
[github-topology]: ../rules/vcs/vcs-confirm-github-remote-topology.md
[git-diffs]: ../rules/vcs/vcs-use-git-formatted-diffs-for-agents.md
[inspect-state]: ../rules/vcs/vcs-inspect-state-before-mutating.md
[jj-agent-workflow]: ../mechanisms/jj-agent-workflow.md
[jj-pager]: https://github.com/jj-vcs/jj/pull/9395
[jj-pager-rule]: ../rules/vcs/vcs-configure-jj-pager.md
[jj-new-rule]: ../rules/vcs/vcs-jj-new-for-review-lanes.md
[jj-snippet]: ../snippets/agents/jj.md
[jj-source]: ../rules/vcs/vcs-jj-as-source-of-truth.md
[jj-topology]: ../principles/jj-topology-is-repo-role-dependent.md
[match-topology]: ../rules/vcs/vcs-match-jj-topology-to-repo-role.md
[no-git-fallback]: ../rules/vcs/vcs-do-not-fall-back-to-git-for-jj-issues.md
[op-point]: ../rules/vcs/vcs-create-operation-log-point-before-reshaping.md
[preserve-work]: ../patterns/preserve-unowned-work.md
[quote-syntax]: ../rules/vcs/vcs-quote-revsets-and-shell-syntax.md
[recover-oplog]: ../rules/vcs/vcs-recover-with-operation-log.md
[repair-topology]: ../rules/vcs/vcs-repair-remote-topology-coherently.md
[scope-files]: ../rules/vcs/vcs-scope-jj-file-tracking.md
[sequential-mutations]: ../rules/vcs/vcs-run-jj-mutations-sequentially.md
[stop-retries]: ../rules/vcs/vcs-stop-repeated-jj-retries-and-localize-state.md
[track-remotes]: ../rules/vcs/vcs-track-remotes-explicitly.md
[vcs-rules]: ../rules/vcs/README.md
[workspace-add]: ../rules/vcs/vcs-workspace-add-for-second-checkouts.md
[working]: https://docs.jj-vcs.dev/latest/working-copy/
