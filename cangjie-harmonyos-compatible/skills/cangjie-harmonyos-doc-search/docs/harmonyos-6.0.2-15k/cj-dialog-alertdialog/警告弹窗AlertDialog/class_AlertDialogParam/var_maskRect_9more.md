### var maskRect

```cangjie
public var maskRect: Option<Rectangle> = Rectangle(x: 0, y: 0, width: 100.percent, height: 100.percent)
```

**功能:** 弹窗遮蔽层区域，在遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。

**类型:** Option\<[Rectangle](./cj-common-types.md#class-rectangle)>

**读写能力:** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var message

```cangjie
public var message: String = ""
```

**功能:** 弹窗内容。

**类型:** String

**读写能力:** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var offset

```cangjie
public var offset: Option<Offset> = Option.None
```

**功能:** 弹窗相对alignment所在位置的偏移量。

**类型:** Option\<[Offset](./cj-common-types.md#class-offset)>

**读写能力:** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var onWillDismiss

```cangjie
public var onWillDismiss: Option<(DismissDialogAction) -> Unit> = None
```

**功能:** 交互式关闭回调函数。

**类型:** Option\<( [DismissDialogAction](cj-dialog-actionsheet.md#class-dismissdialogaction) ) -> Unit>

**读写能力:** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### var showInSubWindow

```cangjie
public var showInSubWindow: Option<Bool> = false
```

**功能:** 某弹框需要显示在主窗口之外时，是否在子窗口显示此弹窗。

**类型:** Option\<Bool>

**读写能力:** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var subtitle

```cangjie
public var subtitle: Option<String> = Option.None
```

**功能:** 弹窗副标题。

**类型:** Option\<String>

**读写能力:** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var textStyle

```cangjie
public var textStyle: Option<WordBreak> = WordBreak.Normal
```

**功能：** 设置弹窗message内容的文本样式。

**类型：** Option\<[WordBreak](./cj-common-types.md#enum-wordbreak)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### var title

```cangjie
public var title: Option<String> = Option.None
```

**功能：** 弹窗标题。

**类型：** Option\<String>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### var transition

```cangjie
public var transition: Option<TransitionEffect> = Option.None
```

**功能：** 设置弹窗显示和退出的过渡效果。

**类型：** Option\<[TransitionEffect](./cj-animation-transition.md#class-transitioneffect)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19