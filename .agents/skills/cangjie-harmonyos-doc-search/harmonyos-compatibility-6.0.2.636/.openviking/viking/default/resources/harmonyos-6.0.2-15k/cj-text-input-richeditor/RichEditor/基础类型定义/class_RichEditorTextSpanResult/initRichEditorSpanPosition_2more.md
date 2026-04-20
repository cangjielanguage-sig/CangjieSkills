#### init(RichEditorSpanPosition, String, RichEditorTextStyleResult, (Int32, Int32))

```cangjie
public init(
    spanPosition: RichEditorSpanPosition,
    value: String,
    textStyle: RichEditorTextStyleResult,
    offsetInSpan: (Int32, Int32)
)
```

**功能：** 创建RichEditorTextSpanResult。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|spanPosition|[RichEditorSpanPosition](#class-richeditorspanposition)|是|-|Span位置。|
|value|String|是|-|文本Span内容。|
|textStyle|[RichEditorTextStyleResult](#class-richeditortextstyleresult)|是|-|文本Span样式信息。|
|offsetInSpan|(Int32, Int32)|是|-|文本Span内容里有效内容的起始和结束位置。|

#### init(RichEditorSpanPosition, String, RichEditorTextStyleResult, (Int32, Int32), RichEditorSymbolSpanStyleResult, RichEditorParagraphStyleResult, String)

```cangjie
public init(
    spanPosition: RichEditorSpanPosition,
    value: String,
    textStyle: RichEditorTextStyleResult,
    offsetInSpan: (Int32, Int32),
    symbolSpanStyle: RichEditorSymbolSpanStyleResult,
    paragraphStyle: RichEditorParagraphStyleResult,
    previewText: String
)
```

**功能：** 创建RichEditorTextSpanResult。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|spanPosition|[RichEditorSpanPosition](#class-richeditorspanposition)|是|-|Span位置。|
|value|String|是|-|文本Span内容。|
|textStyle|[RichEditorTextStyleResult](#class-richeditortextstyleresult)|是|-|文本Span样式信息。|
|offsetInSpan|(Int32, Int32)|是|-|文本Span内容里有效内容的起始和结束位置。|
|symbolSpanStyle|[RichEditorSymbolSpanStyleResult](#class-richeditorsymbolspanstyleresult)|是|-|后端返回的SymbolSpan样式信息。|
|paragraphStyle|[RichEditorParagraphStyleResult](#class-richeditorparagraphstyleresult)|是|-|段落样式。|
|previewText|String|是|-|插入的预上屏文本内容。|