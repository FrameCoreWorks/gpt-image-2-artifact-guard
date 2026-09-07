#!/usr/bin/env python3
"""Build or check local instruction-only archives. No network or dependencies."""

import argparse
import hashlib
import io
import json
from pathlib import Path
import re
import stat
import zipfile


ROOT = Path(__file__).resolve().parents[1]
NAME = "gpt-image-2-artifact-guard"


def read_source(root, relative):
    path = root / relative
    for candidate in (path, *path.parents):
        if candidate == root:
            break
        if candidate.is_symlink():
            raise ValueError(f"Symlink is not a distributable source: {relative}")
    if not path.is_file():
        raise ValueError(f"Missing source file: {relative}")
    return path.read_bytes()


def archive_bytes(entries):
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_STORED) as archive:
        for name, data in sorted(entries.items()):
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = (stat.S_IFREG | 0o644) << 16
            info.compress_type = zipfile.ZIP_STORED
            archive.writestr(info, data)
    return buffer.getvalue()


def expected_artifacts(root=ROOT):
    root = root.resolve()
    manifest_path = Path(".codex-plugin/plugin.json")
    manifest_data = read_source(root, manifest_path)
    manifest = json.loads(manifest_data)
    if manifest.get("name") != NAME:
        raise ValueError("Unexpected plugin name")
    version = manifest.get("version", "")
    if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", version):
        raise ValueError("Expected a numeric major.minor.patch version")
    skill_relative = Path("skills") / NAME
    skill_root = root / skill_relative
    read_source(root, skill_relative / "SKILL.md")
    skill_entries = {}
    for path in sorted(skill_root.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"Symlink in skill: {path.relative_to(root)}")
        if not path.is_file():
            continue
        if path.name == ".DS_Store" or path.name.startswith("._"):
            continue
        if path.suffix not in {".md", ".yaml"}:
            raise ValueError(f"Unexpected runtime file: {path.relative_to(root)}")
        relative = path.relative_to(skill_root).as_posix()
        skill_entries[f"{NAME}/{relative}"] = read_source(root, path.relative_to(root))
    plugin_entries = {
        f"{NAME}/skills/{key}": value for key, value in skill_entries.items()
    }
    plugin_entries[f"{NAME}/.codex-plugin/plugin.json"] = manifest_data
    artifacts = {
        f"{NAME}-skill-{version}.zip": archive_bytes(skill_entries),
        f"{NAME}-plugin-{version}.zip": archive_bytes(plugin_entries),
    }
    checksums = "".join(
        f"{hashlib.sha256(data).hexdigest()}  {name}\n"
        for name, data in sorted(artifacts.items())
    )
    artifacts[f"SHA256SUMS-{version}.txt"] = checksums.encode("utf-8")
    return artifacts


def build_or_check(root=ROOT, check=False):
    artifacts = expected_artifacts(root)
    output = root / "dist"
    if output.is_symlink():
        raise ValueError("Refusing a symlinked dist directory")
    # Check every target first, avoiding partial writes on ordinary conflicts.
    for name, data in artifacts.items():
        target = output / name
        if target.is_symlink():
            raise ValueError(f"Refusing a symlinked output: {name}")
        if target.exists():
            if not target.is_file() or target.read_bytes() != data:
                raise ValueError(f"Existing artifact differs: {name}; bump the version")
        elif check:
            raise ValueError(f"Missing artifact: {name}")
    if not check:
        output.mkdir(exist_ok=True)
        for name, data in artifacts.items():
            target = output / name
            if not target.exists():
                with target.open("xb") as stream:
                    stream.write(data)
    return list(artifacts)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Compare existing ZIPs to sources")
    args = parser.parse_args()
    try:
        names = build_or_check(check=args.check)
    except (OSError, ValueError, zipfile.BadZipFile) as error:
        parser.exit(1, f"ERROR: {error}\n")
    verb = "Verified" if args.check else "Built or already identical"
    for name in names:
        print(f"{verb}: dist/{name}")


if __name__ == "__main__":
    main()
