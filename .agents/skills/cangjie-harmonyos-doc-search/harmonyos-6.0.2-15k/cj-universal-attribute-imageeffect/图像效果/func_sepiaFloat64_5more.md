## func sepia(Float64)

```cangjie
public func sepia(value: Float64): This
```

**功能：** 将图像转换为深褐色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float64|是|\-|将图像转换为深褐色，降低色彩度，产生温暖复古的图像风格。入参为褐色滤镜强度，值为1则完全是深褐色的，值小于等于0则图像无变化，值大于1会进一步放大色彩偏移比例，图像整体会变得更亮且色彩更加偏黄/偏红，但不属于标准sepia效果。<br> 取值范围：[0.0, +∞)，推荐取值范围：(0.0, 1.0]。|

## func sepia(Int64)

```cangjie
public func sepia(value: Int64): This
```

**功能：** 将图像转换为深褐色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int64|是|\-|将图像转换为深褐色，降低色彩度，产生温暖复古的图像风格。入参为褐色滤镜强度，值为1则完全是深褐色的，值小于等于0则图像无变化，值大于1会进一步放大色彩偏移比例，图像整体会变得更亮且色彩更加偏黄/偏红，但不属于标准sepia效果。<br> 取值范围：[0, +∞)，推荐取值范围：(0, 1]。|

## func shadow(Float64, ResourceColor, Float64, Float64)

```cangjie
public func shadow(
    radius!: Float64,
    color!: ResourceColor = Color(0x666666),
    offsetX!: Float64 = 0.0,
    offsetY!: Float64 = 0.0
): This
```

**功能：** 为组件添加阴影效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|radius|Float64|是|\-| **命名参数。** 阴影模糊半径。<br>取值范围：[0, +∞)。<br>单位：px。<br>**说明：**<br> 设置小于0的值时，按值为0处理。|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|Color(0x666666)| **命名参数。** 阴影的颜色|
|offsetX|Float64|否|0.0| **命名参数。** 阴影的X轴偏移量。<br>单位：px。|
|offsetY|Float64|否|0.0| **命名参数。** 阴影的Y轴偏移量。<br>单位：px。|

## func shadow(Int64, ResourceColor, Int64, Int64)

```cangjie
public func shadow(
    radius!: Int64,
    color!: ResourceColor = Color(0x666666),
    offsetX!: Int64 = 0,
    offsetY!: Int64 = 0
): This
```

**功能：** 为组件添加阴影效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|radius|Int64|是|\-| **命名参数。** 阴影模糊半径。<br>取值范围：[0, +∞)。<br>单位：px。<br>**说明：**<br> 设置小于0的值时，按值为0处理。|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|否|Color(0x666666)| **命名参数。** 阴影的颜色|
|offsetX|Int64|否|0| **命名参数。** 阴影的X轴偏移量。<br>单位：px。|
|offsetY|Int64|否|0| **命名参数。** 阴影的Y轴偏移量。<br>单位：px。|

## func sphericalEffect(Float64)

```cangjie
public func sphericalEffect(value: Float64): This
```

**功能：** 设置组件的图像球面化程度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float64|是|\-|设置组件的图像球面化程度。<br> 取值范围：[0,1]。<br> **说明：** <br> 1. 如果value等于0则图像保持原样，如果value等于1则图像为完全球面化效果。在0和1之间，数值越大，则球面化程度越高。value < 0 或者 value > 1为异常情况，value < 0按0处理，value > 1按1处理。 <br> 2. 组件阴影和外描边不支持球面效果。<br> 3. 设置value大于0时，组件冻屏不更新并且把组件内容绘制到透明离屏buffer上，如果要更新组件属性则需要把value设置为0。|