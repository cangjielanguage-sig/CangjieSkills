## func renderGroup(Bool)

```cangjie
public func renderGroup(value: Bool): This
```

**功能：** 设置当前控件和子控件是否先整体离屏渲染绘制后再与父控件融合绘制。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|\-|当前控件和子控件是否先整体离屏渲染绘制后再与父控件融合绘制。当前控件的不透明度不为1时绘制效果可能有差异。<br>初始值：false。|

## func pixelStretchEffect(Length, Length, Length, Length)

```cangjie
public func pixelStretchEffect(top!: Length = 0.vp, right!: Length = 0.vp, bottom!: Length = 0.vp,
    left!: Length = 0.vp): This
```

**功能：** 设置组件的图像边缘像素扩展距离。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

> **说明：**
>
> - 如果距离为正值，表示向外扩展，放大原来图像大小。上下左右四个方向分别用边缘像素填充，填充的距离即为设置的边缘扩展的距离。
> - 如果距离为负值，表示内缩，但是最终图像大小不变。<br> 内缩方式：<br> 图像根据参数的设置缩小，缩小大小为四个方向边缘扩展距离的绝对值。图像用边缘像素扩展到原来大小。
> - 对参数的输入约束：上下左右四个方向的扩展统一为非正值或者非负值。即四个边同时向外扩或者内缩，方向一致。<br> 所有方向的输入均为百分比或者具体值，不支持百分比和具体值混用。<br> 所有异常情况下，显示为{0，0，0，0}效果，即跟原图保持一致。

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|top|[Length](./cj-common-types.md#interface-length)|否|0.vp| **命名参数。** 组件图像上边沿像素扩展距离。|
|right|[Length](./cj-common-types.md#interface-length)|否|0.vp| **命名参数。** 组件图像右边沿像素扩展距离。|
|bottom|[Length](./cj-common-types.md#interface-length)|否|0.vp| **命名参数。** 组件图像下边沿像素扩展距离。|
|left|[Length](./cj-common-types.md#interface-length)|否|0.vp| **命名参数。** 组件图像左边沿像素扩展距离。|

## func saturate(Float64)

```cangjie
public func saturate(value: Float64): This
```

**功能：** 为组件添加饱和度效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float64|是|\-| 为当前组件添加饱和度效果，饱和度为颜色中的含色成分和消色成分(灰)的比例，入参为1时，显示原图像，大于1.0时含色成分越大，饱和度越大，小于1.0时消色成分越大，饱和度越小。<br> 初始值：1.0。 <br>推荐取值范围：[0.0, 50.0)。<br>**说明：**<br> 设置小于0.0的值时，按值为0.0处理。|

## func saturate(Int64)

```cangjie
public func saturate(value: Int64): This
```

**功能：** 为组件添加饱和度效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int64|是|\-|为当前组件添加饱和度效果，饱和度为颜色中的含色成分和消色成分(灰)的比例，入参为1时，显示原图像，大于1时含色成分越大，饱和度越大，小于1时消色成分越大，饱和度越小。<br> 初始值：1。<br>推荐取值范围：[0, 50)。<br>**说明：**<br> 设置小于0的值时，按值为0处理。|