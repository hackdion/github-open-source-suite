# 开源到 GitHub 的标准流程技能 / GitHub Open Source Suite

一个面向 Codex 的技能套件，用来把“已经开发得差不多的本地成果”整理成适合开源到 GitHub 的仓库，并继续支持首发版和后续维护。

A Codex skill suite for turning nearly finished local work into GitHub-ready open-source repositories, then supporting first release and long-term maintainer operations.

## 中文简介

这个仓库解决的是一类反复出现的问题：

- 技能、MCP、插件、小中型项目做完之后，开源到 GitHub 总要重新梳理一遍流程
- README、LICENSE、SECURITY、SUPPORT、issue 模板、PR 模板这些文件总是临时拼装
- 发版和后期维护经常缺少统一标准

这个仓库把这些步骤沉淀成 6 个可复用技能：

1. `oss-repo-bootstrap`
2. `oss-repo-audit`
3. `oss-community-files`
4. `oss-publish-github`
5. `oss-release-management`
6. `oss-maintainer-operations`

## English Overview

This repository packages a six-skill workflow for open-source publication on GitHub. It is intended for skill repositories, MCP servers, plugins, libraries, CLI tools, and small-to-medium projects that are already mostly built and now need a repeatable publishing and maintenance path.

## 工作流 / Workflow

默认推荐流程：

1. 先把本地目录整理成可管理的仓库
2. 做开源体检和仓库类型判断
3. 生成或补齐社区健康文件
4. 准备 GitHub 发布信息与仓库设置
5. 草拟首个 release
6. 建立后续维护规则

Recommended flow:

1. bootstrap the local directory as a repository
2. audit open-source readiness
3. generate community health files
4. prepare GitHub publication details and settings
5. draft the first release
6. define maintainer operations

## 仓库默认配置 / Repository Defaults

本仓库当前采用这些默认值：

- GitHub owner: `hackdion`
- GitHub repo slug: `github-open-source-suite`
- 项目显示名称: `开源到 GitHub 的标准流程技能`
- License: `Apache-2.0`
- 文档语言: 中文 + English
- 支持渠道: GitHub Discussions + Issues
- 安全流程: 本地先写 `SECURITY.md`，仓库公开后优先启用 GitHub private vulnerability reporting

## 目录结构 / Repository Structure

```text
specs/
docs/
  superpowers/
    specs/
    plans/
oss-repo-bootstrap/
oss-repo-audit/
oss-community-files/
oss-publish-github/
oss-release-management/
oss-maintainer-operations/
scripts/
tests/
shared/
  references/
  assets/
```

## SpecForge 项目文档 / SpecForge Project Docs

当前仓库已经补齐最小 SpecForge V3 项目资产，见 [`specs/`](./specs/)：

- `PROJECT-CONTEXT.md`
- `GUARDRAILS.md`
- `已澄清的项目描述.md`
- `产品概述.md`
- `技术栈.md`
- `项目结构.md`
- `开发规范.md`
- `开发路线图.md`

## 使用方式 / How To Use

在 Codex 中按需调用对应技能。例如：

- 用 `oss-repo-audit` 检查仓库是否达到开源基线
- 用 `oss-community-files` 生成根级开源文件和 `.github` 模板
- 用 `oss-publish-github` 准备仓库设置、发布元数据与 release 草稿

Use the relevant skill for the stage you are in. For example:

- use `oss-repo-audit` to check whether a repo meets the open-source baseline
- use `oss-community-files` to generate root docs and `.github` templates
- use `oss-publish-github` to prepare repository settings, metadata, and release drafts

## 本地验证 / Local Verification

当前仓库已经把常用门禁收敛到 [`scripts/verify_project.py`](./scripts/verify_project.py)：

```bash
python3 scripts/verify_project.py local
python3 scripts/verify_project.py local --require-clean-worktree
python3 scripts/verify_project.py github \
  --repo hackdion/github-open-source-suite \
  --expect-public \
  --expect-issues-enabled \
  --expect-discussions-enabled \
  --expect-private-vulnerability-reporting \
  --release-tag v0.1.2 \
  --expect-release-published
```

配套单元测试见 [`tests/test_verify_project.py`](./tests/test_verify_project.py)。

## 首发版草稿 / Initial Release Draft

See [`docs/releases/v0.1.0-draft.md`](./docs/releases/v0.1.0-draft.md).

## Contributing

See [`CONTRIBUTING.md`](./CONTRIBUTING.md).

## Support

See [`SUPPORT.md`](./SUPPORT.md).

## Security

See [`SECURITY.md`](./SECURITY.md).

## License

This repository is licensed under Apache-2.0. See [`LICENSE`](./LICENSE).
