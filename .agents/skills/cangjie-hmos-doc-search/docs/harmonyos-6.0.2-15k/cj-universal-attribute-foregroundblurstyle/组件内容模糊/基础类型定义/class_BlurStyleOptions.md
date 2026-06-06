### class BlurStyleOptions

```cangjie
public open class BlurStyleOptions {
    public BlurStyleOptions (
        public let adaptiveColor: AdaptiveColor,
        public let blurOptions: BlurOptions,
        public let colorMode: ThemeColorMode,
        public let scale: Float32
    )
}
```

**功能：** 内容模糊选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### let adaptiveColor

```cangjie
public let adaptiveColor: AdaptiveColor = AdaptiveColor.DEFAULT
```

**功能：** 内容模糊效果使用的取色模式。

**类型：** [AdaptiveColor](./cj-common-types.md#enum-adaptivecolor)

**读写能力：** 只读

**起始版本：** 19

#### let blurOptions

```cangjie
public let blurOptions: BlurOptions = BlurOptions([0.0, 0.0])
```

**功能：** 灰阶模糊参数。

**类型：** [BlurOptions](./cj-universal-attribute-foregroundblurstyle.md#class-bluroptions)

**读写能力：** 只读

**起始版本：** 19

#### let colorMode

```cangjie
public let colorMode: ThemeColorMode = hemeColorMode.SYSTEM
```

**功能：** 内容模糊效果使用的深浅色模式。

**类型：** [ThemeColorMode](./cj-common-types.md#enum-themecolormode)

**读写能力：** 只读

**起始版本：** 19

#### let scale

```cangjie
public let scale: Float32
```

**功能：** 内容模糊效果程度。取值范围：[0.0, 1.0]。

**类型：** Float32

**读写能力：** 只读

**起始版本：** 19

#### BlurStyleOptions(ThemeColorMode, AdaptiveColor, BlurOptions, Float32)

```cangjie
public BlurStyleOptions (
    public let colorMode: ThemeColorMode,
    public let adaptiveColor: AdaptiveColor,
    public let blurOptions: BlurOptions,
    public let scale: Float32
)
```

**功能：** 构造一个BlurStyleOptions类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
| :---- | :---- | :---- | :---- | :--- |
| colorMode | [ThemeColorMode](./cj-common-types.md#enum-themecolormode) | 是 | - | 内容模糊效果使用的深浅色模式。<br>初始值：ThemeColorMode.SYSTEM。 |
| adaptiveColor | [AdaptiveColor](./cj-common-types.md#enum-adaptivecolor) | 是 | - | 内容模糊效果使用的取色模式。<br>初始值：AdaptiveColor.DEFAULT。 |
| blurOptions | [BlurOptions](./cj-universal-attribute-foregroundblurstyle.md#class-bluroptions) | 是 | - | 灰阶模糊参数。<br>初始值：BlurOptions([0.0, 0.0])。 |
| scale | Float32 | 是 | - | 内容模糊效果程度。<br>取值范围：[0.0, 1.0]。<br>初始值：1.0。 |