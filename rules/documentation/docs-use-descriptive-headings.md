# Docs Use Descriptive Headings

## Metadata

- ID: `DOCS-USE-DESCRIPTIVE-HEADINGS`
- Legacy ID: `R-0525`
- Status: `reviewed`
- Domain: `documentation`
- Depth: `compact`

## Rule

Use headings that describe the section content instead of slogan-like instructions.

## Why

Headings are navigation. A heading like "Choose the narrowest rule family first" sounds forceful but
does not name the kind of information below it. Readers and agents need to infer whether the section
is about rule domains, usage flow, review policy, or setup. A descriptive heading such as "Find rules
by work area" gives the page a clearer scan path.

## Helps

- Makes pages easier to skim, search, link, and navigate non-linearly.

## Limits

Imperative headings can work in procedures, checklists, and tutorials where the section is literally
one step in a task. Prefer descriptive headings on reference pages, indexes, landing pages, and
review guidance where the reader is choosing where to go next.

## Agent Instruction

Use descriptive headings for reference and landing pages so the heading names the content or decision
area, not a slogan-like instruction.

## Mechanisms

Supported by heading review, table-of-contents review, rendered-page inspection, and feedback that
asks what a reader can learn from the heading alone.

## References

- [Diataxis: reference](https://diataxis.fr/reference/)
- [Rustdoc: how to write documentation](https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html)
