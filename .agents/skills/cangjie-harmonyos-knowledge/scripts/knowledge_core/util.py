from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import unicodedata
from pathlib import Path
from typing import Any


CJK_RE = re.compile(r"[\u3400-\u9fff]")


def configure_stdio() -> None:
    """Prefer UTF-8 console IO without failing on older/redirected streams."""
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass


def read_text_lossless(path: Path) -> tuple[str, str]:
    data = path.read_bytes()
    for enc in ("utf-8-sig", "utf-8", "gb18030"):
        try:
            return data.decode(enc), enc
        except UnicodeDecodeError:
            continue
    return data.decode("utf-8", errors="replace"), "utf-8-replace"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def norm_text(value: str) -> str:
    value = unicodedata.normalize("NFKC", value or "")
    return value.strip()


def normalize_symbol(value: str) -> str:
    value = norm_text(value)
    return re.sub(r"[^0-9a-zA-Z_\u3400-\u9fff]+", "", value).lower()


def slugify_heading(text: str) -> str:
    text = norm_text(text)
    text = text.lower()
    text = text.replace("\\", "")
    text = re.sub(r"</?(?:br|sub|sup|kbd|code|span)\b[^>]*>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"[`*~]", "", text)
    text = re.sub(r"[^0-9a-z_\u3400-\u9fff\s-]", "", text)
    text = re.sub(r"\s", "-", text).strip("-")
    return text or "section"


def make_anchor(title: str, existing: dict[str, int]) -> str:
    base = slugify_heading(title)
    count = existing.get(base, 0)
    existing[base] = count + 1
    if count:
        return f"{base}-{count}"
    return base


def relative_posix(path: Path, root: Path) -> str:
    return path.resolve().relative_to(root.resolve()).as_posix()


def json_dumps(data: Any) -> str:
    return json.dumps(data, ensure_ascii=False, separators=(",", ":"))


def json_loads(value: str | None, default: Any) -> Any:
    if not value:
        return default
    try:
        return json.loads(value)
    except Exception:
        return default


def has_cjk(text: str) -> bool:
    return bool(CJK_RE.search(text or ""))


def safe_int(value: Any, default: int) -> int:
    try:
        return int(value)
    except Exception:
        return default


def env_bool(name: str, default: bool = False) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}
