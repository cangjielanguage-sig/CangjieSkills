#### var focusable

```cangjie
public var focusable: Bool = false
```

**功能：** 设置气泡弹出后是否获焦。默认值：false。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var followTransformOfTarget

```cangjie
public var followTransformOfTarget: Bool = false
```

**功能：** 气泡绑定的宿主组件或其宿主组件的父容器添加了旋转、缩放等变换时，气泡是否能显示在对应变化后的位置上。默认值：false。

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

#### var maskColor

```cangjie
public var maskColor: Color = Color(0x1000000)
```

**功能：** 设置气泡遮罩层颜色。

**类型：** [Color](./cj-common-types.md#class-color)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var offset

```cangjie
public var offset: Position = Position(0.0, 0.0)
```

**功能：** 设置popup组件相对于placement设置的显示位置的偏移。不支持设置百分比。

**类型：** [Position](./cj-common-types.md#class-position)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var onStateChange

```cangjie
public var onStateChange: Option<(StateChangeEvent) -> Unit> = Option.None
```

**功能：** 设置弹窗状态变化事件回调，参数为弹窗当前的显示状态。

**类型：** ?[StateChangeEvent](#class-statechangeevent)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var onWillDismiss

```cangjie
public var onWillDismiss: Option<(DismissPopupAction) -> Unit> = None
```

**功能：** 设置popup交互式关闭拦截开关及拦截回调函数。

> **说明：**
>
> 在onWillDismiss回调中，不能再做onWillDismiss拦截。

**类型：** ([DismissPopupAction](#class-dismisspopupaction))->Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var placement

```cangjie
public var placement: Placement = Placement.Bottom
```

**功能：** 设置气泡组件优先显示的位置，当前位置显示不下时，会自动调整位置。默认值：Placement.Bottom。

**类型：** [Placement](./cj-common-types.md#enum-placement)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var popupColor

```cangjie
public var popupColor: Color = Color(0x1000000)
```

**功能：** 设置提示气泡的颜色。如需去除模糊背景填充效果，需将backgroundBlurStyle设置为BlurStyle.NONE。

**类型：** [Color](./cj-common-types.md#class-color)

读写能力：可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var radius

```cangjie
public var radius: Length = 20.vp
```

**功能：** 设置气泡圆角半径。默认值：20.vp。

**类型：** [Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var shadow

```cangjie
public var shadow: ShadowStyle = ShadowStyle.OUTER_DEFAULT_MD
```

**功能：** 设置气泡阴影。默认值：ShadowStyle.OUTER_DEFAULT_MD。

**类型：** [ShadowStyle](cj-common-types.md#enum-shadowstyle)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var showInSubWindow

```cangjie
public var showInSubWindow: Bool = false
```

**功能：** 设置是否在子窗口显示气泡，默认值为false，不显示。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19