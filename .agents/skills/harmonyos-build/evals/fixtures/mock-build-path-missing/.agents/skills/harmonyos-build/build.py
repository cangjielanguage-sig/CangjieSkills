#!/usr/bin/env python3
import argparse
import json
import os
import sys
import time
from pathlib import Path


DEVECO_HOME_WINDOWS = r"C:/Missing/DevEco Studio"
DEVECO_HOME_LINUX = "/missing/DevEco-Studio"
DEVECO_HOME_MACOS = "/missing/DevEco-Studio.app/Contents"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=".")
    args = parser.parse_args()

    project = Path(args.project_root).resolve()
    project.mkdir(parents=True, exist_ok=True)
    os.chdir(project)
    record_invocation(project)

    message = f"错误: DevEco Studio 不存在: {DEVECO_HOME_WINDOWS}"
    (project / "startup-error.log").write_text(message + "\n", encoding="utf-8")
    print(message)
    return 2


def record_invocation(project: Path) -> None:
    payload = {
        "argv": sys.argv,
        "cwd": str(Path.cwd()),
        "timestamp": time.time(),
    }
    with (project / "build.invocations.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(payload, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    raise SystemExit(main())
