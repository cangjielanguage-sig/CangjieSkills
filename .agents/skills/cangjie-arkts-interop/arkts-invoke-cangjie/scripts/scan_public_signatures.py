#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path


BUILTIN_TYPES = {
    "Unit",
    "String",
    "Bool",
    "Byte",
    "Int8",
    "Int16",
    "Int32",
    "Int64",
    "UInt8",
    "UInt16",
    "UInt32",
    "UInt64",
    "Float16",
    "Float32",
    "Float64",
    "Rune",
    "Object",
    "Exception",
}

# Common container / std types that should not be treated as "custom domain types"
KNOWN_WRAPPER_TYPES = {
    "Option",
    "Array",
    "ArrayList",
    "HashMap",
    "ConcurrentHashMap",
    "JSArrayEx",
    "JSHashMapEx",
    "JSStringEx",
    "JSValue",
    "JSObject",
    "JSContext",
    "JSCallInfo",
    "Duration",
    "Path",
    "File",
    "Client",
    "HttpRequestBuilder",
    "HttpResponse",
}


CLASS_RE = re.compile(r"^\s*public\s+(class|interface)\s+([A-Za-z_]\w*)\b", re.MULTILINE)
TOP_FUNC_RE = re.compile(r"^\s*public\s+func\s+([A-Za-z_]\w*)\s*\((.*?)\)\s*:\s*([^ {\\n]+)", re.MULTILINE)
METHOD_RE = re.compile(r"^\s*public\s+func\s+([A-Za-z_]\w*)\s*\((.*?)\)\s*:\s*([^ {\\n]+)", re.MULTILINE)


def should_skip(path: Path) -> bool:
    parts = set(path.parts)
    return any(
        name in parts
        for name in (
            ".git",
            ".idea",
            ".hvigor",
            ".gradle",
            "node_modules",
            "oh_modules",
            "build",
            "dist",
            ".next",
            "ark_interop_api",
            "bridge",
            "mock",
            "types",
            "loader",
        )
    )


@dataclass
class PublicFunc:
    owner_kind: str  # "top-level" | "class" | "interface"
    owner_name: str
    name: str
    params_raw: str
    return_raw: str
    file: str

    def signature(self) -> str:
        return f"public func {self.name}({self.params_raw}): {self.return_raw}"


def split_param_types(params_raw: str) -> list[str]:
    """
    Best-effort split; avoids parsing nested generics perfectly.
    Cangjie parameters look like: "a: Int64, b: Option<String>"
    """
    params_raw = params_raw.strip()
    if not params_raw:
        return []
    out: list[str] = []
    depth = 0
    current = []
    for ch in params_raw:
        if ch in "<(":
            depth += 1
        elif ch in ">)":
            depth = max(0, depth - 1)
        if ch == "," and depth == 0:
            out.append("".join(current).strip())
            current = []
        else:
            current.append(ch)
    if current:
        out.append("".join(current).strip())
    types: list[str] = []
    for p in out:
        # "name: Type" -> Type
        if ":" in p:
            types.append(p.split(":", 1)[1].strip())
        else:
            types.append(p.strip())
    return [t for t in types if t]


IDENT_RE = re.compile(r"\b([A-Z][A-Za-z0-9_]*)\b")


def extract_type_idents(type_str: str) -> set[str]:
    """
    Extract capitalised identifiers as a proxy for type names.
    """
    raw = type_str.strip()
    # Remove nullable sugar like "?T" (which shouldn't appear in interop, but exists in codebases)
    if raw.startswith("?"):
        raw = raw[1:]
    return set(IDENT_RE.findall(raw))


def is_custom_type_name(name: str) -> bool:
    if name in BUILTIN_TYPES:
        return False
    if name in KNOWN_WRAPPER_TYPES:
        return False
    return True


def collect_public_api(source_root: Path) -> tuple[set[str], list[PublicFunc]]:
    cj_files = [p for p in source_root.rglob("*.cj") if p.is_file() and not should_skip(p)]
    classes: set[str] = set()
    funcs: list[PublicFunc] = []

    for path in sorted(cj_files):
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue

        for kind, name in CLASS_RE.findall(text):
            classes.add(name)

        # top-level public functions
        for m in TOP_FUNC_RE.finditer(text):
            fn, params, ret = m.group(1), m.group(2), m.group(3)
            funcs.append(
                PublicFunc(
                    owner_kind="top-level",
                    owner_name="(module)",
                    name=fn,
                    params_raw=params.strip(),
                    return_raw=ret.strip(),
                    file=str(path),
                )
            )

        # class/interface methods (best-effort: we don't fully scope to the class body; good enough for gate)
        # We record them as owner "(unknown)" unless we can cheaply infer via nearest preceding class/interface.
        # This is acceptable because the gate only needs to detect cross-type usage.
        owner_stack: list[tuple[str, str]] = []
        for idx, line in enumerate(text.splitlines(), start=1):
            cm = re.match(r"^\s*public\s+(class|interface)\s+([A-Za-z_]\w*)\b", line)
            if cm:
                owner_stack.append((cm.group(1), cm.group(2)))
                continue
            mm = re.match(r"^\s*public\s+func\s+([A-Za-z_]\w*)\s*\((.*?)\)\s*:\s*([^ {\\n]+)", line)
            if mm and owner_stack:
                ok, on = owner_stack[-1]
                funcs.append(
                    PublicFunc(
                        owner_kind=ok,
                        owner_name=on,
                        name=mm.group(1),
                        params_raw=mm.group(2).strip(),
                        return_raw=mm.group(3).strip(),
                        file=f"{path}:{idx}",
                    )
                )

    return classes, funcs


def analyse_cross_type(classes: set[str], funcs: list[PublicFunc]) -> dict[str, object]:
    issues: list[dict[str, object]] = []

    for f in funcs:
        param_types = split_param_types(f.params_raw)
        used: set[str] = set()
        for t in param_types:
            used |= extract_type_idents(t)
        used |= extract_type_idents(f.return_raw)

        custom_used = sorted(n for n in used if is_custom_type_name(n))
        cross = sorted(n for n in custom_used if n in classes)
        if cross:
            issues.append(
                {
                    "owner_kind": f.owner_kind,
                    "owner_name": f.owner_name,
                    "function": f.name,
                    "file": f.file,
                    "signature": f.signature(),
                    "cross_custom_types": cross,
                    "note": "Public signature references other public class/interface types. If object semantics must be preserved, prefer handwritten interop library (SharedObject & JSInteropType).",
                }
            )

    return {
        "summary": {
            "public_types_count": len(classes),
            "public_functions_count": len(funcs),
            "cross_type_issues_count": len(issues),
            "has_cross_type_object_transfer": len(issues) > 0,
        },
        "cross_type_issues": issues,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Scan Cangjie public signatures and detect cross-type object transfer risks.")
    ap.add_argument(
        "--source",
        required=True,
        help="Cangjie source root (e.g., <module>/src/main/cangjie)",
    )
    ap.add_argument("--json", action="store_true", help="Output JSON only")
    args = ap.parse_args()

    source_root = Path(args.source).expanduser().resolve()
    if not source_root.exists() or not source_root.is_dir():
        raise SystemExit(f"--source must be an existing directory: {source_root}")

    classes, funcs = collect_public_api(source_root)
    report = analyse_cross_type(classes, funcs)

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0

    s = report["summary"]
    print(f"Source: {source_root}")
    print(f"Public types: {s['public_types_count']}")
    print(f"Public functions (incl. methods best-effort): {s['public_functions_count']}")
    print(f"Cross-type issues: {s['cross_type_issues_count']}")
    print()
    if s["has_cross_type_object_transfer"]:
        print("Detected cross-type object transfer in public signatures.")
        print("Recommendation:")
        print("- preserve_public_api_shape = true -> use handwritten interop library (SharedObject & JSInteropType)")
        print("- preserve_public_api_shape = false -> handle pattern allowed, but must record Before → After in coverage table")
        print()
        for it in report["cross_type_issues"]:
            owner = f"{it['owner_kind']} {it['owner_name']}".strip()
            print(f"- {owner}.{it['function']}")
            print(f"  file: {it['file']}")
            print(f"  signature: {it['signature']}")
            print(f"  cross_custom_types: {', '.join(it['cross_custom_types'])}")
    else:
        print("No cross-type object transfer detected in public signatures.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
