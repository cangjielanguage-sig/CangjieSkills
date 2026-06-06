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

    log_lines = [
        ">>> ohpm install --all --registry https://ohpm.openharmony.cn/ohpm/ --strict_ssl true",
        "ERROR NO_ACTIONABLE_DIAGNOSTIC: build failed without stack, module, file, or error code",
    ]
    text = "\n".join(log_lines) + "\n"
    (project / "build.log").write_text(text, encoding="utf-8")
    with (project / "build.attempts.log").open("a", encoding="utf-8") as f:
        f.write(text)
    print(text, end="")
    return 9


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
