### func isBigInt()

```cangjie
public func isBigInt(): Bool
```

**功能：** 判断一个 JSValue 是否是 bigint 类型。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时代表类型为 bigint。|

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
    // 判断是否是 bigint
    let result = arg0.isBigInt()
    // 返回结果
    return context.boolean(result).toJSValue()
}
```

### func isBoolean()

```cangjie
public func isBoolean(): Bool
```

**功能：** 判断一个 JSValue 是否是 boolean 类型。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时代表类型为 boolean。|

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
    // 判断是否是 boolean
    let result = arg0.isBoolean()
    // 返回结果
    return context.boolean(result).toJSValue()
}
```

### func isClass()

```cangjie
public func isClass(): Bool
```

**功能：** 判断一个 JSValue 是否是一个 ArkTS 类（构造函数）。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时代表类型为 ArkTS 类（构造函数）|

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
    // 判断是否是 ArkTS 类（构造函数）
    let result = arg0.isClass()
    // 返回结果
    return context.boolean(result).toJSValue()
}
```

### func isExternal()

```cangjie
public func isExternal(): Bool
```

**功能：** 判断一个 JSValue 是否是一个外部对象（仓颉对象的 ArkTS 引用）。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时代表类型为外部对象（仓颉对象的 ArkTS 引用）。|

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
    // 判断是否是外部对象（仓颉对象的 ArkTS 引用）
    let result = arg0.isExternal()
    // 返回结果
    return context.boolean(result).toJSValue()
}
```