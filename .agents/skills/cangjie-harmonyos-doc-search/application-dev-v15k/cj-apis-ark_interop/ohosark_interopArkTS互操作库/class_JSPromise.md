## class JSPromise

```cangjie
public class JSPromise <: JSHeapObject {}
```

**功能：** 一个回调机制的封装对象。

JSPromise的目标是为回调形式的一致性封装，配合 async、await 的语法糖大大增强其易用性。

JSPromise的生命周期超过引用的 ArkTS 对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**父类型：**

* [JSHeapObject](#class-jsheapobject)

### func catchError(JSFunction)

```cangjie
public func catchError(callback: JSFunction): Unit
```

**功能：** 注册异常处理回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|[JSFunction](#class-jsfunction)|是|-|异常处理回调。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let promise = callInfo[0].asPromise(context)
    let onError: JSLambda = {
        context, callInfo => context.undefined().toJSValue()
    }
    promise.catchError(context.function(onError))
    context.undefined().toJSValue()
}
```

### func then(JSFunction, ?JSFunction)

```cangjie
public func then(onFulfilled: JSFunction, onRejected!: ?JSFunction = None): Unit
```

**功能：** 注册结果处理回调。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|onFulfilled|[JSFunction](#class-jsfunction)|是|-|结果处理回调。|
|onRejected|?[JSFunction](#class-jsfunction)|否|None| **命名参数。** 异常处理回调。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let promise = callInfo[0].asPromise(context)
    let onFulfilled: JSLambda = {
        context, callInfo => context.undefined().toJSValue()
    }
    promise.then(context.function(onFulfilled))
    context.undefined().toJSValue()
}
```