from __future__ import annotations

import json
import math
import time
import urllib.error
import urllib.request
from typing import Any

from .config import AppConfig


class EmbeddingUnavailable(RuntimeError):
    """Raised when the optional embedding provider cannot be used."""


class HTTPJsonClient:
    def __init__(self, *, timeout: float, max_retries: int) -> None:
        self.timeout = timeout
        self.max_retries = max_retries

    def post(self, url: str, headers: dict[str, str], payload: dict[str, Any]) -> dict[str, Any]:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        request = urllib.request.Request(url, data=body, method="POST")
        for key, value in headers.items():
            request.add_header(key, value)
        request.add_header("Content-Type", "application/json")

        last_error: Exception | None = None
        for attempt in range(self.max_retries + 1):
            try:
                with urllib.request.urlopen(request, timeout=self.timeout) as response:
                    return json.loads(response.read().decode("utf-8"))
            except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
                last_error = exc
                if isinstance(exc, urllib.error.HTTPError) and 400 <= exc.code < 500 and exc.code != 429:
                    break
                if attempt < self.max_retries:
                    time.sleep(min(2.0 * (attempt + 1), 6.0))
        raise EmbeddingUnavailable(f"embedding request failed: {type(last_error).__name__}")


class EmbeddingService:
    def __init__(self, cfg: AppConfig) -> None:
        self.cfg = cfg.embedding
        self.http = HTTPJsonClient(timeout=self.cfg.timeout, max_retries=self.cfg.max_retries)
        self.request_count = 0
        self.input_tokens = 0

    @property
    def available(self) -> bool:
        return bool(self.cfg.api_key and self.cfg.model and self.cfg.base_url)

    def embed_texts(self, texts: list[str]) -> list[list[float]]:
        if not self.available:
            raise EmbeddingUnavailable("embedding provider is not configured")
        if not texts:
            return []
        if self.cfg.api_format == "openai":
            vectors = self._embed_openai(texts)
        else:
            vectors = self._embed_dashscope(texts)
        return self._validate_vectors(texts, vectors)

    def embed_query(self, text: str) -> list[float]:
        vectors = self.embed_texts([text])
        return vectors[0] if vectors else []

    def _embed_openai(self, texts: list[str]) -> list[list[float]]:
        payload: dict[str, Any] = {"model": self.cfg.model, "input": texts}
        if self.cfg.dimensions:
            payload["dimensions"] = self.cfg.dimensions
        data = self.http.post(
            self.cfg.base_url.rstrip("/") + "/embeddings",
            {"Authorization": f"Bearer {self.cfg.api_key}"},
            payload,
        )
        self._record_usage(data)
        try:
            rows = sorted(data["data"], key=lambda row: row["index"])
            if [row["index"] for row in rows] != list(range(len(texts))):
                raise ValueError("invalid indexes")
            return [row["embedding"] for row in rows]
        except Exception as exc:
            raise EmbeddingUnavailable(f"unexpected OpenAI embedding response: {type(exc).__name__}") from exc

    def _embed_dashscope(self, texts: list[str]) -> list[list[float]]:
        payload: dict[str, Any] = {"model": self.cfg.model, "input": {"texts": texts}}
        if self.cfg.dimensions:
            payload["parameters"] = {"dimension": self.cfg.dimensions}
        data = self.http.post(
            self.cfg.base_url,
            {"Authorization": f"Bearer {self.cfg.api_key}"},
            payload,
        )
        self._record_usage(data)
        try:
            rows = sorted(data["output"]["embeddings"], key=lambda row: row["text_index"])
            if [row["text_index"] for row in rows] != list(range(len(texts))):
                raise ValueError("invalid text indexes")
            return [row["embedding"] for row in rows]
        except Exception as exc:
            raise EmbeddingUnavailable(f"unexpected DashScope embedding response: {type(exc).__name__}") from exc

    def _validate_vectors(self, texts: list[str], vectors: list[list[float]]) -> list[list[float]]:
        if len(vectors) != len(texts):
            raise EmbeddingUnavailable(
                f"embedding response count mismatch: expected {len(texts)}, got {len(vectors)}"
            )
        normalized: list[list[float]] = []
        dimensions: set[int] = set()
        for vector in vectors:
            if not isinstance(vector, list) or not vector:
                raise EmbeddingUnavailable("embedding response contains an empty or invalid vector")
            try:
                values = [float(value) for value in vector if not isinstance(value, bool)]
            except (TypeError, ValueError) as exc:
                raise EmbeddingUnavailable("embedding response contains a non-numeric value") from exc
            if len(values) != len(vector):
                raise EmbeddingUnavailable("embedding response contains a non-numeric value")
            if not all(math.isfinite(value) for value in values):
                raise EmbeddingUnavailable("embedding response contains a non-finite value")
            dimensions.add(len(values))
            normalized.append(values)
        if len(dimensions) != 1:
            raise EmbeddingUnavailable("embedding response contains inconsistent vector dimensions")
        actual_dimensions = next(iter(dimensions))
        if self.cfg.dimensions and actual_dimensions != self.cfg.dimensions:
            raise EmbeddingUnavailable(
                f"embedding dimension mismatch: expected {self.cfg.dimensions}, got {actual_dimensions}"
            )
        return normalized

    def _record_usage(self, data: dict[str, Any]) -> None:
        self.request_count += 1
        usage = data.get("usage") if isinstance(data, dict) else None
        if not isinstance(usage, dict):
            return
        try:
            self.input_tokens += max(0, int(usage.get("total_tokens", 0)))
        except (TypeError, ValueError):
            pass
