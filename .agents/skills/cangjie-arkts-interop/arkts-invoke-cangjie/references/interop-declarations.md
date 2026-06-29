# 互操作声明

仓颉-ArkTS 互操作的声明文件创建、类型映射、声明同步和验证方法。

## 声明文件创建

### 创建 types 声明目录

创建目录：`<module>/src/main/cangjie/types/lib<module>/`

**types/lib<module>/Index.d.ts**：

```typescript
/**
 * Type declarations for lib<module>.so
 * Cangjie-ArkTS interop bridge
 */

/**
 * <Feature> class
 * 根据 `bridge/<Feature>.cj` 中的实际方法定义类型
 */
export declare class <Feature> {
    /**
     * Constructor
     */
    constructor();

    /**
     * Example method
     */
    exampleMethod(param: string): string;

    // 根据实际的 .cj 文件添加其他方法声明...
}

/**
 * CustomLib interface for requireCJLib
 * 必须定义在 .d.ts 文件中（不是 .ets）以避免 ArkTS 严格模式限制
 */
export declare interface CustomLib {
    <Feature>: { new (): <Feature> };
}
```

**types/lib<module>/oh-package.json5**：

```json5
{
  "name": "lib<module>.so",
  "types": "./Index.d.ts",
  "version": "1.0.0",
  "description": "<Feature> Cangjie-ArkTS interop type declarations"
}
```

### 创建 loader 声明目录

创建目录：`<module>/src/main/cangjie/loader/`

**loader/Index.d.ts**：

```typescript
/**
 * Type declarations for libark_interop_loader.so
 * System library provided by HarmonyOS SDK
 */

/**
 * Load a Cangjie shared library
 * @param libName Library name (e.g., "lib<module>.so")
 * @returns The loaded library object
 */
export declare function requireCJLib(libName: string): ESObject;
```

**loader/oh-package.json5**：

```json5
{
  "name": "libark_interop_loader.so",
  "types": "./Index.d.ts",
  "version": "1.0.0",
  "description": "HarmonyOS Cangjie-ArkTS interop loader"
}
```

## 类型声明规范

```typescript
// ✅ 正确 - 使用 export declare
export declare class MyBridge {
    constructor();
    myMethod(param: string): string;
}

export declare interface CustomLib {
    MyBridge: { new (): MyBridge };
}

// ❌ 错误 - 不要使用 export class
export class MyBridge {  // 会导致 Duplicate identifier
    constructor();
}
```

规则要点：

- 必须使用 `export declare class`（不是 `export class`）
- `CustomLib` 必须在 `.d.ts` 中（见 [cangjie-bridge-rules.md#arkts-构造签名限制](cangjie-bridge-rules.md#arkts-构造签名限制)）
- 文件命名为 `Index.d.ts`（不是 `Index.d.ets`）
- `oh-package.json5` 的 name 与 `.so` 一致
- 不允许同名类重复声明

## 类型映射表

| 仓颉类型 | TypeScript 类型 | 说明 |
|---------|----------------|------|
| `Unit` | `undefined` | - |
| `String`、`JSStringEx` | `string` | 字符串 |
| `Int8`、`Int16`、`Int32`、`Int64` | `number` | 整数 |
| `UInt8`、`UInt16`、`UInt32`、`UInt64` | `number` | 整数 |
| `Float16`、`Float32`、`Float64` | `number` | 浮点数 |
| `Bool` | `boolean` | 布尔值 |
| `Option<T>` | `T \| undefined` | T 不支持 Option<T> 类型和函数类型，如果 T 为自定义类型（class 或 interface 类型），该自定义类型必须被 Interop 宏修饰 |
| `JSArrayEx<T>` | `Array<T>` | 数组（`T` 不能是函数，需递归映射元素类型） |
| `JSHashMapEx<K, V>` | `Map<K, V>` | 映射（`V` 不能是函数） |
| `Array<Byte>` | `ArrayBuffer` | 字节数组 |
| `func` | `function` | 函数类型 |
| `class` / `interface` | `class` / `interface` | 自定义类型（也需被 `@Interop` 修饰） |

`JSStringEx`、`JSArrayEx<T>`、`JSHashMapEx<K, V>` 只能出现在被 `Interop` 修饰的函数、class、interface 中。跨边界使用自定义类型时，自定义类型也要被 `Interop` 修饰。

翻译仓颉 `interface` 时，若原签名出现普通集合类型，先在仓颉互操作边界改成互操作集合类型，再生成声明：`HashMap<K, V>` → `JSHashMapEx<K, V>` → `Map<K, V>`，`Array<T>` → `JSArrayEx<T>` → `Array<T>`。不要在声明里暴露一个与原 interface 不同名的额外 wrapper 类型。

## 类型同步

类型声明必须与仓颉桥接类保持一致。

**示例**：

仓颉侧（bridge/Feature.cj）：
```cj
@Interop[ArkTS]
public class Feature {
    public init() { }

    public func doAction(name: String): Unit { }

    public func getStatus(): Int64 { }

    public func isEnabled(): Bool { }
}
```

TypeScript 侧（types/lib<module>/Index.d.ts）：
```typescript
export declare class Feature {
    constructor();  // 对应 init()

    doAction(name: string): undefined;  // 对应 doAction(String): Unit

    getStatus(): number;  // 对应 getStatus(): Int64

    isEnabled(): boolean;  // 对应 isEnabled(): Bool
}
```

## 增量更新类型声明

当仓颉桥接类添加新方法时：

1. 在 `bridge/<Feature>.cj` 中添加方法（带 `@Interop[ArkTS]`）
2. 在 `types/lib<module>/Index.d.ts` 中添加对应的类型声明
3. 重新构建项目

不需要删除或重新生成整个目录，只需增量更新即可。

**示例**：

```typescript
// 添加前
export declare class Feature {
    constructor();
    doAction(name: string): undefined;
}

// 添加新方法后
export declare class Feature {
    constructor();
    doAction(name: string): undefined;
    reset(): undefined;  // 新增方法
    refresh(): undefined;  // 新增方法
}
```

## 验证类型一致性

确保类型声明与仓颉实现一致：

1. **方法名一致**：TypeScript 中的 `myMethod` 对应仓颉中的 `myMethod`
2. **参数类型一致**：仓颉 `String` 必须映射为 TypeScript `string`
3. **返回类型一致**：仓颉 `Unit` 必须映射为 TypeScript `undefined`
4. **参数数量一致**：TypeScript 声明的参数数量必须与仓颉方法一致

**不一致的后果**：
- 编译可能通过，但运行时会出现类型错误或调用失败
- ArkTS 调用时传递的参数可能无法正确传递给仓颉
- 返回值可能无法正确转换

使用验证脚本检查一致性：`python scripts/verify_interop_structure.py --module <module> --check-types`
