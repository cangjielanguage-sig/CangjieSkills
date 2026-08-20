from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


TOOLS_DIR = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS_DIR))

import add_hybrid_component
import create_hybrid_project
import hybrid_project_check


class HybridProjectTests(unittest.TestCase):
    def _create(self, root: Path) -> Path:
        project = root / "hybrid"
        code = create_hybrid_project.main(
            [
                str(project),
                "--app-name", "Inventory Insights",
                "--bundle-name", "com.example.inventoryinsights",
                "--package-name", "inventory_bridge",
                "--module-name", "main",
            ]
        )
        self.assertEqual(code, 0)
        errors, _ = hybrid_project_check.validate(project, "main")
        self.assertEqual(errors, [])
        return project

    def test_customized_project_and_component_pass_contract_check(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = self._create(Path(tmp))
            code = add_hybrid_component.main(
                [
                    "--project-root", str(project),
                    "--module", "main",
                    "--component", "RiskPanel",
                    "--page", "risk",
                    "--title", "Inventory risk",
                ]
            )
            self.assertEqual(code, 0)
            errors, _ = hybrid_project_check.validate(project, "main")
            self.assertEqual(errors, [])
            pages = (project / "main/src/main/resources/base/profile/main_pages.json").read_text(encoding="utf-8")
            package = (project / "main/oh-package.json5").read_text(encoding="utf-8")
            self.assertIn('"pages/risk"', pages)
            self.assertIn('"@cangjie/cjhybridcomponent": "1.1.1"', package)

    def test_checker_reports_component_library_mismatch(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = self._create(Path(tmp))
            self.assertEqual(
                add_hybrid_component.main(
                    ["--project-root", str(project), "--module", "main", "--component", "RiskPanel"]
                ),
                0,
            )
            wrapper = project / "main/src/main/ets/pages/risk_panel.ets"
            wrapper.write_text(
                wrapper.read_text(encoding="utf-8").replace('library: "inventory_bridge"', 'library: "wrong_bridge"'),
                encoding="utf-8",
            )
            errors, _ = hybrid_project_check.validate(project, "main")
            self.assertTrue(any("library should be inventory_bridge" in item for item in errors), errors)

    def test_component_tool_upgrades_exact_legacy_component_dependency(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = self._create(Path(tmp))
            package_path = project / "main/oh-package.json5"
            package_path.write_text(
                package_path.read_text(encoding="utf-8").replace(
                    '"dependencies": {',
                    '"dependencies": {\n    "@cangjie/cjhybridcomponent": "1.0.0",',
                ),
                encoding="utf-8",
            )
            self.assertEqual(
                add_hybrid_component.main(
                    ["--project-root", str(project), "--module", "main", "--component", "RiskPanel"]
                ),
                0,
            )
            package = package_path.read_text(encoding="utf-8")
            self.assertIn('"@cangjie/cjhybridcomponent": "1.1.1"', package)
            self.assertNotIn('"@cangjie/cjhybridcomponent": "1.0.0"', package)

    def test_checker_warns_for_deprecated_global_router_and_old_component_package(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = self._create(Path(tmp))
            package_path = project / "main/oh-package.json5"
            package_path.write_text(
                package_path.read_text(encoding="utf-8").replace(
                    '"dependencies": {',
                    '"dependencies": {\n    "@cangjie/cjhybridcomponent": "1.0.0",',
                ),
                encoding="utf-8",
            )
            page = project / "main/src/main/ets/pages/Index.ets"
            page.write_text(
                "import { router } from '@kit.ArkUI';\n"
                + page.read_text(encoding="utf-8")
                + "\n// legacy example\nrouter.pushUrl({ url: 'pages/risk' });\n",
                encoding="utf-8",
            )
            errors, warnings = hybrid_project_check.validate(project, "main")
            self.assertEqual(errors, [])
            self.assertTrue(any("deprecated since API 18" in item for item in warnings), warnings)
            self.assertTrue(any("older upstream package" in item for item in warnings), warnings)

    def test_checker_accepts_uicontext_router_without_deprecation_warning(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = self._create(Path(tmp))
            page = project / "main/src/main/ets/pages/Index.ets"
            page.write_text(
                page.read_text(encoding="utf-8")
                + "\n// current page-bound API\nthis.getUIContext().getRouter().pushUrl({ url: 'pages/risk' });\n",
                encoding="utf-8",
            )
            errors, warnings = hybrid_project_check.validate(project, "main")
            self.assertEqual(errors, [])
            self.assertFalse(any("deprecated since API 18" in item for item in warnings), warnings)

    def test_checker_does_not_warn_for_page_bound_router_alias(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = self._create(Path(tmp))
            page = project / "main/src/main/ets/pages/Index.ets"
            page.write_text(
                page.read_text(encoding="utf-8")
                + "\n// current page-bound alias\n"
                + "const router = this.getUIContext().getRouter();\n"
                + "router.pushUrl({ url: 'pages/risk' });\n",
                encoding="utf-8",
            )
            errors, warnings = hybrid_project_check.validate(project, "main")
            self.assertEqual(errors, [])
            self.assertFalse(any("deprecated since API 18" in item for item in warnings), warnings)

    def test_scaffold_config_sets_only_common_hybrid_identity(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            project = root / "hybrid"
            config = root / "cangjie.skills.toml"
            config.write_text(
                '\n'.join([
                    '[scaffold]',
                    'app_name = "Configured Hybrid"',
                    'bundle_name = "com.example.configuredhybrid"',
                    'module_name = "shell"',
                ]),
                encoding="utf-8",
            )
            code = create_hybrid_project.main([
                str(project),
                "--config", str(config),
            ])
            self.assertEqual(code, 0)
            errors, _ = hybrid_project_check.validate(project, "shell")
            self.assertEqual(errors, [])
            self.assertIn("Configured Hybrid", (project / "AppScope/resources/base/element/string.json").read_text(encoding="utf-8"))
            self.assertIn("com.example.configuredhybrid", (project / "AppScope/app.json5").read_text(encoding="utf-8"))
            self.assertTrue((project / "shell").is_dir())
            self.assertTrue((project / "shell/src/main/cangjie/types/libohos_app_cangjie_entry").is_dir())

    def test_hybrid_advanced_cli_overrides_remain_available(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "hybrid"
            code = create_hybrid_project.main([
                str(project),
                "--package-name", "custom_bridge",
                "--sdk-version", "6.2.0(24)",
                "--model-version", "6.2.0",
            ])
            self.assertEqual(code, 0)
            self.assertTrue((project / "entry/src/main/cangjie/types/libcustom_bridge").is_dir())
            self.assertIn('"targetSdkVersion": "6.2.0(24)"', (project / "build-profile.json5").read_text(encoding="utf-8"))
            self.assertIn('"modelVersion": "6.2.0"', (project / "oh-package.json5").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
