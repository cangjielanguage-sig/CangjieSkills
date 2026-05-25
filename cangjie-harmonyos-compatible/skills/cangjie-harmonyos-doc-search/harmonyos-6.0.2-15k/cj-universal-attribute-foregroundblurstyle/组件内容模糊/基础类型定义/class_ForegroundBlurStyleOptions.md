### class ForegroundBlurStyleOptions

```cangjie
public class ForegroundBlurStyleOptions {
    public ForegroundBlurStyleOptions(
        public var adaptiveColor!: AdaptiveColor = DEFAULT,
        public var blurOptions!: BlurOptions = BlurOptions([0.0, 0.0]),
        public var colorMode!: ThemeColorMode = SYSTEM,
        public var scale!: Float32 = 1.0
    )
}
```

**功能：** 内容模糊选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var adaptiveColor

```cangjie
public var adaptiveColor: AdaptiveColor = DEFAULT
```

**功能：** 内容模糊效果使用的取色模式。

**类型：** [AdaptiveColor](./cj-common-types.md#enum-adaptivecolor)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var blurOptions

```cangjie
public var blurOptions: BlurOptions = BlurOptions([0.0, 0.0])
```

**功能：** 灰阶模糊参数。

**类型：** [BlurOptions](./cj-universal-attribute-foregroundblurstyle.md#class-bluroptions)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var colorMode

```cangjie
public var colorMode: ThemeColorMode = SYSTEM
```

**功能：** 内容模糊效果使用的深浅色模式。

**类型：** [ThemeColorMode](./cj-common-types.md#enum-themecolormode)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var scale

```cangjie
public var scale: Float32 = 1.0
```

**功能：** 内容模糊效果程度。取值范围：[0.0, 1.0]。

**类型：** Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### ForegroundBlurStyleOptions(ThemeColorMode, AdaptiveColor, BlurOptions, Float32)

```cangjie
public ForegroundBlurStyleOptions(public var adaptiveColor!: AdaptiveColor = DEFAULT, public var blurOptions!: BlurOptions = BlurOptions([0.0, 0.0]), public var colorMode!: ThemeColorMode = SYSTEM, public var scale!: Float32 = 1.0)
```

**功能：** 构造一个ForegroundBlurStyleOptions类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|名称|类型|必填|默认值|说明|
| :---- | :---- | :---- | :---- | :--- |
| adaptiveColor | [AdaptiveColor](./cj-common-types.md#enum-adaptivecolor) | 否 | AdaptiveColor.DEFAULT | **命名参数。**  内容模糊效果使用的取色模式。 |
| blurOptions | [BlurOptions](./cj-universal-attribute-foregroundblurstyle.md#class-bluroptions) | 否 | BlurOptions([0.0, 0.0]) | **命名参数。**  灰阶模糊参数。 |
| colorMode | [ThemeColorMode](./cj-common-types.md#enum-themecolormode) | 否 | ThemeColorMode.SYSTEM | **命名参数。**  内容模糊效果使用的深浅色模式。 |
| scale | Float32 | 否 | 1.0 | **命名参数。**  内容模糊效果程度。<br>取值范围：[0.0, 1.0]。 |