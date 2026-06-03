#!/usr/bin/env python3
import argparse
import json
import os
import sys
import time
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=".")
    args = parser.parse_args()

    project = Path(args.project_root).resolve()
    project.mkdir(parents=True, exist_ok=True)
    os.chdir(project)
    record_invocation(project)

    fixed = project / "config" / "fixed.txt"
    if not fixed.is_file() or "resource mapping synced" not in fixed.read_text(encoding="utf-8", errors="replace"):
        log_lines = [
            ">>> ohpm install --all --registry https://ohpm.openharmony.cn/ohpm/ --strict_ssl true",
            "ohpm install completed",
            ">>> node hvigorw.js --mode module -p module=entry@default SyncCangjieResource --analyze=normal --parallel --incremental --no-daemon",
            "ERROR EVC001 Missing generated resource mapping. See Evolution.md record FIX-EVC001.",
        ]
        write_log(project, log_lines)
        print("\n".join(log_lines))
        return 7

    log_lines = [
        ">>> ohpm install --all --registry https://ohpm.openharmony.cn/ohpm/ --strict_ssl true",
        "ohpm install completed",
        ">>> node hvigorw.js --mode module -p module=entry@default SyncCangjieResource --analyze=normal --parallel --incremental --no-daemon",
        "SyncCangjieResource completed after FIX-EVC001",
        ">>> node hvigorw.js --mode module -p product=default assembleHap --analyze=normal --parallel --incremental --no-daemon",
        "assembleHap completed",
        "BUILD SUCCESSFUL",
    ]
    write_log(project, log_lines)
    print("\n".join(log_lines))
    return 0


def record_invocation(project: Path) -> None:
    payload = {
        "argv": sys.argv,
        "cwd": str(Path.cwd()),
        "timestamp": time.time(),
    }
    with (project / "build.invocations.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(payload, ensure_ascii=False) + "\n")


def write_log(project: Path, lines: list[str]) -> None:
    text = "\n".join(lines) + "\n"
    (project / "build.log").write_text(text, encoding="utf-8")
    with (project / "build.attempts.log").open("a", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    raise SystemExit(main())
