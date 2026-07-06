---
name: cangjie-skill-lint-fix
description: "Agent Skill lint repair workflow. Use when the user explicitly asks to fix skill-lint errors or warnings by running Skill-CLI, analyzing lint reports, adding validated checks, and iterating to 0 errors / 0 warnings. Not for coding or library lookup."
---

# Skill Lint Fix

## Hard Requirements

执行此 Skill 时必须做真实操作，不能只给建议：

1. 先确认用户输入的目标 Skill 目录；用户已给目录时直接使用该目录。
2. 如果 `skill-lint` 或 `skill-eval` 不可用，先从 `https://gitcode.com/cjse/Skill-CLI/tags/release-1.0.0` 对应 tag 安装 Skill-CLI。
3. 对目标 Skill 目录运行 `skill-lint`，报告必须写入 `reports/lint`。
4. 修复 lint 报告中的全部 errors 和 warnings。
5. 如果新增或修改了 `evals/` 用例，必须用 `skill-eval --runner agent-command` 调用真实 Claude 或 Codex agent 跑一遍，报告必须写入 `reports/eval`。
6. 修复完成后再次运行 `skill-lint`，最终必须达到 `0 errors` 和 `0 warnings`。

## Step 0: Target

使用用户输入的 Skill 目录作为目标，例如 `.agents/skills/<skill-name>` 或绝对路径。不要扫描整个 skills 根目录，除非用户明确要求批量修复。

在仓库根目录执行命令，并为报告创建目录：

```powershell
$target = "用户输入的 Skill 目录"
$skillName = Split-Path -Leaf (Resolve-Path -LiteralPath $target)
New-Item -ItemType Directory -Force -Path "reports\lint","reports\eval" | Out-Null
```

如果目标目录不存在，先停止并要求用户提供正确路径。

## Step 1: Ensure Skill-CLI

先检查命令是否存在：

```powershell
Get-Command skill-lint -ErrorAction SilentlyContinue
Get-Command skill-eval -ErrorAction SilentlyContinue
```

只要任一命令缺失，就安装 release-1.0.0：

```powershell
$cliDir = Join-Path $env:USERPROFILE ".cache\skill-cli\release-1.0.0"
if (-not (Test-Path -LiteralPath $cliDir)) {
  git clone --branch release-1.0.0 --depth 1 https://gitcode.com/cjse/Skill-CLI.git $cliDir
}
python -m pip install -e $cliDir
skill-lint --help
skill-eval --help
```

在 POSIX shell 中使用同等流程：

```bash
CLI_DIR="${HOME}/.cache/skill-cli/release-1.0.0"
test -d "$CLI_DIR" || git clone --branch release-1.0.0 --depth 1 https://gitcode.com/cjse/Skill-CLI.git "$CLI_DIR"
python -m pip install -e "$CLI_DIR"
skill-lint --help
skill-eval --help
```

若 Python 版本低于 3.11、git 不存在、pip 安装失败，先解决环境问题，再继续 lint。

## Step 2: Run Lint

对目标 Skill 目录运行扫描，报告输出到 `reports/lint`：

```powershell
$lintReport = "reports\lint\$skillName.json"
skill-lint --path $target --format json --out $lintReport
Get-Content -LiteralPath $lintReport -Encoding UTF8
```

读取 JSON 报告，重点查看：

- `errors[]`
- `warnings[]`
- 每条诊断的 `ruleId`、`path`、`message`、`suggestion`

不要只看 `status`。默认阈值可能让存在 warnings 的报告仍显示 passed；最终验收必须检查 `summary.errors == 0` 且 `summary.warnings == 0`。

## Step 3: Fix Diagnostics

按报告逐条修复，所有 warning 也必须处理。修复时遵守当前仓库的文件结构，不重排无关内容。

常见规则：

| Rule | Severity | Fix |
| --- | --- | --- |
| `C-1` | blocking | 创建缺失的 `SKILL.md`。 |
| `C-2` | blocking | 修复 frontmatter 分隔符和 YAML 语法。 |
| `C-3` | blocking | 补充非空 `description`。 |
| `C-4` | blocking | 从 `description` 删除模糊词，改成具体触发场景。 |
| `C-5` | blocking | 在 `description` 写清“当...时使用此 Skill”和能力动作。 |
| `C-6` | blocking | 将 `description` 压到 1024 字符以内。 |
| `C-7` | blocking | 补充 `name`。 |
| `C-8` | blocking | 将 `name` 改为 kebab-case，长度不超过 64。 |
| `C-9` | blocking | 保持 `name` 与目录名一致，snake_case 目录按规则映射。 |
| `C-10` | blocking | 将 Skill 层级控制为 Hub Skill 加一层子 Skill。 |
| `C-11` | blocking | 消除检查范围内重复的 Skill name。 |
| `C-12` | blocking | 打破 `dependencies` 循环。 |
| `W-1` | warning | 将 `description` 压到推荐的 512 字符以内。 |
| `W-4` | warning | 缩短过深的 `dependencies` 链。 |
| `X-1` | warning | 将 `globs` 修为非空字符串数组。 |
| `X-2` | warning | 将 `dependencies` 修为合法 Skill name 数组。 |
| `X-3` | warning | 将 `steps` 修为非空字符串数组。 |
| `X-4` | warning | 将 `calls` 修为合法 Skill name 数组。 |
| `X-5` | warning | 将 `version` 修为 SemVer 字符串。 |
| `R-1` | blocking | 修复本地 Markdown 链接，目标必须存在且位于 Skill 目录内。 |
| `E-1` | warning | 创建或修复 `evals/*.jsonl` 用例。 |

修复 `description` 时，触发条件必须放在 frontmatter 的 `description` 里，因为路由只读取 metadata。描述应说明使用场景和能力动作，避免空泛堆叠。

## Step 4: Add Or Fix Evals

遇到 `E-1`，或本次修改改变了 Skill 行为时，创建或修复 `evals/`：

```powershell
New-Item -ItemType Directory -Force -Path (Join-Path $target "evals") | Out-Null
```

至少准备两类 JSONL：

- `evals/content-basic.jsonl`：验证 Skill 被加载后能给出正确执行方案。
- `evals/discovery.jsonl`：验证用户自然表达能命中该 Skill。

用例要求：

- 每行必须是合法 JSON 对象。
- `input` 使用真实用户会说的话，不写内部诊断结论。
- `expected_patterns` 匹配关键产物、命令、报告路径或必要约束，避免只检查寒暄语。
- `min_score` 通常使用 `0.6` 到 `0.8`；关键流程越确定，分数越高。
- discovery 用例至少写 `expected_skills` 和 `min_rank`。
- 如果 eval 需要临时工程，使用 `workspace_fixture` 和 `allow_workspace_edits`，不要修改原始 fixture。

示例：

```json
{"input":"帮我修复 .agents/skills/demo 的 skill-lint warning，最后要没有 errors 和 warnings。","expected_patterns":["skill-lint","reports/lint","0 errors","0 warnings"],"min_score":0.7}
{"input":"skill-lint 报 E-1 缺少 evals，请补用例并验证。","expected_patterns":["evals","skill-eval","agent-command","reports/eval"],"min_score":0.7}
```

## Step 5: Run Real-Agent Eval

只要新增或修改了 `evals/`，必须运行真实 agent。优先使用当前机器可用的 Codex；没有 Codex 时使用 Claude。不能用 `--runner static` 代替这一验收。

```powershell
$codexAdapter = "python -m skill_cli.eval_tools.codex_exec_agent_adapter"
$claudeAdapter = "python -m skill_cli.eval_tools.claude_code_agent_adapter"
if (Get-Command codex -ErrorAction SilentlyContinue) {
  $agentCommand = $codexAdapter
} elseif (Get-Command claude -ErrorAction SilentlyContinue) {
  $agentCommand = $claudeAdapter
} else {
  throw "No real agent CLI found. Install or authenticate Codex or Claude before running skill-eval."
}

$evalReport = "reports\eval\$skillName.json"
skill-eval --path $target --mode all --out $evalReport --timeout 600 --progress --runner agent-command --agent-command $agentCommand --emit-trace
Get-Content -LiteralPath $evalReport -Encoding UTF8
```

Eval 失败时：

- 如果失败原因是用例 schema、断言、fixture 或 Skill 内容不合理，修复后重新跑 eval。
- 如果失败原因是 agent CLI 未安装、未登录、网络或额度问题，停止并向用户报告阻塞原因；不要声称 eval 已通过。
- 保留报告在 `reports/eval/<skill-name>.json`，必要时用 `reports/eval/<skill-name>.round-N.json` 保存中间轮次。

## Step 6: Final Lint Gate

修复和 eval 完成后，重新运行 lint：

```powershell
$lintReport = "reports\lint\$skillName.json"
skill-lint --path $target --format json --out $lintReport
Get-Content -LiteralPath $lintReport -Encoding UTF8
```

验收条件：

- `summary.errors` 必须为 `0`
- `summary.warnings` 必须为 `0`
- `errors` 必须为空数组
- `warnings` 必须为空数组

如果仍有任何 warning 或 error，回到 Step 3 继续修复。

## Final Response

完成后向用户说明：

- 修复的目标 Skill 目录。
- lint 报告路径和最终 `0 errors / 0 warnings` 状态。
- 如果运行过 eval，说明 eval 报告路径和真实 agent 类型。
- 如果存在 agent 环境阻塞，说明具体命令和错误，不把阻塞包装成通过。
