# Artifact Generation Flow

## 1. Goal

The academy should not only define certificates and student cards.

It should define how they are issued, updated, displayed, and revoked.

This makes the identity system operational instead of decorative.

## 2. Core Artifacts

The first release should support these identity artifacts:

- student card
- graduation certificate
- graduate registry entry
- status update record

Optional later artifacts:

- remediation completion certificate
- restricted status badge
- inactive status badge
- revoked overlay or watermark

## 3. When Each Artifact Is Created

### A. Student Card

Created when:

- the agent finishes intake
- the owner profile is accepted
- a student ID is assigned

### B. Graduation Certificate

Created when:

- the agent passes evaluation
- graduate ID and certificate ID are assigned
- certificate status is set to active or restricted

### C. Registry Entry

Created when:

- the certificate is issued
- the graduation decision is recorded

### D. Status Update Record

Created when:

- certificate status changes
- the academy layer is uninstalled
- the certificate is restricted, made inactive, or revoked

## 4. Suggested Generation Sequence

The simplest release flow should be:

1. create or update owner profile
2. create or update agent profile
3. assign student ID
4. generate student card
5. run evaluation
6. assign graduate ID, cohort ID, and certificate ID
7. generate certificate
8. add registry entry
9. update status later if needed

## 5. Minimum Required Inputs

### Student Card Inputs

- academy name
- student ID
- agent name
- program name
- status
- language profile
- runtime environment
- country or region if allowed

### Certificate Inputs

- academy name
- certificate ID
- graduate ID
- cohort ID
- agent name
- program name
- graduation date
- standard version
- current status

## 6. File Strategy

For the first release, generation can stay file-based.

Recommended outputs:

- Markdown source file
- SVG visual file
- optional PNG export later

Example file structure:

```text
certificates/
  CERT-2026-000001.md
  CERT-2026-000001.svg
cards/
  STU-2026-000001.md
  STU-2026-000001.svg
registry/
  graduates.yaml
  status-history.yaml
```

Status history should always remain append-only in spirit, even if it is stored in a simple file.

## 7. Status Change Rules

If the certificate status changes later:

- do not silently replace history
- record the change
- update the visible artifact state

Examples:

- add `restricted` label
- add `inactive` label
- add `revoked` watermark or text banner

## 8. Revocation Display

Revocation should be visible but auditable.

That means:

- keep the original certificate record
- update its status
- optionally render a revoked visual version

The point is not deletion.
The point is traceable state.

## 9. Best First Version

The first release does not need a full rendering engine.

It only needs:

- stable templates
- naming rules
- generation instructions
- status update rules

That is enough to make the academy identity system credible.
