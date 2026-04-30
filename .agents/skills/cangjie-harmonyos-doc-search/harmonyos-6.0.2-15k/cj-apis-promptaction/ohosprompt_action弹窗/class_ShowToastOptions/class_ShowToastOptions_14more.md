## class ShowToastOptions

```cangjie
public class ShowToastOptions {
    public ShowToastOptions(
        public let message!: String = 'ShowToast',
        public let duration!: UInt32 = 1500,
        public let bottom!: String = '80vp',
        public let showMode!: ToastShowMode = ToastShowMode.Default,
        public let alignment!: Alignment = Alignment.Bottom,
        public let offset!: Offset = Offset(0.vp, 0.vp),
        public let backgroundColor!: Color = Color.TRANSPARENT,
        public let textColor!: Color = Color.BLACK,
        public let backgroundBlurStyle!: BlurStyle = BlurStyle.COMPONENT_ULTRA_THICK,
        public let shadowOption!: Option<ShadowOptions> = Option.None,
        public let shadowStyle!: Option<ShadowStyle> = Option.None,
        public let enableHoverMode!: Bool = false,
        public let hoverModeArea!: HoverModeAreaType = HoverModeAreaType.BOTTOM_SCREEN
    )
}
```

**功能：** 文本提示框的选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let message

```cangjie
public let message: String = "ShowToast"
```

**功能：** 表示显示的文本信息。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let duration

```cangjie
public let duration: UInt32 = 1500
```

**功能：** 表示弹窗持续时间。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 19

### let bottom

```cangjie
public let bottom: String = "80vp"
```

**功能：** 表示弹窗底部边框距离导航条的高度。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let showMode

```cangjie
public let showMode: ToastShowMode = ToastShowMode.Default
```

**功能：** 表示弹窗是否显示在应用之上。

**类型：** [ToastShowMode](#enum-toastshowmode)

**读写能力：** 只读

**起始版本：** 19

### let alignment

```cangjie
public let alignment: Alignment = Alignment.Bottom
```

**功能：** 表示弹窗对齐方式。

**类型：** [Alignment](./cj-common-types.md#enum-alignment)

**读写能力：** 只读

**起始版本：** 19

### let offset

```cangjie
public let offset: Offset = Offset(0.vp, 0.vp)
```

**功能：** 表示弹窗在对齐方式上的偏移。

**类型：** [Offset](./cj-common-types.md#class-offset)

**读写能力：** 只读

**起始版本：** 19

### let backgroundColor

```cangjie
public let backgroundColor: Color = Color.TRANSPARENT
```

**功能：** 表示文本提示框背板颜色。

**类型：** [Color](./cj-common-types.md#class-color)

**读写能力：** 只读

**起始版本：** 19

### let textColor

```cangjie
public let textColor: Color = Color.BLACK
```

**功能：** 表示文本提示框文本颜色。

**类型：** [Color](./cj-common-types.md#class-color)

**读写能力：** 只读

**起始版本：** 19

### let backgroundBlurStyle

```cangjie
public let backgroundBlurStyle: BlurStyle = BlurStyle.COMPONENT_ULTRA_THICK
```

**功能：** 表示文本提示框背板模糊材质。

**类型：** [BlurStyle](./cj-universal-attribute-background.md#enum-blurstyle)

**读写能力：** 只读

**起始版本：** 19

### let shadowOption

```cangjie
public let shadowOption: Option<ShadowOptions> = Option.None
```

**功能：** 表示文本提示框背板阴影。

**类型：** Option\<[ShadowOptions](./cj-text-input-text.md#class-shadowoptions)>

**读写能力：** 只读

**起始版本：** 19

### let shadowStyle

```cangjie
public let shadowStyle: Option<ShadowStyle> = Option.None
```

**功能：** 表示文本提示框背板阴影。

**类型：** Option\<[ShadowStyle](#enum-shadowstyle)>

**读写能力：** 只读

**起始版本：** 19

### let enableHoverMode

```cangjie
public let enableHoverMode: Bool = false
```

**功能：** 表示弹窗是否响应悬停态。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let hoverModeArea

```cangjie
public let hoverModeArea: HoverModeAreaType = HoverModeAreaType.BOTTOM_SCREEN
```

**功能：** 表示响应悬停态时，弹窗的显示区域。

**类型：** [HoverModeAreaType](#enum-hovermodeareatype)

**读写能力：** 只读

**起始版本：** 19