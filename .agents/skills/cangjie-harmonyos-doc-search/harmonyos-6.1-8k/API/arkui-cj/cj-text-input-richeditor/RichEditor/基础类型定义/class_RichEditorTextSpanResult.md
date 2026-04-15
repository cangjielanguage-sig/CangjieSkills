### class RichEditorTextSpanResult

```cangjie
public class RichEditorTextSpanResult <: RichEditorSpanResult {
    public var spanPosition: RichEditorSpanPosition
    public var value: String
    public var textStyle: RichEditorTextStyleResult
    public var offsetInSpan: (Int32, Int32)
    public init(
        spanPosition: RichEditorSpanPosition,
        value: String,
        textStyle: RichEditorTextStyleResult,
        offsetInSpan: (Int32, Int32)
    )
}
```

**功能：** 定义文本span结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**父类型：**

- [RichEditorSpanResult](#interface-richeditorspanresult)

#### var spanPosition

```cangjie
public var spanPosition: RichEditorSpanPosition
```

**功能：** 文本span的位置。

**类型：** [RichEditorSpanPosition](#class-richeditorspanposition)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var value

```cangjie
public var value: String
```

**功能：** 文本span的内容。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var textStyle

```cangjie
public var textStyle: RichEditorTextStyleResult
```

**功能：** 文本样式。

**类型：** [RichEditorTextStyleResult](#class-richeditortextstyleresult)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### var offsetInSpan

```cangjie
public var offsetInSpan: (Int32, Int32)
```

**功能：** span中的偏移量。

**类型：** (Int32, Int32)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

#### init(RichEditorSpanPosition, String, RichEditorTextStyleResult, (Int32, Int32))

```cangjie
public init(
    spanPosition: RichEditorSpanPosition,
    value: String,
    textStyle: RichEditorTextStyleResult,
    offsetInSpan: (Int32, Int32)
)
```

**功能：** RichEditorTextSpanResult构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|spanPosition|[RichEditorSpanPosition](#class-richeditorspanposition)|是|-|文本span的位置。|
|value|String|是|-|文本span的内容。|
|textStyle|[RichEditorTextStyleResult](#class-richeditortextstyleresult)|是|-|文本样式。|
|offsetInSpan|(Int32, Int32)|是|-|span中的偏移量。|