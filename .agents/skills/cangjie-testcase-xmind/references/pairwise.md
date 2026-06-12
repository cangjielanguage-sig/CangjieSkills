# Pair-wise Case Design

Use this reference whenever filling `测试覆盖 -> {接口名} -> 多参数组合`.

## Source Values

For each parameter, collect values in this order:

1. `默认值`, unless it is empty, `无`, `无默认值`, `不涉及`, `None`, or `null`.
2. Values under `取值范围 -> 有效等价类`.
3. Values under `取值范围 -> 特殊值`.

Ignore `无效等价类` and `边界值` for `多参数组合`; those belong in single-parameter or negative tests. Deduplicate while preserving order.

## When to Use `不涉及`

Set `多参数组合` to `不涉及` when:

- fewer than two parameters have usable values;
- every usable parameter has only one value;
- parameter values cannot be made concrete enough for a meaningful combined call.

## Required Coverage

When Pair-wise applies, every pair of parameters must have every value pair covered at least once. For parameters:

```text
errorType: ErrorType.CRASH, ErrorType.JS_ERROR
callback: cbInfo, cbWarn
options: ErrorObserverOptions(), Option.None
```

the generated cases must cover all pairs between:

- `errorType` and `callback`
- `errorType` and `options`
- `callback` and `options`

## Output Shape

Use testcase names and concrete steps:

```json
"多参数组合": {
  "test_registerErrorObserver_pairwise_case1": {
    "测试流程": "errorType=ErrorType.CRASH, callback=cbInfo, options=ErrorObserverOptions()",
    "预期结果": "注册成功；模拟触发 CRASH 后 callback 被调用一次"
  }
}
```

Avoid generic names and results such as `用例1`, `返回预期结果`, or `接口正常调用`.

## Script Usage

Generate cases from a full testcase JSON:

```bash
python scripts/generate_pairwise_cases.py path/to/testcase.json --api registerErrorObserver
```

Generate cases from a parameter-only JSON:

```json
{
  "api": "registerErrorObserver",
  "parameters": {
    "errorType": ["ErrorType.CRASH", "ErrorType.JS_ERROR"],
    "callback": ["cbInfo", "cbWarn"],
    "options": ["ErrorObserverOptions()", "Option.None"]
  }
}
```

```bash
python scripts/generate_pairwise_cases.py params.json --result "注册成功；回调按输入参数触发"
```
