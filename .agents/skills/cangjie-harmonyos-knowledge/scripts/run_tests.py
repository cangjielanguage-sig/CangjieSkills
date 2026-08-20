from __future__ import annotations

import argparse
import sys
import unittest
from pathlib import Path

SCRIPTS_ROOT = Path(__file__).resolve().parent
SKILL_ROOT = SCRIPTS_ROOT.parent
if str(SCRIPTS_ROOT) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_ROOT))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the knowledge package unit and optional live tests.")
    parser.add_argument("--pattern", default="test_*.py", help="unittest discovery filename pattern")
    parser.add_argument("-v", "--verbosity", type=int, choices=(0, 1, 2), default=2)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    suite = unittest.defaultTestLoader.discover(str(SKILL_ROOT / "tests"), pattern=args.pattern)
    return 0 if unittest.TextTestRunner(verbosity=args.verbosity).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
