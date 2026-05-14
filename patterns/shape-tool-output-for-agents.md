# Shape Tool Output For Agents

## Metadata

- Name: `Shape Tool Output For Agents`
- ID: `shape-tool-output-for-agents`
- Status: `reviewed`
- Audience: `agents`
- Topics: `agents, tooling, context`
- Related: `use-disk-as-context-sink, deliver-context-just-in-time`

## Problem

Many tools produce output optimized for humans watching a terminal. Verbose progress logs,
duplicated success lines, and full workspace output can bury the failure signal an agent needs.

## Preferred Move

Prefer quiet commands, failure-focused wrappers, structured output, and saved logs. Show agents the
small actionable summary first, with a path or command for inspecting full details when needed.

## Tradeoff

Do not hide context needed to debug failures. Keep full logs available on disk and make the summary
honest about truncation or filtering.

## Agent Instruction

When a command is noisy, use a quiet mode or wrapper that surfaces failures first. If you filter
output, record where the full log can be inspected.

## Examples

Bad: a workspace test floods context with success output.

```bash
pnpm test
```

Good: the wrapper keeps attention on failures and preserves full logs.

```bash
scripts/test-failures-first.sh --log target/test.log
```

## References

| Source                                 | Use      | Note                                                        |
| -------------------------------------- | -------- | ----------------------------------------------------------- |
| [OpenAI context management][knowledge] | `adapts` | Context is scarce, so agents need concise relevant signals. |

[knowledge]: https://openai.com/index/harness-engineering/#we-made-repository-knowledge-the-system-of-record
