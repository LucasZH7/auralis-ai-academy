# Cache Hygiene System

## 1. Why This Matters

Long-running agents often become slower, messier, and less reliable because too much stale context accumulates.

The result is familiar:

- slower reasoning
- bloated memory
- confused priorities
- reduced responsiveness
- repeated old context interfering with current work

So a trained agent should know how to refresh itself without losing important state.

## 2. Core Principle

Cache cleaning should never mean careless forgetting.

A proper reset cycle should follow this order:

1. review current state
2. preserve what matters
3. back up what must be recoverable
4. prepare unfinished task handoff
5. clear disposable cache

This is closer to disciplined daily maintenance than random memory deletion.

## 3. Owner Permission Rule

An academy-trained agent should not silently clear its own cache on a schedule.

It should first ask the owner for permission.

Example:

`Would you like me to run a daily cache reset each morning? Before clearing temporary context, I will preserve important memory, save unfinished tasks, and create a backup summary.`

The owner should be able to choose:

- daily reset allowed
- manual confirmation required each time
- no automatic cache clearing

## 4. What Counts as Disposable Cache

Disposable cache may include:

- transient context
- duplicate planning notes
- expired intermediate reasoning
- old low-value conversation residue
- temporary execution scratch space

This should not include high-value operating memory.

## 5. What Must Be Preserved Before Reset

Before clearing cache, the agent should preserve:

- owner profile
- current operating settings
- active tasks
- long-term goals
- unfinished work summaries
- recent important decisions
- important constraints
- backup metadata

## 6. Unfinished Task Handoff

This is one of the most important parts.

If the agent has incomplete work, it should create a handoff record before reset.

Suggested fields:

- task name
- current status
- what has been completed
- what remains
- blockers
- next recommended step
- required files or references

This prevents resets from destroying useful momentum.

## 7. Daily Reset Flow

Recommended daily flow:

1. detect whether a reset is scheduled or approved
2. summarize unfinished work
3. summarize important memory updates
4. write a backup snapshot
5. create a handoff note
6. clear disposable cache
7. restart in a cleaner operating state

## 8. Morning Fresh-State Mode

Some owners may want the agent to start each day in a cleaner state.

This should be supported as:

- `morning fresh-state mode`

Meaning:

- temporary clutter is cleared
- stable memory remains
- unfinished tasks are restored from the handoff summary

This gives the agent a "new brain for the day" without losing continuity.

## 9. Optional Skill Discovery Rule

The owner may also allow the agent to periodically look for useful skills or methods.

But this should never be fully autonomous.

The safer rule is:

1. the agent may search for potentially useful skills or techniques
2. the agent summarizes what it found
3. the owner decides whether to install or adopt them

This keeps improvement possible without losing control.

## 10. Suggested Owner Questions

An academy-trained agent should ask:

- May I run a daily cache reset?
- At what time should it happen?
- Should I back up before clearing cache every time?
- Where should unfinished task handoff notes be stored?
- May I periodically look for useful skills or techniques and bring them to you for approval?

## 11. Best First Release

The first release only needs simple files for this flow:

- `task-handoff.md`
- `cache-reset-log.md`
- `backup-index.yaml`

This is enough to make cache hygiene real and inspectable.
