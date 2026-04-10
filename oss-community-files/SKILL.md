---
name: oss-community-files
description: Generate or improve GitHub community health files and templates for an open-source repository. Use when a user wants README, LICENSE guidance, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, SUPPORT, issue forms, pull request templates, or `.github` layout created in a repository-aware and sustainable way instead of using generic boilerplate.
---

# OSS Community Files

## Overview

Use this skill to create or improve the repository’s community-facing file set with shared templates and clear placeholders. Keep the file set minimal, accurate, and maintainable.

## Workflow

1. Audit what community files already exist.
2. Collect all blocking publication inputs in one pass.
3. Determine the minimum healthy set for the repo type and readiness state.
4. Load the relevant shared references and templates.
5. Fill templates with repository-aware content and explicit placeholders.
6. Report what still needs maintainer-specific values.

## Required References

Always read:

- `../shared/references/github-community-health-baseline.md`
- `../shared/references/repo-classification-guide.md`
- `../shared/references/maintainer-ops-guide.md`
- `../shared/references/placeholder-and-sensitive-data-checklist.md`
- `../shared/references/publication-inputs-checklist.md`

## Upfront Inputs

Before writing root docs or `.github` files, gather the blocking inputs in one pass:

- project title
- GitHub `owner`
- GitHub `repo` slug
- license choice
- documentation language
- support channel
- security reporting route
- whether GitHub Discussions should be enabled

At minimum, offer these license choices:

- `MIT`
- `Apache-2.0`
- `BSD-3-Clause`
- `GPL-3.0`

If the maintainer has known defaults, apply them explicitly instead of re-asking later.

## Templates

Use shared templates instead of improvising:

- `../shared/assets/community/README-template.md`
- `../shared/assets/community/CONTRIBUTING-template.md`
- `../shared/assets/community/CODE_OF_CONDUCT-template.md`
- `../shared/assets/community/SECURITY-template.md`
- `../shared/assets/community/SUPPORT-template.md`
- `../shared/assets/community/pull_request_template.md`
- `../shared/assets/community/ISSUE_TEMPLATE/bug_report.yml`
- `../shared/assets/community/ISSUE_TEMPLATE/feature_request.yml`
- `../shared/assets/community/ISSUE_TEMPLATE/config.yml`

## File Generation Rules

- Reuse existing good project-specific content when possible.
- Keep placeholder tokens explicit, such as `{{PROJECT_NAME}}`.
- Do not invent maintainer emails, URLs, support guarantees, or security SLAs.
- Do not confuse local-use milestones, passing validators, or an existing `README`/`LICENSE` with a complete public community surface.
- If the repo has no commits yet or maintainer routing is still undecided, prefer the minimum sustainable public surface and leave the unresolved policy values explicit.
- If the repository is tiny, justify any omitted files rather than generating everything blindly.
- For early single-skill or draft repositories, avoid generating every optional document unless the maintainer actually wants that surface area.
- Prefer GitHub-recognized locations when writing files.

## Completion Rules

After filling or drafting files:

- list any unresolved placeholders
- identify which values need maintainer confirmation
- note whether a follow-up publish or release skill should be used next

## Suite Handoffs

- Recommend `oss-repo-bootstrap` when the repository still lacks a stable git foundation or initial commit.
- Recommend `oss-repo-audit` first when repository state is still unclear.
- Recommend `oss-publish-github` only after the repo has at least one commit and the community file set is in good shape.
- Recommend `oss-maintainer-operations` when the user wants stronger post-publication triage rules.
