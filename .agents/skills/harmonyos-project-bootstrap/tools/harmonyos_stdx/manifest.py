"""Atomic, idempotent HarmonyOS stdx target updates for cjpm.toml."""

from __future__ import annotations

import json
import os
import re
import shutil
import tempfile
import tomllib
from pathlib import Path

from .errors import SetupError
from .policy import PLATFORM_TO_TARGET


OHOS_TARGETS = frozenset(PLATFORM_TO_TARGET.values())


def _path_options(parsed: dict[str, object], target: str) -> list[str]:
    targets = parsed.get("target", {})
    if not isinstance(targets, dict):
        raise SetupError("target must be a TOML table")
    target_table = targets.get(target, {})
    if not isinstance(target_table, dict):
        raise SetupError(f"target.{target} must be a TOML table")
    dependencies = target_table.get("bin-dependencies", {})
    if not isinstance(dependencies, dict):
        raise SetupError(f"target.{target}.bin-dependencies must be a TOML table")
    paths = dependencies.get("path-option", [])
    if paths is None:
        return []
    if not isinstance(paths, list) or not all(isinstance(item, str) for item in paths):
        raise SetupError(f"target.{target}.bin-dependencies.path-option must be an array of strings")
    return paths


def _validate_manifest(manifest: Path) -> None:
    try:
        parsed = tomllib.loads(manifest.read_text(encoding="utf-8-sig"))
    except tomllib.TOMLDecodeError as exc:
        raise SetupError(f"cannot configure invalid cjpm.toml: {exc}") from exc
    for target in OHOS_TARGETS:
        _path_options(parsed, target)


def resolve_project(value: Path, no_configure: bool) -> tuple[Path, Path | None]:
    path = value.expanduser().resolve()
    if path.is_file():
        if path.name != "cjpm.toml":
            raise SetupError(f"--project file must be cjpm.toml: {path}")
        if not no_configure:
            _validate_manifest(path)
        return path.parent, path
    if not path.is_dir():
        raise SetupError(f"project directory does not exist: {path}")
    manifest = path / "cjpm.toml"
    if not no_configure and not manifest.is_file():
        raise SetupError(f"cjpm.toml not found under project: {path}")
    if manifest.is_file() and not no_configure:
        _validate_manifest(manifest)
    return path, manifest if manifest.is_file() else None


def _path_key(value: str) -> str:
    path = Path(value).expanduser()
    try:
        normalized = str(path.resolve())
    except OSError:
        normalized = str(path)
    return os.path.normcase(os.path.normpath(normalized))


def _render_paths(values: list[str], indent: str = "    ") -> str:
    encoded = ", ".join(json.dumps(value, ensure_ascii=False) for value in values)
    return f"{indent}path-option = [{encoded}]"


def _is_managed_stdx_path(value: str) -> bool:
    path = Path(value).expanduser()
    return (
        len(path.parts) >= 3
        and path.name == "stdx"
        and path.parent.name in {"dynamic", "static"}
        and re.fullmatch(r"cangjie-stdx-ohos-(?:x64|aarch64)-.+", path.parent.parent.name) is not None
    )


def _merge_target(text: str, target: str, binary_root: Path) -> str:
    if target not in OHOS_TARGETS:
        raise SetupError(f"refusing to configure non-HarmonyOS target: {target}")
    parsed = tomllib.loads(text)
    existing = _path_options(parsed, target)
    desired = str(binary_root.resolve())
    values = [value for value in existing if not _is_managed_stdx_path(value)]
    if _path_key(desired) not in {_path_key(value) for value in values}:
        values.append(desired)

    lines = text.splitlines()
    section = re.compile(rf"^\s*\[target\.{re.escape(target)}\.bin-dependencies\]\s*(?:#.*)?$")
    table = re.compile(r"^\s*\[")
    start = next((index for index, line in enumerate(lines) if section.match(line)), None)
    if start is None:
        if lines and lines[-1].strip():
            lines.append("")
        lines.extend([f"[target.{target}.bin-dependencies]", _render_paths(values)])
    else:
        end = next((index for index in range(start + 1, len(lines)) if table.match(lines[index])), len(lines))
        assignment = next(
            (index for index in range(start + 1, end) if re.match(r"^\s*path-option\s*=", lines[index])),
            None,
        )
        if assignment is None:
            lines.insert(end, _render_paths(values))
        else:
            indent = re.match(r"^(\s*)", lines[assignment]).group(1)
            assignment_end = assignment + 1
            balance = lines[assignment].count("[") - lines[assignment].count("]")
            while balance > 0 and assignment_end < end:
                balance += lines[assignment_end].count("[") - lines[assignment_end].count("]")
                assignment_end += 1
            lines[assignment:assignment_end] = [_render_paths(values, indent)]
    return "\n".join(lines).rstrip() + "\n"


def merge_manifest_text(text: str, binary_roots: dict[str, Path]) -> tuple[str, bool]:
    try:
        tomllib.loads(text)
    except tomllib.TOMLDecodeError as exc:
        raise SetupError(f"cannot configure invalid cjpm.toml: {exc}") from exc
    updated = text.rstrip() + "\n"
    try:
        for target, binary_root in binary_roots.items():
            updated = _merge_target(updated, target, binary_root)
        tomllib.loads(updated)
    except tomllib.TOMLDecodeError as exc:
        raise SetupError(f"internal error: generated invalid cjpm.toml: {exc}") from exc
    return updated, updated != text.rstrip() + "\n"


def configure_manifest(manifest: Path, binary_roots: dict[str, Path], dry_run: bool = False) -> bool:
    original = manifest.read_text(encoding="utf-8-sig")
    updated, changed = merge_manifest_text(original, binary_roots)
    if not changed or dry_run:
        return changed
    backup = manifest.with_name("cjpm.toml.stdx.bak")
    if not backup.exists():
        shutil.copy2(manifest, backup)
    descriptor, temporary_name = tempfile.mkstemp(prefix=".cjpm.toml.", dir=manifest.parent)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as stream:
            stream.write(updated)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, manifest)
    finally:
        temporary.unlink(missing_ok=True)
    return True
