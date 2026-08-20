#!/usr/bin/env python3
"""Create or repair a Cangjie HarmonyOS project from a file template."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path


DEFAULT_TEMPLATE = "cangjie-harmonyos-app"
DEFAULT_APP_NAME = "Cangjie App"
DEFAULT_BUNDLE_NAME = "com.example.myapplication"
CANONICAL_PACKAGE_NAME = "ohos_app_cangjie_entry"
DEFAULT_MODULE_NAME = "entry"
DEFAULT_VENDOR = "example"
DEFAULT_SDK_VERSION = "6.1.0(23)"
DEFAULT_MODEL_VERSION = "6.1.0"
TEXT_SUFFIXES = {
    "",
    ".cj",
    ".gitignore",
    ".json",
    ".json5",
    ".lock",
    ".md",
    ".toml",
    ".ts",
}


def _load_config_helpers():
    skills_dir = Path(__file__).resolve().parents[2]
    helper_dir = skills_dir / "cangjie-harmonyos-dev" / "tools"
    if helper_dir.exists():
        sys.path.insert(0, str(helper_dir))
    try:
        from config_loader import first_value, load_harmony_config
        return first_value, load_harmony_config
    except ImportError:
        return (
            lambda *values: next((v for v in values if v is not None and v != ""), None),
            lambda **_: None,
        )


first_value, load_harmony_config = _load_config_helpers()


def skill_root() -> Path:
    return Path(__file__).resolve().parents[1]


def templates_root() -> Path:
    return skill_root() / "templates"


def json_string_body(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)[1:-1]


def validate_bundle_name(value: str) -> None:
    pattern = re.compile(r"^[A-Za-z][A-Za-z0-9_]*(\.[A-Za-z][A-Za-z0-9_]*)+$")
    if not pattern.match(value):
        raise ValueError(
            "bundle name must use reverse-domain segments, for example com.example.todo"
        )


def validate_module_name(value: str) -> None:
    pattern = re.compile(r"^[A-Za-z][A-Za-z0-9_-]*$")
    if not pattern.match(value):
        raise ValueError("module name must contain letters, numbers, '_' or '-'")


def validate_sdk_version(value: str) -> None:
    pattern = re.compile(r"^\d+\.\d+\.\d+\(\d+\)$")
    if not pattern.match(value):
        raise ValueError("sdk version must look like 6.1.0(23)")


def validate_model_version(value: str) -> None:
    pattern = re.compile(r"^\d+\.\d+\.\d+$")
    if not pattern.match(value):
        raise ValueError("model version must look like 6.1.0")


def build_replacements(args: argparse.Namespace) -> dict[str, str]:
    validate_bundle_name(args.bundle_name)
    validate_module_name(args.module_name)
    validate_sdk_version(args.sdk_version)
    validate_model_version(args.model_version)
    return {
        "__APP_NAME__": json_string_body(args.app_name),
        "__BUNDLE_NAME__": args.bundle_name,
        "__PACKAGE_NAME__": CANONICAL_PACKAGE_NAME,
        "__VENDOR__": json_string_body(args.vendor),
        "__MODULE_NAME__": args.module_name,
        "__SDK_VERSION__": args.sdk_version,
        "__MODEL_VERSION__": args.model_version,
        "COMPILE_CONDITION_ENTRY": f"COMPILE_CONDITION_{args.module_name.upper().replace('-', '_')}",
    }


def list_templates() -> list[str]:
    root = templates_root()
    if not root.exists():
        return []
    return sorted(item.name for item in root.iterdir() if item.is_dir())


def is_text_template(path: Path) -> bool:
    return path.suffix in TEXT_SUFFIXES or path.name in TEXT_SUFFIXES


def render_text(text: str, replacements: dict[str, str]) -> str:
    for token, value in replacements.items():
        text = text.replace(token, value)
    unresolved = sorted(set(re.findall(r"__[A-Z0-9_]+__", text)))
    if unresolved:
        raise ValueError(f"unresolved template tokens: {', '.join(unresolved)}")
    return text


def ensure_writable_target(target: Path, repair: bool) -> None:
    if target.exists() and target.is_file():
        raise ValueError(f"target path is a file: {target}")
    allowed_existing = {".claude", ".agents"}
    existing = []
    if target.exists():
        existing = [item.name for item in target.iterdir() if item.name not in allowed_existing]
    if existing and not repair:
        raise ValueError(
            f"target directory is not empty: {target}. Use --repair to overwrite template files."
        )


def destination_for(relative: Path, module_name: str) -> Path:
    parts = list(relative.parts)
    if parts and parts[0] == "entry":
        parts[0] = module_name
    return Path(*parts)


def copy_template(template_dir: Path, target: Path, replacements: dict[str, str]) -> list[Path]:
    written: list[Path] = []
    module_name = replacements["__MODULE_NAME__"]
    for source in sorted(template_dir.rglob("*")):
        if source.is_dir():
            continue
        relative = source.relative_to(template_dir)
        destination = target / destination_for(relative, module_name)
        destination.parent.mkdir(parents=True, exist_ok=True)
        if is_text_template(source):
            text = source.read_text(encoding="utf-8")
            destination.write_text(render_text(text, replacements), encoding="utf-8", newline="\n")
        else:
            shutil.copy2(source, destination)
        written.append(destination)
    return written


def verify_project(target: Path, module_name: str) -> list[str]:
    required = [
        "build-profile.json5",
        "oh-package.json5",
        "hvigorfile.ts",
        "hvigor/hvigor-config.json5",
        "AppScope/app.json5",
        "AppScope/resources/base/element/string.json",
        "AppScope/resources/base/media/layered_image.json",
        f"{module_name}/build-profile.json5",
        f"{module_name}/cjpm.toml",
        f"{module_name}/src/main/module.json5",
        f"{module_name}/src/main/cangjie/index.cj",
        f"{module_name}/src/main/cangjie/main_ability.cj",
        f"{module_name}/src/main/cangjie/ability_stage.cj",
        f"{module_name}/src/main/resources/base/media/startIcon.png",
    ]
    return [item for item in required if not (target / item).exists()]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create or repair a Cangjie HarmonyOS project from packaged templates."
    )
    parser.add_argument("target", nargs="?", help="project directory to create or repair")
    parser.add_argument("--target-dir", dest="target_dir", help="project directory to create or repair")
    parser.add_argument("--template", default=DEFAULT_TEMPLATE, help="template name under templates/")
    parser.add_argument("--list-templates", action="store_true", help="list available templates and exit")
    parser.add_argument("--repair", action="store_true", help="overwrite files owned by the template")
    parser.add_argument("--config", action="append", default=None, help="Path to cangjie.skills.toml.")
    parser.add_argument("--app-name", default=None, help="display name")
    parser.add_argument("--bundle-name", default=None, help="HarmonyOS bundle name")
    parser.add_argument("--module-name", default=None, help="HarmonyOS module directory/name")
    parser.add_argument("--vendor", default=None, help="advanced: app.json5 vendor")
    parser.add_argument("--sdk-version", default=None, help="advanced: set both target and compatible SDK versions")
    parser.add_argument("--model-version", default=None, help="advanced: oh-package/hvigor model version")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    if args.list_templates:
        for name in list_templates():
            print(name)
        return 0

    target_arg = args.target_dir or args.target
    if not target_arg:
        print("error: target directory is required", file=sys.stderr)
        return 2

    try:
        target = Path(target_arg).resolve()
        cfg = load_harmony_config(project_root=target, config_paths=args.config)
        scaffold = getattr(cfg, "scaffold", None)
        args.app_name = first_value(args.app_name, getattr(scaffold, "app_name", None), DEFAULT_APP_NAME)
        args.bundle_name = first_value(args.bundle_name, getattr(scaffold, "bundle_name", None), DEFAULT_BUNDLE_NAME)
        args.module_name = first_value(args.module_name, getattr(scaffold, "module_name", None), DEFAULT_MODULE_NAME)
        args.vendor = first_value(args.vendor, DEFAULT_VENDOR)
        args.sdk_version = first_value(args.sdk_version, DEFAULT_SDK_VERSION)
        args.model_version = first_value(args.model_version, DEFAULT_MODEL_VERSION)
        template_dir = (templates_root() / args.template).resolve()
        templates_base = templates_root().resolve()
        if not template_dir.is_dir() or templates_base not in template_dir.parents:
            raise ValueError(f"template not found: {args.template}")
        replacements = build_replacements(args)
        ensure_writable_target(target, args.repair)
        target.mkdir(parents=True, exist_ok=True)
        written = copy_template(template_dir, target, replacements)
        missing = verify_project(target, args.module_name)
        if missing:
            raise ValueError("project creation verification failed: " + ", ".join(missing))
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(f"project: {target}")
    print(f"template: {args.template}")
    print(f"bundle: {args.bundle_name}")
    print(f"package: {CANONICAL_PACKAGE_NAME}")
    print(f"files_written: {len(written)}")
    print("next: run harmonyos-build-run-diagnose/tools/build_recovery.py from your installed skills directory")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
