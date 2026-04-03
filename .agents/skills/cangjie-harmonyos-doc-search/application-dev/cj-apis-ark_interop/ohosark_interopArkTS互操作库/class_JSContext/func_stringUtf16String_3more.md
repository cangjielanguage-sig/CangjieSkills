### func string(Utf16String)

```cangjie
public func string(value: Utf16String): JSString
```

**功能：** 从 Utf16String 创建 JSString。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Utf16String](#class-utf16string)|是|-|源 Utf16String 对象。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSString](#class-jsstring)|根据源对象创建的 JSString。|

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
    let utf16string = Utf16String("abc")
    let result = context.string(utf16string)
    return result.toJSValue()
}
```

### func symbol(String)

```cangjie
public func symbol(description!: String = ""): JSSymbol
```

**功能：** 创建一个 ArkTS symbol 对象。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|description|String|否|""| **命名参数。** symbol的描述。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSSymbol](#class-jssymbol)|ArkTS symbol 对象的引用。|

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
    let result = context.symbol()
    let symbol1 = context.symbol(description: "Symbol1")
    return result.toJSValue()
}
```

### func undefined()

```cangjie
public func undefined(): JSUndefined
```

**功能：** 创建一个 ArkTS undefined。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[JSUndefined](#class-jsundefined)|返回 ArkTS undefined。|

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
    let result = context.undefined()
    return result.toJSValue()
}
```