# Prefer 100-Column Prose Wrap

## Metadata

- Name: `Prefer 100-Column Prose Wrap`
- ID: `prefer-100-column-prose-wrap`
- Summary: Wrap Markdown prose and Markdown-bearing doc comments around 100 columns as a
  maintainer readability preference. The exact number is subjective, but it balances source
  reading, monospace density, review diffs, and common screen sizes better than 80 or 120 columns.
- Status: `draft`
- Audience: `both`
- Topics: `documentation, markdown, rustdoc, review`
- Tags: `documentation, local-conventions, reviewability, rustdoc`
- Related: `DOCS-KEEP-MARKDOWN-LINTABLE, RUST-FORMAT-DOCS-AND-COMMENTS-CONSISTENTLY`

## Problem

I prefer 100-column prose wrap because 80 columns makes Markdown prose and doc comments choppy, while
120 columns often breaks laptop and GitHub side-by-side review. Markdown is read in editors,
terminals, generated diffs, GitHub review panes, and doc comments before it is rendered. In those
places, line width affects whether prose feels natural to read or noisy to review.

Prefer hard-wrapped and reflowed Markdown over unwrapped paragraphs. Unwrapped Markdown leaves each
editor, terminal, renderer, and review surface to choose a different visual wrap, which makes source
review less stable. A deliberate line length gives diffs a meaningful shape: paragraph edits,
awkward phrasing, overlong examples, and accidental formatting drift become easier to see.

The 80-column default often leaves too little room after Markdown list markers, indentation,
blockquote markers, Rustdoc prefixes, or link syntax. At the other end, 120 columns can feel good on
a wide editor or 4k display, but it leaves too little margin for review gutters, split panes, and
common laptop screens.

## Preferred Move

Hard-wrap and reflow Markdown prose and Markdown-bearing doc comments around 100 columns. Treat 100
as a preference with rationale, not as proof that every longer line is wrong. Keep the source
readable first, then let the linter enforce the mechanical boundary.

At 100 columns, monospace prose usually keeps one idea together while leaving room for split panes,
review gutters, and diff markers.

## Configuration

Encode the preference with markdownlint rule `MD013` / `line-length` when a project uses
`markdownlint-cli2`.

```yaml
config:
  line-length:
    line_length: 100
    tables: false
```

Common `MD013` choices:

- `line_length: 100`: Set the prose width to the preferred source-reading width.
- `tables: false`: Exclude tables when aligned columns communicate structure better than wrapping.
- `code_blocks`: Keep enabled for prose-like examples, shell snippets, and examples expected to fit
  normal review panes. Disable it when generated output, URLs, command transcripts, API payloads, or
  language examples become less faithful when wrapped.
- `code_block_line_length`: Use a separate code-block width when examples need a different limit
  from prose.
- `heading_line_length` or `headings: false`: Use only for reference-style headings that must
  preserve long names, commands, API paths, or generated titles.

## Tradeoff

This is a maintainer preference, not a universal typography rule. Rendered user-facing text has
different accessibility constraints, and UI layouts should not inherit source-file line length as a
content measure. Code blocks, URLs, generated references, aligned tables, and examples may need
local exceptions.

Do not churn existing prose only to satisfy the number. Apply the preference when editing nearby
text, writing new Markdown, formatting doc comments, or preparing documentation for review. Follow
the repo's configured markdownlint line length when it differs from this pattern.

## Agent Instruction

Hard-wrap and reflow Markdown prose and Markdown-bearing doc comments near 100 columns unless local
config says otherwise. Preserve readable source diffs, avoid churn-only reflow, and report any
intentional exceptions such as tables, generated text, long links, or examples.

## Examples

Bad: a strict 80-column wrap makes a normal explanatory sentence feel chopped up in source.

```markdown
Wrap Markdown prose and Markdown-bearing doc comments around the local
prose line length so source readers can scan the explanation without
unnecessary visual breaks.
```

Good: the same sentence at about 100 columns keeps the idea together while staying diff-friendly.

```markdown
Wrap Markdown prose and Markdown-bearing doc comments around the local prose line length so source
readers can scan the explanation without unnecessary visual breaks.
```

Bad: a 120-column line reads comfortably only when the review surface is wide enough.

<!-- markdownlint-disable MD013 -->

```markdown
Wrap Markdown prose and Markdown-bearing doc comments around the local prose line length so source readers can scan the explanation without unnecessary visual breaks.
```

<!-- markdownlint-enable MD013 -->

Good: allow a wide table when wrapping would hide the columns.

```markdown
| Field                  | Meaning                                                     |
| ---------------------- | ----------------------------------------------------------- |
| `default_branch_alias` | Local jj alias that makes branch-target examples portable.  |
```

## References

| Source                 | Use       | Note                                                                 |
| ---------------------- | --------- | -------------------------------------------------------------------- |
| [markdownlint MD013]   | `adapts`  | Line length is configurable, so the repo can encode its own width.   |
| [rustfmt `max_width`]  | `adapts`  | Rust formatting has a stable 100-column default for source lines.    |
| [WCAG visual text]     | `differs` | Rendered text accessibility constraints are not source diff widths.  |

[markdownlint MD013]: https://github.com/DavidAnson/markdownlint/blob/main/doc/md013.md
[rustfmt `max_width`]: https://rust-lang.github.io/rustfmt/?search=&version=v2.0.0-rc.2
[WCAG visual text]: https://www.w3.org/WAI/WCAG21/Understanding/visual-presentation.html
