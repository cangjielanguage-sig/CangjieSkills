### func blockStyle(SliderBlockType, String, ?ShapeAbstract)

```cangjie
public func blockStyle(`type`: SliderBlockType, image!: String = "", shape!: ?ShapeAbstract = None): This
```

**功能：** 设置滑块形状参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|type|[SliderBlockType](#enum-sliderblocktype)|是|-|滑块形状参数。<br/>初始值：<br/>SliderBlockType.DEFAULT，使用圆形滑块。|
|image|String|否|""| **命名参数。** 设置滑块图片资源。图片显示区域大小由blockSize属性控制，请勿输入尺寸过大的图片。|
|shape|?[ShapeAbstract](./cj-graphic-drawing-shape.md#class-shapeabtract)|否|None| **命名参数。** 设置滑块使用的自定义形状。包含[Circle](./cj-graphic-drawing-circle.md)、[Ellipse](./cj-graphic-drawing-ellipse.md)、[Path](./cj-graphic-drawing-path.md)、[Rect](./cj-graphic-drawing-rect.md)。|

### func blockStyle(SliderBlockType, AppResource, ?ShapeAbstract)

```cangjie
public func blockStyle(`type`: SliderBlockType, image!: AppResource, shape!: ?ShapeAbstract = None): This
```

**功能：** 设置滑块形状参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|type|[SliderBlockType](#enum-sliderblocktype)|是|-|滑块形状参数。<br/>初始值：<br/>SliderBlockType.DEFAULT，使用圆形滑块。|
|image|[AppResource](../apis/LocalizationKit/cj-apis-resource_manager.md#class-appresource)|是|-| **命名参数。** 设置滑块图片资源。图片显示区域大小由blockSize属性控制，请勿输入尺寸过大的图片。|
|shape|?[ShapeAbstract](./cj-graphic-drawing-shape.md#class-shapeabtract)|否|None| **命名参数。** 设置滑块使用的自定义形状。包含[Circle](./cj-graphic-drawing-circle.md)、[Ellipse](./cj-graphic-drawing-ellipse.md)、[Path](./cj-graphic-drawing-path.md)、[Rect](./cj-graphic-drawing-rect.md)。|

### func maxLabel(Float64) <sup>(deprecated)</sup>

```cangjie
public func maxLabel(value: Float64): This
```

**功能：** 根据指定的浮点值设置可滑动的最大值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float64|是|-|最大值。|

### func minLabel(Float64) <sup>(deprecated)</sup>

```cangjie
public func minLabel(value: Float64): This
```

**功能：** 根据指定的浮点值设置可滑动的最小值。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float64|是|-|最小值。|

### func minResponsiveDistance(Float32)

```cangjie
public func minResponsiveDistance(value: Float32): This
```

**功能：** 设置滑动响应的最小距离。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float32|是|-|设置滑动响应的最小距离，滑动超过此距离后才响应使滑块滑动。<br/>**说明**：<br/>单位与参数min和max一致。<br/>当value小于0、大于MAX-MIN或非法值时，取初始值。<br/>初始值：0。|