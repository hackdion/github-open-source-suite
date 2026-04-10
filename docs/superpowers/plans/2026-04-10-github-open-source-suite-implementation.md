# GitHub Open Source Suite Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the first working version of the GitHub open source skill suite in the current directory, including git bootstrap, shared references and templates, and six reusable skills.

**Architecture:** Use the current directory as the suite root. Keep shared guidance in top-level `shared/references` and `shared/assets`, and keep each skill in its own folder with a short `SKILL.md` plus `agents/openai.yaml`. Initialize the repository first, then create reusable suite assets, then create the six skills, then validate and smoke-test.

**Tech Stack:** Git, Markdown, YAML, Python utility scripts from `skill-creator`

---

### Task 1: Initialize The Repository Root

**Files:**
- Create: `.git/` via `git init`
- Create: `/Users/hackdion/Documents/开源到GitHub的标准流程-技能/.gitignore`

- [ ] **Step 1: Verify the directory is not already a git repository**

Run:

```bash
git rev-parse --is-inside-work-tree
```

Expected: non-zero exit code with a "not a git repository" message.

- [ ] **Step 2: Initialize git for the current directory**

Run:

```bash
git init
```

Expected: a new `.git/` directory exists and Git reports the repository was initialized.

- [ ] **Step 3: Add a minimal `.gitignore` suited for a documentation-plus-skill repo**

Write:

```gitignore
.DS_Store
Thumbs.db
*.log
.env
.env.*
__pycache__/
*.pyc
```

- [ ] **Step 4: Verify git now recognizes the repository root**

Run:

```bash
git rev-parse --show-toplevel
git status --short --branch
```

Expected: the top-level path is the current directory and Git shows untracked files.

### Task 2: Create The Suite Skeleton

**Files:**
- Create: `/Users/hackdion/Documents/开源到GitHub的标准流程-技能/shared/references/.gitkeep`
- Create: `/Users/hackdion/Documents/开源到GitHub的标准流程-技能/shared/assets/community/.gitkeep`
- Create: `/Users/hackdion/Documents/开源到GitHub的标准流程-技能/shared/assets/releases/.gitkeep`
- Create: `/Users/hackdion/Documents/开源到GitHub的标准流程-技能/shared/assets/maintenance/.gitkeep`

- [ ] **Step 1: Create the shared suite directories**

Run:

```bash
mkdir -p \
  shared/references \
  shared/assets/community/ISSUE_TEMPLATE \
  shared/assets/releases \
  shared/assets/maintenance
```

Expected: the shared directory tree exists.

- [ ] **Step 2: Add placeholder keep files so empty directories remain tracked**

Create these empty files:

```text
shared/references/.gitkeep
shared/assets/community/.gitkeep
shared/assets/community/ISSUE_TEMPLATE/.gitkeep
shared/assets/releases/.gitkeep
shared/assets/maintenance/.gitkeep
```

- [ ] **Step 3: Verify the suite skeleton exists**

Run:

```bash
find shared -maxdepth 3 -type d | sort
```

Expected: the output lists `shared/references`, `shared/assets/community`, `shared/assets/community/ISSUE_TEMPLATE`, `shared/assets/releases`, and `shared/assets/maintenance`.

### Task 3: Create Shared References And Templates

**Files:**
- Create: `shared/references/github-community-health-baseline.md`
- Create: `shared/references/repo-classification-guide.md`
- Create: `shared/references/release-and-versioning-guide.md`
- Create: `shared/references/maintainer-ops-guide.md`
- Create: `shared/references/placeholder-and-sensitive-data-checklist.md`
- Create: `shared/references/official-sources.md`
- Create: `shared/assets/community/README-template.md`
- Create: `shared/assets/community/CONTRIBUTING-template.md`
- Create: `shared/assets/community/CODE_OF_CONDUCT-template.md`
- Create: `shared/assets/community/SECURITY-template.md`
- Create: `shared/assets/community/SUPPORT-template.md`
- Create: `shared/assets/community/pull_request_template.md`
- Create: `shared/assets/community/ISSUE_TEMPLATE/bug_report.yml`
- Create: `shared/assets/community/ISSUE_TEMPLATE/feature_request.yml`
- Create: `shared/assets/community/ISSUE_TEMPLATE/config.yml`
- Create: `shared/assets/releases/release-checklist.md`
- Create: `shared/assets/releases/release-notes-template.md`
- Create: `shared/assets/maintenance/triage-playbook.md`

- [ ] **Step 1: Write the shared references from the approved spec**

Each reference file must be concise, operational, and reusable across repo types. It must prefer GitHub official guidance over informal blog practices.

- [ ] **Step 2: Write the community and release templates with explicit placeholder tokens**

Use a consistent token format such as:

```text
{{PROJECT_NAME}}
{{MAINTAINER_CONTACT}}
{{SUPPORT_CHANNEL}}
```

Every template must avoid over-promising maintainer responsiveness.

- [ ] **Step 3: Verify the shared assets were created**

Run:

```bash
find shared -type f | sort
```

Expected: the output lists all shared reference and template files.

### Task 4: Initialize The Six Skill Folders

**Files:**
- Create: `oss-repo-bootstrap/`
- Create: `oss-repo-audit/`
- Create: `oss-community-files/`
- Create: `oss-publish-github/`
- Create: `oss-release-management/`
- Create: `oss-maintainer-operations/`

- [ ] **Step 1: Generate each skill folder with `init_skill.py`**

Run:

```bash
python3 /Users/hackdion/.codex/skills/.system/skill-creator/scripts/init_skill.py oss-repo-bootstrap --path /Users/hackdion/Documents/开源到GitHub的标准流程-技能 --interface display_name="OSS Repo Bootstrap" --interface short_description="Bootstrap local repos for GitHub" --interface default_prompt="Use $oss-repo-bootstrap to turn this local folder into a git-backed open-source-ready repository."
python3 /Users/hackdion/.codex/skills/.system/skill-creator/scripts/init_skill.py oss-repo-audit --path /Users/hackdion/Documents/开源到GitHub的标准流程-技能 --interface display_name="OSS Repo Audit" --interface short_description="Audit open-source readiness" --interface default_prompt="Use $oss-repo-audit to inspect this repository and list the gaps before publishing it on GitHub."
python3 /Users/hackdion/.codex/skills/.system/skill-creator/scripts/init_skill.py oss-community-files --path /Users/hackdion/Documents/开源到GitHub的标准流程-技能 --interface display_name="OSS Community Files" --interface short_description="Create GitHub health files" --interface default_prompt="Use $oss-community-files to generate repository-aware community health files and templates for this project."
python3 /Users/hackdion/.codex/skills/.system/skill-creator/scripts/init_skill.py oss-publish-github --path /Users/hackdion/Documents/开源到GitHub的标准流程-技能 --interface display_name="OSS Publish GitHub" --interface short_description="Prepare GitHub publication" --interface default_prompt="Use $oss-publish-github to prepare this repository for GitHub publication and draft the required metadata."
python3 /Users/hackdion/.codex/skills/.system/skill-creator/scripts/init_skill.py oss-release-management --path /Users/hackdion/Documents/开源到GitHub的标准流程-技能 --interface display_name="OSS Release Management" --interface short_description="Standardize project releases" --interface default_prompt="Use $oss-release-management to prepare a release checklist, version notes, and GitHub release draft for this project."
python3 /Users/hackdion/.codex/skills/.system/skill-creator/scripts/init_skill.py oss-maintainer-operations --path /Users/hackdion/Documents/开源到GitHub的标准流程-技能 --interface display_name="OSS Maintainer Operations" --interface short_description="Set up maintainer operations" --interface default_prompt="Use $oss-maintainer-operations to define sustainable issue, PR, support, and security workflows for this repository."
```

Expected: each skill folder contains `SKILL.md` and `agents/openai.yaml`.

- [ ] **Step 2: Verify all skill folders were created**

Run:

```bash
find . -maxdepth 2 -name SKILL.md | sort
find . -maxdepth 3 -path "*/agents/openai.yaml" | sort
```

Expected: six `SKILL.md` files and six `agents/openai.yaml` files appear.

### Task 5: Write The Initial Skill Content

**Files:**
- Modify: `oss-repo-bootstrap/SKILL.md`
- Modify: `oss-repo-audit/SKILL.md`
- Modify: `oss-community-files/SKILL.md`
- Modify: `oss-publish-github/SKILL.md`
- Modify: `oss-release-management/SKILL.md`
- Modify: `oss-maintainer-operations/SKILL.md`

- [ ] **Step 1: Write concise frontmatter descriptions that trigger on the right user requests**

Each `description` must say what the skill does and when it should be used.

- [ ] **Step 2: Write workflow instructions that point to shared references and templates**

Each skill body must:

```text
- inspect local context first
- read only the relevant shared reference files
- use the shared templates instead of improvising
- distinguish low-risk auto actions from high-impact actions that need confirmation
- avoid completion claims without fresh verification
```

- [ ] **Step 3: Cross-link the suite so each skill knows when to recommend another skill**

Examples:

```text
oss-repo-audit -> recommend oss-repo-bootstrap when no git repo exists
oss-publish-github -> recommend oss-community-files when community health files are missing
oss-release-management -> recommend oss-publish-github when publish prerequisites are absent
```

### Task 6: Validate And Smoke-Test The Suite

**Files:**
- Validate: all six skill folders

- [ ] **Step 1: Run quick validation on each skill**

Run:

```bash
python3 /Users/hackdion/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/hackdion/Documents/开源到GitHub的标准流程-技能/oss-repo-bootstrap
python3 /Users/hackdion/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/hackdion/Documents/开源到GitHub的标准流程-技能/oss-repo-audit
python3 /Users/hackdion/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/hackdion/Documents/开源到GitHub的标准流程-技能/oss-community-files
python3 /Users/hackdion/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/hackdion/Documents/开源到GitHub的标准流程-技能/oss-publish-github
python3 /Users/hackdion/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/hackdion/Documents/开源到GitHub的标准流程-技能/oss-release-management
python3 /Users/hackdion/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/hackdion/Documents/开源到GitHub的标准流程-技能/oss-maintainer-operations
```

Expected: all validations exit successfully.

- [ ] **Step 2: Run a suite smoke check for file layout**

Run:

```bash
find /Users/hackdion/Documents/开源到GitHub的标准流程-技能 -maxdepth 3 \( -name SKILL.md -o -path "*/agents/openai.yaml" -o -path "*/shared/*" \) | sort
```

Expected: the output shows the shared resources and all skill metadata files.

- [ ] **Step 3: Record git status after initialization**

Run:

```bash
git status --short
```

Expected: all newly created suite files are visible as untracked or modified files.
