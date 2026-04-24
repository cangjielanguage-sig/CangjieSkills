# 声明式互操作宏 @Interop

## 路径选择：宏优先

| 方向 | 首选工具 | 说明 |
|------|---------|------|
| ArkTS 调用仓颉 | `@Interop` 宏（`ohos.ark_interop_macro`） | 自动生成 `.d.ts` 与胶水层 |
| 仓颉调用 ArkTS | `ohos.ark_interop` 库（`JSRuntime`/`JSContext`） | 加载系统模块、操作 JSObject |
| 宏覆盖不了时 | `ohos.ark_interop` 库手工注册 | `registerModule`/`registerFunc` |

> 宏生成仍依赖 `ark_interop` 运行时，两个 import 都需要。互操作核心类型：`JSValue`、`JSContext`、`JSCallInfo`、`JSRuntime`。

## 动手前确认

1. **方向**：ArkTS→仓颉？仓颉→ArkTS？双向？
2. **导出形态**：函数 / Async / interface / class / enum？
3. **类型边界**：是否涉及 JSStringEx / JSArrayEx / JSHashMapEx / 回调 / 多线程？
4. **线程**：互操作逻辑须在运行时绑定线程上执行
5. **工程**：包名与 `cjpm.toml`、`lib*.so`、ArkTS import 一致；`.d.ts` 生成后 `oh-package.json5` 依赖已加

## 最小示例

```cangjie
package ohos_app_cangjie_entry
import ohos.ark_interop.*
import ohos.ark_interop_macro.*

@Interop[ArkTS]
public func addF64(a: Float64, b!: Float64): Float64 { a + b }
```

DevEco 右键 **Generate → Cangjie-ArkTS Interop API** 在 `cangjie/types/libohos_app_cangjie_entry/` 下生成 `Index.d.ts`，ArkTS 侧 `import { addF64 } from 'libohos_app_cangjie_entry.so'` 调用。

## 场景速查

| 目标 | 宏写法 | 关键约束 |
|------|--------|---------|
| 导出函数 | `@Interop[ArkTS]` | public、无泛型、无默认值；命名参数可用但 ArkTS 侧与普通参数一致 |
| 异步(Promise) | `@Interop[ArkTS, Async]` | **禁用** JSStringEx/JSArrayEx/JSHashMapEx |
| ArkTS→仓颉传对象 | `interface` + `prop`/`func` | 不支持泛型、不支持继承其他接口、不支持操作符重载；支持成员函数和 `mut prop` |
| 仓颉→ArkTS返对象 | `class` | public构造、无泛型、不支持成员变量形参/默认值；不支持静态初始化器/操作符重载；多构造函数不能对应相同 ArkTS 签名；成员变量须 public 且不可省略类型标注；可继承但不展开 |
| 枚举 | `enum` | ArkTS 映射为 `const enum`；**不支持带参数的构造器** |
| 隐藏成员 | `@Interop[ArkTS, Invisible]` | ArkTS 无法理解的类型**必须**隐藏 |

## Async 异步函数

最小示例：

```cangjie
@Interop[ArkTS, Async]
public func doAsync(a: Float64, b: Float64): Float64 {
    a + b
}
```

ArkTS 侧生成声明形态为 `Promise<number>`。

### Async 替代方案（集合数据怎么传）

Async 函数禁用 JSArrayEx（它绑定 JSRuntime，`spawn` 跨线程会崩溃）。替代：**传 String JSON + `stdx.encoding.json` 纯仓颉解析**：

```cangjie
import stdx.encoding.json.*

@Interop[ArkTS, Async]
public func analyzeAsync(jsonStr: String): Result {
    // ✅ String 是值类型，安全跨线程；纯仓颉解析，不碰 JSRuntime
    let jv = JsonValue.fromStr(jsonStr)
    let arr = jv.asObject()["records"].asArray()
    // ...
}
// ❌ Async 中用 JSArrayEx 会编译失败
```

> **备选方案**：若 `stdx.encoding.json` 在仓颉侧解析特定结构出现兼容问题，可改为：ArkTS 侧完成 JSON 解析，将每条数据构造为 `@Interop interface` 对象，通过同步 `@Interop` 函数（如 `addRecord`）逐条传入仓颉，再调用 Async 函数做计算（参数仅传简单值类型）。这样仓颉侧完全不接触 JSON 字符串。

### Async 与多线程切换的关系（重要）

`@Interop[ArkTS, Async]` 宏**自动**完成"spawn 仓颉线程执行 → 切回 ArkTS 线程 resolve Promise"的全过程。所以：

- ✅ 函数体内**直接 return 仓颉值即可**，不要手写 `spawn`、`isInBindThread`、`postJSTask`
- ✅ ArkTS 侧 `await` 调用即可拿到结果
- ⚠️ `isInBindThread + postJSTask` 模式只在**手写 `JSModule.registerFunc` + 手动 `spawn` 新线程 + 用 JSValue 回调** 的底层场景下才需要（参见 interop-lib 多线程章节）

```cangjie
// ✅ 用宏：什么都不用管，直接写业务
@Interop[ArkTS, Async]
public func compute(x: Float64): Float64 {
    heavyWork(x)   // 宏自动 spawn + postJSTask
}

// ⚠️ 仅手写 registerFunc 才需要：
func computeRaw(ctx: JSContext, info: JSCallInfo): JSValue {
    let cb = info[1].asFunction()
    spawn {
        let r = heavyWork(...)
        ctx.postJSTask {              // 必须切回 ArkTS 线程才能 call
            cb.call(ctx.number(r).toJSValue())
        }
    }
    ctx.undefined().toJSValue()
}
```

## interface（ArkTS 创建对象传给仓颉）

interface 支持 **成员属性**（`prop` 只读 / `mut prop` 可读写）和 **成员函数**：

```cangjie
@Interop[ArkTS]
public interface InterfaceDemo {
    mut prop id: Float64
    func foo(a!: Float64): Float64
}

@Interop[ArkTS]
public func doInterface(a: InterfaceDemo): Float64 {
    return a.foo(a: a.id)
}
```

生成的 `.d.ts`（注意：成员函数生成为 **箭头函数属性**）：

```typescript
export declare interface InterfaceDemo {
    id: number
    foo: (a: number) => number
}
export declare function doInterface(a: InterfaceDemo): number
```

ArkTS 侧调用：

```typescript
import { InterfaceDemo, doInterface } from 'libohos_app_cangjie_entry.so'

let callbackInterface = (a: number): number => { return a + 1 }
let inter: InterfaceDemo = { foo: callbackInterface, id: 6 }
console.log("result " + doInterface(inter))
```

纯数据传递的简化写法（多 prop）：

```cangjie
@Interop[ArkTS]
public interface SportRecord {
    prop id: Int64
    prop distance: Float64
    prop duration: Int64
    prop date: String
}
```

> interface 用 `prop` 或 `mut prop`（不是 var/let）。`prop` 只读，`mut prop` 可写。仓颉**不能构造** interface 实例——它是 ArkTS→仓颉的单向传递协议。

## class + Invisible

`@Interop class` 中 `ArrayList`、自定义仓颉 class 等 ArkTS 无法理解的字段**必须** Invisible：

```cangjie
@Interop[ArkTS]
public class SportAnalyzer {
    @Interop[ArkTS, Invisible]
    public var records: ArrayList<SportRecordImpl> = ArrayList<SportRecordImpl>()

    @Interop[ArkTS, Invisible]
    public var fsManager: FileSystemManager = FileSystemManager.getInstance()

    public init() {}

    // 仅这些方法暴露给 ArkTS
    public func loadRecordsFromJson(jsonStr: String): Int64 { ... }
    public func analyze(): AnalysisResult { ... }
    public func getRecordCount(): Int64 { ... }
}
```

## 双向互操作类型分离（工程建议）

同一工程中 `@Interop interface`（ArkTS→仓颉协议）和从 JSObject 解析的实体类**建议分开设计**（因为 interface 无法在仓颉侧实例化，而 JSObject 解析需要可构造的类型）：

```cangjie
// ✅ @Interop interface —— ArkTS→仓颉 的传递协议
// 仓颉无法构造、无法赋值字段，只能接收
@Interop[ArkTS]
public interface SportRecord {
    prop id: Int64
    prop distance: Float64
}

// ✅ 普通 class —— 仓颉内部从 JSObject 解析后持有数据
// 可构造、可赋值、可放入集合
public class SportRecordImpl {
    public var id: Int64 = 0
    public var distance: Float64 = 0.0
}
```

| 能力 | `@Interop interface` | 普通 `class` |
|------|---------------------|-------------|
| 仓颉构造 | ❌ | ✅ `let r = SportRecordImpl()` |
| 赋值字段 | ❌ prop 只读 | ✅ `r.id = 42` |
| 放入集合 | ❌ 无法实例化 | ✅ `list.add(r)` |
| ArkTS 创建传入 | ✅ 核心用途 | ❌ 不适合 |

## 枚举

```cangjie
@Interop[ArkTS]
public enum EnumDemo {
    Red | Green | Blue
}

@Interop[ArkTS]
public func getEnum(e: EnumDemo): EnumDemo { return e }
```

生成的 `.d.ts`：

```typescript
export declare const enum EnumDemo {
    Red = 0, Green = 1, Blue = 2
}
export declare function getEnum(e: EnumDemo): EnumDemo
```

ArkTS 侧调用：

```typescript
import { EnumDemo, getEnum } from 'libohos_app_cangjie_entry.so'
let e = EnumDemo.Green   // ✅ 用导入的 enum 值，不要写 1
getEnum(e)
```

> 枚举必须 public，**不支持带参数的构造器**。

### 端到端使用约束（高频踩坑）

枚举一旦用 `@Interop` 修饰，**必须端到端贯穿使用**，禁止中途降级为数值类型：

```cangjie
// ❌ 错误：函数签名用 Int64 接收 enum，等于丢失了 enum 的语义
@Interop[ArkTS]
public func analyze(sportType: Int64): Result { ... }

// ❌ 错误：interface prop 用 Int64 承载 enum
@Interop[ArkTS]
public interface Record {
    prop sportType: Int64   // 应该是 SportType
}

// ✅ 正确：参数 / 返回值 / interface prop / class 字段都用 enum 本身
@Interop[ArkTS]
public func analyze(sportType: SportType): Result { ... }

@Interop[ArkTS]
public interface Record {
    prop sportType: SportType
}
```

```typescript
// ❌ 错误：ArkTS 侧自己重新定义 const enum，不从 .so import
const enum SportType { Running = 0, Cycling = 1 }
analyze(SportType.Running)

// ✅ 正确：从 .so import 仓颉导出的 enum
import { SportType, analyze } from 'libohos_app_cangjie_entry.so'
analyze(SportType.Running)
```

降级使用的代价：
- 失去类型安全（任意 Int64 都能传入）
- ArkTS IDE 失去枚举智能提示
- `.d.ts` 不会导出 enum 符号，ArkTS 侧只能硬编码数字

## 类型映射

| 仓颉 | ArkTS | 备注 |
|------|-------|------|
| 数值类型 | `number` | |
| `Bool` | `boolean` | |
| `String` / `JSStringEx` | `string` | |
| `Unit` | `undefined` | |
| `Option<T>` | `T \| undefined` | **不支持 `?T` 语法糖**；T 不能再是 Option 或函数；自定义 T 须被 `@Interop` 修饰 |
| `func` | `function` | |
| `JSArrayEx<T>` | `Array<T>` | T 不能是函数；自定义 T 须 `@Interop` |
| `JSHashMapEx<K,V>` | `Map<K,V>` | V 不能是函数；自定义类型须 `@Interop` |
| `Array<Byte>` | `ArrayBuffer` | |
| `enum` | `const enum` | |
| `class` / `interface` | `class` / `interface` | |

> `JSStringEx`/`JSArrayEx`/`JSHashMapEx` **只能**出现在被 `@Interop` 修饰的代码中。

## 命名冲突

- 同包内**禁止**多个 `@Interop` 导出同名符号
- `@Interop` 导出物**禁止**与 `registerModule`/`registerFunc` 注册名重名（后者会覆盖前者）

## 排障清单

1. **宏优先**：能 `@Interop` 就不要 `registerModule`
2. **包名 / .so 名 / import** 三者一致
3. **public / 无泛型 / 无默认值** 宏约束；class 成员变量须 public 且不可省略类型标注
4. **Async 禁用 JSArrayEx** → String + stdx.encoding.json（或 ArkTS 侧解析 + interface 回传）
5. **Async 函数体直接 return**，宏自动处理线程切换；不要手写 spawn/postJSTask
6. **enum 端到端**：函数参数 / interface prop / class 字段必须用 enum 本身，禁止降级为 Int64；ArkTS 侧从 .so import enum，不要本地 const enum 重定义
7. **enum 不支持带参数的构造器**
8. **类型分离**：@Interop interface ≠ JSObject 解析实体类
9. **Invisible 必加**：@Interop class 中 ArkTS 无法理解的字段必须隐藏
10. **`.d.ts` 单源原则**：同一工程的 @Interop 符号集中在单文件，避免多文件各自导出导致 .d.ts 重复声明

## 参考资料

- [互操作总入口](https://gitcode.com/openharmony/docs_cangjie/tree/master/zh-cn/application-dev/learn-cj/FFI/cangjie-arkts)
- 声明式互操作宏：`cj-arkts_interoperability_macro/仓颉-ArkTS_声明式互操作宏/`
- 宏使用方法（含 Generate 流程）：`使用方法/使用方法_2more.md`
- 场景详细说明：`场景详细说明/场景详细说明_4more.md`
- 类型映射表：`类型映射.md`
