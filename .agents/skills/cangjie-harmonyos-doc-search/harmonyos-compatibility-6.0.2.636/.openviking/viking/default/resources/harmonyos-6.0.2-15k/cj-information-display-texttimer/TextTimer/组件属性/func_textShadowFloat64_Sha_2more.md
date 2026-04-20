### func textShadow(Float64, ShadowType, Float64, Float64, Color, Bool)

```cangjie
public func textShadow(
    radius!: Float64,
    shadowType!: ShadowType = ShadowType.COLOR,
    offsetX!: Float64 = 0.0,
    offsetY!: Float64 = 0.0,
    color!: Color = Color.BLACK,
    fill!: Bool = false
): This
```

**功能：** 设置文字阴影效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|radius|Float64|是|-| **命名参数。** 阴影模糊半径。<br/>取值范围：[0, +∞)<br/>单位：px<br/>说明：<br/>设置小于0的值时，按值为0处理。<br/>如需使用vp单位的数值可用[vp2px](./cj-common-pixelunits.md#func-vp2pxlength)进行转换。|
|shadowType|[ShadowType](./cj-common-types.md#enum-shadowtype)|否|ShadowType.COLOR| **命名参数。** 阴影类型。|
|offsetX|Float64|否|0.0| **命名参数。** 阴影的X轴偏移量。<br/>单位：px。<br/>如需使用vp单位的数值可用[vp2px](./cj-common-pixelunits.md#func-vp2pxlength)进行转换。|
|offsetY|Float64|否|0.0| **命名参数。** 阴影的Y轴偏移量。<br/>单位：px。<br/>如需使用vp单位的数值可用[vp2px](./cj-common-pixelunits.md#func-vp2pxlength)进行转换。|
|color|[Color](./cj-common-types.md#class-color)|否|Color.BLACK| **命名参数。** 阴影的颜色。|
|fill|Bool|否|false| **命名参数。** 阴影是否内部填充。|

### func textShadow(Float64, ShadowType, Float64, Float64, UInt32, Bool)

```cangjie
public func textShadow(
    radius!: Float64,
    shadowType!: ShadowType = ShadowType.COLOR,
    offsetX!: Float64 = 0.0,
    offsetY!: Float64 = 0.0,
    color!: UInt32,
    fill!: Bool = false
): This
```

**功能：** 设置文字阴影效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|radius|Float64|是|-| **命名参数。** 阴影模糊半径。<br/>取值范围：[0, +∞)<br/>单位：px<br/>说明：<br/>设置小于0的值时，按值为0处理。<br/>如需使用vp单位的数值可用[vp2px](./cj-common-pixelunits.md#func-vp2pxlength)进行转换。|
|shadowType|[ShadowType](./cj-common-types.md#enum-shadowtype)|否|ShadowType.COLOR| **命名参数。** 阴影类型。|
|offsetX|Float64|否|0.0| **命名参数。** 阴影的X轴偏移量。<br/>单位：px。<br/>如需使用vp单位的数值可用[vp2px](./cj-common-pixelunits.md#func-vp2pxlength)进行转换。|
|offsetY|Float64|否|0.0| **命名参数。** 阴影的Y轴偏移量。<br/>单位：px。<br/>如需使用vp单位的数值可用[vp2px](./cj-common-pixelunits.md#func-vp2pxlength)进行转换。|
|color|UInt32|是|-| **命名参数。** 阴影的颜色。|
|fill|Bool|否|false| **命名参数。** 阴影是否内部填充。|