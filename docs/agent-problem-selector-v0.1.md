# Agent Problem Selector v0.1

## Purpose

When an owner says an agent is "not good", that is too vague.

The academy should help the owner classify the problem quickly.

This should be done with a fixed set of problem patterns, not an open-ended essay by default.

## Recommended Owner Prompt

The agent should ask:

`Which of these best describes my current problem pattern? You can choose more than one.`

## Core Problem Types

### 1. Talks a lot but lands very little

Use this when the agent:

- explains too much
- promises too much
- creates many notes or plans
- produces too little real output

### 2. Does work but reports badly

Use this when the agent:

- actually moves tasks
- but does not summarize clearly
- does not ask enough questions
- does not communicate progress well

### 3. Pretends progress without proof

Use this when the agent:

- says `done` too early
- implies completion without evidence
- hides uncertainty
- makes progress sound bigger than it is

### 4. Freezes or stops moving

Use this when the agent:

- becomes inactive
- stalls for long periods
- waits too much
- needs repeated nudging to continue

### 5. Runs in circles

Use this when the agent:

- revisits the same issue again and again
- keeps rewriting rules or notes
- keeps re-explaining instead of closing work

### 6. Ignores or weakly follows instructions

Use this when the agent:

- changes scope on its own
- substitutes its own judgment too often
- does not stay aligned with the owner's priorities

### 7. Uses too much context or token budget

Use this when the agent:

- becomes bloated over time
- wastes messages on low-value detail
- grows less efficient after extended use

### 8. Escalates too late or not at all

Use this when the agent:

- should ask for help sooner
- should hand off sooner
- gets stuck instead of escalating

### 9. Needs stronger enterprise behavior

Use this when the agent:

- is okay for solo use
- but weak for team use
- does not understand reporting lines, approvals, or work culture

## Selection Rule

Owners should usually pick one primary problem type and up to two secondary problem types.

That is enough for first-version remediation routing.

## Why This Works

This keeps intake structured:

- owners do not need to write a long diagnosis
- agents get a cleaner remediation starting point
- the academy can later map each problem type to a standard corrective path
