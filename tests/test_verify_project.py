import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "verify_project.py"


def load_module():
    spec = importlib.util.spec_from_file_location("verify_project", SCRIPT_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load module from {SCRIPT_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class VerifyProjectTests(unittest.TestCase):
    def test_script_exists(self):
        self.assertTrue(SCRIPT_PATH.exists(), f"Missing script: {SCRIPT_PATH}")

    def test_strip_markdown_code_removes_inline_and_fenced_code(self):
        module = load_module()
        text = (
            "Visible {{PROJECT_NAME}} token\\n"
            "Inline `{{INLINE_TOKEN}}` should be ignored\\n"
            "```md\\n{{BLOCK_TOKEN}}\\nTBD\\n```\\n"
            "Visible TBD marker\\n"
        )

        cleaned = module.strip_markdown_code(text)

        self.assertIn("{{PROJECT_NAME}}", cleaned)
        self.assertIn("Visible TBD marker", cleaned)
        self.assertNotIn("{{INLINE_TOKEN}}", cleaned)
        self.assertNotIn("{{BLOCK_TOKEN}}", cleaned)
        self.assertNotIn("```", cleaned)

    def test_find_unresolved_tokens_only_reports_prose_hits(self):
        module = load_module()
        text = (
            "Keep {{PROJECT_NAME}} in prose\\n"
            "Example `{{INLINE_TOKEN}}` should not count\\n"
            "```yaml\\nkey: {{BLOCK_TOKEN}}\\n```\\n"
            "Still TBD here\\n"
        )

        hits = module.find_unresolved_tokens(text)

        self.assertEqual(hits, ["{{PROJECT_NAME}}", "TBD"])

    def test_iter_public_doc_targets_returns_only_configured_existing_paths(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "specs").mkdir()
            (root / "docs" / "releases").mkdir(parents=True)
            (root / "specs" / "产品概述.md").write_text("# 产品概述\\n")
            (root / "README.md").write_text("# README\\n")
            (root / "docs" / "releases" / "v0.1.2.md").write_text("# Release\\n")
            (root / "notes.txt").write_text("ignore me\\n")

            files = [path.relative_to(root).as_posix() for path in module.iter_public_doc_targets(root)]

        self.assertEqual(
            files,
            [
                "README.md",
                "docs/releases",
                "specs",
            ],
        )


if __name__ == "__main__":
    unittest.main()
