## class ActionSheetOptions

```cangjie
public class ActionSheetOptions {
    public var title: ?ResourceStr
    public var subtitle: ?ResourceStr
    public var message: ?ResourceStr
    public var confirm: ?ActionSheetButtonOptions
    public var cancel: ?VoidCallback
    public var sheets: ?Array<SheetInfo>
    public var autoCancel: ?Bool
    public var alignment: ?DialogAlignment
    public var offset: ?ActionSheetOffset
    public var maskRect: ?Rectangle
    public var showInSubWindow: ?Bool
    public var isModal: ?Bool
    public var backgroundColor: ?ResourceColor
    public var backgroundBlurStyle: ?BlurStyle
    public var onWillDismiss: ?Callback<DismissDialogAction, Unit>
    public var transition: ?TransitionEffect
    public var cornerRadius: ?BorderRadiuses
    public var width: ?Length
    public var height: ?Length
    public var borderWidth: ?Length
    public var borderColor: ?ResourceColor
    public var borderStyle: ?EdgeStyles
    public var shadow: ?ShadowOptions
    public init(
        title!: ?ResourceStr,
        subtitle!: ?ResourceStr = None,
        message!: ?ResourceStr,
        confirm!: ?ActionSheetButtonOptions = None,
        cancel!: ?VoidCallback = None,
        sheets!: ?Array<SheetInfo>,
        autoCancel!: ?Bool = None,
        alignment!: ?DialogAlignment = None,
        offset!: ?ActionSheetOffset = None,
        maskRect!: ?Rectangle = None,
        showInSubWindow!: ?Bool = None,
        isModal!: ?Bool = None,
        backgroundColor!: ?ResourceColor = None,
        backgroundBlurStyle!: ?BlurStyle = None,
        onWillDismiss!: ?Callback<DismissDialogAction, Unit> = None,
        transition!: ?TransitionEffect = None,
        cornerRadius!: ?BorderRadiuses = None,
        width!: ?Length = None,
        height!: ?Length = None,
        borderWidth!: ?Length = None,
        borderColor!: ?ResourceColor = None,
        borderStyle!: ?EdgeStyles = None,
        shadow!: ?ShadowOptions = None
    )
}
```

**功能：** ActionSheet弹窗的配置选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var title

```cangjie
public var title: ?ResourceStr
```

**功能：** 弹窗标题。

**类型：** ?[ResourceStr](./cj-common-types.md#interface-resourcestr)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var subtitle

```cangjie
public var subtitle: ?ResourceStr
```

**功能：** 弹窗副标题。

**类型：** ?[ResourceStr](./cj-common-types.md#interface-resourcestr)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var message

```cangjie
public var message: ?ResourceStr
```

**功能：** 弹窗内容。

**类型：** ?[ResourceStr](./cj-common-types.md#interface-resourcestr)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var confirm

```cangjie
public var confirm: ?ActionSheetButtonOptions
```

**功能：** 确认Button的使能状态、默认焦点、按钮风格、文本内容和点击回调。在弹窗获焦且未进行tab键走焦时，该按钮默认响应Enter键，且多重弹窗可自动获焦连续响应。

**类型：** ?[ActionSheetButtonOptions](#class-actionsheetbuttonoptions)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var cancel

```cangjie
public var cancel: ?VoidCallback
```

**功能：** 点击遮障层关闭dialog时的回调。

**类型：** ?[VoidCallback](./cj-common-types.md#type-voidcallback)

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22

### var sheets

```cangjie
public var sheets: ?Array<SheetInfo>
```

**功能：** 设置选项内容，每个选择项支持设置图片、文本和选中的回调。

**类型：** ?Array\<[SheetInfo](#class-sheetinfo)>

**读写能力：** 可读写

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 22