### init(String)

```cangjie
public init(src: String)
```

**功能：** 从标准库 String 创建一个 Utf16String。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|src|String|是|-|目标字符串。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300002   | Outside error occurred.　             |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func createUtf16String(context: JSContext): JSValue {
    // 从字符串创建 Utf16String
    let utf16Str = Utf16String("Hello World")
    Hilog.info(0, "test", "Created Utf16String with content: ${utf16Str.toString()}")

    // 从 JSValue 创建 Utf16String
    let jsString = context.string("Test String")
    let utf16Str2 = Utf16String(jsString.toString())
    Hilog.info(0, "test", "Created Utf16String from JSValue: ${utf16Str2.toString()}")

    return context.string(utf16Str.toString()).toJSValue()
}
```

### static func fromJSValue(JSContext, JSValue)

```cangjie
public static func fromJSValue(_: JSContext, value: JSValue): Utf16String
```

**功能：** 将 JSValue 转换为 Utf16String 对象。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|_|[JSContext](#class-jscontext)|是|-|ArkTS互操作上下文。|
|value|[JSValue](#class-jsvalue)|是|-|ArkTS统一类型。|

**返回值：**

|类型|说明|
|:----|:----|
|[Utf16String](#class-utf16string)|Utf16String 对象。|

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
import ohos.hilog.Hilog

func createFromJSValue(context: JSContext): JSValue {
    let jsString = context.string("Hello from JS")
    let jsValue = jsString.toJSValue()

    // 从 JSValue 创建 Utf16String
    let utf16Str = Utf16String.fromJSValue(context, jsValue)

    Hilog.info(0, "test", "Created from JSValue: ${utf16Str.toString()}")

    return context.string(utf16Str.toString()).toJSValue()
}
```

### static func toArktsType()

```cangjie
public static func toArktsType(): String
```

**功能：** 对应的 ArkTS 类型名称。

**起始版本：** 22

**返回值：**

|类型| 说明 |
|:----|:---|
|String| 对应的 ArkTS 类型名称。   |

### func compare(Utf16String)

```cangjie
public func compare(target: Utf16String): Ordering
```

**功能：** 按照字符 Unicode 的字典序比较大小。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|target|[Utf16String](#class-utf16string)|是|-|比较的 Utf16String 对象。|

**返回值：**

|类型|说明|
|:----|:----|
|Ordering|比较大小的结果。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |