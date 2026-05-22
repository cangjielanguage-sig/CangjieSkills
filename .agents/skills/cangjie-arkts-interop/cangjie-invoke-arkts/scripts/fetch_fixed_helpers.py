#!/usr/bin/env python3
"""Copy fixed local Cangjie ArkTS bridge helper files into ark_wrapper/ (default output dir)."""

from __future__ import annotations

import argparse
import pathlib
import re


HELPERS = {
    "ark_api_call_async.cj": pathlib.Path(__file__).resolve().parent.parent / "ark_wrapper" / "ark_api_call_async.cj",
    "callback_manager.cj": pathlib.Path(__file__).resolve().parent.parent / "ark_wrapper" / "callback_manager.cj",
    "business_exception.cj": pathlib.Path(__file__).resolve().parent.parent / "ark_wrapper" / "business_exception.cj",
}


def rewrite_package(source: str, package_name: str) -> str:
    return re.sub(r"(?m)^package\s+\S+\s*$", f"package {package_name}", source, count=1)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--bridge-dir",
        default="ark_wrapper",
        help="Directory where helper files are written (default: ark_wrapper)",
    )
    parser.add_argument("--package", required=True, help="Cangjie package name for generated helper files")
    parser.add_argument("--force", action="store_true", help="Overwrite existing helper files")
    args = parser.parse_args()

    bridge_dir = pathlib.Path(args.bridge_dir)
    bridge_dir.mkdir(parents=True, exist_ok=True)

    for filename, local_path in HELPERS.items():
        target = bridge_dir / filename
        if target.exists() and not args.force:
            print(f"skip existing {target}")
            continue

        if not local_path.exists():
            raise FileNotFoundError(f"missing local helper template: {local_path}")
        source = local_path.read_text(encoding="utf-8")
        target.write_text(rewrite_package(source, args.package), encoding="utf-8")
        print(f"wrote {target} (local:{local_path})")


if __name__ == "__main__":
    main()
