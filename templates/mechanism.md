# Mechanism Template

Use this template for lints, formatter settings, CI checks, command recipes, local tool
configuration, templates, and generated artifacts that support rules mechanically.

## Metadata

- Name: `[Human-readable name]`
- ID: `[stable-kebab-case-id]`
- Summary: `[two-to-four sentence scan summary]`
- Status: `draft`
- Audience: `[humans | agents | both]`
- Topics: `[comma-separated topics]`
- Tags: `[comma-separated cluster tags]`
- Related: `[related stable IDs, if any]`

## Purpose

Explain which repeated failure the mechanism is meant to prevent or make cheaper to catch.

## Supported Principles

- `[Principle name]`

## Supported Rules

- `[R-0000 Rule name]`

## Configuration

Show stable configuration snippets when they are part of the guidance.

## Checks

List commands or CI jobs that use the mechanism.

## Agent Consequences

State when agents should suggest, run, or report the mechanism.

## Limits

Explain what the mechanism cannot catch, when it is too expensive, or when human judgment should
override it.
