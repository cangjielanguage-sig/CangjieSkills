#!/usr/bin/env python3
"""Normalize agent runtime traces for rollout collection.

This compatibility entrypoint writes normalized JSON to stdout. It does not
generate or save Rollout Record markdown.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from adapters import collect_trace


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(
        description="Normalize agent trace events for rollout collection."
    )
    parser.add_argument("--runtime", required=True, help="Trace runtime, e.g. codex.")
    parser.add_argument("--workspace", required=True, help="Current workspace path.")
    parser.add_argument("--trace-file", help="Explicit trace file path.")
    parser.add_argument("--session-id", help="Explicit runtime session id.")
    args = parser.parse_args()

    result = collect_trace(
        runtime=args.runtime,
        workspace=Path(args.workspace),
        trace_file=Path(args.trace_file) if args.trace_file else None,
        session_id=args.session_id,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result.get("status") == "ok" else 2


if __name__ == "__main__":
    sys.exit(main())
