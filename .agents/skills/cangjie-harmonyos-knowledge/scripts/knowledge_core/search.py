from __future__ import annotations

import json
import math
import re
import sqlite3
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .config import EMBEDDING_ALL, EMBEDDING_SEARCH, AppConfig
from .db import connect, init_db
from .embedding import EmbeddingService
from .util import has_cjk, json_loads, normalize_symbol
from .vector_cache import VectorCache
from .vector_codec import unpack_vector


ASCII_TOKEN_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*|[0-9]{2,}")
RANDOM_IDENTIFIER_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_]{23,}$")
TECHNICAL_IDENTIFIER_RE = re.compile(r"\b[A-Za-z][A-Za-z0-9_]{2,}\b")
CJK_TOKEN_RE = re.compile(r"[\u3400-\u9fff]{2,}")
LEXICAL_ROUTE_MIN_SCORE = 400.0
CJK_STOP_TERMS = {
    "如何",
    "怎么",
    "怎样",
    "什么",
    "一个",
    "这个",
    "那个",
    "里面",
    "时候",
    "可以",
    "需要",
}
CJK_BAD_GRAM_CHARS = set("如何怎么怎样什么或和与的了在里")
DOMAIN_TERMS = [
    "数据库",
    "持久化",
    "结构化",
    "本地",
    "保存",
    "存储",
    "创建",
    "打开",
    "获取",
    "查询",
    "插入",
    "更新",
    "删除",
    "配置",
    "上传",
    "下载",
    "生成",
    "关闭",
    "释放",
    "错误码",
    "权限",
    "日志",
    "示例",
    "步骤",
    "限制",
    "数据",
]


def _z(text: str) -> str:
    return text.encode("ascii").decode("unicode_escape")


HOWTO_TERMS = tuple(
    _z(item)
    for item in (
        r"\u5982\u4f55",
        r"\u600e\u4e48",
        r"\u600e\u6837",
        r"\u4f7f\u7528",
        r"\u5f00\u53d1",
        r"\u6b65\u9aa4",
        r"\u6d41\u7a0b",
        r"\u793a\u4f8b",
        r"\u914d\u7f6e",
        r"\u8bbe\u7f6e",
    )
) + ("how", "use", "usage", "guide", "example", "configure", "setup")
GUIDE_HEADING_TERMS = tuple(
    _z(item)
    for item in (
        r"\u5f00\u53d1\u6b65\u9aa4",
        r"\u6b65\u9aa4",
        r"\u793a\u4f8b",
        r"\u793a\u4f8b\u4ee3\u7801",
        r"\u4f7f\u7528\u8bf4\u660e",
        r"\u5feb\u901f\u5f00\u59cb",
        r"\u7ea6\u675f\u4e0e\u9650\u5236",
        r"\u6ce8\u610f",
        r"\u5904\u7406\u6b65\u9aa4",
    )
) + ("example", "usage", "quickstart", "steps", "guide", "tutorial", "troubleshooting")
ERROR_TERMS = tuple(_z(item) for item in (r"\u9519\u8bef\u7801", r"\u5f02\u5e38", r"\u5931\u8d25", r"\u539f\u56e0", r"\u5904\u7406")) + ("error", "exception", "failed", "cause", "solution")
LIMIT_TERMS = tuple(_z(item) for item in (r"\u9650\u5236", r"\u5927\u5c0f", r"\u6700\u5927", r"\u6700\u5c0f", r"\u591a\u5c11", r"\u5bb9\u91cf")) + ("limit", "size", "maximum", "minimum", "max", "min")
LIFECYCLE_TERMS = tuple(_z(item) for item in (r"\u5173\u95ed", r"\u91ca\u653e", r"\u9500\u6bc1", r"\u6e05\u7406")) + ("close", "closed", "release", "dispose", "destroy", "cleanup")
CONFIG_TERMS = tuple(_z(item) for item in (r"\u914d\u7f6e", r"\u4fdd\u5b58", r"\u5199\u5165", r"\u6301\u4e45\u5316", r"\u5b58\u50a8")) + ("config", "option", "options", "save", "write", "put", "flush", "persist")
TRANSFER_TERMS = tuple(_z(item) for item in (r"\u4e0a\u4f20", r"\u4e0b\u8f7d", r"\u7f51\u7edc\u8d44\u6e90", r"\u6587\u4ef6")) + ("upload", "download", "file", "resource", "transfer")
PERMISSION_TERMS = tuple(_z(item) for item in (r"\u6743\u9650", r"\u6388\u6743", r"\u7533\u8bf7")) + ("permission", "authorization", "authorize", "grant")
LOG_TERMS = tuple(_z(item) for item in (r"\u65e5\u5fd7", r"\u8f93\u51fa")) + ("log", "logger", "debug", "info", "warn", "error", "fatal")
CAMERA_TERMS = tuple(_z(item) for item in (r"\u76f8\u673a", r"\u62cd\u7167", r"\u9884\u89c8")) + ("camera", "photo", "preview")
UNIT_RE = re.compile(r"\b\d+(?:\.\d+)?\s?(?:b|kb|mb|gb|k|m|g|bytes?|rows?|items?)\b", re.IGNORECASE)
GENERIC_QUERY_TERMS = {
    "如何",
    "怎么",
    "怎样",
    "使用",
    "开发",
    "步骤",
    "示例",
    "配置",
    "设置",
    "创建",
    "打开",
    "获取",
    "查询",
    "数据",
    "保存",
    "存储",
    "本地",
    "how",
    "use",
    "usage",
    "guide",
    "example",
    "configure",
    "setup",
    "steps",
}
FOCUSED_ACTION_TERMS = (
    "发布",
    "订阅",
    "解码",
    "扫描",
    "分享",
    "声明",
    "匹配",
    "旋转",
    "缩放",
    "上传",
    "下载",
)

SEMANTIC_QUERY_ALIASES = (
    (("关系型数据库", "创建"), ("getRdbStore RdbStore",)),
    (("关系型数据库", "打开"), ("getRdbStore RdbStore",)),
    (("等值", "匹配"), ("equalTo",)),
    (("rdbpredicates", "查询"), ("equalTo", "query RdbPredicates")),
    (("resultset", "关闭"), ("ResultSet close",)),
    (("单条", "大小"), ("2M", "2MB relational_store")),
    (("用户首选项", "保存"), ("getPreferences put flush",)),
    (("上传", "下载"), ("request.agent.create Action.UPLOAD Action.DOWNLOAD",)),
    (("web", "深色"), ("darkMode forceDarkAccess WebDarkMode",)),
    (("huks", "生成"), ("generateKeyItem HuksOptions HuksParam",)),
    (("huks", "hmac"), ("UniversalKeystoreKit Huks HMAC",)),
    (("申请", "权限"), ("requestPermissionsFromUser",)),
    (("http", "请求"), ("createHttp HttpRequest request requestInStream",)),
    (("公共事件", "发布"), ("CommonEventManager publish CommonEventPublishData",)),
    (("解码", "pixelmap"), ("createImageSource createPixelMap ImageSource",)),
    (("pixelmap", "encode", "file"), ("ImagePacker packToFile PackingOption",)),
    (("编码", "pixelmap"), ("ImagePacker packToFile PackingOption",)),
    (("ble", "扫描"), ("startBleScanning ScanResult",)),
    (("显式", "隐式", "want"), ("显式Want 隐式Want 匹配规则",)),
    (("相机", "预览"), ("createCameraInput createPreviewOutput PhotoSession",)),
    (("相机", "拍照"), ("createPhotoOutput PhotoSession beginConfig commitConfig",)),
    (("stop receiving", "system broadcast"), ("CommonEventManager unsubscribe CommonEventSubscriber",)),
    (("镜头", "实时画面"), ("createCameraInput createPreviewOutput PhotoSession",)),
    (("低功耗", "外设"), ("startBleScanning ScanResult low energy device discovery",)),
    (("沙箱", "另一个应用"), ("沙箱 另一个应用 FileUri share app file Want",)),
    (("明确组件", "能力条件"), ("显式Want 隐式Want 匹配规则",)),
    (("canvas", "完全定型"), ("CanvasRenderingContext2D",)),
    (("canvas", "显式类型"), ("CanvasRenderingContext2D",)),
    (("foreach", "回调"), ("ItemGeneratorFunc KeyGeneratorFunc ForEach",)),
    (("foreach", "callback"), ("ItemGeneratorFunc KeyGeneratorFunc ForEach",)),
    (("@prop", "父子"), ("@Prop宏 父子单向同步 框架行为 初始渲染 更新",)),
    (("@builder", "bind"), ("bind CustomView ViewBuilder",)),
    (("builder", "绑定"), ("bind CustomView ViewBuilder",)),
)

# These agent-facing contract phrases have curated deterministic aliases with
# compiler-relevant signatures. Once they match, dense retrieval must not
# replace the precise lexical result with a broader conceptual neighbour.
DETERMINISTIC_CONTRACT_QUERY_TERMS = (
    ("canvas", "完全定型"),
    ("canvas", "显式类型"),
    ("foreach", "回调"),
    ("foreach", "callback"),
    ("@prop", "父子"),
    ("@builder", "bind"),
    ("builder", "绑定"),
    ("stop receiving", "system broadcast"),
    ("镜头", "实时画面"),
    ("低功耗", "外设"),
    ("沙箱", "另一个应用"),
    ("明确组件", "能力条件"),
)

# Dense nearest-neighbour search and permissive lexical fallback will always find
# *something*. Reject explicit competing ecosystems and clearly unrelated subject
# areas before either route. The topic groups require multiple independent clues,
# while a HarmonyOS marker wins for legitimate comparison/migration questions.
PLATFORM_MARKERS = (
    "harmonyos",
    "openharmony",
    "arkui",
    "arkts",
    "cangjie",
    "ohos",
    "仓颉",
    "鸿蒙",
)
FOREIGN_TECH_TERMS = (
    "angular",
    "borrow checker",
    "django",
    "docker",
    "flutter",
    "kubernetes",
    "postgresql",
    "redux",
    "ruby on rails",
    "spring boot",
    "swiftui",
    "terraform",
    "vue.js",
    "widgetkit",
)
UNRELATED_TOPIC_GROUPS = (
    ("bake", "bread", "cook", "oven", "recipe", "sourdough", "烘焙", "面包", "食谱", "烤箱"),
    ("calculus", "delta", "epsilon", "integral", "prove", "theorem", "定理", "微积分", "证明"),
    ("hotel", "itinerary", "kyoto", "temple", "tourist", "travel", "旅行", "行程", "酒店", "景点", "寺庙"),
    ("amortization", "loan", "mortgage", "monthly payment", "房贷", "摊销", "贷款", "月供"),
    ("compost", "fertilizer", "gardening", "soil", "tomato", "堆肥", "土壤", "园艺", "番茄"),
    ("basketball", "football", "league", "match score", "篮球", "足球", "联赛", "比分"),
    ("molecule", "titration", "chemical reaction", "laboratory reagent", "分子", "滴定", "化学反应", "试剂"),
)


@dataclass(slots=True)
class Candidate:
    section_id: int
    score: float = 0.0
    reasons: list[str] = field(default_factory=list)
    route_scores: dict[str, float] = field(default_factory=dict)

    def add(self, score: float, reason: str) -> None:
        previous = self.route_scores.get(reason, 0.0)
        if score > previous:
            self.score += score - previous
            self.route_scores[reason] = score
        if reason not in self.reasons:
            self.reasons.append(reason)


class Searcher:
    def __init__(self, cfg: AppConfig) -> None:
        self.cfg = cfg
        self.con = connect(Path(cfg.index_path))
        init_db(self.con)
        self.embedding = EmbeddingService(cfg)
        self.vector_cache = None
        if cfg.search_embeddings and self.embedding.available:
            try:
                self.vector_cache = VectorCache(Path(cfg.vector_cache_path))
            except (OSError, sqlite3.Error):
                self.vector_cache = None

    def close(self) -> None:
        if self.vector_cache:
            self.vector_cache.close()
        self.con.close()

    def __enter__(self) -> "Searcher":
        return self

    def __exit__(self, exc_type: object, exc: object, tb: object) -> None:
        self.close()

    def status(self) -> dict[str, Any]:
        manifest = self.con.execute("select value from metadata where key='manifest'").fetchone()
        totals = self._totals()
        vector_count = totals["vectors"]
        version = normalize_query_version(self.cfg.docs_version)
        version_sql, version_params = version_where("r", version)
        version_vector_count = self.con.execute(
            f"select count(*) c from vectors r where 1 = 1 {version_sql}",
            version_params,
        ).fetchone()["c"]
        embedding_configured = bool(self.embedding and self.embedding.available)
        mode = "deterministic-only"
        if self.cfg.search_embeddings and embedding_configured:
            mode = "embedding-search" if version_vector_count else "embedding-degraded"
        return {
            "ok": True,
            "mode": mode,
            "index_path": str(Path(self.cfg.index_path)),
            "default_version": self.cfg.docs_version,
            "versions": self.versions(),
            "embedding_mode": self.cfg.embedding_mode,
            "embedding_configured": embedding_configured,
            **totals,
            "version_vectors": version_vector_count,
            "manifest": json_loads(manifest["value"], {}) if manifest else None,
        }

    def versions(self) -> list[dict[str, Any]]:
        rows = self.con.execute(
            """
            select
              v.version,
              v.docs_root,
              v.display_name,
              v.status,
              (select count(*) from documents d where d.version = v.version) documents,
              (select count(*) from sections s where s.version = v.version) sections,
              (select count(*) from symbols y where y.version = v.version) symbols,
              (select count(*) from examples e where e.version = v.version) examples,
              (select count(*) from vectors r where r.version = v.version) vectors,
              v.created_at,
              v.updated_at
            from versions v
            where v.status = 'ready'
            order by case when version = ? then 0 else 1 end, updated_at desc, version
            """,
            (self.cfg.docs_version,),
        ).fetchall()
        if rows:
            return [dict(row) for row in rows]
        return []

    def _totals(self) -> dict[str, int]:
        row = self.con.execute(
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

    def search(
        self,
        query: str,
        *,
        top_k: int = 8,
        scope: str = "all",
        embedding_mode: str | None = None,
        version: str | None = None,
    ) -> list[dict[str, Any]]:
        query = (query or "").strip()
        if not query or is_explicitly_out_of_domain(query):
            return []
        version_filter = normalize_query_version(version if version is not None else self.cfg.docs_version)
        if not self._has_active_version(version_filter):
            return []
        runtime_embeddings = self._runtime_embeddings_enabled(embedding_mode)
        semantic_queries = semantic_aliases(query)
        queries = [query, *semantic_queries[:3]]

        candidates: dict[int, Candidate] = {}
        for idx, q in enumerate(queries):
            weight = 1.0 if idx == 0 else (0.86 if q in semantic_queries else 0.62)
            self._symbol_candidates(candidates, q, scope, weight, version_filter)
            self._fts_candidates(candidates, q, scope, weight, version_filter)
            if idx == 0 and scope in {"all", "examples"}:
                self._example_candidates(candidates, q, weight, version_filter)

        self._numeric_candidates(candidates, query, scope, version_filter)
        self._structural_seed_candidates(candidates, query, scope, version_filter)
        self._coverage_candidates(candidates, query, scope, version_filter)
        # Curated aliases encode API-bearing phrases for agent paraphrases. Run
        # the same term-coverage route as the original query; limiting this to
        # two keeps deterministic latency bounded while allowing guide titles
        # such as ``@Prop宏:父子单向同步`` to outrank generic ``prop``
        # symbols.
        for semantic_query in semantic_queries[:2]:
            self._coverage_candidates(candidates, semantic_query, scope, version_filter)
        if len(candidates) < 120:
            fallback_queries = [query, *semantic_queries[:2]]
            for idx, fallback_query in enumerate(fallback_queries):
                self._substring_candidates(
                    candidates,
                    fallback_query,
                    scope,
                    0.75 if idx else 1.0,
                    version_filter,
                )

        if len(candidates) > 800:
            keep = {
                item.section_id
                for item in sorted(candidates.values(), key=lambda item: item.score, reverse=True)[:800]
            }
            candidates = {section_id: item for section_id, item in candidates.items() if section_id in keep}

        self._drop_inactive_candidates(candidates)
        rows = self._section_rows(candidates)
        self._quality_adjustments(candidates, query, rows)
        ordered = sorted(candidates.values(), key=lambda item: item.score, reverse=True)
        lexical_score = ordered[0].score if ordered else 0.0
        vector_route = (
            runtime_embeddings
            and self.embedding.available
            and lexical_score < LEXICAL_ROUTE_MIN_SCORE
            and not matches_deterministic_contract_query(query)
            and self._has_vector_index(scope, version_filter)
        )
        if vector_route:
            if is_probably_random_identifier(query) or self._has_unknown_technical_identifier(query):
                return []
            try:
                vector_results = self._vector_candidates(query, scope, version_filter)
            except Exception:
                vector_results = None
            if vector_results is not None:
                if not vector_results:
                    return []
                return self._hydrate_vector_results(query, vector_results, top_k)

        selected = ordered[: max(top_k, 1)]
        symbols = self._symbols_by_section([item.section_id for item in selected])
        return [
            self._hydrate_candidate(item, query, rows[item.section_id], symbols.get(item.section_id, []))
            for item in selected
            if item.section_id in rows
        ]

    def vector_search(
        self,
        query: str,
        *,
        top_k: int = 8,
        scope: str = "all",
        version: str | None = None,
    ) -> list[dict[str, Any]]:
        """Return pure dense-retrieval results for evaluation and diagnostics."""

        query = (query or "").strip()
        if (
            not query
            or not self.embedding.available
            or is_explicitly_out_of_domain(query)
        ):
            return []
        version_filter = normalize_query_version(version if version is not None else self.cfg.docs_version)
        if not self._has_active_version(version_filter):
            return []
        if not self._has_vector_index(scope, version_filter):
            return []
        try:
            vector_results = self._vector_candidates(query, scope, version_filter)
        except Exception:
            return []
        return self._hydrate_vector_results(query, vector_results, top_k)

    def _hydrate_vector_results(
        self,
        query: str,
        vector_results: list[tuple[int, float]],
        top_k: int,
    ) -> list[dict[str, Any]]:
        selected = vector_results[: max(1, top_k)]
        rows = self._section_rows({section_id: Candidate(section_id) for section_id, _ in selected})
        symbols = self._symbols_by_section([section_id for section_id, _ in selected])
        results: list[dict[str, Any]] = []
        for section_id, similarity in selected:
            row = rows.get(section_id)
            if not row:
                continue
            candidate = Candidate(section_id)
            candidate.add(similarity * 100.0, "vector")
            candidate.add(0.0, "semantic-route")
            results.append(self._hydrate_candidate(candidate, query, row, symbols.get(section_id, [])))
        return results

    def _section_rows(self, candidates: dict[int, Candidate]) -> dict[int, sqlite3.Row]:
        result: dict[int, sqlite3.Row] = {}
        ids = list(candidates)
        for start in range(0, len(ids), 500):
            chunk = ids[start : start + 500]
            placeholders = ",".join("?" for _ in chunk)
            rows = self.con.execute(f"select * from sections where id in ({placeholders})", chunk).fetchall()
            result.update((int(row["id"]), row) for row in rows)
        return result

    def _symbols_by_section(self, section_ids: list[int]) -> dict[int, list[dict[str, Any]]]:
        if not section_ids:
            return {}
        placeholders = ",".join("?" for _ in section_ids)
        rows = self.con.execute(
            f"""
            select section_id, name, kind, signature
            from symbols
            where section_id in ({placeholders})
            order by section_id, id
            """,
            section_ids,
        ).fetchall()
        result: dict[int, list[dict[str, Any]]] = {}
        for row in rows:
            bucket = result.setdefault(int(row["section_id"]), [])
            if len(bucket) < 10:
                bucket.append({key: row[key] for key in ("name", "kind", "signature")})
        return result

    def _has_active_version(self, version: str | None) -> bool:
        if version:
            row = self.con.execute("select 1 from versions where version = ? and status = 'ready' limit 1", (version,)).fetchone()
        else:
            row = self.con.execute("select 1 from versions where status = 'ready' limit 1").fetchone()
        return bool(row)

    def _has_vector_index(self, scope: str, version: str | None) -> bool:
        clauses = ["v.provider = ?", "v.model = ?"]
        params: list[Any] = [self.cfg.embedding.api_format, self.cfg.embedding.model]
        if scope in {"api", "guide"}:
            clauses.append("s.doc_type = ?")
            params.append(scope)
        version_sql, version_params = version_where("s", version)
        params.extend(version_params)
        row = self.con.execute(
            f"""
            select 1 from vectors v join sections s on s.id = v.section_id
            where {' and '.join(clauses)} {version_sql}
            limit 1
            """,
            params,
        ).fetchone()
        return bool(row)

    def _has_unknown_technical_identifier(self, query: str) -> bool:
        """Recognize explicit foreign/unknown technology names before dense fallback.

        Dense nearest-neighbor search always returns a neighbor. A distinctive
        identifier that never occurs in the corpus is therefore strong evidence
        that a weak lexical query belongs to another technical ecosystem.
        """

        for match in TECHNICAL_IDENTIFIER_RE.finditer(query):
            token = match.group(0)
            has_internal_upper = any(char.isupper() for char in token[1:])
            is_mid_sentence_name = match.start() > 0 and token[0].isupper() and len(token) >= 4
            if not ("_" in token or has_internal_upper or is_mid_sentence_name):
                continue
            normalized = normalize_symbol(token)
            symbol = self.con.execute(
                "select 1 from symbols where normalized = ? limit 1",
                (normalized,),
            ).fetchone()
            if symbol:
                continue
            fts_query = make_fts_query(token)
            if fts_query:
                section = self.con.execute(
                    """
                    select 1
                    from fts_sections_lex
                    join sections s on s.id = fts_sections_lex.rowid
                    join versions v on v.version = s.version and v.status = 'ready'
                    where fts_sections_lex match ?
                    limit 1
                    """,
                    (fts_query,),
                ).fetchone()
                if section:
                    continue
            return True
        return False

    def _drop_inactive_candidates(self, candidates: dict[int, Candidate]) -> None:
        if not candidates:
            return
        ids = list(candidates)
        active: set[int] = set()
        for start in range(0, len(ids), 500):
            chunk = ids[start : start + 500]
            placeholders = ",".join("?" for _ in chunk)
            rows = self.con.execute(
                f"""
                select s.id
                from sections s
                join versions v on v.version = s.version and v.status = 'ready'
                where s.id in ({placeholders})
                """,
                chunk,
            ).fetchall()
            active.update(int(row["id"]) for row in rows)
        for section_id in ids:
            if section_id not in active:
                candidates.pop(section_id, None)

    def lookup_symbol(self, name: str, *, include_members: bool = True, include_examples: bool = True, version: str | None = None) -> dict[str, Any] | None:
        norm = normalize_symbol(name)
        version_filter = normalize_query_version(version if version is not None else self.cfg.docs_version)
        version_sql, version_params = version_where("s", version_filter)
        row = self.con.execute(
            f"""
            select s.*, sec.body, sec.breadcrumb, sec.kit, sec.doc_type
            from symbols s join sections sec on sec.id = s.section_id
            where s.normalized = ? {version_sql}
            order by case when s.name = ? then 0 else 1 end, length(s.name)
            limit 1
            """,
            (norm, *version_params, name),
        ).fetchone()
        if not row:
            rows = self.con.execute(
                f"""
                select s.*, sec.body, sec.breadcrumb, sec.kit, sec.doc_type
                from symbols s join sections sec on sec.id = s.section_id
                where s.normalized like ? {version_sql}
                order by length(s.name)
                limit 1
                """,
                (f"%{norm}%", *version_params),
            ).fetchall()
            row = rows[0] if rows else None
        if not row:
            return None
        result = dict(row)
        result["ref"] = f"{row['path']}#{row['anchor']}"
        result["members"] = []
        result["examples"] = []
        if include_members:
            member_version = row["version"] if version_filter is None else version_filter
            result["members"] = [
                dict(item)
                for item in self.con.execute(
                    """
                    select name, kind, signature, path, anchor, start_line, end_line
                    from symbols
                    where parent = ? and id != ? and (? is null or version = ?)
                    order by start_line
                    limit 80
                    """,
                    (row["name"], row["id"], member_version, member_version),
                ).fetchall()
            ]
        if include_examples:
            result["examples"] = self.find_examples(row["name"], top_k=5, version=row["version"] if version_filter is None else version_filter)
        return result

    def read_doc(self, ref: str, *, mode: str = "section", max_chars: int = 12000, version: str | None = None) -> dict[str, Any] | None:
        path, anchor = split_ref(ref)
        version_filter = normalize_query_version(version if version is not None else self.cfg.docs_version)
        version_sql, version_params = version_where("s", version_filter)
        if mode == "full" or not anchor:
            rows = self.con.execute(
                f"""
                select s.title, s.version, s.path, s.start_line, s.end_line, s.body
                from sections s
                where s.path = ? {version_sql}
                order by s.start_line
                """,
                (path, *version_params),
            ).fetchall()
            if not rows:
                return None
            if version_filter is None:
                chosen_version = rows[0]["version"]
                rows = [row for row in rows if row["version"] == chosen_version]
            text = "\n\n".join(row["body"] for row in rows)
            return {
                "path": path,
                "version": rows[0]["version"],
                "title": rows[0]["title"],
                "start_line": rows[0]["start_line"],
                "end_line": rows[-1]["end_line"],
                "content": text[:max_chars],
                "truncated": len(text) > max_chars,
            }
        row = self.con.execute(
            f"select s.* from sections s where s.path = ? and s.anchor = ? {version_sql} limit 1",
            (path, anchor, *version_params),
        ).fetchone()
        if not row:
            return None
        body = row["body"]
        return {
            "path": row["path"],
            "version": row["version"],
            "title": row["title"],
            "breadcrumb": row["breadcrumb"],
            "anchor": row["anchor"],
            "start_line": row["start_line"],
            "end_line": row["end_line"],
            "content": body[:max_chars],
            "truncated": len(body) > max_chars,
        }

    def find_examples(self, query_or_symbol: str, *, top_k: int = 5, version: str | None = None) -> list[dict[str, Any]]:
        version_filter = normalize_query_version(version if version is not None else self.cfg.docs_version)
        version_sql, version_params = version_where("e", version_filter)
        terms = make_fts_query(query_or_symbol)
        rows: list[sqlite3.Row] = []
        if terms:
            try:
                rows = self.con.execute(
                    f"""
                    select e.*, bm25(fts_examples) rank
                    from fts_examples join examples e on e.id = fts_examples.rowid
                    where fts_examples match ? {version_sql}
                    order by rank limit ?
                    """,
                    (terms, *version_params, top_k),
                ).fetchall()
            except sqlite3.OperationalError:
                rows = []
        if not rows:
            rows = self.con.execute(
                f"""
                select e.* from examples e
                where (e.code like ? or e.nearby_symbol like ? or e.imports like ?) {version_sql}
                order by e.start_line limit ?
                """,
                (f"%{query_or_symbol}%", f"%{query_or_symbol}%", f"%{query_or_symbol}%", *version_params, top_k),
            ).fetchall()
        return [
            {
                "path": row["path"],
                "version": row["version"],
                "anchor": row["anchor"],
                "ref": f"{row['path']}#{row['anchor']}",
                "start_line": row["start_line"],
                "end_line": row["end_line"],
                "language": row["language"],
                "imports": json_loads(row["imports"], []),
                "nearby_symbol": row["nearby_symbol"],
                "code": row["code"][:3000],
            }
            for row in rows
        ]

    def related_docs(self, ref: str, *, top_k: int = 8, version: str | None = None) -> list[dict[str, Any]]:
        path, anchor = split_ref(ref)
        version_filter = normalize_query_version(version if version is not None else self.cfg.docs_version)
        version_sql, version_params = version_where("s", version_filter)
        sec = self.con.execute(
            f"select s.* from sections s where s.path = ? and s.anchor = ? {version_sql} limit 1",
            (path, anchor, *version_params),
        ).fetchone()
        if not sec:
            return []
        root = self.con.execute(
            "select min(start_line) from sections where version = ? and path = ?",
            (sec["version"], path),
        ).fetchone()[0]
        outgoing = self.con.execute(
            """
            select s.*
            from links l join sections s on s.id = (
              select target.id from sections target
              where target.version = l.version and target.path = l.target_path
                and (l.target_anchor is null or target.anchor = l.target_anchor)
              order by target.start_line limit 1
            )
            where l.version = ? and l.section_id = ? and l.target_path is not null
            order by case when s.kit = ? then 0 else 1 end, l.line
            limit ?
            """,
            (sec["version"], sec["id"], sec["kit"], top_k),
        ).fetchall()
        incoming = self.con.execute(
            """
            select source.*
            from links l join sections source on source.id = l.section_id
            where l.version = ? and l.target_path = ?
              and (l.target_anchor = ? or (? and l.target_anchor is null))
            order by case when source.kit = ? then 0 else 1 end, l.line
            limit ?
            """,
            (sec["version"], path, anchor, int(sec["start_line"] == root), sec["kit"], top_k),
        ).fetchall()
        results: list[dict[str, Any]] = []
        seen = {int(sec["id"])}
        for reason, rows in (("related-outgoing", outgoing), ("related-incoming", incoming)):
            for row in rows:
                section_id = int(row["id"])
                if section_id in seen:
                    continue
                seen.add(section_id)
                results.append(section_to_result(row, 0.0, [reason]))
                if len(results) >= top_k:
                    return results
        return results

    def _runtime_embeddings_enabled(self, mode: str | None) -> bool:
        if mode == "off":
            return False
        if mode in {EMBEDDING_SEARCH, EMBEDDING_ALL}:
            return bool(self.embedding)
        return bool(self.cfg.search_embeddings and self.embedding)

    def _candidate(self, candidates: dict[int, Candidate], section_id: int) -> Candidate:
        if section_id not in candidates:
            candidates[section_id] = Candidate(section_id)
        return candidates[section_id]

    def _symbol_candidates(self, candidates: dict[int, Candidate], query: str, scope: str, weight: float, version: str | None) -> None:
        if scope not in {"all", "api"}:
            return
        version_sql, version_params = version_where("s", version)
        terms: list[tuple[str, str]] = []
        for term in [query, *fallback_terms(query)]:
            norm = normalize_symbol(term)
            if not norm or any(item[0] == norm for item in terms):
                continue
            terms.append((norm, term))
            if len(terms) >= 8:
                break
        if not terms:
            return
        clauses: list[str] = []
        params: list[Any] = []
        for norm, term in terms:
            clauses.append("(s.normalized = ? or s.normalized like ? or s.name like ?)")
            params.extend((norm, f"{norm}%", f"%{term}%"))
        rows = self.con.execute(
            f"""
            select s.section_id, s.name, s.normalized from symbols s
            where ({' or '.join(clauses)}) {version_sql}
            limit 100
            """,
            (*params, *version_params),
        ).fetchall()
        for row in rows:
            matched_scores = []
            for norm, _ in terms:
                if row["normalized"] == norm:
                    matched_scores.append(120.0)
                elif row["normalized"].startswith(norm):
                    matched_scores.append(85.0)
                elif norm in row["normalized"]:
                    matched_scores.append(55.0)
            if matched_scores:
                self._candidate(candidates, row["section_id"]).add(max(matched_scores) * weight, "symbol")

    def _fts_candidates(self, candidates: dict[int, Candidate], query: str, scope: str, weight: float, version: str | None) -> None:
        if scope == "examples":
            return
        doc_filter = ""
        params_tail: list[Any] = []
        if scope in {"api", "guide"}:
            doc_filter = " and s.doc_type = ?"
            params_tail.append(scope)
        version_sql, version_params = version_where("s", version)
        doc_filter += version_sql
        params_tail.extend(version_params)
        lex = make_fts_query(query)
        if lex:
            try:
                rows = self.con.execute(
                    f"""
                    select s.id, bm25(fts_sections_lex, 4.0, 2.0, 1.0) rank
                    from fts_sections_lex join sections s on s.id = fts_sections_lex.rowid
                    where fts_sections_lex match ? {doc_filter}
                    order by rank limit 80
                    """,
                    [lex, *params_tail],
                ).fetchall()
                for row in rows:
                    self._candidate(candidates, row["id"]).add((35.0 / (1.0 + abs(row["rank"]))) * weight, "fts")
            except sqlite3.OperationalError:
                pass
        tri = make_trigram_query(query)
        if tri:
            try:
                rows = self.con.execute(
                    f"""
                    select s.id, bm25(fts_sections_tri, 4.0, 2.0, 1.0) rank
                    from fts_sections_tri join sections s on s.id = fts_sections_tri.rowid
                    where fts_sections_tri match ? {doc_filter}
                    order by rank limit 80
                    """,
                    [tri, *params_tail],
                ).fetchall()
                for row in rows:
                    self._candidate(candidates, row["id"]).add((42.0 / (1.0 + abs(row["rank"]))) * weight, "trigram")
            except sqlite3.OperationalError:
                pass

    def _substring_candidates(self, candidates: dict[int, Candidate], query: str, scope: str, weight: float, version: str | None) -> None:
        tokens = fallback_terms(query)
        if not tokens:
            return
        clauses = []
        params: list[Any] = []
        for token in tokens[:4]:
            like = f"%{token}%"
            clauses.append("(title like ? or breadcrumb like ? or body like ?)")
            params.extend([like, like, like])
        doc_filter = ""
        if scope in {"api", "guide"}:
            doc_filter = " and s.doc_type = ?"
            params.append(scope)
        version_sql, version_params = version_where("s", version)
        doc_filter += version_sql
        params.extend(version_params)
        rows = self.con.execute(
            f"""
            select s.id, s.title, s.breadcrumb from sections s
            where ({' or '.join(clauses)}) {doc_filter}
            limit 100
            """,
            params,
        ).fetchall()
        for row in rows:
            score = 18.0
            lowered = (row["title"] + " " + row["breadcrumb"]).lower()
            if query.lower() in lowered:
                score += 20.0
            self._candidate(candidates, row["id"]).add(score * weight, "substring")

    def _example_candidates(self, candidates: dict[int, Candidate], query: str, weight: float, version: str | None) -> None:
        version_sql, version_params = version_where("e", version)
        terms = make_fts_query(query)
        rows: list[sqlite3.Row] = []
        if terms:
            try:
                rows = self.con.execute(
                    f"""
                    select e.section_id, bm25(fts_examples) rank
                    from fts_examples join examples e on e.id = fts_examples.rowid
                    where fts_examples match ? {version_sql}
                    order by rank limit 30
                    """,
                    (terms, *version_params),
                ).fetchall()
            except sqlite3.OperationalError:
                rows = []
        if not rows:
            like = f"%{query}%"
            rows = self.con.execute(
                f"""
                select e.section_id
                from examples e
                where (e.code like ? or e.imports like ? or e.nearby_symbol like ?) {version_sql}
                limit 30
                """,
                (like, like, like, *version_params),
            ).fetchall()
        for rank, row in enumerate(rows, 1):
            self._candidate(candidates, row["section_id"]).add((28.0 / rank) * weight, "example")

    def _numeric_candidates(self, candidates: dict[int, Candidate], query: str, scope: str, version: str | None) -> None:
        numbers = [item for item in re.findall(r"\d{5,}", query) if item]
        if not numbers:
            return
        doc_filter = ""
        params_tail: list[Any] = []
        if scope in {"api", "guide"}:
            doc_filter = " and doc_type = ?"
            params_tail.append(scope)
        version_sql, version_params = version_where("", version)
        doc_filter += version_sql
        params_tail.extend(version_params)
        for number in numbers[:4]:
            rows = self.con.execute(
                f"""
                select id, title, breadcrumb, path, anchor, body
                from sections
                where (title like ? or breadcrumb like ? or anchor like ? or body like ?) {doc_filter}
                limit 120
                """,
                [f"%{number}%", f"%{number}%", f"%{number}%", f"%{number}%", *params_tail],
            ).fetchall()
            for row in rows:
                score = 140.0
                if number in (row["title"] or "") or number in (row["anchor"] or ""):
                    score += 110.0
                if "errorcode" in (row["path"] or "").lower():
                    score += 80.0
                self._candidate(candidates, row["id"]).add(score, "number-exact")

    def _structural_seed_candidates(self, candidates: dict[int, Candidate], query: str, scope: str, version: str | None) -> None:
        intents = detect_intents(query)
        if not (intents & {"howto", "limit", "lifecycle", "config", "transfer", "permission", "logging"}):
            return
        clauses = []
        params: list[Any] = []
        seed_terms = structural_seed_terms(query, intents)
        for term in seed_terms[:10]:
            clauses.append("(title like ? or breadcrumb like ? or body like ?)")
            like = f"%{term}%"
            params.extend([like, like, like])
        if not clauses:
            return
        doc_filter = ""
        if scope in {"api", "guide"}:
            doc_filter = " and s.doc_type = ?"
            params.append(scope)
        elif "howto" in intents:
            doc_filter = " and s.doc_type in ('guide', 'api')"
        version_sql, version_params = version_where("s", version)
        doc_filter += version_sql
        params.extend(version_params)
        rows = self.con.execute(
            f"""
            select s.id, s.path, s.title, s.breadcrumb, s.doc_type
            from sections s
            where ({' or '.join(clauses)}) {doc_filter}
            order by s.start_line
            limit 160
            """,
            params,
        ).fetchall()
        for row in rows:
            score = 28.0
            focused_l = f"{row['title']} {row['breadcrumb']}".lower()
            if row["doc_type"] == "guide" and "howto" in intents:
                score += 35.0
            if contains_any(focused_l, GUIDE_HEADING_TERMS):
                score += 35.0
            if query.lower() in focused_l:
                score += 35.0
            self._candidate(candidates, row["id"]).add(score, "structure-seed")

    def _coverage_candidates(self, candidates: dict[int, Candidate], query: str, scope: str, version: str | None) -> None:
        terms = informative_query_terms(query)
        if len(terms) < 2:
            return
        clauses = []
        params: list[Any] = []
        for term in terms[:8]:
            clauses.append("(title like ? or breadcrumb like ? or body like ?)")
            like = f"%{term}%"
            params.extend([like, like, like])
        doc_filter = ""
        if scope in {"api", "guide"}:
            doc_filter = " and s.doc_type = ?"
            params.append(scope)
        version_sql, version_params = version_where("s", version)
        doc_filter += version_sql
        params.extend(version_params)
        rows = self.con.execute(
            f"""
            select s.id, s.title, s.breadcrumb, s.body
            from sections s
            where ({' or '.join(clauses)}) {doc_filter}
            limit 360
            """,
            params,
        ).fetchall()
        total_weight = sum(term_weight(term) for term in terms[:8]) or 1.0
        for row in rows:
            haystack = f"{row['title']}\n{row['breadcrumb']}\n{row['body'][:5000]}".lower()
            focused = f"{row['title']}\n{row['breadcrumb']}".lower()
            matched = [term for term in terms[:8] if term.lower() in haystack]
            if not matched:
                continue
            match_weight = sum(term_weight(term) for term in matched)
            coverage = match_weight / total_weight
            score = 18.0 + (90.0 * coverage)
            if len(matched) >= 2:
                score += 35.0
            focused_matched = [term for term in matched if term.lower() in focused]
            if focused_matched:
                score += 35.0 * (sum(term_weight(term) for term in focused_matched) / total_weight)
            if query.lower() in haystack:
                score += 45.0
            self._candidate(candidates, row["id"]).add(score, "term-coverage")

    def _vector_candidates(self, query: str, scope: str, version: str | None) -> list[tuple[int, float]]:
        if not self.embedding:
            return []
        qvec = self._embed_runtime_query(query)
        if not qvec:
            return []
        doc_filter = ""
        params: list[Any] = [self.cfg.embedding.api_format, self.cfg.embedding.model]
        if scope in {"api", "guide"}:
            doc_filter = " and s.doc_type = ?"
            params.append(scope)
        version_sql, version_params = version_where("s", version)
        doc_filter += version_sql
        params.extend(version_params)
        rows = self.con.execute(
            f"""
            select v.section_id, v.vector_blob
            from vectors v join sections s on s.id = v.section_id
            where v.provider = ? and v.model = ? {doc_filter}
            """,
            params,
        ).fetchall()
        scored: list[tuple[int, float]] = []
        for row in rows:
            vec = unpack_vector(row["vector_blob"])
            sim = cosine(qvec, vec)
            if sim >= self.cfg.embedding.min_similarity:
                scored.append((row["section_id"], sim))
        return sorted(scored, key=lambda item: item[1], reverse=True)[:50]

    def _embed_runtime_query(self, query: str) -> list[float]:
        if not self.embedding:
            return []
        cache_text = f"query:{query}"
        if self.vector_cache:
            cached = self.vector_cache.get(
                provider=self.cfg.embedding.api_format,
                model=self.cfg.embedding.model,
                text=cache_text,
                endpoint=self.cfg.embedding.base_url,
                requested_dimensions=self.cfg.embedding.dimensions,
            )
            if cached:
                return cached.vector
        vector = self.embedding.embed_query(query)
        if vector and self.vector_cache:
            self.vector_cache.put(
                provider=self.cfg.embedding.api_format,
                model=self.cfg.embedding.model,
                text=cache_text,
                vector=vector,
                endpoint=self.cfg.embedding.base_url,
                requested_dimensions=self.cfg.embedding.dimensions,
            )
        return vector

    def _quality_adjustments(
        self,
        candidates: dict[int, Candidate],
        query: str,
        rows: dict[int, sqlite3.Row],
    ) -> None:
        query_l = query.lower().strip()
        terms = [term.lower() for term in fallback_terms(query) if len(term.strip()) >= 2]
        informative = informative_query_terms(query)
        informative_total = sum(term_weight(term) for term in informative[:8]) or 0.0
        raw_identifiers = [item for item in ASCII_TOKEN_RE.findall(query) if len(item) >= 3 and not item.isdigit()]
        identifiers = [item.lower() for item in raw_identifiers]
        api_focus_identifiers = [
            item.lower()
            for item in raw_identifiers
            if "_" in item or any(char.isupper() for char in item[1:])
        ]
        numeric = query_l.isdigit() and len(query_l) >= 5
        intents = detect_intents(query)
        howto = is_howto_query(query)
        numbers = re.findall(r"\d{5,}", query)
        for candidate in list(candidates.values()):
            row = rows.get(candidate.section_id)
            if not row:
                continue
            title_l = row["title"].lower()
            breadcrumb_l = row["breadcrumb"].lower()
            path_l = row["path"].lower()
            body_l = row["body"].lower()
            haystack_l = f"{title_l}\n{breadcrumb_l}\n{body_l[:5000]}"
            if numbers and any(number in haystack_l for number in numbers):
                candidate.add(160.0 if "errorcode" in path_l else 90.0, "number-match")
            if query_l and title_l == query_l:
                candidate.add(90.0, "exact-title")
            elif query_l and title_l.startswith(query_l):
                candidate.add(70.0 if numeric else 35.0, "title-prefix")
            elif query_l and query_l in title_l:
                candidate.add(38.0 if numeric else 22.0, "title-contains")
            if query_l and query_l in breadcrumb_l:
                candidate.add(12.0, "breadcrumb")
            action_matches = [
                term
                for term in FOCUSED_ACTION_TERMS
                if term in query and term in f"{title_l}\n{breadcrumb_l}"
            ]
            if action_matches:
                candidate.add(140.0 + 10.0 * (len(action_matches) - 1), "focused-action")
            if howto and row["doc_type"] == "guide":
                candidate.add(34.0, "guide-intent")
                guide_focus = f"{title_l}\n{breadcrumb_l}"
                guide_terms = [term for term in informative[:8] if term.lower() in guide_focus]
                if len(guide_terms) >= 2:
                    candidate.add(80.0 + min(len(guide_terms), 4) * 10.0, "guide-title-coverage")
            self._intent_boost(candidate, row, intents)
            if "camera" in intents and "/camera/" not in path_l and row["kit"].lower() != "camerakit":
                candidate.score *= 0.35
                candidate.reasons.append("camera-domain-downrank")
            if identifiers:
                matched_ids = [item for item in identifiers if identifier_in_text(item, haystack_l)]
                focused_ids = [item for item in matched_ids if identifier_in_text(item, f"{title_l}\n{breadcrumb_l}")]
                if len(set(matched_ids)) == len(set(identifiers)):
                    candidate.add(95.0, "identifier-match")
                elif matched_ids:
                    candidate.add(35.0, "partial-identifier-match")
                elif not {"symbol", "number-exact", "vector"} & set(candidate.reasons):
                    candidate.score *= 0.72
                    candidate.reasons.append("identifier-miss-downrank")
                if focused_ids:
                    candidate.add(35.0, "focused-identifier-match")
            if api_focus_identifiers:
                api_focus = f"{title_l}\n{breadcrumb_l}\n{path_l}"
                focus_matches = [item for item in api_focus_identifiers if identifier_in_text(item, api_focus)]
                if len(set(focus_matches)) == len(set(api_focus_identifiers)):
                    candidate.add(180.0, "api-focus-match")
                elif focus_matches:
                    candidate.add(30.0, "partial-api-focus-match")
                elif not (
                    howto
                    and row["doc_type"] == "guide"
                    and any(identifier_in_text(item, haystack_l) for item in api_focus_identifiers)
                ) and not {"symbol", "number-exact", "vector"} & set(candidate.reasons):
                    candidate.score *= 0.55
                    candidate.reasons.append("api-focus-miss-downrank")
            if informative_total:
                focused = f"{title_l}\n{breadcrumb_l}"
                matched = [term for term in informative[:8] if term.lower() in haystack_l]
                focused_matched = [term for term in matched if term.lower() in focused]
                coverage = sum(term_weight(term) for term in matched) / informative_total
                focused_coverage = sum(term_weight(term) for term in focused_matched) / informative_total
                if coverage >= 0.85:
                    candidate.add(95.0, "high-term-coverage")
                elif coverage >= 0.55:
                    candidate.add(55.0, "term-coverage")
                elif coverage >= 0.3:
                    candidate.add(20.0, "partial-term-coverage")
                if focused_coverage >= 0.45:
                    candidate.add(45.0, "focused-term-coverage")
                if coverage < 0.22 and not {"symbol", "number-exact", "vector"} & set(candidate.reasons):
                    candidate.score *= 0.62
                    candidate.reasons.append("low-coverage-downrank")
            if len(terms) >= 2:
                matched = sum(1 for term in terms[:5] if term in haystack_l)
                if matched == min(len(terms), 5):
                    candidate.add(36.0, "all-terms")
                elif matched >= 2:
                    candidate.add(12.0, "multi-term")
                focused = f"{title_l}\n{breadcrumb_l}"
                focused_matches = sum(1 for term in terms[:5] if term in focused)
                if focused_matches >= 2:
                    candidate.add(24.0, "focused-terms")
            # Top-level generated table-of-contents pages are useful, but should not outrank
            # focused content pages for ordinary topic searches.
            if row["path"].endswith("/website.md") and query_l not in title_l:
                candidate.score *= 0.35
                candidate.reasons.append("toc-downrank")
            if (row["end_line"] - row["start_line"]) > 650 and query_l not in title_l:
                candidate.score *= 0.75

    def _intent_boost(self, candidate: Candidate, row: sqlite3.Row, intents: set[str]) -> None:
        if not intents:
            return
        title_l = row["title"].lower()
        breadcrumb_l = row["breadcrumb"].lower()
        path_l = row["path"].lower()
        body_l = row["body"][:6000].lower()
        focused = f"{title_l}\n{breadcrumb_l}"
        haystack = f"{focused}\n{path_l}\n{body_l}"

        guide_like = row["doc_type"] == "guide" or contains_any(focused, GUIDE_HEADING_TERMS)
        if "howto" in intents:
            if guide_like:
                candidate.add(45.0, "intent-howto-guide")
            if contains_any(focused, GUIDE_HEADING_TERMS):
                candidate.add(55.0, "intent-howto-heading")
        if "error_code" in intents and contains_any(haystack, ERROR_TERMS):
            candidate.add(90.0, "intent-error")
        if "limit" in intents and (contains_any(haystack, LIMIT_TERMS) or UNIT_RE.search(haystack)):
            candidate.add(95.0, "intent-limit")
        if "lifecycle" in intents and contains_any(haystack, LIFECYCLE_TERMS):
            candidate.add(105.0, "intent-lifecycle")
        if "config" in intents and contains_any(haystack, CONFIG_TERMS):
            candidate.add(80.0, "intent-config")
        if "transfer" in intents and contains_any(haystack, TRANSFER_TERMS):
            candidate.add(85.0, "intent-transfer")
        if "permission" in intents and contains_any(haystack, PERMISSION_TERMS):
            candidate.add(85.0, "intent-permission")
        if "logging" in intents and contains_any(haystack, LOG_TERMS):
            candidate.add(80.0, "intent-logging")
        if "camera" in intents:
            if "/camera/" in path_l or row["kit"].lower() == "camerakit":
                candidate.add(120.0, "intent-camera")
            if "camera-session-management" in path_l:
                candidate.add(180.0, "intent-camera-workflow")
            if any(symbol in haystack for symbol in ("createpreviewoutput", "createphotooutput", "photosession")):
                candidate.add(120.0, "intent-camera-api")

        if guide_like and intents & {"howto", "config", "transfer", "permission", "logging", "lifecycle"}:
            candidate.add(25.0, "workflow-guide")

    def _hydrate_candidate(
        self,
        candidate: Candidate,
        query: str,
        row: sqlite3.Row,
        symbols: list[dict[str, Any]],
    ) -> dict[str, Any]:
        result = section_to_result(row, candidate.score, candidate.reasons)
        result["snippet"] = make_snippet(row["body"], query)
        result["symbols"] = symbols
        return result


def section_to_result(row: sqlite3.Row, score: float, reasons: list[str]) -> dict[str, Any]:
    return {
        "version": row["version"],
        "title": row["title"],
        "kind": row["kind"],
        "doc_type": row["doc_type"],
        "kit": row["kit"],
        "path": row["path"],
        "anchor": row["anchor"],
        "ref": f"{row['path']}#{row['anchor']}",
        "start_line": row["start_line"],
        "end_line": row["end_line"],
        "breadcrumb": row["breadcrumb"],
        "contracts": json_loads(row["contracts_json"], {}),
        "score": round(score, 4),
        "reasons": reasons,
        "snippet": make_snippet(row["body"], row["title"]),
    }


def split_ref(ref: str) -> tuple[str, str | None]:
    if "#" not in ref:
        return ref, None
    path, anchor = ref.split("#", 1)
    return path, anchor or None


def normalize_query_version(version: str | None) -> str | None:
    version = (version or "").strip()
    if not version:
        return None
    if version.lower() in {"all", "*"}:
        return None
    return version


def version_where(alias: str, version: str | None, *, active_only: bool = True) -> tuple[str, list[Any]]:
    prefix = f"{alias}." if alias else ""
    clauses: list[str] = []
    params: list[Any] = []
    if version:
        clauses.append(f"{prefix}version = ?")
        params.append(version)
    if active_only:
        clauses.append(f"exists (select 1 from versions __knowledge_v where __knowledge_v.version = {prefix}version and __knowledge_v.status = 'ready')")
    if not clauses:
        return "", []
    return " and " + " and ".join(clauses), params


def contains_any(text: str, terms: tuple[str, ...] | list[str]) -> bool:
    text_l = text.lower()
    return any(term.lower() in text_l for term in terms)


def is_probably_random_identifier(query: str) -> bool:
    """Reject long unknown snake-case identifiers before semantic retrieval."""

    query = query.strip()
    return "_" in query and bool(RANDOM_IDENTIFIER_RE.fullmatch(query))


def is_explicitly_out_of_domain(query: str) -> bool:
    """Return true only for high-confidence non-HarmonyOS queries.

    This is deliberately a conservative boundary, not a general topic
    classifier. Exact platform markers preserve comparison questions. Foreign
    ecosystems are strong negative evidence; ordinary subject areas need at
    least two independent clues so words such as ``state`` or ``file`` never
    reject a valid platform query on their own.
    """

    query_l = query.strip().lower()
    if not query_l:
        return False
    if is_probably_random_identifier(query_l):
        return True
    if any(marker in query_l for marker in PLATFORM_MARKERS):
        return False
    if any(contains_intent_term(query_l, (term,)) for term in FOREIGN_TECH_TERMS):
        return True
    for group in UNRELATED_TOPIC_GROUPS:
        hits = sum(1 for term in group if contains_intent_term(query_l, (term,)))
        if hits >= 2:
            return True
    return False


def matches_deterministic_contract_query(query: str) -> bool:
    query_l = query.strip().lower()
    return any(
        all(contains_intent_term(query_l, (term,)) for term in required_terms)
        for required_terms in DETERMINISTIC_CONTRACT_QUERY_TERMS
    )


def contains_intent_term(text: str, terms: tuple[str, ...] | list[str]) -> bool:
    """Match CJK intent phrases by substring and ASCII terms as whole identifiers.

    Naive substring matching makes component names such as ``TextInput`` look like
    the configuration verb ``put`` and ``User`` look like ``use``.
    """
    text_l = text.lower()
    for term in terms:
        term_l = term.lower().strip()
        if not term_l:
            continue
        if has_cjk(term_l) or not term_l.replace(" ", "").isascii() or " " in term_l:
            if term_l in text_l:
                return True
        elif identifier_in_text(term_l, text_l):
            return True
    return False


def identifier_in_text(identifier: str, text: str) -> bool:
    identifier = identifier.lower().strip()
    if not identifier:
        return False
    if "_" in identifier or len(identifier) > 4:
        return identifier in text
    return re.search(rf"(?<![a-z0-9_]){re.escape(identifier)}(?![a-z0-9_])", text) is not None


def detect_intents(query: str) -> set[str]:
    query_l = query.lower()
    intents: set[str] = set()
    if is_howto_query(query):
        intents.add("howto")
    if re.search(r"\d{4,}", query) and contains_intent_term(query, ERROR_TERMS):
        intents.add("error_code")
    if contains_intent_term(query, LIMIT_TERMS) or UNIT_RE.search(query_l):
        intents.add("limit")
    if contains_intent_term(query, LIFECYCLE_TERMS):
        intents.add("lifecycle")
    if contains_intent_term(query, CONFIG_TERMS):
        intents.add("config")
    if contains_intent_term(query, TRANSFER_TERMS):
        intents.add("transfer")
    if contains_intent_term(query, PERMISSION_TERMS):
        intents.add("permission")
    if contains_intent_term(query, LOG_TERMS):
        intents.add("logging")
    if contains_intent_term(query, CAMERA_TERMS):
        intents.add("camera")
    return intents


def is_howto_query(query: str) -> bool:
    return contains_intent_term(query, HOWTO_TERMS)


def raw_query_terms(query: str) -> list[str]:
    result: list[str] = []

    def add(term: str) -> None:
        term = term.strip()
        if term and term not in result and term not in CJK_STOP_TERMS:
            result.append(term)

    for item in ASCII_TOKEN_RE.findall(query):
        add(item)
    for run in CJK_TOKEN_RE.findall(query):
        if len(run) <= 10:
            add(run)
        if len(run) > 2:
            for size in (4, 3, 2):
                for idx in range(0, max(0, len(run) - size + 1)):
                    gram = run[idx : idx + size]
                    if gram not in CJK_STOP_TERMS and not any(ch in CJK_BAD_GRAM_CHARS for ch in gram):
                        add(gram)
    return result[:16]


def is_generic_query_term(term: str) -> bool:
    term_l = term.strip().lower()
    if not term_l or term_l in CJK_STOP_TERMS or term_l in GENERIC_QUERY_TERMS:
        return True
    if has_cjk(term_l) and len(term_l) > 4 and any(stop in term_l for stop in CJK_STOP_TERMS):
        return True
    return has_cjk(term_l) and len(term_l) <= 1


def term_weight(term: str) -> float:
    term = term.strip()
    if not term:
        return 0.0
    if term.lower() in GENERIC_QUERY_TERMS:
        return 0.55
    if has_cjk(term):
        if len(term) == 3:
            return 1.9
        if len(term) == 4:
            return 1.75
        if len(term) == 2:
            return 1.25
        return 1.0 + min(len(term), 8) * 0.12
    if term.isdigit():
        return 2.2
    return 1.0 + min(len(term), 16) * 0.08


def informative_query_terms(query: str) -> list[str]:
    raw_terms = raw_query_terms(query)
    specific = [term for term in raw_terms if not is_generic_query_term(term)]
    source = specific if specific else raw_terms
    result: list[str] = []
    for term in sorted(source, key=lambda item: (term_weight(item), len(item)), reverse=True):
        term = term.strip()
        term_l = term.lower()
        if not term_l or term_l in {item.lower() for item in result}:
            continue
        if has_cjk(term) and len(term) > 12:
            continue
        if has_cjk(term) and any(has_cjk(item) and term in item for item in result):
            continue
        result.append(term)
    return result[:12]


def structural_seed_terms(query: str, intents: set[str]) -> list[str]:
    result = raw_query_terms(query)[:6]

    def add_many(items: tuple[str, ...]) -> None:
        for item in items:
            if item and item not in result:
                result.append(item)

    # How-to headings are useful ranking hints, but too broad for recall.
    # Keep them out of seed queries so generic words like "steps" do not
    # retrieve unrelated symbols in other document sets.
    if "limit" in intents:
        add_many(LIMIT_TERMS)
    if "lifecycle" in intents:
        add_many(LIFECYCLE_TERMS)
    if "config" in intents:
        add_many(CONFIG_TERMS)
    if "transfer" in intents:
        add_many(TRANSFER_TERMS)
    if "permission" in intents:
        add_many(PERMISSION_TERMS)
    if "logging" in intents:
        add_many(LOG_TERMS)
    if "error_code" in intents:
        add_many(ERROR_TERMS)
    return result[:24]


def expand_query(query: str) -> list[str]:
    result = [query]
    for item in semantic_aliases(query):
        if item not in result:
            result.append(item)
    for item in raw_query_terms(query):
        if item not in result:
            result.append(item)
    if re.search(r"\d{5,}", query):
        for item in re.findall(r"\d{5,}", query):
            if item not in result:
                result.append(item)
    return result[:18]


def semantic_aliases(query: str) -> list[str]:
    query_l = query.lower()
    result: list[str] = []
    for required_terms, aliases in SEMANTIC_QUERY_ALIASES:
        if all(term.lower() in query_l for term in required_terms):
            for alias in aliases:
                if alias not in result:
                    result.append(alias)
    return result


def make_fts_query(query: str) -> str:
    tokens = []
    for token in ASCII_TOKEN_RE.findall(query):
        token = token.replace('"', '""')
        if len(token) > 2 and not token.isdigit():
            tokens.append(f'"{token}"*')
        else:
            tokens.append(f'"{token}"')
    for token in [term for term in fallback_terms(query) if has_cjk(term)]:
        tokens.append(f'"{token.replace(chr(34), chr(34) * 2)}"')
    return " OR ".join(tokens[:12])


def make_trigram_query(query: str) -> str:
    query = query.strip()
    if len(query) < 3:
        return ""
    if has_cjk(query):
        return f'"{query.replace(chr(34), chr(34) * 2)}"'
    return make_fts_query(query)


def fallback_terms(query: str) -> list[str]:
    terms = []
    query = query.strip()
    def add(term: str) -> None:
        if term and term not in terms and term not in CJK_STOP_TERMS:
            terms.append(term)

    for item in expand_query(query)[1:]:
        add(item)

    for domain in DOMAIN_TERMS:
        if domain in query:
            add(domain)
    for item in re.split(r"\s+", query.strip()):
        item = item.strip(" ，。！？；：、/\\|()（）[]【】{}")
        if has_cjk(item) and len(item) > 8:
            continue
        add(item)
    for item in ASCII_TOKEN_RE.findall(query):
        add(item)
    for run in CJK_TOKEN_RE.findall(query):
        if len(run) <= 8:
            add(run)
        if len(run) > 2:
            for size in (4, 3, 2):
                for idx in range(0, max(0, len(run) - size + 1)):
                    gram = run[idx : idx + size]
                    if gram in CJK_STOP_TERMS or any(ch in CJK_BAD_GRAM_CHARS for ch in gram):
                        continue
                    if gram in query and (gram in DOMAIN_TERMS or size == 2):
                        add(gram)
    # Avoid letting generic UI words drown out domain terms.
    terms = [term for term in terms if term not in CJK_STOP_TERMS]
    return terms[:16]


def make_snippet(text: str, query: str, *, max_chars: int = 700) -> str:
    text = re.sub(r"\n{3,}", "\n\n", text or "").strip()
    if len(text) <= max_chars:
        return text
    terms = fallback_terms(query)
    lower = text.lower()
    pos = -1
    for term in terms:
        pos = lower.find(term.lower())
        if pos >= 0:
            break
    if pos < 0:
        return text[:max_chars].rstrip() + "..."
    start = max(0, pos - max_chars // 3)
    end = min(len(text), start + max_chars)
    prefix = "..." if start else ""
    suffix = "..." if end < len(text) else ""
    return prefix + text[start:end].strip() + suffix


def cosine(a: list[float], b: list[float]) -> float:
    if len(a) != len(b) or not a:
        return 0.0
    dot = sum(float(x) * float(y) for x, y in zip(a, b))
    na = math.sqrt(sum(float(x) * float(x) for x in a))
    nb = math.sqrt(sum(float(y) * float(y) for y in b))
    if not na or not nb:
        return 0.0
    return dot / (na * nb)
