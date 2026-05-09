### var borderWidth

```cangjie
public var borderWidth: ?Length
```

**功能：** 设置弹窗背板的边框宽度。初始值：0.vp

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var cancel

```cangjie
public var cancel: ?VoidCallback
```

**功能：** 返回、ESC键和点击遮障层弹窗退出时的回调。初始值： { => }

**类型：** ?[VoidCallback](./cj-common-types.md#type-voidcallback)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var closeAnimation

```cangjie
public var closeAnimation: ?AnimateParam
```

**功能：** 自定义设置弹窗关闭的动画效果相关参数。

**类型：** ?[AnimateParam](./cj-common-types.md#class-animateparam)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var cornerRadius

```cangjie
public var cornerRadius: ?Length
```

**功能：** 设置背板的圆角半径。初始值：32.vp

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var customStyle

```cangjie
public var customStyle: ?Bool
```

**功能：** 弹窗容器样式是否自定义。初始值：false

**类型：** ?Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var gridCount

```cangjie
public var gridCount: ?UInt32
```

**功能：** 弹窗宽度占栅格宽度的个数。

**类型：** ?UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var height

```cangjie
public var height: ?Length
```

**功能：** 设置弹窗背板的高度。

**类型：** ?[Length](./cj-common-types.md#interface-length)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var isModal

```cangjie
public var isModal: ?Bool
```

**功能：** 弹窗是否为模态窗口，模态窗口有蒙层，非模态窗口无蒙层。初始值：true

**类型：** ?Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var maskColor

```cangjie
public var maskColor: ?ResourceColor
```

**功能：** 自定义蒙层颜色。初始值：Color(0x33000000)

**类型：** ?[ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var maskRect

```cangjie
public var maskRect: ?Rectangle
```

**功能：** 弹窗遮蔽层区域，在遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。初始值：Rectangle()

**类型：** ?[Rectangle](./cj-common-types.md#class-rectangle)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var offset

```cangjie
public var offset: ?Offset
```

**功能：** 弹窗相对alignment所在位置的偏移量。初始值：Offset(0.vp, 0.vp)

**类型：** ?[Offset](./cj-common-types.md#class-offset)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var onWillDismiss

```cangjie
public var onWillDismiss: ?Callback<DismissDialogAction, Unit>
```

**功能：** 交互式关闭回调函数。

**类型：** ?[Callback](./cj-common-types.md#type-callbackt-v)\<[DismissDialogAction](./cj-dialog-actionsheet.md#class-dismissdialogaction),Unit>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var openAnimation

```cangjie
public var openAnimation: ?AnimateParam
```

**功能：** 自定义设置弹窗弹出的动画效果相关参数。

**类型：** ?[AnimateParam](./cj-common-types.md#class-animateparam)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22