### func external(SharedObject)

```cangjie
public func external(data: SharedObject): JSExternal
```

**功能：** 创建一个 ArkTS 对仓颉对象的引用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|data|[SharedObject](#class-sharedobject)|是|-|原始仓颉对象。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSExternal](#class-jsexternal)|ArkTS 对仓颉对象的引用。|

**示例：**

```cangjie
class Data <: SharedObject {}

func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let data = Data()
    let result = context.external(data)
    return result.toJSValue()
}
```

### func function(JSLambda)

```cangjie
public func function(lambda: JSLambda): JSFunction
```

**功能：** 创建一个 ArkTS 函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|lambda|[JSLambda](#type-jslambda)|是|-|仓颉函数。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSFunction](#class-jsfunction)|ArkTS function 的引用。|

**示例：**

```cangjie
func jsCallback(context: JSContext, callInfo: JSCallInfo): JSValue {
    return context.undefined().toJSValue()
}

func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let result = context.function(jsCallback)
    return result.toJSValue()
}
```

### func getNapiEnv()

```cangjie
public func getNapiEnv(): napi_env
```

**功能：** 获取一个全局环境的指针。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 14

**返回值：**

|类型|说明|
|:----|:----|
|[napi_env](#type-napi_env)|全局环境的指针。|

### func isInBindThread()

```cangjie
public func isInBindThread(): Bool
```

**功能：** 多线程工具：检查当前线程是否可执行互操作接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时当前线程可以调用互操作接口|

**示例：**

```cangjie
func createObject(context: JSContext): JSObject {
    if (!context.isInBindThread()) {
        throw Exception("not able to call arkts on current thread")
    }
    return context.object()
}
```

### func null()

```cangjie
public func null(): JSNull
```

**功能：** 创建一个 ArkTS null。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|[JSNull](#struct-jsnull)|返回 ArkTS null。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let result = context.null()
    return result.toJSValue()
}
```

### func number(Float64)

```cangjie
public func number(value: Float64): JSNumber
```

**功能：** 创建一个 ArkTS number。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float64|是|-|仓颉Int32数。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSNumber](#struct-jsnumber)|ArkTS number。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let result = context.number(1.0)
    return result.toJSValue()
}
```

### func number(Int32)

```cangjie
public func number(value: Int32): JSNumber
```

**功能：** 创建一个 ArkTS number。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int32|是|-|仓颉Int32数。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSNumber](#struct-jsnumber)|ArkTS number。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let result = context.number(Int32(10))
    return result.toJSValue()
}
```