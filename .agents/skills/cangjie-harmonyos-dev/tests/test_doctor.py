from __future__ import annotations

import json
import sys
import tempfile
import unittest
from argparse import Namespace
from pathlib import Path


TOOLS_DIR = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS_DIR))

import doctor


class DoctorTests(unittest.TestCase):
    def _project(self, root: Path) -> tuple[Path, Path, Path, Path]:
        project = root / "app"
        (project / "AppScope").mkdir(parents=True)
        (project / "AppScope/app.json5").write_text(
            '{"app":{"bundleName":"com.example.doctor"}}', encoding="utf-8"
        )
        (project / "build-profile.json5").write_text(
            '{"app":{"modules":[{"name":"entry","srcPath":"./entry"}]}}', encoding="utf-8"
        )
        main = project / "entry/src/main"
        main.mkdir(parents=True)
        (main / "module.json5").write_text(
            '{"module":{"abilities":[{"name":"EntryAbility"}]}}', encoding="utf-8"
        )
        hap = project / "entry/build/default/outputs/default/entry.hap"
        hap.parent.mkdir(parents=True)
        hap.write_bytes(b"hap")

        deveco = root / "DevEco"
        deveco.mkdir()
        (deveco / "product-info.json").write_text('{"version":"6.1.test"}', encoding="utf-8")
        sdk = root / "cangjie"
        bin_dir = sdk / "build-tools/bin"
        bin_dir.mkdir(parents=True)
        (bin_dir / doctor._exe("cjc")).write_bytes(b"")
        tools_bin = sdk / "build-tools/tools/bin"
        tools_bin.mkdir(parents=True)
        (tools_bin / doctor._exe("cjpm")).write_bytes(b"")
        hdc = root / doctor._exe("hdc")
        hdc.write_bytes(b"")
        return project, deveco, sdk, hdc

    @staticmethod
    def _args(project: Path, deveco: Path, sdk: Path, hdc: Path, **overrides: object) -> Namespace:
        values: dict[str, object] = {
            "project_root": str(project),
            "config": None,
            "deveco_home": str(deveco),
            "cangjie_sdk": str(sdk),
            "hdc": str(hdc),
            "target": None,
            "module": None,
            "bundle": None,
            "ability": None,
            "hap": None,
            "no_device_check": False,
            "json": True,
            "strict": False,
        }
        values.update(overrides)
        return Namespace(**values)

    def test_report_resolves_sources_runtime_hap_and_connected_device(self):
        with tempfile.TemporaryDirectory() as tmp:
            project, deveco, sdk, hdc = self._project(Path(tmp))

            def runner(command: list[str], timeout: float) -> tuple[int | None, str]:
                del timeout
                if command[-2:] == ["list", "targets"]:
                    return 0, "127.0.0.1:5555\n"
                if command[-1] == "-v":
                    return 0, "Ver: test"
                return 0, "Cangjie Compiler: test"

            report = doctor.collect_report(
                self._args(project, deveco, sdk, hdc), environ={}, runner=runner
            )

        self.assertTrue(report["ready"]["build"])
        self.assertTrue(report["ready"]["runtime"])
        self.assertEqual(report["runtime"]["module"]["value"], "entry")
        self.assertEqual(report["runtime"]["bundle"]["value"], "com.example.doctor")
        self.assertEqual(report["runtime"]["ability"]["value"], "EntryAbility")
        self.assertTrue(report["runtime"]["hap"]["exists"])
        self.assertEqual(report["device"]["status"], "connected")
        self.assertEqual(report["toolchain"]["deveco"]["source"], "cli:--deveco-home")
        self.assertTrue(report["inspection"]["bounded"])

    def test_hdc_failure_text_is_not_treated_as_connected_when_exit_code_is_zero(self):
        with tempfile.TemporaryDirectory() as tmp:
            hdc = Path(tmp) / doctor._exe("hdc")
            hdc.write_bytes(b"")
            report = doctor._device_report(
                hdc,
                "127.0.0.1:5555",
                "test",
                lambda command, timeout: (0, "[Fail] connect failed: no device"),
                True,
            )
        self.assertEqual(report["status"], "error")
        self.assertEqual(report["targets"], [])

    def test_hdc_nonzero_exit_is_an_error_even_if_target_text_is_present(self):
        with tempfile.TemporaryDirectory() as tmp:
            hdc = Path(tmp) / doctor._exe("hdc")
            hdc.write_bytes(b"")
            report = doctor._device_report(
                hdc,
                "127.0.0.1:5555",
                "test",
                lambda command, timeout: (7, "127.0.0.1:5555"),
                True,
            )
        self.assertEqual(report["status"], "error")

    def test_config_provenance_is_reported_without_environment_secret_value(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            project, deveco, sdk, hdc = self._project(root)
            config = root / "override.toml"
            config.write_text(
                "\n".join(
                    [
                        "[device]",
                        'target = "device-1"',
                        "[knowledge.embedding]",
                        'api_key_env = "PRIVATE_VECTOR_KEY"',
                    ]
                ),
                encoding="utf-8",
            )
            args = self._args(project, deveco, sdk, hdc, config=[str(config)], no_device_check=True)
            report = doctor.collect_report(
                args,
                environ={"PRIVATE_VECTOR_KEY": "credential-value-must-not-appear"},
                runner=lambda command, timeout: (0, "test"),
            )
            encoded = json.dumps(report, ensure_ascii=False)

        self.assertEqual(report["configuration"]["mode"], "explicit")
        self.assertEqual(report["configuration"]["final_file"], str(config.resolve()))
        self.assertEqual(report["device"]["source"], f"config:{config.resolve()}")
        self.assertNotIn("credential-value-must-not-appear", encoded)

    def test_device_check_can_be_explicitly_disabled_for_offline_ci(self):
        with tempfile.TemporaryDirectory() as tmp:
            project, deveco, sdk, hdc = self._project(Path(tmp))
            report = doctor.collect_report(
                self._args(project, deveco, sdk, hdc, no_device_check=True),
                environ={},
                runner=lambda command, timeout: (0, "test"),
            )
        self.assertEqual(report["device"]["status"], "not_checked")
        self.assertFalse(report["ready"]["runtime"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
