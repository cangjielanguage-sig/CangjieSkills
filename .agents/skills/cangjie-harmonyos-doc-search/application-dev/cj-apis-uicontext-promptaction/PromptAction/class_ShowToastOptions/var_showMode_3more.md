### var showMode

```cangjie
public var showMode: ToastShowMode
```

**功能：** 确定Toast的显示模式。

**类型：** [ToastShowMode](#enum-toastshowmode)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var textColor

```cangjie
public var textColor: ResourceColor
```

**功能：** Toast的文本颜色。

**类型：** [ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(ResourceStr, UInt32, Length, ToastShowMode, Alignment, Offset, Color, Color, BlurStyle, ?ShadowOptions, Bool, HoverModeAreaType)

```cangjie
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
```

**功能：** Toast显示选项构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|message|[ResourceStr](./cj-common-types.md#interface-resourcestr)|是|-| **命名参数。** 要显示的文本。|
|duration|UInt32|否|1500| **命名参数。** Toast对话框的持续时间。|
|bottom|[Length](./cj-common-types.md#interface-length)|否|80.vp| **命名参数。** Toast对话框与屏幕底部的距离。|
|showMode|[ToastShowMode](#enum-toastshowmode)|否|ToastShowMode.Default| **命名参数。** Toast的显示模式。|
|alignment|[Alignment](./cj-common-types.md#enum-alignment)|否|Alignment.Bottom| **命名参数。** Toast在屏幕上的对齐方式。|
|offset|[Offset](./cj-common-types.md#class-offset)|否|Offset(0.vp, 0.vp)| **命名参数。** Toast偏移量。|
|backgroundColor|[Color](./cj-common-types.md#class-color)|否|Color.Transparent| **命名参数。** Toast的背景颜色。|
|textColor|[Color](./cj-common-types.md#class-color)|否|Color.Black| **命名参数。** Toast的文本颜色。|
|backgroundBlurStyle|[BlurStyle](./cj-common-types.md#enum-blurstyle)|否|BlurStyle.ComponentUltraThick| **命名参数。** Toast的背景模糊样式。|
|shadow|?[ShadowOptions](./cj-common-types.md#class-shadowoptions)|否|None| **命名参数。** Toast的阴影选项。|
|enableHoverMode|Bool|否|false| **命名参数。** 是否响应悬停模式。|
|hoverModeArea|[HoverModeAreaType](#enum-hovermodeareatype)|否|HoverModeAreaType.BottomScreen| **命名参数。** 悬停模式下Toast的显示区域。|