# Run Rustdoc Quality Pass

## Metadata

- Name: `Run Rustdoc Quality Pass`
- ID: `run-rustdoc-quality-pass`
- Summary: Use a bounded checklist when raising a Rust crate's public documentation. The pass
  should teach the crate model, document public contracts, place examples where they prove real use,
  keep documentation layers aligned, and validate Rustdoc as code.
- Status: `reviewed`
- Audience: `both`
- Topics: `rust, rustdoc, documentation, examples, validation`
- Tags: `rust, rustdoc, documentation, public-api, examples`
- Related: `rust-teach-crate-from-crate-root, rust-write-rustdoc-as-api-contract,
  rust-avoid-vague-docs-and-generic-examples, rust-keep-rustdoc-and-readme-examples-aligned,
  rust-docs-validation, rust-keep-pre-release-compatibility-intentional`

## Problem

Rustdoc quality can be easy to name and hard to apply consistently. A pass that only adds
`# Examples` sections can miss the crate model, lifecycle, ownership, invariants, and README drift.
A pass that treats every public accessor as needing a standalone doctest can also make docs noisy
without teaching more.

Large modules and state-heavy public types add another failure mode: each item can have acceptable
local docs while the rendered Rustdoc page still gives readers no map. Users should not have to
scroll every public item to learn which type owns state, which method mutates it, which adapter
renders it, and where the canonical explanation lives.

Experimental crates add another pressure: they still need contract-quality docs for today's
behavior, but those docs must not imply stable API promises the crate has not made.

## Preferred Move

Run a bounded Rustdoc quality pass before handoff. Check the crate as a documentation stack, not
only as isolated item comments:

- README: entry point, setup, commands, support status, and links.
- Crate Rustdoc: user model, lifecycle, first working examples, primary types, feature flags, and
  related crates.
- Module Rustdoc: compact table of contents for the module's public concepts and ownership
  boundaries.
- Item Rustdoc: caller-facing contracts, ownership, invariants, method groups, errors, panics,
  safety, lifecycle, side effects, and compatibility expectations.
- `examples/`: runnable integration using the crate the way users should use it.
- ADR: accepted tradeoff and rejected alternatives.
- PRD: problem, scope, and future decisions.

Use this checklist for the Rustdoc pass:

- The crate root teaches purpose, lifecycle, primary types, primary import paths, and related
  crates, plus what experimental users can rely on today.
- Public modules with several public concepts include short `use this when` or item-map bullets so
  readers can choose the right type, function, method, or submodule without scanning every item.
- Public types explain invariants, ownership, construction, and relationships to neighboring types.
- Public state-machine types, builder-style structs, and other method-heavy types group related
  methods by caller task: lifecycle, inspection, mutation, rendering, dispatch, or integration.
- Public enums document each variant's caller-facing meaning.
- Unsafe functions state complete caller obligations in `# Safety`. Unsafe operations explain why
  those obligations hold locally or link to the precise invariant owned by the surrounding type or
  module.
- Safe wrappers describe the invariant they enforce. If safe callers can violate the safety
  argument, the docs identify the soundness boundary rather than turning current use into proof.
- Repeated low-level safety contracts are consolidated at their nearest stable owner; local sections
  remain only for additional obligations or operation-specific reasoning.
- Items link to the canonical module, type, trait, or method when another page owns the fuller
  explanation; adapters, renderers, event variants, and helpers should not duplicate the shared
  module contract.
- Important public API names use intra-doc links when the link improves navigation or clarifies
  ownership, without linking every repeated mention.
- Constructors, state transitions, fallible methods, side-effecting methods, and lifecycle
  boundaries have local examples or links to nearby richer examples.
- Public item examples sit under `# Example` or `# Examples` unless an existing heading clearly
  introduces the example.
- Related accessors use grouped examples or prose when standalone examples would repeat obvious
  syntax.
- README, crate Rustdoc, item Rustdoc, examples, and doctests use the same import paths, feature
  assumptions, and lifecycle.
- Experimental crates say what is experimental, what may change, and what users can rely on today.
- `cargo doc --document-private-items` is used when the pass also claims maintainer-facing coverage
  of private helpers and internal contracts; public Rustdoc alone does not prove that scope.
- `RUSTDOCFLAGS='-D warnings -D rustdoc::broken_intra_doc_links' cargo doc --workspace --no-deps`
  passes for workspace docs when the crate is in a workspace.
- `rustdoc::redundant_explicit_links` warnings are addressed by simplifying links whose labels
  already resolve.
- `cargo test --doc` or `cargo test --workspace` runs the relevant doctests.

## Tradeoff

Do not turn the checklist into a requirement for one doctest on every public accessor. Prefer local
examples for behavior that teaches construction, validation, state changes, fallibility, side
effects, lifecycle, feature flags, or integration. Prefer grouped examples for related accessors
whose individual syntax is obvious but whose relationship matters. Link to crate-level or runnable
examples when repeating the method-level example would drift.

Do not make every mention of every public type an intra-doc link. Link concepts, methods, variants,
and canonical docs when the reader needs a next hop; leave repeated nearby mentions plain when links
would become visual noise.

Tiny internal crates can use a shorter pass, but public crates should still teach the main model and
validate examples. Experimental status should narrow stability claims, not weaken current-behavior
contracts.

## Agent Instruction

When improving Rust crate docs, run a bounded Rustdoc quality pass across crate root, module maps,
public item contracts, method groups, canonical links, example placement, README/Rustdoc/example
alignment, experimental caveats, safety-contract ownership, and doc validation. Include private
items when the requested coverage extends to internal source, prefer grouped or linked examples for
simple accessors, and report which checks ran.

## Examples

Bad: every accessor gets a standalone doctest while the module page still lacks a map.

```rust
//! Palette types.

/// Stores palette state.
///
/// ```
/// let state = PaletteState::new();
/// ```
pub struct PaletteState;
```

Good: the module explains the public surface, the type groups methods by caller task, and individual
items link back to the canonical explanation instead of repeating it.

```rust
//! Command-palette state and rendering.
//!
//! Use this module when:
//!
//! - [`PaletteState`] owns selection, filtering, and preview state.
//! - [`ActionInvocation`] reports app-owned dispatch requests.
//! - [`render_palette`] turns state into a Ratatui view.

/// Interactive command-palette state.
///
/// Method map:
///
/// - Lifecycle: [`Self::new`], [`Self::reset`]
/// - Inspection: [`Self::selected`], [`Self::preview`]
/// - Mutation: [`Self::select_next`], [`Self::filter`]
///
/// See the [`palette`](crate::palette) module for the full lifecycle.
pub struct PaletteState;
```

## References

| Source                                             | Use        | Note                                                    |
| -------------------------------------------------- | ---------- | ------------------------------------------------------- |
| [Rust API Guidelines: C-CRATE-DOC][crate-doc]      | `supports` | Crate-level docs should be thorough and example-led.    |
| [Rust API Guidelines: C-EXAMPLE][item-examples]    | `adapts`   | Item examples should be useful and applied with limit.  |
| [Rustdoc: How to write documentation][rustdoc]     | `supports` | Rustdoc front pages and items should teach purpose.     |
| [Rustdoc: Linking to items by name][links]         | `supports` | Intra-doc links create navigable public API docs.       |
| [Rustdoc: Lints][rustdoc-lints]                    | `supports` | Rustdoc lints check links and redundant explicit links. |
| [Rustdoc: Documentation tests][doctests]           | `supports` | Public examples can be validated as doctests.           |
| [Diátaxis: How to use Diátaxis][diataxis-workflow] | `adapts`   | Documentation work benefits from separating doc jobs.   |

[crate-doc]: https://rust-lang.github.io/api-guidelines/documentation.html#c-crate-doc
[diataxis-workflow]: https://diataxis.fr/how-to-use-diataxis/
[doctests]: https://doc.rust-lang.org/rustdoc/write-documentation/documentation-tests.html
[item-examples]: https://rust-lang.github.io/api-guidelines/documentation.html#c-example
[links]: https://doc.rust-lang.org/rustdoc/write-documentation/linking-to-items-by-name.html
[rustdoc]: https://doc.rust-lang.org/rustdoc/how-to-write-documentation.html
[rustdoc-lints]: https://doc.rust-lang.org/rustdoc/lints.html
