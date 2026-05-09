## class Utf16String

```cangjie
public class Utf16String <: ToString & Equatable<Utf16String> & Hashable & JSKeyable & JSInteropType<Utf16String> {
    public static let EMPTY: Utf16String
    public init(src: String)
}
```

**功能：** 以 UTF-16 编码格式存储的字符串，在与 ArkTS 字符串相互转换时，相比 String 有更好的性能。

**起始版本：** 22

**父类型：**

- ToString
- Equatable\<Utf16String>
- Hashable
- [JSKeyable](#interface-jskeyable)
- [JSInteropType\<Utf16String>](#interface-jsinteroptypet)

### prop accessible

```cangjie
public prop accessible: Bool
```

**功能：** 判断字符串内容是否可访问。该对象的字符串内容可以使用 dispose 手动释放，释放后继续访问会抛出异常。

**起始版本：** 22

**类型：** Bool

**读写能力：** 只读

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func checkStringAccessibility(context: JSContext): JSValue {
    let utf16Str = Utf16String("Test String")

    if (utf16Str.accessible) {
        Hilog.info(0, "test", "String content is accessible")
        // 安全地使用字符串内容
        let length = utf16Str.size
        Hilog.info(0, "test", "String length: ${length}")
    } else {
        Hilog.info(0, "test", "String content is not accessible")
    }

    return context.boolean(utf16Str.accessible).toJSValue()
}
```

### prop size

```cangjie
public prop size: Int64
```

**功能：** 表示该字符串（UTF-16 编码格式）中编码单元的总长度。其中，UTF-16 编码格式的编码单元占 2 个字节，每个字符有 1-2 个编码单元。

**起始版本：** 22

**类型：** Int64

**读写能力：** 只读

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func getStringSize(context: JSContext): JSValue {
    let utf16Str = Utf16String("Hello 世界")  // 包含中英文混合字符串
    let size = utf16Str.size  // UTF-16编码单元的总长度

    Hilog.info(0, "test", "UTF-16 string size: ${size}")

    return context.number(Float64(size)).toJSValue()
}
```

### prop totalChars

```cangjie
public prop totalChars: Int64
```

**功能：** 该字符的总字符数。

**起始版本：** 22

**类型：** Int64

**读写能力：** 只读

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func getStringTotalChars(context: JSContext): JSValue {
    let utf16Str = Utf16String("Hello 世界")  // 包含中英文混合字符串
    let totalChars = utf16Str.totalChars  // 字符总数

    Hilog.info(0, "test", "Total characters: ${totalChars}")

    return context.number(Float64(totalChars)).toJSValue()
}
```

### static let EMPTY

```cangjie
public static let EMPTY: Utf16String
```

**功能：** 空字符串。

**起始版本：** 22

**类型：** Utf16String

**读写能力：** 只读