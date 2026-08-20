# Configuration

Use one TOML contract everywhere: `cangjie.skills.toml`. Configuration is optional; copy the annotated example from the repository `config/` directory and keep only intentional overrides.

## Unified discovery and doctor report

Run one bounded, read-only discovery command before manually searching for toolchain or project metadata:

```powershell
python -B <cangjie-harmonyos-dev-skill>/tools/doctor.py --project-root . --json
```

The versioned JSON report includes:

- every loaded configuration file and the final highest-precedence file;
- the effective DevEco, Cangjie SDK, and `hdc` path, value source, existence, and available version details;
- the effective module, bundle, ability, and newest/overridden HAP with a source for each value;
- the configured device target, connected targets, and a device state derived from both `hdc` output text and its exit status;
- separate `ready.build` and `ready.runtime` results, plus a machine-readable `inspection.stop` condition.

The report never prints environment values for credentials. `--no-device-check` is available for offline CI. Add `--strict` only when a non-zero exit is desired unless both build and runtime readiness pass. CLI overrides accepted by the doctor follow the same precedence as the build/run tools; use `--help` for the complete list.

When the report contains the required fields, use it instead of recursively reading `.agents/`, templates, packaged knowledge bodies, indexes, `oh_modules`, or build output. Expand inspection only for a missing report field or a concrete later failure.

## Locations and precedence

Value precedence is:

1. CLI argument
2. Direct environment value such as `DEVECO_HOME`, `CANGJIE_SDK_HOME`, or the API-key variable named by `api_key_env`
3. Explicit `--config` files; when a tool accepts repeated flags, the last file wins
4. File named by `CANGJIE_SKILLS_CONFIG`
5. Project file: `<project>/cangjie.skills.toml`
6. User file: `~/.cangjie/cangjie.skills.toml`
7. Automatic detection or the built-in default

Passing `--config` replaces automatic file discovery. Partial files are supported: omitted values retain the lower layer or built-in default. Unknown sections, unknown keys, invalid types, invalid ranges, blank auto-detection overrides, and plaintext `api_key` fields fail with the full key name instead of being ignored.

Missing paths passed with `--config` or `CANGJIE_SKILLS_CONFIG` fail with the requested path. Only absent user and project files discovered at their default locations are skipped.

Store only environment-variable names in configuration. Never store a credential value in TOML, CLI arguments, logs, prompts, or reports.

## Toolchain and device

| Key | Default | Fallback behavior |
| --- | --- | --- |
| `toolchain.deveco_home` | automatic | `DEVECO_HOME`, then the platform default DevEco installation; fail with a path-specific hint if absent |
| `toolchain.cangjie_sdk` | automatic | Used by builds and HarmonyOS stdx setup. Try `CANGJIE_SDK_HOME`, then the newest valid `~/.cangjie-sdk/*/cangjie`, then `~/.cangjie-sdk/6.1/cangjie`; fail if absent |
| `toolchain.hdc` | automatic | `hdc` on `PATH`, then the standard DevEco toolchains path; fail if absent |
| `toolchain.ohpm_registry` | `https://ohpm.openharmony.cn/ohpm/` | Use the built-in registry when omitted; a malformed URL is rejected |
| `toolchain.verify_tls` | `true` | Keep certificate verification enabled; set `false` only for a trusted private registry |
| `device.target` | `127.0.0.1:5555` | Use the local x64 emulator; override with an `hdc list targets` identifier for a device or another emulator |

Machine-specific paths normally belong in `~/.cangjie/cangjie.skills.toml`. `device.target` is shared by UI capture and hilog capture.

## Runtime detection overrides

| Key | Default | Fallback behavior |
| --- | --- | --- |
| `runtime.bundle` | automatic | Read `bundleName` from `AppScope/app.json5`; fail only when launch requires it and detection fails |
| `runtime.ability` | automatic | Read the selected module's `module.json5`; fail only when launch requires it and detection fails |
| `runtime.module` | automatic | Use the sole module, otherwise `entry`, otherwise the first declared module with a warning |
| `runtime.hap` | automatic | Use the newest HAP under the selected module; warn when several outputs exist |

Omit these values for ordinary projects. Set them only for ambiguous multi-module or multi-ability projects. Relative HAP paths resolve from the project root.

## Project scaffolding

| Key | Default | Fallback behavior |
| --- | --- | --- |
| `scaffold.app_name` | generator default | Pure project: `Cangjie App`; hybrid project: `Cangjie ArkTS Hybrid` |
| `scaffold.bundle_name` | generator default | Pure project: `com.example.myapplication`; hybrid project: `com.example.hybrid` |
| `scaffold.module_name` | `entry` | Generate the entry HAP module under this directory/name |

`[scaffold]` contains only identity inputs whose meaning is shared by pure Cangjie and hybrid generators. It affects project creation and template repair only; existing projects remain authoritative in `AppScope/app.json5`, root `build-profile.json5`, and module configuration.

Generator-specific advanced values stay on the generator CLI:

- The pure Stage template pins its internal Cangjie package/library to `ohos_app_cangjie_entry`; it is not configurable.
- Pure-project `--vendor` changes `app.json5.vendor`.
- Hybrid `--package-name` changes the Cangjie native library/package and synchronized ArkTS type paths.
- `--sdk-version` and `--model-version` are advanced template compatibility overrides. Omit them to use the packaged, verified defaults.

## Knowledge retrieval

| Key | Default | Fallback behavior |
| --- | --- | --- |
| `knowledge.version` | `default` | Search the packaged default index version; CLI `--version all` can search all ready versions |

The documentation and index locations are packaged resources and are intentionally not configurable.

### Embeddings

| Key | Default | Fallback behavior |
| --- | --- | --- |
| `knowledge.embedding.mode` | `search` | `search`: use packaged document vectors for weak queries; `off`: deterministic-only retrieval; `index`: strict document-vector build; `all`: strict build plus search. Query-time failures degrade to deterministic retrieval; incomplete index builds fail and preserve the previous index |
| `knowledge.embedding.api_format` | `dashscope` | `dashscope` uses the native shape; `openai` uses `/embeddings`. Other values are rejected during config loading |
| `knowledge.embedding.model` | `text-embedding-v4` | Query-time model failures fall back deterministically; strict index builds fail and preserve the previous index |
| `knowledge.embedding.base_url` | DashScope text-embedding URL | A valid absolute HTTP(S) URL is required; malformed URLs fail config loading. For `openai`, configure the API root before `/embeddings` |
| `knowledge.embedding.api_key_env` | `DASHSCOPE_API_KEY` | Read the credential at runtime. An unset variable disables query embeddings but causes an explicitly requested index build to fail before changing the index |
| `knowledge.embedding.dimensions` | `256` | Positive integer. Balanced default for `text-embedding-v4`; use `512` for quality-first retrieval or set the dimension required by another model. Unsupported dimensions fall back during queries and fail strict index builds |
| `knowledge.embedding.min_similarity` | `0.40` | Reject weaker dense matches; valid range is 0–1. Lower only when a held-out evaluation proves useful recall is being lost |
| `knowledge.embedding.batch_size` | `10` | Positive integer. Process ten texts per request; invalid values fail config loading. Provider batch failures follow the query/build behavior defined by `mode` |
| `knowledge.embedding.timeout_seconds` | `60.0` | After timeout, queries fall back deterministically; strict index builds fail and preserve the previous index |
| `knowledge.embedding.max_retries` | `2` | Retry transient failures and HTTP 429; after exhaustion, queries fall back and strict index builds fail. Ordinary 4xx failures are not retried |

The packaged index contains complete 256-dimensional vectors and defaults to `search`. High-confidence deterministic results bypass the vector service, while weak natural-language or cross-language queries use dense retrieval. Missing credentials, unknown technical identifiers, low-similarity matches, and query-time provider failures reject or fall back without disabling symbol, FTS, example, or anchored-document retrieval. Use `off` only when deterministic-only operation is intentional; use `index` or `all` only for release maintenance.

Use 256 dimensions for the default speed/storage/quality balance. Use 512 when semantic recall matters more than local scan latency. With the current SQLite/Python scan, 1024 and 2048 are valid but not recommended because full-corpus testing found no pass-rate gain over 512.

Transient per-run controls such as capture wait time, retry count, output directory, query `top-k`, and incremental rebuild mode remain CLI arguments. Keeping them out of shared configuration prevents stale task-specific state.
