### class RichEditorParagraphStyle

```cangjie
public class RichEditorParagraphStyle {
    public var textAlign: TextAlign
    public var margin: Option<Length>
    public var placeholder: Option<LeadingMarginPlaceholder>
    public init(textAlign!: TextAlign = TextAlign.Start)
    public init(textAlign!: TextAlign = TextAlign.Start, leadingMargin!: Length)
    public init(textAlign!: TextAlign = TextAlign.Start, leadingMargin!: LeadingMarginPlaceholder)
}
```

**功能：** 段落样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var textAlign

```cangjie
public var textAlign: TextAlign
```

**功能：** 表示文本段落在水平方向的对齐方式。

**类型：** [TextAlign](./cj-common-types.md#enum-textalign)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var margin

```cangjie
public var margin: Option<Length>
```

**功能：** 表示外边距。

**类型：** Option\<[Length](./cj-common-types.md#interface-length)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var placeholder

```cangjie
public var placeholder: Option<LeadingMarginPlaceholder>
```

**功能：** 表示文本段落缩进。

**类型：** Option\<[LeadingMarginPlaceholder](#class-leadingmarginplaceholder)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### init(TextAlign)

```cangjie
public init(textAlign!: TextAlign = TextAlign.Start)
```

**功能：** 创建RichEditorParagraphStyle类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
| :--- | :--- | :--- | :--- | :--- |
| textAlign | [TextAlign](./cj-common-types.md#enum-textalign) | 否 | TextAlign.Start | **命名参数。**  文本段落在水平方向的对齐方式。 |

#### init(TextAlign, Length)

```cangjie
public init(textAlign!: TextAlign = TextAlign.Start, leadingMargin!: Length)
```

**功能：** 创建RichEditorParagraphStyle类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
| :--- | :--- | :--- | :--- | :--- |
| textAlign | [TextAlign](./cj-common-types.md#enum-textalign) | 否 | TextAlign.Start | **命名参数。**  文本段落在水平方向的对齐方式。 |
| leadingMargin | [Length](./cj-common-types.md#interface-length) | 是 | - | **命名参数。**  文本段落缩进，不支持设置百分比。 |

#### init(TextAlign, LeadingMarginPlaceholder)

```cangjie
public init(textAlign!: TextAlign = TextAlign.Start, leadingMargin!: LeadingMarginPlaceholder)
```

**功能：** 创建RichEditorParagraphStyle类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

| 参数名 | 类型 | 必填 | 默认值 | 说明 |
| :--- | :--- | :--- | :--- | :--- |
| textAlign | [TextAlign](./cj-common-types.md#enum-textalign) | 否 | TextAlign.Start | **命名参数。**  文本段落在水平方向的对齐方式。 |
| leadingMargin | [LeadingMarginPlaceholder](#class-leadingmarginplaceholder) | 是 | - | **命名参数。**  文本段落缩进，不支持设置百分比。 |