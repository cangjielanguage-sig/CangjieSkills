# 完整混合工程示例说明

## 目录

1. 适用方式
2. 示例目录
3. 替换点
4. 接入步骤
5. 验证顺序

## 1. 适用方式

`assets/hybrid-demo/` 不是为了替代 DevEco Studio 创建工程的所有根配置，而是作为“标准 Stage 工程上的完整互操作接线示例”。

推荐使用方式：

1. 先用 DevEco Studio 新建一个标准 Stage 工程。
2. 再把 `assets/hybrid-demo/entry/` 下的互操作相关文件合并进去。
3. 按本地实际包名、module 名、`.so` 产物名、SDK 版本调整配置。

如果要快速生成一份可改模板，优先运行：

```bash
scripts/install_hybrid_demo.py --target /path/to/output
```

如果用户只是要范例代码，直接引用里面的 `.cj`、`.ets` 和 `ark_interop_api` 示例即可。

## 2. 示例目录

```text
assets/hybrid-demo/
├── AppScope/
│   ├── app.json5
│   └── resources/base/element/string.json
├── build-profile.json5
├── oh-package.json5
└── entry/
    └── src/main/
        ├── cangjie/
        │   ├── cjpm.toml
        │   ├── MathBridge.cj
        │   └── ark_interop_api/MathBridge.d.ets
        ├── ets/
        │   ├── entryability/EntryAbility.ets
        │   └── pages/Index.ets
        ├── module.json5
        └── resources/base/
            ├── element/string.json
            └── profile/main_pages.json
```

## 3. 替换点

接线时优先替换以下内容：

1. `bundleName`
2. `module.name`
3. `requireCJLib("libmathbridge.so")` 中的库名
4. `cjpm.toml` 里的包名和版本字段
5. `compatibleSdkVersion`
6. `abiFilters`

`ark_interop_api/MathBridge.d.ets` 只是“生成结果示例”。正式工程里应重新执行生成流程，不要长期手工维护它。

## 4. 接入步骤

1. 先保留 DevEco 自动生成的根工程文件。
2. 用示例中的 `module.json5`、`EntryAbility.ets`、`Index.ets`、`MathBridge.cj` 覆盖或对齐本地 module。
3. 根据本地工具链调整 `cjpm.toml`。
4. 执行 `Generate Cangjie-ArkTS Interop API`。
5. 确认 `.so` 产物名后，修正 `Index.ets` 里的 `requireCJLib(...)`。
6. 先验证同步函数调用成功，再扩展到类、组件和回调。

若用户要新目录中的完整模板，可以直接生成并带参数替换：

```bash
scripts/install_hybrid_demo.py \
  --target /path/to/output \
  --bundle-name com.example.hybriddemo \
  --module-name entry \
  --lib-name libmathbridge.so \
  --package-name mathbridge
```

## 5. 验证顺序

1. 仓颉文件能编译。
2. `ark_interop_api` 生成成功。
3. ArkTS 页面能装载仓颉库。
4. 页面按钮点击后能返回正确结果。
5. 最后再增加复杂业务逻辑。
