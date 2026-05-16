# Rust Do Not Default Pub Crate

## Metadata

- ID: `RUST-DO-NOT-DEFAULT-PUB-CRATE`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Do not default to `pub(crate)`.

## Why

`pub(crate)` looks safe because it is not public API, but it still expands the crate-wide surface
and lets modules reach into each other. Start private, then widen visibility only when another
module has a clear ownership reason to call it.

## Helps

Helps keep internal APIs narrow so modules can change independently and readers can tell which items
are truly shared implementation surface.

## Limits

`pub(crate)` is appropriate for deliberate shared internals, test support behind cfg, generated
code, or module families that need a crate-local contract.

## Agent Instruction

Do not default to `pub(crate)` because crate-wide visibility still expands the internal surface and
lets modules reach into each other.

## Mechanisms

Start with private items, widen visibility only when another module needs the item, and prefer
`pub(super)` or smaller module ownership when that captures the real audience.

## References

- [Rust Reference: visibility and
  privacy](https://doc.rust-lang.org/reference/visibility-and-privacy.html)
