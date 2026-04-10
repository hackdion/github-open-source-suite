---
name: oss-repo-bootstrap
description: Bootstrap a local folder into a git-backed repository that is ready for the rest of an open-source GitHub workflow. Use when a project is mostly developed but the current directory is not a git repo yet, has no initial repo hygiene, needs a starter `.gitignore`, needs a first-commit plan, or needs to be prepared before running open-source audit and publishing skills.
---

# OSS Repo Bootstrap

## Overview

Use this skill to turn a local directory into a repository foundation for open-source work. Start local-first, keep changes minimal, and stop before high-impact remote actions.

## Workflow

1. Inspect the directory first.
2. Check whether Git is already initialized.
3. Classify the repository type before suggesting `.gitignore` or first-commit hygiene.
4. Make only low-risk local changes automatically.
5. Hand off to `oss-repo-audit` once the repository can be assessed normally.

## Local Inspection

Check, in order:

- top-level files and folders
- dependency or runtime manifests
- whether `.git/` exists
- whether `.gitignore` exists
- whether there are already commits

Read `../shared/references/repo-classification-guide.md` when deciding what kind of repo this is.

## Default Actions

Low-risk local actions this skill may perform automatically:

- run `git init` when the folder is not already a repository
- create or improve a minimal `.gitignore`
- report whether a first commit is still needed
- suggest an initial branch and repository hygiene checklist

High-impact actions that require explicit confirmation:

- adding or changing remotes
- pushing to GitHub
- deleting tracked files
- rewriting history
- making visibility or publication decisions

## Output Expectations

Report:

- whether the directory is now a git repo
- what local hygiene files were added or changed
- what still blocks open-source readiness
- whether the next step should be `oss-repo-audit`

Do not claim the project is publish-ready. This skill only prepares the floor.

## Suite Handoffs

- If the repo exists and basic hygiene is in place, recommend `oss-repo-audit`.
- If community files are already missing in an otherwise healthy repo, point to `oss-community-files`.

## Shared Resources

Read only what is needed:

- `../shared/references/repo-classification-guide.md`
- `../shared/references/placeholder-and-sensitive-data-checklist.md` when checking whether sample files contain accidental secrets
