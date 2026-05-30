#### var arrowHeight

```cangjie
public var arrowHeight: Length = 8.vp
```

**功能：** 设置箭头高度。默认值：8.vp。

**类型：** [Length](cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var arrowOffset

```cangjie
public var arrowOffset: Length = 0.vp
```

**功能：** 设置popup箭头在弹窗处的偏移。箭头在气泡上下方时，数值为0表示箭头居最左侧，偏移量为箭头至最左侧的距离，默认居中。箭头在气泡左右侧时，偏移量为箭头至最上侧的距离，默认居中。如果显示在屏幕边缘，气泡会自动左右偏移，数值为0时箭头始终指向绑定组件。

**类型：** [Length](cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var arrowPointPosition

```cangjie
public var arrowPointPosition: Option<ArrowPointPosition> = None
```

**功能：** 设置气泡尖角相对于父组件显示位置，气泡尖角在垂直和水平方向上有 "Start"、"Center"、"End"三个位置点可选。以上所有位置点均位于父组件区域所在的范围内，不会超出父组件的边界范围。

**类型：** ?[ArrowPointPosition](cj-common-types.md#enum-arrowpointposition)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var arrowWidth

```cangjie
public var arrowWidth: Length = 16.vp
```

**功能：** 设置箭头宽度。若所设置的箭头宽度超过所在边的长度减去两倍的气泡圆角大小，则不绘制气泡箭头。默认值：16.vp。

**类型：** [Length](cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var autoCancel

```cangjie
public var autoCancel: Bool = true
```

**功能：** 页面有操作时，设置是否自动关闭气泡。默认值：true。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var backgroundBlurStyle

```cangjie
public var backgroundBlurStyle: BlurStyle = BlurStyle.COMPONENT_ULTRA_THICK
```

**功能：** 设置气泡模糊背景参数。默认值：BlurStyle.COMPONENT_ULTRA_THICK。

**类型：** [BlurStyle](./cj-universal-attribute-background.md#enum-blurstyle)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var enableArrow

```cangjie
public var enableArrow: Bool = true
```

**功能：** 设置是否显示箭头。默认值：true。当页面可用空间无法让气泡完全避让时，气泡会覆盖到组件上并且不显示箭头。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var followTransformOfTarget

```cangjie
public var followTransformOfTarget: Bool = false
```

**功能：** 气泡绑定的宿主组件或其宿主组件的父容器添加了旋转、缩放等变换时，设置气泡是否能显示在对应变化后的位置上。默认值：false。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var mask

```cangjie
public var mask: Color = Color(0x1000000)
```

**功能：** 设置遮罩层的颜色。

**类型：** [Color](./cj-common-types.md#class-color)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var message

```cangjie
public var message: String
```

**功能：** 设置弹窗信息内容。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12