### func toFloat32ArrayJSValue()

```cangjie
public func toFloat32ArrayJSValue(): JSValue
```

**功能：** 返回 ArkTS 的 Float32Array 的 JSValue。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#class-jsvalue)|ArkTS统一类型。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300002   | Outside error occurred.　             |
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch. 　                   |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func convertToFloat32Array(context: JSContext, callInfo: JSCallInfo): JSValue {
    let arrayBuffer = callInfo[0].asArrayBuffer()
    let float32Array = arrayBuffer.toFloat32Array()
    Hilog.info(0, "test","Converted to Float32Array with ${float32Array.size} elements")
    return context.number(Float64(float32Array.size)).toJSValue()
}
```

### func toFloat64Array()

```cangjie
public func toFloat64Array(): Array<Float64>
```

**功能：** 转换为仓颉数组 Array\<Float64>。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Float64>|仓颉数组。|

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
import ohos.hilog.Hilog

func convertToFloat64Array(context: JSContext, callInfo: JSCallInfo): JSValue {
    let arrayBuffer = callInfo[0].asArrayBuffer()
    let float64Array = arrayBuffer.toFloat64Array()
    Hilog.info(0, "test","Converted to Float64Array with ${float64Array.size} elements")
    return context.number(Float64(float64Array.size)).toJSValue()
}
```

### func toFloat64ArrayJSValue()

```cangjie
public func toFloat64ArrayJSValue(): JSValue
```

**功能：** 返回 ArkTS 的 Float64Array 的 JSValue。

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
func getFloat64ArrayJSValue(context: JSContext, callInfo: JSCallInfo): JSValue {
    let arrayBuffer = callInfo[0].asArrayBuffer()
    let float64ArrayJSValue = arrayBuffer.toFloat64ArrayJSValue()
    return float64ArrayJSValue
}
```

### func toInt16Array()

```cangjie
public func toInt16Array(): Array<Int16>
```

**功能：** 转换为仓颉数组 Array\<Int16>。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Int16>|仓颉数组。|

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

func convertToInt16Array(context: JSContext, callInfo: JSCallInfo): JSValue {
    let arrayBuffer = callInfo[0].asArrayBuffer()
    let int16Array = arrayBuffer.toInt16Array()
    Hilog.info(0, "test","Converted to Int16Array with ${int16Array.size} elements")
    return context.number(Float64(int16Array.size)).toJSValue()
}
```