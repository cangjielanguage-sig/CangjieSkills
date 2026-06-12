#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from common import extract_parameter_values, generate_pairwise_rows, testcase_from_rows


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate Pair-wise testcase JSON for one Cangjie API.")
    parser.add_argument("json_file", help="Full testcase JSON or parameter-only JSON")
    parser.add_argument("--api", help="API name when reading a full testcase JSON")
    parser.add_argument("--output", "-o", help="Write the generated JSON fragment to this file")
    parser.add_argument(
        "--result",
        default="请补充该组合调用的可验证预期结果",
        help="预期结果 text used for each generated testcase",
    )
    parser.add_argument(
        "--max-candidates",
        type=int,
        default=200000,
        help="Maximum Cartesian candidates to scan while building Pair-wise rows",
    )
    args = parser.parse_args()

    with open(args.json_file, "r", encoding="utf-8-sig") as handle:
        data = json.load(handle)

    api, parameters = extract_parameter_values(data, args.api)
    rows = generate_pairwise_rows(parameters, args.max_candidates)
    fragment = "不涉及" if not rows else testcase_from_rows(api, rows, args.result)
    text = json.dumps(fragment, ensure_ascii=False, indent=2)

    if args.output:
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        with open(args.output, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text + "\n")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
