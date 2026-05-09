## class CustomDialogControllerOptions

```cangjie
public class CustomDialogControllerOptions {
    public var cancel: ?VoidCallback
    public var autoCancel: ?Bool
    public var alignment: ?DialogAlignment
    public var offset: ?Offset
    public var customStyle: ?Bool
    public var gridCount: ?UInt32
    public var maskColor: ?ResourceColor
    public var maskRect: ?Rectangle
    public var openAnimation: ?AnimateParam
    public var closeAnimation: ?AnimateParam
    public var showInSubWindow: ?Bool
    public var backgroundColor: ?ResourceColor
    public var cornerRadius: ?Length
    public var isModal: ?Bool
    public var onWillDismiss: ?Callback<DismissDialogAction, Unit>
    public var width: ?Length
    public var height: ?Length
    public var borderWidth: ?Length
    public var borderColor: ?ResourceColor
    public var borderStyle: ?EdgeStyles
    public var shadow: ?ShadowOptions
    public var backgroundBlurStyle: ?BlurStyle
    public init(
        builder!: CustomView,
        cancel!: ?VoidCallback = None,
        autoCancel!: ?Bool = None,
        alignment!: ?DialogAlignment = None,
        offset!: ?Offset = None,
        customStyle!: ?Bool = None,
        gridCount!: ?UInt32 = None,
        maskColor!: ?ResourceColor = None,
        maskRect!: ?Rectangle = None,
        openAnimation!: ?AnimateParam = None,
        closeAnimation!: ?AnimateParam = None,
        showInSubWindow!: ?Bool = None,
        backgroundColor!: ?ResourceColor = None,
        cornerRadius!: ?Length = None,
        isModal!: ?Bool = None,
        onWillDismiss!: ?Callback<DismissDialogAction, Unit> = None,
        width!: ?Length = None,
        height!: ?Length = None,
        borderWidth!: ?Length = None,
        borderColor!: ?ResourceColor = None,
        borderStyle!: ?EdgeStyles = None,
        shadow!: ?ShadowOptions = None,
        backgroundBlurStyle!: ?BlurStyle = None
    )
}
```

**功能：** 声明自定义弹窗相关设置的参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var alignment

```cangjie
public var alignment: ?DialogAlignment
```

**功能：** 弹窗在竖直方向上的对齐方式。初始值：DialogAlignment.Default

**类型：** ?[DialogAlignment](./cj-common-types.md#enum-dialogalignment)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var autoCancel

```cangjie
public var autoCancel: ?Bool
```

**功能：** 是否允许点击遮障层退出。true表示关闭弹窗，false表示不关闭弹窗。初始值：true

**类型：** ?Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var backgroundBlurStyle

```cangjie
public var backgroundBlurStyle: ?BlurStyle
```

**功能：** 弹窗背板模糊材质。初始值：BlurStyle.ComponentUltraThick

**类型：** ?[BlurStyle](./cj-common-types.md#enum-blurstyle)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var backgroundColor

```cangjie
public var backgroundColor: ?ResourceColor
```

**功能：** 设置弹窗背板填充。初始值：Color.Transparent

**类型：** ?[ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var borderColor

```cangjie
public var borderColor: ?ResourceColor
```

**功能：** 设置弹窗背板的边框颜色。初始值：Color.Black

**类型：** ?[ResourceColor](./cj-common-types.md#interface-resourcecolor)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var borderStyle

```cangjie
public var borderStyle: ?EdgeStyles
```

**功能：** 设置弹窗背板的边框样式。初始值：EdgeStyles()

**类型：** ?[EdgeStyles](./cj-common-types.md#class-edgestyles)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22