from __future__ import annotations

import os
import re
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


TOOLS_DIR = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS_DIR))

import config_loader as config


class ConfigLoadingTests(unittest.TestCase):
    def test_built_in_defaults_are_safe_and_complete(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(config, "USER_CONFIG", Path(tmp) / "missing"):
            loaded = config.load_harmony_config(project_root=tmp)
        self.assertEqual(loaded.loaded_files, [])
        self.assertEqual(loaded.toolchain.ohpm_registry, config.DEFAULT_OHPM_REGISTRY)
        self.assertTrue(loaded.toolchain.verify_tls)
        self.assertEqual(loaded.device.target, "127.0.0.1:5555")
        self.assertEqual(loaded.knowledge.embedding.mode, "search")
        self.assertEqual(loaded.knowledge.embedding.model, "text-embedding-v4")
        self.assertEqual(loaded.knowledge.embedding.dimensions, 256)
        self.assertIsNone(loaded.scaffold.bundle_name)

    def test_later_explicit_config_overrides_earlier(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            first = root / "first.toml"
            second = root / "second.toml"
            first.write_text('[device]\ntarget = "one"\n', encoding="utf-8")
            second.write_text('[device]\ntarget = "two"\n', encoding="utf-8")
            loaded = config.load_harmony_config(config_paths=[first, second])
            self.assertEqual(loaded.device.target, "two")
            self.assertEqual(loaded.loaded_files, [first.resolve(), second.resolve()])

    def test_missing_explicit_config_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            missing = Path(tmp) / "missing.toml"
            with self.assertRaisesRegex(FileNotFoundError, re.escape(str(missing))):
                config.load_harmony_config(config_paths=[missing])

    def test_missing_environment_config_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(
            config, "USER_CONFIG", Path(tmp) / "user" / config.CONFIG_FILENAME
        ):
            missing = Path(tmp) / "missing.toml"
            with patch.dict(os.environ, {config.CONFIG_ENV: str(missing)}, clear=False), self.assertRaisesRegex(
                FileNotFoundError, re.escape(str(missing))
            ):
                config.load_harmony_config(project_root=tmp)

    def test_partial_nested_override_preserves_other_defaults(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / config.CONFIG_FILENAME
            path.write_text(
                '[knowledge.embedding]\nmode = "search"\nbatch_size = 24\n',
                encoding="utf-8",
            )
            loaded = config.load_harmony_config(config_paths=[path])
        self.assertEqual(loaded.knowledge.embedding.mode, "search")
        self.assertEqual(loaded.knowledge.embedding.batch_size, 24)
        self.assertEqual(loaded.knowledge.embedding.model, "text-embedding-v4")

    def test_all_sections_load_together(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / config.CONFIG_FILENAME
            path.write_text(
                '\n'.join([
                    '[toolchain]',
                    'deveco_home = "D:/DevEco"',
                    'cangjie_sdk = "D:/Cangjie"',
                    'hdc = "D:/hdc.exe"',
                    'ohpm_registry = "https://registry.example/ohpm/"',
                    'verify_tls = false',
                    '[device]',
                    'target = "emulator-5554"',
                    '[runtime]',
                    'bundle = "com.example.app"',
                    'ability = "EntryAbility"',
                    'module = "main"',
                    'hap = "main/build/app.hap"',
                    '[scaffold]',
                    'app_name = "Example"',
                    'bundle_name = "com.example.app"',
                    'module_name = "main"',
                    '[knowledge]',
                    'version = "6.1"',
                    '[knowledge.embedding]',
                    'mode = "all"',
                    'dimensions = 1024',
                    'min_similarity = 0.42',
                    'batch_size = 20',
                ]),
                encoding="utf-8",
            )
            loaded = config.load_harmony_config(config_paths=[path])
        self.assertFalse(loaded.toolchain.verify_tls)
        self.assertEqual(loaded.runtime.module, "main")
        self.assertEqual(loaded.scaffold.app_name, "Example")
        self.assertEqual(loaded.knowledge.embedding.mode, "all")
        self.assertEqual(loaded.knowledge.embedding.dimensions, 1024)
        self.assertEqual(loaded.knowledge.embedding.min_similarity, 0.42)

    def test_embedding_min_similarity_must_be_a_probability(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.toml"
            for value in (-0.1, 1.1):
                path.write_text(
                    f"[knowledge.embedding]\nmin_similarity = {value}\n",
                    encoding="utf-8",
                )
                with self.subTest(value=value), self.assertRaisesRegex(ValueError, "between 0 and 1"):
                    config.load_harmony_config(config_paths=[path])

    def test_plaintext_api_key_is_rejected_at_any_depth(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.toml"
            path.write_text('[knowledge.embedding]\napi_key = "not-allowed"\n', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "knowledge.embedding.api_key"):
                config.load_harmony_config(config_paths=[path])

    def test_unknown_key_is_rejected_with_full_name(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.toml"
            path.write_text('[device]\nemulator = "5555"\n', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "device.emulator"):
                config.load_harmony_config(config_paths=[path])

    def test_unknown_section_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.toml"
            path.write_text('[unknown]\nruntime = true\n', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "unknown"):
                config.load_harmony_config(config_paths=[path])

    def test_legacy_project_section_has_actionable_migration_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.toml"
            path.write_text('[project]\nbundle_name = "com.example.app"\n', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, r"use \[scaffold\].*generator CLI"):
                config.load_harmony_config(config_paths=[path])

    def test_scaffold_rejects_generator_specific_advanced_fields(self):
        with tempfile.TemporaryDirectory() as tmp:
            for field, value in (
                ("package_name", "custom_bridge"),
                ("vendor", "Acme"),
                ("sdk_version", "6.1.0(23)"),
                ("model_version", "6.1.0"),
            ):
                path = Path(tmp) / f"bad-{field}.toml"
                path.write_text(f'[scaffold]\n{field} = "{value}"\n', encoding="utf-8")
                with self.subTest(field=field), self.assertRaisesRegex(ValueError, rf"scaffold\.{field}"):
                    config.load_harmony_config(config_paths=[path])

    def test_invalid_type_range_url_and_embedding_mode_are_rejected(self):
        cases = (
            ('[toolchain]\nverify_tls = "yes"\n', "toolchain.verify_tls"),
            ('[toolchain]\nohpm_registry = "not-a-url"\n', "toolchain.ohpm_registry"),
            ('[knowledge.embedding]\nmode = "runtime"\n', "knowledge.embedding.mode"),
            ('[knowledge.embedding]\nbatch_size = 0\n', "knowledge.embedding.batch_size"),
            ('[knowledge.embedding]\nmax_retries = -1\n', "knowledge.embedding.max_retries"),
            ('[knowledge.embedding]\ntimeout_seconds = true\n', "knowledge.embedding.timeout_seconds"),
            ('[knowledge.embedding]\napi_format = "unknown"\n', "knowledge.embedding.api_format"),
            ('[knowledge.embedding]\ndimensions = 256.5\n', "knowledge.embedding.dimensions"),
            ('[knowledge.embedding]\nbatch_size = 1.5\n', "knowledge.embedding.batch_size"),
        )
        with tempfile.TemporaryDirectory() as tmp:
            for index, (content, message) in enumerate(cases):
                path = Path(tmp) / f"bad-{index}.toml"
                path.write_text(content, encoding="utf-8")
                with self.subTest(message=message), self.assertRaisesRegex(ValueError, message.replace(".", r"\.")):
                    config.load_harmony_config(config_paths=[path])

    def test_blank_auto_detect_value_is_rejected_with_omit_hint(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.toml"
            path.write_text('[runtime]\nbundle = ""\n', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "omit it to use automatic detection"):
                config.load_harmony_config(config_paths=[path])

    def test_environment_config_path_is_last(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            env_config = root / "env.toml"
            env_config.write_text('[device]\ntarget = "env"\n', encoding="utf-8")
            with patch.object(config, "USER_CONFIG", root / "missing.toml"), patch.dict(
                os.environ, {config.CONFIG_ENV: str(env_config)}, clear=False
            ):
                paths = config.default_config_paths(root)
            self.assertEqual(paths[-1], env_config)

    def test_discovered_user_project_and_environment_layers_merge_in_order(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            user = root / "user" / config.CONFIG_FILENAME
            project = root / config.CONFIG_FILENAME
            override = root / "override.toml"
            user.parent.mkdir()
            user.write_text('[toolchain]\nhdc = "D:/user/hdc.exe"\n[device]\ntarget = "user"\n', encoding="utf-8")
            project.write_text('[toolchain]\nverify_tls = false\n[device]\ntarget = "project"\n', encoding="utf-8")
            override.write_text('[device]\ntarget = "environment"\n', encoding="utf-8")
            with patch.object(config, "USER_CONFIG", user), patch.dict(
                os.environ, {config.CONFIG_ENV: str(override)}, clear=False
            ):
                loaded = config.load_harmony_config(project_root=root)
        self.assertEqual(loaded.toolchain.hdc, "D:/user/hdc.exe")
        self.assertFalse(loaded.toolchain.verify_tls)
        self.assertEqual(loaded.device.target, "environment")
        self.assertEqual(loaded.loaded_files, [user.resolve(), project.resolve(), override.resolve()])

    def test_canonical_file_locations_are_simple(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(config, "USER_CONFIG", Path(tmp) / "user" / config.CONFIG_FILENAME):
            paths = config.default_config_paths(tmp)
        self.assertEqual(paths[0].name, "cangjie.skills.toml")
        self.assertEqual(paths[1], Path(tmp).resolve() / "cangjie.skills.toml")
        self.assertEqual(config.CONFIG_ENV, "CANGJIE_SKILLS_CONFIG")

    def test_canonical_example_loads_and_documentation_covers_every_key(self):
        repository_root = Path(__file__).resolve().parents[4]
        example = repository_root / "config" / config.CONFIG_FILENAME
        documentation = repository_root / "config" / "README.md"
        loaded = config.load_harmony_config(config_paths=[example])
        self.assertEqual(loaded.loaded_files, [example.resolve()])
        text = documentation.read_text(encoding="utf-8")
        for key in config.supported_config_keys():
            with self.subTest(key=key):
                self.assertIn(f"`{key}`", text)
        self.assertEqual(len(config.supported_config_keys()), 24)


class RuntimeDetectionTests(unittest.TestCase):
    def _project(self, root: Path, module: str = "main") -> Path:
        project = root / "app"
        (project / "AppScope").mkdir(parents=True)
        (project / "AppScope/app.json5").write_text(
            '{"app":{"bundleName":"com.example.clean"}}', encoding="utf-8"
        )
        (project / "build-profile.json5").write_text(
            '{"app":{"modules":[{"name":"%s","srcPath":"./%s"}]}}'
            % (module, module),
            encoding="utf-8",
        )
        module_root = project / module / "src/main"
        module_root.mkdir(parents=True)
        (module_root / "module.json5").write_text(
            '{"module":{"abilities":[{"name":"EntryAbility"}]}}',
            encoding="utf-8",
        )
        return project

    def test_detects_custom_module_bundle_and_ability(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = self._project(Path(tmp))
            detected = config.detect_project_runtime(project)
            self.assertEqual(detected.bundle, "com.example.clean")
            self.assertEqual(detected.module, "main")
            self.assertEqual(detected.ability, "EntryAbility")

    def test_newest_hap_is_selected_with_warning(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = self._project(Path(tmp))
            outputs = project / "main/build/default/outputs/default"
            outputs.mkdir(parents=True)
            old = outputs / "old.hap"
            new = outputs / "new.hap"
            old.write_bytes(b"old")
            new.write_bytes(b"new")
            os.utime(old, (1, 1))
            os.utime(new, (2, 2))
            hap, warnings = config.detect_hap(project, "main")
            self.assertEqual(hap, "main/build/default/outputs/default/new.hap")
            self.assertEqual(len(warnings), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
