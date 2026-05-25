### class RichEditorSpanResult

```cangjie
public class RichEditorSpanResult {
    public var spanType: SpanType
    public var textResult: Option<RichEditorTextSpanResult>
    public var imageResult: Option<RichEditorImageSpanResult>
}
```

**功能：** Span信息类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var imageResult

```cangjie
public var imageResult: Option<RichEditorImageSpanResult>
```

**功能：** 表示image类型的结果。

**类型：** Option\<[RichEditorImageSpanResult](#class-richeditorimagespanresult)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var spanType

```cangjie
public var spanType: SpanType
```

**功能：** 表示Span的类型。

**类型：** [SpanType](#enum-spantype)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var textResult

```cangjie
public var textResult: Option<RichEditorTextSpanResult>
```

**功能：** 表示text类型的结果。

**类型：** Option\<[RichEditorTextSpanResult](#class-richeditortextspanresult)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### class RichEditorParagraphStyleResult

```cangjie
public class RichEditorParagraphStyleResult {
    public var textAlign: TextAlign = TextAlign.Start
    public var leadingMargin: (String, String) = ("", "")
    public var wordBreak: WordBreak = WordBreak.BreakWord
    public var lineBreakStrategy: LineBreakStrategy = LineBreakStrategy.GREEDY
}
```

**功能：** 段落样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var textAlign

```cangjie
public var textAlign: TextAlign = TextAlign.Start
```

**功能：** 表示文本段落在水平方向的对齐方式。

**类型：** [TextAlign](./cj-common-types.md#enum-textalign)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var leadingMargin

```cangjie
public var leadingMargin: (String, String) = ("", "")
```

**功能：** 表示文本段落缩进。

> **说明：**
>
> 当段落仅存在ImageSpan或BuilderSpan时，此属性值不生效。参数为Dimension类型时，不支持以Percentage形式设置。

**类型：** (String， String)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var wordBreak

```cangjie
public var wordBreak: WordBreak = WordBreak.BreakWord
```

**功能：** 表示断行规则。

**类型：** [WordBreak](./cj-common-types.md#enum-wordbreak)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var lineBreakStrategy

```cangjie
public var lineBreakStrategy: LineBreakStrategy = LineBreakStrategy.GREEDY
```

**功能：** 表示折行规则。

**类型：** [LineBreakStrategy](./cj-common-types.md#enum-linebreakstrategy)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19