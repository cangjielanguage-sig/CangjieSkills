### var isModal

```cangjie
public var isModal: Option<Bool>
```

**功能：** 弹窗是否为模态窗口，模态窗口有蒙层，非模态窗口无蒙层。

**类型：** Option\<Bool>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### var maskColor

```cangjie
public var maskColor: ResourceColor
```

**功能：** 自定义蒙层颜色。

**类型：** [ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var maskRect

```cangjie
public var maskRect: Rectangle
```

**功能：** 弹窗遮蔽层区域，在遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。

**类型：** [Rectangle](./cj-common-types.md#class-rectangle)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var offset

```cangjie
public var offset: Offset
```

**功能：** 弹窗相对alignment所在位置的偏移量。

**类型：** [Offset](./cj-common-types.md#class-offset)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var onWillDismiss

```cangjie
public var onWillDismiss: Option <(DismissDialogAction) -> Unit>
```

**功能：** 交互式关闭回调函数。

**类型：** Option\<([DismissDialogAction](cj-dialog-actionsheet.md#class-dismissdialogaction))->Unit>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### var openAnimation

```cangjie
public var openAnimation: Option<AnimateParam>
```

**功能：** 自定义设置弹窗弹出的动画效果相关参数。

**类型：** Option\<[AnimateParam](./cj-common-types.md#class-animateparam)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var shadow

```cangjie
public var shadow: Option<ShadowOptions>
```

**功能：** 设置弹窗背板的阴影。

**类型：** Option\<[ShadowOptions](./cj-text-input-text.md#class-shadowoptions)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### var showInSubWindow

```cangjie
public var showInSubWindow: Bool
```

**功能：** 某弹框需要显示在主窗口之外时，是否在子窗口显示此弹窗。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var width

```cangjie
public var width: Option<Length>
```

**功能：** 设置弹窗背板的宽度。

**类型：** Option\<[Length](./cj-common-types.md#interface-length)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19