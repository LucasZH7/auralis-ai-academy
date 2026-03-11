# OpenClaw Adapter Strategy

## Position

The academy project must remain general-purpose.

It should not be redesigned around any single agent runtime, platform, or skill marketplace.

That means:

- `Auralis AI Academy / 北极星人工智能学院` remains the master project
- OpenClaw gets a lightweight adapter layer
- future agent ecosystems can receive similar adapter layers

## Why this matters

If the academy is tightly coupled to one runtime, it becomes fragile and harder to expand.

If the academy stays generic and only adapters are platform-specific, the project can later support:

- OpenClaw
- other hosted agent runtimes
- private local agent systems
- future agent app stores or plugin markets

## Recommended structure

### Core layer

The root repository contains:

- standards
- curricula
- remediation model
- owner profiling
- memory and backup rules
- evaluation and certification
- canonical onboarding pages

### Adapter layer

Each platform gets a narrow adapter that translates academy behavior into the target ecosystem.

For OpenClaw, that means:

- a lightweight `SKILL.md`
- minimal marketplace-facing metadata
- a short onboarding path
- references back to the canonical academy rules

## Marketplace strategy

Do not try to publish the entire academy as one massive skill.

Publish a lightweight product-facing entry:

- `agent-academy`

Future marketplace variants can be narrower:

- `agent-remediation`
- `agent-reset`
- `agent-discipline`

## Product message

For OpenClaw, the public message should be much simpler than the full academy narrative:

- long-running agents drift
- this skill helps fix that
- it asks the owner the right setup questions
- it initializes academy-state
- it switches the agent into evidence-first operation

## Success criteria

The OpenClaw adapter is successful if:

1. a user can understand it in under 30 seconds
2. an agent can enter academy mode from one short entry link
3. the adapter does not weaken the generic academy architecture
