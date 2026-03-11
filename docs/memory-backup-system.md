# Memory and Backup System

## 1. Goal

An academy-trained agent should not become stronger but harder to manage.

It should become stronger and easier to inspect, back up, migrate, and restore.

That means memory must be structured.

## 2. Design Principles

The memory system should be:

- simple
- portable
- owner-readable
- backup-friendly
- uninstall-friendly
- safe to review

## 3. What the Academy Should Store

The academy layer should not try to store everything.

It should store the most useful operating information:

- owner preferences
- current operating profile
- long-term goals
- active constraints
- key learned facts approved for retention
- recent review summaries
- backup history

## 4. Memory Layers

The system should separate memory into layers.

### Layer A: Owner Preference Memory

Stable preferences that shape behavior.

Examples:

- preferred language
- preferred tone
- preferred detail level
- token mode
- approval threshold
- backup preference
- multi-model routing policy
- owner role or profession
- technical comfort level
- emotional support preference
- sensitive-topic limits
- owner persona summary

### Layer B: Operational Memory

Current working configuration.

Examples:

- current tasks
- long-term projects
- current limits
- current environment facts

### Layer C: Review Memory

Short summaries of what happened during work.

Examples:

- mistakes
- repeated blockers
- token waste patterns
- successful behavior changes

### Layer D: Backup Index

A list of available snapshots and when they were created.

## 5. What Should Not Be Stored Blindly

The academy should avoid keeping raw noise forever.

Do not store everything by default:

- every chat message
- unstable guesses
- duplicate logs
- private secrets unless explicitly approved
- temporary context with no long-term value

## 6. Minimum Backup Package

Every trained agent should be able to prepare a minimum backup package with:

- `owner-profile.yaml`
- `agent-profile.yaml`
- `active-goals.yaml`
- `memory-summary.md`
- `review-log.md`
- `backup-index.yaml`
- `task-handoff.md` when unfinished work exists

This is enough for recovery, migration, and audit.

## 7. Suggested Directory Structure

Recommended academy workspace structure:

```text
academy-state/
  owner-profile.yaml
  agent-profile.yaml
  active-goals.yaml
  memory-summary.md
  review-log.md
  backup-index.yaml
  task-handoff.md
  cache-reset-log.md
  snapshots/
    2026-03-11-foundation/
      owner-profile.yaml
      agent-profile.yaml
      active-goals.yaml
      memory-summary.md
      review-log.md
```

## 8. Owner Permission Rule

Before creating academy memory files, the agent should ask:

- where files may be stored
- whether backups should be local, remote, or both
- how often backups should be created
- whether daily cache reset is allowed

No memory system should be assumed silently.

## 9. Compression Rule

The academy should prefer summaries over raw accumulation.

Good memory behavior:

- compress old logs
- preserve key decisions
- preserve owner preferences
- preserve unresolved long-term items
- discard redundant text
- prepare handoff notes before cache clearing

## 10. Uninstall Rule

If the owner removes the academy layer:

- the agent should be able to archive or export academy-state
- the certificate status should become inactive unless revoked
- the memory package should remain readable by the owner

This makes the system reversible and trustworthy.

## 11. Recovery Rule

On recovery, a trained agent should be able to restore:

- owner preference profile
- current operating mode
- long-term goals
- review history summary
- latest valid backup snapshot

## 12. Best First Release

The first release does not need a database.

Simple YAML and Markdown files are enough.

That is better for:

- portability
- open-source clarity
- GitHub compatibility
- owner trust
