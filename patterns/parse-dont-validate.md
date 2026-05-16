# Parse Dont Validate

## Metadata

- Name: `Parse Dont Validate`
- ID: `parse-dont-validate`
- Summary: Validation that returns raw values forces callers to remember which invariants already
  hold. Parse uncertain input into types that carry those invariants, using constructors or standard
  parsing traits that honestly match the boundary.
- Status: `reviewed`
- Audience: `both`
- Topics: `rust, api-design, validation`
- Tags: `boundary-correctness, validation-policy, public-api`
- Related: `make-invalid-states-hard-to-express, prefer-standard-conversions`

## Problem

Validation that returns the original raw value leaves the caller with a memory burden. They must
remember which strings, maps, paths, or payloads have already passed which checks, and the compiler
cannot tell trusted input from untrusted input.

## Preferred Move

Parse uncertain input into a type that carries the invariant. Put trimming, normalization, decoding,
and validation at the boundary where raw input enters the trusted part of the system. Downstream
code should accept the parsed type, not the raw representation plus an expectation that validation
already happened.

Use `FromStr` when parsing from text is the standard relationship. Use a named constructor when the
boundary has domain policy, context, side effects, or multiple parse modes.

## Tradeoff

Do not create wrapper types for one local branch that immediately unwraps them. Parsing types earn
their keep when they remove repeated checks, clarify API contracts, or prevent invalid values from
crossing a boundary.

## Agent Instruction

When raw input is validated before use, prefer introducing a parsed type at that boundary. Report
which invariant the type now carries and which downstream checks were removed or made unnecessary.

## Examples

Bad: validation returns `()`, so the raw string still has to be trusted by convention.

```rust
fn validate_slug(input: &str) -> Result<(), SlugError> {
    if input.is_empty() || input.contains('/') {
        return Err(SlugError::Invalid);
    }

    Ok(())
}

pub fn publish(slug: &str) -> Result<(), PublishError> {
    validate_slug(slug)?;
    repository::publish_by_slug(slug)
}
```

Good: parsing produces the value that trusted code accepts.

```rust
pub struct PatternSlug(String);

impl FromStr for PatternSlug {
    type Err = SlugError;

    fn from_str(input: &str) -> Result<Self, Self::Err> {
        if input.is_empty() || input.contains('/') {
            return Err(SlugError::Invalid);
        }

        Ok(Self(input.to_owned()))
    }
}

pub fn publish(slug: PatternSlug) -> Result<(), PublishError> {
    repository::publish_by_slug(&slug)
}
```

## References

| Source                      | Use        | Note                                                       |
| --------------------------- | ---------- | ---------------------------------------------------------- |
| [Parse, don't validate][ak] | `adapts`   | Preserve learned input facts in the resulting type.        |
| [C-VALIDATE][validate]      | `supports` | Enforce validity at the API boundary where practical.      |
| [FromStr][from-str]         | `adapts`   | Text parsing should expose a typed result and parse error. |

[ak]: https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/
[from-str]: https://doc.rust-lang.org/std/str/trait.FromStr.html
[validate]: https://rust-lang.github.io/api-guidelines/dependability.html#c-validate
