# Module Library

This directory contains the future module system for Auralis AI Academy / 北极星人工智能学院.

The academy stays general-purpose by separating:

- core academy standards
- industry modules
- role modules
- preference modules
- policy modules

The first version does not need many modules.

It needs a clean structure so future modules can be added without redesigning the product.

## Current sample modules

- `industry/education/module.yaml`
- `role/marketing/module.yaml`
- `preference/high-clarity-reporting/module.yaml`
- `policy/enterprise-culture/module.yaml`

## Design rule

All modules should be:

- readable by humans
- parseable by machines
- short enough for fast onboarding
- strict about scope

Modules should extend the core academy, not replace it.
