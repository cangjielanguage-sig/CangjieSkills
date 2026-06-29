#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
from pathlib import Path

FUNC_RE_TEMPLATE = r"public\s+func\s+{name}\s*\((?P<params>[^)]*)\)\s*(?::\s*(?P<ret>[^\{{\r\n]+))?\s*\{{"
SKIP_DIRS = {".git", ".idea", ".hvigor", "oh_modules", "node_modules", "build", "mock", "bridge", "types", "loader", "ark_interop_api"}


def should_skip(path: Path) -> bool:
    return bool(set(path.parts) & SKIP_DIRS)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def find_function(root: Path, name: str, rel_file: str | None) -> list[tuple[Path, re.Match[str]]]:
    pattern = re.compile(FUNC_RE_TEMPLATE.format(name=re.escape(name)))
    candidates = [root / rel_file] if rel_file else sorted(root.rglob("*.cj"))
    matches: list[tuple[Path, re.Match[str]]] = []
    for path in candidates:
        if not path.is_file() or should_skip(path):
            continue
        text = read_text(path)
        for match in pattern.finditer(text):
            matches.append((path, match))
    return matches


def find_existing(root: Path, name: str) -> list[Path]:
    hits: list[Path] = []
    token = re.compile(rf"\b{re.escape(name)}\b")
    for pattern in ("*.cj", "*.ets", "*.ts"):
        for path in sorted(root.rglob(pattern)):
            if path.is_file() and not should_skip(path) and token.search(read_text(path)):
                hits.append(path)
    return hits


def rel(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def main() -> int:
    parser = argparse.ArgumentParser(description="Plan an incremental ArkTS/Cangjie interop change for one Cangjie function.")
    parser.add_argument("--source", required=True, help="Source HarmonyOS project root")
    parser.add_argument("--target", required=True, help="Target HarmonyOS project root")
    parser.add_argument("--function", required=True, help="Cangjie public function name to expose")
    parser.add_argument("--file", help="Optional source-relative .cj file to inspect")
    args = parser.parse_args()

    source = Path(args.source).expanduser().resolve()
    target = Path(args.target).expanduser().resolve()
    matches = find_function(source, args.function, args.file)
    if not matches:
        raise SystemExit(f"No public func {args.function}(...) found under {source}")
    if len(matches) > 1 and not args.file:
        print(f"Found {len(matches)} candidate functions; rerun with --file to disambiguate.")
    print(f"Function: {args.function}")
    for path, match in matches:
        rel_path = rel(path, source)
        target_path = target / rel_path
        params = " ".join(match.group("params").split())
        ret = " ".join((match.group("ret") or "Unit").split())
        print()
        print(f"Source file: {rel_path}")
        print(f"Signature: public func {args.function}({params}): {ret}")
        print(f"Target file: {rel(target_path, target)} ({'exists' if target_path.exists() else 'missing'})")

    print()
    print("Existing target references:")
    for path in find_existing(target, args.function) or []:
        print(f"  - {rel(path, target)}")
    if not find_existing(target, args.function):
        print("  - (none)")

    print()
    print("Incremental checklist:")
    print("  - Add or update the business function in the target Cangjie file.")
    print("  - Add a thin method in the target @Interop[ArkTS] bridge class.")
    print("  - Update generated/provisional interop declarations for ArkTS type checking.")
    print("  - Add or update the ArkTS wrapper method that app code should call.")
    print("  - Run scripts/scan_interop_project.py on the target project.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
