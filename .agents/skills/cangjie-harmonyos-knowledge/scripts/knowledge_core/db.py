from __future__ import annotations

import sqlite3
from pathlib import Path


SCHEMA = """
pragma journal_mode=WAL;
pragma synchronous=NORMAL;

create table if not exists metadata (
  key text primary key,
  value text not null
);

create table if not exists documents (
  id integer primary key,
  version text not null default 'default',
  path text not null,
  doc_type text not null,
  kit text not null,
  title text not null,
  hash text not null,
  mtime real not null,
  encoding text not null,
  size integer not null,
  unique(version, path)
);

create table if not exists versions (
  version text primary key,
  docs_root text not null,
  display_name text,
  status text not null default 'ready',
  documents integer not null default 0,
  sections integer not null default 0,
  symbols integer not null default 0,
  examples integer not null default 0,
  vectors integer not null default 0,
  created_at text not null,
  updated_at text not null,
  manifest_json text not null default '{}'
);

create table if not exists sections (
  id integer primary key,
  document_id integer not null references documents(id) on delete cascade,
  version text not null default 'default',
  path text not null,
  doc_type text not null,
  kit text not null,
  title text not null,
  level integer not null,
  breadcrumb text not null,
  anchor text not null,
  start_line integer not null,
  end_line integer not null,
  body text not null,
  kind text not null,
  parent_symbol text,
  contracts_json text not null default '{}'
);

create table if not exists symbols (
  id integer primary key,
  section_id integer not null references sections(id) on delete cascade,
  document_id integer not null references documents(id) on delete cascade,
  version text not null default 'default',
  name text not null,
  normalized text not null,
  kind text not null,
  signature text not null,
  title text not null,
  path text not null,
  anchor text not null,
  start_line integer not null,
  end_line integer not null,
  parent text
);

create index if not exists idx_symbols_name on symbols(name);
create index if not exists idx_symbols_norm on symbols(normalized);
create index if not exists idx_sections_path_anchor on sections(path, anchor);
create index if not exists idx_sections_doc_type on sections(doc_type);

create table if not exists examples (
  id integer primary key,
  section_id integer not null references sections(id) on delete cascade,
  document_id integer not null references documents(id) on delete cascade,
  version text not null default 'default',
  path text not null,
  anchor text not null,
  start_line integer not null,
  end_line integer not null,
  language text not null,
  code text not null,
  imports text not null,
  nearby_symbol text
);

create table if not exists links (
  id integer primary key,
  document_id integer not null references documents(id) on delete cascade,
  section_id integer not null references sections(id) on delete cascade,
  version text not null default 'default',
  path text not null,
  line integer not null,
  text text not null,
  target text not null,
  target_path text,
  target_anchor text
);

create table if not exists vectors (
  id integer primary key,
  section_id integer not null references sections(id) on delete cascade,
  version text not null default 'default',
  provider text not null,
  model text not null,
  dimensions integer not null,
  vector_blob blob not null,
  text_hash text not null,
  created_at text not null,
  unique(section_id, provider, model)
);
"""


FTS_SCHEMA = """
create virtual table if not exists fts_sections_lex using fts5(
  title, breadcrumb, body,
  content='sections', content_rowid='id', tokenize='unicode61'
);
create virtual table if not exists fts_sections_tri using fts5(
  title, breadcrumb, body,
  content='sections', content_rowid='id', tokenize='trigram'
);
create virtual table if not exists fts_examples using fts5(
  code, imports, nearby_symbol,
  content='examples', content_rowid='id', tokenize='unicode61'
);
"""


def connect(index_path: Path) -> sqlite3.Connection:
    index_path.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(index_path, check_same_thread=False, timeout=30.0)
    con.row_factory = sqlite3.Row
    con.execute("pragma foreign_keys=on")
    con.execute("pragma busy_timeout=30000")
    return con


def init_db(con: sqlite3.Connection) -> None:
    con.executescript(SCHEMA)
    migrate_db(con)
    con.executescript(FTS_SCHEMA)
    con.commit()


def migrate_db(con: sqlite3.Connection) -> None:
    migrate_documents_version_unique(con)
    for table in ("sections", "symbols", "examples", "links", "vectors"):
        ensure_column(con, table, "version", "text not null default 'default'")
    ensure_column(con, "sections", "contracts_json", "text not null default '{}'")
    ensure_column(con, "vectors", "vector_blob", "blob")
    con.executescript(
        """
        create index if not exists idx_symbols_version_norm on symbols(version, normalized);
        create index if not exists idx_sections_version_path_anchor on sections(version, path, anchor);
        create index if not exists idx_sections_version_doc_type on sections(version, doc_type);
        create index if not exists idx_documents_version_path on documents(version, path);
        create index if not exists idx_sections_document on sections(document_id);
        create index if not exists idx_symbols_document on symbols(document_id);
        create index if not exists idx_examples_document on examples(document_id);
        create index if not exists idx_links_document on links(document_id);
        create index if not exists idx_examples_version on examples(version);
        create index if not exists idx_links_version on links(version);
        create index if not exists idx_vectors_version on vectors(version);
        """
    )
    ensure_default_version_row(con)


def table_columns(con: sqlite3.Connection, table: str) -> set[str]:
    return {row["name"] for row in con.execute(f"pragma table_info({table})")}


def ensure_column(con: sqlite3.Connection, table: str, name: str, definition: str) -> None:
    if name not in table_columns(con, table):
        con.execute(f"alter table {table} add column {name} {definition}")


def migrate_documents_version_unique(con: sqlite3.Connection) -> None:
    row = con.execute("select sql from sqlite_master where type='table' and name='documents'").fetchone()
    if not row:
        return
    sql = str(row["sql"] or "").lower()
    cols = table_columns(con, "documents")
    if "version" in cols and "unique(version, path)" in sql.replace("\n", " "):
        return

    con.execute("pragma foreign_keys=off")
    try:
        con.execute(
            """
            create table if not exists documents_new (
              id integer primary key,
              version text not null default 'default',
              path text not null,
              doc_type text not null,
              kit text not null,
              title text not null,
              hash text not null,
              mtime real not null,
              encoding text not null,
              size integer not null,
              unique(version, path)
            )
            """
        )
        if "version" in cols:
            con.execute(
                """
                insert or ignore into documents_new(id, version, path, doc_type, kit, title, hash, mtime, encoding, size)
                select id, coalesce(version, 'default'), path, doc_type, kit, title, hash, mtime, encoding, size
                from documents
                """
            )
        else:
            con.execute(
                """
                insert or ignore into documents_new(id, version, path, doc_type, kit, title, hash, mtime, encoding, size)
                select id, 'default', path, doc_type, kit, title, hash, mtime, encoding, size
                from documents
                """
            )
        con.execute("drop table documents")
        con.execute("alter table documents_new rename to documents")
    finally:
        con.execute("pragma foreign_keys=on")


def ensure_default_version_row(con: sqlite3.Connection) -> None:
    import datetime as dt

    count = con.execute("select count(*) c from documents where version = 'default'").fetchone()["c"]
    now = dt.datetime.now(dt.UTC).isoformat()
    if count:
        stats = con.execute(
            """
            select
              (select count(*) from documents where version = 'default') documents,
              (select count(*) from sections where version = 'default') sections,
              (select count(*) from symbols where version = 'default') symbols,
              (select count(*) from examples where version = 'default') examples,
              (select count(*) from vectors where version = 'default') vectors
            """
        ).fetchone()
        con.execute(
            """
            insert or ignore into versions(
              version, docs_root, display_name, status, documents, sections, symbols, examples, vectors,
              created_at, updated_at, manifest_json
            )
            values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                "default",
                "docs",
                "default",
                "ready",
                stats["documents"],
                stats["sections"],
                stats["symbols"],
                stats["examples"],
                stats["vectors"],
                now,
                now,
                "{}",
            ),
        )


def clear_db(con: sqlite3.Connection) -> None:
    tables = [
        "fts_sections_lex",
        "fts_sections_tri",
        "fts_examples",
        "vectors",
        "links",
        "examples",
        "symbols",
        "sections",
        "documents",
        "versions",
        "metadata",
    ]
    for table in tables:
        con.execute(f"delete from {table}")
    con.commit()
