### func contains(Utf16String)

```cangjie
public func contains(target: Utf16String): Bool
```

**功能：** 是否包含字符串。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值| 说明                      |
|:---|:---|:---|:---|:------------------------|
|target|[Utf16String](#class-utf16string)|是|-| 目标字符串。当目标字符串为空时返回false。 |

**返回值：**

|类型|说明|
|:----|:----|
|Bool|是否包含目标字符串。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |

### func count(Utf16String)

```cangjie
public func count(src: Utf16String): Int64
```

**功能：** 包含字符串次数。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|src|[Utf16String](#class-utf16string)|是|-|目标字符串。|

**返回值：**

|类型|说明|
|:----|:----|
|Int64|包含目标字符串的次数。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func countSubstring(context: JSContext): JSValue {
    let utf16Str = Utf16String("Hello World Hello Hello")
    let target = Utf16String("Hello")

    let count = utf16Str.count(target)

    Hilog.info(0, "test", "Count of 'Hello': ${count}")

    return context.number(Float64(count)).toJSValue()
}
```

### func dispose()

```cangjie
public func dispose(): Unit
```

**功能：** 释放保存字符串内容的内存。在首次 dispose 之后继续访问该字符串的内容将导致异常。

**起始版本：** 22

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func disposeString(context: JSContext): JSValue {
    let utf16Str = Utf16String("Test String")

    // 使用字符串内容
    let content = utf16Str.toString()
    Hilog.info(0, "test", "String content before dispose: ${content}")

    // 手动释放字符串内容内存
    utf16Str.dispose()

    // dispose 后继续访问会抛出异常
    // let contentAfterDispose = utf16Str.toString() // 这行会抛出异常

    return context.string("String disposed").toJSValue()
}
```

### func endsWith(Utf16String)

```cangjie
public func endsWith(target: Utf16String): Bool
```

**功能：** 字符串是否以目标字符串结束。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值| 说明                     |
|:---|:---|:---|:---|:-----------------------|
|target|[Utf16String](#class-utf16string)|是|-| 目标字符串。目标字符串为空时返回false。 |

**返回值：**

|类型|说明|
|:----|:----|
|Bool|是否以目标字符串结束。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func checkEndsWith(context: JSContext): JSValue {
    let utf16Str = Utf16String("Hello World")
    let target = Utf16String("World")

    let endsWithResult = utf16Str.endsWith(target)

    Hilog.info(0, "test", "String ends with 'World': ${endsWithResult}")

    return context.boolean(endsWithResult).toJSValue()
}
```