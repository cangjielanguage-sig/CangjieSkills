### var offset

```cangjie
public var offset: Offset
```

**功能：** 对话框偏移量。

**类型：** [Offset](./cj-common-types.md#class-offset)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var shadow

```cangjie
public var shadow: ?ShadowOptions
```

**功能：** 对话框的阴影选项。

**类型：** ?[ShadowOptions](./cj-common-types.md#class-shadowoptions)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var showInSubWindow

```cangjie
public var showInSubWindow: Bool
```

**功能：** 是否在子窗口中显示。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var title

```cangjie
public var title: ResourceStr
```

**功能：** 要显示的标题文本。

**类型：** [ResourceStr](./cj-common-types.md#interface-resourcestr)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(ResourceStr, ResourceStr, Array\<ButtonInfo\>, DialogAlignment, Offset, Rectangle, Bool, Bool, Color, BlurStyle, ?ShadowOptions, Bool, HoverModeAreaType)

```cangjie
public init(
    title!: ResourceStr = '',
    message!: ResourceStr = '',
    buttons!: Array<ButtonInfo> = [],
    alignment!: DialogAlignment = DialogAlignment.Default,
    offset!: Offset = Offset(0.vp, 0.vp),
    maskRect!: Rectangle = Rectangle(x: 0.vp, y: 0.vp, width: 100.percent, height: 100.percent),
    showInSubWindow!: Bool = false,
    isModal!: Bool = true,
    backgroundColor!: Color = Color.Transparent,
    backgroundBlurStyle!: BlurStyle = BlurStyle.ComponentUltraThick,
    shadow!: ?ShadowOptions = None,
    enableHoverMode!: Bool = false,
    hoverModeArea!: HoverModeAreaType = HoverModeAreaType.BottomScreen
)
```

**功能：** 对话框显示选项构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|title|[ResourceStr](./cj-common-types.md#interface-resourcestr)|否|''| **命名参数。** 标题文本。|
|message|[ResourceStr](./cj-common-types.md#interface-resourcestr)|否|''| **命名参数。** 文本主体。|
|buttons|Array\<[ButtonInfo](#class-buttoninfo)>|否|[]| **命名参数。** 对话框中的按钮数组。|
|alignment|[DialogAlignment](./cj-common-types.md#enum-dialogalignment)|否|DialogAlignment.Default| **命名参数。** 对话框在屏幕上的对齐方式。|
|offset|[Offset](./cj-common-types.md#class-offset)|否|Offset(0.vp, 0.vp)| **命名参数。** 对话框偏移量。|
|maskRect|[Rectangle](./cj-common-types.md#class-rectangle)|否|Rectangle(x: 0.vp, y: 0.vp, width: 100.percent, height: 100.percent)| **命名参数。** 对话框遮罩区域。|
|showInSubWindow|Bool|否|false| **命名参数。** 是否在子窗口中显示。|
|isModal|Bool|否|true| **命名参数。** 是否为模态对话框。|
|backgroundColor|[Color](./cj-common-types.md#class-color)|否|Color.Transparent| **命名参数。** 对话框的背景颜色。|
|backgroundBlurStyle|[BlurStyle](./cj-common-types.md#enum-blurstyle)|否|BlurStyle.ComponentUltraThick| **命名参数。** 对话框的背景模糊样式。|
|shadow|?[ShadowOptions](./cj-common-types.md#class-shadowoptions)|否|None| **命名参数。** 对话框的阴影选项。|
|enableHoverMode|Bool|否|false| **命名参数。** 是否响应悬停模式。|
|hoverModeArea|[HoverModeAreaType](#enum-hovermodeareatype)|否|HoverModeAreaType.BottomScreen| **命名参数。** 悬停模式下对话框的显示区域。|