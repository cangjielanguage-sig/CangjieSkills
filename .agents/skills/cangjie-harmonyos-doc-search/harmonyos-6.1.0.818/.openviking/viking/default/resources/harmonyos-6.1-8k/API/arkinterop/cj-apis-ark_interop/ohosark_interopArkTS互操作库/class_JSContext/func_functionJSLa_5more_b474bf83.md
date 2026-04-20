### func function(JSLambda)

```cangjie
public func function(lambda: JSLambda): JSFunction
```

**功能：** 创建一个 ArkTS 函数。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|lambda|[JSLambda](#type-jslambda)|是|-|仓颉函数。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSFunction](#class-jsfunction)|ArkTS function 的引用。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300002   | Outside error occurred.                |
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

**示例：**

<!--compile-->
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

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[napi_env](#type-napi_env)|全局环境的指针。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func getNapiEnvironment(context: JSContext): JSValue {
    let napiEnv = context.getNapiEnv()
    Hilog.info(0, "test", "Got napi environment")

    return context.undefined().toJSValue()
}
```

### func isInBindThread()

```cangjie
public func isInBindThread(): Bool
```

**功能：** 多线程工具：检查当前线程是否可执行互操作接口。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时当前线程可以调用互操作接口|

**示例：**

<!--compile-->
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

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[JSNull](#class-jsnull)|返回 ArkTS null。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

**示例：**

<!--compile-->
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

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float64|是|-|仓颉Int32数。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSNumber](#class-jsnumber)|ArkTS number。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

**示例：**

<!--compile-->
```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let result = context.number(1.0)
    return result.toJSValue()
}
```