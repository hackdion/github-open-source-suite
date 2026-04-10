---
name: oss-repo-audit
description: Audit a local repository for open-source readiness before GitHub publication. Use when a user says to check whether a repo is ready to open source, wants a gap analysis before pushing publicly, wants a prioritized checklist of missing GitHub community health files, or needs placeholder, secrets, and sustainability risks identified before publishing.
---

# OSS Repo Audit

## Overview

Use this skill to inspect the repository, classify it, compare it against the GitHub open-source baseline, and produce a prioritized readiness checklist. Inspect local facts first and do not jump straight into writing files.

## Workflow

1. Inspect the repository root, docs, manifests, and git state.
2. Classify the repository type.
3. Compare the repo against the community-health baseline.
4. Scan for placeholders, private references, and sustainability risks.
5. Decide whether the next step is bootstrap, community files, publish prep, or release prep.

## Required References

Load these before scoring gaps:

- `../shared/references/repo-classification-guide.md`
- `../shared/references/github-community-health-baseline.md`
- `../shared/references/placeholder-and-sensitive-data-checklist.md`

Load `../shared/references/release-and-versioning-guide.md` only when release-readiness is part of the audit request.

## Audit Rules

- Prefer the minimum sustainable file set for the repo type.
- Flag missing legal or operational essentials before cosmetic improvements.
- Distinguish blockers from nice-to-haves.
- Distinguish hard blockers from policy risks. Example: security reporting that only routes to public issues should be flagged as a policy risk even if baseline files exist.
- Name any placeholders that must be replaced before publication.
- Call out support or policy wording that promises more than the maintainer can sustain.

## Output Format

Report in four parts:

1. repository type and evidence
2. blockers
3. recommended next actions
4. suggested suite handoff

If the current directory is not a git repo, stop the audit and recommend `oss-repo-bootstrap`.

## Suite Handoffs

- Recommend `oss-repo-bootstrap` when there is no usable git repository.
- Recommend `oss-community-files` when baseline documents or templates are missing.
- Recommend `oss-publish-github` when local readiness is good and GitHub publication prep is next.
- Recommend `oss-release-management` only after publish prerequisites are largely in place.
