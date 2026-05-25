### func isFunction()

```cangjie
public func isFunction(): Bool
```

**功能：** 判断一个 JSValue 是否是 function 类型。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时代表类型为 function。|

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
    // 判断是否是 function
    let result = arg0.isFunction()
    // 返回结果
    return context.boolean(result).toJSValue()
}
```

### func isNull()

```cangjie
public func isNull(): Bool
```

**功能：** 判断一个 JSValue 是否是 null。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时代表类型为 null。|

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
    // 判断是否是 null
    let result = arg0.isNull()
    // 返回结果
    return context.boolean(result).toJSValue()
}
```

### func isNumber()

```cangjie
public func isNumber(): Bool
```

**功能：** 判断一个 JSValue 是否是 number 类型。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时代表类型为 number。|

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
    // 判断是否是 number
    let result = arg0.isNumber()
    // 返回结果
    return context.boolean(result).toJSValue()
}
```

### func isObject()

```cangjie
public func isObject(): Bool
```

**功能：** 判断一个 JSValue 是否是 object 类型。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时代表类型为 object|

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
    let result = arg0.isObject()
    // 返回结果
    return context.boolean(result).toJSValue()
}
```

### func isPromise()

```cangjie
public func isPromise(): Bool
```

**功能：** 判断一个 JSValue 是否是 Promise 类型。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时代表类型为 Promise。|

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
    // 判断是否是 Promise
    let result = arg0.isPromise()
    // 返回结果
    return context.boolean(result).toJSValue()
}
```