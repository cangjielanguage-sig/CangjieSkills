### BaseDialogOptions(Rectangle, DialogAlignment, Offset, Bool, Bool, Color, TransitionEffect, () -> Unit, () -> Unit, () -> Unit, () -> Unit, KeyboardAvoidMode, Bool, HoverModeAreaType)

```cangjie
public BaseDialogOptions(
    public let maskRect!: Rectangle = Rectangle(x: 0.vp, y: 0.vp, width: 100.percent, height: 100.percent),
    public let alignment!: DialogAlignment = DialogAlignment.Default,
    public let offset!: Offset = Offset(0.vp, 0.vp),
    public let isModal!: Bool = true,
    public let showInSubWindow!: Bool = false
    public let maskColor!: Color = Color(0x33000000),
    public let transition!: TransitionEffect = TransitionEffect.OPACITY,
    public let onDidAppear!: () -> Unit = { => },
    public let onDidDisappear!: () -> Unit = { => },
    public let onWillAppear!: () -> Unit = { => },
    public let onWillDisappear!: () -> Unit = { => },
    public let keyboardAvoidMode!: KeyboardAvoidMode = KeyboardAvoidMode.DEFAULT,
    public let enableHoverMode!: Bool = false,
    public let hoverModeArea!: HoverModeAreaType = HoverModeAreaType.BOTTOM_SCREEN
)
```

**功能：** 构造一个BaseDialogOptions类型的对象。

**参数：**