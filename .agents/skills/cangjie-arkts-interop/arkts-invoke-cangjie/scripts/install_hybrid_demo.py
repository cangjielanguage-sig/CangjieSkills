#!/usr/bin/env python3

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def replace_text(path: Path, replacements: dict[str, str]) -> None:
    text = path.read_text(encoding="utf-8")
    for old, new in replacements.items():
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Copy the hybrid demo template and apply basic replacements."
    )
    parser.add_argument("--target", required=True, help="Output directory")
    parser.add_argument(
        "--bundle-name",
        default="com.example.hybriddemo",
        help="Replacement for AppScope/app.json5 bundleName",
    )
    parser.add_argument(
        "--module-name",
        default="entry",
        help="Replacement for entry module name",
    )
    parser.add_argument(
        "--lib-name",
        default="libmathbridge.so",
        help="Replacement for requireCJLib library name",
    )
    parser.add_argument(
        "--package-name",
        default="mathbridge",
        help="Replacement for cjpm.toml package name and version string prefix",
    )
    args = parser.parse_args()

    skill_dir = Path(__file__).resolve().parent.parent
    source = skill_dir / "assets" / "hybrid-demo"
    target = Path(args.target).expanduser().resolve()

    if target.exists():
        raise SystemExit(f"Target already exists: {target}")

    shutil.copytree(source, target)

    replacements = {
        "com.example.hybriddemo": args.bundle_name,
        '"name": "entry"': f'"name": "{args.module_name}"',
        "libmathbridge.so": args.lib_name,
        'name = "mathbridge"': f'name = "{args.package_name}"',
        "mathbridge-0.1.0": f"{args.package_name}-0.1.0",
    }

    replace_text(target / "AppScope" / "app.json5", replacements)
    replace_text(target / "entry" / "src" / "main" / "module.json5", replacements)
    replace_text(
        target / "entry" / "src" / "main" / "ets" / "pages" / "Index.ets",
        replacements,
    )
    replace_text(
        target / "entry" / "src" / "main" / "cangjie" / "cjpm.toml",
        replacements,
    )
    replace_text(
        target / "entry" / "src" / "main" / "cangjie" / "MathBridge.cj",
        replacements,
    )
    replace_text(
        target
        / "entry"
        / "src"
        / "main"
        / "cangjie"
        / "ark_interop_api"
        / "MathBridge.d.ets",
        replacements,
    )

    print(f"Installed hybrid demo to: {target}")
    print("Next steps:")
    print("  1. Merge the generated files into a DevEco-created Stage project.")
    print("  2. Regenerate ark_interop_api from the IDE.")
    print("  3. Verify the final .so name and update requireCJLib if needed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
