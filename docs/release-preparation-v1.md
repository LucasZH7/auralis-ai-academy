# Release Preparation v1

## 1. Goal

Prepare the repository for a first public GitHub release without overbuilding.

The first release should prove:

- the academy concept is coherent
- the operating standards are concrete
- the artifacts are real
- the system is understandable to humans and useful to agents

## 2. What Is Already Ready

The repository already includes:

- academy mission and positioning
- universal foundation curriculum
- remediation diploma
- owner profiling system
- memory and backup system
- cache hygiene system
- evaluation and revocation rules
- identity and numbering system
- sample academy-state package
- sample evaluation records
- certificate and student-card templates

## 3. What Should Be Finalized Before Publishing

### A. English Brand Name

Working choice for v1:

- `Auralis AI Academy`

### B. Repository Name

Recommended examples:

- `northstar-ai-academy`
- `beijixing-ai-academy`
- `ai-agent-academy`

### C. Public One-Line Description

Recommended draft:

- `A practical academy and governance framework for long-running AI agents.`

### D. First Version Tag

Recommended:

- `v0.1.0`

## 4. Suggested First Release Contents

The first release does not need everything.

It should prominently show:

- README
- manifesto
- curriculum
- remediation diploma
- owner profiling
- memory and cache hygiene
- evaluation rules
- identity system
- worked examples

## 5. What Can Wait Until Later

Do not block the first release on:

- a polished website
- a database
- a complex automation backend
- a marketplace
- advanced rendering systems

Those are later-stage features.

## 6. Suggested Release Checklist

1. finalize English name
2. confirm repository name
3. polish README one more time
4. ensure example files are clean and consistent
5. add a simple generation command example
6. create first Git commit for public release

## 7. Minimal Demo Commands

Example certificate generation:

```bash
python3 scripts/generate_artifact.py \
  --template templates/certificate-template.md \
  --data examples/artifacts/demo-certificate-data.yaml \
  --output out/CERT-2026-000001.md
```

Example student-card generation:

```bash
python3 scripts/generate_artifact.py \
  --template templates/student-card-template.svg \
  --data examples/artifacts/demo-student-card-data.yaml \
  --output out/STU-2026-000001.svg
```

## 8. Definition of a Good First Release

A good first release should make a visitor think:

- this is unusual
- this is practical
- this is better structured than typical AI-agent prompt collections
- I can understand how to adapt this to my own agent
