---
name: oss-publish-github
description: Prepare a local repository for GitHub publication with low-risk drafting and clear confirmation gates for high-impact actions. Use when a user wants to publish a finished or nearly finished project to GitHub, needs repository metadata and publication prep, wants help before pushing publicly, or wants a draft of the first release package without automatically executing high-impact GitHub actions.
---

# OSS Publish GitHub

## Overview

Use this skill to prepare the repository for public GitHub publication. It should verify local prerequisites, draft GitHub-facing metadata, and pause for confirmation before remote or irreversible actions.

## Workflow

1. Confirm the repository is bootstrapped and audited.
2. Collect all blocking publication inputs in one pass.
3. Verify local publish prerequisites.
4. Draft repository metadata and publication checklist items.
5. Prepare first-release materials when requested.
6. Stop before push, repo creation, visibility changes, or publication.

## Required References

Always read:

- `../shared/references/github-community-health-baseline.md`
- `../shared/references/release-and-versioning-guide.md`
- `../shared/references/placeholder-and-sensitive-data-checklist.md`
- `../shared/references/publication-inputs-checklist.md`

Use `../shared/assets/releases/release-checklist.md` for publication readiness and `../shared/assets/releases/release-notes-template.md` when drafting first-release text.

## Upfront Inputs

Before any remote publication prep, gather the full blocking set in one pass:

- project title
- GitHub `owner`
- GitHub `repo` slug
- license choice
- documentation language
- support channel
- security reporting route
- whether GitHub Discussions should be enabled
- whether the agent may attempt browser-based GitHub settings changes
- whether a first release should be drafted

If the maintainer has known defaults, restate them once and continue. Do not interrupt execution with one-question-at-a-time follow-ups unless a new high-impact blocker appears.

## Preconditions

If any of these are missing, say so and recommend the right suite skill:

- no git repository -> `oss-repo-bootstrap`
- no baseline audit -> `oss-repo-audit`
- important community files missing -> `oss-community-files`

## Default Actions

Low-risk actions this skill may perform automatically:

- summarize remaining publish prerequisites
- draft repository description, topics, homepage suggestions, and support links
- draft release checklist text
- draft first-release notes

Actions that require explicit confirmation:

- creating a remote repository
- changing repository visibility
- pushing branches or tags
- publishing a GitHub release
- overwriting high-signal docs with materially different wording

## Output Expectations

Report:

- what is ready
- what still needs confirmation
- what high-impact action is next

Do not imply the repo is fully published unless the relevant remote action was actually completed and verified.
