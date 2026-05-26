#### init(AdaptiveColor, BlurOptions, Float64, Color, Color, BlurStyleActivePolicy, Float64, Float64)

```cangjie
public init(adaptiveColor!: AdaptiveColor = AdaptiveColor.DEFAULT, blurOptions!: BlurOptions = BlurOptions([0.0, 0.0]), brightness!: Float64 = 1.0, color!: Color = Color.TRANSPARENT, inactiveColor!: Color = Color.TRANSPARENT, policy!: BlurStyleActivePolicy = BlurStyleActivePolicy.ALWAYS_ACTIVE, radius!: Float64, saturation!: Float64 = 1.0)  
```

**功能：** 构造一个BackgroundEffectOptions类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|adaptiveColor|[AdaptiveColor](./cj-common-types.md#enum-adaptivecolor)|否|AdaptiveColor.DEFAULT| **命名参数。** 背景模糊效果使用的取色模式,默认为DEFAULT。使用AVERAGE时color必须带有透明度，取色模式才生效。|
|blurOptions|[BlurOptions](./cj-universal-attribute-foregroundblurstyle.md#class-bluroptions)|否|BlurOptions([0.0, 0.0])| **命名参数。** 灰阶模糊参数。|
|brightness|Float64|否|1.0| **命名参数。** 亮度，取值范围：[0, +∞)，推荐取值范围：[0, 2]。|
|color|[Color](./cj-common-types.md#color)|否|Color.TRANSPARENT| **命名参数。** 颜色。|
|inactiveColor|[Color](./cj-common-types.md#color)|否| Color.TRANSPARENT| **命名参数。** 窗口失焦后，窗口内控件模糊效果会被移除，则使用inactiveColor作为控件背板颜色。|
|policy|[BlurStyleActivePolicy](./cj-common-types.md#enum-blurstyleactivepolicy)|否|BlurStyleActivePolicy.ALWAYS_ACTIVE| **命名参数。** 内模糊激活策略。|
|radius|Float64|是|-| **命名参数。** 模糊半径，取值范围：[0, +∞)。<br>初始值：0.0。|
|saturation|Float64|否|1.0| **命名参数。** 饱和度，取值范围：[0, +∞)，推荐取值范围：[0, 50]。|