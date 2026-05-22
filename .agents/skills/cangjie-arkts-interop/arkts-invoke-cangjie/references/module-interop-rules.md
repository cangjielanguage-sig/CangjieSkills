# 模块互操作规则

派生、修复或增量暴露 ArkTS 调用仓颉模块的 HarmonyOS 工程时，使用这些规则。

本文件是 SKILL.md 的规则补充，SKILL.md 中已有详细说明的内容此处仅做引用。

## 必要结构

- 业务逻辑保留在仓颉模块内，通常是 `<module>/src/main/cangjie`。
- 生成的仓颉互操作 wrapper 代码必须统一放在 `src/main/cangjie/bridge/`，包括 `@Interop[ArkTS]` class/interface/func、`GlobalContext.cj`、手写 `SharedObject & JSInteropType<T>` 类型、边界适配 helper；不要把新生成的互操作 wrapper 散落到业务源码目录。
- 搜索业务代码、扫描待翻译 public API、生成翻译覆盖表时必须排除 `src/main/cangjie/bridge/` 和 `src/main/cangjie/mock/`。`bridge/` 只作为生成结果目录，`mock/` 只用于测试、兼容或替身实现，都不作为业务源码输入，避免把非业务代码再次当成业务 API 翻译。
- `bridge/` 下生成的每个仓颉文件都必须按实际 `cjpm.toml` 的 `[package].name` 设置包名和导入：`package <package.name>.bridge`，并添加 `import <package.name>.*`。例如 `[package].name = "ohos_app_cangjie_library"` 时，bridge 文件使用 `package ohos_app_cangjie_library.bridge` 和 `import ohos_app_cangjie_library.*`。
- 如果 bridge/wrapper 需要导入业务实现，固定使用 `import <package.name>.bussiness.*`。即使业务文件物理目录是 `business/`，互操作层也按 `.bussiness` 作为业务包导入前缀。
- 业务逻辑文件不要因为需要互操作而随意移动到 `bridge/`；在 `bridge/` 中新增同名或命名一致的互操作边界代码来调用业务实现。
- 如果需要导出全局变量或 `public static` 成员，统一在 `src/main/cangjie/bridge/GlobalVar.cj` 中处理（文件不存在则新建，存在则复用）：简单类型直接导出值，复杂类型通过 getter accessor 暴露。
- 仓颉互操作 wrapper 命名默认与原仓颉代码的公开接口保持一致：`class`、`interface`、`func`、方法名、参数名、生成声明名和 ArkTS wrapper 中引用的 CJ 类型名都优先沿用原名，不默认追加 `Bridge`、`Interop`、`Wrapper`、`Impl` 等后缀；只有在用户明确要求、工程已有同名冲突、ArkTS 关键字冲突或既有工程约定要求时才调整命名。
- 只导出稳定的 ArkTS 面向类，例如 `<Feature>Client`、`<Feature>Callbacks` 或其他边界清晰的 facade。
- 迁移 Android 代码时，把 Android 兼容 shim 放在命名清晰的包内，例如 `mock/`。
- 把线程池、平台 shim、协议适配等兼容辅助代码放在本地依赖或独立包中，并从模块 `cjpm.toml` 引用。
- **HAR 模块必须有 `src/main/ets/Index.ets` 入口文件**，用于 re-export 互操作类型。`oh-package.json5` 的 `"main"` 字段必须设为 `"./src/main/ets/Index.ets"`（带完整路径和 `.ets` 扩展名），`"types"` 字段指向根目录的 `Index.d.ets`。缺少 `ets/` 目录或 `"main"` 值不带扩展名会导致构建报错 `The value of 'main' must be a .ets, .ts, or .js file`。

典型 HAR 互操作目录结构：

```text
<module>/
├── src/main/
│   ├── cangjie/
│   │   ├── bridge/
│   │   │   ├── <Feature>.cj           # @Interop[ArkTS] / 手写互操作 wrapper
│   │   │   └── GlobalContext.cj       # 仅在需要 Context 注入时存在
│   │   ├── ...业务.cj
│   │   ├── loader/                      # libark_interop_loader.so 声明
│   │   │   ├── Index.d.ts
│   │   │   └── oh-package.json5
│   │   └── types/lib<module>/           # lib<module>.so 声明
│   │       ├── Index.d.ts
│   │       └── oh-package.json5
│   ├── ets/
│   │   ├── <feature>/                   # 按功能拆分的 wrapper 子目录
│   │   │   └── <Feature>Client.ets      # wrapper 类 + 回调转换 + 工厂函数
│   │   └── Index.ets                    # ArkTS 入口，仅 re-export
│   └── resources/
├── Index.d.ets                          # 类型声明入口
├── cjpm.toml
├── oh-package.json5                     # main: "./src/main/ets/Index.ets", types: "./Index.d.ets"
└── build-profile.json5
```

`ets/` 目录组织规则：

- **不要把所有内容放在 `Index.ets` 一个文件里**。按功能拆分到子目录，例如 `ets/<feature>/<Feature>Client.ets`。
- `Index.ets` 只做 re-export，不包含实现逻辑。
- 每个功能子目录包含：ArkTS 原生接口、回调转换函数、wrapper 类、工厂函数。
- CJ 类型（`CJXxx`）只在功能子目录内部使用，不 export 到 `Index.ets`。

## 命名规则

### 文件命名

`bridge/` 下生成的仓颉互操作 wrapper 文件名 = 对应业务文件名（去掉 `.cj`）+ `Bridge.cj`：

| 业务文件 | 生成的 bridge 文件 |
|----------|-------------------|
| `FileDownloaderManager.cj` | `FileDownloaderManagerBridge.cj` |
| `UserService.cj` | `UserServiceBridge.cj` |
| `Auth.cj` | `AuthBridge.cj` |

### class / interface / 顶层 func 命名

bridge 目录下的互操作 wrapper 使用独立包名 `<cjpm.toml [package].name>.bridge`，与业务包天然隔离，通常不产生命名冲突。生成规则：

1. **优先同名**：class、interface、顶层 func 名称默认与对应仓颉公开 API 完全一致。
2. **冲突时加 `Bridge` 后缀**：若同名确实产生冲突（bridge 包内已存在同名符号、ArkTS 关键字冲突等），在 class / interface / 顶层 func 名称后追加 `Bridge` 后缀，例如 `FileDownloaderManager` → `FileDownloaderManagerBridge`。
3. **成员函数名永远与业务代码保持一致**：无论类名/接口名是否加了 `Bridge` 后缀，成员方法名**必须**与原仓颉业务代码方法名完全相同，不加任何后缀。

ArkTS 侧对外导出名称跟随相同规则：`Index.ets` / `Index.d.ets` 中导出的类名/接口名与 bridge 侧一致（优先同名，冲突时同步加 `Bridge` 后缀）；方法名始终与业务代码一致。

如果加了 `Bridge` 后缀，在翻译覆盖表的 `Notes` 中写明 `原名 -> 新名`，并保证 bridge、`.d.ts`、`CustomLib`、ArkTS wrapper、`Index.ets` re-export 中使用同一个新名。翻译覆盖表必须细化到函数级别：顶层函数、class 方法、interface 方法分别列行，不能只写某个 class 或 interface 已整体翻译。

### 跨包调用时的类型引用风格（默认短名）

bridge 文件已强制包含 `import <package.name>.*`；如果还要引用业务实现，则额外导入 `import <package.name>.bussiness.*`。此时 bridge 内引用业务包类型/函数时：

- **默认使用短名**（更易读）：`ContextTestExample()`。
- **只有在 bridge 包与业务包存在同名符号**时，才用全限定名 `<package.name>.bussiness.<TypeName>` 或对应实际全限定名。

## API 形态变更规则（默认不允许）

互操作的首要目标是“打通调用”，但在工程化场景中更重要的是 **不意外改变业务 public API 形态**。

- 默认策略：`preserve_public_api_shape = true`，即对 ArkTS 暴露的 API（参数/返回值/字段类型）应尽量保持与业务 public API 一致。
- 当遇到 `@Interop[ArkTS]` 的硬约束（例如 `@Interop` 类之间不能互相引用）时：
  - 若必须保持“对象语义”不变：选 **手写互操作库**（`SharedObject & JSInteropType<T>`）。
  - 只有在用户明确同意时，才允许用 **句柄模式/扁平参数** 改变 API 形态（例如把 `Father` 改成 `Int64` id）。

一旦发生 API 形态变更，翻译覆盖表必须新增两列并逐函数填写：

- `API Shape Changed`：`yes/no`
- `Before → After`：例如 `paramTest(a: Father) → paramTest(fatherId: Int64)`

## 仓颉桥接规则

修饰符约束和回调桥接模式见 [cangjie-bridge-rules.md](cangjie-bridge-rules.md)。本节补充边界处理规则：

- 在边界处转换 ArkTS 可选值。例如调用仓颉业务代码前，把空字符串、缺省参数或 nullable 值转换成业务层期望的 `None`、默认值或具体类型。
- 把 map 或复杂回调载荷转换成简单边界格式，例如 JSON 字符串，再通过 ArkTS 回调返回。
- 通过仓颉 callback holder 对象持有回调，不要把原始 listener 实现传给 ArkTS。

## ArkTS 包装规则

构造签名限制和 CustomLib 规则见 [cangjie-bridge-rules.md#arkts-构造签名限制](cangjie-bridge-rules.md#arkts-构造签名限制)。本节补充包装层实现规则：

- 同时导入 loader 和生成声明：`requireCJLib` 来自 `libark_interop_loader.so`，CJ 类型和 `CustomLib` 来自 `lib<module>.so`。
- **ArkTS 构造签名限制**：`.ets` 源文件中禁止 `typeof`（`arkts-no-type-query`）和 `interface` 中的构造签名（`arkts-no-ctor-signatures-iface`）。`CustomLib` 必须定义在 `.d.ts` 声明文件中：

```ts
// types/lib<module>/Index.d.ts（声明文件，允许构造签名）
export declare class XxxClient {
    constructor(args...);
    // ...方法
}
export declare interface CustomLib {
    XxxClient: { new (args...): XxxClient }
}
```

```ts
// .ets 源文件（只导入，不定义构造签名）
import { XxxClient as CJXxxClient, CustomLib } from 'lib<module>.so'

let globalCJLib: CustomLib | undefined = undefined
function getCJLib(): CustomLib { ... }
```

- 在模块作用域缓存 `requireCJLib('lib<module>.so') as CustomLib` 的结果。
- 用稳定的 ArkTS client 类包装生成的仓颉类。应用代码调用 wrapper，不要直接调用 `requireCJLib`。
- 翻译仓颉 `interface` 时，ArkTS wrapper 和 `CustomLib` 中使用的 CJ 类型名必须与原仓颉 interface 名称一致，不默认追加 `Bridge`、`Impl`、`Wrapper` 等后缀；只有同名冲突或用户明确要求时才改名，并在说明中写清楚。
- 在 wrapper 中把回调载荷转回 ArkTS 原生形态，例如把 JSON 字符串解析成 `Record<string, string>`。
- 从模块根 `Index.ets` 导出 wrapper 类和类型。

## 打包和构建规则

- 在仓颉模块的 `build-profile.json5` 中，把 `buildOption.cangjieOptions.path` 指向模块 `cjpm.toml`（一般为 `./cjpm.toml`，相对模块根）。
- **强制**：检查 `buildOption.cangjieOptions` 是否包含 `flattenLibs`。若未配置或不为 `true`，则在该对象内补齐 `"flattenLibs": true`，并与 `path` 一并保证形如：
  ```json5
  "cangjieOptions": {
    "path": "./cjpm.toml",
    "flattenLibs": true
  }
  ```
  若已有正确的 `path`，只补 `flattenLibs: true` 即可。`flattenLibs: true` 有利于 ArkTS 侧装载布局；除非工程已有验证过的其他打包布局且用户明确要求，否则不要省略。
- **强制**：检查模块 `cjpm.toml` 是否包含 **`[profile.build.combined]`** 且其中有一条 **键为 `[package].name`、值为 `"dynamic"`** 的项（键名字符串须与 `cjpm.toml` 里 `[package].name` 一致，不是 HAP 模块文件夹名）。若缺少整表，则新增：
  ```toml
  [profile.build.combined]
  <package.name> = "dynamic"
  ```
  若仅有表、缺少当前包名对应键，则只追加该行，勿删其他包的键。语义与选项以 [CJPM 用户指南（中文）](https://gitcode.com/Cangjie/cangjie_tools/blob/main/cjpm/doc/user_guide_zh.md) 为准。
- 除非用户明确只面向真机或只面向模拟器，否则 `abiFilters` 同时包含 `arm64-v8a` 和 `x86_64`。
- 在模块 `oh-package.json5` 中声明两个依赖：

```json5
"libark_interop_loader.so": "file:src/main/cangjie/loader",
"lib<module>.so": "file:src/main/cangjie/types/lib<module>"
```

- 保持仓颉包名、生成声明目录、依赖 key、ArkTS import 和 `requireCJLib` 库名一致。
- **强制**：检查 `src/main/cangjie/package.cj`。若不存在则创建：首行 `package` 与 `cjpm.toml` 的 `[package].name` 一致；包含固定行 `import ohos.ark_interop.*`；对 `cjpm.toml` 根表 **`[dependencies]`** 的每个一级键名追加 `import <键名>.*`（与右侧 `path` / `git` 等无关）。已存在则校验收口并补齐缺失的 `import`，勿删仍需要的既有导入。

## 复制和派生规则

- 从可工作的源工程创建同级工程时，同时同步源码、资源、`cjpm.toml`、`src/main/cangjie/package.cj`（若工程使用）、生成类型声明、loader 声明和 ArkTS wrapper。
- 不要因为目录存在就认为它有效；扫描 `@Interop[ArkTS]`、`requireCJLib`、`libark_interop_loader.so` 和生成类型声明。
- 复制时排除或人工确认本地状态目录：`.git`、`.idea`、`.hvigor`、`oh_modules` 和 `build`。
- 复制后运行 `scripts/scan_interop_project.py <target>`，确认没有缺失导出、loader、依赖或 ABI 的发现项。

## 增量函数规则

- 源工程新增某个业务函数时，先在目标同路径业务类或业务文件中复制或重建该函数。
- 给 ArkTS 面向 client 或 facade 增加匹配的桥接方法：创建业务上下文、创建必要的 listener/callback adapter，再调用业务方法。
- 在生成声明或临时声明的 `CustomLib` 暴露类中加入该方法，用于生成声明不可用或刻意保留临时声明时的 ArkTS 类型检查。
- 在 ArkTS wrapper 中加入同名或语义一致的方法；当签名与既有方法匹配时，复用已有 options 类型和回调转换。
- 桥接方法只包含业务函数实际需要的参数，不要沿用相邻方法的额外参数，除非业务函数也接收它。
