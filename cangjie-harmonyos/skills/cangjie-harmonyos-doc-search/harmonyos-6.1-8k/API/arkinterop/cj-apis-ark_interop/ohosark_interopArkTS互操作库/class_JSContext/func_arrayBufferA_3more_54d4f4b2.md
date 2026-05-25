### func arrayBuffer(Array\<Float32>)

```cangjie
public func arrayBuffer(data: Array<Float32>): JSArrayBuffer
```

**功能：** 通过内存块创建一个 ArkTS ArrayBuffer。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|data|Array\<Float32>|是|-|仓颉数组。|

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

func createArrayBufferFromFloat32(context: JSContext): JSValue {
    let float32Array: Array<Float32> = [1.0, 2.0, 3.0]
    let arrayBuffer = context.arrayBuffer(float32Array)

    Hilog.info(0, "test", "Created ArrayBuffer from Float32 array")

    return arrayBuffer.toJSValue()
}
```

### func arrayBuffer(Array\<Int64>)

```cangjie
public func arrayBuffer(data: Array<Int64>): JSArrayBuffer
```

**功能：** 通过内存块创建一个 ArkTS ArrayBuffer。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|data|Array\<Int64>|是|-|仓颉数组。|

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

func createArrayBufferFromInt64(context: JSContext): JSValue {
    let int64Array: Array<Int64> = [1, 2, 3]
    let arrayBuffer = context.arrayBuffer(int64Array)

    Hilog.info(0, "test", "Created ArrayBuffer from Int64 array")

    return arrayBuffer.toJSValue()
}
```

### func arrayBuffer(Array\<UInt64>)

```cangjie
public func arrayBuffer(data: Array<UInt64>): JSArrayBuffer
```

**功能：** 通过内存块创建一个 ArkTS ArrayBuffer。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|data|Array\<UInt64>|是|-|仓颉数组。|

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

func createArrayBufferFromUInt64(context: JSContext): JSValue {
    let uint64Array: Array<UInt64> = [1u64, 2u64, 3u64]
    let arrayBuffer = context.arrayBuffer(uint64Array)

    Hilog.info(0, "test", "Created ArrayBuffer from UInt64 array")

    return arrayBuffer.toJSValue()
}
```