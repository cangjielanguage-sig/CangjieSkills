#!/usr/bin/env python3
"""Regression tests for pure-project scaffolding and fixed package wiring."""

from __future__ import annotations

import argparse
import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path


TOOLS_DIR = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS_DIR))

import create_project as cp


def _args(**overrides) -> argparse.Namespace:
    values = {
        "app_name": "Cangjie App",
        "bundle_name": "com.example.visualexpense",
        "module_name": "main",
        "vendor": "example",
        "sdk_version": "6.1.0(23)",
        "model_version": "6.1.0",
    }
    values.update(overrides)
    return argparse.Namespace(**values)


class ReplacementsTests(unittest.TestCase):
    def test_package_name_is_pinned_to_canonical(self):
        replacements = cp.build_replacements(_args())
        self.assertEqual(replacements["__PACKAGE_NAME__"], cp.CANONICAL_PACKAGE_NAME)

    def test_bundle_and_module_names_remain_configurable(self):
        replacements = cp.build_replacements(
            _args(bundle_name="com.example.custom", module_name="main")
        )
        self.assertEqual(replacements["__BUNDLE_NAME__"], "com.example.custom")
        self.assertEqual(replacements["__MODULE_NAME__"], "main")

    def test_compile_condition_follows_module_name(self):
        replacements = cp.build_replacements(_args(module_name="main"))
        self.assertEqual(
            replacements["COMPILE_CONDITION_ENTRY"], "COMPILE_CONDITION_MAIN"
        )

class EndToEndGenerationTests(unittest.TestCase):
    def test_generation_uses_canonical_package_with_custom_bundle_and_module(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "app"
            args = [
                "--target-dir",
                str(target),
                "--app-name",
                "Visual Expense",
                "--bundle-name",
                "com.example.visualexpense",
                "--module-name",
                "main",
            ]
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                result = cp.main(args)
            self.assertEqual(result, 0, output.getvalue())

            module_json = (target / "main/src/main/module.json5").read_text(
                encoding="utf-8"
            )
            cjpm = (target / "main/cjpm.toml").read_text(encoding="utf-8")
            app_json = (target / "AppScope/app.json5").read_text(encoding="utf-8")
            root_profile = (target / "build-profile.json5").read_text(encoding="utf-8")

            self.assertIn(
                f'"{cp.CANONICAL_PACKAGE_NAME}.MyAbilityStage"', module_json
            )
            self.assertIn(
                f'"{cp.CANONICAL_PACKAGE_NAME}.MainAbility"', module_json
            )
            self.assertIn(f'name = "{cp.CANONICAL_PACKAGE_NAME}"', cjpm)
            self.assertIn("COMPILE_CONDITION_MAIN", cjpm)
            self.assertIn("com.example.visualexpense", app_json)
            self.assertIn('"name": "main"', module_json)
            self.assertIn('"srcPath": "./main"', root_profile)
            self.assertTrue((target / "main").is_dir())
            self.assertFalse((target / "entry").exists())

    def test_pure_generator_does_not_expose_package_name_override(self):
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            cp.parse_args(["app", "--package-name", "visualexpense"])

    def test_scaffold_config_sets_common_identity_fields(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            target = root / "app"
            config = root / "cangjie.skills.toml"
            config.write_text(
                '\n'.join([
                    '[scaffold]',
                    'app_name = "Configured App"',
                    'bundle_name = "com.example.configured"',
                    'module_name = "configured"',
                ]),
                encoding="utf-8",
            )
            result = cp.main(["--target-dir", str(target), "--config", str(config)])
            self.assertEqual(result, 0)
            self.assertIn("Configured App", (target / "AppScope/resources/base/element/string.json").read_text(encoding="utf-8"))
            self.assertIn("com.example.configured", (target / "AppScope/app.json5").read_text(encoding="utf-8"))
            self.assertTrue((target / "configured").is_dir())
            self.assertIn(cp.CANONICAL_PACKAGE_NAME, (target / "configured/cjpm.toml").read_text(encoding="utf-8"))

    def test_advanced_cli_overrides_remain_available(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "app"
            result = cp.main([
                "--target-dir", str(target),
                "--vendor", "Acme",
                "--sdk-version", "6.2.0(24)",
                "--model-version", "6.2.0",
            ])
            self.assertEqual(result, 0)
            self.assertIn('"vendor": "Acme"', (target / "AppScope/app.json5").read_text(encoding="utf-8"))
            self.assertIn('"targetSdkVersion": "6.2.0(24)"', (target / "build-profile.json5").read_text(encoding="utf-8"))
            self.assertIn('"modelVersion": "6.2.0"', (target / "oh-package.json5").read_text(encoding="utf-8"))

    def test_cli_identity_overrides_scaffold_defaults(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            target = root / "app"
            config = root / "cangjie.skills.toml"
            config.write_text(
                '[scaffold]\nbundle_name = "com.example.config"\nmodule_name = "configured"\n',
                encoding="utf-8",
            )
            result = cp.main([
                "--target-dir", str(target),
                "--config", str(config),
                "--bundle-name", "com.example.cli",
                "--module-name", "cli",
            ])
            self.assertEqual(result, 0)
            self.assertIn("com.example.cli", (target / "AppScope/app.json5").read_text(encoding="utf-8"))
            self.assertTrue((target / "cli").is_dir())
            self.assertFalse((target / "configured").exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
