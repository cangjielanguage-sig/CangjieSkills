from __future__ import annotations

import datetime as dt
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .util import sha256_text
from .vector_codec import pack_vector, unpack_vector


CACHE_SCHEMA = """
pragma journal_mode=WAL;
pragma synchronous=NORMAL;

create table if not exists vector_cache (
  cache_key text primary key,
  provider text not null,
  model text not null,
  source_hash text not null,
  dimensions integer not null,
  vector_blob blob not null,
  created_at text not null
);
"""


@dataclass(slots=True)
class CachedVector:
    dimensions: int
    vector: list[float]


class VectorCache:
    def __init__(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        self.path = path
        self.con = sqlite3.connect(path)
        self.con.row_factory = sqlite3.Row
        self.con.executescript(CACHE_SCHEMA)
        self.con.commit()

    def close(self) -> None:
        self.con.close()

    def commit(self) -> None:
        self.con.commit()

    @staticmethod
    def key(
        *,
        provider: str,
        model: str,
        text: str,
        endpoint: str = "",
        requested_dimensions: int | None = None,
    ) -> str:
        dimension_key = str(requested_dimensions) if requested_dimensions else "provider-default"
        return sha256_text(
            "|".join(["vector-v2", provider, endpoint.rstrip("/"), model, dimension_key, sha256_text(text)])
        )

    def get(
        self,
        *,
        provider: str,
        model: str,
        text: str,
        endpoint: str = "",
        requested_dimensions: int | None = None,
    ) -> CachedVector | None:
        row = self.con.execute(
            "select dimensions, vector_blob from vector_cache where cache_key = ?",
            (
                self.key(
                    provider=provider,
                    model=model,
                    text=text,
                    endpoint=endpoint,
                    requested_dimensions=requested_dimensions,
                ),
            ),
        ).fetchone()
        if not row:
            return None
        vector = unpack_vector(row["vector_blob"])
        return CachedVector(dimensions=int(row["dimensions"]), vector=vector)

    def put(
        self,
        *,
        provider: str,
        model: str,
        text: str,
        vector: list[float],
        endpoint: str = "",
        requested_dimensions: int | None = None,
        commit: bool = True,
    ) -> None:
        self.con.execute(
            """
            insert or replace into vector_cache(
              cache_key, provider, model, source_hash, dimensions, vector_blob, created_at
            ) values (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                self.key(
                    provider=provider,
                    model=model,
                    text=text,
                    endpoint=endpoint,
                    requested_dimensions=requested_dimensions,
                ),
                provider,
                model,
                sha256_text(text),
                len(vector),
                pack_vector(vector),
                dt.datetime.now(dt.UTC).isoformat(),
            ),
        )
        if commit:
            self.con.commit()

    def stats(self) -> dict[str, Any]:
        count = self.con.execute("select count(*) c from vector_cache").fetchone()["c"]
        return {"vectors": int(count)}
