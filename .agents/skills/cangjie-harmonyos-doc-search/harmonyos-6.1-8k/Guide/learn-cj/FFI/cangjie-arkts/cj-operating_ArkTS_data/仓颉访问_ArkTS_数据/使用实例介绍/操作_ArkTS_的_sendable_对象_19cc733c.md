### 操作 ArkTS 的 sendable 对象

ArkTS 提供了 sendable 对象类型，在并发通信时支持通过引用传递来解决大量对象并发通信的诉求。

仓颉侧操作 sendable 对象和普通的 ArkTS 对象是一致的。

在 ArkTS 侧定义一个 sendable 对象：

```typescript
// 函数定义
@Sendable
class SendableTestClass {
  desc: string = "sendable: this is SendableTestClass ";
  num1: number = 5;
  num2: number = 5;
  printName() {
    console.info("sendable: SendableTestClass desc is: " + this.desc);
  }
  get getNum(): number {
    return this.num1;
  }
}
```

在仓颉侧操作 sendable 对象：

<!--compile-->
```cangjie
// 定义包名，该包名需要和 cjpm.toml 的 package name 保持一致
package ohos_app_cangjie_entry

// 导入互操作库ark_interop和互操作宏
import ohos.ark_interop.*

// 互操作函数定义，该函数参数类型必须为(JSContext，JSCallInfo),返回值类型必须为JSValue
func readNumber(context: JSContext, callInfo: JSCallInfo): JSValue {
    let obj = callInfo[0].asObject()
    // 从JSObject获取属性
    let argA = obj["num1"]
    let argB = obj["num2"]
    // 把JSValue转换为Float64
    let a = argA.toNumber()
    let b = argB.toNumber()

    let result = a + b
    return context.number(result).toJSValue()
}

// 必须注册该函数到JSModule中
let EXPORT_MODULE = JSModule.registerModule {
    runtime, exports =>
        exports["readNumber"] = runtime.function(readNumber).toJSValue()
}
```

在 Index.d.ts 文件中，提供互操作的接口声明：

```typescript
// libohos_app_cangjie_entry.so 对应的 Index.d.ts
export declare function readNumber(data: SendableTestClass): number;

interface SendableTestClass {}
```

在 ArkTS 侧构建 sendable 对象：

```typescript
// 导入仓颉动态库，该动态库名称为仓颉包名的名称，该名称需要和互操作接口所在的包名一致
import { readNumber } from "libohos_app_cangjie_entry.so"

// 构建 sendable 对象
let a = new SendableTestClass();
// 调用仓颉接口
let result = readNumber(a);
console.log("result = " + result);
```