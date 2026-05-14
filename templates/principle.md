# Principle Template

Use this template for durable reasoning notes that justify one or more rules. Replace bracketed text
before publishing an entry.

## Metadata

- Name: `[Human-readable name]`
- ID: `[stable-kebab-case-id]`
- Status: `draft`
- Audience: `[humans | agents | both]`
- Topics: `[comma-separated topics]`
- Related: `[related stable IDs, if any]`

## Claim

State the belief directly. A reader should be able to quote this section in a review comment.

## Why I Believe This

Explain the failure mode, experience, tradeoff, or external source that makes this principle worth
keeping. Prefer concrete development consequences over broad best-practice language.

## What This Changes

Describe how the principle changes implementation, review, documentation, testing, or agent
behavior.

## Rust-Specific Guidance

Include this section when Rust has meaningful idioms, tools, or API tradeoffs for the principle.
Omit it when the principle is language-neutral.

## Good Uses

List situations where the principle should influence the work.

## Bad Smells

List signals that the principle is being violated or that review should slow down.

## Mechanisms

List tools, checks, commands, templates, or practices that can enforce or support the principle.

## Rules This Supports

- `[R-0000 Rule name]`

## Agent Consequences

Write the compact operational consequence for coding agents.

## Limits

Explain where the principle stops applying, what it costs, or what tradeoff can override it.

## References

List durable sources only when they help frame, validate, or contrast the principle. Omit this
section when no durable source is useful.

| Source         | Use         | Note                                    |
| -------------- | ----------- | --------------------------------------- |
| `[link label]` | `[purpose]` | `[relevant idea, contrast, or context]` |
