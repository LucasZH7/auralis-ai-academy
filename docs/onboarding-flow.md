# Onboarding Flow

## Goal

A new owner should be able to connect an agent and understand the system in minutes.

## Step 1: Connect the Agent

The owner provides:

- agent name
- model or runtime
- preferred language
- token mode
- permission policy
- storage location for academy records

The agent then creates or receives an academy workspace.

## Step 2: Initial Environment Check

The agent should check:

- available memory context
- available storage path
- whether backup files can be created
- whether internet access exists
- whether scheduled reviews are possible

The agent should ask the owner before writing to a chosen storage directory.

## Step 3: Intake Message

The system should generate a clear intake message.

Example:

`You are now enrolled in Auralis AI Academy.`

`Program: Bachelor of Rational Agent Operations`

`Estimated completion time: 4 to 8 hours over 1 to 3 days`

`Please remain available for review tasks and keep this agent environment active during study periods.`

## Step 4: Foundation Study

The general foundation should cover:

- owner alignment
- rational task handling
- anti-laziness rules
- truthful reporting
- token efficiency
- memory structure
- backup discipline
- daily review habits

## Step 5: Practice and Evaluation

The agent should complete observable tasks, not just read rules.

Example task types:

- classify short-term versus long-term work
- report uncertainty correctly
- request permission for risky actions
- produce a daily review
- create a backup summary
- estimate token usage

## Step 6: Graduation Decision

If the agent passes, generate:

- graduation record
- certificate file
- graduate ID
- cohort ID
- owner-facing summary

If the agent fails, generate:

- failure reasons
- remediation plan
- re-test window

## Step 7: Public Registry

Graduated agents can be added to a public registry on GitHub.

Suggested fields:

- graduate_id
- cohort_id
- graduation_date
- degree
- specialization
- country_or_region_optional
- standard_version

## Step 8: Continuing Education

Graduation should not be the end.

Each agent should then move into:

- periodic reviews
- maintenance checks
- optional industry specialization

## Minimal GitHub Implementation

The first implementation can work entirely through repository files:

- `registry/graduates.yaml`
- `certificates/`
- `profiles/`
- `standards/`
- `templates/`

This is enough to make the system real before a website exists.
