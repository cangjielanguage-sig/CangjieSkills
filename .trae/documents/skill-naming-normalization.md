# Skill 目录命名规范化计划

## 背景

根据 `D:\cangjie_skills\docs\skills_spec\Skill 开发规范.md` 第 2 章命名规范：

* **2.1 目录命名**：MUST 使用 kebab-case `^[a-z0-9]+(-[a-z0-9]+)*$`

* **2.2 前缀约定**：统一使用 `cangjie-` 前缀；HarmonyOS 平台 Skill 使用 `cangjie-hmos-` 前缀

## 当前问题

### 需要重命名的 Skill（10 个）

| #  | 当前目录名                                      | 规范目录名                                 | 违规原因                                     |
| -- | ------------------------------------------ | ------------------------------------- | ---------------------------------------- |
| 1  | `agent-skill-evolution`                    | `cangjie-skill-evolution`             | 缺少 `cangjie-` 前缀                         |
| 2  | `skill-lint-fix`                           | `cangjie-skill-lint-fix`              | 缺少 `cangjie-` 前缀                         |
| 3  | `harmonyos-app-diagnose`                   | `cangjie-hmos-app-diagnose`           | 缺少 `cangjie-` 前缀，`harmonyos-` 应为 `hmos-` |
| 4  | `harmonyos-build`                          | `cangjie-hmos-build`                  | 缺少 `cangjie-` 前缀，`harmonyos-` 应为 `hmos-` |
| 5  | `harmonyos-evolution`                      | `cangjie-hmos-evolution`              | 缺少 `cangjie-` 前缀，`harmonyos-` 应为 `hmos-` |
| 6  | `harmonyos-project-init`                   | `cangjie-hmos-project-init`           | 缺少 `cangjie-` 前缀，`harmonyos-` 应为 `hmos-` |
| 7  | `harmonyos-requirements`                   | `cangjie-hmos-requirements`           | 缺少 `cangjie-` 前缀，`harmonyos-` 应为 `hmos-` |
| 8  | `harmonyos-stdx`                           | `cangjie-hmos-stdx`                   | 缺少 `cangjie-` 前缀，`harmonyos-` 应为 `hmos-` |
| 9  | `cangjie-harmonyos-doc-search`             | `cangjie-hmos-doc-search`             | `harmonyos` 应缩写为 `hmos`                  |
| 10 | `cangjie-harmonyos-doc-search-maintenance` | `cangjie-hmos-doc-search-maintenance` | `harmonyos` 应缩写为 `hmos`                  |

### 已符合规范的 Skill（5 个，无需修改）

* `cangjie-arkts-interop` ✓

* `cangjie-lang-features` ✓

* `cangjie-original-docs` ✓

* `cangjie-std` ✓

* `cangjie-stdx` ✓

## 实施步骤

### 步骤 1：重命名目录

对 10 个 Skill 执行目录重命名（`Move-Item`）：

```
agent-skill-evolution → cangjie-skill-evolution
skill-lint-fix → cangjie-skill-lint-fix
harmonyos-app-diagnose → cangjie-hmos-app-diagnose
harmonyos-build → cangjie-hmos-build
harmonyos-evolution → cangjie-hmos-evolution
harmonyos-project-init → cangjie-hmos-project-init
harmonyos-requirements → cangjie-hmos-requirements
harmonyos-stdx → cangjie-hmos-stdx
cangjie-harmonyos-doc-search → cangjie-hmos-doc-search
cangjie-harmonyos-doc-search-maintenance → cangjie-hmos-doc-search-maintenance
```

### 步骤 2：更新 SKILL.md frontmatter 中的 `name` 字段

每个重命名的 Skill 的 `SKILL.md` 中 `name` 字段必须与目录名一致（规范 C-9）：

| 文件                                             | 旧 name                                     | 新 name                                |
| ---------------------------------------------- | ------------------------------------------ | ------------------------------------- |
| `cangjie-skill-evolution/SKILL.md`             | `agent-skill-evolution`                    | `cangjie-skill-evolution`             |
| `cangjie-skill-lint-fix/SKILL.md`              | `skill-lint-fix`                           | `cangjie-skill-lint-fix`              |
| `cangjie-hmos-app-diagnose/SKILL.md`           | `harmonyos-app-diagnose`                   | `cangjie-hmos-app-diagnose`           |
| `cangjie-hmos-build/SKILL.md`                  | `harmonyos-build`                          | `cangjie-hmos-build`                  |
| `cangjie-hmos-evolution/SKILL.md`              | `harmonyos-evolution`                      | `cangjie-hmos-evolution`              |
| `cangjie-hmos-project-init/SKILL.md`           | `harmonyos-project-init`                   | `cangjie-hmos-project-init`           |
| `cangjie-hmos-requirements/SKILL.md`           | `harmonyos-requirements`                   | `cangjie-hmos-requirements`           |
| `cangjie-hmos-stdx/SKILL.md`                   | `harmonyos-stdx`                           | `cangjie-hmos-stdx`                   |
| `cangjie-hmos-doc-search/SKILL.md`             | `cangjie-harmonyos-doc-search`             | `cangjie-hmos-doc-search`             |
| `cangjie-hmos-doc-search-maintenance/SKILL.md` | `cangjie-harmonyos-doc-search-maintenance` | `cangjie-hmos-doc-search-maintenance` |

同时更新子 Skill 的 name：
\| `cangjie-hmos-doc-search/doc-card/SKILL.md` | `doc-card` | `doc-card`（子 Skill 短名称，无需改） |
\| `cangjie-hmos-doc-search/doc-graph/SKILL.md` | `doc-graph` | `doc-graph`（子 Skill 短名称，无需改） |

### 步骤 3：更新 SKILL.md 正文中对旧名称的引用

在所有 SKILL.md 文件中，将旧名称引用替换为新名称。涉及文件：

1. **`cangjie-skill-evolution/SKILL.md`**：`skill-lint-fix` → `cangjie-skill-lint-fix`
2. **`cangjie-skill-evolution/README.md`**：`agent-skill-evolution` → `cangjie-skill-evolution`，`skill-lint-fix` → `cangjie-skill-lint-fix`
3. **`cangjie-hmos-app-diagnose/SKILL.md`**：路径中 `harmonyos-app-diagnose` → `cangjie-hmos-app-diagnose`
4. **`cangjie-hmos-build/SKILL.md`**：`harmonyos-evolution` → `cangjie-hmos-evolution`，`cangjie-harmonyos-doc-search` → `cangjie-hmos-doc-search`，路径中 `harmonyos-build` → `cangjie-hmos-build`
5. **`cangjie-hmos-evolution/SKILL.md`**：`harmonyos-build` → `cangjie-hmos-build`
6. **`cangjie-hmos-project-init/SKILL.md`**：路径中 `harmonyos-project-init` → `cangjie-hmos-project-init`，`harmonyos-build` → `cangjie-hmos-build`，`harmonyos-evolution` → `cangjie-hmos-evolution`
7. **`cangjie-hmos-requirements/SKILL.md`**：`cangjie-harmonyos-doc-search` → `cangjie-hmos-doc-search`，`harmonyos-build` → `cangjie-hmos-build`，`harmonyos-app-diagnose` → `cangjie-hmos-app-diagnose`，`harmonyos-evolution` → `cangjie-hmos-evolution`
8. **`cangjie-hmos-stdx/SKILL.md`**：路径中 `harmonyos-stdx` → `cangjie-hmos-stdx`，`cangjie-harmonyos-doc-search` → `cangjie-hmos-doc-search`
9. **`cangjie-hmos-doc-search/SKILL.md`**：路径中 `cangjie-harmonyos-doc-search` → `cangjie-hmos-doc-search`
10. **`cangjie-hmos-doc-search/doc-card/SKILL.md`**：`cangjie-harmonyos-doc-search-maintenance` → `cangjie-hmos-doc-search-maintenance`，路径中 `cangjie-harmonyos-doc-search` → `cangjie-hmos-doc-search`
11. **`cangjie-hmos-doc-search/doc-graph/SKILL.md`**：`cangjie-harmonyos-doc-search-maintenance` → `cangjie-hmos-doc-search-maintenance`，路径中 `cangjie-harmonyos-doc-search` → `cangjie-hmos-doc-search`
12. **`cangjie-hmos-doc-search-maintenance/SKILL.md`**：`cangjie-harmonyos-doc-search` → `cangjie-hmos-doc-search`，路径中 `cangjie-harmonyos-doc-search-maintenance` → `cangjie-hmos-doc-search-maintenance`
13. **`cangjie-arkts-interop/SKILL.md`**：路径中 `cangjie-harmonyos-doc-search` → `cangjie-hmos-doc-search`

### 步骤 4：更新 Python 脚本中的目录名引用

涉及文件（约 20+ 处）：

1. **`cangjie-hmos-doc-search/doc-card/search_v3.py`**：`cangjie-harmonyos-doc-search-maintenance` → `cangjie-hmos-doc-search-maintenance`
2. **`cangjie-hmos-doc-search/unified_search.py`**：`cangjie-harmonyos-doc-search` → `cangjie-hmos-doc-search`
3. **`cangjie-hmos-doc-search/doc-graph/cli.py`**：`cangjie-harmonyos-doc-search-maintenance` → `cangjie-hmos-doc-search-maintenance`
4. **`cangjie-hmos-doc-search-maintenance/graph/scripts/validate_graph_data.py`**：`cangjie-harmonyos-doc-search` → `cangjie-hmos-doc-search`
5. **`cangjie-hmos-doc-search-maintenance/graph/scripts/docs_statistics.py`**：同上
6. **`cangjie-hmos-doc-search-maintenance/graph/evals/run_eval.py`**：同上
7. **`cangjie-hmos-doc-search-maintenance/graph/builder/build_cli.py`**：同上
8. **`cangjie-hmos-doc-search-maintenance/fusion/scripts/run_release_eval.py`**：两处引用
9. **`cangjie-hmos-doc-search-maintenance/fusion/scripts/run_maintenance.py`**：同上
10. **`cangjie-hmos-doc-search-maintenance/fusion/scripts/generate_appdev_eval_batch3_blind.py`**：同上
11. **`cangjie-hmos-doc-search-maintenance/fusion/scripts/regenerate_15k_independent_evals.py`**：同上
12. **`cangjie-hmos-doc-search-maintenance/fusion/scripts/run_ab_eval.py`**：同上
13. **`cangjie-hmos-doc-search-maintenance/card/scripts/run_v3_regression_gate.py`**：同上
14. **`cangjie-hmos-doc-search-maintenance/card/scripts/sync_v3_to_graph.py`**：两处引用
15. **`cangjie-hmos-doc-search-maintenance/card/scripts/run_corpus_expansion.py`**：两处引用
16. **`cangjie-hmos-doc-search-maintenance/card/scripts/run_maintenance.py`**：同上
17. **`cangjie-hmos-doc-search-maintenance/card/scripts/run_semantic_capability_gate.py`**：同上
18. **`cangjie-hmos-doc-search-maintenance/card/scripts/repair_llm_failure_cache.py`**：三处引用
19. **`cangjie-hmos-doc-search-maintenance/card/scripts/run_ab_eval.py`**：两处引用
20. **`cangjie-hmos-doc-search-maintenance/card/scripts/eval_bench.py`**：同上
21. **`cangjie-hmos-doc-search-maintenance/card/scripts/enrich_existing_index_appdev.py`**：同上
22. **`cangjie-hmos-doc-search-maintenance/card/scripts/audit_api_coverage.py`**：同上
23. **`cangjie-hmos-doc-search-maintenance/card/scripts/audit_coverage.py`**：同上
24. **`cangjie-hmos-doc-search-maintenance/card/scripts/build_doc_manifest.py`**：同上
25. **`cangjie-hmos-doc-search-maintenance/card/builder/build_index_v3.py`**：两处引用
26. **`cangjie-hmos-stdx/scripts/fetch_stdx.py`**：`harmonyos-stdx` → `cangjie-hmos-stdx`
27. **`cangjie-skill-evolution/evals/validate_evolution.py`**：`skill-lint-fix` → `cangjie-skill-lint-fix`
28. **`cangjie-hmos-build/evals/validate_build_steps.py`**：`harmonyos-evolution` → `cangjie-hmos-evolution`

### 步骤 5：更新 evals JSONL 文件中的 skill name 引用

涉及文件：

1. **`cangjie-skill-evolution/evals/discovery.jsonl`**：`agent-skill-evolution` → `cangjie-skill-evolution`
2. **`cangjie-skill-lint-fix/evals/discovery.jsonl`**：`skill-lint-fix` → `cangjie-skill-lint-fix`
3. **`cangjie-hmos-app-diagnose/evals/discovery.jsonl`**：`harmonyos-app-diagnose` → `cangjie-hmos-app-diagnose`
4. **`cangjie-hmos-build/evals/discovery.jsonl`**：`harmonyos-build` → `cangjie-hmos-build`
5. **`cangjie-hmos-build/evals/content-basic.jsonl`**：`harmonyos-evolution` → `cangjie-hmos-evolution`
6. **`cangjie-hmos-evolution/evals/discovery.jsonl`**：`harmonyos-evolution` → `cangjie-hmos-evolution`
7. **`cangjie-hmos-project-init/evals/discovery.jsonl`**：`harmonyos-project-init` → `cangjie-hmos-project-init`
8. **`cangjie-hmos-requirements/evals/discovery.jsonl`**：`harmonyos-requirements` → `cangjie-hmos-requirements`
9. **`cangjie-hmos-stdx/evals/discovery.jsonl`**：`harmonyos-stdx` → `cangjie-hmos-stdx`
10. **`cangjie-hmos-stdx/evals/content-basic.jsonl`**：`harmonyos-stdx` → `cangjie-hmos-stdx`
11. **`cangjie-hmos-doc-search/evals/discovery.jsonl`**：`cangjie-harmonyos-doc-search` → `cangjie-hmos-doc-search`
12. **`cangjie-hmos-doc-search/evals/content-basic.jsonl`**：`cangjie-harmonyos-doc-search` → `cangjie-hmos-doc-search`
13. **`cangjie-hmos-doc-search-maintenance/evals/discovery.jsonl`**：`cangjie-harmonyos-doc-search-maintenance` → `cangjie-hmos-doc-search-maintenance`
14. **`cangjie-hmos-doc-search-maintenance/evals/content-basic.jsonl`**：`cangjie-harmonyos-doc-search` → `cangjie-hmos-doc-search`
15. **`cangjie-hmos-doc-search-maintenance/card/evals/discovery.jsonl`**：`cangjie-harmonyos-doc-search-maintenance` → `cangjie-hmos-doc-search-maintenance`
16. **`cangjie-hmos-doc-search-maintenance/card/evals/content-basic.jsonl`**：`cangjie-harmonyos-doc-search` → `cangjie-hmos-doc-search`

### 步骤 6：更新其他 Markdown 文件中的引用

1. **`cangjie-hmos-doc-search-maintenance/README.md`**：所有 `cangjie-harmonyos-doc-search` → `cangjie-hmos-doc-search`，`cangjie-harmonyos-doc-search-maintenance` → `cangjie-hmos-doc-search-maintenance`
2. **`cangjie-hmos-doc-search-maintenance/card/references/workflow-overview.md`**：同上
3. **`cangjie-hmos-doc-search-maintenance/card/docs/card-recommendation-guide.md`**：同上
4. **`cangjie-hmos-doc-search-maintenance/card/records/expansion-8k-to-15k.md`**：同上
5. **`cangjie-hmos-build/evals/fixtures/mock-build-evolution-failure/Evolution.md`**：`harmonyos-build` → `cangjie-hmos-build`

### 步骤 7：验证

* 确认所有目录名符合 `^[a-z0-9]+(-[a-z0-9]+)*$` 正则

* 确认所有 SKILL.md 的 `name` 字段与目录名一致

* 确认无残留的旧名称引用（grep 检查）

