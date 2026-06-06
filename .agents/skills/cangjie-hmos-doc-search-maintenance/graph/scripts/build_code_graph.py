#!/usr/bin/env python3
"""构建源码图谱入口脚本。转发至 build_cli.py build-code。"""
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
BUILDER_CLI = SCRIPT_DIR.parent / "builder" / "build_cli.py"

subprocess.run([sys.executable, str(BUILDER_CLI), "build-code"] + sys.argv[1:], check=True)