from __future__ import annotations

import os
import sys
from dataclasses import dataclass, field
from pathlib import Path


EMBEDDING_OFF = "off"
EMBEDDING_INDEX = "index"
EMBEDDING_SEARCH = "search"
EMBEDDING_ALL = "all"
EMBEDDING_MODES = (EMBEDDING_OFF, EMBEDDING_SEARCH, EMBEDDING_INDEX, EMBEDDING_ALL)
SKILL_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DATA_ROOT = SKILL_ROOT / "data"
DEFAULT_DOCS_ROOT = DEFAULT_DATA_ROOT / "docs"
DEFAULT_INDEX_DIR = DEFAULT_DATA_ROOT
DEFAULT_CACHE_DIR = Path.home() / ".cangjie" / "cache" / "cangjie-harmonyos-knowledge"


@dataclass(slots=True)
class EmbeddingConfig:
    api_format: str = "dashscope"
    base_url: str = "https://dashscope.aliyuncs.com/api/v1/services/embeddings/text-embedding/text-embedding"
    api_key_env: str = "DASHSCOPE_API_KEY"
    api_key: str | None = None
    model: str = "text-embedding-v4"
    dimensions: int = 256
    min_similarity: float = 0.40
    timeout: float = 60.0
    max_retries: int = 2
    batch_size: int = 10


@dataclass(slots=True)
class AppConfig:
    docs_root: str = str(DEFAULT_DOCS_ROOT)
    index_dir: str = str(DEFAULT_INDEX_DIR)
    docs_version: str = "default"
    embedding_mode: str = EMBEDDING_SEARCH
    embedding: EmbeddingConfig = field(default_factory=EmbeddingConfig)

    @property
    def index_path(self) -> Path:
        return Path(self.index_dir) / "index.sqlite"

    @property
    def vector_cache_path(self) -> Path:
        index_dir = Path(self.index_dir)
        if index_dir.resolve() == DEFAULT_INDEX_DIR.resolve():
            return DEFAULT_CACHE_DIR / "vector_cache.sqlite"
        return index_dir / "vector_cache.sqlite"

    @property
    def index_embeddings(self) -> bool:
        return self.embedding_mode in (EMBEDDING_INDEX, EMBEDDING_ALL)

    @property
    def search_embeddings(self) -> bool:
        return self.embedding_mode in (EMBEDDING_SEARCH, EMBEDDING_ALL)


def _load_unified_config(path: str | Path | None = None):
    skills_dir = SKILL_ROOT.parent
    helper_dir = skills_dir / "cangjie-harmonyos-dev" / "tools"
    if helper_dir.exists() and str(helper_dir) not in sys.path:
        sys.path.insert(0, str(helper_dir))
    try:
        from config_loader import load_harmony_config
    except ImportError:
        if path:
            raise RuntimeError("cangjie.skills.toml loader is unavailable")
        return None
    paths = [Path(path).expanduser()] if path else None
    return load_harmony_config(project_root=Path.cwd(), config_paths=paths)


def _apply_unified_config(cfg: AppConfig, unified: object | None) -> None:
    knowledge = getattr(unified, "knowledge", None)
    if not knowledge:
        return
    cfg.docs_version = knowledge.version
    embedding = knowledge.embedding
    apply_embedding_mode(cfg, embedding.mode)
    for name in (
        "model",
        "base_url",
        "api_key_env",
        "api_format",
        "dimensions",
        "min_similarity",
        "batch_size",
        "max_retries",
    ):
        setattr(cfg.embedding, name, getattr(embedding, name))
    cfg.embedding.timeout = embedding.timeout_seconds


def load_config(path: str | Path | None = None) -> AppConfig:
    cfg = AppConfig()
    _apply_unified_config(cfg, _load_unified_config(path))
    cfg.embedding.api_key = os.getenv(cfg.embedding.api_key_env) or cfg.embedding.api_key
    return cfg


def apply_embedding_mode(cfg: AppConfig, mode: str | None) -> AppConfig:
    if not mode:
        return cfg
    if mode not in EMBEDDING_MODES:
        raise ValueError(f"Unsupported embedding mode: {mode}")
    cfg.embedding_mode = mode
    return cfg


def apply_overrides(
    cfg: AppConfig,
    *,
    docs_root: str | None = None,
    index_dir: str | None = None,
    docs_version: str | None = None,
    embedding_mode: str | None = None,
    embedding_api_format: str | None = None,
    embedding_model: str | None = None,
    embedding_base_url: str | None = None,
    embedding_api_key_env: str | None = None,
    embedding_batch_size: int | None = None,
    embedding_dimensions: int | None = None,
) -> AppConfig:
    if docs_root:
        cfg.docs_root = docs_root
    if index_dir:
        cfg.index_dir = index_dir
    if docs_version:
        cfg.docs_version = docs_version
    apply_embedding_mode(cfg, embedding_mode)
    if embedding_api_format:
        cfg.embedding.api_format = embedding_api_format
    if embedding_model:
        cfg.embedding.model = embedding_model
    if embedding_base_url:
        cfg.embedding.base_url = embedding_base_url
    if embedding_api_key_env:
        cfg.embedding.api_key_env = embedding_api_key_env
        cfg.embedding.api_key = os.getenv(embedding_api_key_env)
    if embedding_batch_size is not None:
        if embedding_batch_size <= 0:
            raise ValueError("embedding batch size must be > 0")
        cfg.embedding.batch_size = embedding_batch_size
    if embedding_dimensions is not None:
        if embedding_dimensions <= 0:
            raise ValueError("embedding dimensions must be > 0")
        cfg.embedding.dimensions = embedding_dimensions
    return cfg
