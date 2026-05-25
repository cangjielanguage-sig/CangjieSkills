### struct TextPickerResult<sup>(deprecated)</sup>

```cangjie
public struct TextPickerResult {
    public TextPickerResult(
        public let value: CString,
        public let index: UInt32
    )
}
```

**功能：** 记录文本选择器组件的结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### let index

```cangjie
public let index: UInt32
```

**功能：** 文本选择器组件选择结果所在下标。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 12

#### let value

```cangjie
public let value: CString
```

**功能：** 文本选择器组件的文本。

**类型：** [CString](./cj-common-types.md#string)

**读写能力：** 只读

**起始版本：** 12

#### TextPickerResult(CString, UInt32)

```cangjie
public TextPickerResult(
    public let value: CString,
    public let index: UInt32
)
```

**功能：** 创建TextPickerResult结构。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[CString](./cj-common-types.md#string)|是|-|文本选择器组件的文本。|
|index|UInt32|是|-|文本选择器组件选择结果所在下标。|

### class ValueParams<sup>(deprecated)</sup>

```cangjie
public class ValueParams {
    public var value: String
    public var valuechangeEvent:(String) -> Unit
    public init(value!: String="")
    public init(value!: (String, (String) -> Unit) = ( "", {value => }))
}
```

**功能：** 记录文本选择器组件参数的结构。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var value

```cangjie
public var value: String
```

**功能：** 文本选择器的值参数。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var valuechangeEvent

```cangjie
public var valuechangeEvent:(String) -> Unit
```

**功能：** 文本选择器值改变时回调的事件。

**类型：** (String)->Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(String)

```cangjie
public init(value!: String="")
```

**功能：** 构建ValueParams结构体。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|否|""| **命名参数。** 文本选择器的值参数。|

#### init((String,(String) -> Unit))

```cangjie
public init(value!: (String, (String) -> Unit) = ( "", {_ =>}))
```

**功能：** 构建ValueParams结构体。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|(String,(String)->Unit)|否|("", {_ =>})| **命名参数。** 文本选择器的值参数。|