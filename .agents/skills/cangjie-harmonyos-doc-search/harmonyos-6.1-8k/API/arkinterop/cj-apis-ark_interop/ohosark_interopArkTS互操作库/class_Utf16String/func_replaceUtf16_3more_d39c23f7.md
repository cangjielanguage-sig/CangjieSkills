### func replace(Utf16String, Utf16String, Int64)

```cangjie
public func replace(old: Utf16String, new: Utf16String, count!: Int64 = Int64.Max): Utf16String
```

**功能：** 替换字符串。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|old|[Utf16String](#class-utf16string)|是|-|替换前的元素|
|new|[Utf16String](#class-utf16string)|是|-|替换后的元素|
|count|Int64|否|Int64.Max|替换次数|

**返回值：**

|类型|说明|
|:----|:----|
|[Utf16String](#class-utf16string)| 替换完的字符串 |

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func replaceString(context: JSContext): JSValue {
    let utf16Str = Utf16String("Hello World Hello")
    let target = Utf16String("Hello")
    let replacement = Utf16String("Hi")

    // 替换最多1次
    let replacedStr = utf16Str.replace(target, replacement, count: 1)

    Hilog.info(0, "test", "Original string: ${utf16Str.toString()}")
    Hilog.info(0, "test", "Replaced string: ${replacedStr.toString()}")

    return context.string(replacedStr.toString()).toJSValue()
}
```

### func runes()

```cangjie
public func runes(): Iterator<Rune>
```

**功能：** 获取字符迭代器。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Iterator\<Rune>|字符迭代器。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |

### func split(Utf16String, Bool)

```cangjie
public func split(separator: Utf16String, removeEmpty!: Bool = false): Array<Utf16String>
```

**功能：** 分割字符串。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值| 说明                        |
|:---|:---|:---|:---|:--------------------------|
|separator|[Utf16String](#class-utf16string)|是|-| 分隔符。当分隔符为空字符串时，每个字符都是单独的元素。|
|removeEmpty|Bool|否|false| 是否删除空白元素，为true时删除空白元素。    |

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[Utf16String](#class-utf16string)>|分割后的元素数组。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func splitString(context: JSContext): JSValue {
    let utf16Str = Utf16String("Hello,World,Test")
    let separator = Utf16String(",")

    // 分割字符串，最多分割成3个部分，不移除空元素
    let splitResult = utf16Str.split(separator, 3, removeEmpty: false)

    Hilog.info(0, "test", "Split result size: ${splitResult.size}")

    for (i in 0..splitResult.size) {
        Hilog.info(0, "test", "Part ${i}: ${splitResult[i].toString()}")
    }

    return context.number(Float64(splitResult.size)).toJSValue()
}
```