### func arrayBuffer(Array\<UInt16>)

```cangjie
public func arrayBuffer(data: Array<UInt16>): JSArrayBuffer
```

**功能：** 通过内存块创建一个 ArkTS ArrayBuffer。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|data|Array\<UInt16>|是|-|仓颉数组。|

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

func createArrayBufferFromUInt16(context: JSContext): JSValue {
    let uint16Array: Array<UInt16> = [1, 2, 3]
    let arrayBuffer = context.arrayBuffer(uint16Array)

    Hilog.info(0, "test", "Created ArrayBuffer from UInt16 array")

    return arrayBuffer.toJSValue()
}
```

### func arrayBuffer(Array\<UInt32>)

```cangjie
public func arrayBuffer(data: Array<UInt32>): JSArrayBuffer
```

**功能：** 通过内存块创建一个 ArkTS ArrayBuffer。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|data|Array\<UInt32>|是|-|仓颉数组。|

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

func createArrayBufferFromUInt32(context: JSContext): JSValue {
    let uint32Array: Array<UInt32> = [1, 2, 3]
    let arrayBuffer = context.arrayBuffer(uint32Array)

    Hilog.info(0, "test", "Created ArrayBuffer from UInt32 array")

    return arrayBuffer.toJSValue()
}
```

### func arrayBuffer(Array\<Int32>)

```cangjie
public func arrayBuffer(data: Array<Int32>): JSArrayBuffer
```

**功能：** 通过内存块创建一个 ArkTS ArrayBuffer。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|data|Array\<Int32>|是|-|仓颉数组。|

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

func createArrayBufferFromInt32(context: JSContext): JSValue {
    let int32Array: Array<Int32> = [1, 2, 3]
    let arrayBuffer = context.arrayBuffer(int32Array)

    Hilog.info(0, "test", "Created ArrayBuffer from Int32 array")

    return arrayBuffer.toJSValue()
}
```