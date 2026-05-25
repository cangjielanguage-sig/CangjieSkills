### func lazySplit(Utf16String, Bool)

```cangjie
public func lazySplit(separator: Utf16String, removeEmpty!: Bool = false): Iterator<Utf16String>
```

**功能：** 懒分割字符串。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|separator|[Utf16String](#class-utf16string)|是|-|分隔符。当分隔符为空字符串时，每个字符都是单独的元素。|
|removeEmpty|Bool|否|false|是否删除空白元素，为true时删除空白元素。|

**返回值：**

|类型|说明|
|:----|:----|
|Iterator\<[Utf16String](#class-utf16string)>|分割后的元素迭代器。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func lazySplitString(context: JSContext): JSValue {
    let utf16Str = Utf16String("Hello,World,Test,Example")
    let separator = Utf16String(",")

    // 懒分割字符串，移除空元素
    let splitIterator = utf16Str.lazySplit(separator, removeEmpty: true)

    var count = 0
    for (part in splitIterator) {
        Hilog.info(0, "test", "Lazy split part ${count}: ${part.toString()}")
        count = count + 1
    }

    return context.number(Float64(count)).toJSValue()
}
```

### func lazySplit(Utf16String, Int64, Bool)

```cangjie
public func lazySplit(separator: Utf16String, maxSplit: Int64, removeEmpty!: Bool = false): Iterator<Utf16String>
```

**功能：** 懒分割字符串。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值| 说明                          |
|:---|:---|:---|:---|:----------------------------|
|separator|[Utf16String](#class-utf16string)|是|-| 分隔符。当分隔符为空字符串时，每个字符都是单独的元素。 |
|maxSplit|Int64|是|-| 分割最大数量。为0时最大分割数量无限制。        |
|removeEmpty|Bool|否|false| 是否删除空白元素，为true时删除空白元素。                   |

**返回值：**

|类型|说明|
|:----|:----|
|Iterator\<[Utf16String](#class-utf16string)>|分割后的元素迭代器。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |

### func lines()

```cangjie
public func lines(): Iterator<Utf16String>
```

**功能：** 获取行迭代器。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Iterator\<[Utf16String](#class-utf16string)>|行迭代器。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func getLines(context: JSContext): JSValue {
    let utf16Str = Utf16String("Line 1\nLine 2\nLine 3")

    // 获取行迭代器
    let lineIterator = utf16Str.lines()

    var count = 0
    for (line in lineIterator) {
        Hilog.info(0, "test", "Line ${count}: ${line.toString()}")
        count = count + 1
    }

    return context.number(Float64(count)).toJSValue()
}
```