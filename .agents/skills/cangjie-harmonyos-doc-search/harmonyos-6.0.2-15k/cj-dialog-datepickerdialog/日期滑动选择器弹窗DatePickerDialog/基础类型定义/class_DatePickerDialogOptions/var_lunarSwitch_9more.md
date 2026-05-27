#### var lunarSwitch

```cangjie
public var lunarSwitch: Bool = false
```

**功能：** 是否展示切换农历的开关，true表示展示开关，false表示不展示开关。初始值：false。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var maskRect

```cangjie
public var maskRect: ?Rectangle
```

**功能：** 弹窗遮蔽层区域，在遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。初始值：Rectangle(x: 0.vp, y: 0.vp, width: 100.percent, height: 100.percent)。

**类型：** ?[Rectangle](./cj-common-types.md#class-rectangle)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var offset

```cangjie
public var offset: ?Offset = Offset(0.vp, 0.vp)
```

**功能：** 弹窗相对alignment所在位置的偏移量。初始值：Offset(0.vp, 0.vp)。

**类型：** ?[Offset](./cj-common-types.md#class-offset)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var onCancel

```cangjie
public var onCancel: ?() -> Unit
```

**功能：** 点击弹窗中的“取消”按钮时触发该回调。

**类型：** ?()->Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var onDateAccept

```cangjie
public var onDateAccept: ?(DateTime) -> Unit
```

**功能：** 点击弹窗中的“确定”按钮时触发该回调。

> **说明：**
>
> 当showTime设置为true时，回调接口返回值value中时和分为选择器选择的时和分。否则，返回值value中时和分为系统时间的时和分。

**类型：** ?(DateTime)->Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var onDateChange

```cangjie
public var onDateChange: ?(DateTime) -> Unit
```

**功能：** 滑动弹窗中的滑动选择器使当前选中项改变时触发该回调。

> **说明：**
>
> 当showTime设置为true时，回调接口返回值value中时和分为选择器选择的时和分。否则，返回值value中时和分为系统时间的时和分。

**类型：** ?(DateTime)->Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var onDidAppear

```cangjie
public var onDidAppear: ?() -> Unit
```

**功能：** 弹窗弹出时的事件回调。

> **说明：**
>
> - 正常时序依次为：onWillAppear>>onDidAppear>>(onDateAccept/onCancel/onDateChange)>>onWillDisappear>>onDidDisappear。
> - 在onDidAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。
> - 快速点击弹出，消失弹窗时，存在onWillDisappear在onDidAppear前生效。
> - 当弹窗入场动效未完成时关闭弹窗，该回调不会触发。

**类型：** ?()->Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var onDidDisappear

```cangjie
public var onDidDisappear: ?() -> Unit
```

**功能：** 弹窗消失时的事件回调。

> **说明：**
>
> - 正常时序依次为：onWillAppear>>onDidAppear>>(onDateAccept/onCancel/onDateChange)>>onWillDisappear>>onDidDisappear。

**类型：** ?()->Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

#### var onWillAppear

```cangjie
public var onWillAppear: ?() -> Unit
```

**功能：** 弹窗显示动效前的事件回调。

> **说明：**
>
> - 正常时序依次为：onWillAppear>>onDidAppear>>(onDateAccept/onCancel/onDateChange)>>onWillDisappear>>onDidDisappear。
> - 在onWillAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。

**类型：** ?()->Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19