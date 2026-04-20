## class JSPromiseCapability

```cangjie
public class JSPromiseCapability {
}
```

**功能：** JSPromiseCapability 对应一个 Promise 对象，可以通过它来 resolve 和 reject 该 Promise。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

生命周期：JSPromiseCapability是一个弱引用，对应ArkTS对象的生命周期在首次 resolve 或 reject 时结束，结束后继续使用会抛出仓颉异常。

### func reject(JSValue)

```cangjie
public func reject(value: JSValue): Unit
```

**功能：** 向 Promise 提交异常。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[JSValue](#struct-jsvalue)|是|-|异常数据，一般是 Error 对象或 string。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let promise = context.promiseCapability()
    // toJSValue 需要在 reject 前，在 reject 之后该对象将不可访问
    let result = promise.toJSValue()
    promise.reject(context.string("a exception occured").toJSValue())
    return result
}
```

### func resolve(JSValue)

```cangjie
public func resolve(value: JSValue): Unit
```

**功能：** 通知 Promise 正常结束并提交返回值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[JSValue](#struct-jsvalue)|是|-|处理结果。|

**示例：**

```cangjie
func addNumberAsync(context: JSContext, callInfo: JSCallInfo): JSValue {
    let a = callInfo[0].toNumber()
    let b = callInfo[1].toNumber()
    let promise = context.promiseCapability()
    // toJSValue 需要在 resolve 前，在 resolve 之后该对象将不可访问
    let result = promise.toJSValue()
    promise.resolve(context.number(a + b).toJSValue())
    return result
}
```

### func toJSValue()

```cangjie
public func toJSValue(): JSValue
```

**功能：** 转换为 ArkTS 统一类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#struct-jsvalue)|ArkTS统一类型。|

**示例：**

```cangjie
func addNumberAsync(context: JSContext, callInfo: JSCallInfo): JSValue {
    // 把 ArkTS 入参转换为仓颉类型
    let a = callInfo[0].toNumber()
    let b = callInfo[1].toNumber()
    // 创建 PromiseCapability
    let promise = context.promiseCapability()
    spawn {
        // 使用新线程来执行运算密集的任务
        let result = a + b
        // 回到 ArkTS 线程
        context.postJSTask {
            // 向 ArkTS 返回结果
            promise.resolve(context.number(result).toJSValue())
        }
    }
    // 返回 Promise
    promise.toJSValue()
}
```