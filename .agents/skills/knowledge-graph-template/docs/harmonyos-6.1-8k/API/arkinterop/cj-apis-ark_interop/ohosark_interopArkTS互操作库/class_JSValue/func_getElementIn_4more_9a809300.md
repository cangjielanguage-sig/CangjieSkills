### func getElement(Int64)

```cangjie
public func getElement(index: Int64): JSValue
```

**功能：** 从 ArkTS 数组读取元素。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|数组元素索引。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#class-jsvalue)|一个 ArkTS 值。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 1     | The accessing index is out of range. |
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |
| 34300005   | The ArkTS data types do not match.   |

**示例：**

<!--compile-->
```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let jsArr = callInfo[0]
    let element = jsArr.getElement(0)
    return element
}
```

### func getProperty(JSKeyable)

```cangjie
public func getProperty(key: JSKeyable): JSValue
```

**功能：** 从 ArkTS 对象读取属性。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|[JSKeyable](#interface-jskeyable)|是|-|属性的键，可以是 String 、 JSString 或 JSSymbol。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#class-jsvalue)|取到的值|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |
| 34300005   | The ArkTS data types do not match.   |

**示例：**

<!--compile-->
```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let jsObJ = callInfo[0]
    let element = jsObJ.getProperty("a")
    let element1 = jsObJ.getProperty(context.string("a"))
    let element2 = jsObJ.getProperty(context.symbol())
    return element
}
```

>

### func isArray()

```cangjie
public func isArray(): Bool
```

**功能：** 判断一个 JSValue 是否是 Array 类型。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时代表类型为 Array。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

**示例：**

<!--compile-->
```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    // 获取入参
    let arg0 = callInfo[0]
    // 判断是否是 object
    let result = arg0.isArray()
    // 返回结果
    return context.boolean(result).toJSValue()
}
```

### func isArrayBuffer()

```cangjie
public func isArrayBuffer(): Bool
```

**功能：** 判断一个 JSValue 是否是 ArrayBuffer 类型。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时代表类型为 ArrayBuffer。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

**示例：**

<!--compile-->
```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    // 获取入参
    let arg0 = callInfo[0]
    // 判断是否是 ArrayBuffer
    let result = arg0.isArrayBuffer()
    // 返回结果
    return context.boolean(result).toJSValue()
}
```