#!/usr/bin/env python3
"""Install stdx for HarmonyOS x64 emulator and ARM64 device targets."""

from __future__ import annotations

import sys
from pathlib import Path

sys.dont_write_bytecode = True
TOOLS_ROOT = Path(__file__).resolve().parent
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))

from harmonyos_stdx.cli import main


if __name__ == "__main__":
    raise SystemExit(main())
