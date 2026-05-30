#### var messageOptions

```cangjie
public var messageOptions: PopupMessageOptions = PopupMessageOptions()
```

**功能：** 设置弹窗信息文本参数。

**类型：** [PopupMessageOptions](#struct-popupmessageoptions)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

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

**类型：** ?([StateChangeEvent](#class-statechangeevent))->Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var onWillDismiss

```cangjie
public var onWillDismiss: Option<(DismissPopupAction) -> Unit> = None
```

**功能：** 设置拦截退出事件且执行回调函数。

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

**功能：** 设置popup组件相对于目标的显示位置，默认值为Placement.Bottom。如果同时设置了placementOnTop和placement，则以placement的设置生效。

**类型：** [Placement](./cj-common-types.md#enum-placement)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var placementOnTop<sup>(deprecated)</sup>

```cangjie
public var placementOnTop: Bool = false
```

**功能：** 设置是否在组件上方显示，默认值为false。已经废弃，建议使用placement替代。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var popupColor

```cangjie
public var popupColor: Color = Color(0x1000000)
```

**功能：** 设置提示气泡的颜色。如需去除模糊背景填充效果，需将backgroundBlurStyle设置为BlurStyle.NONE。

**类型：** [Color](./cj-common-types.md#class-color)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var primaryButton

```cangjie
public var primaryButton: Action = Action(value: "", action: {=>})
```

**功能：** 设置第一个按钮。value: 弹窗里主按钮的文本。action: 点击主按钮的回调函数。

**类型：** [Action](#class-action)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var radius

```cangjie
public var radius: Length = 20.vp
```

**功能：** 设置气泡圆角半径。默认值：20.vp。

**类型：** [Length](cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var secondaryButton

```cangjie
public var secondaryButton: Action = Action(value: "", action: {=>})
```

**功能：** 设置第二个按钮。 value: 弹窗里辅助按钮的文本。action: 点击辅助按钮的回调函数。

**类型：** [Action](#class-action)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

#### var shadows

```cangjie
public var shadow: ShadowStyle = ShadowStyle.OUTER_DEFAULT_MD
```

**功能：** 设置气泡阴影。默认值：ShadowStyle.OUTER_DEFAULT_MD。

**类型：** [ShadowStyle](cj-common-types.md#enum-shadowstyle)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19