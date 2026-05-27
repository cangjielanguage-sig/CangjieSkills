### class RichEditorTextSpanResult

```cangjie
public class RichEditorTextSpanResult {
    public var spanPosition: RichEditorSpanPosition
    public var value: String
    public var textStyle: RichEditorTextStyleResult
    public var offsetInSpan: (Int32, Int32)
    public var symbolSpanStyle: RichEditorSymbolSpanStyleResult = RichEditorSymbolSpanStyleResult()
    public var paragraphStyle: RichEditorParagraphStyleResult = RichEditorParagraphStyleResult()
    public var previewText: String = ""

    public init(
        spanPosition: RichEditorSpanPosition,
        value: String,
        textStyle: RichEditorTextStyleResult,
        offsetInSpan: (Int32, Int32)
    )

    public init(
        spanPosition: RichEditorSpanPosition,
        value: String,
        textStyle: RichEditorTextStyleResult,
        offsetInSpan: (Int32, Int32),
        symbolSpanStyle: RichEditorSymbolSpanStyleResult,
        paragraphStyle: RichEditorParagraphStyleResult,
        previewText: String
    )
}
```

**功能：** 后端返回的文本样式信息类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var offsetInSpan

```cangjie
public var offsetInSpan:(Int32, Int32)
```

**功能：** 表示文本Span内容里有效内容的起始和结束位置。

**类型：** (Int32, Int32)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var paragraphStyle

```cangjie
public var paragraphStyle: RichEditorParagraphStyleResult = RichEditorParagraphStyleResult()
```

**功能：** 表示段落样式。

**类型：** [RichEditorParagraphStyleResult](#class-richeditorparagraphstyleresult)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var previewText

```cangjie
public var previewText: String = ""
```

**功能：** 表示插入的预上屏文本内容。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var spanPosition

```cangjie
public var spanPosition: RichEditorSpanPosition
```

**功能：** 表示Span位置。

**类型：** [RichEditorSpanPosition](#class-richeditorspanposition)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var symbolSpanStyle

```cangjie
public var symbolSpanStyle: RichEditorSymbolSpanStyleResult = RichEditorSymbolSpanStyleResult()
```

**功能：** 设置后端返回的SymbolSpan样式信息。

**类型：** [RichEditorSymbolSpanStyleResult](#class-richeditorsymbolspanstyleresult)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var textStyle

```cangjie
public var textStyle: RichEditorTextStyleResult
```

**功能：** 表示文本Span样式信息。

**类型：** [RichEditorTextStyleResult](#class-richeditortextstyleresult)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var value

```cangjie
public var value: String
```

**功能：** 表示文本Span内容。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12