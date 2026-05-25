### func isString()

```cangjie
public func isString(): Bool
```

**功能：** 判断一个 JSValue 是否是 string 类型。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时代表类型为 string。|

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
    // 判断是否是 string
    let result = arg0.isString()
    // 返回结果
    return context.boolean(result).toJSValue()
}
```

### func isSymbol()

```cangjie
public func isSymbol(): Bool
```

**功能：** 判断一个 JSValue 是否是 Symbol 类型。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时代表类型为 Symbol。|

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
    // 判断是否是 Symbol
    let result = arg0.isSymbol()
    // 返回结果
    return context.boolean(result).toJSValue()
}
```

### func isUndefined()

```cangjie
public func isUndefined(): Bool
```

**功能：** 判断一个 JSValue 是否是 undefined。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时代表类型为 undefined。|

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
    // 判断是否是 undefined
    let result = arg0.isUndefined()
    // 返回结果
    return context.boolean(result).toJSValue()
}
```

### func setElement(Int64, JSValue)

```cangjie
public func setElement(index: Int64, value: JSValue): Unit
```

**功能：** 从 ArkTS 数组写入元素。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|数组写入索引。|
|value|[JSValue](#class-jsvalue)|是|-|写入数组的值。|

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
    let setValue = context.number(1.0)
    jsArr.setElement(0, setValue.toJSValue())
    let element = jsArr.getElement(0)
    return element
}
```