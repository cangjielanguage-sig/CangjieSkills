## 场景详细说明

声明式互操作宏可修饰范围包括函数（含异步函数）、接口、类和枚举，针对不同的场景使用建议如下表：

| 适用场景                          | 使用类型  | 修饰                                                                                       |
| :-------------------------------- | :-------- | :----------------------------------------------------------------------------------------- |
| ArkTS 调用仓颉函数                | 函数      | @Interop[ArkTS]                                                                            |
| ArkTS 调用耗时仓颉函数            | 异步函数  | @Interop[ArkTS, Async]                                                                     |
| 用于传递 ArkTS 侧创建的对象给仓颉 | interface | @Interop[ArkTS]                                                                            |
| 用于返回仓颉侧创建的对象给 ArkTS  | class     | @Interop[ArkTS] 修饰整个 class<br>@Interop[ArkTS, Invisible] 修饰 class 中不准备暴露的成员 |
| 用于仓颉和 ArkTS 互相传递枚举数据 | enum      | @Interop[ArkTS]                                                                            |

### 函数

对于声明式互操作宏修饰的函数，必须满足以下条件，不满足时将会编译报错：

- 必须由 public 修饰
- 不支持类型参数
- 支持命名参数，但 ArkTS 调用方法和非命名参数一致
- 不支持默认值

函数互操作使用示例请参见[使用方法](#使用方法)。

### 异步函数

对于声明式互操作宏修饰的异步函数，必须满足以下条件，不满足时将会编译报错：

- 必须由 public 修饰
- 不支持类型参数
- 支持命名参数，但 ArkTS 调用方法和非命名参数一致
- 不支持默认值
- `JSStringEx`、`JSArrayEx<T>` 和 `JSHashMapEx<K, V>` 三种类型不能在异步函数中使用

异步函数互操作使用示例：

<!--compile-->
```cangjie
// 仓颉侧创建互操作函数
package ohos_app_cangjie_entry

import ohos.ark_interop.*
import ohos.ark_interop_macro.*

@Interop[ArkTS, Async]
public func doAsync(a: Float64, b: Float64): Float64 {
    a + b
}
```

自动生成的 ArkTS 接口：

```typescript
// Generate... > Cangjie-ArkTS Interop API 后自动生成 .d.ts
export declare function doAsync(a: number, b: number): Promise<number>
```

ArkTS 侧对于仓颉模块的调用：

```typescript
// 导入仓颉动态库，该动态库名称为仓颉包名的名称，该名称需要和互操作接口所在的包名一致
import { doAsync } from "libohos_app_cangjie_entry.so";

doAsync(1, 2).then(result => {
    console.log("result " + result);
});
```

### 接口

对于声明式互操作宏修饰的接口，必须满足以下条件，不满足时将会编译报错：

- 必须由 public 修饰
- 不支持类型参数
- 不支持继承其他接口
- 支持不带修饰符的成员函数，其他和函数限制一致
- 不支持操作符重载
- 支持成员属性，支持 mut 修饰符

接口互操作使用示例：

<!--compile-->
```cangjie
// 仓颉侧创建互操作函数
package ohos_app_cangjie_entry

import ohos.ark_interop.*
import ohos.ark_interop_macro.*

@Interop[ArkTS]
public interface InterfaceDemo {
    mut prop id: Float64
    func foo(a!: Float64): Float64
}

@Interop[ArkTS]
public func doInterface(a: InterfaceDemo): Float64  {
    return a.foo(a: a.id)
}
```

自动生成的 ArkTS 接口：

```typescript
// Generate... > Cangjie-ArkTS Interop API 后自动生成 .d.ts
export declare interface InterfaceDemo {
    id: number
    foo: (a: number) => number
}

export declare function doInterface(a: InterfaceDemo): number
```

ArkTS 侧对于仓颉模块的调用：

```typescript
// 导入仓颉动态库，该动态库名称为仓颉包名的名称，该名称需要和互操作接口所在的包名一致
import { InterfaceDemo, doInterface } from "libohos_app_cangjie_entry.so";

let callbackInterface = (a: number): number => {
  return a + 1;
}
let inter: InterfaceDemo = {foo: callbackInterface, id: 6};
console.log("result " + doInterface(inter));
```