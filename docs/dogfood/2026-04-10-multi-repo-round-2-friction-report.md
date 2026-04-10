# Dogfood Friction Report: Multi-Repo Round 2

Target repositories:

- `/Users/hackdion/Documents/防停摆-技能`
- `/Users/hackdion/Documents/独立复核-技能`
- `/Users/hackdion/Documents/避免重复造轮子`

Mode:

- read-only evaluation
- no file edits in target repositories

## Summary

The suite handled the three target repositories without mutating them, but the second round exposed a shared decision-quality gap:

- repository type was not enough; the suite also needed an explicit readiness model
- local maturity signals were too easy to overread as publication readiness
- handoff order needed to be stricter for repos that are useful locally but not yet ready for GitHub publication

## Cross-Repo Findings By Required Category

### 1) Wrong assumptions

- Assumption risk: a repo that is useful locally, passes validators, or already has some root files may still be far from public-ready.
- Evidence:
  - `防停摆-技能` had no commits yet and all files were untracked.
  - `避免重复造轮子` was locally coherent but still lacked the public-facing GitHub community baseline.
  - `独立复核-技能` had real content, but its main issues were documentation and handoff precision, not open-source packaging gaps.
- Fix applied: the suite now separates repository type from readiness state and treats "no commits yet" or "local V1 complete" as earlier-stage signals.

### 2) Missing upfront inputs

- The maintainer-input checklist itself was already sufficient.
- The real gap was stage discipline: the suite needed to stop pretending those inputs mattered only at publish time when the repo had not even crossed the bootstrap or community-surface threshold yet.
- Fix applied: `oss-publish-github` and `oss-release-management` now reject premature use when the repo is still missing first-commit or public-surface prerequisites.

### 3) Template overreach

- Early or single-skill repositories do not always need every optional community document immediately.
- Evidence:
  - `防停摆-技能` still needed a clean first public surface and maintainer routing choices.
  - `避免重复造轮子` needed clearer sequencing more than heavier templating.
- Fix applied: `oss-community-files` now prefers the minimum sustainable public surface for early repositories and avoids treating partial file presence as full public readiness.

### 4) Handoff ambiguity

- Handoff order was too easy to blur for repos that were locally mature but not open-source ready.
- Evidence:
  - `避免重复造轮子` pointed toward several next steps at once, where the correct order should have been community files -> publish prep -> release management.
  - `独立复核-技能` needed a documentation-oriented next step more than GitHub publication work.
- Fix applied: `oss-repo-audit` now reports readiness state explicitly and tightens suite handoff rules.

## Per-Repository Snapshot

### 防停摆-技能

- Git state during evaluation: `No commits yet on main`
- Best next suite step under the refined rules: `oss-repo-bootstrap`, then `oss-community-files`
- Main lesson for this suite: no-commit repos must not be treated as publish candidates

### 独立复核-技能

- Git state during evaluation: existing repo with user modifications already in progress
- Best next step for that repo: `project-doc-updater`
- Main lesson for this suite: not every repo with friction needs GitHub packaging changes; some need clearer internal docs and output contracts

### 避免重复造轮子

- Git state during evaluation: active feature branch, no dirty output from this dogfood run
- Best next suite step: `oss-community-files`
- Main lesson for this suite: local usefulness and validator success do not equal open-source publish readiness

## Applied Improvements In This Suite

- Updated `shared/references/repo-classification-guide.md`
- Updated `oss-repo-audit/SKILL.md`
- Updated `oss-community-files/SKILL.md`
- Updated `oss-publish-github/SKILL.md`
- Updated `oss-release-management/SKILL.md`
