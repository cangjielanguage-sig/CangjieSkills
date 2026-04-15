### func toUInt64ArrayJSValue()

```cangjie
public func toUInt64ArrayJSValue(): JSValue
```

**功能：** 返回 ArkTS 的 BigUint64Array 的 JSValue。

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
func getUInt64ArrayJSValue(context: JSContext, callInfo: JSCallInfo): JSValue {
    let arrayBuffer = callInfo[0].asArrayBuffer()
    let uint64ArrayJSValue = arrayBuffer.toUInt64ArrayJSValue()
    return uint64ArrayJSValue
}
```

### func toUInt8Array()

```cangjie
public func toUInt8Array(): Array<UInt8>
```

**功能：** 转换为仓颉数组 Array\<UInt8>。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Array\<UInt8>|仓颉数组。|

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

func convertToUInt8Array(context: JSContext, callInfo: JSCallInfo): JSValue {
    let arrayBuffer = callInfo[0].asArrayBuffer()
    let uint8Array = arrayBuffer.toUInt8Array()
    Hilog.info(0, "test", "Converted to UInt8Array with ${uint8Array.size} elements")
    return context.number(Float64(uint8Array.size)).toJSValue()
}
```

### func toUInt8ArrayJSValue()

```cangjie
public func toUInt8ArrayJSValue(): JSValue
```

**功能：** 返回 ArkTS 的 Uint8Array 的 JSValue。

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
func getUInt8ArrayJSValue(context: JSContext, callInfo: JSCallInfo): JSValue {
    let arrayBuffer = callInfo[0].asArrayBuffer()
    let uint8ArrayJSValue = arrayBuffer.toUInt8ArrayJSValue()
    return uint8ArrayJSValue
}
```

### func toUInt8ClampedArrayJSValue()

```cangjie
public func toUInt8ClampedArrayJSValue(): JSValue
```

**功能：** 返回 ArkTS 的 Uint8ClampedArray 的 JSValue。

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
func getUInt8ClampedArrayJSValue(context: JSContext, callInfo: JSCallInfo): JSValue {
    let arrayBuffer = callInfo[0].asArrayBuffer()
    let uint8ClampedArrayJSValue = arrayBuffer.toUInt8ClampedArrayJSValue()
    return uint8ClampedArrayJSValue
}
```