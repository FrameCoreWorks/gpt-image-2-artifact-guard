"""Structural/package checks, not proof of model behavior or visual efficacy."""

import hashlib
import importlib.util
import io
import json
from pathlib import Path, PurePosixPath
import re
import shutil
import struct
import tempfile
import unittest
from urllib.parse import unquote
import zipfile


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("package", ROOT / "scripts/package.py")
PACKAGE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PACKAGE)
SKILL = ROOT / "skills" / PACKAGE.NAME


class SourceTests(unittest.TestCase):
    def test_metadata_and_required_resources(self):
        manifest = json.loads((ROOT / ".codex-plugin/plugin.json").read_text())
        self.assertEqual(manifest["skills"], "./skills/")
        self.assertFalse({"mcpServers", "apps", "hooks"} & manifest.keys())
        skill = (SKILL / "SKILL.md").read_text()
        self.assertTrue(skill.startswith(f"---\nname: {PACKAGE.NAME}\n"))
        self.assertLess(len(skill.splitlines()), 500)
        self.assertIn(f"Version {manifest['version']}. ", skill)
        for resource in ("risk-taxonomy", "prompt-patterns", "qa-and-recovery",
                         "evidence-register", "workflow-integration", "onboarding",
                         "pattern-morphology", "human-photorealism"):
            self.assertTrue((SKILL / "references" / f"{resource}.md").is_file())
        self.assertIn(f"${PACKAGE.NAME}", (SKILL / "agents/openai.yaml").read_text())

    def test_local_markdown_links_resolve(self):
        for path in ROOT.rglob("*.md"):
            for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
                if "://" in target or target.startswith("#"):
                    continue
                target = unquote(target.split("#", 1)[0])
                resolved = (path.parent / target).resolve()
                self.assertTrue(resolved.is_relative_to(ROOT), (path.name, target))
                self.assertTrue(resolved.exists(), (path.name, target))

    def test_portable_instruction_sources(self):
        for path in SKILL.rglob("*"):
            if path.is_file():
                text = path.read_text()
                self.assertNotIn("/Volumes/", text, path.name)
                self.assertNotIn("/Users/", text, path.name)
                self.assertNotIn("[TODO", text, path.name)
        self.assertFalse((ROOT / ".mcp.json").exists())
        self.assertFalse((ROOT / ".app.json").exists())

    def test_behavioral_fixture_ids(self):
        cases = json.loads((ROOT / "tests/cases.json").read_text())
        ids = [case["id"] for case in cases]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertGreaterEqual(len(ids), 12)
        for case in cases:
            self.assertTrue(case["request"])
            self.assertTrue(case["rubric"])
            self.assertIn(case["trigger"], {"yes", "no"})

    def test_selected_readme_banner(self):
        relative = "assets/readme-banner-v6-microtexture.png"
        self.assertIn(f"]({relative})", (ROOT / "README.md").read_text())
        data = (ROOT / relative).read_bytes()
        self.assertEqual(data[:8], b"\x89PNG\r\n\x1a\n")
        self.assertEqual(data[12:16], b"IHDR")
        self.assertEqual(struct.unpack(">II", data[16:24]), (1983, 793))


class PackageTests(unittest.TestCase):
    def test_deterministic_archives_and_checksums(self):
        first = PACKAGE.expected_artifacts()
        self.assertEqual(first, PACKAGE.expected_artifacts())
        sums = next(value for key, value in first.items() if key.startswith("SHA256SUMS-"))
        self.assertEqual(len(sums.decode().splitlines()), 4)
        for line in sums.decode().splitlines():
            digest, name = line.split("  ")
            self.assertEqual(hashlib.sha256(first[name]).hexdigest(), digest)

    def test_archives_are_safe_and_share_identical_skill(self):
        artifacts = PACKAGE.expected_artifacts()
        archives = {}
        for name, payload in artifacts.items():
            if not name.endswith(".zip"):
                continue
            with zipfile.ZipFile(io.BytesIO(payload)) as archive:
                self.assertIsNone(archive.testzip())
                members = archive.namelist()
                self.assertEqual(len(members), len(set(members)))
                for member in members:
                    path = PurePosixPath(member)
                    self.assertFalse(path.is_absolute())
                    self.assertNotIn("..", path.parts)
                    self.assertEqual(path.parts[0], PACKAGE.NAME)
                    self.assertNotIn("scripts", path.parts)
                    self.assertNotIn("tests", path.parts)
                    self.assertNotIn(".DS_Store", path.parts)
                    self.assertFalse(path.name.startswith("._"))
                archives["skill" if "-skill-" in name else "plugin"] = {
                    member: archive.read(member) for member in members
                }
        for name, data in archives["skill"].items():
            self.assertEqual(archives["plugin"][f"{PACKAGE.NAME}/skills/{name}"], data)
        self.assertEqual(len(archives["plugin"]), len(archives["skill"]) + 1)

    def fixture(self, directory):
        root = Path(directory)
        shutil.copytree(ROOT / "skills", root / "skills")
        shutil.copytree(ROOT / ".codex-plugin", root / ".codex-plugin")
        shutil.copytree(ROOT / "prompts", root / "prompts")
        return root

    def test_setup_prompts_are_exact_release_copies(self):
        artifacts = PACKAGE.expected_artifacts()
        version = json.loads((ROOT / ".codex-plugin/plugin.json").read_text())["version"]
        for surface, source in (("CHATGPT-WORK", "install-chatgpt-work.txt"),
                                ("CODEX", "install-codex.txt")):
            self.assertEqual(artifacts[f"INSTALL-{surface}-{version}.txt"],
                             (ROOT / "prompts" / source).read_bytes())

    def test_standalone_roundtrip_to_isolated_project(self):
        artifacts = PACKAGE.expected_artifacts()
        payload = next(value for key, value in artifacts.items() if "-skill-" in key)
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / ".agents" / "skills"
            with zipfile.ZipFile(io.BytesIO(payload)) as archive:
                archive.extractall(destination)
            installed = destination / PACKAGE.NAME
            expected = {p.relative_to(SKILL).as_posix(): p.read_bytes()
                        for p in SKILL.rglob("*") if p.suffix in {".md", ".yaml"}}
            actual = {p.relative_to(installed).as_posix(): p.read_bytes()
                      for p in installed.rglob("*") if p.is_file()}
            self.assertEqual(actual, expected)

    def test_rejects_inconsistent_skill_version(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self.fixture(directory)
            path = root / ".codex-plugin/plugin.json"
            manifest = json.loads(path.read_text())
            manifest["version"] = "9.9.9"
            path.write_text(json.dumps(manifest))
            with self.assertRaisesRegex(ValueError, "Skill version"):
                PACKAGE.expected_artifacts(root)

    def test_rejects_stale_setup_prompt(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self.fixture(directory)
            path = root / "prompts/install-codex.txt"
            version = json.loads((root / ".codex-plugin/plugin.json").read_text())["version"]
            path.write_text(path.read_text().replace(version, "0.0.0"))
            with self.assertRaisesRegex(ValueError, "Setup prompt version"):
                PACKAGE.expected_artifacts(root)

    def test_build_check_and_no_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self.fixture(directory)
            with self.assertRaisesRegex(ValueError, "Missing artifact"):
                PACKAGE.build_or_check(root, check=True)
            PACKAGE.build_or_check(root)
            PACKAGE.build_or_check(root, check=True)
            PACKAGE.build_or_check(root)
            archive = next((root / "dist").glob("*.zip"))
            archive.write_bytes(b"existing user file")
            with self.assertRaisesRegex(ValueError, "Existing artifact differs"):
                PACKAGE.build_or_check(root)
            self.assertEqual(archive.read_bytes(), b"existing user file")

    def test_rejects_symlinked_source(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self.fixture(directory)
            (root / "skills" / PACKAGE.NAME / "linked.md").symlink_to(ROOT / "README.md")
            with self.assertRaisesRegex(ValueError, "Symlink"):
                PACKAGE.expected_artifacts(root)

    def test_rejects_unexpected_runtime_file(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self.fixture(directory)
            (root / "skills" / PACKAGE.NAME / "unexpected.py").write_text("print('test')")
            with self.assertRaisesRegex(ValueError, "Unexpected runtime file"):
                PACKAGE.expected_artifacts(root)

    def test_rejects_symlinked_output(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self.fixture(directory)
            (root / "other").mkdir()
            (root / "dist").symlink_to(root / "other", target_is_directory=True)
            with self.assertRaisesRegex(ValueError, "symlinked dist"):
                PACKAGE.build_or_check(root)


if __name__ == "__main__":
    unittest.main()
