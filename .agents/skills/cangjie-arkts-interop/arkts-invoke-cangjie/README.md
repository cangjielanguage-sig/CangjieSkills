---
name: arkts-cangjie-interop
description: ArkTS 与仓颉互操作的开发、接线与排障。覆盖两类场景：(1) 在 HarmonyOS 混合工程中将仓颉函数、类、接口、枚举暴露给 ArkTS，支持按文件或函数增量生成互操作代码；(2) 修复互操作链路问题，包括声明不同步、符号冲突、装载失败、ABI 不匹配等。
---

# ArkTS Cangjie Interop

## Overview

ArkTS-Cangjie 互操作用于 HarmonyOS 混合工程中把仓颉函数、类、接口、枚举暴露给 ArkTS。核心流程：仓颉侧用 `@Interop[ArkTS]` 标记导出 → 创建类型声明 → 配置依赖 → ArkTS 侧用 `requireCJLib` 装载并包装。

## 工作流一览

| 任务 | 做什么 | 参考文档 |
|------|-------------------|-----------|
| 0 | **识别工程结构** — 确认调用方向、扫描目录和配置 | 本文件 |
| 1 | **创建仓颉桥接层** — 条件前置 GlobalContext + `@Interop[ArkTS]` 桥接类、修饰符约束、回调模式 | [cangjie-bridge-rules.md](references/cangjie-bridge-rules.md) |
| 2 | **创建互操作声明** — `Index.d.ts`、`CustomLib`、类型映射 | [interop-declarations.md](references/interop-declarations.md) |
| 3 | **配置模块依赖** — `oh-package.json5`、loader 声明 | [module-interop-rules.md](references/module-interop-rules.md) |
| 4 | **创建 ArkTS 包装层** — wrapper 类、re-export | [module-interop-rules.md#arkts-包装规则](references/module-interop-rules.md#arkts-包装规则) |
| 5 | **装载与验证** — `requireCJLib`、验证脚本 | 本文件 |
| 6 | **增量函数互操作** — 按函数增量生成互操作代码 | [module-interop-rules.md#增量函数规则](references/module-interop-rules.md#增量函数规则) |
| 7 | **排查运行时问题** — 按顺序排查常见故障 | [interop-reference.md#5-调试顺序](references/interop-reference.md#5-调试顺序) |
| 8 | **编译构建** — 运行构建脚本、按日志排查编译失败 | [build/SKILL.md](build/SKILL.md) |

## 按任务类型路由

| 任务 | 阅读参考 |
|------|-------------------|
| 创建新互操作模块（从零开始） | 任务 0 → 1 → 2 → 3 → 4 → 5 → 8 |
| 修复已有互操作（声明不同步、装载失败等） | 任务 0 → 5 → 7 |
| 按函数增量暴露 | 任务 6 |
| Context 处理 | [cangjie-bridge-rules.md#context-处理](references/cangjie-bridge-rules.md#context-处理) |
| 回调桥接模式选择 | [cangjie-bridge-rules.md#回调桥接模式](references/cangjie-bridge-rules.md#回调桥接模式) |
| 类型映射查表 | [interop-declarations.md#类型映射表](references/interop-declarations.md#类型映射表) |
| 完整工程示例/可套用模板 | [full-hybrid-example.md](references/full-hybrid-example.md) |
| 模块级互操作规则（迁移/派生/打包） | [module-interop-rules.md](references/module-interop-rules.md) |
| 最小闭环代码骨架、调试顺序、常见故障 | [interop-reference.md](references/interop-reference.md) |

## 工作流

### 任务 0：识别工程结构

**扫描前先阅读 [interop-reference.md#3-文件与目录线索](references/interop-reference.md#3-文件与目录线索)。**

确认任务属于"ArkTS 主调，仓颉被调"。若用户只是说"互操作坏了"，先不要直接改调用代码，先对齐以下六项：调用方向、导出符号、生成声明、ArkTS 导入方式、`.so` 名称、ABI/打包配置。

#### 业务代码目录收口（强制规则）

为避免把生成物/桥接层/业务层混在一起，仓颉侧目录约定如下：

- **业务代码必须放在**：`<module>/src/main/cangjie/business/`
- **互操作桥接与边界适配必须放在**：`<module>/src/main/cangjie/bridge/`
- **生成声明与 loader 必须放在**：`types/`、`loader/`、`ark_interop_api/` 等目录（见文档既有规则）
- **导入业务代码时固定使用**：`import <package.name>.bussiness.*`。即使业务文件物理目录是 `business/`，生成互操作 wrapper 时也按 `.bussiness` 作为业务包导入前缀。

检查步骤：

1. 查看 `<module>/src/main/cangjie/business/` 是否存在；若不存在则创建。
2. 检查业务 `.cj` 文件是否散落在 `src/main/cangjie/` 根目录或其他非生成目录中；若是，将这些**业务实现代码**移动到 `business/` 下，并相应更新引用（`package` / `import`）。
3. `src/main/cangjie/package.cj` 按本 skill 的既有规则创建或补齐（固定 `ohos.ark_interop.*` + 读取 `cjpm.toml` 的 `[dependencies]` 生成 import），用于聚合依赖导入。
4. 生成 bridge/wrapper 前，核对业务导入是否统一为 `import <package.name>.bussiness.*`；不要从 bridge 中直接写 `import <package.name>.*` 去抓业务实现。

搜索业务代码以生成互操作 wrapper 时，**不要搜索 `src/main/cangjie/bridge/` 和 `src/main/cangjie/mock/`**。`bridge/` 只用于存放生成出来的仓颉互操作 wrapper，`mock/` 只用于测试/兼容/替身实现，都不是业务源码输入；扫描 public API、列翻译覆盖表、寻找待翻译 `class` / `interface` / `func` 时都必须排除它们。

确认生成策略：先运行 `python3 scripts/scan_interop_project.py <project-root>` 扫描工程结构，根据扫描结果判断：

- **全量翻译**：工程尚未建立互操作 wrapper 时：
  - 若用户明确指定了具体的 `class`、`interface`、`func`，只为这几个对象生成互操作代码。
  - 若用户未指定具体对象，扫描目标范围内所有 `public` 的 `class`、`interface`、`func` 及其他需要暴露的公开互操作对象，统一生成或补齐 bridge、类型声明、`CustomLib` 暴露和 ArkTS wrapper。保持命名、导出和装载方式一致，不要只挑其中一部分对象生成半套 wrapper。
- **增量翻译**：工程已有互操作 wrapper 时：
  - 若用户明确指定了具体的 `class`、`interface`、`func`，只翻译指定的对象及其运行所必需的最小桥接、声明和 wrapper 变更。不要因为看到了其他 `public` 对象就一起补齐。若指定的是 `class` 或 `interface`，只补该对象及其直接依赖的最小公开 surface；若指定的是 `func`，只补该函数需要的最小调用链。
  - 若用户未指定具体对象，为所有 `public` 且尚不存在互操作代码的对象补齐 bridge、声明和 wrapper。

可重复任务优先用脚本：

- 扫现有工程并输出修复建议：`python3 scripts/scan_interop_project.py <project-root>`（会合并检查每个 `cjpm.toml` 的 `[profile.build.combined]`、`[dependencies]` 与 `package.cj`，以及对应模块的 `build-profile.json5` 中 `cangjieOptions.path` / `flattenLibs`；`--json` 结果里见 `interop_config_issues`）
- 按源工程函数生成增量互操作计划：`python3 scripts/plan_incremental_interop.py --source <source-root> --target <target-root> --function <name> [--file <relative-cj-file>]`
- 落完整示例骨架：`python3 scripts/install_hybrid_demo.py --target <dir>`

#### Interop Strategy Gate（强制门禁，避免“偷偷改 public API”）

**默认策略：保留业务 public API 形态（preserve_public_api_shape = true）。**

在决定用 `@Interop[ArkTS]` 还是手写互操作库之前，必须先扫描“准备暴露给 ArkTS 的 public API”里的**所有参数类型、返回值类型、字段类型**。

优先用脚本做一次静态门禁扫描（只读、不改代码）：

```bash
python3 scripts/scan_public_signatures.py --source <module>/src/main/cangjie
```

该脚本默认跳过 `bridge/`、`mock/`、`types/`、`loader/`、`ark_interop_api/` 等非业务输入目录，只扫描业务 public API。

如需机器可读输出：

```bash
python3 scripts/scan_public_signatures.py --source <module>/src/main/cangjie --json
```

然后按以下规则选路：

- **listener/interface 回调**
  - 默认不要要求 ArkTS 去“实现一个仓颉 interface 并传回去”；优先用回调桥接模式（函数参数回调/注册式回调）+ 仓颉侧 adapter（见 [cangjie-bridge-rules.md#回调桥接模式](references/cangjie-bridge-rules.md#回调桥接模式)）。

完成代码生成后，**必须输出一张"翻译覆盖表"**，并细化到函数级别：顶层 `func` 每个函数一行，`class` / `interface` 的每个 `public func` 或需要暴露的成员方法也各自一行，逐项说明哪些函数已翻译、哪些未翻译。若是增量任务，范围至少覆盖"用户指定对象 + 扫描到的同层公开对象及其 public 函数"；不要只报本次改动的一个函数。

**翻译覆盖表模板（按需增删行）：**

| Owner Kind | Owner Name | Function/Member | Source File | Signature | Status | API Shape Changed | Before → After | Notes |
|------------|------------|-----------------|-------------|-----------|--------|-------------------|---------------|-------|
| class | UserService | getUser | `src/main/cangjie/service/UserService.cj` | `public func getUser(id: String): User` | translated | no | - | 已完成 bridge + 声明 + ArkTS wrapper |
| class | UserService | deleteUser | `src/main/cangjie/service/UserService.cj` | `public func deleteUser(id: String): Unit` | not translated | no | - | 未在本次范围；等待用户确认是否纳入 |
| top-level func | Auth | login | `src/main/cangjie/service/Auth.cj` | `public func login(name: String): Bool` | translated | no | - | 已加入桥接类并更新 `Index.d.ts` |
| interface | UserRepo | findAll | `src/main/cangjie/repo/UserRepo.cj` | `public func findAll(): Array<User>` | translated | yes | `Array<User>` → `JSArrayEx<User>` | 边界签名已转为 `JSArrayEx<User>` |

**Checklist:**
- [ ] 定位仓颉源码目录和桥接文件
- [ ] 搜索业务代码时已排除 `src/main/cangjie/bridge/`（bridge 只存放生成的互操作 wrapper）
- [ ] 搜索业务代码时已排除 `src/main/cangjie/mock/`（mock 只用于测试、兼容或替身实现）
- [ ] 若 bridge/wrapper 需要导入业务代码，已使用 `import <package.name>.bussiness.*`
- [ ] 定位 ArkTS 源码目录和 wrapper 文件
- [ ] 确认 `oh-package.json5` 和 `cjpm.toml` 存在且可读，并记录 `cjpm.toml` 的 `[package].name`
- [ ] 若模块含 `src/main/cangjie/`，确认 `package.cj` 符合任务 3「package.cj」规则（`package` 行、`ohos.ark_interop.*`、与 `[dependencies]` 对齐的 `import`）
- [ ] 检查 `ark_interop_api/` 是否为最新生成物
- [ ] 已执行 Interop Strategy Gate：已扫描所有将暴露的 public 签名，并选择了“@Interop / 句柄 / 手写互操作库”的正确路径
- [ ] **默认 preserve_public_api_shape = true：未改变业务 public API 形态**（如确需改变，必须在覆盖表标记 `API Shape Changed = yes` 并写 `Before → After`）
- [ ] 已输出函数级翻译覆盖表（顶层 `func`、`class` 方法、`interface` 方法均逐函数标注 translated / not translated）

### 任务 1：创建仓颉桥接层

**编写桥接代码前先阅读 [cangjie-bridge-rules.md](references/cangjie-bridge-rules.md)。**

#### 1.1 前置：GlobalContext（仅当业务需要 Context 时）

编写或调整桥接前，在仓颉业务与桥接代码中检索：是否误用 `kit.AbilityKit.Context`、`ohos.ability.Context`，或在 `@Interop[ArkTS]` 方法签名中直接暴露能力上下文。若业务需要 `UIAbilityContext`（由 ArkTS 注入），按本节与下文模板添加或复用 `GlobalContext.cj`；否则跳过本节。

**必读：[cangjie-bridge-rules.md#context-处理](references/cangjie-bridge-rules.md#context-处理)**

**固定内容（需要添加包名）：**

创建文件：`<module>/src/main/cangjie/bridge/GlobalContext.cj`

```cj
package <cjpm.package.name>.bridge

import <cjpm.package.name>.*
import ohos.ability.*
import ohos.ability.interop.*
import ohos.ark_interop.*

var ctx:?UIAbilityContext = None
func setContext(runtime: JSContext, callInfo: JSCallInfo): JSValue {
    ctx = createAbilityContextFromJSValue(runtime, callInfo[0])
    runtime.string("hello").toJSValue()
}

let EXPORT_MODULE_CONTEXT = JSModule.registerModule {
    runtime, exports =>
        exports["setContext"] = runtime.function(setContext).toJSValue()
}
```

**使用规则：**
- 文件路径：`<module>/src/main/cangjie/bridge/GlobalContext.cj`（与其他桥接文件同目录）
- 业务代码通过 `ctx.getOrThrow()` 获取 Context
- 桥接方法签名中**不暴露** Context 参数
- 已有同用途文件则复用，不重复创建
- 若需要导出**全局变量**或 **`public` 成员上的 `static` 变量**，统一放在 `GlobalVar.cj` 中（不存在则新建，存在则复用），不要散落到其他 bridge 文件

**Checklist:**
- [ ] 除按说明补充模块包名/路径外，模板核心（导入、`setContext`、`registerModule`）与文档一致，不自创 Context 注入实现
- [ ] 导入 `ohos.ability.*` 和 `ohos.ability.interop.*`（不是 `kit.AbilityKit`）
- [ ] 使用 `UIAbilityContext` 类型（不是 `Context`）
- [ ] 使用 `createAbilityContextFromJSValue` 转换
- [ ] 使用 `JSModule.registerModule` 导出
- [ ] 若存在全局变量或 `public static` 成员导出需求，已按下文“全局变量 / static 变量导出规则”统一放入 `GlobalVar.cj`（不存在则新建）

#### 1.1.1 全局变量 / static 变量导出规则

当仓颉业务代码里存在需要给 ArkTS 暴露的全局变量，或 `public class` 中的 `public static let/var` 成员时，统一在 `GlobalVar.cj` 中用 `JSModule.registerModule` 导出（文件不存在则新建，已存在则增量复用）。

**规则 1：简单类型直接导出值**

适用范围：`String`、整数、浮点、布尔等简单类型。

若业务代码中有：

```cj
public class FileDownloader {
    public static let DOWNLOADING: String = "DOWNLOADING"
    public static let STOP: String = "STOP"
    public static let CANCEL: String = "CANCEL"
}
```

则在 `GlobalVar.cj` 中生成同类导出：

```cj
let EXPORT_MODULE_CONTEXT = JSModule.registerModule {
    runtime, exports =>
        exports["STATE_DOWNLOADING"] = runtime.string("DOWNLOADING").toJSValue()
        exports["STATE_STOP"] = runtime.string("STOP").toJSValue()
        exports["STATE_CANCEL"] = runtime.string("CANCEL").toJSValue()
}
```

要求：

- 简单类型值直接转成 `JSValue` 后挂到 `exports[...]`
- 导出代码放在 `GlobalVar.cj`（不存在则新建），不要另起新的 bridge 文件
- 导出名可按业务语义重命名，但必须稳定且在声明、ArkTS 侧引用中保持一致

**规则 2：复杂类型用 accessor 暴露 getter**

适用范围：自定义类型、需要调用对象自己的 `toJSValue(...)` 才能转换的对象。

若业务代码中有：

```cj
public class C {
    func toJSValue(context: JSContext) {
        context.string("a").toJSValue()
    }
}

public var globalVar: C = C()
```

则在 `GlobalVar.cj` 中生成：

```cj
let EXPORT_GLOBAL_VAR = JSModule.registerModule {
    runtime, exports =>
        let getterGlobalVar = runtime.function {
            context, callInfo =>
                globalVar.toJSValue(runtime)
        }
        exports.defineOwnAccessor("globalVar", getter: getterGlobalVar)
}
```

要求：

- 复杂类型不要把对象本体直接塞进 `exports[...]`
- 为每个复杂全局对象生成 getter，并通过 `defineOwnAccessor(...)` 暴露
- getter 内调用真实对象的 `toJSValue(runtime)` 或等价转换逻辑
- 生成代码仍然放在 `GlobalVar.cj`（不存在则新建）

#### 1.2 创建桥接类

创建文件：`<module>/src/main/cangjie/bridge/<Feature>.cj`

```cj
package <cjpm.package.name>.bridge

import <cjpm.package.name>.*
import ohos.ark_interop.*
import ohos.ark_interop_macro.*

@Interop[ArkTS]
public class <Feature> {
    public init() { }

    public func exampleMethod(param: String): String {
        // 业务逻辑...
        param
    }
}
```

**Checklist:**
- [ ] 生成的仓颉互操作 wrapper 代码统一放在 `src/main/cangjie/bridge/` 目录下，包括 `@Interop[ArkTS]` class/interface/func、`GlobalContext.cj`、手写 `SharedObject & JSInteropType<T>` 类型、边界适配 helper；不要把新生成的互操作 wrapper 散落到业务源码目录
- [ ] 已读取实际 `cjpm.toml` 的 `[package].name`；所有 `bridge/` 下生成的仓颉文件 package 均为 `<package.name>.bridge`，并导入 `import <package.name>.*`
- [ ] bridge 文件命名：`<业务文件名去掉.cj>Bridge.cj`（例如 `FileDownloaderManager.cj` → `FileDownloaderManagerBridge.cj`）
- [ ] class / interface / 顶层 func 命名：优先与业务代码同名；仅在产生冲突时加 `Bridge` 后缀（例如 `FileDownloaderManager` → `FileDownloaderManagerBridge`）；**成员函数名永远与业务代码保持一致，不加任何后缀**
- [ ] 加了 `Bridge` 后缀时，在翻译覆盖表 `Notes` 中写明 `原名 -> 新名`，并在 bridge、`.d.ts`、`CustomLib`、ArkTS wrapper、`Index.ets` re-export 中统一使用新名
- [ ] 翻译仓颉 `interface` 时，互操作侧 interface 文件也放在 `bridge/`；若原 interface 已在 `bridge/` 内，可直接在原 `interface` 上添加 `@Interop[ArkTS]`，否则在 `bridge/` 中生成同名互操作 interface，不额外生成继承类或继承 interface；互操作 wrapper / 声明 / ArkTS 引用命名与原 `interface` 名称保持一致
- [ ] 给 `interface` 添加 `@Interop[ArkTS]` 前，扫描所有公开签名：`HashMap<K, V>` 改为 `JSHashMapEx<K, V>`，`Array<T>` 改为 `JSArrayEx<T>`，再同步生成 ArkTS 声明类型（`Map<K, V>` / `Array<T>`）
- [ ] 同时导入 `ohos.ark_interop.*` 和 `ohos.ark_interop_macro.*`
- [ ] 使用 `@Interop[ArkTS]` 标记需要暴露给 ArkTS 的类
- [ ] 只使用 `public` 修饰符（不能用 `open`, `protected`, `mut`）
- [ ] 只导出稳定、扁平、边界清晰的接口
- [ ] 在桥接层主动构造 `JSHashMapEx` / `JSArrayEx` 等互操作集合并调用 ArkTS listener 时，使用 `JSCurrentJSContext.set(mainThreadContext)` 包裹构造与调用逻辑，结束后调用 `JSCurrentJSContext.unset()`，确保操作在正确 JSContext 下进行（详见 `cangjie-bridge-rules.md#jshashmapex--jsarrayex-与-jscurrentjscontext`）
- [ ] 若业务层存在 `spawn { ... }` 后台线程触发“仓颉 → ArkTS”互操作回调：**不改 business 代码**，在生成的互操作桥接层中用 `mainThreadContext.getOrThrow().postJSTask { ... }` 投递回主 JS 线程执行，并在 task 内按规则 `JSCurrentJSContext.set(...)` / `unset()`（详见 `cangjie-bridge-rules.md#spawn--后台线程调用-arkts-回调`）
- [ ] **`@Interop[ArkTS]` 类的 `public` 成员签名中不引用其他 `@Interop[ArkTS]` 类**（参数、返回值、字段均不可）；若确有跨类协作，三选一重构：(1) 被引用方降级为仓颉内部普通 `public` 业务类；(2) 句柄模式（返回 id，仓颉侧 `HashMap` 持有真实对象）；(3) 手写互操作库（整类改为 `<: SharedObject & JSInteropType<T>`，自行实现 `registerClass` + `jsConstructor` + `xxx_ArkTS_Interop_Identifier` 跳板 + `toJSValue` / `fromJSValue` / `toArkTsType`，不再用 `@Interop[ArkTS]` 宏）。详见 [cangjie-bridge-rules.md#interop-类之间禁止相互引用](references/cangjie-bridge-rules.md#interop-类之间禁止相互引用)
- [ ] 回调使用函数参数或注册式模式（见 [cangjie-bridge-rules.md#回调桥接模式](references/cangjie-bridge-rules.md#回调桥接模式)）
- [ ] **如需 Context，从 `GlobalContext.ctx.getOrThrow()` 获取，不在方法签名中暴露**

### 任务 2：创建互操作声明

**编写互操作声明前先阅读 [interop-declarations.md](references/interop-declarations.md)。**

1. 创建 types 声明目录：`<module>/src/main/cangjie/types/lib<module>/`（见 [interop-declarations.md#声明文件创建](references/interop-declarations.md#声明文件创建)）
2. 创建 loader 声明目录：`<module>/src/main/cangjie/loader/`（见 [interop-declarations.md#声明文件创建](references/interop-declarations.md#声明文件创建)）
3. 确保类型映射与仓颉桥接类一致（见 [interop-declarations.md#类型映射表](references/interop-declarations.md#类型映射表)）

**Checklist:**
- [ ] 文件命名为 `Index.d.ts`（不是 `Index.d.ets`）
- [ ] `oh-package.json5` 的 name 与 `.so` 名称一致
- [ ] `CustomLib` 定义在 `.d.ts` 中（不是 `.ets`）
- [ ] 类型声明使用 `export declare class`（不是 `export class`）
- [ ] 类型映射与仓颉桥接类一致（见 [interop-declarations.md#类型映射表](references/interop-declarations.md#类型映射表)）
- [ ] loader 的 name 固定为 `"libark_interop_loader.so"`
- [ ] **如使用 GlobalContext，在 `.d.ts` 增加 `import { common } from "@kit.AbilityKit"`**
- [ ] **如使用 GlobalContext，在 `CustomLib` 增加 `setContext(ctx: common.UIAbilityContext): void;`**

### 任务 3：配置模块依赖

**编辑配置前先阅读 [module-interop-rules.md#打包和构建规则](references/module-interop-rules.md#打包和构建规则)。**

#### build-profile.json5（强制检查）

处理含仓颉互操作的模块时，打开该模块下的 `build-profile.json5`，在各构建 target 中定位 `buildOption.cangjieOptions`（若工程 JSON5 层级与 DevEco 模板不一致，以文件内实际嵌套为准，字段名仍为 `cangjieOptions`）。

1. **检查** `cangjieOptions` 是否包含 `"flattenLibs": true`。
2. **若缺少 `flattenLibs`，或值为 `false`**：在对应 `cangjieOptions` 对象内补齐为至少包含：

```json5
"cangjieOptions": {
  "path": "./cjpm.toml",
  "flattenLibs": true
}
```

3. **若已有 `path`** 且已正确指向本模块的 `cjpm.toml`，保留现有 `path`，仅新增或改为 `"flattenLibs": true`。
4. **`path` 含义**：`./cjpm.toml` 相对该 HAR/HSP 模块根目录，须与模块内真实 `cjpm.toml` 位置一致。

#### cjpm.toml（`profile.build.combined`，强制检查）

互操作模块的 `cjpm.toml` 需满足 CJPM 对 **combined 构建 profile** 的约定（见 [CJPM 用户指南（中文）](https://gitcode.com/Cangjie/cangjie_tools/blob/main/cjpm/doc/user_guide_zh.md) 中 `profile.build.combined` 相关说明）。

1. 先读取本模块 `cjpm.toml` 的 **`[package].name`**（下文记为 `<cjpm.package.name>`），不要用目录名或 `oh-package.json5` 的模块名猜测。
2. **检查** 是否存在表头 **`[profile.build.combined]`**。
3. **若不存在该表**：在文件中新增（键名为包名，值为 `"dynamic"`）：

```toml
[profile.build.combined]
# 左侧键名必须等于本文件 [package].name，例如 name = "filedownloader" 时：
filedownloader = "dynamic"
```

示例：若 `[package].name = "filedownloader"`，则为 `filedownloader = "dynamic"`（与 [CJPM 用户指南](https://gitcode.com/Cangjie/cangjie_tools/blob/main/cjpm/doc/user_guide_zh.md) 示例一致，只是 key 随包名变化）。

4. **若已存在 `[profile.build.combined]`** 但缺少以 `<cjpm.package.name>` 为键的项：在同一表下追加一行 `<cjpm.package.name> = "dynamic"`，不要覆盖该表中其他包的条目。
5. **若该键已存在**：不要擅自改成别的值；仅当用户明确要求或构建文档指明时才调整。

#### `package.cj`（仓颉根目录，强制检查）

路径：`<module>/src/main/cangjie/package.cj`（与 `cjpm.toml` 同模块的仓颉根目录）。

1. **若不存在该文件**：创建；**若已存在**：校验收口（见下），缺则补，不要随意删掉工程里已有且仍需要的 `import`。
2. **第一行 `package`**：必须为 `cjpm.toml` 中 **`[package].name`** 的取值（与 `bridge/` 等业务源码的包声明根一致），例如 `[package].name = "filedownloader"` 时写 `package filedownloader`（含多级包名时整串照抄，如 `ohos_app_cangjie_library`）。
3. **固定导入（互操作必备）**：文件中须包含  
   `import ohos.ark_interop.*`  
   （各 `bridge/` 等源码里若另有 `ohos.ark_interop_macro.*`、`ohos.ability.*` 等，仍在各自 `.cj` 中声明；`package.cj` 只保证聚合互操作核心与 CJPM 依赖。）
4. **按配置导入**：读取同一模块 `cjpm.toml` 的 **`[dependencies]`** 表，将其中**每个一级依赖键名** `dep_name` 转成一行：  
   `import dep_name.*`  
   与 `cjpm.toml` 里该键右侧是 `path`、`git`、`version` 等何种形态无关，**只取键名**。

**示例**：`cjpm.toml` 片段

```toml
[dependencies]
  j2cj = { path = "./libs/j2cj" }
  xml_ffi = { git = "https://gitcode.com/Cangjie-TPC/xml-ffi.git", branch = "xml-1.0.5_cangjie-plugin-5.1.1.851" }
```

若 `[package].name = "filedownloader"`，则 `package.cj` 至少为：

```cj
package filedownloader

import ohos.ark_interop.*
import j2cj.*
import xml_ffi.*
```

`import` 顺序建议：**先固定** `ohos.ark_interop.*`，**再按 `cjpm.toml` 中 `[dependencies]` 键的出现顺序**列出各 `import <键>.*`（键名含下划线时保持原样）。

5. **边界**：若依赖声明在 target 专属表而非根 `[dependencies]`，以工程实际为准合并进 `package.cj`；不要为 `cjpm.toml` 里没有的键发明 `import`。

更新 `<module>/oh-package.json5`：

```json5
{
  "name": "<module>",
  "version": "1.0.0",
  "description": "<Module> HAR with Cangjie-ArkTS interop support",
  "main": "./src/main/ets/Index.ets",
  "types": "./Index.d.ets",
  "license": "Apache-2.0",
  "dependencies": {
    "libark_interop_loader.so": "file:src/main/cangjie/loader",
    "lib<module>.so": "file:src/main/cangjie/types/lib<module>"
  }
}
```

**Checklist:**
- [ ] `main` 设为 `"./src/main/ets/Index.ets"`（完整路径 + 扩展名）
- [ ] `types` 指向根目录 `Index.d.ets`
- [ ] 两个依赖指向不同目录：`loader/` 和 `types/lib<module>/`
- [ ] `build-profile.json5` 中 `buildOption.cangjieOptions.path` 指向模块 `cjpm.toml`（通常为 `./cjpm.toml`）
- [ ] `buildOption.cangjieOptions` 已配置 `"flattenLibs": true`（若缺失则按本节「build-profile.json5（强制检查）」补齐）
- [ ] `cjpm.toml` 已配置 `[profile.build.combined]`，且包含键 `<cjpm.toml [package].name>`、值为 `"dynamic"`（若缺失则按本节「cjpm.toml（profile.build.combined）」补齐）
- [ ] `src/main/cangjie/package.cj` 存在；`package` 行与 `[package].name` 一致；含 `import ohos.ark_interop.*`；`[dependencies]` 各键均有对应 `import <键>.*`（若缺失则按本节「package.cj」创建或补齐）
- [ ] `abiFilters` 同时包含 `arm64-v8a` 和 `x86_64`（除非用户明确只面向一种）

### 任务 4：创建 ArkTS 包装层

**编写包装层前先阅读 [module-interop-rules.md#arkts-包装规则](references/module-interop-rules.md#arkts-包装规则)。**

**src/main/ets/<feature>/<Feature>Client.ets**：

```typescript
/**
 * <Feature> ArkTS wrapper
 */

import { requireCJLib } from 'libark_interop_loader.so';
import {
  <Feature>Bridge as CJ<Feature>Bridge,
  CustomLib
} from 'lib<module>.so';

let globalCJLib: CustomLib | undefined = undefined;

function getCJLib(): CustomLib {
  if (globalCJLib === undefined) {
    globalCJLib = requireCJLib('lib<module>.so') as CustomLib;
  }
  return globalCJLib;
}

export interface <Feature>Options {
  // 配置选项...
}

export class <Feature>Client {
  private bridge: CJ<Feature>Bridge;

  constructor(options?: <Feature>Options) {
    const lib = getCJLib();
    this.bridge = new lib.<Feature>Bridge();
  }

  public exampleMethod(param: string): string {
    return this.bridge.exampleMethod(param);
  }
}
```

**src/main/ets/Index.ets**：

```typescript
export { <Feature>Client } from './<feature>/<Feature>Client';
```

**<module>/Index.d.ets**：

```typescript
export { <Feature>Client } from './src/main/ets/<feature>/<Feature>Client';
export { <Feature>Bridge, CustomLib } from 'lib<module>.so';
```

**Checklist:**
- [ ] wrapper 从 `lib<module>.so` 导入（不是相对路径）
- [ ] `requireCJLib` 结果在模块作用域缓存
- [ ] `Index.ets` 只做 re-export，不包含实现逻辑
- [ ] CJ 类型只在功能子目录内部使用，不 export 到 `Index.ets`

### 任务 5：装载与验证

ArkTS 侧优先检查：

- 是否从 `libark_interop_loader.so` 导入 `requireCJLib`
- `requireCJLib("libxxx.so")` 里的库名是否与实际仓颉产物一致
- 类型断言是否指向生成的 interop 声明或与其一致的本地 interface
- 所在模块的 `oh-package.json5` 是否同时声明了 `libark_interop_loader.so` 和被装载的 `libxxx.so` 文件依赖

若库名是拍脑袋写的，先去工程配置或构建产物中核对，不要继续猜。

**验证脚本**：`python3 scripts/verify_interop_structure.py --module <module> --check-types`（含 `cjpm.toml` / `build-profile.json5` / `package.cj` 与技能文档一致的静态校验）

**Checklist:**
- [ ] `loader/oh-package.json5` 中 name 是 `"libark_interop_loader.so"`
- [ ] `types/lib<module>/oh-package.json5` 中 name 是 `"lib<module>.so"`
- [ ] 模块 `oh-package.json5` 中 main 是 `"./src/main/ets/Index.ets"`
- [ ] 两个依赖指向不同目录
- [ ] 类型声明使用 `export declare class`
- [ ] `CustomLib` 定义在 `.d.ts` 中
- [ ] ArkTS wrapper 从 `lib<module>.so` 导入
- [ ] 生成的仓颉互操作 wrapper 代码均位于 `src/main/cangjie/bridge/`，未散落在业务源码目录
- [ ] `bridge/` 下生成的仓颉文件 package 为 `<cjpm.toml [package].name>.bridge`，且包含 `import <cjpm.toml [package].name>.*`
- [ ] 类型映射正确
- [ ] 所有 `@Interop[ArkTS]` 类的方法只使用 `public` 修饰符
- [ ] 文件扩展名正确：`.d.ts` 不是 `.d.ets`

### 任务 6：增量函数互操作

**生成增量代码前先阅读 [module-interop-rules.md#增量函数规则](references/module-interop-rules.md#增量函数规则)。**

先判断本次任务走增量翻译还是全量翻译（见任务 0）：

- **增量翻译**：工程已有互操作 wrapper 时，若用户指定了具体对象则只补这几个，否则为所有 `public` 且尚不存在互操作代码的对象补齐。
- **全量翻译**：工程尚未建立互操作 wrapper 时，若用户指定了具体对象则只为这几个生成，否则扫描所有 `public` 对象统一生成。

当用户指定源工程、目标工程、文件或函数名时：

1. 运行 `python3 scripts/plan_incremental_interop.py --source <source-root> --target <target-root> --function <name> [--file <relative-cj-file>]` 定位源函数签名和目标缺口。
2. 先把业务函数增量补到目标同路径 Cangjie 文件；如果函数体为空，也照源函数保留空实现，不自行发明业务逻辑。
3. 在目标已有 `@Interop[ArkTS]` 桥接类中添加同名或语义一致的方法，把 ArkTS 扁平参数转换成业务函数需要的 Cangjie 对象。
4. 更新生成声明或临时 `.d.ts`，并在 ArkTS wrapper 中添加对应方法。只改这个函数需要的最小调用链。
5. 最后扫描目标工程，并用文本搜索确认函数名同时出现在业务层、桥接层、声明层和 ArkTS wrapper。
6. 输出本次范围的函数级翻译覆盖表，至少包含：用户指定对象、同文件/同模块下扫描到的 `public class`、`public interface` 的每个 `public func`，以及顶层 `public func`；逐函数标注 `translated` 或 `not translated`。

不要把源工程整目录覆盖到目标工程来实现单函数增量；除非用户明确要求同步目录。

**Checklist:**
- [ ] 源函数签名已定位
- [ ] 业务函数已增量补到目标
- [ ] 桥接方法已添加
- [ ] 类型声明已更新
- [ ] ArkTS wrapper 已更新
- [ ] 函数名在四层（业务/桥接/声明/wrapper）均出现
- [ ] 若需 Context：已确认任务 1 存在 `GlobalContext.cj`，且任务 2 声明与 ArkTS 侧 `setContext` 调用链已同步
- [ ] 已输出增量范围内的函数级翻译覆盖表（包括未翻译函数）

### 任务 7：排查运行时问题

**排查故障前先阅读 [interop-reference.md#5-调试顺序](references/interop-reference.md#5-调试顺序)。**

按这个顺序排查：

1. `@Interop[ArkTS]` 是否标到了真正导出对象上。
2. 互操作声明是否重新生成过。
3. ArkTS 调用名是否与导出名一致。
4. `requireCJLib` 的 `.so` 名称是否正确。
5. ABI 是否覆盖目标设备或模拟器。
6. 是否把 ArkTS 线程相关对象带到了其他线程。
7. 如果是异步导出，检查是否误用 `JSStringEx`、`JSArrayEx<T>`、`JSHashMapEx<K, V>`。
8. 如果调用为 `undefined`，检查是否存在 `registerModule`、`registerClass`、`registerFunc` 与宏导出同名覆盖。

### 任务 8：编译构建

**编译前先阅读 [build/SKILL.md](build/SKILL.md)。**

互操作代码写完后，运行构建脚本验证编译是否通过：

```bash
python3 skills/x2cj/build/build.py --project-root <DevEco project root>
```

环境要求：设置 `DEVECO_HOME`（DevEco Studio 安装根目录）和 `CANGJIE_SDK_HOME`（仓颉 SDK 根目录，须包含 `compiler/`）。

构建成功标志：日志中出现 `BUILD SUCCESSFUL`。完整日志在项目目录的 `build.log` 中。

若编译失败，阅读 `build.log` 定位错误，修复后重新构建，重复此过程直到编译成功。排查优先级：

1. **分析日志**：从 `build.log` 中定位仓颉编译错误或 ArkTS 类型错误，修复对应源码或配置。
2. **查文档**：如果日志信息不足以定位问题，参考 [build/SKILL.md](build/SKILL.md) 的故障排查流程和 [interop-reference.md#5-调试顺序](references/interop-reference.md#5-调试顺序)。
3. **请用户协助**：如果仍无法解决，请用户在 DevEco Studio 中复现并分享完整错误信息。

## 工作规则

###  Context 处理强制规范

**如仓颉业务代码涉及 `Context`，必须遵守以下规则（不可变通）：**

1. **固定模板**：按 [cangjie-bridge-rules.md#context-处理](references/cangjie-bridge-rules.md#context-处理) 的固定内容创建 `GlobalContext.cj`，不可自行发明实现
2. **正确导入**：使用 `import ohos.ability.*` 和 `import ohos.ability.interop.*`（不是 `kit.AbilityKit`）
3. **正确类型**：使用 `UIAbilityContext`（不是 `Context`）
4. **JSModule 导出**：必须用 `JSModule.registerModule` + `createAbilityContextFromJSValue`
5. **方法签名**：桥接方法签名中不暴露 Context 参数，业务逻辑内部通过 `ctx.getOrThrow()` 获取
6. **声明同步**：`.d.ts` 增加 `import { common } from "@kit.AbilityKit"` 和 `setContext(ctx: common.UIAbilityContext): void;`

### 通用规则

- 最小闭环优先：先打通一个函数或一个类，再扩展。
- 工具生成优先：能从工具生成，就不要手工复制声明。
- 本地环境优先：遇到版本差异时，以本地 SDK/DevEco Studio 生成结果为准。
- 复用骨架：需要完整目录骨架或可改模板时，运行 `scripts/install_hybrid_demo.py`。
- 先扫描后改：处理现有工程时，先运行 `scripts/scan_interop_project.py` 生成修复顺序。
