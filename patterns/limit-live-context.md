# Limit Live Context

## Metadata

- Name: `Limit Live Context`
- ID: `limit-live-context`
- Status: `reviewed`
- Audience: `both`
- Topics: `rust, readability, decomposition`
- Related: `reader-locality, chunk-statements, move-declaration-and-initialization-together`

## Problem

Long functions and modules make every earlier fact a possible influence on every later line. A
reader trying to understand one block must keep prior variables, flags, partial calculations,
side effects, and ordering assumptions in mind because any of them might still matter.

This cost grows faster than line count. The problem is not only that the code is long; it is that the
reader cannot tell which facts are still live.

## Preferred Move

Shrink the active set of facts a reader must hold at once. Keep scopes narrow, end temporary state
quickly, group phases into visible blocks, and extract a named helper when a block has a clear
purpose and limited interaction with the surrounding code.

When reading a later block, a maintainer should be able to answer: "Which earlier facts can affect
this?" If the answer is "most of the function," reduce the live context before adding more behavior.

## Tradeoff

Extraction can make context worse when it hides weak facts behind a vague name or forces the reader
to jump between files. Prefer local blocks, smaller scopes, and explaining names until a helper has
a strong contract.

Some algorithms genuinely require a large shared working set. In those cases, make the shared state
explicit, document the invariant, and keep unrelated work outside the algorithm.

## Agent Instruction

Before editing a long function or module, identify the facts that remain live across the area being
changed. Narrow scopes, split phases, or extract a helper when that reduces the live context needed
to review the change. Do not extract weak helpers only to reduce line count.

## Examples

Bad: later code can depend on any earlier mutation, so the reviewer has to keep the whole function
active while reading the final decision.

```rust
let mut score = base_score(pattern);
let mut has_examples = false;
let mut has_public_docs = false;

for example in pattern.examples() {
    has_examples = true;
    score += example.weight();
}

for doc in pattern.docs() {
    if doc.visibility().is_public() {
        has_public_docs = true;
        score += 2;
    }
}

if has_examples && has_public_docs && score >= policy.publish_score() {
    publish(pattern)?;
}
```

Good: each decision names the fact it contributes, and the final condition has a small active set.

```rust
let example_score = score_examples(pattern.examples());
let doc_score = score_public_docs(pattern.docs());
let publish_score = base_score(pattern) + example_score + doc_score;

let publishable = example_score.has_examples()
    && doc_score.has_public_docs()
    && publish_score >= policy.publish_score();

if publishable {
    publish(pattern)?;
}
```

## References

| Source                                                                              | Use      | Note                                                          |
| ----------------------------------------------------------------------------------- | -------- | ------------------------------------------------------------- |
| [Code That Fits in Your Head: Heuristics for Software Engineering, Ch. 6][ctfh-ch6] | `adapts` | Memory limits should shape code organization.                 |
| [Code That Fits in Your Head: Heuristics for Software Engineering, Ch. 7][ctfh-ch7] | `adapts` | Decomposition helps when it reduces the context in view.      |
| [Tidy First, Ch. 11][tidy-ch11]                                                     | `adapts` | Separating phases can reveal a routine's internal shape.      |
| [Tidy First, Ch. 12][tidy-ch12]                                                     | `adapts` | Extract helpers when a block has a purpose and small surface. |

[ctfh-ch6]: https://www.oreilly.com/library/view/code-that-fits/9780137464302/ch06.xhtml
[ctfh-ch7]: https://www.oreilly.com/library/view/code-that-fits/9780137464302/ch07.xhtml
[tidy-ch11]: https://www.oreilly.com/library/view/tidy-first/9781098151232/ch11.html
[tidy-ch12]: https://www.oreilly.com/library/view/tidy-first/9781098151232/ch12.html
