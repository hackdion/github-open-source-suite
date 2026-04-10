---
name: github-open-source-suite
description: Use when a user wants one entry skill that can take a local project through the GitHub open-source workflow without manually choosing among bootstrap, audit, community files, publish prep, release management, and maintainer operations.
---

# GitHub Open Source Suite

## Overview

This is the suite entrypoint. Use it when the user wants the GitHub open-source workflow handled end-to-end through a single skill name instead of manually selecting the stage skill.

## Workflow

1. Inspect the current repository root, docs, and git state first.
2. Decide the current readiness stage.
3. Route to the narrowest stage skill that matches the real state.
4. If the user wants the full flow, keep chaining forward until a confirmation gate or blocker appears.
5. Do not duplicate stage-skill logic in this facade.

## Current-State Check

Check, in order:

- whether `.git/` exists
- whether the repo has any commits
- whether baseline community files exist
- whether the repo has already been audited
- whether publish metadata or release docs already exist
- whether the user is asking for a full run or just the next stage

If repository state is unclear, route to `oss-repo-audit`.

## Routing Map

- no git repo or no commits yet -> `oss-repo-bootstrap`
- git foundation exists but readiness is unknown -> `oss-repo-audit`
- community surface is missing or weak -> `oss-community-files`
- community surface is in place and GitHub publication prep is next -> `oss-publish-github`
- publish prep is in place and release framing is next -> `oss-release-management`
- post-publication support / issue / PR / security operations are the focus -> `oss-maintainer-operations`

## Full-Flow Rule

When the user says things like:

- "帮我开源到 GitHub"
- "从现在开始一路做完"
- "不要让我自己选技能"
- "用一个技能把这个项目整理并发布"

then this facade should keep routing forward across stage skills until one of these conditions is reached:

- a high-impact confirmation gate appears
- a required maintainer input is missing
- the requested workflow has completed and been verified
- the user explicitly asks to stop

## Guardrails

- This skill is a router, not the implementation layer.
- Do not rewrite the six stage workflows here.
- Do not skip local inspection just because the user asked for end-to-end execution.
- Do not claim publication, release, or completion unless the downstream stage actually verified it.
- Preserve the confirmation gates already defined by the stage skills.

## Recommended User Prompts

- "Use $github-open-source-suite to take this repo from local completion to GitHub open-source release."
- "Use $github-open-source-suite and decide the correct next stage automatically."
- "Use $github-open-source-suite to audit this project and continue until you hit a real confirmation gate."

## Suite Handoffs

- This facade should always hand off to one of the six `oss-*` skills for actual work.
- If the request becomes a repo-specific documentation problem rather than an open-source workflow problem, say so and stop routing deeper.
