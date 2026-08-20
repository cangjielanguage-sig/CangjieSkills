#!/usr/bin/env python3
"""Bounded HarmonyOS hilog capture helper for Agent diagnostics."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

_TOOLS_DIR = Path(__file__).resolve().parent
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))

from hdc_utils import hdc_command_ok, hdc_failure_reason


DEFAULT_HDC = Path(r"C:\Program Files\Huawei\DevEco Studio\sdk\default\openharmony\toolchains\hdc.exe")


def _load_config_helpers():
    skills_dir = Path(__file__).resolve().parents[2]
    helper_dir = skills_dir / "cangjie-harmonyos-dev" / "tools"
    if helper_dir.exists():
        sys.path.insert(0, str(helper_dir))
    try:
        from config_loader import detect_project_runtime, first_value, load_harmony_config
        return detect_project_runtime, first_value, load_harmony_config
    except ImportError:
        return (
            lambda *_, **__: None,
            lambda *values: next((v for v in values if v is not None and v != ""), None),
            lambda **_: None,
        )


detect_project_runtime, first_value, load_harmony_config = _load_config_helpers()


def resolve_hdc(explicit: str | None = None) -> Path:
    if explicit:
        return Path(explicit).expanduser()
    found = shutil.which("hdc")
    if found:
        return Path(found)
    return DEFAULT_HDC


def hdc_cmd(hdc: Path, target: str | None, *args: str) -> list[str]:
    cmd = [str(hdc)]
    if target:
        cmd.extend(["-t", target])
    cmd.extend(args)
    return cmd


def run_result(cmd: list[str], timeout: int = 30) -> tuple[int, str]:
    proc = subprocess.run(cmd, capture_output=True, text=True, errors="replace", timeout=timeout)
    return proc.returncode, (proc.stdout + proc.stderr).strip()


def run(cmd: list[str], timeout: int = 30) -> str:
    return run_result(cmd, timeout=timeout)[1]


def checked_run(cmd: list[str], operation: str, timeout: int = 30) -> str:
    """Run hdc and reject failures reported only through command output."""
    code, output = run_result(cmd, timeout=timeout)
    reason = hdc_failure_reason(code, output)
    if reason:
        raise RuntimeError(f"{operation} failed: {reason}")
    return output


def capture_process(cmd: list[str], out_file: Path, seconds: int) -> None:
    with out_file.open("w", encoding="utf-8", errors="replace") as fh:
        proc = subprocess.Popen(cmd, stdout=fh, stderr=subprocess.STDOUT, text=True, errors="replace")
        try:
            proc.wait(timeout=seconds)
        except subprocess.TimeoutExpired:
            proc.terminate()
            try:
                proc.wait(timeout=3)
            except subprocess.TimeoutExpired:
                proc.kill()
                proc.wait(timeout=3)

    # A disconnected hdc can finish immediately with exit code 0 and a textual
    # failure. A normally bounded hilog process is terminated by us, so its exit
    # code is intentionally not used here.
    output = out_file.read_text(encoding="utf-8", errors="replace") if out_file.exists() else ""
    reason = hilog_transport_failure_reason(output)
    if reason:
        raise RuntimeError(f"hilog capture failed: {reason}")


def hilog_transport_failure_reason(output: str) -> str | None:
    """Inspect hdc control output without mistaking application log text for hdc failure."""
    control_output = "\n".join(
        line for line in output.splitlines() if extract_hilog_pid(line) is None
    )
    return hdc_failure_reason(0, control_output)


def parse_pidof_output(exit_code: int, output: str) -> set[int]:
    """Parse `pidof` output only when hdc reports semantic success."""
    if not hdc_command_ok(exit_code, output):
        return set()
    tokens = output.replace("\r", " ").replace("\n", " ").split()
    if not tokens or any(not token.isdigit() for token in tokens):
        return set()
    return {int(token) for token in tokens if int(token) > 0}


def _process_matches(name: str, bundle: str) -> bool:
    return name == bundle or name.startswith(bundle + ":")


def parse_ps_pids(output: str, bundle: str) -> set[int]:
    """Extract app process IDs from common toybox `ps` output variants."""
    pids: set[int] = set()
    for raw_line in output.splitlines():
        fields = raw_line.split()
        if len(fields) < 2 or not _process_matches(fields[-1], bundle):
            continue
        pid = next((int(field) for field in fields[:-1] if field.isdigit() and int(field) > 0), None)
        if pid is not None:
            pids.add(pid)
    return pids


def query_app_pids(hdc: Path, target: str | None, bundle: str) -> tuple[set[int], str]:
    """Resolve target PIDs, preferring pidof and falling back to process listing."""
    code, output = run_result(hdc_cmd(hdc, target, "shell", "pidof", bundle), timeout=15)
    pids = parse_pidof_output(code, output)
    if pids:
        return pids, "pidof"

    ps_code, ps_output = run_result(hdc_cmd(hdc, target, "shell", "ps", "-A"), timeout=15)
    if hdc_command_ok(ps_code, ps_output):
        pids = parse_ps_pids(ps_output, bundle)
        if pids:
            return pids, "ps"
    return set(), "bundle-text-fallback"


_HILOG_PID = re.compile(
    r"^\s*\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}(?:\.\d+)?\s+(\d+)\s+(\d+)\b"
)


def extract_hilog_pid(line: str) -> int | None:
    """Return the process ID from the standard hilog timestamp/PID/TID prefix."""
    match = _HILOG_PID.match(line)
    return int(match.group(1)) if match else None


def select_app_lines(lines: list[str], bundle: str, pids: set[int]) -> tuple[list[str], str]:
    """Attribute lines by PID when possible, with bundle text as legacy fallback."""
    if pids:
        return [line for line in lines if extract_hilog_pid(line) in pids], "pid"
    return [line for line in lines if bundle in line], "bundle-text-fallback"


def summarize(log_file: Path) -> dict[str, int]:
    counts = {"FATAL": 0, "ERROR": 0, "WARN": 0, "INFO": 0}
    if not log_file.exists():
        return counts
    for line in log_file.read_text(encoding="utf-8", errors="replace").splitlines():
        upper = line.upper()
        if " F " in upper or "FATAL" in upper:
            counts["FATAL"] += 1
        elif " E " in upper or "ERROR" in upper:
            counts["ERROR"] += 1
        elif " W " in upper or "WARN" in upper:
            counts["WARN"] += 1
        elif " I " in upper or "INFO" in upper:
            counts["INFO"] += 1
    return counts


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle", default=None)
    parser.add_argument("--ability", default=None)
    parser.add_argument("--module", default=None)
    parser.add_argument("--project-root", default=".")
    parser.add_argument("--out", required=True)
    parser.add_argument("--target", default=None)
    parser.add_argument("--hdc", default=None)
    parser.add_argument("--config", action="append", default=None, help="Path to cangjie.skills.toml.")
    parser.add_argument("--seconds", type=int, default=8)
    parser.add_argument("--no-launch", action="store_true")
    parser.add_argument("--no-clear", action="store_true")
    args = parser.parse_args()

    project = Path(args.project_root).expanduser().resolve()
    cfg = load_harmony_config(project_root=project, config_paths=args.config)
    toolchain_cfg = getattr(cfg, "toolchain", None)
    device_cfg = getattr(cfg, "device", None)
    runtime_cfg = getattr(cfg, "runtime", None)

    configured_module = getattr(runtime_cfg, "module", None) if runtime_cfg else None
    if not args.module:
        args.module = configured_module
    detected = detect_project_runtime(project, module=args.module)
    for warning in getattr(detected, "warnings", []) or []:
        print(f"WARN: {warning}")
    args.bundle = first_value(args.bundle, getattr(runtime_cfg, "bundle", None) if runtime_cfg else None, getattr(detected, "bundle", None))
    args.ability = first_value(args.ability, getattr(runtime_cfg, "ability", None) if runtime_cfg else None, getattr(detected, "ability", None))
    args.module = first_value(args.module, getattr(detected, "module", None))
    if not args.target:
        args.target = getattr(device_cfg, "target", None) if device_cfg else None
    if not args.target:
        args.target = "127.0.0.1:5555"

    if not args.bundle:
        raise SystemExit("bundle not detected. Pass --bundle or set [runtime].bundle as an advanced override.")
    if not args.ability:
        raise SystemExit("ability not detected. Pass --ability or set [runtime].ability as an advanced override.")

    hdc = resolve_hdc(args.hdc or (getattr(toolchain_cfg, "hdc", None) if toolchain_cfg else None))
    if not hdc.exists():
        raise SystemExit(f"hdc not found: {hdc}. Configure [toolchain].hdc or pass --hdc.")

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    if not args.no_clear:
        try:
            print(checked_run(hdc_cmd(hdc, args.target, "shell", "hilog", "-r"), "hilog clear", timeout=20))
        except RuntimeError as exc:
            raise SystemExit(str(exc)) from exc

    if not args.no_launch:
        launch_args = ["shell", "aa", "start", "-a", args.ability, "-b", args.bundle]
        if args.module:
            launch_args.extend(["-m", args.module])
        try:
            print(checked_run(hdc_cmd(hdc, args.target, *launch_args), "app launch", timeout=20))
        except RuntimeError as exc:
            raise SystemExit(str(exc)) from exc
        time.sleep(2)

    pids, pid_source = query_app_pids(hdc, args.target, args.bundle)

    full_log = out_dir / "hilog_full.txt"
    err_log = out_dir / "hilog_error.txt"
    app_log = out_dir / "hilog_app.txt"

    try:
        capture_process(hdc_cmd(hdc, args.target, "shell", "hilog"), full_log, args.seconds)
        capture_process(hdc_cmd(hdc, args.target, "shell", "hilog", "-L", "E"), err_log, max(3, min(args.seconds, 8)))
    except RuntimeError as exc:
        raise SystemExit(str(exc)) from exc

    # Include a PID observed after capture in case the app restarted during the
    # bounded window. Never weaken a successful PID attribution to text matching.
    after_pids, after_source = query_app_pids(hdc, args.target, args.bundle)
    pids.update(after_pids)
    if pid_source == "bundle-text-fallback" and after_pids:
        pid_source = after_source

    all_lines: list[str] = []
    if full_log.exists():
        all_lines = full_log.read_text(encoding="utf-8", errors="replace").splitlines()
    lines, attribution_mode = select_app_lines(all_lines, args.bundle, pids)
    app_log.write_text("\n".join(lines), encoding="utf-8")

    counts = summarize(full_log)
    app_counts = summarize(app_log)
    summary = out_dir / "hilog_summary.md"
    summary.write_text(
        "\n".join([
            "# hilog Summary",
            "",
            f"- bundle: `{args.bundle}`",
            f"- ability: `{args.ability}`",
            f"- target: `{args.target}`",
            f"- capture_seconds: {args.seconds}",
            f"- attribution: `{attribution_mode}`",
            f"- process_discovery: `{pid_source}`",
            f"- app_pids: `{', '.join(str(pid) for pid in sorted(pids)) or 'unavailable'}`",
            f"- full_log: `{full_log}`",
            f"- error_log: `{err_log}`",
            f"- app_log: `{app_log}`",
            "",
            "## Level Counts (full log)",
            "",
            f"- FATAL: {counts['FATAL']}",
            f"- ERROR: {counts['ERROR']}",
            f"- WARN: {counts['WARN']}",
            f"- INFO: {counts['INFO']}",
            "",
            "## App Lines",
            "",
            f"- Attributed app lines: {len(lines)}",
            f"- App-line FATAL: {app_counts['FATAL']}",
            f"- App-line ERROR: {app_counts['ERROR']}",
            f"- App-line WARN: {app_counts['WARN']}",
            f"- App-line INFO: {app_counts['INFO']}",
        ]),
        encoding="utf-8",
    )
    print(summary)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
