### func toUInt16ArrayJSValue()

```cangjie
public func toUInt16ArrayJSValue(): JSValue
```

**功能：** 返回 ArkTS 的 Uint16Array 的 JSValue。

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
func getUInt16ArrayJSValue(context: JSContext, callInfo: JSCallInfo): JSValue {
    let arrayBuffer = callInfo[0].asArrayBuffer()
    let uint16ArrayJSValue = arrayBuffer.toUInt16ArrayJSValue()
    return uint16ArrayJSValue
}
```

### func toUInt32Array()

```cangjie
public func toUInt32Array(): Array<UInt32>
```

**功能：** 转换为仓颉数组 Array\<UInt32>。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Array\<UInt32>|仓颉数组。|

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

func convertToUInt32Array(context: JSContext, callInfo: JSCallInfo): JSValue {
    let arrayBuffer = callInfo[0].asArrayBuffer()
    let uint32Array = arrayBuffer.toUInt32Array()
    Hilog.info(0, "test", "Converted to UInt32Array with ${uint32Array.size} elements")
    return context.number(Float64(uint32Array.size)).toJSValue()
}
```

### func toUInt32ArrayJSValue()

```cangjie
public func toUInt32ArrayJSValue(): JSValue
```

**功能：** 返回 ArkTS 的 Uint32Array 的 JSValue。

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
func getUInt32ArrayJSValue(context: JSContext, callInfo: JSCallInfo): JSValue {
    let arrayBuffer = callInfo[0].asArrayBuffer()
    let uint32ArrayJSValue = arrayBuffer.toUInt32ArrayJSValue()
    return uint32ArrayJSValue
}
```

### func toUInt64Array()

```cangjie
public func toUInt64Array(): Array<UInt64>
```

**功能：** 转换为仓颉数组 Array\<UInt64>。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Array\<UInt64>|仓颉数组。|

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

func convertToUInt64Array(context: JSContext, callInfo: JSCallInfo): JSValue {
    let arrayBuffer = callInfo[0].asArrayBuffer()
    let uint64Array = arrayBuffer.toUInt64Array()
    Hilog.info(0, "test", "Converted to UInt64Array with ${uint64Array.size} elements")
    return context.number(Float64(uint64Array.size)).toJSValue()
}
```