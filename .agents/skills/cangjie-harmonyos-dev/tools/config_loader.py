#!/usr/bin/env python3
from __future__ import annotations

import os
import re
import tomllib
from dataclasses import dataclass, field, fields
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


CONFIG_FILENAME = "cangjie.skills.toml"
CONFIG_ENV = "CANGJIE_SKILLS_CONFIG"
USER_CONFIG = Path.home() / ".cangjie" / CONFIG_FILENAME
PROJECT_CONFIG = Path(CONFIG_FILENAME)
DEFAULT_OHPM_REGISTRY = "https://ohpm.openharmony.cn/ohpm/"
DEFAULT_DEVICE_TARGET = "127.0.0.1:5555"
DEFAULT_EMBEDDING_BASE_URL = (
    "https://dashscope.aliyuncs.com/api/v1/services/embeddings/text-embedding/text-embedding"
)
DEFAULT_EMBEDDING_DIMENSIONS = 256
EMBEDDING_MODES = ("off", "search", "index", "all")


@dataclass(slots=True)
class ToolchainConfig:
    deveco_home: str | None = None
    cangjie_sdk: str | None = None
    hdc: str | None = None
    ohpm_registry: str = DEFAULT_OHPM_REGISTRY
    verify_tls: bool = True


@dataclass(slots=True)
class DeviceConfig:
    target: str = DEFAULT_DEVICE_TARGET


@dataclass(slots=True)
class RuntimeConfig:
    bundle: str | None = None
    ability: str | None = None
    module: str | None = None
    hap: str | None = None


@dataclass(slots=True)
class ScaffoldConfig:
    app_name: str | None = None
    bundle_name: str | None = None
    module_name: str | None = None


@dataclass(slots=True)
class KnowledgeEmbeddingConfig:
    mode: str = "search"
    api_format: str = "dashscope"
    model: str = "text-embedding-v4"
    base_url: str = DEFAULT_EMBEDDING_BASE_URL
    api_key_env: str = "DASHSCOPE_API_KEY"
    dimensions: int = DEFAULT_EMBEDDING_DIMENSIONS
    min_similarity: float = 0.40
    batch_size: int = 10
    timeout_seconds: float = 60.0
    max_retries: int = 2


@dataclass(slots=True)
class KnowledgeConfig:
    version: str = "default"
    embedding: KnowledgeEmbeddingConfig = field(default_factory=KnowledgeEmbeddingConfig)


@dataclass(slots=True)
class HarmonyConfig:
    toolchain: ToolchainConfig = field(default_factory=ToolchainConfig)
    device: DeviceConfig = field(default_factory=DeviceConfig)
    runtime: RuntimeConfig = field(default_factory=RuntimeConfig)
    scaffold: ScaffoldConfig = field(default_factory=ScaffoldConfig)
    knowledge: KnowledgeConfig = field(default_factory=KnowledgeConfig)
    loaded_files: list[Path] = field(default_factory=list)


@dataclass(slots=True)
class DetectedRuntime:
    bundle: str | None = None
    ability: str | None = None
    module: str | None = None
    hap: str | None = None
    warnings: list[str] = field(default_factory=list)


def supported_config_keys() -> tuple[str, ...]:
    """Return the public TOML keys in documentation order."""
    return (
        *(f"toolchain.{item.name}" for item in fields(ToolchainConfig)),
        *(f"device.{item.name}" for item in fields(DeviceConfig)),
        *(f"runtime.{item.name}" for item in fields(RuntimeConfig)),
        *(f"scaffold.{item.name}" for item in fields(ScaffoldConfig)),
        "knowledge.version",
        *(f"knowledge.embedding.{item.name}" for item in fields(KnowledgeEmbeddingConfig)),
    )


def find_project_root(start: str | Path | None = None) -> Path:
    cur = Path(start or Path.cwd()).expanduser().resolve()
    if cur.is_file():
        cur = cur.parent
    for candidate in (cur, *cur.parents):
        if (
            (candidate / CONFIG_FILENAME).exists()
            or (candidate / "build-profile.json5").exists()
            or (candidate / "AppScope").exists()
        ):
            return candidate
    return cur


def default_config_paths(project_root: str | Path | None = None) -> list[Path]:
    paths = [USER_CONFIG]
    project = find_project_root(project_root)
    paths.append(project / PROJECT_CONFIG)
    env_path = os.getenv(CONFIG_ENV)
    if env_path:
        paths.append(Path(env_path).expanduser())
    return paths


def _fail(path: Path, key: str, message: str) -> None:
    raise ValueError(f"invalid configuration in {path}: {key} {message}")


def _table(data: dict[str, Any], name: str, path: Path) -> dict[str, Any]:
    value = data.get(name, {})
    if not isinstance(value, dict):
        _fail(path, name, "must be a TOML table")
    return value


def _reject_unknown(data: dict[str, Any], allowed: set[str], path: Path, prefix: str = "") -> None:
    unknown = sorted(set(data) - allowed)
    if unknown:
        names = ", ".join(f"{prefix}{key}" for key in unknown)
        raise ValueError(f"unknown configuration key(s) in {path}: {names}")


def _assign(obj: Any, data: dict[str, Any], path: Path, prefix: str) -> None:
    allowed = {item.name for item in fields(obj)}
    _reject_unknown(data, allowed, path, prefix)
    for key, value in data.items():
        setattr(obj, key, value)


def _load_toml(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8-sig")
    data = tomllib.loads(text)
    return data if isinstance(data, dict) else {}


def _plaintext_secret_fields(data: dict[str, Any], prefix: str = "") -> list[str]:
    found: list[str] = []
    for key, value in data.items():
        dotted = f"{prefix}.{key}" if prefix else key
        if key == "api_key":
            found.append(dotted)
        if isinstance(value, dict):
            found.extend(_plaintext_secret_fields(value, dotted))
    return found


def _reject_plaintext_secrets(data: dict[str, Any], path: Path) -> None:
    forbidden = _plaintext_secret_fields(data)
    if forbidden:
        raise ValueError(
            f"plaintext API-key fields are not allowed in {path}: {', '.join(forbidden)}; "
            "configure only api_key_env and set that environment variable"
        )


def _require_type(path: Path, key: str, value: Any, expected: type | tuple[type, ...]) -> None:
    numeric = expected in (int, float) or (
        isinstance(expected, tuple) and any(item in (int, float) for item in expected)
    )
    if numeric and isinstance(value, bool):
        _fail(path, key, "must be a number")
    if not isinstance(value, expected):
        label = "number" if expected == (int, float) else getattr(expected, "__name__", "valid value")
        _fail(path, key, f"must be {label}")


def _validate_optional_text(path: Path, key: str, value: str | None) -> None:
    if value is None:
        return
    _require_type(path, key, value, str)
    if not value.strip():
        _fail(path, key, "must not be blank; omit it to use automatic detection")


def _validate_url(path: Path, key: str, value: str) -> None:
    _require_type(path, key, value, str)
    parsed = urlparse(value)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        _fail(path, key, "must be an absolute http(s) URL")


def _validate_non_negative(path: Path, key: str, value: int) -> None:
    _require_type(path, key, value, int)
    if value < 0:
        _fail(path, key, "must be >= 0")


def _validate_positive(path: Path, key: str, value: int | float) -> None:
    _require_type(path, key, value, (int, float))
    if value <= 0:
        _fail(path, key, "must be > 0")


def _validate_positive_integer(path: Path, key: str, value: int) -> None:
    _require_type(path, key, value, int)
    if value <= 0:
        _fail(path, key, "must be > 0")


def _validate(cfg: HarmonyConfig, path: Path) -> None:
    for key in ("deveco_home", "cangjie_sdk", "hdc"):
        _validate_optional_text(path, f"toolchain.{key}", getattr(cfg.toolchain, key))
    _validate_url(path, "toolchain.ohpm_registry", cfg.toolchain.ohpm_registry)
    _require_type(path, "toolchain.verify_tls", cfg.toolchain.verify_tls, bool)
    _validate_optional_text(path, "device.target", cfg.device.target)

    for key in ("bundle", "ability", "module", "hap"):
        _validate_optional_text(path, f"runtime.{key}", getattr(cfg.runtime, key))
    for key in ("app_name", "bundle_name", "module_name"):
        _validate_optional_text(path, f"scaffold.{key}", getattr(cfg.scaffold, key))

    _validate_optional_text(path, "knowledge.version", cfg.knowledge.version)
    embedding = cfg.knowledge.embedding
    if embedding.mode not in EMBEDDING_MODES:
        _fail(path, "knowledge.embedding.mode", f"must be one of: {', '.join(EMBEDDING_MODES)}")
    for key in ("model", "api_key_env"):
        _validate_optional_text(path, f"knowledge.embedding.{key}", getattr(embedding, key))
    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", embedding.api_key_env):
        _fail(path, "knowledge.embedding.api_key_env", "must be an environment-variable name")
    _validate_url(path, "knowledge.embedding.base_url", embedding.base_url)
    _validate_positive(path, "knowledge.embedding.timeout_seconds", embedding.timeout_seconds)
    _validate_non_negative(path, "knowledge.embedding.max_retries", embedding.max_retries)
    _validate_optional_text(path, "knowledge.embedding.api_format", cfg.knowledge.embedding.api_format)
    if cfg.knowledge.embedding.api_format not in {"dashscope", "openai"}:
        _fail(path, "knowledge.embedding.api_format", "must be one of: dashscope, openai")
    if cfg.knowledge.embedding.dimensions is not None:
        _validate_positive_integer(path, "knowledge.embedding.dimensions", cfg.knowledge.embedding.dimensions)
    _require_type(path, "knowledge.embedding.min_similarity", embedding.min_similarity, (int, float))
    if not 0 <= embedding.min_similarity <= 1:
        _fail(path, "knowledge.embedding.min_similarity", "must be between 0 and 1")
    _validate_positive_integer(path, "knowledge.embedding.batch_size", cfg.knowledge.embedding.batch_size)


def _apply(data: dict[str, Any], cfg: HarmonyConfig, path: Path) -> None:
    if "project" in data:
        raise ValueError(
            f"unsupported legacy section in {path}: project; use [scaffold] for "
            "app_name, bundle_name, and module_name; pass package, vendor, SDK, or model overrides to the generator CLI"
        )
    _reject_unknown(data, {"toolchain", "device", "runtime", "scaffold", "knowledge"}, path)
    _assign(cfg.toolchain, _table(data, "toolchain", path), path, "toolchain.")
    _assign(cfg.device, _table(data, "device", path), path, "device.")
    _assign(cfg.runtime, _table(data, "runtime", path), path, "runtime.")
    _assign(cfg.scaffold, _table(data, "scaffold", path), path, "scaffold.")

    knowledge = _table(data, "knowledge", path)
    _reject_unknown(knowledge, {"version", "embedding"}, path, "knowledge.")
    if "version" in knowledge:
        cfg.knowledge.version = knowledge["version"]
    _assign(cfg.knowledge.embedding, _table(knowledge, "embedding", path), path, "knowledge.embedding.")


def load_harmony_config(
    *,
    project_root: str | Path | None = None,
    config_paths: list[str | Path] | None = None,
) -> HarmonyConfig:
    cfg = HarmonyConfig()
    explicit_paths = config_paths is not None
    paths = [Path(p).expanduser() for p in config_paths] if explicit_paths else default_config_paths(project_root)
    environment_path = Path(os.environ[CONFIG_ENV]).expanduser() if not explicit_paths and os.getenv(CONFIG_ENV) else None
    for path in paths:
        if not path.exists():
            if explicit_paths or path == environment_path:
                raise FileNotFoundError(f"configuration file does not exist: {path}")
            continue
        data = _load_toml(path)
        _reject_plaintext_secrets(data, path)
        _apply(data, cfg, path)
        _validate(cfg, path)
        cfg.loaded_files.append(path.resolve())
    return cfg


def first_value(*values: Any) -> Any:
    for value in values:
        if value is not None and value != "":
            return value
    return None


def path_value(value: str | None) -> Path | None:
    return Path(value).expanduser() if value else None


def strip_json5_comments(text: str) -> str:
    text = re.sub(r"//.*", "", text)
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    return text


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def _string_value(text: str, key: str) -> str | None:
    match = re.search(rf'["\']{re.escape(key)}["\']\s*:\s*["\']([^"\']+)["\']', text)
    return match.group(1) if match else None


def detect_bundle(project_root: str | Path) -> str | None:
    app_json = Path(project_root) / "AppScope" / "app.json5"
    return _string_value(strip_json5_comments(_read(app_json)), "bundleName")


def detect_modules(project_root: str | Path) -> list[str]:
    project = Path(project_root)
    profile = strip_json5_comments(_read(project / "build-profile.json5"))
    modules_block = re.search(r'["\']modules["\']\s*:\s*\[(?P<body>.*?)\]\s*,', profile, re.S)
    if modules_block:
        names = re.findall(r'["\']name["\']\s*:\s*["\']([^"\']+)["\']', modules_block.group("body"))
        if names:
            return list(dict.fromkeys(names))
    found = [
        path.parent.parent.parent.name
        for path in sorted(project.glob("*/src/main/module.json5"))
        if path.is_file()
    ]
    return list(dict.fromkeys(found))


def detect_ability(project_root: str | Path, module: str | None = None) -> str | None:
    project = Path(project_root)
    module_names = [module] if module else detect_modules(project)
    for name in [item for item in module_names if item]:
        text = strip_json5_comments(_read(project / name / "src/main/module.json5"))
        if not text:
            continue
        abilities = re.search(r'["\']abilities["\']\s*:\s*\[(?P<body>.*?)\]', text, re.S)
        if abilities:
            ability = _string_value(abilities.group("body"), "name")
            if ability:
                return ability
        ability = _string_value(text, "name")
        if ability and "Ability" in ability:
            return ability
    return None


def detect_hap(project_root: str | Path, module: str | None = None) -> tuple[str | None, list[str]]:
    project = Path(project_root)
    module_names = [module] if module else detect_modules(project)
    candidates: list[Path] = []
    for name in [item for item in module_names if item]:
        candidates.extend(sorted((project / name / "build").glob("**/*.hap")))
    if not candidates:
        candidates = sorted(project.glob("*/build/**/*.hap"))
    candidates = [path for path in candidates if path.is_file()]
    if not candidates:
        return None, []
    candidates.sort(key=lambda path: path.stat().st_mtime, reverse=True)
    rel = str(candidates[0].relative_to(project))
    warnings: list[str] = []
    if len(candidates) > 1:
        warnings.append(
            "multiple HAP outputs detected; using newest. Pass --hap or set [runtime].hap to override."
        )
    return rel.replace("\\", "/"), warnings


def detect_project_runtime(
    project_root: str | Path | None = None,
    *,
    module: str | None = None,
) -> DetectedRuntime:
    project = find_project_root(project_root)
    modules = detect_modules(project)
    warnings: list[str] = []

    selected_module = module
    if not selected_module:
        if len(modules) == 1:
            selected_module = modules[0]
        elif "entry" in modules:
            selected_module = "entry"
            warnings.append("multiple modules detected; using entry. Pass --module or set [runtime].module to override.")
        elif modules:
            selected_module = modules[0]
            warnings.append(
                f"multiple modules detected; using {selected_module}. Pass --module or set [runtime].module to override."
            )

    hap, hap_warnings = detect_hap(project, selected_module)
    warnings.extend(hap_warnings)
    return DetectedRuntime(
        bundle=detect_bundle(project),
        ability=detect_ability(project, selected_module),
        module=selected_module,
        hap=hap,
        warnings=warnings,
    )
