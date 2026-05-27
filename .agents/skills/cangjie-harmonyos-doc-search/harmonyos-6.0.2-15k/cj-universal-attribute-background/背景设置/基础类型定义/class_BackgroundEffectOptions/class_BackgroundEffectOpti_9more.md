### class BackgroundEffectOptions

```cangjie
public class BackgroundEffectOptions {
    public let adaptiveColor: AdaptiveColor
    public let blurOptions: BlurOptions
    public let brightness: Float64
    public let color: Color
    public let inactiveColor: Color
    public let policy: BlurStyleActivePolicy
    public let radius: Float64
    public let saturation: Float64
    public init(
        adaptiveColor!: AdaptiveColor = AdaptiveColor.DEFAULT,
        blurOptions!: BlurOptions = BlurOptions([0.0, 0.0]),
        brightness!: Float64 = 1.0,
        color!: Color = Color.TRANSPARENT,
        inactiveColor!: Color = Color.TRANSPARENT,
        policy!: BlurStyleActivePolicy = BlurStyleActivePolicy.ALWAYS_ACTIVE,
        radius!: Float64,
        saturation!: Float64 = 1.0
        )
}
```

**功能：** 背景效果参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let adaptiveColor

```cangjie
public let adaptiveColor: AdaptiveColor
```

**功能：** 背景模糊效果使用的取色模式，默认为DEFAULT。使用AVERAGE时color必须带有透明度，取色模式才生效。

**类型：** [AdaptiveColor](./cj-common-types.md#enum-adaptivecolor)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let blurOptions

```cangjie
public let blurOptions: BlurOptions
```

**功能：** 灰阶模糊参数。

**类型：** [BlurOptions](./cj-universal-attribute-foregroundblurstyle.md#class-bluroptions)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let brightness

```cangjie
public let brightness: Float64
```

**功能：** 亮度，取值范围：[0, +∞)。推荐取值范围：[0, 2]。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let color

```cangjie
public let color: Color
```

**功能：** 颜色。

**类型：** [Color](./cj-common-types.md#color)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let inactiveColor

```cangjie
public let inactiveColor: Color
```

**功能：** 窗口失焦后，窗口内控件模糊效果会被移除，则使用inactiveColor作为控件背板颜色。

**类型：** [Color](./cj-common-types.md#color)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let policy

```cangjie
public let policy: BlurStyleActivePolicy
```

**功能：** 模糊激活策略。

**类型：** [BlurStyleActivePolicy](./cj-universal-attribute-background.md#enum-blurstyleactivepolicy)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let radius

```cangjie
public let radius: Float64
```

**功能：** 模糊半径，取值范围：[0, +∞)。初始值为0.0。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let saturation

```cangjie
public let saturation: Float64
```

**功能：** 饱和度，取值范围：[0, +∞)。推荐取值范围：[0, 50]。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19