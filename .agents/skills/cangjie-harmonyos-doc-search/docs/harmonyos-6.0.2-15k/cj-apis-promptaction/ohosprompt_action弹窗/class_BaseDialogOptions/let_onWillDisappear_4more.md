### let onWillDisappear

```cangjie
public let onWillDisappear: () -> Unit = {=>}
```

**功能：** 表示弹窗退出动效前的事件回调。

**类型：** () -> Unit

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let keyboardAvoidMode

```cangjie
public let keyboardAvoidMode: KeyboardAvoidMode = KeyboardAvoidMode.DEFAULT
```

**功能：** 表示用于设置弹窗是否在拉起软键盘时进行自动避让。

**类型：** [KeyboardAvoidMode](#enum-keyboardavoidmode)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let enableHoverMode

```cangjie
public let enableHoverMode: Bool = false
```

**功能：** 表示是否响应悬停态。

**类型：** Bool

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let hoverModeArea

```cangjie
public let hoverModeArea: HoverModeAreaType = HoverModeAreaType.BOTTOM_SCREEN
```

**功能：** 表示悬停态下弹窗默认展示区域。

**类型：** [HoverModeAreaType](#enum-hovermodeareatype)

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19