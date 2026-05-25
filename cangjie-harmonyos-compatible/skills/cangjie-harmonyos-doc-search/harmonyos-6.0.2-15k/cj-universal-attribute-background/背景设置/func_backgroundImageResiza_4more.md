## func backgroundImageResizable(EdgeWidths)

```cangjie
public func backgroundImageResizable(slice: EdgeWidths): This
```

**功能：** 设置背景图在拉伸时可调整大小的图像选项。

设置合法的ResizableOptions时，[backgroundImage](./cj-universal-attribute-background.md#func-backgroundimageappresource-imagerepeat)属性中的repeat参数设置不生效。

当设置top+bottom大于原图的高或者left+right大于原图的宽时，ResizableOptions属性设置不生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|slice|[EdgeWidths](./cj-universal-attribute-border.md#class-edgewidths)|是|-|边框宽度类型，用于描述组件边框不同方向的宽度。<br>只有当bottom和right同时大于0时，该属性生效。默认单位：vp。|

## func backgroundBrightness(Float64, Float64)

```cangjie
public func backgroundBrightness(rate: Float64, lightUpDegree: Float64): This
```

**功能：** 设置组件背景提亮效果，包含亮度变化速率和提亮程度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rate|Float64|是|-|亮度变化速率。亮度变化速率越大，提亮程度下降速度越快。若rate为0，则lightUpDegree将不生效，即不会产生任何提亮效果。<br>初始值：0.0。<br>取值范围：[-1.0, 1.0]。|
|lightUpDegree|Float64|是|-|提亮程度。提亮程度越大，亮度提升程度越大。<br>初始值：0.0。<br>取值范围：(0.0, +∞)。|

## func backgroundEffect(BackgroundEffectOptions)

```cangjie
public func backgroundEffect(value: BackgroundEffectOptions): This
```

**功能：** 设置组件背景属性，包含背景模糊半径，亮度，饱和度，颜色等参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[BackgroundEffectOptions](./cj-universal-attribute-background.md#class-backgroundeffectoptions)|是|-|组件背景属性包括：饱和度，亮度，颜色。|

## func background(() -> Unit, Alignment)

```cangjie
public func background(builder: () -> Unit, align!: Alignment=Alignment.Center): This
```

**功能：** 设置组件背景。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|名称|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|builder|() -> Unit|是|-|自定义背景。使用时结合[@Builder](../../../Dev_Guide/arkui-cj/paradigm/cj-macro-builder.md)和[bind](./cj-ui-framework.md#func-bindcustomview---viewbuilder-customview)方法使用。|
|align|[Alignment](./cj-common-types.md#enum-alignment)|否|Alignment.Center| **命名参数。** 自定义背景与组件的对齐方式。<br>同时设置了background，backgroundColor，backgroundImage时，叠加显示，background在最上层。|