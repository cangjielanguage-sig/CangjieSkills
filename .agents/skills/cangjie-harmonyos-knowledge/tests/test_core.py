from __future__ import annotations

import json
import io
import os
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
from unittest import mock

from knowledge_core.admin import ADMIN_HTML
from knowledge_core.config import AppConfig, DEFAULT_CACHE_DIR, DEFAULT_DOCS_ROOT, DEFAULT_INDEX_DIR, apply_overrides, load_config
from knowledge_core.cli import doctor, main as cli_main
from knowledge_core.embedding import EmbeddingService, EmbeddingUnavailable
from knowledge_core.http_server import sanitize_payload
import knowledge_core.indexer as indexer
from knowledge_core.indexer import build_index, compact_index, format_console_event, normalize_link_path, remove_version
from knowledge_core.mcp_server import tool_specs
from knowledge_core.parser import extract_symbol_name, parse_markdown
from knowledge_core.search import (
    Searcher,
    detect_intents,
    is_explicitly_out_of_domain,
    matches_deterministic_contract_query,
    semantic_aliases,
)
from knowledge_core.util import slugify_heading
from knowledge_core.vector_cache import VectorCache
from knowledge_core.vector_codec import pack_vector, unpack_vector


SAMPLE_API = """# ohos.data.relational_store（关系型数据库）

## func getRdbStore(UIAbilityContext, StoreConfig)

```cangjie
public func getRdbStore(context: UIAbilityContext, config: StoreConfig): RdbStore
```

**功能：** 创建或打开已有的关系型数据库。

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 22

**异常：**

| 错误码ID | 错误信息 |
| :---- | :--- |
| 14800011 | Failed to open the database because it is corrupted. |

**示例：**

```cangjie
import kit.ArkData.*
let store = getRdbStore(context, StoreConfig(RelationalStoreSecurityLevel.S1, name: "RdbTest.db"))
```

## class RdbPredicates

```cangjie
public class RdbPredicates {
    public init(name: String)
}
```

**功能：** 表示关系型数据库的谓词。

### func equalTo(String, RelationalStoreValueType)

```cangjie
public func equalTo(field: String, value: RelationalStoreValueType): RdbPredicates
```
"""


SAMPLE_GUIDE = """# 通过关系型数据库实现数据持久化

## 场景介绍

关系型数据库适用于存储包含复杂关系数据的场景，此时需要使用关系型数据库来持久化保存数据。

## 开发步骤

调用 getRdbStore 获取 RdbStore，然后执行增删改查。
"""


class CoreTests(unittest.TestCase):
    def test_run_tests_help_does_not_execute_suite(self):
        script = Path(__file__).resolve().parents[1] / "scripts" / "run_tests.py"
        completed = subprocess.run(
            [sys.executable, str(script), "--help"],
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        output = completed.stdout + completed.stderr
        self.assertEqual(completed.returncode, 0)
        self.assertIn("usage: run_tests.py", output)
        self.assertNotIn("Ran ", output)

    def test_ascii_intent_terms_do_not_match_inside_component_names(self):
        self.assertNotIn("config", detect_intents("TextInput init text placeholder controller"))
        self.assertNotIn("howto", detect_intents("requestPermissionsFromUser"))
        self.assertIn("config", detect_intents("Preferences put flush"))

    def test_explicit_domain_boundary_rejects_unrelated_topics_conservatively(self):
        for query in (
            "how to bake sourdough bread in an oven",
            "calculate monthly payment and mortgage amortization",
            "build a React component with Redux",
            "怎么给番茄土壤制作堆肥",
            "zzqx_impossible_harmony_api_kappa7429",
        ):
            with self.subTest(query=query):
                self.assertTrue(is_explicitly_out_of_domain(query))
        for query in (
            "persist user settings across app launches",
            "Canvas 显式类型完全定型",
            "HarmonyOS 如何从 SwiftUI 迁移页面",
        ):
            with self.subTest(query=query):
                self.assertFalse(is_explicitly_out_of_domain(query))

    def test_curated_agent_contracts_are_not_overridden_by_dense_retrieval(self):
        for query in (
            "Canvas 上下文字段怎样显式类型完全定型",
            "ForEach itemGenerator 回调参数形状和索引类型",
            "@Prop 父子组件单向传值",
            "@Builder 成员函数 bind(this)",
            "stop receiving a previously registered system broadcast",
            "把设备镜头采集到的实时画面显示在应用界面",
            "发现周围正在广播的低功耗无线外设",
            "把沙箱中的文档交给另一个应用打开或处理",
            "按明确组件或按能力条件选择要启动的页面",
        ):
            with self.subTest(query=query):
                self.assertTrue(matches_deterministic_contract_query(query))
        self.assertFalse(matches_deterministic_contract_query("persist settings across launches"))

    def test_markdown_parser_ignores_headings_and_links_inside_fences(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            path = root / "docs" / "Guide" / "tools" / "sample.md"
            path.parent.mkdir(parents=True)
            path.write_text(
                """# Real title

```shell
# not a heading
echo '[not a link](fake.md)'
```

## Real section

~~~text
## still not a heading
~~~
""",
                encoding="utf-8",
            )
            parsed = parse_markdown(path, root)
        self.assertEqual([section.title for section in parsed.sections], ["Real title", "Real section"])
        self.assertEqual(parsed.sections[0].links, [])
        self.assertEqual(len(parsed.sections[0].code_blocks), 1)
        self.assertEqual(len(parsed.sections[1].code_blocks), 1)

    def test_source_compatible_anchors_and_reference_paths(self):
        self.assertEqual(
            slugify_heading("func onCreate(Want, LaunchParam)"),
            "func-oncreatewant-launchparam",
        )
        self.assertEqual(slugify_heading(r"type AsyncCallback\<T>"), "type-asynccallbackt")
        self.assertEqual(slugify_heading("static let MAX_KEY_LENGTH"), "static-let-max_key_length")
        self.assertEqual(
            slugify_heading(r"func getKVStore\<T>(String, KVOptions) where T \<: SingleKVStore"),
            "func-getkvstoretstring-kvoptions-where-t--singlekvstore",
        )
        self.assertEqual(
            normalize_link_path(
                "docs/Guide/application-models/lifecycle.md",
                "../reference/AbilityKit/ui_ability.md",
            ),
            "docs/API/AbilityKit/ui_ability.md",
        )
        self.assertEqual(
            normalize_link_path(
                "docs/Guide/arkui-cj/topic.md",
                "../../arkui-cj/rendering_control/ifelse.md",
            ),
            "docs/Guide/arkui-cj/rendering_control/ifelse.md",
        )
        self.assertEqual(
            normalize_link_path(
                "docs/API/cj-development-intro.md",
                "../../application-dev/security/AccessToken/overview.md",
            ),
            "docs/Guide/security/AccessToken/overview.md",
        )

    def test_symbol_parser_supports_modifiers_and_stable_constructor_names(self):
        self.assertEqual(extract_symbol_name("static func create(Int32)"), ("func", "create"))
        self.assertEqual(extract_symbol_name("public static let LIMIT"), ("let", "LIMIT"))
        self.assertEqual(extract_symbol_name("static const EVENT_READY"), ("const", "EVENT_READY"))
        self.assertEqual(extract_symbol_name("type Permissions"), ("type", "Permissions"))
        self.assertEqual(extract_symbol_name("init(UInt32, String)"), ("init", "init"))
        self.assertEqual(extract_symbol_name("operator +(Int32, Int32)"), ("operator", "operator +"))
        self.assertEqual(extract_symbol_name(r"operator func \[](Int64)"), ("operator", r"operator \[]"))

    def test_cli_section_read_requires_anchor(self):
        output = io.StringIO()
        with redirect_stdout(output):
            status = cli_main(["read", "docs/API/example.md"])
        self.assertEqual(status, 2)
        self.assertIn("exact anchored ref", output.getvalue())

    def make_index(self):
        tmp = tempfile.TemporaryDirectory()
        root = Path(tmp.name)
        api_dir = root / "docs" / "API" / "ArkData"
        guide_dir = root / "docs" / "Guide" / "database"
        api_dir.mkdir(parents=True)
        guide_dir.mkdir(parents=True)
        (api_dir / "cj-apis-relational_store.md").write_text(SAMPLE_API, encoding="utf-8")
        (guide_dir / "cj-data-persistence-by-rdb-store.md").write_text(SAMPLE_GUIDE, encoding="utf-8")
        cfg = AppConfig(docs_root=str(root / "docs"), index_dir=str(root / "index"))
        stats = build_index(cfg, quiet=True)
        return tmp, cfg, stats

    def test_build_and_search_deterministically(self):
        tmp, cfg, stats = self.make_index()
        self.addCleanup(tmp.cleanup)
        self.assertEqual(stats.documents, 2)
        self.assertGreaterEqual(stats.symbols, 3)
        searcher = Searcher(cfg)
        self.addCleanup(searcher.close)

        results = searcher.search("getRdbStore", top_k=3)
        self.assertTrue(results)
        self.assertEqual(results[0]["title"], "func getRdbStore(UIAbilityContext, StoreConfig)")
        self.assertIn("docs/API/ArkData", results[0]["path"])

        symbol = searcher.lookup_symbol("RdbPredicates")
        self.assertIsNotNone(symbol)
        self.assertTrue(any(member["name"] == "equalTo" for member in symbol["members"]))

        guide = searcher.search("关系型数据库 持久化", scope="guide", top_k=1)
        self.assertTrue(guide)
        self.assertIn("cj-data-persistence", guide[0]["path"])

        natural = searcher.search("如何创建或打开关系型数据库", top_k=3)
        self.assertTrue(natural)
        self.assertTrue(any("关系型数据库" in item["breadcrumb"] or "关系型数据库" in item["snippet"] for item in natural))
        self.assertTrue(any(item["doc_type"] in {"api", "guide"} for item in natural))

        semantic = searcher.search("仓颉里怎么保存本地结构化数据", top_k=3)
        self.assertTrue(semantic)
        self.assertTrue(any("持久化" in item["breadcrumb"] or "持久化" in item["snippet"] for item in semantic))

        err = searcher.search("14800011", top_k=1)
        self.assertTrue(err)
        self.assertIn("14800011", err[0]["snippet"])
        self.assertEqual(err[0]["contracts"]["error_codes"], ["14800011"])

        contract = searcher.search("getRdbStore", top_k=1)[0]["contracts"]
        self.assertEqual(contract["permissions"], ["ohos.permission.DISTRIBUTED_DATASYNC"])
        self.assertEqual(contract["syscaps"], ["SystemCapability.DistributedDataManager.RelationalStore.Core"])
        self.assertEqual(contract["since"], ["22"])

    def test_related_docs_resolves_exact_internal_links_only(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        docs = root / "docs" / "Guide" / "links"
        docs.mkdir(parents=True)
        (docs / "a.md").write_text(
            """# Document A

## Source

[target](b.md#target) and [external](https://example.com/reference).

![illustration only](b.md#other)

## Unrelated

Must not be returned for the external link.
""",
            encoding="utf-8",
        )
        (docs / "b.md").write_text(
            """# Document B

## Target

Exact target.

## Other

Must not be returned for the anchored link.
""",
            encoding="utf-8",
        )
        (docs / "c.md").write_text(
            """# Document C

## Referrer

[back](b.md#target)
""",
            encoding="utf-8",
        )
        cfg = AppConfig(docs_root=str(root / "docs"), index_dir=str(root / "index"))
        build_index(cfg, quiet=True)
        searcher = Searcher(cfg)
        self.addCleanup(searcher.close)

        outgoing = searcher.related_docs("docs/Guide/links/a.md#source")
        self.assertEqual([item["ref"] for item in outgoing], ["docs/Guide/links/b.md#target"])
        self.assertEqual(outgoing[0]["reasons"], ["related-outgoing"])

        incoming = searcher.related_docs("docs/Guide/links/b.md#target")
        self.assertEqual(
            {item["ref"] for item in incoming},
            {"docs/Guide/links/a.md#source", "docs/Guide/links/c.md#referrer"},
        )
        self.assertTrue(all(item["reasons"] == ["related-incoming"] for item in incoming))

    def test_default_config_uses_packaged_data_paths(self):
        old_cwd = Path.cwd()
        with tempfile.TemporaryDirectory() as d:
            os.chdir(d)
            try:
                cfg = load_config()
            finally:
                os.chdir(old_cwd)
        self.assertEqual(Path(cfg.docs_root), DEFAULT_DOCS_ROOT)
        self.assertEqual(Path(cfg.index_dir), DEFAULT_INDEX_DIR)
        self.assertEqual(cfg.embedding_mode, "search")
        self.assertEqual(cfg.embedding.dimensions, 256)
        self.assertEqual(cfg.vector_cache_path, DEFAULT_CACHE_DIR / "vector_cache.sqlite")

    def test_doctor_requires_configured_vectors_in_search_mode(self):
        tmp, cfg, _ = self.make_index()
        self.addCleanup(tmp.cleanup)
        with redirect_stdout(io.StringIO()):
            self.assertFalse(doctor(cfg))
        cfg.embedding_mode = "off"
        with redirect_stdout(io.StringIO()):
            self.assertTrue(doctor(cfg))

    def test_doctor_rejects_unresolved_internal_anchor(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        docs = root / "docs" / "Guide" / "links"
        docs.mkdir(parents=True)
        (docs / "a.md").write_text("# A\n\n[broken](b.md#missing)\n", encoding="utf-8")
        (docs / "b.md").write_text("# B\n\n## Present\n", encoding="utf-8")
        cfg = AppConfig(docs_root=str(root / "docs"), index_dir=str(root / "index"), embedding_mode="off")
        build_index(cfg, quiet=True)
        output = io.StringIO()
        with redirect_stdout(output):
            self.assertFalse(doctor(cfg))
        report = json.loads(output.getvalue())
        self.assertEqual(report["link_counts"]["anchored"], 1)
        self.assertEqual(report["link_counts"]["resolved_anchors"], 0)

    def test_semantic_aliases_cover_agent_workflows(self):
        self.assertIn("equalTo", semantic_aliases("RdbPredicates 怎么按字段等值匹配并查询"))
        self.assertIn(
            "ImagePacker packToFile PackingOption",
            semantic_aliases("PixelMap encode write file API"),
        )
        self.assertIn("ResultSet close", semantic_aliases("ResultSet 查询完是否需要关闭"))
        self.assertTrue(any("generateKeyItem" in item for item in semantic_aliases("HUKS 如何生成密钥")))
        camera = semantic_aliases("如何使用相机拍照或预览")
        self.assertTrue(any("createPreviewOutput" in item for item in camera))
        self.assertTrue(any("createPhotoOutput" in item for item in camera))
        self.assertTrue(any("CanvasRenderingContext2D" in item for item in semantic_aliases("Canvas 显式类型完全定型")))
        self.assertTrue(any("ItemGeneratorFunc" in item for item in semantic_aliases("ForEach 回调参数形状")))
        self.assertTrue(any("单向同步" in item for item in semantic_aliases("@Prop 父子组件传值")))
        self.assertTrue(any("CustomView" in item for item in semantic_aliases("@Builder bind this")))

    def test_unified_knowledge_config_does_not_override_packaged_paths(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            project = root / "project"
            project.mkdir()
            (project / "cangjie.skills.toml").write_text(
                '[knowledge]\nversion = "6.1.1.345"\n',
                encoding="utf-8",
            )
            old_cwd = Path.cwd()
            os.chdir(project)
            try:
                cfg = load_config()
            finally:
                os.chdir(old_cwd)
        self.assertEqual(cfg.docs_version, "6.1.1.345")
        self.assertEqual(Path(cfg.docs_root), DEFAULT_DOCS_ROOT)
        self.assertEqual(Path(cfg.index_dir), DEFAULT_INDEX_DIR)

    def test_explicit_cangjie_skills_config_overrides_version(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "cangjie.skills.toml"
            path.write_text(
                '[knowledge]\nversion = "7.0.0"\n',
                encoding="utf-8",
            )
            cfg = load_config(path)
        self.assertEqual(cfg.docs_version, "7.0.0")
        self.assertEqual(Path(cfg.docs_root), DEFAULT_DOCS_ROOT)
        self.assertEqual(Path(cfg.index_dir), DEFAULT_INDEX_DIR)

    def test_all_embedding_modes_map_to_index_and_search_flags(self):
        expected = {
            "off": (False, False),
            "search": (False, True),
            "index": (True, False),
            "all": (True, True),
        }
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "cangjie.skills.toml"
            for mode, flags in expected.items():
                path.write_text(f'[knowledge.embedding]\nmode = "{mode}"\n', encoding="utf-8")
                cfg = load_config(path)
                self.assertEqual((cfg.index_embeddings, cfg.search_embeddings), flags)

    def test_embedding_dimension_cli_override_is_validated(self):
        cfg = AppConfig()
        self.assertEqual(apply_overrides(cfg, embedding_dimensions=512).embedding.dimensions, 512)
        with self.assertRaisesRegex(ValueError, "dimensions must be > 0"):
            apply_overrides(AppConfig(), embedding_dimensions=0)

    def test_embedding_settings_map_without_exposing_secret_values(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "cangjie.skills.toml"
            path.write_text(
                '\n'.join([
                    '[knowledge.embedding]',
                    'mode = "all"',
                    'api_format = "openai"',
                    'model = "custom-embedding"',
                    'base_url = "https://embedding.example/v1"',
                    'api_key_env = "TEST_EMBEDDING_KEY"',
                    'dimensions = 768',
                    'min_similarity = 0.45',
                    'batch_size = 4',
                    'timeout_seconds = 11',
                    'max_retries = 1',
                ]),
                encoding="utf-8",
            )
            with mock.patch.dict(os.environ, {"TEST_EMBEDDING_KEY": "embedding-secret"}):
                cfg = load_config(path)
        self.assertEqual(cfg.embedding_mode, "all")
        self.assertEqual(cfg.embedding.api_format, "openai")
        self.assertEqual(cfg.embedding.dimensions, 768)
        self.assertEqual(cfg.embedding.min_similarity, 0.45)
        self.assertEqual(cfg.embedding.batch_size, 4)
        self.assertEqual(cfg.embedding.api_key, "embedding-secret")
        self.assertTrue(cfg.index_embeddings)

    def test_local_config_rejects_plaintext_api_keys(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "cangjie.skills.toml"
            path.write_text('[knowledge.embedding]\napi_key = "must-not-live-in-a-file"\n', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "api_key_env"):
                load_config(path)

    def test_embedding_search_degrades_without_key(self):
        tmp, cfg, _ = self.make_index()
        self.addCleanup(tmp.cleanup)
        cfg.embedding_mode = "search"
        cfg.embedding.api_key = None
        searcher = Searcher(cfg)
        self.addCleanup(searcher.close)
        results = searcher.search("getRdbStore", embedding_mode="search", top_k=1)
        self.assertEqual(results[0]["title"], "func getRdbStore(UIAbilityContext, StoreConfig)")
        self.assertFalse(Path(cfg.vector_cache_path).exists())

    def test_vector_codec_and_independent_dense_recall(self):
        vector = [0.125, -0.5, 1.0]
        restored = unpack_vector(pack_vector(vector))
        self.assertEqual(len(restored), len(vector))
        for actual, expected in zip(restored, vector):
            self.assertAlmostEqual(actual, expected, places=6)

        tmp, cfg, _ = self.make_index()
        self.addCleanup(tmp.cleanup)
        target_path = Path(cfg.docs_root) / "Guide" / "camera" / "semantic.md"
        target_path.parent.mkdir(parents=True)
        target_path.write_text("# Dense-only target\n\nCamera photography workflow.", encoding="utf-8")
        build_index(cfg, quiet=True)

        cfg.embedding_mode = "search"
        cfg.embedding.api_key = "test-key"
        searcher = Searcher(cfg)
        self.addCleanup(searcher.close)
        sections = searcher.con.execute("select id, path from sections order by id").fetchall()
        for section in sections:
            dense = [0.0, 1.0] if section["path"].endswith("semantic.md") else [1.0, 0.0]
            searcher.con.execute(
                """
                insert into vectors(
                  section_id, version, provider, model, dimensions, vector_blob, text_hash, created_at
                ) values (?, 'default', ?, ?, 2, ?, 'test', 'now')
                """,
                (section["id"], cfg.embedding.api_format, cfg.embedding.model, pack_vector(dense)),
            )
        searcher.con.commit()
        with mock.patch.object(searcher.embedding, "embed_query", return_value=[0.0, 1.0]) as embed_query:
            lexical = searcher.search("getRdbStore", embedding_mode="search", top_k=1)
            self.assertEqual(lexical[0]["title"], "func getRdbStore(UIAbilityContext, StoreConfig)")
            embed_query.assert_not_called()

            query = "show a live view from the device lens"
            results = searcher.search(query, embedding_mode="search", top_k=10)
            vector_only = searcher.vector_search(query, top_k=1)
        dense_result = next(item for item in results if item["path"].endswith("semantic.md"))
        self.assertIn("vector", dense_result["reasons"])
        self.assertIn("semantic-route", dense_result["reasons"])
        self.assertTrue(vector_only[0]["path"].endswith("semantic.md"))
        self.assertEqual(vector_only[0]["reasons"], ["vector", "semantic-route"])

        with mock.patch.object(searcher.embedding, "embed_query") as embed_query:
            self.assertEqual(
                searcher.search("qzvx_nwkp_rtym_bcdf_ghjs_luae", embedding_mode="search"),
                [],
            )
            embed_query.assert_not_called()

        with mock.patch.object(searcher.embedding, "embed_query") as embed_query:
            self.assertEqual(
                searcher.search(
                    "build a React component that synchronizes state with Redux",
                    embedding_mode="search",
                ),
                [],
            )
            embed_query.assert_not_called()

        with mock.patch.object(searcher.embedding, "embed_query") as embed_query:
            self.assertEqual(
                searcher.search("resolve a Rust async borrow checker error", embedding_mode="search"),
                [],
            )
            embed_query.assert_not_called()

    def test_dense_recall_lifts_three_lexically_disjoint_queries(self):
        tmp, cfg, _ = self.make_index()
        self.addCleanup(tmp.cleanup)
        semantic_dir = Path(cfg.docs_root) / "Guide" / "semantic"
        semantic_dir.mkdir(parents=True)
        targets = {
            "preferences.md": [1.0, 0.0, 0.0],
            "bluetooth.md": [0.0, 1.0, 0.0],
            "camera.md": [0.0, 0.0, 1.0],
        }
        for name in targets:
            (semantic_dir / name).write_text(
                f"# Opaque {name}\n\nInternal operation marker only.",
                encoding="utf-8",
            )
        build_index(cfg, quiet=True)

        cfg.embedding_mode = "search"
        cfg.embedding.api_key = "test-key"
        searcher = Searcher(cfg)
        self.addCleanup(searcher.close)
        for name, vector in targets.items():
            section = searcher.con.execute(
                "select id from sections where path like ? limit 1",
                (f"%/{name}",),
            ).fetchone()
            searcher.con.execute(
                """
                insert into vectors(
                  section_id, version, provider, model, dimensions, vector_blob, text_hash, created_at
                ) values (?, 'default', ?, ?, 3, ?, 'test', 'now')
                """,
                (section["id"], cfg.embedding.api_format, cfg.embedding.model, pack_vector(vector)),
            )
        searcher.con.commit()

        queries = {
            "retain settings between app launches": ("preferences.md", [1.0, 0.0, 0.0]),
            "discover nearby wireless peripherals": ("bluetooth.md", [0.0, 1.0, 0.0]),
            "show a live view from the device lens": ("camera.md", [0.0, 0.0, 1.0]),
        }
        for query, (expected_path, query_vector) in queries.items():
            lexical = searcher.search(query, embedding_mode="off", top_k=1)
            self.assertFalse(lexical and lexical[0]["path"].endswith(expected_path))
            with mock.patch.object(searcher.embedding, "embed_query", return_value=query_vector):
                dense = searcher.search(query, embedding_mode="search", top_k=1)
            self.assertTrue(dense[0]["path"].endswith(expected_path))
            self.assertIn("vector", dense[0]["reasons"])
            self.assertIn("semantic-route", dense[0]["reasons"])

class EmbeddingServiceTests(unittest.TestCase):
    def test_dashscope_embedding_response(self):
        class Handler(BaseHTTPRequestHandler):
            def do_POST(self):  # noqa: N802
                _ = self.rfile.read(int(self.headers.get("Content-Length", "0")))
                body = json.dumps({
                    "output": {"embeddings": [{"text_index": 0, "embedding": [0.1, 0.2]}]},
                    "usage": {"total_tokens": 7},
                }).encode()
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def log_message(self, *args):
                return

        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(server.shutdown)

        cfg = AppConfig()
        cfg.embedding.api_key = "test-key"
        cfg.embedding.base_url = f"http://127.0.0.1:{server.server_address[1]}"
        cfg.embedding.dimensions = 2
        client = EmbeddingService(cfg)
        self.assertEqual(client.embed_texts(["hello"]), [[0.1, 0.2]])
        self.assertEqual(client.request_count, 1)
        self.assertEqual(client.input_tokens, 7)

    def test_openai_embedding_format_uses_embeddings_path_and_dimensions(self):
        request: dict[str, object] = {}

        class Handler(BaseHTTPRequestHandler):
            def do_POST(self):  # noqa: N802
                request["path"] = self.path
                request["payload"] = json.loads(
                    self.rfile.read(int(self.headers.get("Content-Length", "0")))
                )
                body = json.dumps({
                    "data": [{"index": 0, "embedding": [0.3, 0.4]}],
                    "usage": {"total_tokens": 5},
                }).encode()
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def log_message(self, *args):
                return

        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(server.shutdown)

        cfg = AppConfig()
        cfg.embedding.api_format = "openai"
        cfg.embedding.api_key = "test-key"
        cfg.embedding.base_url = f"http://127.0.0.1:{server.server_address[1]}/v1"
        cfg.embedding.dimensions = 2
        client = EmbeddingService(cfg)
        self.assertEqual(client.embed_texts(["hello"]), [[0.3, 0.4]])
        self.assertEqual(request["path"], "/v1/embeddings")
        self.assertEqual(
            request["payload"],
            {"model": "text-embedding-v4", "input": ["hello"], "dimensions": 2},
        )
        self.assertEqual(client.request_count, 1)
        self.assertEqual(client.input_tokens, 5)

    def test_embedding_response_rejects_missing_or_duplicate_rows(self):
        cfg = AppConfig()
        cfg.embedding.api_key = "test-key"
        client = EmbeddingService(cfg)
        client.http.post = mock.Mock(
            return_value={"output": {"embeddings": [{"text_index": 0, "embedding": [0.1]}]}}
        )
        with self.assertRaisesRegex(EmbeddingUnavailable, "response"):
            client.embed_texts(["one", "two"])

        client.http.post = mock.Mock(
            return_value={
                "output": {
                    "embeddings": [
                        {"text_index": 0, "embedding": [0.1]},
                        {"text_index": 0, "embedding": [0.2]},
                    ]
                }
            }
        )
        with self.assertRaisesRegex(EmbeddingUnavailable, "response"):
            client.embed_texts(["one", "two"])

    def test_embedding_response_rejects_bad_dimensions_and_values(self):
        cfg = AppConfig()
        cfg.embedding.api_key = "test-key"
        cfg.embedding.dimensions = None
        client = EmbeddingService(cfg)
        with self.assertRaisesRegex(EmbeddingUnavailable, "inconsistent"):
            client._validate_vectors(["one", "two"], [[0.1], [0.2, 0.3]])
        with self.assertRaisesRegex(EmbeddingUnavailable, "non-finite"):
            client._validate_vectors(["one"], [[float("nan")]])
        cfg.embedding.dimensions = 2
        with self.assertRaisesRegex(EmbeddingUnavailable, "expected 2, got 1"):
            client._validate_vectors(["one"], [[0.1]])


class UtilityTests(unittest.TestCase):
    def test_admin_html_contains_core_controls(self):
        self.assertIn("HarmonyOS Knowledge 管理面板", ADMIN_HTML)
        self.assertIn("id=\"start-build\"", ADMIN_HTML)
        self.assertIn("id=\"physical_remove\"", ADMIN_HTML)
        self.assertIn("id=\"compact-index\"", ADMIN_HTML)
        self.assertIn("id=\"versions\"", ADMIN_HTML)
        self.assertIn("id=\"query_out\"", ADMIN_HTML)
        self.assertIn("/api/build", ADMIN_HTML)
        self.assertIn("/api/versions/remove", ADMIN_HTML)
        self.assertIn("/api/compact", ADMIN_HTML)
        self.assertIn("embedding_mode", ADMIN_HTML)

    def test_mcp_surface_is_retrieval_only(self):
        specs = tool_specs()
        names = {item["name"] for item in specs}
        self.assertEqual(
            names,
            {"search_docs", "lookup_symbol", "read_doc", "find_examples", "related_docs", "status"},
        )
        search_spec = next(item for item in specs if item["name"] == "search_docs")
        self.assertIn("embedding_mode", search_spec["inputSchema"]["properties"])

    def test_http_payload_sanitizes_api_key(self):
        payload = sanitize_payload({"api_key": "secret", "version": "6.1"})
        self.assertEqual(payload["api_key"], "***")
        self.assertEqual(payload["version"], "6.1")

    def test_console_event_format_is_readable(self):
        plain = format_console_event("embed", "vectors=10", 65, use_color=False)
        self.assertIn("1m05s", plain)
        self.assertIn("EMBED", plain)
        self.assertIn("vectors=10", plain)
        self.assertNotIn("\x1b[", plain)
        colored = format_console_event("done", "ok", 1, use_color=True)
        self.assertIn("\x1b[", colored)


class AtomicAndCacheTests(unittest.TestCase):
    def make_single_doc_config(self):
        tmp = tempfile.TemporaryDirectory()
        root = Path(tmp.name)
        api_dir = root / "docs" / "API" / "ArkData"
        api_dir.mkdir(parents=True)
        (api_dir / "cj-apis-relational_store.md").write_text(SAMPLE_API, encoding="utf-8")
        cfg = AppConfig(docs_root=str(root / "docs"), index_dir=str(root / "index"))
        return tmp, cfg

    def test_vector_cache_is_namespaced_by_endpoint_and_requested_dimensions(self):
        with tempfile.TemporaryDirectory() as directory:
            cache = VectorCache(Path(directory) / "vectors.sqlite")
            try:
                cache.put(
                    provider="dashscope",
                    model="text-embedding-v4",
                    endpoint="https://region-a.example/embedding",
                    requested_dimensions=512,
                    text="same text",
                    vector=[0.1, 0.2],
                )
                self.assertIsNotNone(
                    cache.get(
                        provider="dashscope",
                        model="text-embedding-v4",
                        endpoint="https://region-a.example/embedding/",
                        requested_dimensions=512,
                        text="same text",
                    )
                )
                self.assertIsNone(
                    cache.get(
                        provider="dashscope",
                        model="text-embedding-v4",
                        endpoint="https://region-b.example/embedding",
                        requested_dimensions=512,
                        text="same text",
                    )
                )
                self.assertIsNone(
                    cache.get(
                        provider="dashscope",
                        model="text-embedding-v4",
                        endpoint="https://region-a.example/embedding",
                        requested_dimensions=1024,
                        text="same text",
                    )
                )
            finally:
                cache.close()

    def test_failed_rebuild_preserves_previous_main_index(self):
        tmp, cfg = self.make_single_doc_config()
        self.addCleanup(tmp.cleanup)
        first = build_index(cfg, quiet=True)
        self.assertEqual(first.documents, 1)

        def boom(*args, **kwargs):
            raise RuntimeError("simulated build interruption")

        with mock.patch.object(indexer, "insert_document", side_effect=boom):
            with self.assertRaises(RuntimeError):
                build_index(cfg, quiet=True)

        searcher = Searcher(cfg)
        self.addCleanup(searcher.close)
        results = searcher.search("getRdbStore", top_k=1)
        self.assertTrue(results)
        self.assertEqual(results[0]["title"], "func getRdbStore(UIAbilityContext, StoreConfig)")

    def test_vector_build_without_key_preserves_previous_main_index(self):
        tmp, cfg = self.make_single_doc_config()
        self.addCleanup(tmp.cleanup)
        build_index(cfg, quiet=True)
        original = Path(cfg.index_path).read_bytes()

        cfg.embedding_mode = "index"
        cfg.embedding.api_key = None
        with self.assertRaisesRegex(RuntimeError, cfg.embedding.api_key_env):
            build_index(cfg, quiet=True)

        self.assertEqual(Path(cfg.index_path).read_bytes(), original)
        self.assertFalse(Path(cfg.index_path).with_name("index.building.sqlite").exists())

    def test_vector_cache_reuses_embeddings(self):
        calls = {"embedding": 0}

        class Handler(BaseHTTPRequestHandler):
            def do_POST(self):  # noqa: N802
                _ = self.rfile.read(int(self.headers.get("Content-Length", "0")))
                calls["embedding"] += 1
                body = json.dumps(
                    {
                        "output": {
                            "embeddings": [
                                {"text_index": 0, "embedding": [1.0, 0.0]},
                                {"text_index": 1, "embedding": [0.0, 1.0]},
                                {"text_index": 2, "embedding": [0.5, 0.5]},
                                {"text_index": 3, "embedding": [0.2, 0.8]},
                            ]
                        }
                    }
                ).encode()
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def log_message(self, *args):
                return

        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(server.shutdown)

        tmp, cfg = self.make_single_doc_config()
        self.addCleanup(tmp.cleanup)
        cfg.embedding_mode = "index"
        cfg.embedding.api_key = "test-key"
        cfg.embedding.base_url = f"http://127.0.0.1:{server.server_address[1]}/embedding"
        cfg.embedding.batch_size = 10
        cfg.embedding.dimensions = 2

        first = build_index(cfg, quiet=True)
        first_calls = dict(calls)
        self.assertGreater(first.vectors, 0)
        self.assertGreater(first_calls["embedding"], 0)

        second = build_index(cfg, quiet=True)
        self.assertEqual(calls, first_calls)
        self.assertGreater(second.vector_cache_hits, 0)


class VersioningTests(unittest.TestCase):
    def write_doc(self, root: Path, name: str, symbol: str, desc: str) -> Path:
        api_dir = root / "docs" / "API" / "Kit"
        api_dir.mkdir(parents=True, exist_ok=True)
        path = api_dir / name
        path.write_text(
            f"""# Kit API

## func {symbol}()

```cangjie
public func {symbol}(): Unit
```

**Function:** {desc}
""",
            encoding="utf-8",
        )
        return path

    def test_multiple_versions_share_one_index(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            cfg = AppConfig(docs_root=str(root / "docs"), index_dir=str(root / "index"), docs_version="6.0.2.636")

            self.write_doc(root, "same-path.md", "oldFunc", "available only in 6.0")
            first = build_index(cfg, quiet=True)
            self.assertEqual(first.documents, 1)

            self.write_doc(root, "same-path.md", "newFunc", "available only in 6.1")
            cfg.docs_version = "6.1.1.345"
            second = build_index(cfg, quiet=True)
            self.assertEqual(second.documents, 1)

            searcher = Searcher(cfg)
            try:
                versions = {item["version"] for item in searcher.versions()}
                self.assertEqual(versions, {"6.0.2.636", "6.1.1.345"})

                self.assertEqual(searcher.search("newFunc", top_k=1)[0]["version"], "6.1.1.345")
                self.assertFalse(searcher.search("oldFunc", top_k=1))
                self.assertEqual(searcher.search("oldFunc", version="6.0.2.636", top_k=1)[0]["version"], "6.0.2.636")
                self.assertEqual(searcher.search("oldFunc", version="all", top_k=1)[0]["version"], "6.0.2.636")
            finally:
                searcher.close()

    def test_incremental_build_updates_and_removes_missing_docs(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            cfg = AppConfig(docs_root=str(root / "docs"), index_dir=str(root / "index"), docs_version="7.0.0")

            alpha = self.write_doc(root, "alpha.md", "alphaFunc", "first version")
            beta = self.write_doc(root, "beta.md", "betaFunc", "removed later")
            build_index(cfg, quiet=True)

            alpha.write_text(
                """# Kit API

## func alphaRenamed()

```cangjie
public func alphaRenamed(): Unit
```

**Function:** updated incrementally
""",
                encoding="utf-8",
            )
            beta.unlink()
            stats = build_index(cfg, quiet=True, incremental=True)
            self.assertEqual(stats.documents, 1)
            self.assertEqual(stats.documents_removed, 1)
            self.assertEqual(stats.documents_updated, 1)

            searcher = Searcher(cfg)
            try:
                self.assertTrue(searcher.search("alphaRenamed", top_k=1))
                self.assertFalse(searcher.search("alphaFunc", top_k=1))
                self.assertFalse(searcher.search("betaFunc", top_k=1))
            finally:
                searcher.close()

    def test_incremental_build_can_keep_missing_docs(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            cfg = AppConfig(docs_root=str(root / "docs"), index_dir=str(root / "index"), docs_version="7.1.0")
            beta = self.write_doc(root, "beta.md", "betaFunc", "kept when missing")
            build_index(cfg, quiet=True)
            beta.unlink()

            stats = build_index(cfg, quiet=True, incremental=True, remove_missing=False)
            self.assertEqual(stats.documents_skipped, 0)
            self.assertEqual(stats.documents_removed, 0)

            searcher = Searcher(cfg)
            try:
                self.assertTrue(searcher.search("betaFunc", top_k=1))
            finally:
                searcher.close()

    def test_remove_version_removes_only_that_version(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            cfg = AppConfig(docs_root=str(root / "docs"), index_dir=str(root / "index"), docs_version="8.0.0")
            self.write_doc(root, "api.md", "oldOnly", "old")
            build_index(cfg, quiet=True)
            self.write_doc(root, "api.md", "newOnly", "new")
            cfg.docs_version = "8.1.0"
            build_index(cfg, quiet=True)

            removed = remove_version(cfg, "8.0.0")
            self.assertEqual(removed["mode"], "logical")
            self.assertIn("tombstone_version", removed)
            self.assertEqual(removed["documents"], 1)

            searcher = Searcher(cfg)
            try:
                self.assertFalse(searcher.search("oldOnly", version="all", top_k=1))
                self.assertTrue(searcher.search("newOnly", version="8.1.0", top_k=1))
                self.assertEqual({item["version"] for item in searcher.versions()}, {"8.1.0"})
            finally:
                searcher.close()

            compacted = compact_index(cfg)
            self.assertEqual(compacted["before_active"]["documents"], 1)
            self.assertGreater(compacted["before_physical"]["documents"], compacted["before_active"]["documents"])
            self.assertEqual(compacted["after_physical"]["documents"], 1)
            searcher = Searcher(cfg)
            try:
                self.assertFalse(searcher.search("oldOnly", version="all", top_k=1))
                self.assertTrue(searcher.search("newOnly", version="8.1.0", top_k=1))
            finally:
                searcher.close()

    def test_build_progress_callback_receives_events(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            cfg = AppConfig(docs_root=str(root / "docs"), index_dir=str(root / "index"), docs_version="9.0.0")
            self.write_doc(root, "api.md", "progressFunc", "progress")
            events = []
            build_index(cfg, quiet=True, progress_callback=events.append)
            stages = [event["stage"] for event in events]
            self.assertIn("start", stages)
            self.assertIn("done", stages)
            self.assertTrue(all("elapsed_text" in event for event in events))


@unittest.skipUnless(
    os.getenv("CANGJIE_KNOWLEDGE_RUN_LIVE_EMBEDDING") == "1" and os.getenv("DASHSCOPE_API_KEY"),
    "live embedding test disabled",
)
class LiveAliyunEmbeddingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api_key = os.environ["DASHSCOPE_API_KEY"]

    def live_cfg(self, tmp_root: Path | None = None) -> AppConfig:
        cfg = AppConfig(embedding_mode="all")
        cfg.embedding.api_key = self.api_key
        cfg.embedding.batch_size = 3
        if tmp_root:
            cfg.docs_root = str(tmp_root / "docs")
            cfg.index_dir = str(tmp_root / "index")
        return cfg

    def test_live_embedding_batch(self):
        cfg = self.live_cfg()
        client = EmbeddingService(cfg)
        vectors = client.embed_texts(["getRdbStore 关系型数据库", "RdbPredicates 谓词"])
        self.assertEqual(len(vectors), 2)
        self.assertEqual(len(vectors[0]), 256)
        self.assertEqual(len(vectors[1]), 256)
        for vector in vectors:
            norm = sum(float(x) * float(x) for x in vector) ** 0.5
            self.assertGreater(norm, 0.9)
            self.assertLess(norm, 1.1)

    def test_live_embedding_index_and_search(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            api_dir = root / "docs" / "API" / "ArkData"
            guide_dir = root / "docs" / "Guide" / "database"
            api_dir.mkdir(parents=True)
            guide_dir.mkdir(parents=True)
            (api_dir / "cj-apis-relational_store.md").write_text(SAMPLE_API, encoding="utf-8")
            (guide_dir / "cj-data-persistence-by-rdb-store.md").write_text(SAMPLE_GUIDE, encoding="utf-8")
            cfg = self.live_cfg(root)
            stats = build_index(cfg, quiet=True)
            self.assertEqual(stats.documents, 2)
            self.assertGreaterEqual(stats.vectors, stats.sections)
            self.assertEqual(stats.vector_failures, 0)

            searcher = Searcher(cfg)
            try:
                status = searcher.status()
                self.assertEqual(status["mode"], "embedding-search")
                self.assertGreaterEqual(status["vectors"], stats.sections)

                semantic = searcher.search("仓颉里怎么保存本地结构化数据", embedding_mode="search", top_k=3)
                self.assertTrue(semantic)
                self.assertTrue(any("关系型数据库" in item["breadcrumb"] or "持久化" in item["breadcrumb"] for item in semantic))
            finally:
                searcher.close()

    def test_live_bad_key_preserves_index_and_search_degrades(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            api_dir = root / "docs" / "API" / "ArkData"
            api_dir.mkdir(parents=True)
            (api_dir / "cj-apis-relational_store.md").write_text(SAMPLE_API, encoding="utf-8")
            cfg = self.live_cfg(root)
            cfg.embedding_mode = "off"
            build_index(cfg, quiet=True)
            original = Path(cfg.index_path).read_bytes()

            cfg.embedding_mode = "all"
            cfg.embedding.api_key = "bad-key"
            with self.assertRaisesRegex(RuntimeError, "embedding index incomplete"):
                build_index(cfg, quiet=True)
            self.assertEqual(Path(cfg.index_path).read_bytes(), original)

            cfg.embedding_mode = "search"
            searcher = Searcher(cfg)
            try:
                results = searcher.search("getRdbStore", embedding_mode="search", top_k=1)
                self.assertEqual(results[0]["title"], "func getRdbStore(UIAbilityContext, StoreConfig)")
            finally:
                searcher.close()


if __name__ == "__main__":
    unittest.main()
