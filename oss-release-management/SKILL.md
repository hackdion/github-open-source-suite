---
name: oss-release-management
description: Standardize first-release and ongoing release work for an open-source repository. Use when a user wants to prepare release notes, choose an initial version, decide between pre-release and stable release, build a release checklist, or keep future releases consistent without rediscovering GitHub release practices every time.
---

# OSS Release Management

## Overview

Use this skill to turn a prepared repository state into a repeatable release workflow. Keep release framing honest, lightweight, and appropriate for the project’s maturity.

## Workflow

1. Verify whether publish prerequisites were already checked.
2. Choose a release framing that matches project maturity.
3. Draft a release checklist, version label, and notes.
4. Call out anything that blocks a trustworthy release.
5. Hand off to GitHub publication only after confirmation gates are satisfied.

## Required References

Always read:

- `../shared/references/release-and-versioning-guide.md`
- `../shared/references/placeholder-and-sensitive-data-checklist.md`
- `../shared/references/publication-inputs-checklist.md`

Use:

- `../shared/assets/releases/release-checklist.md`
- `../shared/assets/releases/release-notes-template.md`

## Release Rules

- Prefer `0.x` framing for early projects unless there is a strong reason not to.
- Do not label a release as stable when onboarding, docs, or scope are still obviously unstable.
- Keep "Known limitations" visible when the project is young.
- Avoid promising compatibility guarantees that are not documented elsewhere.

## Preconditions

If the repository has not been audited or publication prep is incomplete, recommend:

- `oss-repo-audit`
- `oss-community-files`
- `oss-publish-github`

Before release drafting, make sure the blocking publication inputs were already collected in one pass. If they were not, direct the flow through `oss-publish-github` instead of asking scattered follow-up questions.

## Output Expectations

Report:

- suggested version label
- pre-release versus stable recommendation
- release highlights
- known limitations
- remaining blockers before an actual release can be published
