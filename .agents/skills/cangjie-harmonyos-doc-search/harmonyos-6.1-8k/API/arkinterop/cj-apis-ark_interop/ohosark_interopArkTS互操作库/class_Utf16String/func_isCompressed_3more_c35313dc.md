### func isCompressed()

```cangjie
public func isCompressed(): Bool
```

**功能：** 判断内容是否被压缩。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool| 是否被压缩 |

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func checkIsCompressed(context: JSContext): JSValue {
    let utf16Str = Utf16String("Hello World")

    let isCompressed = utf16Str.isCompressed()

    Hilog.info(0, "test", "String is compressed: ${isCompressed}")

    return context.boolean(isCompressed).toJSValue()
}
```

### func lastIndexOf(Utf16String)

```cangjie
public func lastIndexOf(target: Utf16String): ?Int64
```

**功能：** 向前查找字符所在的位置。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|target|[Utf16String](#class-utf16string)|是|-|目标字符串。|

**返回值：**

|类型|说明|
|:----|:----|
|?Int64|首次找到目标字符串时返回位置索引，未找到时返回 None。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func findLastSubstring(context: JSContext): JSValue {
    let utf16Str = Utf16String("Hello World Hello")
    let target = Utf16String("Hello")

    let index = utf16Str.lastIndexOf(target)

    if (index != None) {
        Hilog.info(0, "test", "Last 'Hello' found at index: ${index}")
    } else {
        Hilog.info(0, "test", "Substring not found")
    }

    return context.number(Float64(index.getOrDefault({=> -1}))).toJSValue()
}
```

### func lastIndexOf(Utf16String, Int64)

```cangjie
public func lastIndexOf(target: Utf16String, fromIndex: Int64): ?Int64
```

**功能：** 向前查找字符所在的位置。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值| 说明                                                                 |
|:---|:---|:---|:---|:-------------------------------------------------------------------|
|target|[Utf16String](#class-utf16string)|是|-| 目标字符串。                                                             |
|fromIndex|Int64|是|-| 当前字符串的查找起始位置（从目标字符串末尾往前匹配）。fromIndex小于0或大于等于size时视为size-1，字符串末尾位置。 |

**返回值：**

|类型|说明|
|:----|:----|
|?Int64|首次找到目标字符串时返回位置索引，未找到时返回 None。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func findLastSubstringFromIndex(context: JSContext): JSValue {
    let utf16Str = Utf16String("Hello World Hello")
    let target = Utf16String("Hello")

    // 从索引10开始向前查找
    let index = utf16Str.lastIndexOf(target, 10)

    if (index != None) {
        Hilog.info(0, "test", "Last 'Hello' found at index: ${index}")
    } else {
        Hilog.info(0, "test", "Substring not found")
    }

    return context.number(Float64(index.getOrDefault({=> -1}))).toJSValue()
}
```