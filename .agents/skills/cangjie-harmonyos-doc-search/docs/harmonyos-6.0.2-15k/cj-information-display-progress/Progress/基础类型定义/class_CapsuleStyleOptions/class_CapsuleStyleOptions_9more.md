### class CapsuleStyleOptions

```cangjie
public class CapsuleStyleOptions {
    public var content: String
    public var font: Fonts
    public var borderWidth: Length
    public var borderColor: ResourceColor
    public var fontColor: ResourceColor
    public var showDefaultPercentage: Bool
    public var enableSmoothEffect: Bool
    public var enableScanEffect: Bool
    public init(content!: String = "HarmonyOS Sans", font!: Fonts = Fonts(), borderWidth!: Length = 1.vp,
        borderColor!: ResourceColor = Color(0x33007dff), fontColor!: ResourceColor = Color(0xff182431), showDefaultPercentage!: Bool = false,
        enableSmoothEffect!: Bool = true, enableScanEffect!: Bool = false)
}
```

**功能：** Capsule的样式参数类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var borderColor

```cangjie
public var borderColor: ResourceColor
```

**功能：** 内描边颜色。

**类型：** [ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var borderWidth

```cangjie
public var borderWidth: Length
```

**功能：** 内描边宽度（不支持百分比设置）。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var content

```cangjie
public var content: String
```

**功能：** 文本内容，应用可自定义。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var enableScanEffect

```cangjie
public var enableScanEffect: Bool
```

**功能：** 扫光效果的开关。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var enableSmoothEffect

```cangjie
public var enableSmoothEffect: Bool
```

**功能：** 进度平滑动效的开关。开启平滑动效后设置进度，进度会从当前值渐变至设定值，否则进度从当前值突变至设定值。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var font

```cangjie
public var font: Fonts
```

**功能：** 文本样式。

**类型：** [Fonts](./cj-common-types.md#class-fonts)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var fontColor

```cangjie
public var fontColor: ResourceColor
```

**功能：** 文本颜色。

**类型：** [ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var showDefaultPercentage

```cangjie
public var showDefaultPercentage: Bool
```

**功能：** 显示百分比文本的开关，开启后会在进度条上显示当前进度的百分比。设置了content属性时该属性不生效。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19