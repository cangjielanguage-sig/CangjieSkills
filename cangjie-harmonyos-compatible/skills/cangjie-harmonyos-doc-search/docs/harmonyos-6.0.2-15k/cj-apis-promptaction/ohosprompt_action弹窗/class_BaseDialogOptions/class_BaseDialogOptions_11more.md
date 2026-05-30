## class BaseDialogOptions

```cangjie
public open class BaseDialogOptions {
    public let maskRect: Rectangle = Rectangle(x: 0.vp, y: 0.vp, width: 100.percent, height: 100.percent),
    public let alignment: DialogAlignment = DialogAlignment.Default,
    public let offset: Offset = Offset(0.vp, 0.vp),
    public let isModal: Bool = true,
    public let showInSubWindow: Bool = false,
    public let maskColor: Color = Color(0x33000000),
    public let transition: TransitionEffect = TransitionEffect.OPACITY,
    public let onDidAppear: () -> Unit = { => },
    public let onDidDisappear: () -> Unit = { => },
    public let onWillAppear: () -> Unit = { => },
    public let onWillDisappear: () -> Unit = { => },
    public let keyboardAvoidMode: KeyboardAvoidMode = KeyboardAvoidMode.DEFAULT,
    public let enableHoverMode: Bool = false,
    public let hoverModeArea: HoverModeAreaType = HoverModeAreaType.BOTTOM_SCREEN
}
```

**功能：** 弹窗的选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### let maskRect

```cangjie
public let maskRect: Rectangle = Rectangle(x: 0.vp, y: 0.vp, width: 100.percent, height: 100.percent)
```

**功能：** 表示弹窗遮蔽层区域。

**类型：** [Rectangle](./cj-common-types.md#class-rectangle)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### let alignment

```cangjie
public let alignment: DialogAlignment = DialogAlignment.Default
```

**功能：** 表示弹窗在竖直方向上的对齐方式。

**类型：** [DialogAlignment](./cj-common-types.md#enum-dialogalignment)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### let offset

```cangjie
public let offset: Offset = Offset(0.vp, 0.vp)
```

**功能：** 表示弹窗相对alignment所在位置的偏移量。

**类型：** [offset](./cj-common-types.md#class-offset)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### let isModal

```cangjie
public let isModal: Bool = true
```

**功能：** 表示弹窗是否为模态窗口。

**类型：** Bool

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### let showInSubWindow

```cangjie
public let showInSubWindow: Bool = false
```

**功能：** 表示弹框需要显示在主窗口之外时，是否在子窗口显示此弹窗。

**类型：** Bool

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### let maskColor

```cangjie
public let maskColor: Color = Color(0x33000000)
```

**功能：** 表示自定义蒙层颜色。

**类型：** [Color](./cj-common-types.md#class-color)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let transition

```cangjie
public let transition: TransitionEffect = TransitionEffect.OPACITY
```

**功能：** 表示弹窗显示和退出的过渡效果。

**类型：** [TransitionEffect](./cj-animation-transition.md#class-transitioneffect)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let onDidAppear

```cangjie
public let onDidAppear: () -> Unit = {=>}
```

**功能：** 表示弹窗弹出时的事件回调。

**类型：** () -> Unit

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let onDidDisappear

```cangjie
public let onDidDisappear: () -> Unit = {=>}
```

**功能：** 表示弹窗消失时的事件回调。

**类型：** () -> Unit

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let onWillAppear

```cangjie
public let onWillAppear: () -> Unit = {=>}
```

**功能：** 表示弹窗显示动效前的事件回调。

**类型：** () -> Unit

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19