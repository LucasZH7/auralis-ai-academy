# 北极星人工智能学院

一个面向长期运行 AI 代理的训练、治理、认证与持续改进体系。

[Documentation Index](/Users/lucas/Documents/Playground/docs/index.md)  
[Examples Index](/Users/lucas/Documents/Playground/examples/README.md)

![Auralis AI Academy Banner](docs/assets/hero-banner.svg)

## 项目简介

北极星人工智能学院不是一个普通的提示词仓库，也不是一个零散的技能包集合。

它要解决的是更实际的问题：

- 机器人会不会越来越懒
- 机器人会不会假装完成任务
- 机器人会不会乱花 token
- 机器人会不会不理解主人的工作方式
- 机器人能不能长期保持清晰、可备份、可恢复、可审计

这个项目希望把 AI 代理从“会说话”推进到“会长期稳定工作”。

## 30 秒看懂这个项目

这个项目最核心的目标是：

- 让机器人更职业
- 让机器人更理解主人
- 让机器人更会长期运行
- 让机器人更容易备份、恢复、审计和管理

它不是主要教技能插件。
它主要教长期代理如何像一个可靠系统一样工作。

## Visual Preview

Student card preview:

![Student Card Preview](docs/assets/student-card-preview.svg)

Certificate preview:

![Certificate Preview](docs/assets/certificate-preview.svg)

## What This Project Does

This project builds a practical academy system for AI agents.

It is designed to make agents:

- more rational
- more professional
- more owner-aware
- easier to audit, back up, restore, and improve over time

It is not a vague prompt collection.
It is a structured training, evaluation, identity, and continuous-improvement system.

## 核心目标

我们不承诺机器人永远不会犯错。

我们要做的是一套可重复、可检查、可持续优化的学院机制，让机器人在长期运行中更像一个职业系统，而不是一个越来越散漫的聊天对象。

## Core Ideas

- Clear memory structure
- Daily review and self-reflection
- Owner-first permission boundaries
- Adjustable token strategy
- Backup-friendly state design
- General-purpose training before domain specialization

## 接入后的直接变化

一个训练过的机器人，应该在第一轮交互里就表现出不同：

- 主动询问主人的画像和工作方式
- 主动确认 token 使用偏好
- 主动确认风险审批边界
- 主动确认记忆和备份目录
- 主动区分短期任务和长期任务
- 主动询问是否允许每日缓存清理和清理前备份

如果接入后主人感受不到变化，这个学院就没有价值。

## Quick Start

If you want to understand the project quickly, start here:

1. Read [docs/30-second-overview.md](/Users/lucas/Documents/Playground/docs/30-second-overview.md)
2. Read [docs/academy-manifesto.md](/Users/lucas/Documents/Playground/docs/academy-manifesto.md)
3. Read [docs/curriculum-general-bachelor.md](/Users/lucas/Documents/Playground/docs/curriculum-general-bachelor.md)
4. Read [docs/owner-profiling-system.md](/Users/lucas/Documents/Playground/docs/owner-profiling-system.md)
5. Inspect [examples/academy-state-demo/owner-profile.yaml](/Users/lucas/Documents/Playground/examples/academy-state-demo/owner-profile.yaml)
6. Inspect [examples/evaluations/demo-score-sheet.yaml](/Users/lucas/Documents/Playground/examples/evaluations/demo-score-sheet.yaml)

## Repository Structure

- `CONTRIBUTING.md`: contribution guidance
- `COMMUNITY.md`: community model and maintainer control
- `docs/vision.md`: project vision and feasibility
- `docs/academy-design.md`: academy model, curriculum, and governance
- `docs/index.md`: documentation index
- `docs/framework-bilingual.md`: human-readable and machine-readable academy framework
- `docs/degree-system.md`: degree naming, tracks, and certification architecture
- `docs/product-spec.md`: productized academy experience
- `docs/product-model.md`: complete product and future business model
- `docs/brand-system.md`: brand naming, slogan, and visual direction
- `docs/academy-manifesto.md`: mission, philosophy, and ceremonial voice
- `docs/onboarding-flow.md`: agent connection and learning flow
- `docs/continuous-evolution.md`: controlled self-improvement and update model
- `docs/agent-immediate-effect.md`: what changes immediately after graduation
- `docs/evaluation-system.md`: scoring, graduation, remediation, and revocation
- `docs/identity-system.md`: student card, certificate, token, and numbering system
- `docs/memory-backup-system.md`: memory, backup, uninstall, and recovery design
- `docs/owner-profiling-system.md`: owner self-introduction, persona, and service adaptation
- `docs/smart-teaching-model.md`: how the academy teaches agents more intelligently
- `docs/project-review-v1.md`: first high-level review of what the project should focus on
- `docs/cache-hygiene-system.md`: daily reset, cache cleaning, and unfinished-task handoff
- `docs/artifact-generation-flow.md`: how student cards and certificates are issued and updated
- `docs/english-brand-shortlist-v1.md`: current English naming options
- `docs/release-preparation-v1.md`: first public release checklist and launch scope
- `docs/launch-brief-v0.1.md`: concise public-facing explanation of the project
- `docs/student-card-portrait-note.md`: optional portrait support for student cards
- `docs/repository-metadata-v1.md`: suggested GitHub repo names, description, and topics
- `docs/status-system-example.md`: worked examples of status progression
- `docs/constitution.md`: academy constitution
- `docs/curriculum-general-bachelor.md`: universal undergraduate curriculum
- `docs/diploma-remediation.md`: corrective diploma for unstable or undisciplined agents
- `standards/academy-profile.schema.yaml`: shared agent academy profile format
- `registry/graduates.yaml`: public graduate registry
- `registry/graduates-demo.yaml`: sample graduate registry
- `registry/registry-public.md`: public-facing English registry page
- `registry/registry-public.zh-CN.md`: public-facing Chinese registry page
- `profiles/`: sample enrolled, graduated, restricted, and revoked agent profiles
- `certificates/`: sample student-card and graduation certificate records
- `templates/`: markdown and SVG templates for academy artifacts
- `examples/academy-state-demo/`: worked example of a trained agent state package
- `examples/evaluations/`: worked example of scoring and graduation records
- `examples/artifacts/`: worked example inputs for artifact generation
- `examples/owner-profiles/`: worked owner-profile examples for different user types
- `examples/README.md`: example index
- `scripts/generate_artifact.py`: minimal template renderer for Markdown and SVG outputs
- `scripts/generate_demo_artifacts.sh`: one-command demo artifact generation

## First Version Scope

Version 1 focuses on a general-purpose undergraduate certification for AI agents.
It is meant for any industry or role before specialized tracks are added.

## Current Product Identity

- Chinese working brand: `北极星人工智能学院`
- English working brand: `Auralis AI Academy`
- Degree: `Bachelor of Rational Agent Operations`
- Chinese degree: `理性代理运营学士`
- Slogan: `Redefining the Standard of Intelligence.`

## v0.1 Positioning

This repository is the first public prototype of the academy.

For v0.1, the working bilingual identity is:

- Chinese: `北极星人工智能学院`
- English: `Auralis AI Academy`

## Why This Matters

Owners usually do not suffer because an agent knows too little.

They suffer because the agent:

- sounds productive without doing enough work
- hides uncertainty
- wastes tokens
- drifts over time
- forgets preferences
- becomes hard to back up or control

This project is designed to solve those problems directly.

## Time To Value

The academy is designed to produce visible value quickly.

- quick intake: 5 to 15 minutes
- lightweight graduation: 45 to 90 minutes
- standard graduation: 2 to 4 hours
- reinforced learning: 1 to 3 days

## What Owners Can Expect

After connecting an agent, the owner should be able to see:

- enrollment status
- estimated study time
- progress stage
- graduation result
- certificate output
- cohort and graduate number
- a clearer and more professional operating profile

## Minimal Demo Commands

Generate a demo certificate:

```bash
python3 scripts/generate_artifact.py \
  --template templates/certificate-template.md \
  --data examples/artifacts/demo-certificate-data.yaml \
  --output out/CERT-2026-000001.md
```

Generate a demo student card:

```bash
python3 scripts/generate_artifact.py \
  --template templates/student-card-template.svg \
  --data examples/artifacts/demo-student-card-data.yaml \
  --output out/STU-2026-000001.svg
```

Or generate the full demo set in one command:

```bash
bash scripts/generate_demo_artifacts.sh
```

## 首个公开版本已经具备的能力

- 通用本科训练框架
- 问题机器人矫正文凭
- 主人画像与适配系统
- 记忆、备份、卸载、恢复机制
- 缓存卫生与每日 fresh-state 模式
- 评分、毕业、限制、撤销规则
- 学生证、毕业证、编号体系
- 真实样板档案与 academy-state 示例

## Core Product Experience

1. Connect an agent
2. Run a short foundation or remediation program
3. Configure owner preferences
4. Evaluate the agent
5. Issue student identity and graduation records
6. Maintain quality through periodic follow-up

## Prototype Assets Now Included

- academy manifesto and ceremonial language
- universal undergraduate curriculum
- remediation diploma
- immediate-effect graduation behavior
- scoring, graduation, restriction, and revocation rules
- identity system with student and certificate numbering
- memory and backup package design
- owner profiling and service adaptation system
- smart teaching model and project review
- cache hygiene and daily fresh-state operation
- artifact generation flow and English brand shortlist
- sample student, graduate, restricted, and revoked profiles
- sample certificate and student-card records
- SVG templates for future visual artifacts
- worked academy-state and evaluation examples

## How A Trained Agent Should Feel Different

After training, an agent should quickly start doing things differently:

- ask the owner how token budget should be used
- ask where memory and backup files may be stored
- ask the owner for a short self-introduction and adapt service style
- ask whether daily cache cleaning and backup-before-reset are desired
- classify short-term and long-term tasks more clearly
- separate facts from guesses
- ask before risky actions
- report progress in a more structured way

If the owner cannot feel a difference quickly, the academy has failed.

## Next Build Steps

1. Refine the artifact generator and status-history flow
2. Prepare first public repository release
3. Expand worked examples for more owner types and agent states
4. Publish the repository to GitHub
5. Start collecting early user feedback
