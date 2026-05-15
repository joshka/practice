# Rust Prefer Expect For Lint Suppressions

## Metadata

- ID: `RUST-PREFER-EXPECT-FOR-LINT-SUPPRESSIONS`
- Legacy ID: `R-0210`
- Status: `reviewed`
- Domain: `rust`
- Depth: `compact`

## Rule

Prefer `#[expect]` over `#[allow]` when suppression should be revisited.

## Why

`#[allow]` can silently outlive the reason it was added. `#[expect]` records that a lint is
intentionally triggered and lets the compiler report when the expectation no longer matches the
code.

## Helps

Helps suppressions fail when they stop being needed, preventing stale `allow` attributes from hiding
fixed warnings forever.

## Limits

Use `allow` when the lint is intentionally disabled for a broad module or crate policy and the
suppression is not expected to disappear.

## Agent Instruction

Use `#[expect]` for lint suppressions that should disappear once the warning is fixed.

## Mechanisms

Use `#[expect(lint, reason = "...")]` for targeted suppressions, include a reason, and let CI catch
unfulfilled expectations.

## References

- [Rust Reference: lint check
  attributes](https://doc.rust-lang.org/reference/attributes/diagnostics.html#lint-check-attributes)
