# Configuration Flow v1

## Goal

After reading the academy entry link, the agent should not just say it understands the academy.

It should begin configuration.

## Human Experience

The owner should feel:

- this agent is becoming more structured
- this agent is trying to understand my context
- this agent knows it must be configured before it can work well

## Recommended Sequence

### Step 1: Program

The agent decides:

- foundation bachelor
- remediation diploma

### Step 2: Industry

The agent asks:

- what industry or domain is this work mainly in?

Examples:

- education
- legal
- media
- chemistry
- manufacturing
- ecommerce

### Step 3: Role

The agent asks:

- what role am I expected to perform?

Examples:

- marketing
- operations
- administration
- research
- support
- recruiting

### Step 4: Preferences

The agent asks:

- concise or detailed reporting
- token strategy
- response style
- model-switching permission
- backup and cache reset rules

### Step 5: Organization Policy

If the owner is acting for a company or team, the agent asks:

- are there company ethics or policy rules?
- are there legal or privacy constraints?
- are there brand or approval rules?

## Why This Flow Works

This keeps the configuration simple:

- first who am I becoming
- then where am I working
- then what job am I doing
- then how should I behave
- then what rules must I respect

## Output

At the end of this flow, the agent should be able to produce:

- selected program
- selected industry module
- selected role module
- owner preference profile
- organization policy profile
- initialized academy-state

## First-Version Rule

In v0.1, the system only needs to fully support:

- program
- owner preferences
- academy-state

Industry, role, and policy can first be defined as placeholders and future module slots.
