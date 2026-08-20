---
name: cangjie-harmonyos-knowledge
description: "Use this skill to retrieve packaged local documentation for Cangjie HarmonyOS platform development: ArkUI components and modifiers, HarmonyOS Kits and system APIs, permissions, SysCaps, lifecycle, configuration, platform error codes, guides, and Cangjie-versus-ArkTS API differences. Use cangjie-coding for Cangjie language, std/stdx API, or cjpm knowledge; use harmonyos-project-bootstrap to provision HarmonyOS stdx binaries."
---

# Cangjie HarmonyOS Knowledge

## Retrieval Workflow

Treat the current `SKILL.md` directory as `<skill-root>`. The public CLI is `<skill-root>/scripts/knowledge.py`; packaged data is under `<skill-root>/data`. Both resolve independently of whether the skills container is `.agents`, `.claude`, or another directory.

```powershell
python -B <skill-root>/scripts/knowledge.py doctor --strict
python -B <skill-root>/scripts/knowledge.py query "TextInput onChange" --top-k 3
python -B <skill-root>/scripts/knowledge.py symbol Button
python -B <skill-root>/scripts/knowledge.py read "docs/API/arkui-cj/cj-text-input-textinput.md#func-onchangestring---unit"
```

1. Run `doctor --strict` once per task or after copying/updating the skill.
2. Before coding, combine up to five independent concrete lookups in one shell invocation; keep each query focused on one API, component, error, permission, or intent and keep `--top-k` at 3.
3. Select results by `ref`, `breadcrumb`, signature, and snippet. Do not select by title alone.
4. Use `read <ref>` only when the snippet lacks parameters, exceptions, constraints, permissions, SysCap, or a complete example. The ref must include the exact `#anchor`; never read a whole document during ordinary API lookup. Use `--mode full` only when the task explicitly requires whole-document context.
5. Cite the selected `ref` in implementation notes or the final handoff.
6. Search is adaptive by default: strong deterministic matches return immediately, while weak matches use the packaged vectors when the configured embedding service is available. If status reports `embedding-degraded`, rewrite with English API symbols plus short Chinese intent words.

Without a configured query-embedding provider, the fallback is symbol/FTS/structure retrieval, not a semantic model. It remains authoritative for API symbols and concrete platform terms, but heavily paraphrased natural-language requests may miss; do not treat the offline semantic diagnostic score as equivalent to the online quality gate.

The query boundary rejects high-confidence unrelated subjects and competing technology ecosystems before lexical or vector retrieval. An empty result is therefore expected for clearly out-of-domain requests. Keep HarmonyOS/OpenHarmony/ArkUI/Cangjie markers in comparison or migration queries so the platform side remains explicit.

For recurring ArkUI agent patterns, include the contract-bearing names in the focused query: `Canvas CanvasRenderingContext2D 显式类型`, `ForEach ItemGeneratorFunc KeyGeneratorFunc 回调`, `@Prop 父子单向同步`, or `@Builder bind CustomView`. The returned signature or guide section is the source of truth; do not infer callback shapes from ArkTS syntax.

Stop after the first batch when signatures and snippets are sufficient. Do not query familiar cosmetic modifiers such as `fontColor`, `padding`, `margin`, or `borderRadius` one by one when an existing project/template already demonstrates them. Run a second lookup only for a missing contract, a compiler/runtime error, or a genuinely new API boundary.

Before the first source edit, the platform-knowledge budget is one `doctor`, one query command containing at most five `query` calls, and at most two anchored `read` calls. Exceeding that budget without a named missing contract is a workflow failure. After editing starts, query again only against an exact compiler/runtime symptom.

`symbol <name>` returns the exact symbol and signature by default. Add `--members` or `--examples` only when the task needs those expansions; broad classes such as `JSValue` otherwise produce unnecessarily large responses.

```powershell
python -B <skill-root>/scripts/knowledge.py query "Web darkMode forceDarkAccess" --top-k 5
python -B <skill-root>/scripts/knowledge.py query "相机 预览 createPreviewOutput PhotoSession" --top-k 5
```

Use HTTP or MCP only for a long-lived integration, not for ordinary coding-agent queries:

```powershell
python -B <skill-root>/scripts/knowledge.py serve --port 8765
python -B <skill-root>/scripts/knowledge.py mcp
```

## Routing

| Need | Use |
| --- | --- |
| HarmonyOS API, ArkUI, Guide, permissions, SysCap | `scripts/knowledge.py query` |
| Cangjie syntax, language features, std/stdx API, cjpm | `cangjie-coding` |
| Download or configure HarmonyOS stdx binaries | `harmonyos-project-bootstrap` |
| Cangjie syntax, collection, conversion, or cjpm error | `cangjie-coding`; then `harmonyos-build-run-diagnose` for build workflow |
| Hvigor, ArkUI, HarmonyOS platform, or device error | This knowledge index; then `harmonyos-build-run-diagnose` |
| ArkTS/Cangjie interop | `cangjie-arkts-interop` |

## Guardrails

- Do not use the removed remote doc-search path.
- Do not browse all raw documentation files to guess an API. Use the index; fall back to the exact raw `ref` only when the index is unavailable.
- When inspecting an application project, exclude `.agents/`, `.claude/`, and other Skill containers from recursive file listings.
- Treat `scripts/knowledge.py` as an executable knowledge tool: inspect `--help` and query it, but do not read `scripts/knowledge_core/` during an application-development task.
- Do not assume an ArkTS object literal, callback, unit, or collection member is valid Cangjie.
- If `doctor --strict` fails, run the maintenance procedure before relying on results.
- Read `references/maintenance.md` only when auditing, rebuilding, updating, or evaluating this knowledge package.

## Packaged Embeddings

The release index contains 256-dimensional vectors for every section. Search-time embedding reads credentials from an environment variable:

```powershell
$env:DASHSCOPE_API_KEY = "<secure value>"
python -B <skill-root>/scripts/knowledge.py query "persist user settings across app launches"
```

Layered config may set `[knowledge].version` and `[knowledge.embedding]` in `cangjie.skills.toml`. `knowledge.embedding.mode` accepts `off`, `search`, `index`, or `all`; the default is `search`. Missing credentials and query-time provider failures degrade to deterministic retrieval. Do not configure docs or index paths; they are packaged inside this skill.

Embedding search is adaptive. High-confidence symbol/FTS results return without an API call or vector scan. Weak lexical queries use dense retrieval when matching vectors exist. Long random identifiers, explicit technical identifiers absent from the corpus, and dense matches below `min_similarity` are rejected. Provider errors fall back to deterministic results.

The built-in profile uses `text-embedding-v4`, 256 dimensions, batches of 10, and `min_similarity = 0.40`. `doctor --strict` verifies full vector coverage and the configured provider/model/dimension profile. A release rebuild requested with `index` or `all` fails atomically if credentials are missing or any document vector is unavailable.

Never write API keys to repository files, command arguments, logs, MCP config, prompts, or generated reports.
