# OpenClaw Publish Checklist v0.1

## Goal

Publish a lightweight OpenClaw-facing skill without turning the whole academy into a platform-specific project.

## Minimum publish set

The OpenClaw adapter should include:

- `integrations/openclaw/agent-academy/SKILL.md`
- `integrations/openclaw/agent-academy/agents/openai.yaml`
- short marketplace copy
- one clear entry link into the main academy project

## Pre-publish checks

Before listing:

1. confirm the skill name is short and direct
2. confirm the first sentence states the problem clearly
3. confirm the skill routes agents into bachelor vs remediation
4. confirm the owner questions are present
5. confirm evidence-first reporting is explicit
6. confirm academy-state is local and owner-controlled
7. confirm the adapter references the main project instead of duplicating it

## Marketplace quality bar

A user should understand all of this in under 30 seconds:

- what problem this solves
- who it is for
- what changes after install
- how to start

## Launch order

1. keep the main GitHub project as the canonical source
2. package `agent-academy` as the first OpenClaw-facing listing
3. test on one drifting real agent
4. collect before/after evidence
5. use that evidence to improve the listing and future variants

## Future variants

After the first listing works, expand with narrower skills:

- `agent-remediation`
- `agent-reset`
- `agent-discipline`

Do not launch all variants at once.
