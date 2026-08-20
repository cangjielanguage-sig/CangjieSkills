# Knowledge Package Maintenance

Read this file only when auditing, updating, rebuilding, or evaluating the packaged knowledge base.

## Package Boundary

- `data/docs/`: authoritative packaged Markdown source for HarmonyOS platform APIs and guides.
- `data/index.sqlite`: derived release index with complete 256-dimensional document vectors; it must be reproducible from `data/docs/`.
- `scripts/knowledge.py`: public CLI.
- `scripts/knowledge_core/`: retrieval, indexing, query embedding, HTTP, and MCP implementation.
- `tests/cases/`: standard, holdout, semantic, and unrelated-domain evaluation cases.
- `scripts/evaluate.py`: evaluation runner.

Keep Cangjie language, std/stdx API, and cjpm knowledge in `cangjie-coding`. Keep HarmonyOS stdx binary provisioning in `harmonyos-project-bootstrap`. Do not duplicate either resource here.

## Quality Gate

Run from any directory:

```powershell
python -B <skill-root>/scripts/knowledge.py doctor --strict
python -B <skill-root>/scripts/run_tests.py
python -B <skill-root>/scripts/evaluate.py --embedding-mode off --fail-under 1.00 --max-p95-ms 750
python -B <skill-root>/scripts/evaluate.py --cases <skill-root>/tests/cases/holdout.json --embedding-mode off --fail-under 0.90 --max-p95-ms 750
python -B <skill-root>/scripts/evaluate.py --cases <skill-root>/tests/cases/semantic.json --embedding-mode off --fail-under 0.40 --max-p95-ms 750
python -B <skill-root>/scripts/evaluate.py --cases <skill-root>/tests/cases/ood.json --embedding-mode off --fail-under 1.00 --max-p95-ms 750
python -B <skill-root>/scripts/evaluate.py --cases <skill-root>/tests/cases/agent_patterns.json --embedding-mode off --fail-under 1.00 --max-p95-ms 750
```

`doctor --strict` must report a healthy source/index mapping, FTS integrity, full configured-vector coverage, and at least 99% document and anchor resolution for internal links. The deterministic retrieval evaluation must pass before packaging.
The evaluation reports pass rate, MRR, nDCG, top-1 accuracy, and p50/p95 latency. Keep held-out cases independent from query aliases and require every case to satisfy its declared maximum relevant rank.

The no-credential gate is intentionally split: `retrieval` and `holdout` protect deterministic API lookup, `agent_patterns` protects recurring code-generation contracts, `ood` protects the domain boundary, and the offline `semantic` score is only a diagnostic floor. Offline fallback has no query embedding and must not be presented as semantic retrieval quality. The online semantic gate below is the release claim for paraphrased natural-language retrieval. `--max-p95-ms 750` is the deterministic regression line for the packaged corpus on a normal local/CI machine; investigate sustained regressions instead of silently increasing it.

## Release Rebuild and Compact

Release builds require embeddings and fail atomically rather than replacing the previous index with an incomplete artifact:

```powershell
$env:DASHSCOPE_API_KEY = "<value>"
python -B <skill-root>/scripts/knowledge.py build --embedding-mode index
python -B <skill-root>/scripts/knowledge.py versions compact
python -B <skill-root>/scripts/knowledge.py doctor --strict
python -B <skill-root>/scripts/evaluate.py --embedding-mode search --embedding-dimensions 256 --require-embeddings --fail-under 1.00 --max-p95-ms 5000
python -B <skill-root>/scripts/evaluate.py --cases <skill-root>/tests/cases/semantic.json --embedding-mode search --embedding-dimensions 256 --require-embeddings --fail-under 0.95 --max-p95-ms 5000
python -B <skill-root>/scripts/evaluate.py --cases <skill-root>/tests/cases/ood.json --embedding-mode search --embedding-dimensions 256 --require-embeddings --fail-under 1.00 --max-p95-ms 5000
python -B <skill-root>/scripts/evaluate.py --cases <skill-root>/tests/cases/agent_patterns.json --embedding-mode search --embedding-dimensions 256 --require-embeddings --fail-under 1.00 --max-p95-ms 5000
```

Use `--incremental` only when updating the same named document version. Use a distinct `--version` when sources represent another SDK/document release.

The release package does not include `vector_cache.sqlite`; it is a rebuild/query optimization rather than runtime knowledge. The default query cache is `~/.cangjie/cache/cangjie-harmonyos-knowledge/vector_cache.sqlite`. Retrieval continues without cached query vectors when the cache is unavailable.

## Provider Validation

Validate the provider on a small temporary corpus before a full build. Keep the key in `DASHSCOPE_API_KEY` and never in TOML:

```powershell
$env:CANGJIE_KNOWLEDGE_RUN_LIVE_EMBEDDING = "1"
$env:DASHSCOPE_API_KEY = "<secure value>"
python -B <skill-root>/scripts/run_tests.py
```

For dimension experiments, keep alternate indexes outside the packaged `data/` directory:

```powershell
python -B <skill-root>/scripts/knowledge.py --index-dir <temp-index> --embedding-dimensions 256 build --embedding-mode index
python -B <skill-root>/scripts/evaluate.py --index-dir <temp-index> --embedding-mode search --embedding-dimensions 256
python -B <skill-root>/scripts/evaluate.py --cases <skill-root>/tests/cases/semantic.json --index-dir <temp-index> --embedding-mode search --embedding-dimensions 256 --fail-under 0
python -B <skill-root>/scripts/evaluate.py --cases <skill-root>/tests/cases/ood.json --index-dir <temp-index> --embedding-mode search --embedding-dimensions 256 --fail-under 0
```

On the current 12,324-section corpus, 256 dimensions are the release default and 512 is the quality-first experimental option. The tested 1024/2048 dimensions did not improve semantic pass rate over 512 and substantially increased brute-force scan latency.

## Update Checklist

1. Replace or add source Markdown under the correct `API` or `Guide` hierarchy.
2. Rebuild the index atomically.
3. Run strict doctor, unit tests, deterministic evaluation, 256-dimensional semantic evaluation, and OOD evaluation.
4. Add or update evaluation cases for every proven retrieval regression.
5. Scan the full solution and test artifacts for plaintext secrets and Python cache files.
6. Re-run at least one clean-project build and one emulator interaction scenario when API examples or templates changed.
