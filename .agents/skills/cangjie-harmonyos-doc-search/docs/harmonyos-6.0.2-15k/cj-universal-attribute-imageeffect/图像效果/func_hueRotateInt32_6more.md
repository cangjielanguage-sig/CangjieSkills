## func hueRotate(Int32)

```cangjie
public func hueRotate(value: Int32): This
```

**功能：** 色相旋转效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int32|是|\-|色相旋转效果，输入参数为旋转角度。<br>初始值：0。 <br>取值范围：(-∞, +∞)。 <br>**说明：**<br>色调旋转360度会显示原始颜色。先将色调旋转 180 度，然后再旋转-180度会显示原始颜色。|

## func invert(Float64)

```cangjie
public func invert(value: Float64): This
```

**功能：** 反转输入的图像。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float64|是|\-|反转输入的图像。入参为图像反转的比例，值为1.0时完全反转，值为0.0则图像无变化。<br> 初始值：0.0。 <br>取值范围：[0.0, 1.0]。<br>**说明：**<br> 设置小于0.0的值时，按值为0.0处理。|

## func invert(Int64)

```cangjie
public func invert(value: Int64): This
```

**功能：** 反转输入的图像。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int64|是|\-|反转输入的图像。入参为图像反转的比例，值为1时完全反转，值为0则图像无变化。<br> 初始值：0。 <br>取值范围：[0, 1]。<br>**说明：**<br> 设置小于0的值时，按值为0处理。|

## func invert(Float64, Float64, Float64, Float64)

```cangjie
public func invert(low!: Float64, high!: Float64, threshold!: Float64, thresholdRange!: Float64): This
```

**功能：** 反转输入的图像。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|low|Float64|是|-| **命名参数。** 背景颜色灰度值大于阈值区间时的取值。<br> 取值范围：[0,1]。|
|high|Float64|是|-| **命名参数。** 背景颜色灰度值小于阈值区间时的取值。<br> 取值范围：[0,1]。|
|threshold|Float64|是|-| **命名参数。** 灰度阈值。<br> 取值范围：[0,1]。|
|thresholdRange|Float64|是|-| **命名参数。** 阈值范围。<br> 取值范围：[0,1]。 <br>**说明：**<br> 灰度阈值上下偏移thresholdRange构成阈值区间，背景颜色灰度值在区间内取值由high线性渐变到low。|

## func lightUpEffect(Float64)

```cangjie
public func lightUpEffect(value: Float64): This
```

**功能：** 设置组件图像亮起程度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float64|是|\-|组件图像亮起程度。<br> 取值范围：[0,1]。<br> 如果value等于0则图像为全黑，如果value等于1则图像为全亮效果。0到1之间数值越大，表示图像亮度越高。value < 0 或者 value > 1为异常情况，value < 0按0处理，value > 1按1处理。|

## func linearGradientBlur(Float64, LinearGradientBlurOptions)

```cangjie
public func linearGradientBlur(value: Float64, options: LinearGradientBlurOptions): This
```

**功能：** 为组件添加内容线性渐变模糊效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float64|是|\-|模糊半径，模糊半径越大越模糊，为0时不模糊。<br>取值范围：\[0, 1000]。<br>线性梯度模糊包含两个部分fractionStops和direction。|
|options|[LinearGradientBlurOptions](#class-lineargradientbluroptions)|是|-|线性渐变模糊效果。|