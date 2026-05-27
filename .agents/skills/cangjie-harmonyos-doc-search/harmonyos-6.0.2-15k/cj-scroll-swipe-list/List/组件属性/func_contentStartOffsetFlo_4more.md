### func contentStartOffset(Float64)

```cangjie
public func contentStartOffset(startOffset: Float64): This
```

**功能：** 设置内容区域起始偏移量。列表滚动到起始位置时，列表内容与列表显示区域边界保留指定距离。

contentStartOffset + contentEndOffset超过List内容区长度后contentStartOffset和contentEndOffset会置0。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|startOffset|Float64|是|-|内容区域起始偏移量。<br/>初始值：0.0。<br/>单位：vp。<br/>**说明：**<br/>设置为负数时，按初始值处理。|

### func contentStartOffset(Int64)

```cangjie
public func contentStartOffset(startOffset: Int64): This
```

**功能：** 设置内容区域起始偏移量。列表滚动到起始位置时，列表内容与列表显示区域边界保留指定距离。

contentStartOffset + contentEndOffset超过List内容区长度后contentStartOffset和contentEndOffset会置0。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|startOffset|Int64|是|-|内容区域起始偏移量。<br/>初始值：0。<br/>单位：vp。<br/>**说明：**<br/>设置为负数时，按初始值处理。|

### func divider(Length, ResourceColor, Length, Length)

```cangjie
public func divider(strokeWidth!: Length, color!: ResourceColor = Color.BLACK, startMargin!: Length = 0.vp, endMargin!: Length = 0.vp): This
```

**功能：** 用于设置ListItem分割线样式，默认无分割线。

List的分割线画在主轴方向两个子组件之间，第一个子组件上方和最后一个子组件下方不会绘制分割线。

多列模式下，ListItem与ListItem之间的分割线起始边距从每一列的交叉轴方向起始边开始计算，单列模式从List交叉轴方向起始边开始计算。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|strokeWidth|[Length](cj-common-types.md#interface-length)|是|-| **命名参数。** 分割线的线宽。<br/>**说明：**<br/>设置为负数或者大于等于List内容区长度时，按0处理。|
|color|[ResourceColor](cj-common-types.md#interface-resourcecolor)|否|Color.BLACK| **命名参数。** 分割线的颜色。|
|startMargin|[Length](cj-common-types.md#interface-length)|否|0.vp| **命名参数。** 分割线距离列表侧边起始端的距离。<br/>**说明：**<br/>设置为负数时，按初始值处理。|
|endMargin|[Length](cj-common-types.md#interface-length)|否|0.vp| **命名参数。** 分割线距离列表侧边结束端的距离。<br/>**说明：**<br/>设置为负数时，按初始值处理。|

### func edgeEffect(EdgeEffect)

```cangjie
public func edgeEffect(value: EdgeEffect): This
```

**功能：** 设置边缘滑动效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[EdgeEffect](cj-common-types.md#enum-EdgeEffect)|是|-|List组件的边缘滑动效果，支持弹簧效果和阴影效果。<br/>初始值：EdgeEffect.Spring。|