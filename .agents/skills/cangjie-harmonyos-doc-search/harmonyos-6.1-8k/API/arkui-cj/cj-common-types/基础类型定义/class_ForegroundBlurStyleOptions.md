## class ForegroundBlurStyleOptions

```cangjie
public class ForegroundBlurStyleOptions {
    public var colorMode: ?ThemeColorMode
    public var adaptiveColor: ?AdaptiveColor
    public var blurOptions: ?BlurOptions
    public var scale: ?Float32
    public init(colorMode!: ?ThemeColorMode = None, adaptiveColor!: ?AdaptiveColor = None, blurOptions!: ?BlurOptions = None, scale!: ?Float32 = None)
}
```

**功能：** 内容模糊选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var colorMode

```cangjie
public var colorMode: ?ThemeColorMode
```

**功能：** 内容模糊效果使用的深浅色模式。

**类型：** ?[ThemeColorMode](#enum-themecolormode)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var adaptiveColor

```cangjie
public var adaptiveColor: ?AdaptiveColor
```

**功能：** 内容模糊效果使用的取色模式。

**类型：** ?[AdaptiveColor](#enum-adaptivecolor)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var blurOptions

```cangjie
public var blurOptions: ?BlurOptions
```

**功能：** 灰阶模糊参数。

**类型：** ?[BlurOptions](#class-bluroptions)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var scale

```cangjie
public var scale: ?Float32
```

**功能：** 内容模糊效果程度。取值范围：[0.0, 1.0]。

**类型：** ?Float32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### init(?ThemeColorMode, ?AdaptiveColor, ?BlurOptions, ?Float32)

```cangjie
public init(colorMode!: ?ThemeColorMode = None, adaptiveColor!: ?AdaptiveColor = None, blurOptions!: ?BlurOptions = None, scale!: ?Float32 = None)
```

**功能：** 构造一个ForegroundBlurStyleOptions类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|colorMode|?[ThemeColorMode](./cj-common-types.md#enum-themecolormode)|否|None|**命名参数。** 内容模糊效果使用的深浅色模式。初始值为ThemeColorMode.System。|
|adaptiveColor|?[AdaptiveColor](./cj-common-types.md#enum-adaptivecolor)|否|None|**命名参数。** 内容模糊效果使用的取色模式。初始值为AdaptiveColor.Default。|
|blurOptions|?[BlurOptions](#class-bluroptions)|否|None|**命名参数。** 灰阶模糊参数。初始值为BlurOptions([0.0, 0.0])。|
|scale|?Float32|否|None|**命名参数。** 内容模糊效果程度。<br>取值范围：[0.0, 1.0]。初始值为1.0。|