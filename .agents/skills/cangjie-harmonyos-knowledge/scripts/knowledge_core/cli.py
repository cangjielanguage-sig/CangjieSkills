from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path

from .config import EMBEDDING_MODES, apply_overrides, load_config
from .db import connect, init_db
from .http_server import run_http
from .indexer import build_index, compact_index, remove_version
from .mcp_server import run_mcp
from .search import Searcher
from .util import configure_stdio


def main(argv: list[str] | None = None) -> int:
    configure_stdio()
    parser = argparse.ArgumentParser(prog="knowledge", description="Cangjie HarmonyOS packaged knowledge service")
    parser.add_argument("--config", help="Path to cangjie.skills.toml")
    parser.add_argument("--index-dir", help="Override the packaged data directory")
    parser.add_argument("--embedding-api-format", choices=("dashscope", "openai"))
    parser.add_argument("--embedding-model")
    parser.add_argument("--embedding-base-url")
    parser.add_argument("--embedding-api-key-env")
    parser.add_argument("--embedding-batch-size", type=int)
    parser.add_argument("--embedding-dimensions", type=int)

    sub = parser.add_subparsers(dest="cmd", required=True)
    p_build = sub.add_parser("build", help="Build the local index")
    p_build.add_argument("docs_root", nargs="?", default=None)
    p_build.add_argument("--version", default=None, help="SDK/docs version stored in the index, for example 6.1.1.345")
    p_build.add_argument("--incremental", action="store_true", help="Update only changed files for this version and preserve other versions")
    p_build.add_argument("--no-remove-missing", action="store_true", help="In incremental mode, keep indexed docs that no longer exist on disk")
    p_build.add_argument("--embedding-mode", choices=("off", "index", "all"), default=None)
    p_build.add_argument("--progress-interval", type=int, default=10, help="Log progress every N files or vector batches")
    p_build.add_argument("--quiet", action="store_true")

    p_query = sub.add_parser("query", help="Search docs from CLI")
    p_query.add_argument("query")
    p_query.add_argument("--version", default=None, help="Version to search; use 'all' to search every version")
    p_query.add_argument("--embedding-mode", choices=("off", "search", "all"), default=None)
    p_query.add_argument("--scope", choices=("all", "api", "guide", "examples"), default="all")
    p_query.add_argument("--top-k", type=int, default=8)

    p_symbol = sub.add_parser("symbol", help="Look up an API symbol")
    p_symbol.add_argument("name")
    p_symbol.add_argument("--version", default=None)
    p_symbol.add_argument("--members", action="store_true", help="Include up to 80 direct members")
    p_symbol.add_argument("--examples", action="store_true", help="Include related examples")

    p_doc = sub.add_parser("read", help="Read doc by ref")
    p_doc.add_argument("ref")
    p_doc.add_argument("--version", default=None)
    p_doc.add_argument("--mode", choices=("section", "full"), default="section")
    p_doc.add_argument("--max-chars", type=int, default=12000)

    p_serve = sub.add_parser("serve", help="Run HTTP server")
    p_serve.add_argument("--host", default="127.0.0.1")
    p_serve.add_argument("--port", type=int, default=8765)
    p_serve.add_argument("--embedding-mode", choices=EMBEDDING_MODES, default=None)

    p_mcp = sub.add_parser("mcp", help="Run MCP stdio server")
    p_mcp.add_argument("--embedding-mode", choices=EMBEDDING_MODES, default=None)

    p_versions = sub.add_parser("versions", help="List or remove indexed document versions")
    versions_sub = p_versions.add_subparsers(dest="versions_cmd", required=True)
    versions_sub.add_parser("list", help="List indexed versions")
    p_versions_remove = versions_sub.add_parser("remove", help="Remove one indexed version")
    p_versions_remove.add_argument("version")
    p_versions_remove.add_argument("--physical", action="store_true", help="Physically delete rows and rebuild FTS; slower, mainly for offline maintenance")
    versions_sub.add_parser("compact", help="Physically compact the index by keeping ready versions only")

    p_doctor = sub.add_parser("doctor", help="Check source/index integrity and SQLite capabilities")
    p_doctor.add_argument("--strict", action="store_true", help="Return a non-zero status when the package is unhealthy")

    args = parser.parse_args(argv)
    cfg = load_config(args.config)
    cfg = apply_overrides(
        cfg,
        docs_root=getattr(args, "docs_root", None),
        index_dir=args.index_dir,
        docs_version=getattr(args, "version", None),
        embedding_mode=getattr(args, "embedding_mode", None),
        embedding_api_format=args.embedding_api_format,
        embedding_model=args.embedding_model,
        embedding_base_url=args.embedding_base_url,
        embedding_api_key_env=args.embedding_api_key_env,
        embedding_batch_size=args.embedding_batch_size,
        embedding_dimensions=args.embedding_dimensions,
    )

    if args.cmd == "build":
        stats = build_index(
            cfg,
            quiet=args.quiet,
            progress_interval=args.progress_interval,
            incremental=args.incremental,
            remove_missing=not args.no_remove_missing,
        )
        print(json.dumps(asdict(stats), ensure_ascii=False, indent=2))
        return 0

    if args.cmd == "versions":
        if args.versions_cmd == "remove":
            print(json.dumps(remove_version(cfg, args.version, physical=args.physical), ensure_ascii=False, indent=2))
            return 0
        if args.versions_cmd == "compact":
            print(json.dumps(compact_index(cfg), ensure_ascii=False, indent=2))
            return 0
        searcher = Searcher(cfg)
        try:
            print(json.dumps(searcher.versions(), ensure_ascii=False, indent=2))
        finally:
            searcher.close()
        return 0

    if args.cmd == "doctor":
        healthy = doctor(cfg)
        return 0 if healthy or not args.strict else 1

    if args.cmd == "serve":
        run_http(cfg, host=args.host, port=args.port)
        return 0

    if args.cmd == "mcp":
        run_mcp(cfg)
        return 0

    if args.cmd == "read" and args.mode == "section" and "#" not in args.ref:
        print(
            json.dumps(
                {
                    "error": "section reads require an exact anchored ref",
                    "hint": "use a query result ref containing #anchor, or pass --mode full explicitly",
                    "ref": args.ref,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return 2

    searcher = Searcher(cfg)
    try:
        if args.cmd == "query":
            print(
                json.dumps(
                    searcher.search(
                        args.query,
                        top_k=args.top_k,
                        scope=args.scope,
                        embedding_mode=args.embedding_mode,
                        version=args.version,
                    ),
                    ensure_ascii=False,
                    indent=2,
                )
            )
        elif args.cmd == "symbol":
            print(
                json.dumps(
                    searcher.lookup_symbol(
                        args.name,
                        include_members=args.members,
                        include_examples=args.examples,
                        version=args.version,
                    ),
                    ensure_ascii=False,
                    indent=2,
                )
            )
        elif args.cmd == "read":
            print(json.dumps(searcher.read_doc(args.ref, mode=args.mode, max_chars=args.max_chars, version=args.version), ensure_ascii=False, indent=2))
    finally:
        searcher.close()
    return 0


def doctor(cfg) -> bool:
    import sqlite3

    index_path = Path(cfg.index_path)
    docs_root = Path(cfg.docs_root)
    docs_files = sorted(docs_root.rglob("*.md")) if docs_root.is_dir() else []
    checks: dict[str, object] = {
        "sqlite_version": sqlite3.sqlite_version,
        "index_path": str(index_path),
        "index_exists": index_path.is_file(),
        "index_size_bytes": index_path.stat().st_size if index_path.is_file() else 0,
        "docs_root": str(docs_root),
        "docs_root_exists": docs_root.is_dir(),
        "docs_files": len(docs_files),
    }
    if not index_path.is_file():
        checks.update(
            fts5_trigram="not-checked",
            documents=0,
            sections=0,
            symbols=0,
            examples=0,
            vectors=0,
            unindexed_docs=[],
            missing_source_docs=[],
            healthy=False,
        )
        print(json.dumps(checks, ensure_ascii=False, indent=2))
        return False

    con = connect(index_path)
    init_db(con)
    try:
        con.execute("create virtual table if not exists temp.__knowledge_tri using fts5(x, tokenize='trigram')")
        checks["fts5_trigram"] = True
    except Exception as exc:
        checks["fts5_trigram"] = f"failed:{type(exc).__name__}"
    try:
        for table in ("fts_sections_lex", "fts_sections_tri", "fts_examples"):
            con.execute(f"insert into {table}({table}, rank) values ('integrity-check', 1)")
        checks["fts_integrity"] = "ok"
    except Exception as exc:
        checks["fts_integrity"] = f"failed:{type(exc).__name__}"
    try:
        active = con.execute(
            """
            select
              (select count(*) from documents d where exists (select 1 from versions v where v.version = d.version and v.status = 'ready')) documents,
              (select count(*) from sections s where exists (select 1 from versions v where v.version = s.version and v.status = 'ready')) sections,
              (select count(*) from symbols y where exists (select 1 from versions v where v.version = y.version and v.status = 'ready')) symbols,
              (select count(*) from examples e where exists (select 1 from versions v where v.version = e.version and v.status = 'ready')) examples,
              (select count(*) from vectors r where exists (select 1 from versions v where v.version = r.version and v.status = 'ready')) vectors
            """
        ).fetchone()
        physical = con.execute(
            """
            select
              (select count(*) from documents) documents,
              (select count(*) from sections) sections,
              (select count(*) from symbols) symbols,
              (select count(*) from examples) examples,
              (select count(*) from vectors) vectors
            """
        ).fetchone()
        checks["documents"] = active["documents"]
        checks["sections"] = active["sections"]
        checks["symbols"] = active["symbols"]
        checks["examples"] = active["examples"]
        checks["vectors"] = active["vectors"]
        checks["vector_coverage"] = round(active["vectors"] / active["sections"], 4) if active["sections"] else 0.0
        vector_profile = con.execute(
            """
            select r.provider, r.model, r.dimensions, count(*) count
            from vectors r
            where exists (select 1 from versions v where v.version = r.version and v.status = 'ready')
            group by r.provider, r.model, r.dimensions
            order by r.provider, r.model, r.dimensions
            """
        ).fetchall()
        configured_vector_params: list[object] = [cfg.embedding.api_format, cfg.embedding.model]
        configured_dimension_sql = ""
        if cfg.embedding.dimensions is not None:
            configured_dimension_sql = " and r.dimensions = ?"
            configured_vector_params.append(cfg.embedding.dimensions)
        configured_vectors = int(
            con.execute(
                f"""
                select count(*)
                from vectors r
                where r.provider = ? and r.model = ? {configured_dimension_sql}
                  and exists (select 1 from versions v where v.version = r.version and v.status = 'ready')
                """,
                configured_vector_params,
            ).fetchone()[0]
        )
        checks["vector_required"] = bool(cfg.search_embeddings or cfg.index_embeddings)
        checks["configured_vectors"] = configured_vectors
        checks["configured_vector_coverage"] = (
            round(configured_vectors / active["sections"], 4) if active["sections"] else 0.0
        )
        checks["vector_profile"] = [dict(row) for row in vector_profile]
        checks["physical_counts"] = {key: physical[key] for key in ("documents", "sections", "symbols", "examples", "vectors")}
        checks["contract_sections"] = con.execute(
            "select count(*) c from sections where contracts_json != '{}'"
        ).fetchone()["c"]
        links = con.execute(
            """
            select
              count(*) total,
              sum(case when l.target_path is not null then 1 else 0 end) internal,
              sum(case when l.target_path is not null and exists(
                select 1 from sections s where s.version = l.version and s.path = l.target_path
              ) then 1 else 0 end) resolved_documents,
              sum(case when l.target_path is not null and l.target_anchor is not null then 1 else 0 end) anchored,
              sum(case when l.target_path is not null and l.target_anchor is not null and exists(
                select 1 from sections s
                where s.version = l.version and s.path = l.target_path and s.anchor = l.target_anchor
              ) then 1 else 0 end) resolved_anchors
            from links l
            where exists(select 1 from versions v where v.version = l.version and v.status = 'ready')
            """
        ).fetchone()
        internal_links = int(links["internal"] or 0)
        anchored_links = int(links["anchored"] or 0)
        checks["link_counts"] = {
            "total": int(links["total"] or 0),
            "internal": internal_links,
            "resolved_documents": int(links["resolved_documents"] or 0),
            "document_resolution": round(int(links["resolved_documents"] or 0) / internal_links, 4)
            if internal_links
            else 1.0,
            "anchored": anchored_links,
            "resolved_anchors": int(links["resolved_anchors"] or 0),
            "anchor_resolution": round(int(links["resolved_anchors"] or 0) / anchored_links, 4)
            if anchored_links
            else 1.0,
        }
        checks["fts_counts"] = {
            "sections_lex": con.execute("select count(*) c from fts_sections_lex").fetchone()["c"],
            "sections_tri": con.execute("select count(*) c from fts_sections_tri").fetchone()["c"],
            "examples": con.execute("select count(*) c from fts_examples").fetchone()["c"],
        }
        indexed_paths = {
            str(row["path"])
            for row in con.execute(
                """
                select distinct d.path
                from documents d
                where exists (select 1 from versions v where v.version = d.version and v.status = 'ready')
                """
            ).fetchall()
        }
        source_paths = {
            f"{docs_root.name}/{path.relative_to(docs_root).as_posix()}"
            for path in docs_files
        }
        checks["unindexed_docs"] = sorted(source_paths - indexed_paths)[:20]
        checks["missing_source_docs"] = sorted(indexed_paths - source_paths)[:20]
        checks["source_newer_than_index"] = sum(
            1 for path in docs_files if path.stat().st_mtime_ns > index_path.stat().st_mtime_ns
        )
        checks["sqlite_quick_check"] = con.execute("pragma quick_check").fetchone()[0]
        checks["versions"] = [
            dict(row)
            for row in con.execute(
                """
                select version, status, docs_root, documents, sections, symbols, examples, vectors, updated_at
                from versions
                order by updated_at desc, version
                """
            ).fetchall()
        ]
    finally:
        con.close()
    cache_path = Path(cfg.vector_cache_path)
    if cache_path.exists():
        cache_con = connect(cache_path)
        try:
            checks["vector_cache"] = cache_con.execute("select count(*) c from vector_cache").fetchone()["c"]
        except Exception:
            checks["vector_cache"] = "unavailable"
        finally:
            cache_con.close()
    else:
        checks["vector_cache"] = 0
    checks["healthy"] = bool(
        checks["docs_root_exists"]
        and checks["docs_files"]
        and checks.get("documents")
        and checks.get("sections")
        and not checks.get("unindexed_docs")
        and not checks.get("missing_source_docs")
        and checks.get("sqlite_quick_check") == "ok"
        and checks.get("fts_integrity") == "ok"
        and checks.get("fts_counts", {}).get("sections_lex") == checks.get("sections")
        and checks.get("fts_counts", {}).get("sections_tri") == checks.get("sections")
        and checks.get("fts_counts", {}).get("examples") == checks.get("examples")
        and checks.get("link_counts", {}).get("resolved_documents")
        == checks.get("link_counts", {}).get("internal")
        and checks.get("link_counts", {}).get("resolved_anchors")
        == checks.get("link_counts", {}).get("anchored")
        and (
            not checks.get("vector_required")
            or checks.get("configured_vectors") == checks.get("sections")
        )
    )
    print(json.dumps(checks, ensure_ascii=False, indent=2))
    return bool(checks["healthy"])
