### 操作 ArkTS 的普通对象

从一个互操作函数的实现举例:

1. 仓颉函数实现：

    <!--compile-->
    ```cangjie
    // 定义包名，该包名需要和 cjpm.toml 的 package name 保持一致
    package ohos_app_cangjie_entry

    // 导入互操作库ark_interop和互操作宏
    import ohos.ark_interop.*

    // 互操作函数定义，该函数参数类型必须为(JSContext，JSCallInfo),返回值类型必须为JSValue
    func addByObject(context: JSContext, callInfo: JSCallInfo): JSValue {
        // callInfo中记录的为函数调用的参数。如下为获取首个参数：
        let arg0 = callInfo[0]
        // 校验参数0是否是对象，否则返回undefined
        if (!arg0.isObject()) {
            return context.undefined().toJSValue()
        }
        // 把JSValue转换为Float64
        let a = arg0.asObject()["a"].toNumber()
        let b = arg0.asObject()["b"].toNumber()

        let result = a + b
        return context.number(result).toJSValue()
    }

    // 必须注册该函数到JSModule中
    let EXPORT_MODULE = JSModule.registerModule {
        runtime, exports =>
            exports["addByObject"] = runtime.function(addByObject).toJSValue()
    }
    ```

2. 互操作接口声明：

    ```typescript
    // libohos_app_cangjie_entry.so 对应的Index.d.ts
    export declare interface CustomObject {
        a: number;
        b: number;
    }
    // 定义的仓颉互操作函数，名称与仓颉侧注册名称一致
    export declare function addByObject(args: CustomObject): number;
    ```

3. ArkTS 调用函数：

    ```typescript
    // 导入仓颉动态库，该动态库名称为仓颉包名的名称，该名称需要和互操作接口所在的包名一致
    import { addByObject } from "libohos_app_cangjie_entry.so";

    // 调用仓颉接口
    let result = addByObject({a: 1, b: 2});
    console.log("result = " + result);
    ```

除了可以从对象上读取属性外，还可以对属性赋值或创建新属性，操作方式为 `JSObject[key] = value`，其中 key 可以是仓颉 String 、JSString 或 JSSymbol 类型，value 是 JSValue 类型 。

> **说明：**
>
> 通过 `JSObject[key] = value` 定义属性时，该属性可写、可枚举、可配置。
> 更多参见 [JavaScript 标准内置对象](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object)。

**值得注意的是：**

1. 对属性赋值在以下几种场景会失败，失败之后没有异常或日志：

   1. 目标对象是 sealed 对象，由 `Object.seal()` 接口创建的对象具有不可修改的特性，无法创建新的属性和修改原有属性。
   2. 目标属性的 writable 是 false ，由 `Object.defineProperty(object, key, {writable: false, value: xxx})` 定义属性时，可以指定属性是否可写。

2. 对于一个未知对象，可以枚举出该对象的可枚举属性：

   <!--compile-->
   ```cangjie
   func handleUnknownObject(context: JSContext, target: JSObject): Unit {
       // keys接口枚举对象的可枚举属性
       let keys = target.keys()
       println("target keys: ${keys}")
   }
   ```

3. 创建一个新的 ArkTS 对象，可以通过 `JSContext.object()` 来创建。

4. 对于 ArkTS 运行时，有一个特殊的 ArkTS 全局对象，在任何 ArkTS 代码里都可以直接访问该对象下的属性，在仓颉侧可以通过 `JSContext.global` 来访问。