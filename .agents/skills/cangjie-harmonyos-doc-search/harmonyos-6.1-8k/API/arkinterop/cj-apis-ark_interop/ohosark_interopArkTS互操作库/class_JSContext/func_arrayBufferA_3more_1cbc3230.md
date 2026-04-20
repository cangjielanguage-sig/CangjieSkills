### func arrayBuffer(Array\<Float64>)

```cangjie
public func arrayBuffer(data: Array<Float64>): JSArrayBuffer
```

**功能：** 通过内存块创建一个 ArkTS ArrayBuffer。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|data|Array\<Float64>|是|-|仓颉数组。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSArrayBuffer](#class-jsarraybuffer)|ArkTS ArrayBuffer 对象的引用。|

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
import ohos.hilog.Hilog

func createArrayBufferFromFloat64(context: JSContext): JSValue {
    let float64Array: Array<Float64> = [1.0, 2.0, 3.0]
    let arrayBuffer = context.arrayBuffer(float64Array)

    Hilog.info(0, "test", "Created ArrayBuffer from Float64 array")

    return arrayBuffer.toJSValue()
}
```

### func arrayBuffer(CPointer\<Byte>, Int32, JSBufferFinalizer)

```cangjie
public unsafe func arrayBuffer(rawData: CPointer<Byte>, length: Int32, finalizer: JSBufferFinalizer): JSArrayBuffer
```

**功能：** 通过内存块创建一个 ArkTS ArrayBuffer。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rawData|CPointer\<Byte>|是|-|内存块地址。|
|length|Int32|是|-|内存块大小。|
|finalizer|[JSBufferFinalizer](#type-jsbufferfinalizer)|是|-|内存块回收函数。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSArrayBuffer](#class-jsarraybuffer)|ArkTS ArrayBuffer 对象的引用。|

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
    let rawPtr = unsafe {
        LibC.malloc<Byte>(count: 10)
    }
    let result = unsafe { context.arrayBuffer(rawPtr, 10) { rawPtr =>
        LibC.free(rawPtr)
    }}
    return result.toJSValue()
}
```

### func bigint(Int64)

```cangjie
public func bigint(value: Int64): JSBigInt
```

**功能：** 通过仓颉 BigInt 创建一个等值的 ArkTS bigint。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int64|是|-|仓颉BigInt。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSBigInt](#class-jsbigint)|ArkTS bigint 对象的引用。|

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
    let result = context.bigint(100)
    return result.toJSValue()
}
```