#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_QUICK_VALIDATE = (
    Path.home() / ".codex" / "skills" / ".system" / "skill-creator" / "scripts" / "quick_validate.py"
)
REQUIRED_SPECS = [
    "PROJECT-CONTEXT.md",
    "GUARDRAILS.md",
    "已澄清的项目描述.md",
    "产品概述.md",
    "技术栈.md",
    "项目结构.md",
    "开发规范.md",
    "开发路线图.md",
]
REQUIRED_SKILLS = [
    "github-open-source-suite",
    "oss-repo-bootstrap",
    "oss-repo-audit",
    "oss-community-files",
    "oss-publish-github",
    "oss-release-management",
    "oss-maintainer-operations",
]
PUBLIC_DOC_TARGETS = [
    "README.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "SUPPORT.md",
    "docs/dogfood",
    "docs/releases",
    "specs",
]
PLACEHOLDER_RE = re.compile(r"\{\{[^}]+\}\}")
TBD_RE = re.compile(r"\bTBD\b")


def strip_markdown_code(text: str) -> str:
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"`[^`\n]+`", "", text)
    return text


def find_unresolved_tokens(text: str) -> list[str]:
    cleaned = strip_markdown_code(text)
    hits: list[str] = []
    seen: set[str] = set()

    for match in PLACEHOLDER_RE.finditer(cleaned):
        token = match.group(0)
        if token not in seen:
            hits.append(token)
            seen.add(token)

    for match in TBD_RE.finditer(cleaned):
        token = match.group(0)
        if token not in seen:
            hits.append(token)
            seen.add(token)

    return hits


def iter_public_doc_targets(root: Path) -> list[Path]:
    targets: list[Path] = []
    for rel in PUBLIC_DOC_TARGETS:
        path = root / rel
        if path.exists():
            targets.append(path)
    return targets


def iter_public_doc_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for target in iter_public_doc_targets(root):
        if target.is_file():
            files.append(target)
            continue
        files.extend(sorted(path for path in target.rglob("*") if path.is_file()))
    return files


def run_command(args: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=cwd, text=True, capture_output=True)


def print_ok(message: str) -> None:
    print(f"[OK] {message}")


def print_fail(message: str) -> None:
    print(f"[FAIL] {message}")


def verify_specs(root: Path) -> list[str]:
    specs_root = root / "specs"
    missing = [name for name in REQUIRED_SPECS if not (specs_root / name).exists()]
    if missing:
        print_fail(f"Missing SpecForge docs: {', '.join(missing)}")
    else:
        print_ok("Required SpecForge docs are present")
    return missing


def verify_skills(root: Path, quick_validate: Path) -> list[str]:
    failures: list[str] = []
    if not quick_validate.exists():
        failures.append(f"quick_validate.py not found: {quick_validate}")
        print_fail(failures[-1])
        return failures

    for skill_name in REQUIRED_SKILLS:
        skill_dir = root / skill_name
        result = run_command([sys.executable, str(quick_validate), str(skill_dir)], root)
        if result.returncode != 0:
            failures.append(f"{skill_name}: {result.stdout.strip() or result.stderr.strip()}")
            print_fail(f"{skill_name} validation failed")
            if result.stdout.strip():
                print(result.stdout.strip())
            if result.stderr.strip():
                print(result.stderr.strip())
        else:
            print_ok(f"{skill_name} validation passed")
    return failures


def verify_git_diff(root: Path) -> list[str]:
    result = run_command(["git", "diff", "--check"], root)
    if result.returncode != 0:
        output = result.stdout.strip() or result.stderr.strip() or "git diff --check failed"
        print_fail(output)
        return [output]
    print_ok("git diff --check passed")
    return []


def verify_clean_worktree(root: Path) -> list[str]:
    result = run_command(["git", "status", "--short"], root)
    output = result.stdout.strip()
    if output:
        print_fail("Worktree is not clean")
        print(output)
        return [output]
    print_ok("Worktree is clean")
    return []


def verify_public_docs(root: Path) -> list[str]:
    failures: list[str] = []
    for path in iter_public_doc_files(root):
        text = path.read_text(encoding="utf-8", errors="ignore")
        hits = find_unresolved_tokens(text)
        if not hits:
            continue
        rel = path.relative_to(root).as_posix()
        failures.append(f"{rel}: {', '.join(hits)}")
        print_fail(f"Unresolved token(s) in {rel}: {', '.join(hits)}")

    if not failures:
        print_ok("Public docs scan found no unresolved placeholders")
    return failures


def verify_local(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    failures: list[str] = []

    failures.extend(verify_specs(root))
    failures.extend(verify_skills(root, Path(args.quick_validate).expanduser()))
    failures.extend(verify_git_diff(root))
    failures.extend(verify_public_docs(root))

    if args.require_clean_worktree:
        failures.extend(verify_clean_worktree(root))

    if failures:
        print_fail(f"Local verification failed with {len(failures)} issue(s)")
        return 1

    print_ok("Local verification passed")
    return 0


def gh_json(args: list[str], cwd: Path) -> dict:
    result = run_command(args, cwd)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip() or "gh command failed")
    return json.loads(result.stdout)


def verify_github(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    failures: list[str] = []

    auth = run_command(["gh", "auth", "status"], root)
    if auth.returncode != 0:
        print_fail(auth.stderr.strip() or auth.stdout.strip() or "gh auth status failed")
        return 1
    print_ok("gh auth status passed")

    repo = gh_json(["gh", "api", f"repos/{args.repo}"], root)
    print_ok(f"Loaded repo metadata for {args.repo}")

    if args.expect_public and repo.get("private") is not False:
        failures.append("Repository is not public")
        print_fail(failures[-1])
    if args.expect_issues_enabled and repo.get("has_issues") is not True:
        failures.append("Issues are not enabled")
        print_fail(failures[-1])
    if args.expect_discussions_enabled and repo.get("has_discussions") is not True:
        failures.append("Discussions are not enabled")
        print_fail(failures[-1])

    if args.expect_private_vulnerability_reporting:
        pvr = gh_json(["gh", "api", f"repos/{args.repo}/private-vulnerability-reporting"], root)
        if pvr.get("enabled") is not True:
            failures.append("Private vulnerability reporting is not enabled")
            print_fail(failures[-1])
        else:
            print_ok("Private vulnerability reporting is enabled")

    if args.release_tag:
        release = gh_json(
            [
                "gh",
                "release",
                "view",
                args.release_tag,
                "--repo",
                args.repo,
                "--json",
                "isDraft,isPrerelease,tagName,targetCommitish,url,name",
            ],
            root,
        )
        print_ok(f"Loaded release metadata for {args.release_tag}")
        if args.expect_release_published and release.get("isDraft") is True:
            failures.append(f"Release {args.release_tag} is still draft")
            print_fail(failures[-1])
        if args.expect_release_published and release.get("isPrerelease") is True:
            failures.append(f"Release {args.release_tag} is prerelease")
            print_fail(failures[-1])

    if failures:
        print_fail(f"GitHub verification failed with {len(failures)} issue(s)")
        return 1

    print_ok("GitHub verification passed")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Verify local and GitHub release readiness for this repository.")
    parser.add_argument("--root", default=str(ROOT), help="Repository root path")
    subparsers = parser.add_subparsers(dest="command", required=True)

    local_parser = subparsers.add_parser("local", help="Run local verification gates")
    local_parser.add_argument(
        "--quick-validate",
        default=str(DEFAULT_QUICK_VALIDATE),
        help="Path to skill-creator quick_validate.py",
    )
    local_parser.add_argument(
        "--require-clean-worktree",
        action="store_true",
        help="Fail if git status is not clean",
    )
    local_parser.set_defaults(handler=verify_local)

    github_parser = subparsers.add_parser("github", help="Run GitHub read-only verification gates")
    github_parser.add_argument("--repo", required=True, help="GitHub repository in owner/name form")
    github_parser.add_argument("--release-tag", help="Release tag to verify")
    github_parser.add_argument("--expect-public", action="store_true", help="Require the repository to be public")
    github_parser.add_argument(
        "--expect-issues-enabled",
        action="store_true",
        help="Require GitHub Issues to be enabled",
    )
    github_parser.add_argument(
        "--expect-discussions-enabled",
        action="store_true",
        help="Require GitHub Discussions to be enabled",
    )
    github_parser.add_argument(
        "--expect-private-vulnerability-reporting",
        action="store_true",
        help="Require private vulnerability reporting to be enabled",
    )
    github_parser.add_argument(
        "--expect-release-published",
        action="store_true",
        help="Require the specified release to be non-draft and non-prerelease",
    )
    github_parser.set_defaults(handler=verify_github)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.handler(args)


if __name__ == "__main__":
    raise SystemExit(main())
