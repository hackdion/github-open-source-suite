# 项目上下文强制协议

> 这是当前仓库在 SpecForge V3 下的项目上下文入口。任何项目级 Skill 在执行前，都必须先读取这里定义的上下文顺序。

## 1. 项目身份

- **项目名称**: 开源到 GitHub 的标准流程技能 / GitHub Open Source Suite
- **项目类型**: 文档与技能驱动的开源工作流仓库
- **核心目标**: 把“本地成果接近完成后的 GitHub 开源发布与维护流程”沉淀成可复用技能套件
- **主要交付物**:
  - 6 个 `oss-*` 技能
  - `shared/references` 中的共享规范
  - `shared/assets` 中的共享模板
  - 根级开源文件与 GitHub 社区文件
  - dogfood 报告与 release notes

## 2. 执行前必读顺序

在当前仓库执行任何 SpecForge 项目级技能前，必须按这个顺序建立认知：

1. `specs/` 下全部文档
2. [`README.md`](/Users/hackdion/Documents/开源到GitHub的标准流程-技能/README.md)
3. `docs/superpowers/specs/` 与 `docs/superpowers/plans/` 中的设计与实施文档
4. `docs/dogfood/` 中的真实仓库复盘
5. `docs/releases/` 与 [`CHANGELOG.md`](/Users/hackdion/Documents/开源到GitHub的标准流程-技能/CHANGELOG.md)
6. 目标技能目录下的 `SKILL.md`
7. `shared/references/` 中与当前任务直接相关的规范

如果任务涉及 GitHub 实际写入，还必须补读：

- [`SECURITY.md`](/Users/hackdion/Documents/开源到GitHub的标准流程-技能/SECURITY.md)
- [`SUPPORT.md`](/Users/hackdion/Documents/开源到GitHub的标准流程-技能/SUPPORT.md)
- [`.github/ISSUE_TEMPLATE/config.yml`](/Users/hackdion/Documents/开源到GitHub的标准流程-技能/.github/ISSUE_TEMPLATE/config.yml)

## 3. 事实优先级

遇到冲突时，按下面顺序判定事实：

1. 当前仓库文件与 git 状态
2. `specs/` 中的项目级定义
3. 根级入口文档与当前 release 文档
4. `docs/dogfood/` 中的经验结论
5. 历史设计/计划文档

禁止拿旧计划里的占位符或过期假设覆盖当前仓库事实。

## 4. 当前项目边界

这个仓库负责的是 GitHub 开源发布工作流的标准化，不负责：

- 替目标仓库写其业务功能实现
- 替目标仓库设计其完整产品文档
- 把所有协作问题都收敛成 GitHub 发布问题
- 覆盖 GitHub 以外平台的完整发布体系

## 5. 当前仓库的核心结构

- `oss-repo-bootstrap/`: 本地目录与 Git 基础准备
- `oss-repo-audit/`: 开源 readiness 审计
- `oss-community-files/`: 社区健康文件与模板
- `oss-publish-github/`: GitHub 发布准备
- `oss-release-management/`: 首发版与持续发版
- `oss-maintainer-operations/`: 发布后维护规则
- `shared/references/`: 共享规范
- `shared/assets/`: 共享模板
- `docs/dogfood/`: 真实仓库验证结论
- `docs/releases/`: 发布说明

## 6. 当前项目状态

截至当前文档生成时：

- 仓库已公开发布到 GitHub
- `v0.1.0` 作为 bootstrap draft 保留
- `v0.1.1` 与 `v0.1.2` 已发布
- 已完成至少两轮真实 dogfood
- 当前重点从“做出套件”转向“提高泛化质量与项目治理完整度”

## 7. 项目级任务的默认目标

在这个仓库内执行项目级 Skill 时，默认目标是：

- 补齐或维护项目治理文档
- 保持技能、共享规范、release 文档和 README 一致
- 让后续 SpecForge 流程可以直接接管该项目
- 不因为补项目文档而破坏当前已发布的技能行为
