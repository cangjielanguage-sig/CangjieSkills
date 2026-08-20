#!/usr/bin/env python3
"""Add a Cangjie UI component and ArkTS CJHybridComponent wrapper page."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


def _load_config_helpers():
    skills_dir = Path(__file__).resolve().parents[2]
    helper_dir = skills_dir / "cangjie-harmonyos-dev" / "tools"
    if helper_dir.exists():
        sys.path.insert(0, str(helper_dir))
    try:
        from config_loader import detect_project_runtime, first_value, load_harmony_config
        return detect_project_runtime, first_value, load_harmony_config
    except ImportError:
        return (
            lambda *_, **__: None,
            lambda *values: next((v for v in values if v is not None and v != ""), None),
            lambda **_: None,
        )


detect_project_runtime, first_value, load_harmony_config = _load_config_helpers()
CJHYBRIDCOMPONENT_VERSION = "1.1.1"


def skill_root() -> Path:
    return Path(__file__).resolve().parents[1]


def template_dir() -> Path:
    return skill_root() / "templates" / "cjhybridcomponent"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def validate_identifier(value: str, label: str) -> None:
    if not re.match(r"^[A-Za-z_][A-Za-z0-9_]*$", value):
        raise ValueError(f"{label} must be a valid identifier")


def parse_cjpm_package(cjpm: Path) -> str:
    in_package = False
    for line in read_text(cjpm).splitlines():
        stripped = line.strip()
        if stripped == "[package]":
            in_package = True
            continue
        if stripped.startswith("[") and stripped != "[package]":
            in_package = False
        if in_package:
            match = re.match(r'name\s*=\s*"([^"]+)"', stripped)
            if match:
                return match.group(1)
    raise ValueError(f"cannot find [package].name in {cjpm}")


def snake_name(name: str) -> str:
    out = re.sub(r"(?<!^)([A-Z])", r"_\1", name).lower()
    return re.sub(r"[^a-z0-9_]+", "_", out).strip("_") or "component"


def render_template(name: str, replacements: dict[str, str]) -> str:
    path = template_dir() / name
    text = path.read_text(encoding="utf-8")
    for token, value in replacements.items():
        text = text.replace(token, value)
    unresolved = sorted(set(re.findall(r"__[A-Z0-9_]+__", text)))
    if unresolved:
        raise ValueError(f"unresolved template tokens: {', '.join(unresolved)}")
    return text


def add_dependency(oh_package: Path) -> bool:
    text = read_text(oh_package)
    if '"@cangjie/cjhybridcomponent"' in text:
        updated = re.sub(
            r'("@cangjie/cjhybridcomponent"\s*:\s*)"1\.0\.0"',
            rf'\1"{CJHYBRIDCOMPONENT_VERSION}"',
            text,
        )
        if updated == text:
            return False
        write_text(oh_package, updated)
        return True
    marker = '"dependencies": {'
    if marker not in text:
        raise ValueError(f"{oh_package} does not contain a dependencies object")
    idx = text.index(marker) + len(marker)
    remainder = text[idx:]
    if re.search(r'"\S+"\s*:', remainder.split("}", 1)[0]):
        insert = f'\n    "@cangjie/cjhybridcomponent": "{CJHYBRIDCOMPONENT_VERSION}",'
    else:
        insert = f'\n    "@cangjie/cjhybridcomponent": "{CJHYBRIDCOMPONENT_VERSION}"'
    text = text[:idx] + insert + text[idx:]
    # If inserted before existing dependency, ensure JSON5 comma after new line is OK.
    text = text.replace(
        f'"@cangjie/cjhybridcomponent": "{CJHYBRIDCOMPONENT_VERSION}",\n    \n',
        f'"@cangjie/cjhybridcomponent": "{CJHYBRIDCOMPONENT_VERSION}",\n',
    )
    write_text(oh_package, text)
    return True


def strip_json5_comments(text: str) -> str:
    text = re.sub(r"//.*", "", text)
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    text = re.sub(r",\s*([}\]])", r"\1", text)
    return text


def update_main_pages(path: Path, page_ref: str) -> bool:
    raw = read_text(path)
    try:
        data = json.loads(strip_json5_comments(raw))
    except Exception:
        data = {"src": []}
    src = data.get("src")
    if not isinstance(src, list):
        src = []
        data["src"] = src
    if page_ref in src:
        return False
    src.append(page_ref)
    write_text(path, json.dumps(data, ensure_ascii=False, indent=2))
    return True


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Add a Cangjie HybridComponent and ArkTS wrapper page.")
    parser.add_argument("--project-root", default=".", help="project root")
    parser.add_argument("--config", action="append", default=None, help="Path to cangjie.skills.toml.")
    parser.add_argument("--module", default=None, help="HarmonyOS module")
    parser.add_argument("--component", required=True, help="Cangjie component class name")
    parser.add_argument("--page", default=None, help="ArkTS page file stem/ref, default is component name in lower snake case")
    parser.add_argument("--title", default=None, help="initial Cangjie component title")
    parser.add_argument("--button-text", default="Tap Cangjie Component")
    parser.add_argument("--clicked-title", default=None, help="title after clicking the Cangjie button")
    parser.add_argument("--force", action="store_true", help="overwrite existing generated component/page files")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    try:
        validate_identifier(args.component, "component")
        project = Path(args.project_root).expanduser().resolve()
        cfg = load_harmony_config(project_root=project, config_paths=args.config)
        runtime_cfg = getattr(cfg, "runtime", None)
        detected = detect_project_runtime(project, module=args.module or (getattr(runtime_cfg, "module", None) if runtime_cfg else None))
        args.module = first_value(args.module, getattr(runtime_cfg, "module", None) if runtime_cfg else None, getattr(detected, "module", None), "entry")
        module = project / args.module
        package_name = parse_cjpm_package(module / "cjpm.toml")
        page_stem = args.page or snake_name(args.component)
        page_stem = page_stem.replace("\\", "/").strip("/")
        if page_stem.startswith("pages/"):
            page_file_stem = page_stem.removeprefix("pages/")
            page_ref = page_stem
        else:
            page_file_stem = page_stem
            page_ref = f"pages/{page_stem}"
        wrapper_struct = re.sub(r"[^A-Za-z0-9_]", "_", page_file_stem.title().replace("_", ""))
        validate_identifier(wrapper_struct, "wrapper struct")

        replacements = {
            "__PACKAGE_NAME__": package_name,
            "__COMPONENT_NAME__": args.component,
            "__WRAPPER_STRUCT__": wrapper_struct,
            "__TITLE__": args.title or f"{args.component} Panel",
            "__BUTTON_TEXT__": args.button_text,
            "__CLICKED_TITLE__": args.clicked_title or f"{args.component} Clicked",
        }

        component_path = module / "src/main/cangjie" / f"{snake_name(args.component)}.cj"
        wrapper_path = module / "src/main/ets/pages" / f"{page_file_stem}.ets"
        for path in (component_path, wrapper_path):
            if path.exists() and not args.force:
                raise ValueError(f"refusing to overwrite existing file without --force: {path}")

        write_text(component_path, render_template("Component.cj.tpl", replacements))
        write_text(wrapper_path, render_template("Wrapper.ets.tpl", replacements))
        dep_added = add_dependency(module / "oh-package.json5")
        route_added = update_main_pages(module / "src/main/resources/base/profile/main_pages.json", page_ref)
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(f"component: {component_path}")
    print(f"wrapper: {wrapper_path}")
    print(f"page_ref: {page_ref}")
    print(f"dependency_added: {dep_added}")
    print(f"route_added: {route_added}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
