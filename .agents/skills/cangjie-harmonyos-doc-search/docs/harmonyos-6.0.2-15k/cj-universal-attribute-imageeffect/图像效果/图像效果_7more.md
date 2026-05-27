# 图像效果

设置组件的模糊、阴影、球面效果以及设置图片的图像效果。

## func blendMode(BlendMode, BlendApplyType)

```cangjie
public open func blendMode(value: BlendMode, `type`: BlendApplyType): This
```

**功能：** 将当前控件的内容（包含子节点内容）与下方画布（可能为离屏画布）已有内容进行混合。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[BlendMode](./cj-common-types.md#enum-blendmode)|是|\-|混合模式。<br> 初始值：BlendMode.NONE。<br> **说明：** <br>混合模式设置为BlendMode.NONE时，blend效果实际为默认的BlendMode.SRC_OVER，且BlendApplyType不生效。|
|\`type\`|[BlendApplyType](./cj-common-types.md#enum-blendapplytype)|是|\-|blendMode实现方式是否离屏。<br> **说明：** <br> 1. 设置BlendApplyType.FAST时，不离屏。<br>2. 设置BlendApplyType.OFFSCREEN时，会创建当前组件大小的离屏画布，再将当前组件（含子组件）的内容绘制到离屏画布上，再用指定的混合模式与下方画布已有内容进行混合。使用该实现方式时，将导致[linearGradientBlur](#func-lineargradientblurfloat64-lineargradientbluroptions)，[backgroundEffect](./cj-universal-attribute-background.md#func-backgroundeffectbackgroundeffectoptions)，[brightness](#func-brightnessfloat64)等需要截屏的接口无法截取到正确的画面。|

## func blur(Float64)

```cangjie
public func blur(value: Float64): This
```

**功能：** 为组件添加内容模糊效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float64|是|\-|为当前组件添加内容模糊效果，入参为模糊半径，模糊半径越大越模糊，为 0 时不模糊。|

## func blur(Int64)

```cangjie
public func blur(value: Int64): This
```

**功能：** 为组件添加内容模糊效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int64|是|\-|为当前组件添加背景模糊效果，入参为模糊半径，模糊半径越大越模糊，为0时不模糊。|

## func brightness(Float64)

```cangjie
public func brightness(value: Float64): This
```

**功能：** 为组件添加高光效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Float64|是|\-|为当前组件添加高光效果，入参为高光比例，值为1时没有效果，小于1.0时亮度变暗，0.0为全黑，大于1.0时亮度增加，数值越大亮度越大，亮度为2.0时会变为全白。<br> 初始值：1.0。 <br>取值范围：[0.0, 2.0]。<br>**说明：**<br> 设置小于0.0的值时，按值为0.0处理。|

## func brightness(Int64)

```cangjie
public func brightness(value: Int64): This
```

**功能：** 为组件添加高光效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Int64|是|\-|为当前组件添加高光效果，入参为高光比例，值为1时没有效果，小于1时亮度变暗，0为全黑，大于1时亮度增加，数值越大亮度越大，亮度为2时会变为全白。<br> 初始值：1。 <br>取值范围：[0, 2]。<br>**说明：**<br> 设置小于0的值时，按值为0处理。|

## func colorBlend(ResourceColor)

```cangjie
public func colorBlend(color: ResourceColor): This
```

**功能：** 为组件添加颜色叠加效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|为当前组件添加颜色叠加效果，入参为叠加的颜色。|