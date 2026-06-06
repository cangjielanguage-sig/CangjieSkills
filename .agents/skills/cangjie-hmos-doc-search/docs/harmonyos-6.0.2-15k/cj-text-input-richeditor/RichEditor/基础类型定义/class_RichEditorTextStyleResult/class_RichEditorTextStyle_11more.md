### class RichEditorTextStyleResult

```cangjie
public class RichEditorTextStyleResult {
    public var fontColor: String
    public var fontSize: Float64
    public var fontStyle: FontStyle
    public var fontWeight: Int32
    public var fontFamily: String
    public var decoration: TextDecorationResult
    public var textShadow: Array<ShadowOptionsResult> = []
    public var lineHeight: Float64 = 0.0
    public var letterSpacing: Float64 = 0.0
    public var fontFeature: String = ""

    public init(
        fontColor: String,
        fontSize: Float64,
        fontStyle: FontStyle,
        fontWeight: Int32,
        fontFamily: String,
        decoration: TextDecorationResult
    )
    public init(
        fontColor: String,
        fontSize: Float64,
        fontStyle: FontStyle,
        fontWeight: Int32,
        fontFamily: String,
        decoration: TextDecorationResult,
        textShadow: Array<ShadowOptionsResult>,
        lineHeight: Float64,
        letterSpacing: Float64,
        fontFeature: String
    )
}
```

**功能：** 后端返回的文本样式信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var decoration

```cangjie
public var decoration: TextDecorationResult
```

**功能：** 表示文本装饰线样式及其颜色。

**类型：** [TextDecorationResult](#class-textdecorationresult)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var fontColor

```cangjie
public var fontColor: String
```

**功能：** 表示文本颜色。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var fontFamily

```cangjie
public var fontFamily: String
```

**功能：** 表示字体列表。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var fontSize

```cangjie
public var fontSize: Float64
```

**功能：** 表示字体大小。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var fontStyle

```cangjie
public var fontStyle: FontStyle
```

**功能：** 表示字体样式。

**类型：** [FontStyle](./cj-common-types.md#enum-fontstyle)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var fontWeight

```cangjie
public var fontWeight: Int32
```

**功能：** 表示字体粗细。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### let fontFeature

```cangjie
public var fontFeature: String = ""
```

**功能：** 表示文本字符间距。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let letterSpacing

```cangjie
public var letterSpacing: Float64 = 0.0
```

**功能：** 表示文本字符间距。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let lineHeight

```cangjie
public var lineHeight: Float64 = 0.0
```

**功能：** 表示文本行高。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let textShadow

```cangjie
public var textShadow: Array<ShadowOptionsResult> = []
```

**功能：** 表示文字阴影效果。

**类型：** Array\<[ShadowOptionsResult](#class-shadowoptionsresult)>

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19