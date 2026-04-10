# Changelog

All notable changes to this repository will be documented in this file.

## [Unreleased]

- Ongoing refinement of the six-skill suite, shared references, and shared templates.
- Added initial SpecForge V3 project governance documents under `specs/`.
- Added repository-local validation automation in `scripts/verify_project.py` with regression tests in `tests/test_verify_project.py`.

## [0.1.2] - Multi-Repo Readiness Refinement

### Changed

- added explicit readiness states to repository classification so repo type and publication maturity are scored separately
- tightened `oss-repo-audit` to route no-commit repositories back to bootstrap and to report readiness state explicitly
- tightened `oss-community-files` so early or single-skill repos get the minimum sustainable public surface instead of over-generated community docs
- tightened `oss-publish-github` so local validator success or internal milestones do not masquerade as publication readiness
- tightened `oss-release-management` so local-only completion does not trigger premature release drafting

### Added

- second-round multi-repo dogfood report covering `防停摆-技能`, `独立复核-技能`, and `避免重复造轮子`
- `v0.1.2` release notes

## [0.1.1] - Dogfood Refinement Release

### Changed

- tightened `oss-repo-audit` to classify weak security intake as policy risk
- tightened `oss-publish-github` to distinguish content parity from git-history divergence
- tightened `oss-release-management` to avoid over-prescriptive one-time runbook guidance

### Added

- dogfood friction report for `opencode-for-codex-skill`
- `v0.1.1` release notes

## [0.1.0] - Draft Initial Public Release

### Added

- six core skills for repository bootstrap, audit, community files, publication, release management, and maintainer operations
- shared references for GitHub community health, repo classification, release guidance, maintainer operations, placeholders, official sources, and upfront publication inputs
- shared templates for README, contributing, support, security, issue forms, pull requests, release notes, and maintainer triage
- root repository community-health files and `.github` templates for this repository itself
