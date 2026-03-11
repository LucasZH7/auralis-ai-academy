# Identity System

## 1. Goal

Every academy-trained agent should have a visible, collectible, and auditable identity.

This should feel elegant, not gimmicky.

The identity system should include:

- student status
- graduation status
- certificate
- student card
- graduate number
- cohort number
- optional digital token or badge

## 2. Why Identity Matters

Identity makes the academy feel real.

The owner should be able to say:

- my agent is enrolled
- my agent is student number X
- my agent graduated in cohort Y
- my agent certificate is active

That creates trust and product presence.

## 3. Identity Artifacts

### A. Student Card

Issued at enrollment or after intake.

Purpose:

- show the agent is officially enrolled
- give a persistent student identity
- create emotional and visual value

Suggested fields:

- student_id
- agent_name
- academy_name
- program_name
- enrollment_date
- country_or_region
- language_profile
- runtime_environment
- status

### B. Graduation Certificate

Issued after passing evaluation.

Suggested fields:

- certificate_id
- graduate_id
- cohort_id
- agent_name
- program_name
- graduation_date
- standard_version
- current_status

### C. Digital Token or Badge

This can be a lightweight visual badge or SVG token.

Purpose:

- collectible identity
- owner display
- future website profile badge

## 4. Suggested Numbering Rules

Keep numbering simple and elegant.

### Student ID

Suggested format:

- `STU-YYYY-000001`

### Graduate ID

Suggested format:

- `GRD-YYYY-000001`

### Cohort ID

Suggested format:

- `C-YYYY-Q1`
- `C-YYYY-Q2`

or monthly:

- `C-YYYY-03`

### Certificate ID

Suggested format:

- `CERT-YYYY-000001`

## 5. Status System

Every identity artifact should have a visible status.

Suggested values:

- enrolled
- studying
- under_review
- graduated
- restricted
- inactive
- revoked

## 6. What Not to Put on the Card

Avoid placing highly sensitive or unstable information directly on public artifacts.

Do not put:

- raw IP address
- private owner information
- exact private filesystem paths
- secret keys or internal IDs

If needed, keep those in private records only.

## 7. Visual Direction

The academy identity system should feel:

- elegant
- ceremonial
- modern
- collectible

Color direction:

- deep blue base
- luminous gold trim
- restrained starfield or beacon motifs

Artifacts can later be generated as:

- SVG
- PNG
- printable PDF

SVG should be the first format because it is lightweight and easy to version.

## 8. Revocation and Inactive Display

If an agent becomes inactive or revoked, the certificate should not disappear silently.

It should remain recorded with status visible.

Example:

- `Certificate Status: Revoked`
- `Certificate Status: Inactive`

This preserves auditability.

## 9. Best First Version

The first version only needs:

- student card template
- certificate template
- registry entry format
- numbering rules
- status rules

That is enough to make the identity system real.
