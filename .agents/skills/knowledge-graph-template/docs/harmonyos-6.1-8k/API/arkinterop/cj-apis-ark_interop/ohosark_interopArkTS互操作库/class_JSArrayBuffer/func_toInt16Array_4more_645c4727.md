### func toInt16ArrayJSValue()

```cangjie
public func toInt16ArrayJSValue(): JSValue
```

**功能：** 返回 ArkTS 的 Int16Array 的 JSValue。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#class-jsvalue)|ArkTS统一类型。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息 |
|:------| :--- |
| 34300002   | Outside error occurred. |
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch. |

**示例：**

<!--compile-->
```cangjie
func getInt16ArrayJSValue(context: JSContext, callInfo: JSCallInfo): JSValue {
    let arrayBuffer = callInfo[0].asArrayBuffer()
    let int16ArrayJSValue = arrayBuffer.toInt16ArrayJSValue()
    return int16ArrayJSValue
}
```

### func toInt32Array()

```cangjie
public func toInt32Array(): Array<Int32>
```

**功能：** 转换为仓颉数组 Array\<Int32>。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Int32>|仓颉数组。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                     |
|:------|:-----------------------------------------|
| 34300002   | Outside error occurred.　             |
| 34300003   | Accessing reference is beyond reach.     |
| 34300004   | Thread mismatch.                         |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func convertToInt32Array(context: JSContext, callInfo: JSCallInfo): JSValue {
    let arrayBuffer = callInfo[0].asArrayBuffer()
    let int32Array = arrayBuffer.toInt32Array()
    Hilog.info(0, "test", "Converted to Int32Array with ${int32Array.size} elements")
    return context.number(Float64(int32Array.size)).toJSValue()
}
```

### func toInt32ArrayJSValue()

```cangjie
public func toInt32ArrayJSValue(): JSValue
```

**功能：** 返回 ArkTS 的 Int32Array 的 JSValue。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#class-jsvalue)|ArkTS统一类型。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息 |
|:------| :--- |
| 34300002   | Outside error occurred. |
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch. |

**示例：**

<!--compile-->
```cangjie
func getInt32ArrayJSValue(context: JSContext, callInfo: JSCallInfo): JSValue {
    let arrayBuffer = callInfo[0].asArrayBuffer()
    let int32ArrayJSValue = arrayBuffer.toInt32ArrayJSValue()
    return int32ArrayJSValue
}
```

### func toInt64Array()

```cangjie
public func toInt64Array(): Array<Int64>
```

**功能：** 转换为仓颉数组 Array\<Int64>。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Int64>|仓颉数组。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                     |
|:------|:-----------------------------------------|
| 34300002   | Outside error occurred.　             |
| 34300003   | Accessing reference is beyond reach.     |
| 34300004   | Thread mismatch.                         |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func convertToInt64Array(context: JSContext, callInfo: JSCallInfo): JSValue {
    let arrayBuffer = callInfo[0].asArrayBuffer()
    let int64Array = arrayBuffer.toInt64Array()
    Hilog.info(0, "test", "Converted to Int64Array with ${int64Array.size} elements")
    return context.number(Float64(int64Array.size)).toJSValue()
}
```