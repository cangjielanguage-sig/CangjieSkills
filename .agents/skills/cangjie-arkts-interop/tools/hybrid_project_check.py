#!/usr/bin/env python3
"""Validate the practical Cangjie-ArkTS hybrid app layout."""

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


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def strip_json5_comments(text: str) -> str:
    text = re.sub(r"//.*", "", text)
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    text = re.sub(r",\s*([}\]])", r"\1", text)
    return text


def load_json5ish(path: Path) -> object | None:
    try:
        return json.loads(strip_json5_comments(read_text(path)))
    except Exception:
        return None


def parse_cjpm_package(cjpm: Path) -> str | None:
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
    return None


def parse_main_pages(path: Path) -> list[str]:
    data = load_json5ish(path)
    if isinstance(data, dict) and isinstance(data.get("src"), list):
        return [str(item) for item in data["src"]]
    return []


def collect_hybrid_components(module: Path) -> list[tuple[Path, str, str]]:
    found: list[tuple[Path, str, str]] = []
    pattern = re.compile(
        r"CJHybridComponent\s*\(\s*\{(?P<body>.*?)\}\s*\)",
        re.S,
    )
    library_re = re.compile(r"library\s*:\s*['\"]([^'\"]+)['\"]")
    component_re = re.compile(r"component\s*:\s*['\"]([^'\"]+)['\"]")
    pages_dir = module / "src/main/ets/pages"
    for page in sorted(pages_dir.rglob("*.ets")) if pages_dir.exists() else []:
        text = read_text(page)
        for match in pattern.finditer(text):
            body = match.group("body")
            library = library_re.search(body)
            component = component_re.search(body)
            if library and component:
                found.append((page, library.group(1), component.group(1)))
    return found


def cangjie_component_exists(module: Path, component: str) -> bool:
    cangjie_dir = module / "src/main/cangjie"
    if not cangjie_dir.exists():
        return False
    class_re = re.compile(rf"@HybridComponentEntry\s*@Component\s*class\s+{re.escape(component)}\b", re.S)
    for path in cangjie_dir.rglob("*.cj"):
        if class_re.search(read_text(path)):
            return True
    return False


def validate(project: Path, module_name: str) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    module = project / module_name
    cjpm = module / "cjpm.toml"
    package_name = parse_cjpm_package(cjpm)
    lib_name = f"lib{package_name}.so" if package_name else None

    required = [
        project / "build-profile.json5",
        project / "oh-package.json5",
        project / "hvigorfile.ts",
        project / "AppScope/app.json5",
        module / "build-profile.json5",
        module / "oh-package.json5",
        module / "src/main/module.json5",
        module / "src/main/ets/entryability/EntryAbility.ets",
        module / "src/main/ets/pages/Index.ets",
        module / "src/main/cangjie/index.cj",
        module / "src/main/resources/base/profile/main_pages.json",
    ]
    for path in required:
        if not path.exists():
            errors.append(f"missing required file: {path}")

    if not package_name:
        errors.append(f"{cjpm}: missing [package].name")
    else:
        cjpm_text = read_text(cjpm)
        expected_condition = f"COMPILE_CONDITION_{module_name.upper().replace('-', '_')}"
        if expected_condition not in cjpm_text:
            errors.append(f"cjpm.toml should use {expected_condition} in compile-option for module {module_name}")
        index_cj = read_text(module / "src/main/cangjie/index.cj")
        if f"package {package_name}" not in index_cj:
            errors.append("Cangjie package line does not match cjpm [package].name")
        if "JSModule.registerModule" not in index_cj and "@Interop[ArkTS]" not in index_cj:
            errors.append("Cangjie code exports neither JSModule.registerModule nor @Interop[ArkTS]")

        types_dir = module / f"src/main/cangjie/types/lib{package_name}"
        if not (types_dir / "Index.d.ts").exists():
            errors.append(f"missing TypeScript declaration: {types_dir / 'Index.d.ts'}")
        type_pkg = read_text(types_dir / "oh-package.json5")
        if lib_name and f'"name": "{lib_name}"' not in type_pkg:
            errors.append(f"types oh-package.json5 must declare name {lib_name}")

    entry_pkg = read_text(module / "oh-package.json5")
    if lib_name and lib_name not in entry_pkg:
        errors.append(f"entry oh-package.json5 must depend on {lib_name}")
    if package_name and f"file:src/main/cangjie/types/lib{package_name}" not in entry_pkg:
        errors.append("entry oh-package.json5 .so dependency path does not match package name")
    if re.search(
        r'["\']@cangjie/cjhybridcomponent["\']\s*:\s*["\']1\.0\.0["\']',
        entry_pkg,
    ):
        warnings.append(
            "@cangjie/cjhybridcomponent 1.0.0 is an older upstream package; use the template-tested "
            "1.1.1 release to reduce package-owned migration warnings"
        )

    module_json = load_json5ish(module / "src/main/module.json5")
    if isinstance(module_json, dict):
        mod = module_json.get("module", {})
        if mod.get("srcEntry"):
            errors.append("hybrid app module should use ArkTS Ability, not Cangjie module srcEntry")
        if "pages" not in mod:
            errors.append("module.json5 should contain pages: \"$profile:main_pages\"")
        abilities = mod.get("abilities") or []
        if abilities:
            src_entry = str(abilities[0].get("srcEntry", ""))
            if not src_entry.endswith(".ets"):
                errors.append("EntryAbility srcEntry should point to an ArkTS .ets file")
    else:
        warnings.append("could not parse module.json5")

    pages = parse_main_pages(module / "src/main/resources/base/profile/main_pages.json")
    if "pages/Index" not in pages:
        errors.append("main_pages.json must register pages/Index")

    index_ets = read_text(module / "src/main/ets/pages/Index.ets")
    if lib_name and f"from '{lib_name}'" not in index_ets and f'from "{lib_name}"' not in index_ets:
        errors.append(f"ArkTS page should import Cangjie exports from {lib_name}")

    build_profile = read_text(module / "build-profile.json5")
    if '"path": "./cjpm.toml"' not in build_profile:
        errors.append("entry/build-profile.json5 cangjieOptions.path should be ./cjpm.toml")
    if "x86_64" not in build_profile:
        warnings.append("entry/build-profile.json5 lacks x86_64 abi filter for emulator coverage")
    if "arm64-v8a" not in build_profile:
        warnings.append("entry/build-profile.json5 lacks arm64-v8a abi filter for device coverage")

    hybrid_components = collect_hybrid_components(module)
    if hybrid_components:
        if '"@cangjie/cjhybridcomponent"' not in entry_pkg:
            errors.append("CJHybridComponent is used but entry oh-package.json5 lacks @cangjie/cjhybridcomponent")
        for page, library, component in hybrid_components:
            if package_name and library != package_name:
                errors.append(f"{page}: CJHybridComponent library should be {package_name}, got {library}")
            if not cangjie_component_exists(module, component):
                errors.append(f"{page}: component {component} is not defined as @HybridComponentEntry @Component in Cangjie source")
            page_ref = "pages/" + page.stem
            if page_ref not in pages and page.name != "Index.ets":
                errors.append(f"{page}: wrapper page {page_ref} is not registered in main_pages.json")

    pages_dir = module / "src/main/ets/pages"
    for page in sorted(pages_dir.rglob("*.ets")) if pages_dir.exists() else []:
        text = read_text(page)
        imports_global_router = bool(
            re.search(
                r"\bimport\s+(?:router|\{[^}]*\brouter\b[^}]*\})\s+from\s+"
                r"[\"'](?:@ohos\.router|@kit\.ArkUI)[\"']",
                text,
                re.DOTALL,
            )
        )
        if imports_global_router and re.search(
            r"\brouter\s*\.\s*(?:pushUrl|replaceUrl|back|clear)\s*\(", text
        ):
            warnings.append(
                f"{page}: global router API is deprecated since API 18; use "
                "this.getUIContext().getRouter() inside an ArkUI component"
            )

    return errors, warnings


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Validate a Cangjie-ArkTS hybrid HarmonyOS project.")
    parser.add_argument("--project-root", default=".", help="project root")
    parser.add_argument("--config", action="append", default=None, help="Path to cangjie.skills.toml.")
    parser.add_argument("--module", default=None, help="module name")
    args = parser.parse_args(argv)

    project = Path(args.project_root).expanduser().resolve()
    cfg = load_harmony_config(project_root=project, config_paths=args.config)
    runtime_cfg = getattr(cfg, "runtime", None)
    detected = detect_project_runtime(project, module=args.module or (getattr(runtime_cfg, "module", None) if runtime_cfg else None))
    args.module = first_value(args.module, getattr(runtime_cfg, "module", None) if runtime_cfg else None, getattr(detected, "module", None), "entry")
    errors, warnings = validate(project, args.module)

    print("# Hybrid Project Check")
    print(f"project: {project}")
    print(f"module: {args.module}")
    if warnings:
        print("\nWarnings:")
        for item in warnings:
            print(f"- {item}")
    if errors:
        print("\nErrors:")
        for item in errors:
            print(f"- {item}")
        return 1
    print("\nOK: hybrid Cangjie-ArkTS wiring looks consistent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
