# Module Library v0.1

## Purpose

This document defines the first practical shape of the module system.

The goal is not to launch dozens of modules now.

The goal is to make the product obviously extensible.

## Module Categories

The academy should support these official module categories:

1. `industry`
2. `role`
3. `preference`
4. `policy`

The core academy itself stays outside the module marketplace because it is always required.

## Official Structure

Recommended repository layout:

- `modules/industry/<name>/module.yaml`
- `modules/role/<name>/module.yaml`
- `modules/preference/<name>/module.yaml`
- `modules/policy/<name>/module.yaml`

## Minimum Module Fields

Every module should include:

- `module_id`
- `module_type`
- `version`
- `name`
- `summary`
- `best_for`
- `key_expectations`
- `adds_to_core`

Different module types can add more fields later.

## First Sample Modules

The first repository samples are:

- Education industry module
- Marketing role module
- High-clarity reporting preference module
- Enterprise culture and workforce policy module

These are not the final best modules.

They are structural examples that prove the assembly model works.

## Why This Matters

This turns the academy from:

- one generic training system

into:

- a configurable agent operating system

That is the right long-term product direction.
