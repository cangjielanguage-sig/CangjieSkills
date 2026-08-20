from __future__ import annotations

import copy
import datetime as dt
import json
import threading
import uuid
from dataclasses import asdict
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any
from urllib.parse import parse_qs, unquote, urlparse

from .admin import ADMIN_HTML
from .config import AppConfig, apply_overrides
from .indexer import build_index, compact_index, remove_version
from .search import Searcher


MAX_JOB_LOGS = 300


def run_http(cfg: AppConfig, *, host: str = "127.0.0.1", port: int = 8765) -> None:
    state = ServerState()

    class Handler(BaseHTTPRequestHandler):
        server_version = "CangjieHarmonyKnowledge/0.1"

        def do_GET(self) -> None:  # noqa: N802
            parsed = urlparse(self.path)
            qs = parse_qs(parsed.query)
            try:
                if parsed.path == "/admin":
                    self._html(ADMIN_HTML)
                    return
                if parsed.path == "/api/jobs":
                    self._json(state.jobs_snapshot())
                    return
                if parsed.path == "/api/versions":
                    with Searcher(cfg) as searcher:
                        self._json(searcher.versions())
                    return
                if parsed.path == "/health":
                    with Searcher(cfg) as searcher:
                        self._json(searcher.status())
                    return
                if parsed.path == "/search":
                    with Searcher(cfg) as searcher:
                        self._json(
                            searcher.search(
                                one(qs, "q"),
                                top_k=safe_int(one(qs, "top_k", "8"), 8),
                                scope=one(qs, "scope", "all"),
                                embedding_mode=one(qs, "embedding", None),
                                version=one(qs, "version", None),
                            )
                        )
                    return
                if parsed.path.startswith("/symbol/"):
                    name = unquote(parsed.path.removeprefix("/symbol/"))
                    with Searcher(cfg) as searcher:
                        self._json(
                            searcher.lookup_symbol(
                                name,
                                include_members=safe_bool(one(qs, "members", "false")),
                                include_examples=safe_bool(one(qs, "examples", "false")),
                                version=one(qs, "version", None),
                            )
                            or {"error": "not_found"}
                        )
                    return
                if parsed.path == "/doc":
                    with Searcher(cfg) as searcher:
                        doc = searcher.read_doc(
                            one(qs, "ref"),
                            mode=one(qs, "mode", "section"),
                            max_chars=safe_int(one(qs, "max_chars", "12000"), 12000),
                            version=one(qs, "version", None),
                        )
                    self._json(doc or {"error": "not_found"})
                    return
                if parsed.path == "/examples":
                    with Searcher(cfg) as searcher:
                        self._json(
                            searcher.find_examples(
                                one(qs, "q"),
                                top_k=safe_int(one(qs, "top_k", "5"), 5),
                                version=one(qs, "version", None),
                            )
                        )
                    return
                self._json({"error": "not_found"}, status=404)
            except Exception as exc:
                self._json(error_payload(exc), status=500)

        def do_POST(self) -> None:  # noqa: N802
            parsed = urlparse(self.path)
            try:
                payload = self._read_json()
                if parsed.path == "/api/build":
                    self._json(state.start_build(cfg, payload), status=202)
                    return
                if parsed.path == "/api/versions/remove":
                    version = str(payload.get("version") or "").strip()
                    if not version:
                        self._json({"error": "version_required"}, status=400)
                        return
                    self._json(state.remove_version(cfg, version, physical=bool(payload.get("physical"))))
                    return
                if parsed.path == "/api/compact":
                    self._json(state.compact(cfg))
                    return
                self._json({"error": "not_found"}, status=404)
            except Exception as exc:
                self._json(error_payload(exc), status=500)

        def log_message(self, fmt: str, *args: Any) -> None:
            return

        def _json(self, data: Any, *, status: int = 200) -> None:
            body = json.dumps(data, ensure_ascii=False, indent=2).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def _html(self, html: str, *, status: int = 200) -> None:
            body = html.encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def _read_json(self) -> dict[str, Any]:
            length = safe_int(self.headers.get("Content-Length"), 0)
            raw = self.rfile.read(length).decode("utf-8") if length else "{}"
            payload = json.loads(raw or "{}")
            if not isinstance(payload, dict):
                raise ValueError("JSON body must be an object")
            return payload

    httpd = ThreadingHTTPServer((host, port), Handler)
    print(f"HarmonyOS Knowledge HTTP server listening on http://{host}:{port}")
    print(f"HarmonyOS Knowledge admin panel: http://{host}:{port}/admin")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("HarmonyOS Knowledge HTTP server stopped")
    finally:
        httpd.server_close()


class ServerState:
    def __init__(self) -> None:
        self.jobs: dict[str, dict[str, Any]] = {}
        self.job_lock = threading.Lock()
        self.build_lock = threading.Lock()

    def jobs_snapshot(self) -> list[dict[str, Any]]:
        with self.job_lock:
            return sorted((copy.deepcopy(job) for job in self.jobs.values()), key=lambda item: item.get("started_at", ""), reverse=True)

    def start_build(self, base_cfg: AppConfig, payload: dict[str, Any]) -> dict[str, Any]:
        job_id = uuid.uuid4().hex[:12]
        job = {
            "id": job_id,
            "status": "running",
            "started_at": utc_now(),
            "request": sanitize_payload(payload),
            "logs": [],
        }
        with self.job_lock:
            self.jobs[job_id] = job

        thread = threading.Thread(target=self._run_build, args=(job_id, base_cfg, payload), name=f"knowledge-build-{job_id}", daemon=True)
        thread.start()
        return {"job_id": job_id, "status": "running"}

    def remove_version(self, cfg: AppConfig, version: str, *, physical: bool = False) -> dict[str, int | str]:
        with self.build_lock:
            return remove_version(cfg, version, physical=physical)

    def compact(self, cfg: AppConfig) -> dict[str, Any]:
        with self.build_lock:
            return compact_index(cfg)

    def _run_build(self, job_id: str, base_cfg: AppConfig, payload: dict[str, Any]) -> None:
        acquired = self.build_lock.acquire(blocking=False)
        if not acquired:
            self._update_job(job_id, status="queued", message="waiting for another build to finish")
            self.build_lock.acquire()
        try:
            self._update_job(job_id, status="running", message="")
            cfg = build_cfg_from_payload(base_cfg, payload)
            stats = build_index(
                cfg,
                incremental=bool(payload.get("incremental")),
                remove_missing=not bool(payload.get("keep_missing")),
                quiet=bool(payload.get("quiet", True)),
                progress_interval=safe_int(payload.get("progress_interval"), 10),
                progress_callback=lambda event: self._append_log(job_id, event),
            )
            self._update_job(job_id, status="complete", finished_at=utc_now(), result=asdict(stats))
        except Exception as exc:
            self._update_job(job_id, status="failed", finished_at=utc_now(), **error_payload(exc))
        finally:
            self.build_lock.release()

    def _append_log(self, job_id: str, event: dict[str, Any]) -> None:
        with self.job_lock:
            job = self.jobs.get(job_id)
            if not job:
                return
            logs = list(job.get("logs") or [])
            logs.append({**event, "time": utc_now()})
            job["logs"] = logs[-MAX_JOB_LOGS:]
            job["last_event"] = event

    def _update_job(self, job_id: str, **updates: Any) -> None:
        with self.job_lock:
            if job_id in self.jobs:
                self.jobs[job_id].update(updates)


def build_cfg_from_payload(base_cfg: AppConfig, payload: dict[str, Any]) -> AppConfig:
    cfg = copy.deepcopy(base_cfg)
    return apply_overrides(
        cfg,
        docs_root=str(payload.get("docs_root") or cfg.docs_root),
        docs_version=str(payload.get("version") or cfg.docs_version),
        embedding_mode=payload.get("embedding_mode"),
        embedding_api_key_env=payload.get("embedding_api_key_env"),
        embedding_batch_size=safe_int(payload.get("embedding_batch_size"), 0) or None,
    )


def sanitize_payload(payload: dict[str, Any]) -> dict[str, Any]:
    result = dict(payload)
    if result.get("api_key"):
        result["api_key"] = "***"
    return result


def error_payload(exc: Exception) -> dict[str, str]:
    return {"error": type(exc).__name__, "message": str(exc)}


def utc_now() -> str:
    return dt.datetime.now(dt.UTC).isoformat()


def safe_int(value: Any, default: int) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def safe_bool(value: Any) -> bool:
    return str(value).strip().lower() in {"1", "true", "yes", "on"}


def one(qs: dict[str, list[str]], key: str, default: str | None = "") -> str:
    values = qs.get(key)
    if not values:
        return default or ""
    return values[0]
