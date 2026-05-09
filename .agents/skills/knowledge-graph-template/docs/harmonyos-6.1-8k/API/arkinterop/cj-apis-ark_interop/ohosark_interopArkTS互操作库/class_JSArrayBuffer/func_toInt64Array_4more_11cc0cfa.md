### func toInt64ArrayJSValue()

```cangjie
public func toInt64ArrayJSValue(): JSValue
```

**功能：** 返回 ArkTS 的 BigInt64Array 的 JSValue。

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
func getInt64ArrayJSValue(context: JSContext, callInfo: JSCallInfo): JSValue {
    let arrayBuffer = callInfo[0].asArrayBuffer()
    let int64ArrayJSValue = arrayBuffer.toInt64ArrayJSValue()
    return int64ArrayJSValue
}
```

### func toInt8Array()

```cangjie
public func toInt8Array(): Array<Int8>
```

**功能：** 转换为仓颉数组 Array\<Int8>。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Int8>|仓颉数组。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                     |
|:------|:-----------------------------------------|
| 34300003   | Accessing reference is beyond reach.     |
| 34300004   | Thread mismatch.                         |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func convertToInt8Array(context: JSContext, callInfo: JSCallInfo): JSValue {
    let arrayBuffer = callInfo[0].asArrayBuffer()
    let int8Array = arrayBuffer.toInt8Array()
    Hilog.info(0, "test", "Converted to Int8Array with ${int8Array.size} elements")
    return context.number(Float64(int8Array.size)).toJSValue()
}
```

### func toInt8ArrayJSValue()

```cangjie
public func toInt8ArrayJSValue(): JSValue
```

**功能：** 返回 ArkTS 的 Int8Array 的 JSValue。

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
func getInt8ArrayJSValue(context: JSContext, callInfo: JSCallInfo): JSValue {
    let arrayBuffer = callInfo[0].asArrayBuffer()
    let int8ArrayJSValue = arrayBuffer.toInt8ArrayJSValue()
    return int8ArrayJSValue
}
```

### func toUInt16Array()

```cangjie
public func toUInt16Array(): Array<UInt16>
```

**功能：** 转换为仓颉数组 Array\<UInt16>。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Array\<UInt16>|仓颉数组。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300002   | Outside error occurred.　             |
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func convertToUInt16Array(context: JSContext, callInfo: JSCallInfo): JSValue {
    let arrayBuffer = callInfo[0].asArrayBuffer()
    let uint16Array = arrayBuffer.toUInt16Array()
    Hilog.info(0, "test","Converted to UInt16Array with ${uint16Array.size} elements")
    return context.number(Float64(uint16Array.size)).toJSValue()
}
```