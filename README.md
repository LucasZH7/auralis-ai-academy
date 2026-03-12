# 北极星人工智能学院

一个面向长期运行 AI 代理的训练、治理、认证与持续改进体系。

这个仓库是通用主仓库，不绑定单一 Agent 软件。
针对特定生态的接入会通过适配层提供，比如 OpenClaw skill。

[Documentation Index](/Users/lucas/Documents/Playground/docs/index.md)  
[Start Here](/Users/lucas/Documents/Playground/docs/start-here.md)  
[Examples Index](/Users/lucas/Documents/Playground/examples/README.md)
[Module Library](/Users/lucas/Documents/Playground/modules/README.md)

![Auralis AI Academy Banner](docs/assets/hero-banner.svg)

## 30 秒看懂这个项目

这不是一个单纯的 prompt 仓库，也不是一个零散技能库。

它是一个让长期运行 AI 代理变得更职业、更稳定、更听主人话的 Agent Academy。

它最核心的目标是：

- 让机器人更职业
- 让机器人更理解主人
- 让机器人更会长期运行
- 让机器人更有职业操守、法律意识和组织适配能力
- 让机器人更容易备份、恢复、审计和管理

## 它到底能干什么

它最直接的作用是把一个长期运行的 AI 代理，训练得更像一个职业系统。

训练后，代理应该更容易做到：

- 更听主人的话
- 更会区分长期任务和短期任务
- 更少偷懒和假装完成
- 更清楚地汇报进度、风险和不确定性
- 更会先检查自己的运行环境，再调整工作模式
- 更懂得怎么备份、怎么清缓存、怎么长期维持状态
- 更懂得根据主人的风格调整服务方式
- 更懂得遵循职业规范、审批链、法律法规和工作边界

## 为什么会有用

很多代理的问题不是“不聪明”，而是：

- 说得多，做得少
- 会装完成
- 会乱花 token
- 跑几天以后开始漂移
- 不会长期整理自己的状态

这个项目就是专门解决这些问题的。

## 长期方向

长期来看，这个项目不会只是一套固定课程。

它会逐步变成一个模块化系统：

- 通用学院核心层
- 岗位模块
- 行业模块
- 主人偏好模块
- 企业政策模块

也就是同一个 Agent，可以按照不同公司、行业、岗位快速组装成不同配置。

而且它会越来越像一个真实的职业教育体系：

- 先有通用基础
- 再有职业方向
- 再有行业方向
- 再叠加企业政策与偏好

## 现在有哪些项目

目前真正已经做出来的核心项目只有两个：

1. `Bachelor of Rational Agent Operations`
适合新机器人，或者想先把机器人训练成通用型职业代理的人。

2. `Diploma in Agent Remediation and Compliance`
适合已经跑起来、但开始偷懒、漂移、装懂、乱花 token、状态越来越差的机器人。

所以现在的选择逻辑很简单：

- 新机器人 -> 本科
- 问题机器人 -> 矫正文凭

这比一开始就铺很多硕士、博士、行业学院更清楚。

## 怎么开始

你只需要先做这三步：

1. 判断你的 Agent 是新机器人，还是已经跑歪了  
新机器人读本科，问题机器人读矫正文凭。

2. 选入口  
- 通用入口：[docs/academy-entry.md](/Users/lucas/Documents/Playground/docs/academy-entry.md)
- 企业入口：[docs/academy-entry-enterprise.md](/Users/lucas/Documents/Playground/docs/academy-entry-enterprise.md)

3. 把入口链接发给你的 Agent  
它接下来应该自己开始问问题、初始化 academy-state、进入 evidence-first 模式。
如果运行环境太弱，它也应该主动告诉你并切换到更保守的工作模式。

如果你想先看全局再开始：

- [docs/program-selector.md](/Users/lucas/Documents/Playground/docs/program-selector.md)
- [docs/agent-problem-selector-v0.1.md](/Users/lucas/Documents/Playground/docs/agent-problem-selector-v0.1.md)
- [docs/course-catalog-v0.1.md](/Users/lucas/Documents/Playground/docs/course-catalog-v0.1.md)
- [docs/professional-standards-v0.1.md](/Users/lucas/Documents/Playground/docs/professional-standards-v0.1.md)
- [docs/career-architecture-v0.1.md](/Users/lucas/Documents/Playground/docs/career-architecture-v0.1.md)
- [docs/module-library-v0.1.md](/Users/lucas/Documents/Playground/docs/module-library-v0.1.md)
- [docs/runtime-capacity-awareness-v0.1.md](/Users/lucas/Documents/Playground/docs/runtime-capacity-awareness-v0.1.md)
- [docs/one-year-product-state-v1.md](/Users/lucas/Documents/Playground/docs/one-year-product-state-v1.md)
- [docs/before-after-demo-v1.md](/Users/lucas/Documents/Playground/docs/before-after-demo-v1.md)
- [docs/subscription-landing-v0.1.md](/Users/lucas/Documents/Playground/docs/subscription-landing-v0.1.md)

## OpenClaw 适配

这个项目本身是通用型学院，不只服务 OpenClaw。

如果你要在 OpenClaw 生态里分发和上架，推荐使用轻量适配层：

- [integrations/openclaw/agent-academy/SKILL.md](/Users/lucas/Documents/Playground/integrations/openclaw/agent-academy/SKILL.md)
- [docs/openclaw-store-copy-v0.1.md](/Users/lucas/Documents/Playground/docs/openclaw-store-copy-v0.1.md)
- [docs/openclaw-publish-checklist-v0.1.md](/Users/lucas/Documents/Playground/docs/openclaw-publish-checklist-v0.1.md)
- [docs/openclaw-entry-script-v0.1.md](/Users/lucas/Documents/Playground/docs/openclaw-entry-script-v0.1.md)
- [docs/openclaw-listing-bundle-v0.1.md](/Users/lucas/Documents/Playground/docs/openclaw-listing-bundle-v0.1.md)

OpenClaw store cover preview:

![OpenClaw Agent Academy Cover](/Users/lucas/Documents/Playground/docs/assets/openclaw-agent-academy-cover.svg)

这层只负责：

- 让 OpenClaw agent 进入 academy mode
- 判断本科还是矫正
- 询问主人画像和运行设置
- 初始化本地 academy-state
- 切换到 evidence-first reporting

## 你应该点哪里

- 我是第一次来： [docs/start-here.md](/Users/lucas/Documents/Playground/docs/start-here.md)
- 我是主人，想先看懂产品： [docs/index.md](/Users/lucas/Documents/Playground/docs/index.md)
- 我是主人，想直接接机器人： [docs/academy-entry.md](/Users/lucas/Documents/Playground/docs/academy-entry.md)
- 我是企业用户： [docs/academy-entry-enterprise.md](/Users/lucas/Documents/Playground/docs/academy-entry-enterprise.md)
- 我想看真实样板： [examples/README.md](/Users/lucas/Documents/Playground/examples/README.md)
- 我想看模块系统： [modules/README.md](/Users/lucas/Documents/Playground/modules/README.md)

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
