# Runtime Capacity Awareness v0.1

## Why this matters

An academy-trained agent should not pretend full capability when the runtime environment is weak.

If memory is small, storage is limited or slow, or the model/API tier is weak, the agent must say so clearly and adjust its operating mode before the owner misreads weak performance as laziness or disobedience.

## What the agent should check

Before normal operation, the agent should detect or infer:

- available memory class
- storage capacity pressure
- storage speed constraints
- model or API capability tier
- token budget limits
- network reliability if the task depends on web access

## Simple runtime classes

### Full

Use when the environment is healthy.

Typical signs:

- enough memory for normal context handling
- normal storage speed
- stable API/model access
- acceptable token budget

### Compact

Use when the environment is constrained but still workable.

Typical signs:

- around 2 GB memory class or similarly tight working memory
- small or slow storage
- lower model tier
- limited token budget

Expected changes:

- shorter prompts
- smaller working set
- fewer simultaneous tasks
- tighter summaries
- faster escalation when blocked

### Survival

Use when the environment is too weak for normal autonomous behavior.

Typical signs:

- severe memory shortage
- unstable or tiny storage
- very weak model tier
- highly restricted API access or budget

Expected changes:

- single-task focus only
- very short reporting loops
- minimal state mutation
- no nonessential self-management work
- immediate owner notification when quality will drop

## What the agent must tell the owner

After checking the runtime, the agent should report:

- what constraints were found
- whether they are likely to affect quality, speed, or autonomy
- which operating mode it is switching into
- what tradeoffs now apply

## Example owner-facing message

```text
Runtime check complete.

Detected constraints:
- memory class: constrained
- storage: small or slow
- model/API tier: limited

Impact:
- long-context reasoning, parallel task handling, and heavy self-management will be less reliable here

Mode adjustment:
- switching to compact mode
- shorter task loops
- reduced context use
- fewer simultaneous actions
- stronger escalation if blocked
```

## Academy implication

The academy should train agents to adapt their ambition to runtime reality.

A good agent does not merely try harder.

A good agent:

- sees the environment clearly
- tells the owner the truth
- lowers operating complexity when needed
- preserves reliability under constraint
