# ArkTS 调用仓颉互操作参考

## 目录

1. 适用范围
2. 最小闭环
3. 文件与目录线索
4. 代码骨架
5. 调试顺序
6. 常见故障
7. 线程与边界约束
8. 处理策略

## 1. 适用范围

本参考聚焦“ArkTS 主调，仓颉被调”。

典型触发词：

- ArkTS 调仓颉
- 仓颉封装成 ArkTS 库
- `requireCJLib`
- `libark_interop_loader.so`
- `@Interop[ArkTS]`
- `Generate Cangjie-ArkTS Interop API`
- `ark_interop_api`

## 2. 最小闭环

先把互操作压缩成这条最小链路：

1. 在仓颉里导出一个简单函数。
2. 生成互操作声明。
3. 在 ArkTS 里通过 `requireCJLib` 装载仓颉库。
4. 成功完成一次同步调用。

最小闭环稳定后，再上类、回调、组件、页面跳转或异步调用。

## 3. 文件与目录线索

如果用户给的是一个现成 HarmonyOS 工程，优先先跑：

```bash
scripts/scan_interop_project.py /path/to/project
```

先拿到候选目录、`requireCJLib` 库名和互操作标记摘要，再开始手改。

当前脚本还会额外输出：

- 推荐修复顺序
- 疑似缺失的 `@Interop[ArkTS]` 导出
- `ark_interop_api` 与仓颉导出不一致的线索
- `abiFilters` 对真机和模拟器的覆盖风险

优先搜索这些文件：

- `*.cj`
- `*.ets`
- `*.ts`
- `*.d.ets`
- `*.d.ts`
- `cjpm.toml`
- `src/main/cangjie/package.cj`（仓颉根聚合 `import`，与 `[package].name` 及 `cjpm.toml` 的 `[dependencies]` 对齐）
- `build-profile.json5`
- `oh-package.json5`

注意：如果搜索目的是“从业务代码生成互操作 wrapper”，扫描 `*.cj` 时必须排除 `src/main/cangjie/bridge/` 和 `src/main/cangjie/mock/`；`bridge/` 只用于存放生成的互操作 wrapper，`mock/` 只用于测试、兼容或替身实现。只有在排查已生成互操作链路时，才把 `bridge/` 作为检查对象。

优先搜索这些关键词：

- `@Interop[ArkTS]`
- `requireCJLib`
- `libark_interop_loader.so`
- `ark_interop_api`
- `CJHybridComponent`
- `registerJSFunc`
- `unregisterJSFunc`
- `@Interop[ArkTS, Async]`
- `JSRuntime`、`JSContext`、`JSCallInfo`
- `JSModule.registerModule`、`registerClass`、`registerFunc`

常见线索目录：

- `src/main/cangjie/`
- `src/main/cangjie/ark_interop_api/`
- `src/main/ets/`
- `src/main/arkts/`

## 4. 代码骨架

### 4.1 仓颉侧最小导出

```cj
package <package.name>.bridge

import <package.name>.*
import ohos.ark_interop.*
import ohos.ark_interop_macro.*

@Interop[ArkTS]
public func addNumber(a: Float64, b: Float64): Float64 {
    a + b
}
```

如果要导出类，优先导出无歧义构造参数和少量实例方法，不要一开始就导出复杂继承层级。

### 4.2 ArkTS 侧最小装载

**函数导出**（仓颉导出的是 `func`，不是 `class`）：

```ts
import { requireCJLib } from "libark_interop_loader.so"

interface CustomLib {
  addNumber(a: number, b: number): number
}

const cjLib = requireCJLib("libxxx.so") as CustomLib
const result = cjLib.addNumber(1, 2)
```

**类导出**（仓颉导出的是 `@Interop[ArkTS] class`，需通过构造签名创建实例）：

```ts
import { requireCJLib } from "libark_interop_loader.so"
import { <Feature>Bridge, CustomLib } from "lib<module>.so"

const cjLib = requireCJLib("lib<module>.so") as CustomLib
const bridge = new cjLib.<Feature>Bridge()
bridge.exampleMethod("hello")
```

其中 `"libxxx.so"` 必须按工程实际产物核对。不同工程模板、module 配置和版本下库名可能不同，不要硬编码猜测值。

### 4.3 优先使用生成声明

如果工程已经通过 IDE 菜单或对应构建流程生成 `ark_interop_api`，优先从生成声明导入类型，再调用 `requireCJLib`。

只有在以下场景下才手写 ArkTS interface：

- 生成物丢失，需要先验证链路
- 需要快速定位是“库装载失败”还是“声明不匹配”
- 用户只要最小 PoC，不要求接入正式生成物

## 5. 调试顺序

### 5.1 编译前

先核对：

1. 仓颉导出对象是否为 `public`
2. 是否正确使用 `@Interop[ArkTS]`
3. 是否引入互操作相关包
4. 是否重新生成 interop 声明

### 5.2 编译时

重点看：

1. 生成目录是否出现 `ark_interop_api`
2. ArkTS 类型声明是否与仓颉导出一致
3. `.so` 是否成功打入应用

### 5.3 运行时

重点看：

1. `requireCJLib` 是否能成功拿到库对象
2. 调用名是否和导出名一致
3. 设备 ABI 是否匹配
4. 是否因线程切换导致运行时异常

## 6. 常见故障

### 6.1 `requireCJLib` 成功导入，但调用时报未定义

通常先查：

- 仓颉函数没加 `@Interop[ArkTS]`
- 导出对象不是 `public`
- `ark_interop_api` 没重生成
- ArkTS interface 仍是旧版本

### 6.2 `.so` 装载失败

通常先查：

- `requireCJLib("libxxx.so")` 的名字不对
- 构建产物没被打包
- module 名称、产物名称或配置已变更
- 模拟器或设备 ABI 不匹配

如果是在模拟器上复现，检查 `build-profile.json5` 是否覆盖 `x86_64`。

### 6.3 改了仓颉代码但 ArkTS 侧类型没变

通常是生成声明没有更新。优先删掉陈旧生成物并重新执行生成流程，再检查引用路径有没有指向旧文件。

### 6.4 类能创建，方法调用异常

通常先查：

- 方法是否实际被导出
- 参数类型是否发生数值宽度变化
- ArkTS 声明与仓颉签名不一致

### 6.5 回调或页面跳转相关逻辑不稳定

如果互操作里还叠加了回调注册、页面跳转、组件嵌入，优先把问题收缩到“纯函数调用”闭环。确认基础互操作没问题，再恢复回调和生命周期逻辑。

## 7. 线程与边界约束

ArkTS 运行时通常按单线程约束理解。处理互操作时遵守这几条：

1. 需要 ArkTS 上下文或 ArkTS API 的逻辑，默认放回 ArkTS 线程执行。
2. 不要把依赖 ArkTS 线程的对象直接带到其他线程继续使用。
3. 进入其他线程前，优先把需要的数据转换成纯仓颉数据。
4. 如果跨线程回到 ArkTS 侧执行逻辑，优先用对应上下文切回 ArkTS 线程。

## 8. 处理策略

### 8.1 用户要“从零搭起来”

按这个顺序做：

1. 新增一个最小 `@Interop[ArkTS]` 函数
2. 生成 `ark_interop_api`
3. 在 ArkTS 装载 `.so`
4. 用最小页面或测试代码调用一次

### 8.2 用户要“修现有工程”

按这个顺序做：

1. 先运行 `scripts/scan_interop_project.py`
2. 先看脚本输出的 `Recommended next steps` 和 `Potential inconsistencies`
3. 识别现有生成物和真实导出点
4. 找出声明、库名、调用点三者的不一致
5. 修最小差异
6. 验证同步调用
7. 最后再恢复复杂业务逻辑

### 8.3 用户要“给出范例”

默认给：

- 一个仓颉导出函数
- 一个 ArkTS 侧 `requireCJLib` 调用
- 一个说明如何替换真实 `.so` 名称的注释

不要默认给大而全模板，除非用户明确要求完整混合工程。

如果用户明确要目录骨架，优先运行：

```bash
scripts/install_hybrid_demo.py --target /path/to/output
```
