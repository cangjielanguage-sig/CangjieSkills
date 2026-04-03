### class BackgroundBlurStyleOptions

```cangjie
public class BackgroundBlurStyleOptions <: BlurStyleOptions {
    public let inactiveColor: Color
    public let policy: BlurStyleActivePolicy
    public init(
        colorMode!: ThemeColorMode = ThemeColorMode.SYSTEM,
        adaptiveColor!: AdaptiveColor = AdaptiveColor.DEFAULT,
        blurOptions!: BlurOptions = BlurOptions([0.0, 0.0]),
        scale!: Float32 = 1.0,
        policy!: BlurStyleActivePolicy = BlurStyleActivePolicy.ALWAYS_ACTIVE,
        inactiveColor!: ResourceColor = Color.TRANSPARENT
    )
}
```

**功能：** 背景模糊选项类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**父类型：**

- [BlurStyleOptions](./cj-universal-attribute-foregroundblurstyle.md#class-blurstyleoptions)

#### let inactiveColor

```cangjie
public let inactiveColor: ResourceColor
```

**功能：** 窗口失焦后，窗口内控件模糊效果会被移除，则使用inactiveColor作为控件背板颜色。

**类型：** [ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let policy

```cangjie
public let policy: BlurStyleActivePolicy
```

**功能：** 模糊激活策略。

**类型：** [BlurStyleActivePolicy](./cj-common-types.md#enum-blurstyleactivepolicy)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### init(ThemeColorMode, AdaptiveColor, BlurOptions, Float32, BlurStyleActivePolicy, ResourceColor)

```cangjie
public init(colorMode!: ThemeColorMode, adaptiveColor!: AdaptiveColor,
blurOptions!: BlurOptions, scale!: Float32, policy!: BlurStyleActivePolicy, inactiveColor!: ResourceColor)
```

**功能：** 构造一个BackgroundBlurStyleOptions类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|colorMode|[ThemeColorMode](./cj-common-types.md#enum-themecolormode)|否|ThemeColorMode.SYSTEM|**命名参数。** 内容模糊效果使用的深浅色模式。|
|adaptiveColor|[AdaptiveColor](./cj-common-types.md#enum-adaptivecolor)|否|AdaptiveColor.DEFAULT| **命名参数。** 内容模糊效果使用的取色模式。|
|blurOptions|[BlurOptions](./cj-universal-attribute-foregroundblurstyle.md#class-bluroptions)|否|BlurOptions([0.0, 0.0])| **命名参数。** 灰阶模糊参数。|
|scale|Float32|否|1.0| **命名参数。** 内容模糊效果程度。|
|policy|[BlurStyleActivePolicy](./cj-common-types.md#enum-blurstyleactivepolicy)|否|BlurStyleActivePolicy.ALWAYS_ACTIVE| **命名参数。** 内模糊激活策略。|
|inactiveColor|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|Color.TRANSPARENT| **命名参数。** 窗口失焦后，窗口内控件模糊效果会被移除，则使用inactiveColor作为控件背板颜色。|