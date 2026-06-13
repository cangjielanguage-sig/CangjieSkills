## Rollout Record

- rollout_id: cangjie-testcase-xmind-20260613-105118-001
- target_skill: cangjie-testcase-xmind
- task_id: abilitykit-error-observer-xmind
- outcome: partial
- trace_outcome: not_verified
- adjudicated_outcome: partial
- outcome_source: ground_truth
- ground_truth_status: provided
- trace_runtime: codex
- trace_source: codex session 019ebed1-1b5e-73d0-9d4c-4f8fc240a721 (rollout-2026-06-13T10-30-42-019ebed1-1b5e-73d0-9d4c-4f8fc240a721.jsonl)
- collection_confidence: high
- original_task: [$cangjie-testcase-xmind](D:\\cangjie_skills\\CangjieSkills\\.agents\\skills\\cangjie-testcase-xmind\\SKILL.md) [$cangjie-rollout-collector](D:\\cangjie_skills\\CangjieSkills\\.agents\\skills\\cangjie-rollout-collector\\SKILL.md) 请帮我设计 D:\cangjie_dev\docs_cangjie\zh-cn\application-dev\reference\AbilityKit\cj-apis-application-error_observer.md 脑图
- key_constraints: none
- skill_used: cangjie-testcase-xmind
- summary: Collected 27 trace events; trace_outcome=not_verified; ground_truth adjudicated outcome is partial. No trace verification evidence was found.

### Observable Steps

| step | trace_ref | action/tool | input/params | public rationale | observed result | used_experience |
| --- | --- | --- | --- | --- | --- | --- |
| S1 | T001 | user_message | [$cangjie-testcase-xmind](D:\\cangjie_skills\\CangjieSkills\\.agents\\skills\\cangjie-testcase-xmind\\SKILL.md) [$cangjie-rollout-collector](D:\\cangjie_skills\\CangjieSkills\\.agents\\skills\\cangjie-rollout-collector\\SKILL.md) 请帮我设计 D:\cangjie_dev\docs_cangjie\zh-cn\application-dev\reference\AbilityKit\cj-apis-application-error_observer.md 脑图 | trace event | observed | none |
| S2 | T002 | agent_message | none | trace event | 我会按你点名的两个 Skill 来做：先读 `cangjie-testcase-xmind` 的脑图生成规范，再读 `cangjie-rollout-collector` 的记录规范，随后读取目标 API 文档并产出脑图文件。 | none |
| S3 | T003 | tool_call:shell_command | {"command": "Get-Content -Raw -LiteralPath 'D:\\cangjie_skills\\CangjieSkills\\.agents\\skills\\cangjie-testcase-xmind\\SKILL.md'", "timeout_ms": 10000, "workdir": "d:\\cangjie_skills\\CangjieSkills"} | trace event | exit_code=0; wall_time=0.2 seconds; stdout omitted: command printed file content; input_summary keeps command/path | none |
| S4 | T004 | tool_call:shell_command | {"command": "Get-Content -Raw -LiteralPath 'D:\\cangjie_skills\\CangjieSkills\\.agents\\skills\\cangjie-rollout-collector\\SKILL.md'", "timeout_ms": 10000, "workdir": "d:\\cangjie_skills\\CangjieSkills"} | trace event | exit_code=0; wall_time=0.2 seconds; stdout omitted: command printed file content; input_summary keeps command/path | none |
| S5 | T005 | agent_message | none | trace event | 我已经拿到测试脑图 Skill 的流程：要先做固定结构 JSON、校验，再转 `.xmind`。接下来我会读取它的格式说明和目标 AbilityKit 文档，把 API 信息抽成可验证的测试用例树。 | none |
| S6 | T006 | tool_call:shell_command | {"command": "Get-Content -Raw -Encoding UTF8 -LiteralPath 'D:\\cangjie_skills\\CangjieSkills\\.agents\\skills\\cangjie-testcase-xmind\\references\\xmind-format.md'", "timeout_ms": 10000, "workdir": "d:\\cangjie_skills\\CangjieSkills"} | trace event | exit_code=0; wall_time=0.3 seconds; stdout omitted: command printed file content; input_summary keeps command/path | none |
| S7 | T007 | tool_call:shell_command | {"command": "Get-Content -Raw -Encoding UTF8 -LiteralPath 'D:\\cangjie_skills\\CangjieSkills\\.agents\\skills\\cangjie-rollout-collector\\SKILL.md'", "timeout_ms": 10000, "workdir": "d:\\cangjie_skills\\CangjieSkills"} | trace event | exit_code=0; wall_time=0.3 seconds; stdout omitted: command printed file content; input_summary keeps command/path | none |
| S8 | T008 | tool_call:shell_command | {"command": "Get-Content -Raw -Encoding UTF8 -LiteralPath 'D:\\cangjie_skills\\CangjieSkills\\.agents\\skills\\cangjie-testcase-xmind\\references\\pairwise.md'", "timeout_ms": 10000, "workdir": "d:\\cangjie_skills\\CangjieSkills"} | trace event | exit_code=0; wall_time=0.3 seconds; stdout omitted: command printed file content; input_summary keeps command/path | none |
| S9 | T009 | tool_call:shell_command | {"command": "Get-Content -Raw -Encoding UTF8 -LiteralPath 'D:\\cangjie_dev\\docs_cangjie\\zh-cn\\application-dev\\reference\\AbilityKit\\cj-apis-application-error_observer.md'", "timeout_ms": 10000, "workdir": "d:\\cangjie_skills\\CangjieSkills"} | trace event | exit_code=0; wall_time=0.3 seconds; stdout omitted: command printed file content; input_summary keeps command/path | none |
| S10 | T010 | agent_message | none | trace event | 目标文档比较小，核心是 `ErrorObject`、`ErrorObserver` 两个类，以及 `ErrorObserver.init` 构造异常监听器。因为只有构造函数存在可调用参数，我会把属性读写也纳入用例树，组合用例主要落在构造函数的两个回调参数上。 | none |
| S11 | T011 | tool_call:shell_command | {"command": "Get-ChildItem -Recurse -File -LiteralPath 'D:\\cangjie_skills\\CangjieSkills\\.agents\\skills\\cangjie-testcase-xmind' \| Select-Object -ExpandProperty FullName", "timeout_ms": 10000, "workdir": "d:\\cangjie_skills\\CangjieSkills"} | trace event | exit_code=0; wall_time=0.3 seconds; output: D:\cangjie_skills\CangjieSkills\.agents\skills\cangjie-testcase-xmind\SKILL.md<br>D:\cangjie_skills\CangjieSkills\.agents\skills\cangjie-testcase-xmind\agents\openai.yaml<br>D:\cangjie_skills\CangjieSkills\.agents\skills\cangjie-testcase-xmind\assets\template.xmind<br>D:\cangjie_skills\CangjieSkills\.agents\skills\cangjie-t... <truncated 708 chars> | none |
| S12 | T012 | tool_call:shell_command | {"command": "Get-Content -Raw -Encoding UTF8 -LiteralPath 'D:\\cangjie_skills\\CangjieSkills\\.agents\\skills\\cangjie-testcase-xmind\\scripts\\validate_testcase_xmind_json.py'", "timeout_ms": 10000, "workdir": "d:\\cangjie_skills\\CangjieSkills"} | trace event | exit_code=0; wall_time=0.3 seconds; stdout omitted: command printed file content; input_summary keeps command/path | none |
| S13 | T013 | tool_call:shell_command | {"command": "Get-Content -Raw -Encoding UTF8 -LiteralPath 'D:\\cangjie_skills\\CangjieSkills\\.agents\\skills\\cangjie-testcase-xmind\\scripts\\json_to_xmind.py'", "timeout_ms": 10000, "workdir": "d:\\cangjie_skills\\CangjieSkills"} | trace event | exit_code=0; wall_time=0.3 seconds; stdout omitted: command printed file content; input_summary keeps command/path | none |
| S14 | T014 | tool_call:shell_command | {"command": "Get-Content -Raw -Encoding UTF8 -LiteralPath 'D:\\cangjie_skills\\CangjieSkills\\.agents\\skills\\cangjie-testcase-xmind\\scripts\\generate_pairwise_cases.py'", "timeout_ms": 10000, "workdir": "d:\\cangjie_skills\\CangjieSkills"} | trace event | exit_code=0; wall_time=0.3 seconds; stdout omitted: command printed file content; input_summary keeps command/path | none |
| S15 | T015 | agent_message | none | trace event | 我会把脑图产物放在仓库下一个清晰的 `outputs/` 路径里，保留同名 JSON 方便后续修订，并用 Skill 自带校验器检查结构和 Pair-wise 覆盖。 | none |
| S16 | T016 | tool_call:shell_command | {"command": "Get-Content -Raw -Encoding UTF8 -LiteralPath 'D:\\cangjie_skills\\CangjieSkills\\.agents\\skills\\cangjie-testcase-xmind\\scripts\\common.py'", "timeout_ms": 10000, "workdir": "d:\\cangjie_skills\\CangjieSkills"} | trace event | exit_code=0; wall_time=0.2 seconds; stdout omitted: command printed file content; input_summary keeps command/path | none |
| S17 | T017 | agent_message | none | trace event | 现在开始写 JSON 草稿。它会同时包含接口清单和测试覆盖两棵主分支，字段、构造函数和回调属性都会分开建节点，便于 XMind 里按 API 点展开。 | none |
| S18 | T018 | patch:apply_patch | *** Begin Patch<br>*** Add File: outputs/abilitykit_error_observer_testcase.json<br>+{<br>+  "ohos.application.error_observer": {<br>+    "接口列表": {<br>+      "ErrorObject.name": {<br>+        "接口类型": "只读属性",<br>+        "是否涉及权限检查": "不涉及；文档未声明该属性存在单独权限校验",<br>+        "参数": "不涉及",<br>+        "返回值": {<br>+          "String": {<br>+            "返回值说明": {<br>+              "异常事件的名称": ""<br>+... <truncated 667 chars> | trace event | changes={"d:\\cangjie_skills\\CangjieSkills\\outputs\\abilitykit_error_observer_testcase.json": {"content": "{\n  \"ohos.application.error_observer\": {\n    \"接口列表\": {\n      \"ErrorObject.name\": {\n        \"接口类型\": \"只读属性\",\n        \"是否涉及权限检查\": \"不涉及；文档未声明该属性存在单独权限校验\",\n        \"参数\": \"不涉及\",\n        \"返回值\": {\n          \"String\": {\n... <truncated 766 chars> | none |
| S19 | T019 | agent_message | none | trace event | JSON 草稿已经写好。接下来我会跑校验器，重点看固定七类覆盖节点是否齐全，以及 `ErrorObserver.init` 的 Pair-wise 组合是否完整。 | none |
| S20 | T020 | tool_call:shell_command | {"command": "python 'D:\\cangjie_skills\\CangjieSkills\\.agents\\skills\\cangjie-testcase-xmind\\scripts\\validate_testcase_xmind_json.py' 'D:\\cangjie_skills\\CangjieSkills\\outputs\\abilitykit_error_observer_testcase.json'", "timeout_ms": 10000, "workdir": "d:\\cangjie_skills\\CangjieSkills"} | trace event | exit_code=0; wall_time=0.3 seconds; output: Validation passed | none |
| S21 | T021 | agent_message | none | trace event | 校验通过了，结构没有掉节点，组合覆盖也完整。现在把 JSON 转成 `.xmind`，再检查压缩包里的 `content.xml` 是否包含预期根节点和关键 API 节点。 | none |
| S22 | T022 | tool_call:shell_command | {"command": "python 'D:\\cangjie_skills\\CangjieSkills\\.agents\\skills\\cangjie-testcase-xmind\\scripts\\json_to_xmind.py' 'D:\\cangjie_skills\\CangjieSkills\\outputs\\abilitykit_error_observer_testcase.json' 'D:\\cangjie_skills\\CangjieSkills\\outputs\\abilitykit_error_observer_testcase.xmind'", "timeout_ms": 10000, "workdir": "d:\\cangjie_skills\\CangjieS... <truncated 7 chars> | trace event | exit_code=0; wall_time=0.3 seconds; output: Successfully converted to XMind: D:\cangjie_skills\CangjieSkills\outputs\abilitykit_error_observer_testcase.xmind | none |
| S23 | T023 | agent_message | none | trace event | `.xmind` 已生成。最后做一次内容抽检，确认 XMind 归档里确实写入了根模块、接口列表、测试覆盖和关键 Pair-wise 用例。 | none |
| S24 | T024 | tool_call:shell_command | {"command": "Add-Type -AssemblyName System.IO.Compression.FileSystem\n$path = 'D:\\cangjie_skills\\CangjieSkills\\outputs\\abilitykit_error_observer_testcase.xmind'\n$zip = [System.IO.Compression.ZipFile]::OpenRead($path)\ntry {\n  $zip.Entries \| Select-Object FullName, Length\n  $entry = $zip.GetEntry('content.xml')\n  $reader = [System.IO.StreamReader]::ne... <truncated 444 chars> | trace event | exit_code=0; wall_time=0.3 seconds; output: FullName              Length<br>--------              ------<br>content.xml            67031<br>styles.xml               475<br>meta.xml                 173<br>META-INF/manifest.xml    302 | none |
| S25 | T025 | agent_message | none | trace event | 归档结构是正常的；刚才 PowerShell 把两组对象混在一起显示得不太友好。我再用纯文本形式抽检一次关键节点。 | none |
| S26 | T026 | tool_call:shell_command | {"command": "Add-Type -AssemblyName System.IO.Compression.FileSystem\n$path = 'D:\\cangjie_skills\\CangjieSkills\\outputs\\abilitykit_error_observer_testcase.xmind'\n$zip = [System.IO.Compression.ZipFile]::OpenRead($path)\ntry {\n  $entry = $zip.GetEntry('content.xml')\n  $reader = [System.IO.StreamReader]::new($entry.Open(), [System.Text.Encoding]::UTF8)\n... <truncated 388 chars> | trace event | exit_code=0; wall_time=0.3 seconds; output: ohos.application.error_observer: True<br>接口列表: True<br>测试覆盖: True<br>ErrorObserver.init: True<br>test_ErrorObserver.init_pairwise_case9: True | none |
| S27 | T027 | agent_message | none | trace event | 脑图产物已经完成并抽检通过。你还点名了 rollout collector，我现在按它的正式入口尝试采集本次任务 trace；如果工具要求用户验收信息，我会把摘要展示出来再请你确认。 | none |

### Trace Evidence Map

| trace_ref | event_type | tool/status | evidence_ref | summary |
| --- | --- | --- | --- | --- |
| T001 | user_message | observed | session:019ebed1-1b5e-73d0-9d4c-4f8fc240a721#line:7 | [$cangjie-testcase-xmind](D:\\cangjie_skills\\CangjieSkills\\.agents\\skills\\cangjie-testcase-xmind\\SKILL.md) [$cangjie-rollout-collector](D:\\cangjie_skills\\CangjieSkills\\.agents\\skills\\cangjie-rollout-collector\\SKILL.md) 请帮我设计 D:\cangjie_dev\docs_cangjie\zh-cn\application-dev\reference\AbilityKit\cj-apis-application-error_observer.md 脑图 |
| T002 | agent_message | observed | session:019ebed1-1b5e-73d0-9d4c-4f8fc240a721#line:9 | 我会按你点名的两个 Skill 来做：先读 `cangjie-testcase-xmind` 的脑图生成规范，再读 `cangjie-rollout-collector` 的记录规范，随后读取目标 API 文档并产出脑图文件。 |
| T003 | tool_call | shell_command/success | session:019ebed1-1b5e-73d0-9d4c-4f8fc240a721#call:call_EtGmSuWL1eUwVpBbUmTYezOy | exit_code=0; wall_time=0.2 seconds; stdout omitted: command printed file content; input_summary keeps command/path |
| T004 | tool_call | shell_command/success | session:019ebed1-1b5e-73d0-9d4c-4f8fc240a721#call:call_dWbNwMiHD4nU9fOtz5v0tKxu | exit_code=0; wall_time=0.2 seconds; stdout omitted: command printed file content; input_summary keeps command/path |
| T005 | agent_message | observed | session:019ebed1-1b5e-73d0-9d4c-4f8fc240a721#line:17 | 我已经拿到测试脑图 Skill 的流程：要先做固定结构 JSON、校验，再转 `.xmind`。接下来我会读取它的格式说明和目标 AbilityKit 文档，把 API 信息抽成可验证的测试用例树。 |
| T006 | tool_call | shell_command/success | session:019ebed1-1b5e-73d0-9d4c-4f8fc240a721#call:call_8DCHotGrc2UQM8UAwlZDFgcY | exit_code=0; wall_time=0.3 seconds; stdout omitted: command printed file content; input_summary keeps command/path |
| T007 | tool_call | shell_command/success | session:019ebed1-1b5e-73d0-9d4c-4f8fc240a721#call:call_sxICmJLAZuOP0ueH9d7z1ngC | exit_code=0; wall_time=0.3 seconds; stdout omitted: command printed file content; input_summary keeps command/path |
| T008 | tool_call | shell_command/success | session:019ebed1-1b5e-73d0-9d4c-4f8fc240a721#call:call_3Wf0cm39csWBjfC9I9cenwnB | exit_code=0; wall_time=0.3 seconds; stdout omitted: command printed file content; input_summary keeps command/path |
| T009 | tool_call | shell_command/success | session:019ebed1-1b5e-73d0-9d4c-4f8fc240a721#call:call_5REiKRQApdDgUwv0EHL1ocUS | exit_code=0; wall_time=0.3 seconds; stdout omitted: command printed file content; input_summary keeps command/path |
| T010 | agent_message | observed | session:019ebed1-1b5e-73d0-9d4c-4f8fc240a721#line:29 | 目标文档比较小，核心是 `ErrorObject`、`ErrorObserver` 两个类，以及 `ErrorObserver.init` 构造异常监听器。因为只有构造函数存在可调用参数，我会把属性读写也纳入用例树，组合用例主要落在构造函数的两个回调参数上。 |
| T011 | tool_call | shell_command/success | session:019ebed1-1b5e-73d0-9d4c-4f8fc240a721#call:call_v4JHD2sj55RJZISwHlYPsABs | exit_code=0; wall_time=0.3 seconds; output: D:\cangjie_skills\CangjieSkills\.agents\skills\cangjie-testcase-xmind\SKILL.md<br>D:\cangjie_skills\CangjieSkills\.agents\skills\cangjie-testcase-xmind\agents\openai.yaml<br>D:\cangjie_skills\CangjieSkills\.agents\skills\cangjie-testcase-xmind\assets\template.xmind<br>D:\cangjie_skills\CangjieSkills\.agents\skills\cangjie-t... <truncated 708 chars> |
| T012 | tool_call | shell_command/success | session:019ebed1-1b5e-73d0-9d4c-4f8fc240a721#call:call_6suM8yzHtvFBfYMafueWGU4q | exit_code=0; wall_time=0.3 seconds; stdout omitted: command printed file content; input_summary keeps command/path |
| T013 | tool_call | shell_command/success | session:019ebed1-1b5e-73d0-9d4c-4f8fc240a721#call:call_HGdCsD5Sof7DG8YXRSP8PvAB | exit_code=0; wall_time=0.3 seconds; stdout omitted: command printed file content; input_summary keeps command/path |
| T014 | tool_call | shell_command/success | session:019ebed1-1b5e-73d0-9d4c-4f8fc240a721#call:call_9jVcdmftnaLlpl1NHhd0Psph | exit_code=0; wall_time=0.3 seconds; stdout omitted: command printed file content; input_summary keeps command/path |
| T015 | agent_message | observed | session:019ebed1-1b5e-73d0-9d4c-4f8fc240a721#line:41 | 我会把脑图产物放在仓库下一个清晰的 `outputs/` 路径里，保留同名 JSON 方便后续修订，并用 Skill 自带校验器检查结构和 Pair-wise 覆盖。 |
| T016 | tool_call | shell_command/success | session:019ebed1-1b5e-73d0-9d4c-4f8fc240a721#call:call_ihXtqefYXCcPgCT02FQ55FBS | exit_code=0; wall_time=0.2 seconds; stdout omitted: command printed file content; input_summary keeps command/path |
| T017 | agent_message | observed | session:019ebed1-1b5e-73d0-9d4c-4f8fc240a721#line:47 | 现在开始写 JSON 草稿。它会同时包含接口清单和测试覆盖两棵主分支，字段、构造函数和回调属性都会分开建节点，便于 XMind 里按 API 点展开。 |
| T018 | patch | apply_patch/success | session:019ebed1-1b5e-73d0-9d4c-4f8fc240a721#call:call_Ne4llqXavMaZ1wXdJv1QJjWA | changes={"d:\\cangjie_skills\\CangjieSkills\\outputs\\abilitykit_error_observer_testcase.json": {"content": "{\n  \"ohos.application.error_observer\": {\n    \"接口列表\": {\n      \"ErrorObject.name\": {\n        \"接口类型\": \"只读属性\",\n        \"是否涉及权限检查\": \"不涉及；文档未声明该属性存在单独权限校验\",\n        \"参数\": \"不涉及\",\n        \"返回值\": {\n          \"String\": {\n... <truncated 766 chars> |
| T019 | agent_message | observed | session:019ebed1-1b5e-73d0-9d4c-4f8fc240a721#line:54 | JSON 草稿已经写好。接下来我会跑校验器，重点看固定七类覆盖节点是否齐全，以及 `ErrorObserver.init` 的 Pair-wise 组合是否完整。 |
| T020 | tool_call | shell_command/success | session:019ebed1-1b5e-73d0-9d4c-4f8fc240a721#call:call_UUkmWaWMxFd5TzJWz756e3kJ | exit_code=0; wall_time=0.3 seconds; output: Validation passed |
| T021 | agent_message | observed | session:019ebed1-1b5e-73d0-9d4c-4f8fc240a721#line:60 | 校验通过了，结构没有掉节点，组合覆盖也完整。现在把 JSON 转成 `.xmind`，再检查压缩包里的 `content.xml` 是否包含预期根节点和关键 API 节点。 |
| T022 | tool_call | shell_command/success | session:019ebed1-1b5e-73d0-9d4c-4f8fc240a721#call:call_ENroIA57sNCb2aita8H4djl5 | exit_code=0; wall_time=0.3 seconds; output: Successfully converted to XMind: D:\cangjie_skills\CangjieSkills\outputs\abilitykit_error_observer_testcase.xmind |
| T023 | agent_message | observed | session:019ebed1-1b5e-73d0-9d4c-4f8fc240a721#line:66 | `.xmind` 已生成。最后做一次内容抽检，确认 XMind 归档里确实写入了根模块、接口列表、测试覆盖和关键 Pair-wise 用例。 |
| T024 | tool_call | shell_command/success | session:019ebed1-1b5e-73d0-9d4c-4f8fc240a721#call:call_QVG38BF9j1GEmzvoM4BTX87a | exit_code=0; wall_time=0.3 seconds; output: FullName              Length<br>--------              ------<br>content.xml            67031<br>styles.xml               475<br>meta.xml                 173<br>META-INF/manifest.xml    302 |
| T025 | agent_message | observed | session:019ebed1-1b5e-73d0-9d4c-4f8fc240a721#line:72 | 归档结构是正常的；刚才 PowerShell 把两组对象混在一起显示得不太友好。我再用纯文本形式抽检一次关键节点。 |
| T026 | tool_call | shell_command/success | session:019ebed1-1b5e-73d0-9d4c-4f8fc240a721#call:call_tHWLL1U4w1Ou0VAJqBnQTutt | exit_code=0; wall_time=0.3 seconds; output: ohos.application.error_observer: True<br>接口列表: True<br>测试覆盖: True<br>ErrorObserver.init: True<br>test_ErrorObserver.init_pairwise_case9: True |
| T027 | agent_message | observed | session:019ebed1-1b5e-73d0-9d4c-4f8fc240a721#line:78 | 脑图产物已经完成并抽检通过。你还点名了 rollout collector，我现在按它的正式入口尝试采集本次任务 trace；如果工具要求用户验收信息，我会把摘要展示出来再请你确认。 |

### Artifacts

- trace file: C:\Users\张睿鸣\.codex\sessions\2026\06\13\rollout-2026-06-13T10-30-42-019ebed1-1b5e-73d0-9d4c-4f8fc240a721.jsonl
- rollout record: D:\cangjie_skills\CangjieSkills\.agents\skills\cangjie-rollout-collector\records\rollouts\cangjie-testcase-xmind\abilitykit-error-observer-xmind\cangjie-testcase-xmind-20260613-105118-001.md

### Verification

- not_verified

### Ground Truth (yi*)

- reviewer: user
- reviewed_at: 2026-06-13T02:51:18+00:00
- task_completed: partial
- adjudicated_outcome: partial
- result_gaps: 测试覆盖中的单参数测试缺少按具体参数展开的层级，未在 ErrorObserver.init 等接口下展开 onUnhandledException、onException 及其有效等价类、无效等价类、边界值、特殊值讨论。
- process_gaps: none
- missed_steps: 单参数测试应覆盖参数节点及等价类分类；上一版未覆盖该层级。
- notes: T026 only confirmed root/basic nodes and a Pair-wise case; not_observed for parameter/equivalence-class nodes under 单参数测试.
- confidence: high

### Failure Or Detour

- none

### Transferable Observations

- pattern: none
  generality: low
  source_steps: not_observed
