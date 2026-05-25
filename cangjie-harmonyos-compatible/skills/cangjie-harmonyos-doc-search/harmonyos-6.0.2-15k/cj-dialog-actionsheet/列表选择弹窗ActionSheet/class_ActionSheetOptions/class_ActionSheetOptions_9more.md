## class ActionSheetOptions

```cangjie
public class ActionSheetOptions {
    public ActionSheetOptions(
        public var title: String,
        public var message: String,
        public var sheets: Array<SheetInfo>,
        public var subtitle!: Option<String> = Option.None,
        public var confirm!: Option<Confirm> = Option.None,
        public var autoCancel!: Option<Bool> = true,
        public var cancel!: Option<() -> Unit> = Option.None,
        public var alignment!: Option<DialogAlignment> = DialogAlignment.Bottom,
        public var offset!: Option<Offset> = Option.None,
        public var maskRect!: Option<Rectangle> = Rectangle(x: Length(0), y: Length(0),
            width: Length(100, unitType: LengthType.percent), height: Length(100, unitType: LengthType.percent)),
        public var showInSubWindow!: Option<Bool> = false,
        public var isModal!: Option<Bool> = true,
        public var backgroundColor!: Option<Color> = Color.TRANSPARENT,
        public var backgroundBlurStyle!: Option<BlurStyle> = BlurStyle.COMPONENT_ULTRA_THICK,
        public var onWillDismiss!: Option<(DismissDialogAction) -> Unit> = None,
        public var cornerRadius!: Option<BorderRadiuses> = BorderRadiuses(topLeft: 32.vp, topRight: 32.vp,
            bottomLeft: 32.vp, bottomRight: 32.vp),
        public var borderWidth!: Option<BorderWidth> = BorderWidth(0.vp, 0.vp, 0.vp, 0.vp),
        public var borderColor!: Option<Color> = Color.BLACK,
        public var borderStyle!: Option<EdgeStyle> = EdgeStyle.SOILD,
        public var width!: Option<Length> = Option<Length>.None,
        public var height!: Option<Length> = Option<Length>.None,
        public var transition!: Option<TransitionEffect> = Option.None
    ) {}
}
```

**功能：** 列表选择弹窗的参数配置。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### var alignment

```cangjie
public var alignment: Option<DialogAlignment> = DialogAlignment.Bottom
```

**功能：** 弹窗在竖直方向上的对齐方式。

**类型：** Option\<[DialogAlignment](./cj-common-types.md#enum-dialogalignment)>

**读写能力：** 可读写

**起始版本：** 19

### var autoCancel

```cangjie
public var autoCancel: Option<Bool> = true
```

**功能：** 点击遮障层时，是否关闭弹窗。

**类型：** Option\<Bool>

**读写能力：** 可读写

**起始版本：** 19

### var backgroundBlurStyle

```cangjie
public var backgroundBlurStyle: Option<BlurStyle> = BlurStyle.COMPONENT_ULTRA_THICK
```

**功能：** 弹窗背板模糊材质。

**类型：** Option\<[BlurStyle](./cj-universal-attribute-background.md#enum-blurstyle)>

**读写能力：** 可读写

**起始版本：** 19

### var backgroundColor

```cangjie
public var backgroundColor: Option<Color> = Color.TRANSPARENT
```

**功能：** 弹窗背板颜色。

**类型：** Option\<[Color](./cj-common-types.md#class-color)>

**读写能力：** 可读写

**起始版本：** 19

### var borderColor

```cangjie
public var borderColor: Option<Color> = Color.BLACK
```

**功能：** 设置弹窗背板的边框颜色。如果使用borderColor属性，需要和borderWidth属性一起使用。

**类型：** Option\<[Color](./cj-common-types.md#class-color)>

**读写能力：** 可读写

**起始版本：** 19

### var borderStyle

```cangjie
public var borderStyle: Option<EdgeStyle> = EdgeStyle.SOILD
```

**功能：** 设置弹窗背板的边框样式。如果使用borderStyle属性，需要和borderWidth属性一起使用。

**类型：** Option\<[EdgeStyle](cj-dialog-actionsheet.md#class-edgestyle)>

**读写能力：** 可读写

**起始版本：** 19

### var borderWidth

```cangjie
public var borderWidth: Option<Length> = 0.vp
```

**功能：** 设置弹窗背板的边框宽度。

**类型：** Option\<[Length](./cj-common-types.md#interface-length)>

**读写能力：** 可读写

**起始版本：** 19

### var cancel

```cangjie
public var cancel: Option<() -> Unit> = Option.None
```

**功能：** 点击遮障层关闭dialog时的回调。

**类型：** Option\<()->Unit>

**读写能力：** 可读写

**起始版本：** 19