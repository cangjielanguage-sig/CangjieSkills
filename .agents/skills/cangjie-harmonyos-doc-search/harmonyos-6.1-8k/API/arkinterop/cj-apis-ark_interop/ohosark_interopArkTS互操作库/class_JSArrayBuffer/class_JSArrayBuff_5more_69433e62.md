## class JSArrayBuffer

```cangjie
public class JSArrayBuffer <: JSHeapObject {}
```

**功能：** JSArrayBuffer 对象用来表示通用的原始二进制数据缓冲区。通过创建 JS ArrayBuffer 对象，可以获取对象字节长度，转换为仓颉数组。

**起始版本：** 22

**父类型：**

- [JSHeapObject](#class-jsheapobject)

### prop byteLength

```cangjie
public prop byteLength: Int32
```

**功能：** ArrayBuffer 的字节数。

**起始版本：** 22

**类型：** Int32

**读写能力：** 只读

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                  |
|:------|:--------------------------------------|
| 34300003   | Accessing reference is beyond reach.  |
| 34300004   | Thread mismatch.                      |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func getBufferLength(context: JSContext, callInfo: JSCallInfo): JSValue {
    let arrayBuffer = callInfo[0].asArrayBuffer()
    let length = arrayBuffer.byteLength
    Hilog.info(0, "test", "ArrayBuffer length: ${length}")
    return context.number(Float64(length)).toJSValue()
}
```

### func readBytes()

```cangjie
public func readBytes(): Array<Byte>
```

**功能：** 读取二进制数据，转换为仓颉数组。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Byte>|仓颉数组。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                  |
|:------|:--------------------------------------|
| 34300003   | Accessing reference is beyond reach.  |
| 34300004   | Thread mismatch.                      |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func readBufferBytes(context: JSContext, callInfo: JSCallInfo): JSValue {
    let arrayBuffer = callInfo[0].asArrayBuffer()
    let bytes = arrayBuffer.readBytes()
    Hilog.info(0, "test","Read ${bytes.size} bytes from ArrayBuffer")
    return context.number(Float64(bytes.size)).toJSValue()
}
```

### func toArrayBufferJSValue()

```cangjie
public func toArrayBufferJSValue(): JSValue
```

**功能：** 返回 ArkTS 的 ArrayBuffer 的 JSValue。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#class-jsvalue)|ArkTS统一类型。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息 |
|:------| :--- |
| 34300002   | Outside error occurred.|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch. |

**示例：**

<!--compile-->
```cangjie
func getArrayBufferJSValue(context: JSContext): JSValue {
    let data: Array<Byte> = [1, 2, 3, 4]
    let arrayBuffer = context.arrayBuffer(data)
    let jsValue = arrayBuffer.toArrayBufferJSValue()
    return jsValue
}
```

### func toFloat32Array()

```cangjie
public func toFloat32Array(): Array<Float32>
```

**功能：** 转换为仓颉数组 Array\<Float32>。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Float32>|仓颉数组。|

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

func createFloat32Array(context: JSContext): Unit {
    let data: Array<Float32> = [1.0, 2.0, 3.0, 4.0]
    let arrayBuffer = context.arrayBuffer(data)
    let received = arrayBuffer.toFloat32Array()
    Hilog.info(0, "test", "Converted to Float32Array ${received}")
}
```