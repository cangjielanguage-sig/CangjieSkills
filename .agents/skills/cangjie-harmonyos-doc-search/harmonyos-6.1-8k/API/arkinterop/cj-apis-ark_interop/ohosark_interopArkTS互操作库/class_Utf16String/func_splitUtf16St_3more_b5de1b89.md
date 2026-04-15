### func split(Utf16String, Int64, Bool)

```cangjie
public func split(separator: Utf16String, maxSplit: Int64, removeEmpty!: Bool = false): Array<Utf16String>
```

**功能：** 分割字符串。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值| 说明                          |
|:---|:---|:---|:---|:----------------------------|
|separator|[Utf16String](#class-utf16string)|是|-| 分隔符。当分隔符为空字符串时，每个字符都是单独的元素。 |
|maxSplit|Int64|是|-| 分割最大数量。为0时最大分割数量无限制。            |
|removeEmpty|Bool|否|false| 是否删除空白元素，为true时删除空白元素。      |

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[Utf16String](#class-utf16string)>|分割后的元素数组。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 1     | The accessing index is out of range. |
| 34300003   | Accessing reference is beyond reach. |

### func startsWith(Utf16String)

```cangjie
public func startsWith(target: Utf16String): Bool
```

**功能：** 字符串是否以目标字符串开头。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值| 说明                     |
|:---|:---|:---|:---|:-----------------------|
|target|[Utf16String](#class-utf16string)|是|-| 目标字符串。目标字符串为空时返回false。 |

**返回值：**

|类型|说明|
|:----|:----|
|Bool|是否以目标字符串开头。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func checkStartsWith(context: JSContext): JSValue {
    let utf16Str = Utf16String("Hello World")
    let target = Utf16String("Hello")

    let startsWithResult = utf16Str.startsWith(target)

    Hilog.info(0, "test", "String starts with 'Hello': ${startsWithResult}")

    return context.boolean(startsWithResult).toJSValue()
}
```

### func toJSValue(JSContext)

```cangjie
public func toJSValue(context: JSContext): JSValue
```

**功能：** 将 Utf16String 对象转换成 JSValue。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#class-jsvalue)|ArkTS 统一类型。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func convertToJSValue(context: JSContext): JSValue {
    let utf16Str = Utf16String("Hello from Utf16String")

    // 转换为 JSValue
    let jsValue = utf16Str.toJSValue(context)

    Hilog.info(0, "test", "Converted to JSValue")

    return jsValue
}
```