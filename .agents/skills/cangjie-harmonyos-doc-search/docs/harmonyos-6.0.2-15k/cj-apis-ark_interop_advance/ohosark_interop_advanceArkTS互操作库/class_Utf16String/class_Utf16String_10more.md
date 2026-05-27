## class Utf16String

```cangjie
public class Utf16String <: ToString & Equatable<Utf16String> & Hashable & JSKeyable & JSInteropType<Utf16String> {
    public init(src: String)
}
```

**功能：** 以 UTF-16 编码格式存储的字符串，在与 ArkTS 字符串相互转换时，相比 String 有更好的性能。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**父类型：**

* ToString
* Equatable\<Utf16String>
* Hashable
* [JSKeyable](#interface-jskeyable)
* [JSInteropType\<Utf16String>](#interface-jsinteroptype)

### prop accessible

```cangjie
public prop accessible: Bool
```

**功能：** 判断字符串内容是否可访问。该对象的字符串内容可以使用 dispose 手动释放，释放后继续访问会抛出异常。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**类型：** Bool

**读写能力：** 只读

### prop size

```cangjie
public prop size: Int64
```

**功能：** 表示该字符串（UTF-16 编码格式）中编码单元的总长度。其中，UTF-16 编码格式的编码单元占 2 个字节，每个字符有 1-2 个编码单元。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**类型：** Int64

**读写能力：** 只读

### prop totalChars

```cangjie
public prop totalChars: Int64
```

**功能：** 该字符的总字符数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**类型：** Int64

**读写能力：** 只读

### static let empty

```cangjie
public static let empty: Utf16String
```

**功能：** 空字符串。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**类型：** Utf16String

**读写能力：** 只读

### init(String)

```cangjie
public init(src: String)
```

**功能：** 从标准库 String 创建一个 Utf16String。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|src|String|是|-|目标字符串。|

### static func fromJSValue(JSContext, JSValue)

```cangjie
public static func fromJSValue(_: JSContext, value: JSValue): Utf16String
```

**功能：** 将 JSValue 转换为 Utf16String 对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|_|[JSContext](#class-jscontext)|是|-|ArkTS互操作上下文。|
|value|[JSValue](#struct-jsvalue)|是|-|ArkTS统一类型。|

**返回值：**

|类型|说明|
|:----|:----|
|[Utf16String](#class-utf16string)|Utf16String 对象。|

### static func toArkTsType()

```cangjie
public static func toArkTsType(): String
```

**功能：** 对应的 ArkTS 类型名称。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**返回值：**

|类型| 说明 |
|:----|:---|
|String| 对应的 ArkTS 类型名称。   |

### func compare(Utf16String)

```cangjie
public func compare(target: Utf16String): Ordering
```

**功能：** 按照字符 Unicode 的字典序比较大小。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|target|[Utf16String](#class-utf16string)|是|-|比较的 Utf16String 对象。|

**返回值：**

|类型|说明|
|:----|:----|
|Ordering|比较大小的结果。|

### func contains(Utf16String)

```cangjie
public func contains(target: Utf16String): Bool
```

**功能：** 是否包含字符串。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|target|[Utf16String](#class-utf16string)|是|-|目标字符串。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|是否包含目标字符串。|