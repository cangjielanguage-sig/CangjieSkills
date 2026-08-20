from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


TOOLS_DIR = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS_DIR))

import build_analyzer
import build_recovery
import hdc_utils
import hilog_capture
import ui_capture


class BuildRecoveryTests(unittest.TestCase):
    def test_cache_paths_follow_custom_module(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp)
            (project / "main").mkdir()
            (project / "main/cjpm.toml").touch()
            paths = build_recovery.cache_paths(project)
            self.assertIn(project / "main/build/default/intermediates/cj", paths)
            self.assertNotIn(project / "entry/build/default/intermediates/cj", paths)

    def test_remove_inside_project_refuses_outside_target(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "project"
            project.mkdir()
            with self.assertRaisesRegex(RuntimeError, "outside project"):
                build_recovery.remove_inside_project(project.resolve(), project.parent / "outside")

    def test_known_cache_markers(self):
        self.assertTrue(build_recovery.has_known_cache_failure("DepModel::loadDepIncrementalCache"))
        self.assertFalse(build_recovery.has_known_cache_failure("unrelated compiler error"))


class BuildAnalyzerTests(unittest.TestCase):
    def test_later_failure_prevents_success_finding(self):
        with tempfile.TemporaryDirectory() as tmp:
            log = Path(tmp) / "build.log"
            log.write_text("BUILD SUCCESSFUL\n> Hvigor ERROR: BUILD FAILED\n", encoding="utf-8")
            codes = {item["code"] for item in build_analyzer.analyze(log)["findings"]}
            self.assertNotIn("build_successful", codes)

    def test_arkts_builder_statement_is_actionable(self):
        findings = build_analyzer.detect_findings("Only UI component syntax can be written here")
        self.assertEqual([item.code for item in findings], ["arkts_builder_non_ui_statement"])


class UiAssertionTests(unittest.TestCase):
    @staticmethod
    def _tree(text: str) -> dict:
        return {
            "attributes": {"type": "root"},
            "children": [
                {
                    "attributes": {
                        "type": "Text",
                        "key": "status",
                        "text": text,
                        "bounds": "[0,0][100,40]",
                    }
                }
            ],
        }

    def test_semantic_assertions_on_before_and_after_layouts(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            before = root / "before.json"
            after = root / "after.json"
            before.write_text(json.dumps(self._tree("Idle")), encoding="utf-8")
            after.write_text(json.dumps(self._tree("Ready")), encoding="utf-8")
            assertions = [
                {"type": "exists", "target": {"key": "status"}},
                {"type": "text_changed", "target": {"key": "status"}},
                {"type": "text_equals", "target": {"key": "status"}, "expected": "Ready"},
            ]
            results = ui_capture.evaluate_assertions(assertions, str(before), str(after), {})
            self.assertTrue(all(item["passed"] for item in results), results)

    def test_snapshot_step_evaluates_partial_assertions_immediately(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "layout.json").write_text(json.dumps(self._tree("Idle")), encoding="utf-8")

            def fake_capture(out_dir, bundle):
                snapshot = Path(out_dir)
                snapshot.mkdir(parents=True, exist_ok=True)
                screenshot = snapshot / "screenshot.png"
                layout = snapshot / "layout.json"
                summary = snapshot / "ui_summary.md"
                screenshot.write_bytes(b"png")
                layout.write_text(json.dumps(self._tree("Ready")), encoding="utf-8")
                summary.write_text("summary", encoding="utf-8")
                return str(screenshot), str(layout), str(summary), True, True, True

            step = {
                "action": "snapshot",
                "label": "ready",
                "assertions": [
                    {"type": "exists", "target": {"key": "status"}},
                    {"type": "text_equals", "target": {"key": "status"}, "expected": "Ready"},
                    {"type": "text_changed", "target": {"key": "status"}},
                ],
            }
            with mock.patch.object(ui_capture, "capture_once", side_effect=fake_capture):
                result = ui_capture.execute_step(step, [], 1080, 2340, str(root), 2, "com.example")

            self.assertTrue(result["success"], result)
            self.assertEqual(3, len(result["assertions"]))
            self.assertTrue(all(item["passed"] for item in result["assertions"]))
            self.assertIn("3/3", result["detail"])

    def test_snapshot_assertion_failure_fails_step_with_actual_and_expected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "layout.json").write_text(json.dumps(self._tree("Idle")), encoding="utf-8")

            def fake_capture(out_dir, bundle):
                snapshot = Path(out_dir)
                snapshot.mkdir(parents=True, exist_ok=True)
                screenshot = snapshot / "screenshot.png"
                layout = snapshot / "layout.json"
                summary = snapshot / "ui_summary.md"
                screenshot.write_bytes(b"png")
                layout.write_text(json.dumps(self._tree("Loading")), encoding="utf-8")
                return str(screenshot), str(layout), str(summary), True, True, True

            step = {
                "action": "snapshot",
                "assertions": [{
                    "type": "text_equals",
                    "target": {"key": "status"},
                    "expected": "Ready",
                    "message": "intermediate status",
                }],
            }
            with mock.patch.object(ui_capture, "capture_once", side_effect=fake_capture):
                result = ui_capture.execute_step(step, [], 1080, 2340, str(root), 1, "com.example")

            self.assertFalse(result["success"])
            self.assertIn("intermediate status", result["detail"])
            self.assertIn('期望="Ready"', result["detail"])

    def test_snapshot_assertions_require_layout_and_target_bundle(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            screenshot = root / "only.png"
            screenshot.write_bytes(b"png")
            capture = (str(screenshot), str(root / "missing.json"), "", True, False, False)
            step = {"action": "snapshot", "assertions": [{"type": "exists", "target": {"key": "x"}}]}
            with mock.patch.object(ui_capture, "capture_once", return_value=capture):
                result = ui_capture.execute_step(step, [], 1080, 2340, str(root), 1, "com.example")
            self.assertFalse(result["success"])
            self.assertIn("控件树未采集到", result["detail"])

    def test_scenario_validation_rejects_non_array_snapshot_assertions(self):
        scenario = {"steps": [{"action": "snapshot", "assertions": {"type": "exists"}}]}
        with self.assertRaisesRegex(ValueError, "snapshot step 1.assertions must be an array"):
            ui_capture.validate_scenario(scenario)

    def test_snapshot_label_cannot_escape_output_directory(self):
        label = ui_capture._snapshot_label("../../outside:bad", 1)
        self.assertNotIn("/", label)
        self.assertNotIn("\\", label)
        self.assertNotIn(":", label)


class HdcResultTests(unittest.TestCase):
    def test_exit_zero_fail_marker_is_failure(self):
        reason = hdc_utils.hdc_failure_reason(0, "[Fail]ExecuteCommand need connect-key")
        self.assertIn("hdc reported failure", reason or "")

    def test_exit_zero_disconnected_device_is_failure(self):
        self.assertFalse(hdc_utils.hdc_command_ok(0, "Device not founded or connected"))

    def test_nonzero_exit_is_failure_even_without_output(self):
        self.assertEqual("exit code 7", hdc_utils.hdc_failure_reason(7, ""))

    def test_success_and_no_error_are_not_false_positives(self):
        self.assertTrue(hdc_utils.hdc_command_ok(0, "Success"))
        self.assertTrue(hdc_utils.hdc_command_ok(0, "No error detected"))

    def test_ui_command_wrapper_uses_shared_semantics(self):
        self.assertFalse(ui_capture.command_ok(0, "target unauthorized"))
        self.assertTrue(ui_capture.command_ok(0, "Command executed successfully"))


class HilogAttributionTests(unittest.TestCase):
    APP = "com.example.app"
    APP_LINE = "08-20 10:11:12.123  4242  4243 E AppTag: app error"
    SYSTEM_MENTION = "08-20 10:11:12.124   901   902 E SCB: com.example.app not in featureMap"

    def test_pid_attribution_excludes_system_line_that_mentions_bundle(self):
        selected, mode = hilog_capture.select_app_lines(
            [self.APP_LINE, self.SYSTEM_MENTION], self.APP, {4242})
        self.assertEqual("pid", mode)
        self.assertEqual([self.APP_LINE], selected)

    def test_bundle_text_fallback_is_retained_when_pid_unavailable(self):
        selected, mode = hilog_capture.select_app_lines(
            [self.APP_LINE, self.SYSTEM_MENTION], self.APP, set())
        self.assertEqual("bundle-text-fallback", mode)
        self.assertEqual([self.SYSTEM_MENTION], selected)

    def test_hilog_pid_parser_requires_standard_prefix(self):
        self.assertEqual(4242, hilog_capture.extract_hilog_pid(self.APP_LINE))
        self.assertIsNone(hilog_capture.extract_hilog_pid("SCB mentions pid 4242"))

    def test_pidof_rejects_text_failure_with_exit_zero(self):
        self.assertEqual(set(), hilog_capture.parse_pidof_output(0, "[Fail]Device not found"))
        self.assertEqual({42, 43}, hilog_capture.parse_pidof_output(0, "42 43"))

    def test_ps_parser_uses_exact_bundle_or_child_process(self):
        output = "\n".join([
            "u0_a1 4242 1 com.example.app",
            "u0_a1 4244 1 com.example.app:worker",
            "u0_a1 9999 1 com.example.application",
        ])
        self.assertEqual({4242, 4244}, hilog_capture.parse_ps_pids(output, self.APP))

    def test_query_pids_falls_back_from_pidof_to_ps(self):
        responses = [
            (0, "[Fail]ExecuteCommand need connect-key"),
            (0, "u0_a1 4242 1 com.example.app"),
        ]
        with mock.patch.object(hilog_capture, "run_result", side_effect=responses):
            pids, source = hilog_capture.query_app_pids(Path("fake-hdc"), "target", self.APP)
        self.assertEqual({4242}, pids)
        self.assertEqual("ps", source)

    def test_checked_run_rejects_exit_zero_text_failure(self):
        with mock.patch.object(hilog_capture, "run_result", return_value=(0, "[Fail]Device offline")):
            with self.assertRaisesRegex(RuntimeError, "app launch failed"):
                hilog_capture.checked_run(["fake-hdc", "shell"], "app launch")

    def test_hilog_transport_check_ignores_failure_words_inside_app_log(self):
        business_log = "08-20 10:11:12.123  4242  4243 E AppTag: connection failed"
        self.assertIsNone(hilog_capture.hilog_transport_failure_reason(business_log))
        self.assertIn(
            "hdc reported failure",
            hilog_capture.hilog_transport_failure_reason("[Fail]Device not found") or "",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
