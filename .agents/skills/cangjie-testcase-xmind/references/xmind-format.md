# XMind Output Format

Use this reference whenever creating, validating, or repairing testcase JSON for this skill.

## Required Tree

```text
{组件名}
├── 接口列表
│   └── {接口名}
│       ├── 接口类型
│       ├── 是否涉及权限检查
│       ├── 参数
│       ├── 返回值
│       └── 抛出异常
└── 测试覆盖
    └── {接口名}
        ├── 单参数测试
        ├── 多参数组合
        ├── 返回值验证
        ├── 异常处理
        ├── 权限检查
        ├── 特殊场景
        └── 组合场景
```

`接口列表` and `测试覆盖` must contain exactly the same interface names. Keep all seven fixed `测试覆盖` nodes even when a category does not apply.

## Interface Details

- Put one node under `接口列表` for each public API that needs testcase design.
- Under each API, include `接口类型`, `是否涉及权限检查`, `参数`, `返回值`, and `抛出异常`.
- If an API has no parameters, use `参数: "不涉及"` or `参数: { "不涉及": "" }`.
- If a parameter exists, include `参数说明`, `是否必填`, `参数形式`, `类型`, `默认值`, `是否支持Option`, and `取值范围`.
- Under `取值范围`, use `有效等价类`, `无效等价类`, `边界值`, and `特殊值`; each concrete value should be a child key.
- Under `返回值`, use `{返回值类型} -> 返回值说明 -> {具体说明}`.
- Under `抛出异常`, use one child key per error code, with scenario descriptions under that error code. If none apply, use `不涉及`.

## Testcase Nodes

Every testcase must be:

```json
"test_api_scenario": {
  "测试流程": "具体测试步骤",
  "预期结果": "具体预期结果"
}
```

The XMind converter maps this to:

```text
test_api_scenario
└── 具体测试步骤
    └── 具体预期结果
```

Do not output `测试流程` or `预期结果` as mind-map node titles. Do not insert `用例1`, `用例2`, or similar wrapper nodes.

## Color Hints

The converter marks these category nodes with style hints:

- `有效等价类`: green
- `无效等价类`: red
- `边界值`: blue

`特殊值` uses the default style.

## Not Applicable

Use `不涉及` only as a leaf:

```json
"权限检查": "不涉及"
```

or:

```json
"权限检查": {
  "不涉及": ""
}
```
