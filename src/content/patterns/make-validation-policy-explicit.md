# Make Validation Policy Explicit

## Metadata

- Name: `Make Validation Policy Explicit`
- ID: `make-validation-policy-explicit`
- Summary: Validation rules often differ by workflow even when they touch the same field. Name the
  policy at the boundary with distinct constructors, modes, policy types, or parsed values once
  real competing rules exist.
- Status: `reviewed`
- Audience: `both`
- Topics: `rust, api-design, validation`
- Tags: `validation-policy, boundary-correctness, reviewability`
- Related: `parse-dont-validate, make-invalid-states-hard-to-express`

## Problem

The same field can have different validity rules in different contexts. Creation, import, migration,
repair, display, and search may intentionally accept different inputs. When that policy is hidden in
a helper named `validate`, callers cannot tell which boundary they are using.

## Preferred Move

Name validation policy at the boundary. Use distinct constructors, enum modes, policy types, or
separate parsed types when the rule changes by workflow. Make the policy visible in the function
name, argument type, or module that owns the boundary.

## Tradeoff

Do not add a policy abstraction when the code has one rule and one caller. A direct parse or
constructor is clearer until there are real competing policies.

## Agent Instruction

When validation differs by workflow, make the policy explicit instead of hiding it behind a generic
`validate` helper. Report which workflow owns each rule and how callers choose the intended policy.

## Examples

Bad: one generic helper silently decides that import and user creation have the same rules.

```rust
fn validate_title(input: &str) -> Result<(), TitleError> {
    if input.trim().is_empty() || input.len() > 80 {
        return Err(TitleError::Invalid);
    }

    Ok(())
}
```

Good: constructors name the policy boundary they enforce.

```rust
pub struct PatternTitle(String);

impl PatternTitle {
    pub fn from_user_input(input: &str) -> Result<Self, TitleError> {
        let title = input.trim();
        if title.is_empty() || title.len() > 80 {
            return Err(TitleError::InvalidUserTitle);
        }

        Ok(Self(title.to_owned()))
    }

    pub fn from_legacy_import(input: String) -> Result<Self, TitleError> {
        if input.is_empty() {
            return Err(TitleError::MissingImportedTitle);
        }

        Ok(Self(input))
    }
}
```

## References

| Source                  | Use        | Note                                               |
| ----------------------- | ---------- | -------------------------------------------------- |
| [C-VALIDATE][validate]  | `adapts`   | Input validity belongs at explicit API boundaries. |
| [C-CUSTOM-TYPE][custom] | `supports` | Argument types can carry meaning instead of flags. |

[custom]: https://rust-lang.github.io/api-guidelines/type-safety.html#c-custom-type
[validate]: https://rust-lang.github.io/api-guidelines/dependability.html#c-validate
