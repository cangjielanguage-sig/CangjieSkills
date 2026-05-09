## class JSContext

```cangjie
public class JSContext {}
```

**功能：** 一个单线程执行的 ArkTS 互操作上下文。

JSContext和ArkTS运行时是一一对应的关系，其主要目标是创建JSValue和安全引用、管理ArkTS侧引用的仓颉对象的生命周期。

一个JSContext持有一个ArkTS运行时的弱引用，这个JSContext不会影响ArkTS运行时的生命周期，当ArkTS运行时失效后使用这个JSContext会抛出仓颉异常。

**起始版本：** 22

### prop env

```cangjie
public prop env: JSEnv
```

**功能：** ArkTS 互操作上下文。

**起始版本：** 22

**类型：** JSEnv

**读写能力：** 只读

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

func accessContextEnv(context: JSContext): JSValue {
    let env = context.env
    Hilog.info(0, "test", "Context env accessed")

    return context.undefined().toJSValue()
}
```

### prop global

```cangjie
public prop global: JSObject
```

**功能：** js全局环境变量 globalThis。

**起始版本：** 22

**类型：** [JSObject](#class-jsobject)

**读写能力：** 只读

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

func accessGlobalObject(context: JSContext): JSValue {
    let globalObj = context.global
    let globalKeys = globalObj.keys()

    Hilog.info(0, "test", "Global object has ${globalKeys.size} keys")

    return globalObj.toJSValue()
}
```

### func array(Array\<JSValue>)

```cangjie
public func array(arr: Array<JSValue>): JSArray
```

**功能：** 创建一个 ArkTS 数组。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|arr|Array\<[JSValue](#class-jsvalue)>|是|-|ArkTS 数组的引用。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSArray](#class-jsarray)|ArkTS 数组|

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
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let result = context.array([])
    return result.toJSValue()
}
```

### func arrayBuffer(Int32)

```cangjie
public func arrayBuffer(length: Int32): JSArrayBuffer
```

**功能：** 通过内存块创建一个 ArkTS ArrayBuffer。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|length|Int32|是|-|内存块大小。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSArrayBuffer](#class-jsarraybuffer)|ArkTS ArrayBuffer 对象的引用。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 1     | The arrayBuffer length is invalid.          |
| 34300002   | Outside error occurred.                |
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

**示例：**

<!--compile-->
```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let result = context.arrayBuffer(Int32(10))
    return result.toJSValue()
}
```