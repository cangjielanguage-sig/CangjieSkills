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

> 异步互操作优先 `@Interop[ArkTS, Async]`，避免手写 Promise 胶水。多线程禁止跨线程触摸同一 `JSContext`。需要跨语言锁时查阅 `AsyncLock`、`Sendable` 专题文档。

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

> 枚举必须 public，**不支持带参数的构造器**。

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
4. **Async 禁用 JSArrayEx** → String + stdx.encoding.json
5. **enum 不支持带参数的构造器**
6. **类型分离**：@Interop interface ≠ JSObject 解析实体类
7. **Invisible 必加**：@Interop class 中 ArkTS 无法理解的字段必须隐藏

## 参考资料

- [互操作总入口](https://gitcode.com/openharmony/docs_cangjie/tree/master/zh-cn/application-dev/learn-cj/FFI/cangjie-arkts)
- 声明式互操作宏：`cj-arkts_interoperability_macro/仓颉-ArkTS_声明式互操作宏/`
- 宏使用方法（含 Generate 流程）：`使用方法/使用方法_2more.md`
- 场景详细说明：`场景详细说明/场景详细说明_4more.md`
- 类型映射表：`类型映射.md`
