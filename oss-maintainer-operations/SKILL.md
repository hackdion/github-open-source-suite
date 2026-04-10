---
name: oss-maintainer-operations
description: Define sustainable maintainer operations for an open-source repository after publication. Use when a user wants issue triage rules, pull request intake guidance, support boundaries, security reporting routes, contribution expectations, or long-term maintenance wording that reduces chaos without over-promising maintainer availability.
---

# OSS Maintainer Operations

## Overview

Use this skill to define a sustainable post-publication operating model for the repository. Keep maintainer guidance clear, realistic, and consistent with the community files and support routes already in the repo.

## Workflow

1. Inspect existing support, contribution, and security documents.
2. Load the maintainer operations baseline.
3. Draft or refine rules for issue intake, PR intake, support routing, and security handling.
4. Align the wording with existing community files and actual maintainer capacity.
5. Report any policy gaps or over-commitments that still need revision.

## Required References

Always read:

- `../shared/references/maintainer-ops-guide.md`
- `../shared/references/github-community-health-baseline.md`

Use:

- `../shared/assets/maintenance/triage-playbook.md`

## Operating Rules

- Prefer public support channels over private personal contact unless the maintainer explicitly wants private routing.
- Separate support questions from vulnerability reporting.
- State when the project is maintained in spare time if that is true.
- Use labels and triage categories only as far as the maintainer can sustain them.

## Suite Handoffs

- Recommend `oss-community-files` if `SUPPORT.md`, `CONTRIBUTING.md`, or `SECURITY.md` do not exist yet.
- Recommend `oss-release-management` when the user wants maintenance rules reflected in future release notes or release cadence language.

## Output Expectations

Report:

- proposed support flow
- issue and PR intake rules
- security reporting route
- any promises that should be softened before publication
