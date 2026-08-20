from __future__ import annotations

import datetime as dt
import os
import re
import sqlite3
import sys
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Callable
from urllib.parse import urldefrag

from .config import SKILL_ROOT, AppConfig
from .db import FTS_SCHEMA, clear_db, connect, init_db
from .embedding import EmbeddingService
from .parser import ParsedDocument, extract_symbol_name, parse_markdown
from .util import json_dumps, normalize_symbol, relative_posix, sha256_text
from .vector_cache import VectorCache
from .vector_codec import pack_vector


SIGNATURE_RE = re.compile(r"```[A-Za-z0-9_-]*\n(.*?)```", re.DOTALL)
DELETED_VERSION_PREFIX = "__deleted__/"


@dataclass(slots=True)
class BuildStats:
    documents: int = 0
    documents_skipped: int = 0
    documents_removed: int = 0
    documents_updated: int = 0
    sections: int = 0
    symbols: int = 0
    examples: int = 0
    links: int = 0
    vector_batches: int = 0
    embedding_requests: int = 0
    embedding_input_tokens: int = 0
    vector_cache_hits: int = 0
    vector_failures: int = 0
    vectors: int = 0


@dataclass(slots=True)
class VectorJob:
    section_id: int
    text: str
    version: str = "default"


@dataclass(slots=True)
class BuildProgress:
    total_files: int
    quiet: bool = False
    interval: int = 10
    callback: Callable[[dict[str, Any]], None] | None = None
    start_time: float = field(default_factory=time.monotonic)
    last_log_time: float = field(default_factory=time.monotonic)
    use_color: bool = field(default_factory=lambda: sys.stderr.isatty() and not os.environ.get("NO_COLOR"))

    def log(self, stage: str, message: str, *, force: bool = False) -> None:
        elapsed = time.monotonic() - self.start_time
        event = {"stage": stage, "message": message, "elapsed": round(elapsed, 3), "elapsed_text": format_duration(elapsed)}
        if not self.quiet:
            print(format_console_event(stage, message, elapsed, use_color=self.use_color), file=sys.stderr, flush=True)
        if self.callback:
            self.callback(event)
        self.last_log_time = time.monotonic()

    def maybe_log(self, stage: str, message: str, count: int, *, force: bool = False) -> None:
        now = time.monotonic()
        if force or count <= 1 or count % max(1, self.interval) == 0 or now - self.last_log_time >= 30:
            self.log(stage, message, force=force)


def build_index(
    cfg: AppConfig,
    *,
    rebuild: bool = True,
    quiet: bool = False,
    progress_interval: int = 10,
    incremental: bool = False,
    remove_missing: bool = True,
    progress_callback: Callable[[dict[str, Any]], None] | None = None,
) -> BuildStats:
    docs_root = Path(cfg.docs_root)
    if not docs_root.exists():
        raise FileNotFoundError(f"docs root not found: {docs_root}")
    root = docs_root.resolve().parent
    version = normalize_version(cfg.docs_version)

    final_index = Path(cfg.index_path)
    building_index = final_index.with_name(final_index.stem + ".building" + final_index.suffix)
    cache: VectorCache | None = None
    con: sqlite3.Connection | None = None
    progress = BuildProgress(total_files=0, quiet=quiet, interval=progress_interval, callback=progress_callback)
    embedding = EmbeddingService(cfg) if cfg.index_embeddings else None
    if cfg.index_embeddings and not (embedding and embedding.available):
        raise RuntimeError(
            f"embedding index build requires the credential environment variable "
            f"{cfg.embedding.api_key_env}; previous index preserved"
        )
    try:
        preserve_other_versions = bool(rebuild and not incremental and version != "default" and final_index.exists())
        if incremental:
            target_index = final_index
            rebuild = False
        elif rebuild:
            remove_sqlite_family(building_index)
            if preserve_other_versions:
                clone_index(final_index, building_index)
            target_index = building_index
        else:
            target_index = final_index

        con = connect(target_index)
        init_db(con)
        if rebuild and target_index == final_index:
            clear_db(con)
        if preserve_other_versions:
            delete_version_contents(con, version)

        stats = BuildStats()
        cache = VectorCache(Path(cfg.vector_cache_path)) if embedding else None
        files = sorted(docs_root.rglob("*.md"))
        progress.total_files = len(files)
        progress.log(
            "start",
            f"docs={docs_root} files={len(files)} target={final_index} staging={target_index if rebuild else '-'} "
            f"version={version} incremental={incremental} remove_missing={remove_missing} "
            f"embedding_mode={cfg.embedding_mode} "
            f"embeddings={'on' if embedding and embedding.available else 'off'} "
            f"embedding_model={cfg.embedding.model if cfg.index_embeddings else '-'} "
            f"embedding_batch={cfg.embedding.batch_size}",
            force=True,
        )
        if cache:
            progress.log("cache", f"path={cfg.vector_cache_path} {cache.stats()}", force=True)
        seen_paths: set[str] = set()
        existing_paths = existing_document_paths(con, version) if incremental else set()
        deferred_vector_jobs: list[VectorJob] = []
        for idx, path in enumerate(files, 1):
            parsed = parse_markdown(path, root)
            seen_paths.add(parsed.rel_path)
            progress.maybe_log(
                "parse",
                f"{idx}/{len(files)} {parsed.rel_path} sections={len(parsed.sections)}",
                idx,
                force=idx == 1,
            )
            if incremental and is_document_unchanged(con, version, parsed):
                stats.documents_skipped += 1
                progress.maybe_log(
                    "skip",
                    f"{idx}/{len(files)} unchanged={stats.documents_skipped} {parsed.rel_path}",
                    stats.documents_skipped,
                )
                continue
            if incremental:
                removed = delete_document_by_path(con, version, parsed.rel_path)
                if removed:
                    stats.documents_updated += 1
            insert_document(
                con,
                parsed,
                stats,
                embedding,
                cache,
                progress,
                version=version,
                deferred_vector_jobs=deferred_vector_jobs,
            )
            progress.maybe_log(
                "index",
                f"{idx}/{len(files)} docs={stats.documents} sections={stats.sections} symbols={stats.symbols} "
                f"skipped={stats.documents_skipped} removed={stats.documents_removed} updated={stats.documents_updated} "
                f"examples={stats.examples} vectors={stats.vectors} "
                f"vector_cache={stats.vector_cache_hits} failures={stats.vector_failures}",
                idx,
                force=idx == len(files),
            )
        if incremental and remove_missing:
            for missing in sorted(existing_paths - seen_paths):
                if delete_document_by_path(con, version, missing):
                    stats.documents_removed += 1
                    progress.maybe_log("remove", f"version={version} removed={stats.documents_removed} {missing}", stats.documents_removed)
        if embedding and embedding.available and deferred_vector_jobs:
            insert_vectors(con, embedding, stats, deferred_vector_jobs, "all-documents", progress, cache)
        if embedding:
            expected_vectors = int(
                con.execute("select count(*) from sections where version = ?", (version,)).fetchone()[0]
            )
            vector_params: list[Any] = [version, embedding.cfg.api_format, embedding.cfg.model]
            dimension_sql = ""
            if embedding.cfg.dimensions is not None:
                dimension_sql = " and r.dimensions = ?"
                vector_params.append(embedding.cfg.dimensions)
            indexed_vectors = int(
                con.execute(
                    f"""
                    select count(*)
                    from vectors r
                    join sections s on s.id = r.section_id
                    where s.version = ? and r.provider = ? and r.model = ? {dimension_sql}
                    """,
                    vector_params,
                ).fetchone()[0]
            )
            if indexed_vectors != expected_vectors:
                raise RuntimeError(
                    f"embedding index incomplete for version {version}: "
                    f"expected {expected_vectors}, got {indexed_vectors}; previous index preserved"
                )
        write_manifest(con, cfg, stats)
        write_version_manifest(con, cfg, stats, version)
        con.commit()
        checkpoint_sqlite(con)
        con.close()
        con = None
        if rebuild:
            promote_index(building_index, final_index)
            progress.log("swap", f"promoted {building_index.name} -> {final_index.name}", force=True)
        progress.log(
            "done",
            f"docs={stats.documents} sections={stats.sections} symbols={stats.symbols} "
            f"skipped={stats.documents_skipped} removed={stats.documents_removed} updated={stats.documents_updated} "
            f"examples={stats.examples} links={stats.links} vector_batches={stats.vector_batches} "
            f"embedding_requests={stats.embedding_requests} input_tokens={stats.embedding_input_tokens} "
            f"vectors={stats.vectors} vector_cache={stats.vector_cache_hits} failures={stats.vector_failures}",
            force=True,
        )
        return stats
    except Exception:
        if con is not None:
            con.close()
            con = None
        if rebuild:
            remove_sqlite_family(building_index)
        raise
    finally:
        if con is not None:
            con.close()
        if cache is not None:
            cache.close()


def insert_document(
    con: sqlite3.Connection,
    parsed: ParsedDocument,
    stats: BuildStats,
    embedding: EmbeddingService | None,
    cache: VectorCache | None = None,
    progress: BuildProgress | None = None,
    *,
    version: str = "default",
    deferred_vector_jobs: list[VectorJob] | None = None,
) -> None:
    mtime = parsed.path.stat().st_mtime
    cur = con.execute(
        """
        insert into documents(version, path, doc_type, kit, title, hash, mtime, encoding, size)
        values (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            version,
            parsed.rel_path,
            parsed.doc_type,
            parsed.kit,
            parsed.title,
            parsed.digest,
            mtime,
            parsed.encoding,
            parsed.size,
        ),
    )
    doc_id = int(cur.lastrowid)
    stats.documents += 1
    vector_jobs: list[VectorJob] = []

    for section in parsed.sections:
        cur = con.execute(
            """
            insert into sections(
              document_id, version, path, doc_type, kit, title, level, breadcrumb, anchor,
              start_line, end_line, body, kind, parent_symbol, contracts_json
            )
            values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                doc_id,
                version,
                parsed.rel_path,
                parsed.doc_type,
                parsed.kit,
                section.title,
                section.level,
                section.breadcrumb,
                section.anchor,
                section.start_line,
                section.end_line,
                section.body,
                section.kind,
                section.parent_symbol,
                json_dumps(section.contracts),
            ),
        )
        section_id = int(cur.lastrowid)
        stats.sections += 1

        con.execute(
            "insert into fts_sections_lex(rowid, title, breadcrumb, body) values (?, ?, ?, ?)",
            (section_id, section.title, section.breadcrumb, section.body),
        )
        con.execute(
            "insert into fts_sections_tri(rowid, title, breadcrumb, body) values (?, ?, ?, ?)",
            (section_id, section.title, section.breadcrumb, section.body),
        )

        kind, symbol_name = extract_symbol_name(section.title)
        if kind and symbol_name:
            signature = extract_signature(section.body)
            insert_symbol(con, doc_id, section_id, parsed.rel_path, section, kind, symbol_name, signature, version=version)
            stats.symbols += 1

        for block in section.code_blocks:
            cur = con.execute(
                """
                insert into examples(section_id, document_id, version, path, anchor, start_line, end_line, language, code, imports, nearby_symbol)
                values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    section_id,
                    doc_id,
                    version,
                    parsed.rel_path,
                    section.anchor,
                    block.start_line,
                    block.end_line,
                    block.language,
                    block.code,
                    json_dumps(block.imports),
                    section.parent_symbol or symbol_name or section.title,
                ),
            )
            example_id = int(cur.lastrowid)
            con.execute(
                "insert into fts_examples(rowid, code, imports, nearby_symbol) values (?, ?, ?, ?)",
                (example_id, block.code, " ".join(block.imports), section.parent_symbol or symbol_name or section.title),
            )
            stats.examples += 1

        for link in section.links:
            target, frag = urldefrag(link.target)
            target_path = normalize_link_path(parsed.rel_path, target) if target else parsed.rel_path
            con.execute(
                """
                insert into links(document_id, section_id, version, path, line, text, target, target_path, target_anchor)
                values (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (doc_id, section_id, version, parsed.rel_path, link.line, link.text, link.target, target_path, frag or None),
            )
            stats.links += 1

        if embedding and embedding.available:
            vector_jobs.append(VectorJob(section_id=section_id, text=vector_source_text(parsed, section), version=version))

    if embedding and embedding.available and vector_jobs:
        if deferred_vector_jobs is not None:
            deferred_vector_jobs.extend(vector_jobs)
        else:
            insert_vectors(con, embedding, stats, vector_jobs, parsed.rel_path, progress, cache)


def normalize_version(version: str | None) -> str:
    version = (version or "default").strip()
    if not version or version in {"*", "all"}:
        raise ValueError("build version must be a concrete value")
    return version


def existing_document_paths(con: sqlite3.Connection, version: str) -> set[str]:
    return {
        row["path"]
        for row in con.execute("select path from documents where version = ?", (version,)).fetchall()
    }


def is_document_unchanged(con: sqlite3.Connection, version: str, parsed: ParsedDocument) -> bool:
    row = con.execute(
        "select hash, size from documents where version = ? and path = ? limit 1",
        (version, parsed.rel_path),
    ).fetchone()
    return bool(row and row["hash"] == parsed.digest and int(row["size"]) == int(parsed.size))


def delete_document_by_path(con: sqlite3.Connection, version: str, rel_path: str) -> bool:
    row = con.execute("select id from documents where version = ? and path = ? limit 1", (version, rel_path)).fetchone()
    if not row:
        return False
    delete_document(con, int(row["id"]))
    return True


def delete_version_contents(con: sqlite3.Connection, version: str) -> dict[str, int]:
    before = version_totals(con, version)
    if not any(before.values()):
        con.execute("delete from versions where version = ?", (version,))
        return before
    con.execute("delete from vectors where version = ?", (version,))
    con.execute("delete from links where version = ?", (version,))
    con.execute("delete from examples where version = ?", (version,))
    con.execute("delete from symbols where version = ?", (version,))
    con.execute("delete from sections where version = ?", (version,))
    con.execute("delete from documents where version = ?", (version,))
    con.execute("delete from versions where version = ?", (version,))
    rebuild_fts(con)
    return before


def delete_document(con: sqlite3.Connection, document_id: int) -> None:
    section_ids = [int(row["id"]) for row in con.execute("select id from sections where document_id = ?", (document_id,))]
    example_ids = [int(row["id"]) for row in con.execute("select id from examples where document_id = ?", (document_id,))]
    for section_id in section_ids:
        con.execute("delete from fts_sections_lex where rowid = ?", (section_id,))
        con.execute("delete from fts_sections_tri where rowid = ?", (section_id,))
    for example_id in example_ids:
        con.execute("delete from fts_examples where rowid = ?", (example_id,))
    con.execute("delete from documents where id = ?", (document_id,))


def rebuild_fts(con: sqlite3.Connection) -> None:
    for table in ("fts_sections_lex", "fts_sections_tri", "fts_examples"):
        con.execute(f"drop table if exists {table}")
    con.executescript(FTS_SCHEMA)
    con.execute(
        """
        insert into fts_sections_lex(rowid, title, breadcrumb, body)
        select id, title, breadcrumb, body
        from sections
        """
    )
    con.execute(
        """
        insert into fts_sections_tri(rowid, title, breadcrumb, body)
        select id, title, breadcrumb, body
        from sections
        """
    )
    con.execute(
        """
        insert into fts_examples(rowid, code, imports, nearby_symbol)
        select id, code, imports, coalesce(nearby_symbol, '')
        from examples
        """
    )


def extract_signature(body: str) -> str:
    match = SIGNATURE_RE.search(body)
    if not match:
        return ""
    code = match.group(1).strip()
    lines = [line.rstrip() for line in code.splitlines() if line.strip()]
    return "\n".join(lines[:12])


def insert_vectors(
    con: sqlite3.Connection,
    embedding: EmbeddingService,
    stats: BuildStats,
    jobs: list[VectorJob],
    rel_path: str = "",
    progress: BuildProgress | None = None,
    cache: VectorCache | None = None,
) -> None:
    batch_size = max(1, int(embedding.cfg.batch_size or 1))
    pending: list[VectorJob] = []
    for job in jobs:
        cached = (
            cache.get(
                provider=embedding.cfg.api_format,
                model=embedding.cfg.model,
                text=job.text,
                endpoint=embedding.cfg.base_url,
                requested_dimensions=embedding.cfg.dimensions,
            )
            if cache
            else None
        )
        if cached:
            insert_vector_row(con, embedding, job.section_id, job.text, cached.vector, version=job.version)
            stats.vectors += 1
            stats.vector_cache_hits += 1
        else:
            pending.append(job)
    if progress and stats.vector_cache_hits:
        progress.maybe_log(
            "embed",
            f"{rel_path} cache_hits={stats.vector_cache_hits} pending={len(pending)} vectors={stats.vectors}",
            stats.vector_cache_hits,
        )
    for start in range(0, len(pending), batch_size):
        batch = pending[start : start + batch_size]
        batch_start = time.monotonic()
        stats.vector_batches += 1
        try:
            vectors = embedding.embed_texts([job.text for job in batch])
        except Exception:
            stats.vector_failures += len(batch)
            if progress:
                progress.maybe_log(
                    "embed",
                    f"{rel_path} batch={stats.vector_batches} failed items={len(batch)} "
                    f"vector_failures={stats.vector_failures}",
                    stats.vector_batches,
                    force=True,
                )
            continue
        finally:
            stats.embedding_requests = embedding.request_count
            stats.embedding_input_tokens = embedding.input_tokens
        for job, vector in zip(batch, vectors):
            if not vector:
                stats.vector_failures += 1
                continue
            if cache:
                cache.put(
                    provider=embedding.cfg.api_format,
                    model=embedding.cfg.model,
                    text=job.text,
                    vector=vector,
                    endpoint=embedding.cfg.base_url,
                    requested_dimensions=embedding.cfg.dimensions,
                    commit=False,
                )
            insert_vector_row(con, embedding, job.section_id, job.text, vector, version=job.version)
            stats.vectors += 1
        if cache:
            cache.commit()
        if progress:
            progress.maybe_log(
                "embed",
                f"{rel_path} batch={stats.vector_batches} items={len(batch)} "
                f"vectors={stats.vectors} cache={stats.vector_cache_hits} "
                f"last={format_duration(time.monotonic() - batch_start)}",
                stats.vector_batches,
            )


def insert_vector_row(
    con: sqlite3.Connection,
    embedding: EmbeddingService,
    section_id: int,
    text: str,
    vector: list[float],
    version: str = "default",
) -> None:
    con.execute(
        """
        insert or replace into vectors(section_id, version, provider, model, dimensions, vector_blob, text_hash, created_at)
        values (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            section_id,
            version,
            embedding.cfg.api_format,
            embedding.cfg.model,
            len(vector),
            pack_vector(vector),
            sha256_text(text),
            dt.datetime.now(dt.UTC).isoformat(),
        ),
    )


def insert_symbol(
    con: sqlite3.Connection,
    doc_id: int,
    section_id: int,
    rel_path: str,
    section,
    kind: str,
    symbol_name: str,
    signature: str,
    *,
    version: str = "default",
) -> None:
    con.execute(
        """
        insert into symbols(section_id, document_id, version, name, normalized, kind, signature, title, path, anchor, start_line, end_line, parent)
        values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            section_id,
            doc_id,
            version,
            symbol_name,
            normalize_symbol(symbol_name),
            kind,
            signature,
            section.title,
            rel_path,
            section.anchor,
            section.start_line,
            section.end_line,
            section.parent_symbol,
        ),
    )


def normalize_link_path(source_rel: str, target: str) -> str | None:
    if not target or "://" in target or target.startswith("#"):
        return None
    src = Path(source_rel).parent
    target_path = (src / target).as_posix()
    parts: list[str] = []
    for part in target_path.split("/"):
        if part == "..":
            if parts:
                parts.pop()
        elif part and part != ".":
            parts.append(part)
    normalized = "/".join(parts)
    guide_reference = "docs/Guide/reference/"
    if normalized.startswith(guide_reference):
        return "docs/API/" + normalized[len(guide_reference) :]
    root_reference = "docs/reference/"
    if normalized.startswith(root_reference):
        return "docs/API/" + normalized[len(root_reference) :]
    if normalized.startswith("docs/") and not normalized.startswith(("docs/API/", "docs/Guide/")):
        return "docs/Guide/" + normalized[len("docs/") :]
    if normalized.startswith("application-dev/"):
        return "docs/Guide/" + normalized[len("application-dev/") :]
    return normalized


def vector_source_text(parsed: ParsedDocument, section) -> str:
    chunks = [
        parsed.title,
        parsed.kit,
        section.breadcrumb,
        section.title,
        section.body[:4000],
    ]
    return "\n".join(part for part in chunks if part)


def write_manifest(con: sqlite3.Connection, cfg: AppConfig, stats: BuildStats) -> None:
    manifest = {
        "built_at": dt.datetime.now(dt.UTC).isoformat(),
        "docs_root": portable_docs_root(cfg.docs_root),
        "docs_version": cfg.docs_version,
        "embedding_mode": cfg.embedding_mode,
        "index_embeddings": cfg.index_embeddings,
        "embedding_model": cfg.embedding.model if cfg.index_embeddings else None,
        "stats": asdict(stats),
    }
    con.execute("insert or replace into metadata(key, value) values ('manifest', ?)", (json_dumps(manifest),))


def write_version_manifest(con: sqlite3.Connection, cfg: AppConfig, stats: BuildStats, version: str) -> None:
    now = dt.datetime.now(dt.UTC).isoformat()
    totals = version_totals(con, version)
    manifest = {
        "built_at": now,
        "docs_root": portable_docs_root(cfg.docs_root),
        "docs_version": version,
        "embedding_mode": cfg.embedding_mode,
        "index_embeddings": cfg.index_embeddings,
        "embedding_model": cfg.embedding.model if cfg.index_embeddings else None,
        "last_build_stats": asdict(stats),
    }
    con.execute(
        """
        insert into versions(
          version, docs_root, display_name, status, documents, sections, symbols, examples, vectors,
          created_at, updated_at, manifest_json
        )
        values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        on conflict(version) do update set
          docs_root = excluded.docs_root,
          display_name = excluded.display_name,
          status = excluded.status,
          documents = excluded.documents,
          sections = excluded.sections,
          symbols = excluded.symbols,
          examples = excluded.examples,
          vectors = excluded.vectors,
          updated_at = excluded.updated_at,
          manifest_json = excluded.manifest_json
        """,
        (
            version,
            portable_docs_root(cfg.docs_root),
            version,
            "ready",
            totals["documents"],
            totals["sections"],
            totals["symbols"],
            totals["examples"],
            totals["vectors"],
            now,
            now,
            json_dumps(manifest),
        ),
    )


def portable_docs_root(docs_root: str) -> str:
    resolved = Path(docs_root).resolve()
    try:
        return resolved.relative_to(SKILL_ROOT.resolve()).as_posix()
    except ValueError:
        return str(resolved)


def version_totals(con: sqlite3.Connection, version: str) -> dict[str, int]:
    row = con.execute(
        """
        select
          (select count(*) from documents where version = ?) documents,
          (select count(*) from sections where version = ?) sections,
          (select count(*) from symbols where version = ?) symbols,
          (select count(*) from examples where version = ?) examples,
          (select count(*) from vectors where version = ?) vectors
        """,
        (version, version, version, version, version),
    ).fetchone()
    return {key: int(row[key]) for key in ("documents", "sections", "symbols", "examples", "vectors")}


def active_totals(con: sqlite3.Connection) -> dict[str, int]:
    row = con.execute(
        """
        select
          (select count(*) from documents d where exists (select 1 from versions v where v.version = d.version and v.status = 'ready')) documents,
          (select count(*) from sections s where exists (select 1 from versions v where v.version = s.version and v.status = 'ready')) sections,
          (select count(*) from symbols y where exists (select 1 from versions v where v.version = y.version and v.status = 'ready')) symbols,
          (select count(*) from examples e where exists (select 1 from versions v where v.version = e.version and v.status = 'ready')) examples,
          (select count(*) from vectors r where exists (select 1 from versions v where v.version = r.version and v.status = 'ready')) vectors
        """
    ).fetchone()
    return {key: int(row[key]) for key in ("documents", "sections", "symbols", "examples", "vectors")}


def physical_totals(con: sqlite3.Connection) -> dict[str, int]:
    row = con.execute(
        """
        select
          (select count(*) from documents) documents,
          (select count(*) from sections) sections,
          (select count(*) from symbols) symbols,
          (select count(*) from examples) examples,
          (select count(*) from vectors) vectors
        """
    ).fetchone()
    return {key: int(row[key]) for key in ("documents", "sections", "symbols", "examples", "vectors")}


def logical_remove_version(con: sqlite3.Connection, cfg: AppConfig, version: str) -> dict[str, int | str]:
    before = version_totals(con, version)
    now = dt.datetime.now(dt.UTC).isoformat()
    tombstone = f"{DELETED_VERSION_PREFIX}{version}/{dt.datetime.now(dt.UTC).strftime('%Y%m%dT%H%M%S%fZ')}"
    for table in ("vectors", "links", "examples", "symbols", "sections", "documents"):
        con.execute(f"update {table} set version = ? where version = ?", (tombstone, version))
    manifest = {
        "removed_at": now,
        "remove_mode": "logical",
        "tombstone_version": tombstone,
        "previous_counts": before,
    }
    con.execute(
        """
        insert into versions(
          version, docs_root, display_name, status, documents, sections, symbols, examples, vectors,
          created_at, updated_at, manifest_json
        )
        values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        on conflict(version) do update set
          status = excluded.status,
          documents = excluded.documents,
          sections = excluded.sections,
          symbols = excluded.symbols,
          examples = excluded.examples,
          vectors = excluded.vectors,
          updated_at = excluded.updated_at,
          manifest_json = excluded.manifest_json
        """,
        (
            version,
            cfg.docs_root,
            version,
            "deleted",
            before["documents"],
            before["sections"],
            before["symbols"],
            before["examples"],
            before["vectors"],
            now,
            now,
            json_dumps(manifest),
        ),
    )
    return {"version": version, "mode": "logical", "tombstone_version": tombstone, **before}


def remove_version(cfg: AppConfig, version: str, *, physical: bool = False) -> dict[str, int | str]:
    version = normalize_version(version)
    con = connect(Path(cfg.index_path))
    try:
        init_db(con)
        con.execute("begin immediate")
        before = delete_version_contents(con, version) if physical else logical_remove_version(con, cfg, version)
        con.commit()
        if physical:
            checkpoint_sqlite(con)
        return {"version": version, **before}
    except Exception:
        con.rollback()
        raise
    finally:
        con.close()


def compact_index(cfg: AppConfig) -> dict[str, Any]:
    final_index = Path(cfg.index_path)
    compacting_index = final_index.with_name(final_index.stem + ".compacting" + final_index.suffix)
    remove_sqlite_family(compacting_index)
    src = connect(final_index)
    dst = connect(compacting_index)
    try:
        init_db(src)
        init_db(dst)
        clear_db(dst)
        before_physical = physical_totals(src)
        before_active = active_totals(src)
        ready_versions = [row["version"] for row in src.execute("select version from versions where status = 'ready' order by version")]
        for table in ("metadata",):
            copy_table(src, dst, table)
        if ready_versions:
            placeholders = ",".join("?" for _ in ready_versions)
            where = f"version in ({placeholders})"
            for table in ("versions", "documents", "sections", "symbols", "examples", "links", "vectors"):
                copy_table(src, dst, table, where=where, params=ready_versions)
            rebuild_fts(dst)
        dst.commit()
        checkpoint_sqlite(dst)
    finally:
        src.close()
        dst.close()
    promote_index(compacting_index, final_index)
    con = connect(final_index)
    try:
        init_db(con)
        after_physical = physical_totals(con)
    finally:
        con.close()
    return {
        "compacted": True,
        "versions": ready_versions,
        "before_active": before_active,
        "before_physical": before_physical,
        "after_physical": after_physical,
    }


def copy_table(
    src: sqlite3.Connection,
    dst: sqlite3.Connection,
    table: str,
    *,
    where: str | None = None,
    params: list[Any] | tuple[Any, ...] = (),
) -> int:
    columns = [row["name"] for row in src.execute(f"pragma table_info({table})")]
    if not columns:
        return 0
    select_sql = f"select {', '.join(columns)} from {table}"
    if where:
        select_sql += f" where {where}"
    placeholders = ", ".join("?" for _ in columns)
    insert_sql = f"insert into {table}({', '.join(columns)}) values ({placeholders})"
    count = 0
    for row in src.execute(select_sql, params):
        dst.execute(insert_sql, [row[column] for column in columns])
        count += 1
    return count


def sqlite_family(path: Path) -> list[Path]:
    return [path, Path(str(path) + "-wal"), Path(str(path) + "-shm")]


def remove_sqlite_family(path: Path) -> None:
    for item in sqlite_family(path):
        try:
            item.unlink()
        except FileNotFoundError:
            pass


def clone_index(source: Path, target: Path) -> None:
    remove_sqlite_family(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    if not source.exists():
        return
    src = sqlite3.connect(source)
    dst = sqlite3.connect(target)
    try:
        src.backup(dst)
    finally:
        dst.close()
        src.close()


def checkpoint_sqlite(con: sqlite3.Connection) -> None:
    try:
        con.execute("pragma wal_checkpoint(TRUNCATE)")
    except sqlite3.DatabaseError:
        pass


def promote_index(building_index: Path, final_index: Path) -> None:
    checkpoint_candidates = sqlite_family(building_index)
    if not building_index.exists():
        raise FileNotFoundError(f"staging index not found: {building_index}")
    final_index.parent.mkdir(parents=True, exist_ok=True)
    # Remove sidecar files first so a replaced main db is not paired with stale WAL/SHM.
    for sidecar in sqlite_family(final_index)[1:]:
        try:
            sidecar.unlink()
        except FileNotFoundError:
            pass
    os.replace(building_index, final_index)
    for item in checkpoint_candidates[1:]:
        try:
            item.unlink()
        except FileNotFoundError:
            pass


STAGE_COLORS = {
    "start": "36",
    "cache": "35",
    "parse": "34",
    "skip": "90",
    "index": "32",
    "embed": "35",
    "degrade": "33",
    "remove": "33",
    "swap": "36",
    "done": "32",
}


def format_console_event(stage: str, message: str, elapsed: float, *, use_color: bool = False) -> str:
    label = stage.upper()[:8].ljust(8)
    elapsed_text = format_duration(elapsed).rjust(8)
    if use_color:
        color = STAGE_COLORS.get(stage, "37")
        label = f"\033[{color};1m{label}\033[0m"
        elapsed_text = f"\033[90m{elapsed_text}\033[0m"
    return f"{elapsed_text} | {label} | {message}"


def format_duration(seconds: float) -> str:
    seconds_i = max(0, int(seconds))
    if seconds_i < 60:
        return f"{seconds_i}s"
    minutes, secs = divmod(seconds_i, 60)
    if minutes < 60:
        return f"{minutes}m{secs:02d}s"
    hours, minutes = divmod(minutes, 60)
    return f"{hours}h{minutes:02d}m"
