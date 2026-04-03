### class RichEditorSymbolSpanStyleResult

```cangjie
public class RichEditorSymbolSpanStyleResult {
    public var fontColor: String = ""
    public var fontSize: Float64 = 0.0
    public var fontWeight: FontWeight = FontWeight.Normal
    public var renderingStrategy: SymbolRenderingStrategy = SymbolRenderingStrategy.SINGLE
    public var effectStrategy: SymbolEffectStrategy = SymbolEffectStrategy.NONE
}
```

**功能：** 后端返回的SymbolSpan样式信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var fontColor

```cangjie
public var fontColor: String = ""
```

**功能：** 表示SymbolSpan组件颜色。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var fontSize

```cangjie
public var fontSize: Float64 = 0.0
```

**功能：** 表示SymbolSpan组件大小。单位：fp。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var fontWeight

```cangjie
public var fontWeight: FontWeight = FontWeight.Normal
```

**功能：** 表示SymbolSpan组件粗细。

**类型：** [FontWeight](./cj-common-types.md#enum-fontweight)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var renderingStrategy

```cangjie
public var renderingStrategy: SymbolRenderingStrategy = SymbolRenderingStrategy.SINGLE
```

**功能：** 表示SymbolSpan组件渲染策略。

**类型：** [SymbolRenderingStrategy](./cj-text-input-symbolglyph.md#enum-symbolrenderingstrategy)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var effectStrategy

```cangjie
public var effectStrategy: SymbolEffectStrategy = SymbolEffectStrategy.NONE
```

**功能：** 表示SymbolSpan组件动效策略。

**类型：** [SymbolEffectStrategy](./cj-text-input-symbolglyph.md#enum-symboleffectstrategy)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19