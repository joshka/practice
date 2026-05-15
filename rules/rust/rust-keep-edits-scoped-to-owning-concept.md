# Rust Keep Edits Scoped To Owning Concept

## Metadata

- ID: `RUST-KEEP-EDITS-SCOPED-TO-OWNING-CONCEPT`
- Legacy ID: `none`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Keep Rust edits scoped to the owning concept.

## Why

Rust crates often make it easy to touch nearby modules, re-exports, features, and examples while
solving one issue. Unscoped edits mix concepts, increase review cost, and make it harder to know
which module owns the behavior.

This is the change-shape counterpart to concept-owned modules. If a change crosses crate, module,
feature, or public facade boundaries, it should be because the behavior's owner requires that
surface, not because the files were nearby.

## Helps

- Helps changes stay atomic and lets reviewers verify the behavior in the module that owns it.

## Limits

Cross-cutting API, feature, or workspace changes can be necessary. Make the ownership and reason
explicit when a change must cross module or crate boundaries. Split mechanical cleanup from behavior
changes when the cleanup is not required to make the behavior understandable.

## Agent Instruction

Before editing Rust code, identify the owning module or crate and keep unrelated cleanup out of the
change.

## Mechanisms

Supported by jj change shape, module ownership review, focused tests, and separate follow-up
changes for unrelated cleanup.

## References

- [Rule: CHANGE-IDENTIFY-OWNING-MODULE-BEFORE-EDITING](../change-shape/change-identify-owning-module-before-editing.md)
- [Rule: CHANGE-USE-ONE-PURPOSE-PER-CHANGE](../change-shape/change-use-one-purpose-per-change.md)
