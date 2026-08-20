#!/usr/bin/env python3
"""Regression tests for HarmonyOS-only stdx installation and configuration."""

from __future__ import annotations

import contextlib
import io
import json
import sys
import tempfile
import tomllib
import unittest
import zipfile
from pathlib import Path
from unittest import mock


TOOLS_DIR = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS_DIR))

from harmonyos_stdx import cli, manifest, policy
from harmonyos_stdx.errors import SetupError
from harmonyos_stdx.models import Toolchain


VERSION = "1.1.0.1"


def make_archive(directory: Path, platform: str, *, version: str = VERSION) -> Path:
    archive = directory / f"cangjie-stdx-{platform}-{version}.zip"
    payload = f"cangjie-stdx-{platform}_cjnative/dynamic/stdx"
    with zipfile.ZipFile(archive, "w") as bundle:
        bundle.writestr(f"{payload}/stdx.cjo", b"cjo")
        bundle.writestr(f"{payload}/libstdx.so", b"so")
    return archive


def make_project(root: Path) -> tuple[Path, Path]:
    project = root / "entry"
    project.mkdir()
    manifest_path = project / "cjpm.toml"
    manifest_path.write_text(
        '\n'.join([
            '[package]',
            'name = "example"',
            'version = "1.0.0"',
            '',
            '[target.x86_64-linux-ohos.bin-dependencies]',
            'path-option = ["C:/vendor/lib"]',
            '',
        ]),
        encoding="utf-8",
    )
    return project, manifest_path


def toolchain() -> Toolchain:
    return Toolchain("1.1.0", policy.release_for_cjc("1.1.0"))


class PolicyTests(unittest.TestCase):
    def test_policy_contains_only_harmonyos_targets(self):
        self.assertEqual(policy.OHOS_PLATFORMS, ("ohos-x64", "ohos-aarch64"))
        self.assertEqual(
            policy.PLATFORM_TO_TARGET,
            {"ohos-x64": "x86_64-linux-ohos", "ohos-aarch64": "aarch64-linux-ohos"},
        )
        source = Path(policy.__file__).read_text(encoding="utf-8")
        for unrelated in ("android", "ios", "windows-x64", "linux-x64", "mac-x64"):
            self.assertNotIn(unrelated, source)

    def test_release_mapping_and_asset_urls(self):
        release = policy.release_for_cjc("1.1.0")
        self.assertEqual(release.version, VERSION)
        self.assertEqual(policy.release_for_cjc("1.1.0-beta.22"), release)
        self.assertEqual(
            policy.asset_url(release, "ohos-x64"),
            "https://gitcode.com/Cangjie/cangjie_stdx/releases/download/v1.1.0.1/"
            "cangjie-stdx-ohos-x64-1.1.0.1.zip",
        )
        self.assertEqual(
            policy.asset_url(release, "ohos-aarch64"),
            "https://gitcode.com/Cangjie/cangjie_stdx/releases/download/v1.1.0.1/"
            "cangjie-stdx-ohos-aarch64-1.1.0.1.zip",
        )
        self.assertEqual(policy.parse_cjc_output("Cangjie Compiler: 1.1.0\nTarget: host").release, release)
        with self.assertRaisesRegex(SetupError, "no HarmonyOS stdx compatibility policy"):
            policy.release_for_cjc("1.0.5")

    def test_cli_rejects_non_harmonyos_platforms(self):
        for platform in ("windows-x64", "linux-x64", "mac-aarch64", "android-aarch64"):
            with (
                self.subTest(platform=platform),
                contextlib.redirect_stderr(io.StringIO()),
                self.assertRaises(SystemExit),
            ):
                cli.parse_args(["--platform", platform])


class ManifestTests(unittest.TestCase):
    def test_dual_target_merge_is_idempotent_and_preserves_unrelated_paths(self):
        original = (
            '[package]\nname = "example"\n\n'
            '[target.x86_64-linux-ohos.bin-dependencies]\n'
            'path-option = ["C:/vendor/lib"]\n'
        )
        roots = {
            "x86_64-linux-ohos": Path("C:/stdx/x64/dynamic/stdx"),
            "aarch64-linux-ohos": Path("C:/stdx/arm64/dynamic/stdx"),
        }
        updated, changed = manifest.merge_manifest_text(original, roots)
        repeated, changed_again = manifest.merge_manifest_text(updated, roots)
        parsed = tomllib.loads(updated)
        self.assertTrue(changed)
        self.assertFalse(changed_again)
        self.assertEqual(repeated, updated)
        self.assertIn("C:/vendor/lib", parsed["target"]["x86_64-linux-ohos"]["bin-dependencies"]["path-option"])
        self.assertEqual(len(parsed["target"]["aarch64-linux-ohos"]["bin-dependencies"]["path-option"]), 1)

    def test_atomic_replace_failure_preserves_manifest(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "cjpm.toml"
            original = '[package]\nname = "example"\n'
            path.write_text(original, encoding="utf-8")
            roots = {"x86_64-linux-ohos": Path(tmp) / "stdx" / "dynamic" / "stdx"}
            with (
                mock.patch.object(manifest.os, "replace", side_effect=OSError("simulated")),
                self.assertRaises(OSError),
            ):
                manifest.configure_manifest(path, roots)
            self.assertEqual(path.read_text(encoding="utf-8"), original)

    def test_non_harmonyos_target_is_rejected(self):
        with self.assertRaisesRegex(SetupError, "non-HarmonyOS"):
            manifest.merge_manifest_text('[package]\nname = "example"\n', {"x86_64-w64-mingw32": Path("C:/stdx")})

    def test_malformed_target_shape_has_an_actionable_error(self):
        with self.assertRaisesRegex(SetupError, "target must be a TOML table"):
            manifest.merge_manifest_text('target = "invalid"\n', {"x86_64-linux-ohos": Path("C:/stdx")})


class SetupWorkflowTests(unittest.TestCase):
    def test_offline_dual_abi_install_and_repeat_are_idempotent(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            project, manifest_path = make_project(root)
            archives = root / "archives"
            archives.mkdir()
            for platform in policy.OHOS_PLATFORMS:
                make_archive(archives, platform)
            destination = root / "installed"
            args = cli.parse_args([
                "--project", str(project),
                "--archive-dir", str(archives),
                "--offline",
                "--destination", str(destination),
            ])
            first = cli.run(args, toolchain())
            second = cli.run(args, toolchain())
            parsed = tomllib.loads(manifest_path.read_text(encoding="utf-8"))

            self.assertTrue(first["configured"])
            self.assertFalse(second["configured"])
            self.assertEqual([item["platform"] for item in first["platforms"]], list(policy.OHOS_PLATFORMS))
            self.assertTrue(all(item["installation_reused"] for item in second["platforms"]))
            for platform, target in policy.PLATFORM_TO_TARGET.items():
                paths = parsed["target"][target]["bin-dependencies"]["path-option"]
                self.assertTrue(any(f"cangjie-stdx-{platform}-{VERSION}" in path for path in paths))
            self.assertIn(
                "C:/vendor/lib",
                parsed["target"]["x86_64-linux-ohos"]["bin-dependencies"]["path-option"],
            )

    def test_missing_second_archive_does_not_install_or_edit(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            project, manifest_path = make_project(root)
            original = manifest_path.read_bytes()
            archives = root / "archives"
            archives.mkdir()
            make_archive(archives, "ohos-x64")
            destination = root / "installed"
            args = cli.parse_args([
                "--project", str(project),
                "--archive-dir", str(archives),
                "--offline",
                "--destination", str(destination),
            ])
            with self.assertRaisesRegex(SetupError, "not a valid ZIP archive"):
                cli.run(args, toolchain())
            self.assertEqual(manifest_path.read_bytes(), original)
            self.assertFalse(destination.exists())

    def test_dry_run_defaults_to_both_harmonyos_platforms_without_writes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            project, manifest_path = make_project(root)
            original = manifest_path.read_bytes()
            destination = root / "installed"
            args = cli.parse_args(["--project", str(project), "--destination", str(destination), "--dry-run"])
            result = cli.run(args, toolchain())
            self.assertTrue(result["dry_run"])
            self.assertEqual([item["platform"] for item in result["platforms"]], list(policy.OHOS_PLATFORMS))
            self.assertEqual(manifest_path.read_bytes(), original)
            self.assertFalse(destination.exists())

    def test_configured_sdk_is_resolved(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            project, _manifest_path = make_project(root)
            sdk = root / "sdk"
            compiler = sdk / "build-tools" / "bin" / ("cjc.exe" if sys.platform == "win32" else "cjc")
            compiler.parent.mkdir(parents=True)
            compiler.write_bytes(b"compiler")
            config = root / "cangjie.skills.toml"
            config.write_text(f'[toolchain]\ncangjie_sdk = {json.dumps(str(sdk))}\n', encoding="utf-8")
            args = cli.parse_args(["--project", str(project), "--config", str(config), "--dry-run"])
            self.assertEqual(cli._resolve_sdk(args), sdk.resolve())

    def test_invalid_shared_config_has_no_traceback(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            project, _manifest_path = make_project(root)
            config = root / "invalid.toml"
            config.write_text('[toolchain]\nunknown = "value"\n', encoding="utf-8")
            stderr = io.StringIO()
            with contextlib.redirect_stderr(stderr):
                status = cli.main(["--project", str(project), "--config", str(config), "--dry-run"])
            self.assertEqual(status, 1)
            self.assertIn("toolchain.unknown", stderr.getvalue())
            self.assertNotIn("Traceback", stderr.getvalue())


if __name__ == "__main__":
    unittest.main(verbosity=2)
