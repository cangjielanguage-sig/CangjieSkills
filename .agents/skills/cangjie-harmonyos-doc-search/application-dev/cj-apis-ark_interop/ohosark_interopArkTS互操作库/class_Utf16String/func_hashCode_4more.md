### func hashCode()

```cangjie
public func hashCode(): Int64
```

**功能：** 字符串 hash 值。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Int64|字符串 hash 值。<br>**注意：** 不保证该 hash 值与相同内容的 String 的 hash 一致。不保证该 hash 值与相同内容的 ArkTS string 的 hash 一致。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func getStringHashCode(context: JSContext): JSValue {
    let utf16Str = Utf16String("Hello World")
    let hashCode = utf16Str.hashCode()

    Hilog.info(0, "test", "String hash code: ${hashCode}")

    return context.number(Float64(hashCode)).toJSValue()
}
```

### func indexOf(Utf16String)

```cangjie
public func indexOf(target: Utf16String): ?Int64
```

**功能：** 向后查找字符串所在的位置（字符索引）。

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

func findSubstring(context: JSContext): JSValue {
    let utf16Str = Utf16String("Hello World Hello")
    let target = Utf16String("World")

    let index = utf16Str.indexOf(target)

    if (index != None) {
        Hilog.info(0, "test", "Found 'World' at index: ${index}")
    } else {
        Hilog.info(0, "test", "Substring not found")
    }

    return context.number(Float64(index.getOrDefault({=> -1}))).toJSValue()
}
```

### func indexOf(Utf16String, Int64)

```cangjie
public func indexOf(target: Utf16String, fromIndex: Int64): ?Int64
```

**功能：** 向后查找字符串所在的位置（编码单元索引）。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|target|[Utf16String](#class-utf16string)|是|-|目标字符串。|
|fromIndex|Int64|是|-|当前字符串的查找起始位置。|

**返回值：**

|类型|说明|
|:----|:----|
|?Int64|首次找到目标字符串时返回位置索引，未找到时返回 None。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |

### func isEmpty()

```cangjie
public func isEmpty(): Bool
```

**功能：** 是否为空字符串。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|是否为空字符串。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func checkIsEmpty(context: JSContext): JSValue {
    let emptyStr = Utf16String("")
    let nonEmptyStr = Utf16String("Hello")

    let isEmpty1 = emptyStr.isEmpty()
    let isEmpty2 = nonEmptyStr.isEmpty()

    Hilog.info(0, "test", "Empty string is empty: ${isEmpty1}")
    Hilog.info(0, "test", "Non-empty string is empty: ${isEmpty2}")

    return context.boolean(isEmpty1).toJSValue()
}
```