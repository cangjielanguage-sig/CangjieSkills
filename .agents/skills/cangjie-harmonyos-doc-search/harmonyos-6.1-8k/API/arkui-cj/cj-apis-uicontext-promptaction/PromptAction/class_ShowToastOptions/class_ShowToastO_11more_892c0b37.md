## class ShowToastOptions

```cangjie
public class ShowToastOptions {
    public var message: ResourceStr
    public var duration: UInt32
    public var bottom: Length
    public var showMode: ToastShowMode
    public var alignment: Alignment
    public var offset: Offset
    public var backgroundColor: ResourceColor
    public var textColor: ResourceColor
    public var backgroundBlurStyle: BlurStyle
    public var shadow: ?ShadowOptions = None
    public var enableHoverMode: Bool
    public var hoverModeArea: HoverModeAreaType
    public init(
        message!: ResourceStr,
        duration!: UInt32 = 1500,
        bottom!: Length = 80.vp,
        showMode!: ToastShowMode = ToastShowMode.Default,
        alignment!: Alignment = Alignment.Bottom,
        offset!: Offset = Offset(0.vp, 0.vp),
        backgroundColor!: Color = Color.Transparent,
        textColor!: Color = Color.Black,
        backgroundBlurStyle!: BlurStyle = BlurStyle.ComponentUltraThick,
        shadow!: ?ShadowOptions = None,
        enableHoverMode!: Bool = false,
        hoverModeArea!: HoverModeAreaType = HoverModeAreaType.BottomScreen
    )
}
```

**功能：** Toast显示选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var alignment

```cangjie
public var alignment: Alignment
```

**功能：** Toast在屏幕上的对齐方式。

**类型：** [Alignment](./cj-common-types.md#enum-alignment)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var backgroundColor

```cangjie
public var backgroundColor: ResourceColor
```

**功能：** Toast的背景颜色。

**类型：** [ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var bottom

```cangjie
public var bottom: Length
```

**功能：** Toast对话框与屏幕底部的距离。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var duration

```cangjie
public var duration: UInt32
```

**功能：** Toast对话框的持续时间。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var enableHoverMode

```cangjie
public var enableHoverMode: Bool
```

**功能：** 是否响应悬停模式。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var hoverModeArea

```cangjie
public var hoverModeArea: HoverModeAreaType
```

**功能：** 悬停模式下Toast的显示区域。

**类型：** [HoverModeAreaType](#enum-hovermodeareatype)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var message

```cangjie
public var message: ResourceStr
```

**功能：** 要显示的文本。

**类型：** [ResourceStr](./cj-common-types.md#interface-resourcestr)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var offset

```cangjie
public var offset: Offset
```

**功能：** Toast偏移量。

**类型：** [Offset](./cj-common-types.md#class-offset)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var backgroundBlurStyle

```cangjie
public var backgroundBlurStyle: BlurStyle
```

**功能：** Toast的背景模糊样式。

**类型：** [BlurStyle](./cj-common-types.md#enum-blurstyle)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var shadow

```cangjie
public var shadow: ?ShadowOptions = None
```

**功能：** Toast的阴影选项。

**类型：** ?[ShadowOptions](./cj-common-types.md#class-shadowoptions)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22