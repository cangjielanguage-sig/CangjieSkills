### 调用 ArkTS 函数

#### 普通函数调用

获取一个 ArkTS 函数后（通过参数传递，全局变量传递，从 ArkTS 数据集合里获取如从数组通过索引获取元素），可以在仓颉里直接调用。
该示例是先从 ArkTS 调用仓颉函数，然后在仓颉函数的实现里回调 ArkTS 函数。

1. ArkTS 调用仓颉：

    ```typescript
    // libohos_app_cangjie_entry.so对应的Index.d.ts
    export declare function addByCallback(a: number, b: number, callback: (result: number) => void): void;
    ```

    ```typescript
    // 1.导入仓颉动态库，该动态库名称为仓颉包名的名称，该名称需要和互操作接口所在的包名一致
    import { addByCallback } from "libohos_app_cangjie_entry.so";

    // 2.调用仓颉接口
    addByCallback(1, 2, (result) => {
        console.log(`1 + 2 = ${result}`);
    });
    ```

2. 仓颉代码中回调 ArkTS 函数：

    <!--compile-->
    ```cangjie
    package ohos_app_cangjie_entry

    internal import ohos.ark_interop.JSModule
    internal import ohos.ark_interop.JSContext
    internal import ohos.ark_interop.JSCallInfo
    internal import ohos.ark_interop.JSValue

    func addByCallback(context: JSContext, callInfo: JSCallInfo): JSValue {
        // 获取第1、2个参数，并转换为Float64
        let a = callInfo[0].toNumber()
        let b = callInfo[1].toNumber()
        // 把第3个参数转换为JSFunction
        let callback = callInfo[2].asFunction()
        // 计算结果
        let result = a + b
        // 从仓颉Float64创建ArkTS number
        let retJSValue = context.number(result).toJSValue()
        // 调用回调函数
        callback.call(retJSValue)
    }

    let EXPORT_MODULE = JSModule.registerModule {
        runtime, exports =>
            exports["addByCallback"] = runtime.function(addByCallback).toJSValue()
    }
    ```

#### 带 this 指针的函数调用

这个用例里的函数是不带 this 指针的，针对需要 this 指针的方法调用，可以通过命名参数 `thisArg` 来指定。

<!--compile-->
```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let callback = callInfo[0].asFunction()
    let thisArg = callInfo[1]

    callback.call(thisArg: thisArg)
}
```

在 ArkTS 代码里，可以通过 `对象.方法(...)` 来进行调用，这时会隐式传递 this 指针。

```typescript
class Someone {
    id: number = 0;
    doSth(): void {
        console.log(`someone ${this.id} have done something`);
    }
}

let target = new Someone();

// 这里会隐式传递this指针，调用正常
target.doSth();

let doSth = target.doSth;
// 这里没有传递this指针，会出现异常`can't read property of undefined`
doSth.call();
```

在仓颉里，对应的写法如下：

<!--compile.error-->
```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let object = callInfo[0].asObject()
    // 会隐式传递this指针，调用正常
    object.callMethod("doSth")

    let doSth = object["doSth"].asFunction()
    // 未传递this指针，会出现异常`can't read property of undefined`
    doSth.call()
    // 显式传递this指针，调用正常
    doSth.call(thisArg: object.toJSValue())
}
```