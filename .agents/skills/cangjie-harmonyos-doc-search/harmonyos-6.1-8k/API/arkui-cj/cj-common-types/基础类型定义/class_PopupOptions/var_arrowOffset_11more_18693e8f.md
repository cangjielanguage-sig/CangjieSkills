### var arrowOffset

```cangjie
public var arrowOffset: ?Length
```

**功能：** 设置popup箭头在弹窗处的偏移。箭头在气泡上下方时，数值为0表示箭头居最左侧，偏移量为箭头至最左侧的距离，默认居中。箭头在气泡左右侧时，偏移量为箭头至最上侧的距离，默认居中。如果显示在屏幕边缘，气泡会自动左右偏移，数值为0时箭头始终指向绑定组件。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var showInSubWindow

```cangjie
public var showInSubWindow: ?Bool
```

**功能：** 设置是否在子窗口显示气泡，默认值为false，不显示。

**类型：** ?Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var mask

```cangjie
public var mask: ?ResourceColor
```

**功能：** 设置遮罩层的颜色。

**类型：** ?[ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var messageOptions

```cangjie
public var messageOptions: ?PopupMessageOptions
```

**功能：** 设置弹窗信息文本参数。

**类型：** ?[PopupMessageOptions](#class-popupmessageoptions)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var targetSpace

```cangjie
public var targetSpace: ?Length
```

**功能：** 设置popup与目标的间隙。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var offset

```cangjie
public var offset: ?Position
```

**功能：** 设设置popup组件相对于placement设置的显示位置的偏移。不支持设置百分比。

**类型：** ?[Position](#class-position)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var enableArrow

```cangjie
public var enableArrow: ?Bool
```

**功能：** 设置是否显示箭头。默认值：true。当页面可用空间无法让气泡完全避让时，气泡会覆盖到组件上并且不显示箭头。

**类型：** ?Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var popupColor

```cangjie
public var popupColor: ?ResourceColor
```

**功能：** 设置提示气泡的颜色。如需去除模糊背景填充效果，需将backgroundBlurStyle设置为BlurStyle.NONE。

**类型：** ?[ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var autoCancel

```cangjie
public var autoCancel: ?Bool
```

**功能：** 页面有操作时，是否自动关闭气泡。默认值：true。

**类型：** ?Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var width

```cangjie
public var width: ?Length
```

**功能：** 设置弹出窗口的宽度。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var arrowPointPosition

```cangjie
public var arrowPointPosition: Option<ArrowPointPosition>
```

**功能：** 设置气泡尖角相对于父组件显示位置，气泡尖角在垂直和水平方向上有 "Start"、"Center"、"End"三个位置点可选。以上所有位置点均位于父组件区域所在的范围内，不会超出父组件的边界范围。

**类型：** Option<[ArrowPointPosition](#enum-arrowpointposition)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22