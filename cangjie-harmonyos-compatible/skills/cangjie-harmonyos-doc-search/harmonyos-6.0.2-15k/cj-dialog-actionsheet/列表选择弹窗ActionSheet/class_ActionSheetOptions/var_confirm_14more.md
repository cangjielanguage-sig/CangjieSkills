### var confirm

```cangjie
public var confirm: Option<Confirm> = Option.None
```

**功能：** 确认Button的使能状态、默认焦点、按钮风格、文本内容和点击回调。在弹窗获焦且未进行tab键走焦时，该按钮默认响应Enter键，且多重弹窗可自动获焦连续响应。

**类型：** Option\<[Confirm](cj-dialog-actionsheet.md#class-confirm)>

**读写能力：** 可读写

**起始版本：** 19

### var cornerRadius

```cangjie
public var cornerRadius: Option<BorderRadiuses> = BorderRadiuses(topLeft: 32.vp, topRight: 32.vp, bottomLeft: 32.vp,
    bottomRight: 32.vp)
```

**功能：** 设置背板的圆角半径。可分别设置4个圆角的半径。

**类型：** Option\<[BorderRadiuses](./cj-common-types.md#class-borderradiuses)>

**读写能力：** 可读写

**起始版本：** 19

### var height

```cangjie
public var height: Option<Length> = Option<Length>.None
```

**功能：** 设置弹窗背板的高度。

**类型：** Option\<[Length](./cj-common-types.md#interface-length)>

**读写能力：** 可读写

**起始版本：** 19

### var isModal

```cangjie
public var isModal: Option<Bool> = true
```

**功能：** 弹窗是否为模态窗口，模态窗口有蒙层，非模态窗口无蒙层。

**类型：** Option\<Bool>

**读写能力：** 可读写

**起始版本：** 19

### var maskRect

```cangjie
public var maskRect: Option<Rectangle> = Rectangle(x: 0, y: 0, width: 100.percent, height: 100.percent)
```

**功能：** 弹窗遮蔽层区域，在遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。

**类型：** Option\<[Rectangle](./cj-common-types.md#class-rectangle)>

**读写能力：** 可读写

**起始版本：** 19

### var message

```cangjie
public var message: String
```

**功能：** 弹窗内容。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var offset

```cangjie
public var offset: Option<Offset> = Option.None
```

**功能：** 弹窗相对alignment所在位置的偏移量。

**类型：** Option\<[Offset](./cj-common-types.md#class-offset)>

**读写能力：** 可读写

**起始版本：** 19

### var onWillDismiss

```cangjie
public var onWillDismiss: Option<(DismissDialogAction) -> Unit> = None
```

**功能：** 交互式关闭回调函数。

**类型：** Option\<([DismissDialogAction](cj-dialog-actionsheet.md#class-dismissdialogaction)) -> Unit>

**读写能力：** 可读写

**起始版本：** 19

### var sheets

```cangjie
public var sheets: Array<SheetInfo>
```

**功能：** 设置选项内容，每个选择项支持设置图片、文本和选中的回调。

**类型：** Array\<[SheetInfo](cj-dialog-actionsheet.md#class-sheetinfo)>

**读写能力：** 可读写

**起始版本：** 19

### var showInSubWindow

```cangjie
public var showInSubWindow: Option<Bool> = false
```

**功能：** 某弹框需要显示在主窗口之外时，是否在子窗口显示此弹窗。

**类型：** Option\<Bool>

**读写能力：** 可读写

**起始版本：** 19

### var subtitle

```cangjie
public var subtitle: Option<String> = Option.None
```

**功能：** 弹窗副标题。

**类型：** Option\<String>

**读写能力：** 可读写

**起始版本：** 19

### var title

```cangjie
public var title: String
```

**功能：** 弹窗标题。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var transition

```cangjie
public var transition: Option<TransitionEffect> = Option.None
```

**功能：** 设置弹窗显示和退出的过渡效果。

**类型：** Option\<[TransitionEffect](./cj-animation-transition.md#class-transitioneffect)>

**读写能力：** 可读写

**起始版本：** 19

### var width

```cangjie
public var width: Option<Length> = Option<Length>.None
```

**功能：** 设置弹窗背板的宽度。

**类型：** Option\<[Length](./cj-common-types.md#interface-length)>

**读写能力：** 可读写

**起始版本：** 19