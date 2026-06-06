#!/usr/bin/env python3
"""graph 发布评测入口脚本 — 透传参数调用 graph/evals/run_eval.py。

本脚本是 graph 分区维护流水线的评测入口，仅作为便捷的命令行入口，
实际评测逻辑在 graph/evals/run_eval.py 中实现。所有参数原样透传。
"""
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
EVAL_SCRIPT = SCRIPT_DIR.parent / "evals" / "run_eval.py"

subprocess.run([sys.executable, str(EVAL_SCRIPT)] + sys.argv[1:], check=True)