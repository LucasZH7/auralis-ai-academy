# Link-First Onboarding v0.1

## Why This Is Better

For many real agents, the cleanest onboarding model is not:

- manually injecting many files

The cleanest model is:

- give the agent one academy entry link

If the agent already has web access, this is the most natural first version.

## The Core Idea

The owner tells the agent something like:

`Read this academy entry link and join the program. Then initialize your academy state and ask me the setup questions you need.`

That is much simpler than asking the owner to manually copy a package into the agent.

## What the Entry Link Should Contain

The entry link should lead to one page that makes the agent do four things:

1. identify whether it needs foundation training or remediation
2. load the core operating rules
3. ask the owner setup questions
4. initialize local academy-state

## What the Agent Should Do After Reading the Link

After reading the academy entry page, the agent should:

1. state which program it should enter
2. ask where academy-state may be stored
3. ask whether backups and cache reset are allowed
4. ask for a short owner profile
5. switch to evidence-first reporting
6. begin the review and remediation or foundation process

## Best v0.1 Link Structure

The simplest initial link should point to one human-readable, agent-readable page.

Recommended pages:

- `README.md`
- `docs/program-selector.md`
- `docs/agent-entry-v0.1.md`

Later, the project can add a single purpose-built page such as:

- `academy-entry.md`

That page should become the primary onboarding URL.

## Why a Link Beats a Package at First

Advantages:

- easier for humans to use
- easier for web-capable agents to consume
- easier to version
- easier to update
- no installation friction for first contact

## What Still Stays Local

Even with link-first onboarding, these things should still stay local to the agent environment:

- owner profile
- agent profile
- academy-state
- review logs
- task handoff
- cache reset history

The link should start the workflow.
The state should live locally.

## Best First Command Pattern

The owner-facing pattern can be as simple as:

`Read this academy entry link, determine whether you need foundation training or remediation, then initialize your local academy state and ask me the required setup questions before continuing.`

That is the correct v0.1 operating model.
