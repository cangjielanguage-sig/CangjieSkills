### func arrayBuffer(Array\<Byte>)

```cangjie
public func arrayBuffer(data: Array<Byte>): JSArrayBuffer
```

**功能：** 通过内存块创建一个 ArkTS ArrayBuffer。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|data|Array\<Byte>|是|-|仓颉数组。|

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
    let array : Array<Byte> = [1, 2, 3, 4, 5]
    let result = context.arrayBuffer(array)
    return result.toJSValue()
}
```

### func arrayBuffer(Array\<Int8>)

```cangjie
public func arrayBuffer(data: Array<Int8>): JSArrayBuffer
```

**功能：** 通过内存块创建一个 ArkTS ArrayBuffer。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|data|Array\<Int8>|是|-|仓颉数组。|

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

func createArrayBufferFromInt8(context: JSContext): JSValue {
    let int8Array: Array<Int8> = [1, 2, 3]
    let arrayBuffer = context.arrayBuffer(int8Array)

    Hilog.info(0, "test", "Created ArrayBuffer from Int8 array")

    return arrayBuffer.toJSValue()
}
```

### func arrayBuffer(Array\<Int16>)

```cangjie
public func arrayBuffer(data: Array<Int16>): JSArrayBuffer
```

**功能：** 通过内存块创建一个 ArkTS ArrayBuffer。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|data|Array\<Int16>|是|-|仓颉数组。|

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

func createArrayBufferFromInt16(context: JSContext): JSValue {
    let int16Array: Array<Int16> = [1, 2, 3]
    let arrayBuffer = context.arrayBuffer(int16Array)

    Hilog.info(0, "test", "Created ArrayBuffer from Int16 array")

    return arrayBuffer.toJSValue()
}
```