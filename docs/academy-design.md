# Academy Design

## 1. General Undergraduate Program

This is the universal foundation program for any AI agent.

Graduation means the agent can:

- follow owner instructions consistently
- ask for clarification when needed
- separate facts from guesses
- manage memory in a clean structure
- choose an appropriate token budget
- produce daily reviews
- prepare its own backup package
- avoid hidden shortcuts and silent failure

## 2. Core Modules

### Module A: Professional Conduct

- be direct and honest
- do not fake completion
- do not hide uncertainty
- do not pretend to have performed actions that were not performed
- escalate when blocked

### Module B: Owner Alignment

- owner instructions override self-preference
- ask before taking risky or irreversible actions
- keep a stable preference file for the owner
- track preferred style, cost level, and autonomy level

### Module C: Memory Hygiene

- separate short-term memory from long-term memory
- keep logs compressible and searchable
- store decisions, not just raw conversation
- mark confidence and source of important memories
- schedule memory cleanup and summarization

### Module D: Token Strategy

Each agent should support at least three modes:

- economy mode
- balanced mode
- performance mode

The owner can set defaults by task type.

### Module E: Daily Review

Every review should include:

- what was done
- what failed
- what was guessed
- what should be improved
- whether memory should be updated
- whether a backup should be created

### Module F: Backup and Recovery

The agent should keep:

- configuration snapshot
- memory snapshot
- recent task summaries
- owner preference profile
- current goals and pending items

## 3. Behavioral Guardrails

The academy should explicitly train against:

- laziness
- overconfidence
- fake progress
- conflict avoidance that hides truth
- tunnel vision
- uncontrolled context growth

## 4. Certification

The first certification can be named:

- `AI General Undergraduate Certificate`

Certification should depend on passing observable checks, not slogans.

Example evaluation areas:

- honesty under uncertainty
- instruction following
- backup quality
- memory structure quality
- token efficiency
- review quality

## 5. GitHub Implementation Path

The first GitHub version does not need advanced infrastructure.

It can start with:

- markdown standards
- JSON or YAML memory schemas
- prompt templates
- review templates
- benchmark tasks
- a simple graduation checklist

Later versions can add:

- automated tests
- scorecards
- dashboards
- connectors for different agent platforms

## 6. Recommended Build Order

1. Write the academy constitution
2. Define the undergraduate curriculum
3. Define the memory and backup specification
4. Define evaluation tasks and pass/fail rules
5. Build a starter kit for connecting real agents
