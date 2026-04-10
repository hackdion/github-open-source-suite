# Dogfood Friction Report: opencode-for-codex-skill

Target repository:

- `/Users/hackdion/Documents/opencode-for-codex-skill`

Mode:

- read-only evaluation
- no file edits in target repository

## Summary

The suite behaves correctly on an already structured repository. The main gaps are not structural failures. They are decision quality and wording precision in two places:

- classify security-reporting limitations as policy risk, not only file-presence success
- distinguish history divergence from content divergence in publication readiness

## Findings By Required Category

### 1) Wrong assumptions

- Assumption risk: passing community-file presence may hide a weak security reporting channel.
- Impact: audit can overstate readiness when `SECURITY.md` exists but private vulnerability intake is missing.
- Fix applied: `oss-repo-audit` now explicitly marks this as policy risk.

### 2) Missing upfront inputs

- No blocking gap found in this run.
- `oss-community-files` and `oss-publish-github` already enforce one-shot upfront input collection.

### 3) Template overreach

- No major template overreach found on this target.
- Minor guidance gap found in release framing: avoid turning long-lived release docs into one-time runbooks.
- Fix applied: `oss-release-management` now explicitly enforces durable guidance style.

### 4) Handoff ambiguity

- Handoff quality was mostly correct (`oss-repo-audit` -> `oss-publish-github`).
- Ambiguity risk: publish stage may treat git ancestry divergence as a content blocker.
- Fix applied: `oss-publish-github` now distinguishes content parity from history divergence and defaults to incremental publication guidance.

## Evidence Snapshot

- Target repo baseline community files are present (`README`, `LICENSE`, `CONTRIBUTING`, `CODE_OF_CONDUCT`, `SECURITY`, `SUPPORT`, issue/PR templates).
- Release documentation already exists (`RELEASE.md`, `docs/release-notes/v0.1.0.md`, `CHANGELOG.md`).
- Dogfood completed without mutating the target repository.

## Applied Improvements In This Suite

- Updated `oss-repo-audit/SKILL.md`
- Updated `oss-publish-github/SKILL.md`
- Updated `oss-release-management/SKILL.md`
